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
    Görsel baytlarını alır, Gemini 1.5 Flash ile Türkçe alt-text üretir.
    Anahtar yoksa örnek metne düşer.
    """
    if not settings.GEMINI_API_KEY:
        return _mock_alt_text()

    try:
        import google.generativeai as genai

        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel(settings.GEMINI_MODEL)
        yanit = model.generate_content(
            [
                W3C_PROMPT,
                {"mime_type": mime_tur, "data": icerik},
            ]
        )
        metin = (yanit.text or "").strip()
        return metin or _mock_alt_text()
    except Exception:
        # Ağ/anahtar/kütüphane sorununda iskeletin çalışmaya devam etmesi için:
        return _mock_alt_text()
