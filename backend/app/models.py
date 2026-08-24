"""
Veritabanı modelleri (ORM) — Users, Contents, AnalysisResults.

Not: Sütun adları Türkçe anlamlarını korur ama SQL/Python uyumu için "ı, ş, ç" olmadan yazılmıştır: kullanici_adi, sifre_hash gibi.

Sütunlar SQLAlchemy 2.0'ın tip bildirimli biçimiyle (Mapped + mapped_column) tanımlanır.
Böylece kullanici.id gerçek tipiyle (int) görünür; eski Column biçiminde tip
denetleyici bunu Column[int] sanıp hatalı uyarı veriyordu.
"""

from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


def _simdi() -> datetime:
    return datetime.now(timezone.utc)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    kullanici_adi: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    sifre_hash: Mapped[str] = mapped_column(String(255))
    eposta: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    kayit_tarihi: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)

    # Bir kullanıcının birden çok içeriği olabilir
    contents: Mapped[List["Content"]] = relationship(
        back_populates="user", cascade="all, delete-orphan",
    )


class Content(Base):
    __tablename__ = "contents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # misafir kullanıcı için boş olabilir
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)
    # görsel/video dosyasının yolu
    dosya_yolu: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    # düz metin gönderildiyse
    orijinal_metin: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    paylasildi_mi: Mapped[bool] = mapped_column(Boolean, default=False)
    olusturulma_tarihi: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_simdi)

    user: Mapped[Optional["User"]] = relationship(back_populates="contents")
    # Bir içeriğin bir analiz sonucu olur
    analiz: Mapped[Optional["AnalysisResult"]] = relationship(
        back_populates="content", cascade="all, delete-orphan",
    )


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    content_id: Mapped[int] = mapped_column(ForeignKey("contents.id"))

    otomatik_alt_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    # WebVTT/SRT dosya adresi
    otomatik_altyazi_yolu: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    renk_kontrast_skoru: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    okunabilirlik_skoru: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    # 0-100 arası genel puan
    genel_erisilebilirlik_puani: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    onaylandi_mi: Mapped[bool] = mapped_column(Boolean, default=False)
    guncelleme_tarihi: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_simdi, onupdate=_simdi,
    )

    content: Mapped["Content"] = relationship(back_populates="analiz")
