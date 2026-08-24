"""
Sadeleştirme Servisi (uzun/karmaşık metin → sade Türkçe).

NLP modülü hazır olunca gerçek modele bağlanacak. Şimdilik örnek yanıt döner.
"""


def sadelestir(metin: str) -> str:

    onizleme = (metin or "").strip().replace("\n", " ")
    if len(onizleme) > 100:
        onizleme = onizleme[:100] + "..."
    return f"Sade hâli (örnek): {onizleme}" if onizleme else "Sadeleştirilecek metin bulunamadı."
