"""
NSosyal Erişilebilir Destek - API Uç Durum (Edge Case) ve Doğrulama Testleri

Testler geçici bir SQLite veritabanı ve geçici bir yükleme klasörü kullanır;
böylece geliştirme veritabanı (nsosyal.db) ve uploads/ klasörü kirlenmez.

Çalıştırmak için:  pytest -q
"""

import io
import os
import tempfile

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.database import Base, get_db
from app.main import app

# API'nin beklediği form alanı adı (app/routers/analyze.py). Yanlış ad 422 döndürür.
DOSYA_ALANI = "dosya"


@pytest.fixture(scope="module")
def yukleme_dizini():
    """Testlerin dosya yazdığı geçici klasör."""
    with tempfile.TemporaryDirectory(prefix="nsosyal_test_") as dizin:
        eski = settings.UPLOAD_DIR
        settings.UPLOAD_DIR = dizin
        yield dizin
        settings.UPLOAD_DIR = eski


@pytest.fixture(scope="module")
def client(yukleme_dizini):
    """Geçici veritabanına bağlı test istemcisi."""
    db_yolu = os.path.join(yukleme_dizini, "test.db")
    engine = create_engine(f"sqlite:///{db_yolu}", connect_args={"check_same_thread": False})
    TestSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    Base.metadata.create_all(bind=engine)

    def test_db():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = test_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def _gorsel(ad="ornek.jpg"):
    return {DOSYA_ALANI: (ad, io.BytesIO(b"\xFF\xD8\xFF\xE0" + b"ORNEK_GORSEL" * 20), "image/jpeg")}


# ---------- Sağlık ----------

def test_health_check(client):
    """Sistem sağlık ve kök dizin kontrolü"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["durum"] == "calisiyor"


# ---------- Girdi doğrulama ----------

def test_missing_file_field(client):
    """Form alanı adı 'dosya' olmalı; eksik/yanlış alan 422 döndürür."""
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("yanlis_alan.jpg", io.BytesIO(b"veri"), "image/jpeg")},
    )
    assert response.status_code == 422


def test_empty_file_validation(client):
    """Boş dosya yükleme kontrolü (0 byte)"""
    response = client.post(
        "/api/v1/analyze",
        files={DOSYA_ALANI: ("empty.png", io.BytesIO(b""), "image/png")},
    )
    assert response.status_code == 400
    assert "boş" in response.json()["detail"].lower()


def test_unsupported_file_extension(client):
    """Desteklenmeyen dosya türü kontrolü"""
    response = client.post(
        "/api/v1/analyze",
        files={DOSYA_ALANI: ("malicious.exe", io.BytesIO(b"MZ_DUMMY_DATA"), "application/x-msdownload")},
    )
    assert response.status_code == 415


def test_file_size_limit(client, monkeypatch):
    """Boyut sınırı aşıldığında 413 döner."""
    monkeypatch.setattr(settings, "MAKS_BOYUT_MB", 0)
    response = client.post("/api/v1/analyze", files=_gorsel())
    assert response.status_code == 413


# ---------- Analiz akışı ----------

def test_valid_image_upload(client):
    """Geçerli görsel yükleme akışı"""
    response = client.post("/api/v1/analyze", files=_gorsel())
    assert response.status_code == 200
    veri = response.json()
    assert veri["islem_turu"] == "gorsel"
    assert veri["modul"] == "gorsel_aciklama"
    assert veri["sonuc"]["otomatik_alt_text"]
    assert 0 <= veri["sonuc"]["genel_erisilebilirlik_puani"] <= 100


def test_text_upload_simplification(client):
    """Düz metin yüklendiğinde sadeleştirme modülü çalışır."""
    response = client.post(
        "/api/v1/analyze",
        files={DOSYA_ALANI: ("metin.txt", io.BytesIO("Uzun ve karmaşık bir cümle.".encode("utf-8")), "text/plain")},
    )
    assert response.status_code == 200
    assert response.json()["islem_turu"] == "metin"


def test_video_upload_creates_subtitle(client):
    """Video yüklendiğinde altyazı (WebVTT) yolu üretilir."""
    response = client.post(
        "/api/v1/analyze",
        files={DOSYA_ALANI: ("video.mp4", io.BytesIO(b"\x00" * 100), "video/mp4")},
    )
    assert response.status_code == 200
    altyazi_yolu = response.json()["sonuc"]["otomatik_altyazi_yolu"]
    assert altyazi_yolu.endswith(".vtt")
    assert os.path.exists(altyazi_yolu)


def test_upload_filename_is_sanitized(client, yukleme_dizini):
    """Dizin atlatma denemesi ('../../') yükleme klasörünün dışına yazamaz."""
    response = client.post(
        "/api/v1/analyze",
        files={DOSYA_ALANI: ("../../kotucul.jpg", io.BytesIO(b"\xFF\xD8\xFF\xE0veri"), "image/jpeg")},
    )
    assert response.status_code == 200

    content_id = response.json()["content_id"]
    dosya_yolu = client.post(
        f"/api/v1/posts/{content_id}/publish",
        json={"onaylandi_mi": True},
    ).json()["dosya_yolu"]

    kok = os.path.abspath(yukleme_dizini)
    assert os.path.abspath(dosya_yolu).startswith(kok + os.sep)
    assert ".." not in dosya_yolu


def test_two_uploads_do_not_overwrite(client, yukleme_dizini):
    """Aynı adlı iki dosya birbirini ezmemeli."""
    ilk = client.post("/api/v1/analyze", files=_gorsel("ayni_ad.jpg")).json()["content_id"]
    ikinci = client.post("/api/v1/analyze", files=_gorsel("ayni_ad.jpg")).json()["content_id"]
    assert ilk != ikinci

    gonderiler = {}
    for content_id in (ilk, ikinci):
        yanit = client.post(
            f"/api/v1/posts/{content_id}/publish",
            json={"orijinal_metin": "test", "otomatik_alt_text": "test", "onaylandi_mi": True},
        )
        assert yanit.status_code == 200
        gonderiler[content_id] = yanit.json()["dosya_yolu"]

    assert gonderiler[ilk] != gonderiler[ikinci]


# ---------- Gönderi ve profil ----------

def test_publish_unknown_content(client):
    """Var olmayan içerik yayınlanamaz."""
    response = client.post("/api/v1/posts/999999/publish", json={"onaylandi_mi": True})
    assert response.status_code == 404


def test_feed_returns_published_posts(client):
    """Yayınlanan gönderi akışta görünür."""
    content_id = client.post("/api/v1/analyze", files=_gorsel()).json()["content_id"]
    client.post(
        f"/api/v1/posts/{content_id}/publish",
        json={"orijinal_metin": "Akış testi", "otomatik_alt_text": "Alternatif metin", "onaylandi_mi": True},
    )
    akis = client.get("/api/v1/posts")
    assert akis.status_code == 200
    assert any(gonderi["id"] == content_id for gonderi in akis.json())


def test_unknown_user_score(client):
    """Var olmayan kullanıcı için 404 döner."""
    response = client.get("/api/v1/users/olmayan_kullanici/score")
    assert response.status_code == 404
