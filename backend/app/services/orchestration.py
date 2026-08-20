"""
Orkestrasyon Servisi — gelen isteği türüne göre ilgili yapay zeka modülüne
yönlendirir, sonuçları ve erişilebilirlik puanlarını birleştirir ve veritabanına
kaydeder. /api/v1/analyze bu servisi kullanır.
"""

import os
from typing import Optional

from sqlalchemy.orm import Session

from ..config import settings
from ..models import AnalysisResult, Content
from . import (
    alt_text_service,
    readability_service,
    simplification_service,
    subtitle_service,
)

GORSEL_TURLERI = {"image/png", "image/jpeg", "image/jpg", "image/webp"}
VIDEO_TURLERI = {"video/mp4", "video/webm", "video/quicktime"}
METIN_TURLERI = {"text/plain"}


def _tur_belirle(mime: str, dosya_adi: str) -> Optional[str]:
    """MIME türünden (yoksa uzantıdan) işlem türünü belirler: gorsel / video / metin."""
    if mime in GORSEL_TURLERI:
        return "gorsel"
    if mime in VIDEO_TURLERI:
        return "video"
    if mime in METIN_TURLERI:
        return "metin"
    # Yedek: uzantıdan tahmin
    uzanti = os.path.splitext(dosya_adi or "")[1].lower()
    if uzanti in {".png", ".jpg", ".jpeg", ".webp"}:
        return "gorsel"
    if uzanti in {".mp4", ".webm", ".mov"}:
        return "video"
    if uzanti in {".txt"}:
        return "metin"
    return None


def _dosya_kaydet(icerik: bytes, dosya_adi: str) -> str:
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    yol = os.path.join(settings.UPLOAD_DIR, dosya_adi)
    with open(yol, "wb") as f:
        f.write(icerik)
    return yol


def analiz_et(
    icerik: bytes,
    mime: str,
    dosya_adi: str,
    db: Session,
    user_id: Optional[int] = None,
) -> dict:
    """
    Ana orkestrasyon akışı:
    1) Türü belirle
    2) İlgili modülü çağır (görsel/video/metin)
    3) Erişilebilirlik puanlarını hesapla
    4) Content + AnalysisResult olarak veritabanına kaydet
    5) Birleşik sonucu döndür
    """
    tur = _tur_belirle(mime, dosya_adi)
    if tur is None:
        raise ValueError(f"Desteklenmeyen dosya türü: {mime}. Görsel, video veya düz metin gönderin.")

    alt_text = None
    altyazi_yolu = None
    orijinal_metin = None
    sade_metin = None
    dosya_yolu = None
    modul = ""

    if tur == "gorsel":
        modul = "gorsel_aciklama"
        dosya_yolu = _dosya_kaydet(icerik, dosya_adi)
        alt_text = alt_text_service.gorsel_aciklama_uret(icerik, mime)

    elif tur == "video":
        modul = "otomatik_altyazi"
        dosya_yolu = _dosya_kaydet(icerik, dosya_adi)
        altyazi_yolu = subtitle_service.altyazi_uret(icerik, dosya_adi)

    else:  # metin
        modul = "sadelestirme"
        orijinal_metin = icerik.decode("utf-8", errors="ignore")
        sade_metin = simplification_service.sadelestir(orijinal_metin)
        alt_text = sade_metin  # sade metni de alt_text alanında saklıyoruz (örnek)

    # Erişilebilirlik puanları
    kontrast = readability_service.renk_kontrast_skoru_hesapla(icerik if tur == "gorsel" else None)
    okunabilirlik = readability_service.okunabilirlik_skoru_hesapla(orijinal_metin or alt_text)
    genel = readability_service.genel_puan_hesapla(
        kontrast, okunabilirlik, alt_text_var=bool(alt_text), altyazi_var=bool(altyazi_yolu)
    )

    # Veritabanına kaydet
    content = Content(
        user_id=user_id,
        dosya_yolu=dosya_yolu,
        orijinal_metin=orijinal_metin,
    )
    db.add(content)
    db.flush()  # content.id almak için

    sonuc = AnalysisResult(
        content_id=content.id,
        otomatik_alt_text=alt_text,
        otomatik_altyazi_yolu=altyazi_yolu,
        renk_kontrast_skoru=kontrast,
        okunabilirlik_skoru=okunabilirlik,
        genel_erisilebilirlik_puani=genel,
    )
    db.add(sonuc)
    db.commit()
    db.refresh(sonuc)

    return {"content_id": content.id, "islem_turu": tur, "modul": modul, "sonuc": sonuc}
