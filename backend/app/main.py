"""
Erişilebilir Destek (NSosyal) — API Gateway / ana giriş noktası.

Katmanlar:
  - API Gateway .......... bu dosya (FastAPI uygulaması, CORS, router'ların birleştirilmesi)
  - Kimlik Doğrulama ..... app/auth
  - Orkestrasyon ......... app/services/orchestration.py  (+ app/routers/analyze.py)
  - Yapay Zeka Modülleri . app/services/*_service.py
  - Veri Katmanı ......... app/database.py, app/models.py

Çalıştırma:
    uvicorn app.main:app --reload
Dokümantasyon:  http://127.0.0.1:8000/docs
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .auth.router import router as auth_router
from .config import settings
from .database import Base, engine
from .routers.analyze import router as analyze_router
from .routers.posts import router as posts_router

# Tablolar yoksa oluştur (geliştirme kolaylığı; üretimde Alembic önerilir).
Base.metadata.create_all(bind=engine)

# Yükleme klasörünün varlığından emin ol
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

app = FastAPI(
    title="Erişilebilir Destek (NSosyal) API",
    description="TEKNOFEST 2026 — erişilebilir sosyal medya destek platformu backend'i.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dosya Paylaşımı (yüklenen resimler/videolar/altyazılar için).
# Adres, veritabanında saklanan göreli yolla ("uploads/...") birebir eşleşmelidir.
app.mount(f"/{settings.UPLOAD_DIR}", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")

# Router'lar
app.include_router(auth_router)
app.include_router(analyze_router)
app.include_router(posts_router)



@app.get("/", tags=["Sağlık"])
def saglik_kontrolu():
    return {"durum": "calisiyor", "servis": "Erişilebilir Destek (NSosyal) API", "surum": "1.0.0"}
