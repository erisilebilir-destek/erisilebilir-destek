"""
Kimlik Doğrulama Servisi — kayıt ve giriş uç noktaları,
ayrıca istekten mevcut kullanıcıyı çözen bağımlılıklar.
"""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..schemas import Token, UserCreate, UserOut
from .security import sifre_dogrula, sifre_hashle, token_coz, token_uret

router = APIRouter(prefix="/auth", tags=["Kimlik Doğrulama"])

# auto_error=False: token yoksa hata fırlatmaz, None döner (misafir kullanım için).
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login", auto_error=False)


@router.post("/register", response_model=UserOut, status_code=201)
def kayit_ol(veri: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.kullanici_adi == veri.kullanici_adi).first():
        raise HTTPException(status_code=400, detail="Bu kullanıcı adı zaten alınmış.")
    if db.query(User).filter(User.eposta == veri.eposta).first():
        raise HTTPException(status_code=400, detail="Bu e-posta zaten kayıtlı.")

    kullanici = User(
        kullanici_adi=veri.kullanici_adi,
        eposta=veri.eposta,
        sifre_hash=sifre_hashle(veri.sifre),
    )
    db.add(kullanici)
    db.commit()
    db.refresh(kullanici)
    return kullanici


@router.post("/login", response_model=Token)
def giris_yap(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # OAuth2 formu 'username' alanı kullanır; biz kullanıcı adı olarak alıyoruz.
    kullanici = db.query(User).filter(User.kullanici_adi == form.username).first()
    if not kullanici or not sifre_dogrula(form.password, kullanici.sifre_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Kullanıcı adı veya şifre hatalı.",
        )
    token = token_uret({"sub": str(kullanici.id), "kullanici_adi": kullanici.kullanici_adi})
    return Token(access_token=token)


def mevcut_kullanici_opsiyonel(
    token: Optional[str] = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> Optional[User]:
    """Token varsa kullanıcıyı döndürür; yoksa None (misafir). Endpoint'i kilitlemez."""
    if not token:
        return None
    veri = token_coz(token)
    if not veri:
        return None
    return db.query(User).filter(User.id == int(veri.get("sub", 0))).first()
