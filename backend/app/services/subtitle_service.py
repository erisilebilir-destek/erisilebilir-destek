"""
Altyazı Servisi (video → Türkçe altyazı).

Bu servis, Sevda'nın Whisper + FFmpeg hattına (S-02/S-03/S-08) bağlanacaktır.
Şimdilik örnek bir WebVTT içeriği/yolu döndürür.
"""

import os

from ..config import settings

_ORNEK_VTT = (
    "WEBVTT\n\n"
    "00:00:00.000 --> 00:00:02.500\n"
    "Merhaba, bu bir örnek Türkçe altyazıdır.\n\n"
    "00:00:02.500 --> 00:00:05.000\n"
    "Gerçek altyazı Whisper hattı bağlanınca üretilecek.\n"
)


def altyazi_uret(icerik: bytes, dosya_adi: str) -> str:
    """
    Video baytlarını alır ve bir WebVTT dosyası yolu döndürür.
    TODO: Sevda'nın hattına bağla (FFmpeg ile ses ayır -> Whisper -> Türkçe NLP -> WebVTT).
    """
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    vtt_yolu = os.path.join(settings.UPLOAD_DIR, f"{os.path.splitext(dosya_adi)[0]}.vtt")
    with open(vtt_yolu, "w", encoding="utf-8") as f:
        f.write(_ORNEK_VTT)
    return vtt_yolu
