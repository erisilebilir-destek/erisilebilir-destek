"""
Okunabilirlik ve Erişilebilirlik Puanlama Servisi.
"""

from typing import Optional


def renk_kontrast_skoru_hesapla(icerik: Optional[bytes]) -> float:
    """TODO: Gerçek kontrast analizi (WCAG oranı). Örnek: sabit makul bir değer."""
    return 4.5  # WCAG AA eşiği 4.5:1


def okunabilirlik_skoru_hesapla(metin: Optional[str]) -> float:
    """
    Çok basit bir örnek: cümle başına ortalama kelime sayısına göre 0-100.
    TODO: Türkçeye uygun gerçek okunabilirlik formülüyle değiştir (B-04).
    """
    if not metin:
        return 70.0
    cumleler = [c for c in metin.replace("!", ".").replace("?", ".").split(".") if c.strip()]
    if not cumleler:
        return 70.0
    ort_kelime = sum(len(c.split()) for c in cumleler) / len(cumleler)
    # Kısa cümle -> daha okunabilir. 8 kelime civarını ideal kabul edelim.
    puan = max(0.0, min(100.0, 100 - abs(ort_kelime - 8) * 5))
    return round(puan, 1)


def genel_puan_hesapla(kontrast: float, okunabilirlik: float, alt_text_var: bool, altyazi_var: bool) -> int:
    """
    0-100 arası genel erişilebilirlik puanı (örnek ağırlıklandırma).
    """
    puan = 0.0
    puan += min(25.0, kontrast / 7.0 * 25)          # kontrast (maks 25)
    puan += okunabilirlik / 100 * 35                # okunabilirlik (maks 35)
    puan += 20 if alt_text_var else 0               # alternatif metin (20)
    puan += 20 if altyazi_var else 0                # altyazı (20)
    return int(round(min(100.0, puan)))
