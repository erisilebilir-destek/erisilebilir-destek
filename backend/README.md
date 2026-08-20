# Erişilebilir Destek (NSosyal) — Backend

TEKNOFEST 2026 projesi için modüler FastAPI backend'i. Bir dosya alır (görsel,
video veya metin), türüne göre ilgili yapay zeka modülüne yönlendirir,
erişilebilirlik puanlarını hesaplar, sonucu PostgreSQL'e kaydeder ve tek bir JSON
olarak döner.

## Mimari ve klasör yapısı

```
backend/
├── requirements.txt
├── .env.example              # .env olarak kopyalayın
├── README.md
└── app/
    ├── main.py               # API Gateway — FastAPI girişi, CORS, router birleştirme
    ├── config.py             # Ayarlar (.env'den okur)
    ├── database.py           # Veri katmanı — SQLAlchemy motoru/oturumu
    ├── models.py             # ORM modelleri: Users, Contents, AnalysisResults
    ├── schemas.py            # Pydantic şemaları
    ├── auth/                 # Kimlik Doğrulama Servisi
    │   ├── security.py       # şifre hash + JWT
    │   └── router.py         # /auth/register, /auth/login
    ├── services/             # Orkestrasyon + Yapay Zeka Modülleri
    │   ├── orchestration.py  # isteği türüne göre yönlendirir, sonucu birleştirir + kaydeder
    │   ├── alt_text_service.py      # Görsel açıklama — Gemini 1.5 Flash
    │   ├── subtitle_service.py      # Altyazı (Whisper hattına bağlanacak)
    │   ├── simplification_service.py# Metin sadeleştirme
    │   └── readability_service.py   # Kontrast + okunabilirlik + 0-100 puan
    └── routers/
        └── analyze.py        # POST /api/v1/analyze (orkestrasyon uç noktası)
```

## Kurulum ve çalıştırma

```bash
cd backend
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                 # sonra .env'i düzenleyin
uvicorn app.main:app --reload
```

- Sağlık kontrolü: <http://127.0.0.1:8000/>
- Otomatik dokümantasyon (Swagger): <http://127.0.0.1:8000/docs>

> **Veritabanı:** Kolay başlangıç için varsayılan SQLite'tır (kurulum gerektirmez).
> Canlı/rapor için `.env` içindeki `DATABASE_URL`'i PostgreSQL adresiyle değiştirin:
> `postgresql+psycopg2://kullanici:sifre@localhost:5432/nsosyal`
>
> **Gemini:** `GEMINI_API_KEY` boşsa görsel açıklama örnek (mock) metne düşer,
> sistem yine çalışır. Anahtar girilince gerçek Gemini 1.5 Flash yanıtı döner.

## Uç noktalar

| Yöntem | Yol                 | Açıklama                                          |
|--------|---------------------|---------------------------------------------------|
| GET    | `/`                 | Sağlık kontrolü                                   |
| POST   | `/auth/register`    | Kayıt (kullanıcı_adı, e-posta, şifre)             |
| POST   | `/auth/login`       | Giriş → JWT token                                 |
| POST   | `/api/v1/analyze`   | Dosya al → analiz et → JSON döndür (token opsiyonel) |

## Postman ile test

**Kayıt:** POST `/auth/register`, Body → raw → JSON:
```json
{ "kullanici_adi": "zeynep", "eposta": "zeynep@ornek.com", "sifre": "gizli123" }
```

**Giriş:** POST `/auth/login`, Body → x-www-form-urlencoded: `username=zeynep`,
`password=gizli123`. Dönen `access_token`'ı kopyalayın.

**Analiz:** POST `/api/v1/analyze`, Body → form-data: Key `dosya` (tür: File),
bir dosya seçin. İsterseniz Authorization → Bearer Token alanına token'ı yapıştırın
(token olmadan da misafir olarak çalışır). **Send.**

### Beklenen davranış (test edildi)

- Geçerli görsel/metin → **200**, sonuç veritabanına kaydedilir, JSON döner.
- Boş dosya → **400** anlaşılır hata.
- Desteklenmeyen tür → **415** anlaşılır hata.
- Çok büyük dosya (>25 MB) → **413**.

## Gerçek modellere bağlama (sonraki adım)

`app/services/` altındaki servis fonksiyonlarının içi, ilgili modül hazır olunca
doldurulacak:

- `alt_text_service.gorsel_aciklama_uret` → Merve'nin M-04 modeli / Gemini
- `subtitle_service.altyazi_uret` → Sevda'nın Whisper + FFmpeg hattı (S-08)
- `readability_service.*` → Beril'in 100 puanlık matrisi (B-04)

Yanıt anahtarları sabit tutulduğu sürece arayüz ve diğer modüller etkilenmeden
gerçek modele geçilebilir.
