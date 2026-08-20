"""
Uygulama ayarları. Değerler ortam değişkenlerinden (.env) okunur.
Geliştirme kolaylığı için veritabanı varsayılan olarak SQLite'tır; canlıda/raporda
PostgreSQL kullanmak için .env içindeki DATABASE_URL'i PostgreSQL adresiyle değiştirin.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Veritabanı — PostgreSQL için örnek:
    # postgresql+psycopg2://kullanici:sifre@localhost:5432/nsosyal
    DATABASE_URL: str = "sqlite:///./nsosyal.db"

    # JWT / oturum yönetimi
    JWT_SECRET: str = "lutfen-bu-degeri-uretimde-degistirin"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24  # 1 gün

    # Google Gemini (görsel açıklama). Boşsa sistem örnek/mock yanıta düşer.
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-1.5-flash"

    # Yüklenen dosyaların kaydedileceği klasör
    UPLOAD_DIR: str = "uploads"
    MAKS_BOYUT_MB: int = 25


settings = Settings()
