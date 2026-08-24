"""
Pydantic şemaları — istek/yanıt gövdelerinin doğrulanması ve serileştirilmesi.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


#  Kullanıcı
class UserCreate(BaseModel):
    kullanici_adi: str = Field(min_length=3, max_length=50)
    eposta: EmailStr
    sifre: str = Field(min_length=6, max_length=128)


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    kullanici_adi: str
    eposta: EmailStr
    kayit_tarihi: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Analiz sonucu
class AnalysisResultOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    otomatik_alt_text: Optional[str] = None
    otomatik_altyazi_yolu: Optional[str] = None
    renk_kontrast_skoru: Optional[float] = None
    okunabilirlik_skoru: Optional[float] = None
    genel_erisilebilirlik_puani: Optional[int] = None
    onaylandi_mi: bool = False


class AnalyzeResponse(BaseModel):
    durum: str
    content_id: int
    islem_turu: str            # gorsel / video / metin
    modul: str                 # calisan modul adi
    sonuc: AnalysisResultOut
    not_: Optional[str] = Field(default=None, alias="not")


# Gönderi
class PostPublishRequest(BaseModel):
    orijinal_metin: Optional[str] = None
    otomatik_alt_text: Optional[str] = None
    onaylandi_mi: bool = True


class UserMinOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    kullanici_adi: str


class PostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user: Optional[UserMinOut] = None
    dosya_yolu: Optional[str] = None
    orijinal_metin: Optional[str] = None
    paylasildi_mi: bool
    olusturulma_tarihi: datetime
    analiz: Optional[AnalysisResultOut] = None

