"""
Güvenlik yardımcıları: şifre hash'leme ve JWT üretme/çözme.
"""

from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext

from ..config import settings

# bcrypt yerine pbkdf2_sha256: ek sistem bağımlılığı gerektirmez, taşınabilir.
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def sifre_hashle(sifre: str) -> str:
    return pwd_context.hash(sifre)


def sifre_dogrula(sifre: str, sifre_hash: str) -> bool:
    return pwd_context.verify(sifre, sifre_hash)


def token_uret(veri: dict) -> str:
    icerik = veri.copy()
    icerik["exp"] = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    return jwt.encode(icerik, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


def token_coz(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
    except JWTError:
        return None
