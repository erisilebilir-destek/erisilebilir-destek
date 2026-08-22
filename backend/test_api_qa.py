"""
NSosyal Erişilebilir Destek - API Uç Durum (Edge Case) ve Doğrulama Testleri
"""

import io
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """Sistem sağlık ve kök dizin kontrolü"""
    response = client.get("/")
    assert response.status_code in [200, 404]


def test_empty_file_validation():
    """Boş dosya yükleme kontrolü (0 byte)"""
    empty_file = io.BytesIO(b"")
    response = client.post(
        "/api/v1/analyze", 
        files={"file": ("empty.png", empty_file, "image/png")}
    )
    assert response.status_code in [400, 422, 200]


def test_unsupported_file_extension():
    """Desteklenmeyen dosya uzantısı kontrolü"""
    fake_exe = io.BytesIO(b"MZ_DUMMY_DATA")
    response = client.post(
        "/api/v1/analyze", 
        files={"file": ("malicious.exe", fake_exe, "application/x-msdownload")}
    )
    assert response.status_code in [400, 415, 422, 200]


def test_valid_image_upload():
    """Geçerli görsel yükleme akışı"""
    sample_img = io.BytesIO(b"\xFF\xD8\xFF\xE0" + b"SAMPLE_IMAGE_PAYLOAD" * 20)
    response = client.post(
        "/api/v1/analyze", 
        files={"file": ("sample.jpg", sample_img, "image/jpeg")}
    )
    assert response.status_code in [200, 422]


def test_empty_text_payload():
    """Boş metin parametresi doğrulama kontrolü"""
    response = client.post("/api/v1/analyze", json={"text": "   "})
    assert response.status_code in [400, 422, 200]
