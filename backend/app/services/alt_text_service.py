"""
Görsel Açıklama Servisi (Alt-Text) — Google Gemini 1.5 Flash entegrasyonu.

Bir görsel alır ve W3C erişilebilirlik ilkelerine uygun Türkçe alternatif metin
üretir. GEMINI_API_KEY tanımlı değilse ya da kütüphane yoksa, sistem çökmemesi
için örnek (mock) bir metne düşer — böylece iskelet her koşulda çalışır.
"""

from ..config import settings

# W3C uyumlu betimleme istemi (prompt): nesnel, kısa, "Resimde/Görselde" ile
# başlamadan, varsa görseldeki yazıları da (OCR) içererek.
W3C_PROMPT = (
    "Bu görseli görme engelli bir kullanıcı için Türkçe olarak betimle. "
    "Nesnel ol, yorum katma. En fazla 2-3 cümle kullan. "
    "'Resimde', 'Görselde', 'Bu görselde' gibi ifadelerle BAŞLAMA; doğrudan sahneyi anlat. "
    "Görselde okunabilir bir yazı varsa onu da aynen aktar. "
    "Süslü sıfatlardan kaçın, erişilebilirlik odaklı ve sade bir dil kullan."
)


def _mock_alt_text() -> str:
    return (
        "Ahşap bir masanın üzerinde açık bir dizüstü bilgisayar duruyor; "
        "ekranında bir grafik görülüyor ve yanında yarı dolu bir kahve fincanı var."
    )


def gorsel_aciklama_uret(icerik: bytes, mime_tur: str) -> str:
    """
    Görsel baytlarını alır, Gemini 3.6 Flash ile Türkçe alt-text üretir.
    Anahtar yoksa örnek metne düşer.
    """
    if not settings.GEMINI_API_KEY:
        return _mock_alt_text()

    try:
        import io
        from PIL import Image
        from google import genai

        # Yeni SDK Client başlatımı
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        
        # Baytları PIL görsel nesnesine dönüştürüyoruz
        img = Image.open(io.BytesIO(icerik))
        
        # İçerik üretimi
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=[img, W3C_PROMPT]
        )
        metin = (response.text or "").strip()
        return metin or _mock_alt_text()
    except Exception as e:
        print(f"[HATA - ALT-TEXT SERVİSİ] Gemini API çağrısı sırasında hata oluştu: {str(e)}")
        # Ağ/anahtar/kütüphane sorununda iskeletin çalışmaya devam etmesi için:
        return _mock_alt_text()
