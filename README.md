# Erişilebilir Destek

**Erişilebilir Destek**, sosyal medya içeriklerini herkes için erişilebilir hâle getiren yapay zeka tabanlı bir platformdur. Paylaşılan görsel, video ve metinleri işleyerek Türkçe alt metin, otomatik altyazı, sadeleştirilmiş içerik ve erişilebilirlik puanı üretir; böylece görme, işitme veya okuma güçlüğü yaşayan kullanıcıların içeriğe erişimini kolaylaştırır.

## İçindekiler

- [Özellikler](#özellikler)
- [Klasör Yapısı](#klasör-yapısı)
- [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)
- [Sistem Mimarisi](#sistem-mimarisi)
- [Teknolojiler](#teknolojiler)
- [Tasarım ve Arayüz](#tasarım-ve-arayüz-uiux)
- [Dokümanlar](#dokümanlar)
- [Ekip](#ekip)

## Özellikler

Platform dört yapay zeka modülünden oluşur:

- **Görsel Açıklama** — Paylaşılan görseldeki nesne, ortam ve önemli detayları analiz ederek Türkçe alternatif metin (alt text) oluşturur.
- **Otomatik Altyazı** — Videodaki konuşmayı metne çevirir, zaman kodlarını düzenler ve Türkçe altyazı (WebVTT) üretir.
- **Sadeleştirme (NLP)** — Uzun veya karmaşık gönderileri özetler, daha sade bir Türkçeyle yeniden yazar ve metni seslendirmeye uygun hâle getirir.
- **Erişilebilirlik Kontrolü** — Renk kontrastı, okunabilirlik ve eksik alt metin/altyazı durumunu değerlendirerek 0-100 arası bir erişilebilirlik puanı verir.

Tüm modüller, erişilebilir bir kullanıcı arayüzü (ekran okuyucu uyumu, klavye navigasyonu, yüksek kontrast, ölçeklenebilir yazı) üzerinden tek bir sistemde birleşir.

## Klasör Yapısı

```
erisilebilir-destek/
├── README.md
├── backend/                        # FastAPI uygulaması (ayrıntı: backend/README.md)
│   ├── requirements.txt
│   ├── .env.example                # .env olarak kopyalanır
│   └── app/
│       ├── main.py                 # API Gateway — FastAPI girişi, CORS, router birleştirme
│       ├── config.py               # Ayarlar (.env'den okunur)
│       ├── database.py             # Veri katmanı — SQLAlchemy motoru/oturumu
│       ├── models.py               # ORM modelleri: users, contents, analysis_results
│       ├── schemas.py              # Pydantic istek/yanıt şemaları
│       ├── auth/                   # Kimlik doğrulama — JWT üretimi, kayıt/giriş
│       ├── routers/                # REST uç noktaları (analyze, posts)
│       └── services/               # Orkestrasyon + yapay zeka modül servisleri
├── frontend/                       # Erişilebilir web arayüzü (HTML + CSS + JS)
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── poc/                            # Kavram kanıtı scriptleri (tarihsel kayıt)
└── docs/                           # Mimari ve proje dokümantasyonu
    └── arsiv/                      # Süperseded eski taslak sürümler
```

> Yapay zeka modülleri ayrı bir `ai-modules/` klasöründe değil, `backend/app/services/`
> altında birer servis olarak yaşar. Her modül bağımsız bir dosyadır; ortak
> girdi/çıktı sözleşmesiyle orkestrasyon servisine bağlanır.

## Kurulum ve Çalıştırma

### Backend

```bash
git clone https://github.com/erisilebilir-destek/erisilebilir-destek.git
cd erisilebilir-destek/backend

python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env                # sonra .env'i kendi anahtarlarınızla doldurun
uvicorn app.main:app --reload
```

- Sağlık kontrolü: <http://127.0.0.1:8000/>
- Swagger dokümantasyonu: <http://127.0.0.1:8000/docs>

### Frontend

Arayüz bağımlılıksız statik dosyalardan oluşur. Backend çalışırken:

```bash
cd frontend
python -m http.server 5500
```

Ardından <http://127.0.0.1:5500> adresini açın. Arayüz `http://127.0.0.1:8000`
adresindeki backend'e bağlanır (`frontend/app.js` içindeki `API_BASE_URL`).

> **Anahtar yoksa da çalışır:** `GEMINI_API_KEY` boşsa, FFmpeg/Whisper kurulu
> değilse sistem çökmez; ilgili servis örnek (mock) çıktıya düşer.

## Sistem Mimarisi

Platform katmanlı bir mimariye sahiptir: kullanıcı arayüzü → backend (FastAPI) →
yapay zeka modülleri → model/servis katmanı → veri katmanı. Şema ve veri akışı
için [`docs/mimari.md`](docs/mimari.md) dosyasına bakınız
(tarayıcıda görüntülenebilir sürüm: [`docs/mimari-diyagram.html`](docs/mimari-diyagram.html)).

## Teknolojiler

- **Backend:** Python, FastAPI
- **Veritabanı:** SQLite (geliştirme) / PostgreSQL (canlı)
- **API:** REST (JSON), JWT kimlik doğrulama
- **Yapay Zeka:** Gemini Flash (görsel betimleme), Whisper + FFmpeg (konuşma tanıma), dil modeli (sadeleştirme)
- **Arayüz:** Erişilebilir, mobil uyumlu web arayüzü (HTML5, CSS3, vanilla JS)

## Tasarım ve Arayüz (UI/UX)

- **Figma Tasarım Dosyası:** [Figma Tasarım Şablonu](https://www.figma.com/design/aNmnXW0srUldtlIRkjBoPe/233125013432---22DH114378---Tr%E1%BA%A7n-Th%E1%BB%8B-Ng%E1%BB%8Dc-Vy--Community-?node-id=9-47&t=lXy90I1TdTgpuIB1-1)
- **Geliştirilen Ekranlar:** Gönderi Akışı, Profil, Gönderi Paylaşımı (Erişilebilirlik Kontrolü ile birlikte).

## Dokümanlar

| Doküman | İçerik |
|---------|--------|
| [`docs/mimari.md`](docs/mimari.md) | Katmanlı mimari şeması ve veri akışı |
| [`docs/proje-tanitim-raporu.md`](docs/proje-tanitim-raporu.md) | Problem tanımı, amaç, kapsam — proje tanıtım raporu |
| [`docs/inovasyon-teknik-raporu.md`](docs/inovasyon-teknik-raporu.md) | İnovasyon ve teknik rapor |
| [`docs/model-karsilastirma-notu.md`](docs/model-karsilastirma-notu.md) | VLM model karşılaştırması ve seçim gerekçesi |
| `docs/entegrasyon-dokumani.docx` | Modüllerin backend'e entegrasyon planı |
| `docs/teknik-kontrol-notu.docx` | Teknik kontrol / test notları |
| `docs/arsiv/` | Yerini yeni sürümlere bırakmış eski taslaklar |

## Ekip

| Üye | Rol |
|-----|-----|
| Merve | Takım kaptanı ve yapay zeka |
| Zeynep Ecren | Yazılım, backend ve sistem entegrasyonu |
| Nez | Backend desteği, kalite güvence ve test |
| Beril | Erişilebilirlik analizi, UI/UX ve puanlama |
| Sevda | Video, ses ve otomatik altyazı modülü |

---

*Bu proje bir ekip çalışması kapsamında geliştirilmektedir.*
