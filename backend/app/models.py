"""
Veritabanı modelleri (ORM) — Users, Contents, AnalysisResults.

Not: Sütun adları Türkçe anlamlarını korur ama SQL/Python uyumu için
diyakritiksiz (ı, ş, ç olmadan) yazılmıştır: kullanici_adi, sifre_hash gibi.
"""

from datetime import datetime, timezone

from sqlalchemy import (
    Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text,
)
from sqlalchemy.orm import relationship

from .database import Base


def _simdi():
    return datetime.now(timezone.utc)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    kullanici_adi = Column(String(50), unique=True, nullable=False, index=True)
    sifre_hash = Column(String(255), nullable=False)
    eposta = Column(String(120), unique=True, nullable=False, index=True)
    kayit_tarihi = Column(DateTime(timezone=True), default=_simdi)

    # Bir kullanıcının birden çok içeriği olabilir
    contents = relationship("Content", back_populates="user", cascade="all, delete-orphan")


class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # misafir için boş olabilir
    dosya_yolu = Column(String(255), nullable=True)      # görsel/video dosyasının yolu
    orijinal_metin = Column(Text, nullable=True)         # düz metin gönderildiyse
    paylasildi_mi = Column(Boolean, default=False)
    olusturulma_tarihi = Column(DateTime(timezone=True), default=_simdi)

    user = relationship("User", back_populates="contents")
    # Bir içeriğin bir analiz sonucu olur
    analiz = relationship(
        "AnalysisResult", back_populates="content",
        uselist=False, cascade="all, delete-orphan",
    )


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, ForeignKey("contents.id"), nullable=False)

    otomatik_alt_text = Column(Text, nullable=True)
    otomatik_altyazi_yolu = Column(String(255), nullable=True)   # WebVTT/SRT dosya adresi
    renk_kontrast_skoru = Column(Float, nullable=True)
    okunabilirlik_skoru = Column(Float, nullable=True)
    genel_erisilebilirlik_puani = Column(Integer, nullable=True)  # 0-100
    onaylandi_mi = Column(Boolean, default=False)
    guncelleme_tarihi = Column(DateTime(timezone=True), default=_simdi, onupdate=_simdi)

    content = relationship("Content", back_populates="analiz")
