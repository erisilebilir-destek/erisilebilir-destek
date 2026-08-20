"""
Sadeleştirme Servisi (uzun/karmaşık metin → sade Türkçe).

NLP modülü hazır olunca gerçek modele bağlanacak. Şimdilik örnek yanıt döner.
"""


def sadelestir(metin: str) -> str:
    """
    TODO: Gerçek sadeleştirme modeline bağla.
    Şimdilik metnin kısa bir önizlemesiyle örnek bir yanıt üretir.
    """
    onizleme = (metin or "").strip().replace("\n", " ")
    if len(onizleme) > 100:
        onizleme = onizleme[:100] + "..."
    return f"Sade hâli (örnek): {onizleme}" if onizleme else "Sadeleştirilecek metin bulunamadı."
