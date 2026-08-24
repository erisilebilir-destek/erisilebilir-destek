"""
Gönderi (Post) ve Profil uç noktaları:
- GET /api/v1/posts (Gönderi Akışı)
- POST /api/v1/posts/{content_id}/publish (Gönderi Paylaşma/Yayınlama)
- GET /api/v1/users/{username}/posts (Kullanıcı Profil Gönderileri)
- GET /api/v1/users/{username}/score (Kullanıcının Engelsiz Yaşam Puanı)
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Content, AnalysisResult, User
from ..schemas import PostResponse, PostPublishRequest
from ..auth.router import mevcut_kullanici_opsiyonel

router = APIRouter(prefix="/api/v1", tags=["Gönderiler"])


@router.get("/posts", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    """Paylaşılan tüm gönderileri (akışı) listeler."""
    posts = (
        db.query(Content)
        .filter(Content.paylasildi_mi == True)
        .order_by(Content.olusturulma_tarihi.desc())
        .all()
    )
    return posts


@router.post("/posts/{content_id}/publish", response_model=PostResponse)
def publish_post(
    content_id: int,
    veri: PostPublishRequest,
    db: Session = Depends(get_db),
    kullanici: Optional[User] = Depends(mevcut_kullanici_opsiyonel),
):
    """Gönderiyi yayınlar, alt metni günceller ve onay durumunu işaretler."""
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        raise HTTPException(status_code=404, detail="İçerik bulunamadı.")

    # Gönderi sahibi yoksa veya misafirse oturum açan kullanıcıya ata
    if kullanici:
        content.user_id = kullanici.id
    elif not content.user_id:
        # Varsayılan demo kullanıcıyı bul/yarat
        demo = db.query(User).filter(User.kullanici_adi == "teknofest").first()
        if demo:
            content.user_id = demo.id

    content.orijinal_metin = veri.orijinal_metin
    content.paylasildi_mi = True

    # Analiz sonucunu güncelle
    if content.analiz:
        if veri.otomatik_alt_text:
            content.analiz.otomatik_alt_text = veri.otomatik_alt_text
        content.analiz.onaylandi_mi = veri.onaylandi_mi
    else:
        # Eğer hiç analizi yoksa (sadece düz metin paylaşıldıysa)
        # Basit bir analiz kaydı oluştur
        analiz = AnalysisResult(
            content_id=content.id,
            otomatik_alt_text=veri.otomatik_alt_text,
            genel_erisilebilirlik_puani=100,  # Düz metin varsayılan 100
            onaylandi_mi=veri.onaylandi_mi,
        )
        db.add(analiz)

    db.commit()
    db.refresh(content)
    return content


@router.get("/users/{username}/posts", response_model=List[PostResponse])
def get_user_posts(username: str, db: Session = Depends(get_db)):
    """Belirli bir kullanıcının paylaştığı gönderileri listeler."""
    user = db.query(User).filter(User.kullanici_adi == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")

    posts = (
        db.query(Content)
        .filter(Content.user_id == user.id, Content.paylasildi_mi == True)
        .order_by(Content.olusturulma_tarihi.desc())
        .all()
    )
    return posts


@router.get("/users/{username}/score")
def get_user_accessibility_score(username: str, db: Session = Depends(get_db)):
    """Kullanıcının paylaştığı gönderilerden hesaplanan Engelsiz Yaşam Puanı."""
    user = db.query(User).filter(User.kullanici_adi == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")

    posts = (
        db.query(Content)
        .filter(Content.user_id == user.id, Content.paylasildi_mi == True)
        .all()
    )

    if not posts:
        # Varsayılan başlangıç puanı
        return {"username": username, "score": 94, "adet": 0}

    toplam_puan = 0
    analizli_adet = 0

    for post in posts:
        if post.analiz and post.analiz.genel_erisilebilirlik_puani is not None:
            toplam_puan += post.analiz.genel_erisilebilirlik_puani
            analizli_adet += 1

    if analizli_adet == 0:
        return {"username": username, "score": 94, "adet": 0}

    ortalama = round(toplam_puan / analizli_adet)
    return {"username": username, "score": ortalama, "adet": analizli_adet}
