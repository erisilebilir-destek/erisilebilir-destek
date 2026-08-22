"""
Altyazı Servisi — video → Türkçe altyazı (WebVTT).

Sevda'nın STT PoC'si (nsosyal_poc_stt.py, S-02/S-03) bu servise uyarlanmıştır.
Akış: video baytları → geçici dosya → FFmpeg ile 16 kHz mono ses → Whisper (Türkçe)
→ zaman kodlu WebVTT.

Sağlamlık: FFmpeg veya openai-whisper kurulu değilse sistem çökmez, örnek (mock)
altyazıya düşer. Böylece backend her koşulda çalışır.

Gerçek altyazı için kurulum:
    brew install ffmpeg
    pip install openai-whisper
"""

import os
import subprocess

from ..config import settings

_ORNEK_VTT = (
    "WEBVTT\n\n"
    "00:00:00.000 --> 00:00:02.500\n"
    "Merhaba, bu bir örnek Türkçe altyazıdır.\n\n"
    "00:00:02.500 --> 00:00:05.000\n"
    "Gerçek altyazı için FFmpeg ve Whisper kurulmalıdır.\n"
)


def _ffmpeg_var_mi() -> bool:
    """Sistemde FFmpeg kurulu mu? (Sevda'nın check_ffmpeg mantığı)"""
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


def _sesi_ayikla(video_yolu: str, wav_yolu: str) -> None:
    """FFmpeg ile videodan 16 kHz mono PCM ses ayıklar (Whisper'ın beklediği biçim)."""
    komut = ["ffmpeg", "-y", "-i", video_yolu, "-vn",
             "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", wav_yolu]
    subprocess.run(komut, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)


def _zaman_bicimle(saniye: float) -> str:
    """Saniyeyi WebVTT zaman biçimine çevirir: HH:MM:SS.mmm (Sevda'nın format_timestamp'i)."""
    ms = int(round((saniye - int(saniye)) * 1000))
    if ms >= 1000:
        saniye += 1
        ms -= 1000
    dk, sn = divmod(int(saniye), 60)
    sa, dk = divmod(dk, 60)
    return f"{sa:02d}:{dk:02d}:{sn:02d}.{ms:03d}"


def _vtt_yaz(segmentler: list, cikti_yolu: str) -> None:
    """Zaman damgalı segmentleri WebVTT olarak yazar (Sevda'nın write_vtt_file'i)."""
    with open(cikti_yolu, "w", encoding="utf-8") as f:
        f.write("WEBVTT\n\n")
        for i, seg in enumerate(segmentler, 1):
            bas = _zaman_bicimle(seg["start"])
            son = _zaman_bicimle(seg["end"])
            f.write(f"{i}\n{bas} --> {son}\n{seg['text'].strip()}\n\n")


def altyazi_uret(icerik: bytes, dosya_adi: str) -> str:
    """
    Video baytlarını alır, Türkçe altyazı (WebVTT) üretir ve dosya yolunu döndürür.
    FFmpeg/Whisper yoksa örnek altyazıya düşer.
    """
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    ad = os.path.splitext(dosya_adi)[0] or "video"
    video_yolu = os.path.join(settings.UPLOAD_DIR, dosya_adi or "video.mp4")
    vtt_yolu = os.path.join(settings.UPLOAD_DIR, f"{ad}.vtt")

    with open(video_yolu, "wb") as f:
        f.write(icerik)

    # Whisper kurulu mu?
    try:
        import whisper
    except ImportError:
        whisper = None

    # Gerekli araçlar yoksa örnek altyazı üret
    if whisper is None or not _ffmpeg_var_mi():
        with open(vtt_yolu, "w", encoding="utf-8") as f:
            f.write(_ORNEK_VTT)
        return vtt_yolu

    # Gerçek akış: ses ayıkla → Whisper ile Türkçe deşifre → WebVTT yaz
    wav_yolu = os.path.join(settings.UPLOAD_DIR, f"{ad}_temp.wav")
    try:
        _sesi_ayikla(video_yolu, wav_yolu)
        model = whisper.load_model(settings.WHISPER_MODEL)
        sonuc = model.transcribe(wav_yolu, language="tr")
        _vtt_yaz(sonuc["segments"], vtt_yolu)
    except Exception:
        # Herhangi bir hatada sistemin çalışmaya devam etmesi için örnek altyazı
        with open(vtt_yolu, "w", encoding="utf-8") as f:
            f.write(_ORNEK_VTT)
    finally:
        if os.path.exists(wav_yolu):
            os.remove(wav_yolu)

    return vtt_yolu