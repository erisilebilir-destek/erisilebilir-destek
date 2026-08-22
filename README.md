# Erişilebilir Destek

**Erişilebilir Destek**, sosyal medya içeriklerini herkes için erişilebilir hâle getiren yapay zeka tabanlı bir platformdur. Paylaşılan görsel, video ve metinleri işleyerek Türkçe alt metin, otomatik altyazı, sadeleştirilmiş içerik ve erişilebilirlik puanı üretir; böylece görme, işitme veya okuma güçlüğü yaşayan kullanıcıların içeriğe erişimini kolaylaştırır.

## İçindekiler

- [Özellikler](#özellikler)
- [Sistem Mimarisi](#sistem-mimarisi)
- [Teknolojiler](#teknolojiler)
- [Klasör Yapısı](#klasör-yapısı)
- [Kurulum](#kurulum)
- [Ekip](#ekip)

## Özellikler

Platform dört yapay zeka modülünden oluşur:

- **Görsel Açıklama** — Paylaşılan görseldeki nesne, ortam ve önemli detayları analiz ederek Türkçe alternatif metin (alt text) oluşturur.
- **Otomatik Altyazı** — Videodaki konuşmayı metne çevirir, zaman kodlarını düzenler ve Türkçe altyazı üretir.
- **Sadeleştirme (NLP)** — Uzun veya karmaşık gönderileri özetler, daha sade bir Türkçeyle yeniden yazar ve metni seslendirmeye uygun hâle getirir.
- **Erişilebilirlik Kontrolü** — Renk kontrastı, yazı büyüklüğü, renk körlüğü uyumu ve okunabilirliği değerlendirerek bir erişilebilirlik puanı verir.

Tüm modüller, erişilebilir bir kullanıcı arayüzü (ekran okuyucu uyumu, klavye navigasyonu, yüksek kontrast, ölçeklenebilir yazı) üzerinden tek bir sistemde birleştirilir.

## Tasarım ve Arayüz (UI/UX)

- **Figma Tasarım Dosyası:** [Figma Tasarım Şablonu](https://www.figma.com/design/aNmnXW0srUldtlIRkjBoPe/233125013432---22DH114378---Tr%E1%BA%A7n-Th%E1%BB%8B-Ng%E1%BB%8Dc-Vy--Community-?node-id=9-47&t=lXy90I1TdTgpuIB1-1)
- **Geliştirilen Ekranlar:** Gönderi Akışı, Profil, Gönderi Paylaşımı (Erişilebilirlik Kontrolü ile birlikte).

## Sistem Mimarisi

Platform katmanlı bir mimariye sahiptir: kullanıcı arayüzü → backend (FastAPI) → yapay zeka modülleri → model/servis katmanı → veri katmanı. Detaylı şema ve veri akışı için [`mimari.md`](mimari.md) dosyasına bakınız.

## Teknolojiler

- **Backend:** Python, FastAPI
- **Veritabanı:** PostgreSQL / SQLite (PoC)
- **API:** REST (JSON)
- **Yapay Zeka:** Görüntü tanıma (Gemini/VLM), Konuşma tanıma (Whisper/ASR), Dil modeli (Metin sadeleştirme), Metin-Sesi (TTS)
- **Arayüz:** Erişilebilir Mobil Uyumlu Web Arayüzü (HTML5, CSS3, JS)

> Teknoloji seçimleri PoC aşamasında netleştirilmiştir.


## Klasör Yapısı

```
erisilebilir-destek/
├── README.md
├── docs/                    # Mimari ve dokümantasyon
│   └── mimari.md
├── backend/                 # FastAPI uygulaması, API gateway, orkestrasyon
├── api/                     # REST uç noktaları
├── database/                # Veritabanı modelleri ve şema
├── ai-modules/              # Yapay zeka modülleri
│   ├── image-description/   # Görsel açıklama
│   ├── captioning/          # Otomatik altyazı
│   ├── simplification/      # Sadeleştirme (NLP)
│   └── accessibility-check/ # Erişilebilirlik kontrolü
└── frontend/                # Erişilebilir kullanıcı arayüzü
```

## Kurulum

> Proje geliştirme aşamasındadır. Aşağıdaki adımlar backend iskeleti hazır olduğunda geçerli olacaktır.

```bash
# Depoyu klonla
git clone https://github.com/ORGANIZASYON-ADI/erisilebilir-destek.git
cd erisilebilir-destek

# Sanal ortam oluştur ve bağımlılıkları kur
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Backend'i çalıştır
uvicorn backend.main:app --reload
```

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
