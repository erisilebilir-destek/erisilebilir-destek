# PoC Scriptleri

Bu klasör, projenin **kavram kanıtı (Proof of Concept)** aşamasında yazılmış,
tek başına çalışan demo scriptlerini içerir. Bunlar tarihsel kayıt olarak
saklanır; **çalışan sistemde kullanılmazlar.**

| Dosya | Konu | Sorumlu | Üretime geçtiği yer |
|-------|------|---------|---------------------|
| `poc_gorsel_alt_text.py` | Gemini ile Türkçe alternatif metin üretimi | Zeynep Ecren | `backend/app/services/alt_text_service.py` |
| `poc_altyazi_stt.py` | FFmpeg + Whisper ile Türkçe altyazı (WebVTT/SRT) | Sevda | `backend/app/services/subtitle_service.py` |

## Çalıştırma

Scriptler backend'den bağımsızdır ve kendi bağımlılıklarını ister:

```bash
# Görsel alt metin PoC
pip install google-genai pillow
export GEMINI_API_KEY="anahtariniz"
python poc/poc_gorsel_alt_text.py

# Altyazı PoC (sistemde FFmpeg kurulu olmalı)
pip install openai-whisper
python poc/poc_altyazi_stt.py
```

> Not: `poc_gorsel_alt_text.py` içindeki test görseli yolu sabit yazılmıştır;
> çalıştırmadan önce kendi görselinizin yolunu vermeniz gerekir.
