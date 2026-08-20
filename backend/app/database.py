"""
Veri katmanı: SQLAlchemy motoru, oturum (session) üreticisi ve taban model.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import settings

# SQLite kullanılıyorsa çoklu iş parçacığı için özel ayar gerekir.
connect_args = (
    {"check_same_thread": False}
    if settings.DATABASE_URL.startswith("sqlite")
    else {}
)

engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():
    """Her istek için bir veritabanı oturumu açar ve iş bitince kapatır (FastAPI bağımlılığı)."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
