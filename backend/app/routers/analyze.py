"""
Orkestrasyon uç noktası: POST /api/v1/analyze
Dosyayı alır, orkestrasyon servisine verir ve tek bir JSON sonuç döner.
"""

from typing import Optional

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from ..auth.router import mevcut_kullanici_opsiyonel
from ..config import settings
from ..database import get_db
from ..models import User
from ..schemas import AnalyzeResponse
from ..services import orchestration

router = APIRouter(prefix="/api/v1", tags=["Analiz"])


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(
    dosya: UploadFile = File(...),
    db: Session = Depends(get_db),
    kullanici: Optional[User] = Depends(mevcut_kullanici_opsiyonel),
):
    icerik = await dosya.read()
    boyut = len(icerik)

    if boyut == 0:
        raise HTTPException(status_code=400, detail="Dosya boş görünüyor. Lütfen geçerli bir dosya gönderin.")
    if boyut > settings.MAKS_BOYUT_MB * 1024 * 1024:
        raise HTTPException(status_code=413, detail=f"Dosya çok büyük. En fazla {settings.MAKS_BOYUT_MB} MB kabul edilir.")

    try:
        cikti = orchestration.analiz_et(
            icerik=icerik,
            mime=dosya.content_type or "",
            dosya_adi=dosya.filename or "dosya",
            db=db,
            user_id=kullanici.id if kullanici else None,
        )
    except ValueError as e:
        # Desteklenmeyen tür gibi anlaşılır kullanıcı hataları
        raise HTTPException(status_code=415, detail=str(e))

    return AnalyzeResponse(
        durum="basarili",
        content_id=cikti["content_id"],
        islem_turu=cikti["islem_turu"],
        modul=cikti["modul"],
        sonuc=cikti["sonuc"],
        **{"not": "Sonuç veritabanına kaydedildi. Gerçek modeller bağlanana kadar bazı çıktılar örnektir."},
    )
