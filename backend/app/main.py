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

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth.router import router as auth_router
from .database import Base, engine
from .routers.analyze import router as analyze_router

# Tablolar yoksa oluştur (geliştirme kolaylığı; üretimde Alembic önerilir).
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Erişilebilir Destek (NSosyal) API",
    description="TEKNOFEST 2026 — erişilebilir sosyal medya destek platformu backend'i.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # geliştirme; üretimde arayüz adresine daraltılacak
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router'lar
app.include_router(auth_router)
app.include_router(analyze_router)


@app.get("/", tags=["Sağlık"])
def saglik_kontrolu():
    return {"durum": "calisiyor", "servis": "Erişilebilir Destek (NSosyal) API", "surum": "1.0.0"}
