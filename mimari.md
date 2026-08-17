# Sistem Mimarisi — Erişilebilir Destek

Bu belge, **Erişilebilir Destek** platformunun backend ve entegrasyon mimarisini tanımlar.
Platform; paylaşılan görsel, video ve metin içeriklerini yapay zeka modülleriyle işleyerek
erişilebilir çıktılar (Türkçe alt metin, altyazı, sade metin, erişilebilirlik puanı) üretir.

## Katmanlı mimari şeması

```mermaid
flowchart TB
    subgraph client["KULLANICI KATMANI"]
        UI["Erisilebilir Web Arayuzu<br/>Ekran okuyucu uyumlu - klavye navigasyonu<br/>yuksek kontrast - olceklenebilir yazi"]
    end

    subgraph backend["BACKEND KATMANI - FastAPI"]
        GW["API Gateway<br/>REST uc noktalari"]
        AUTH["Kimlik Dogrulama<br/>JWT / oturum yonetimi"]
        ORCH["Orkestrasyon Servisi<br/>istek yonlendirme - modul cagrisi<br/>sonuclarin birlestirilmesi"]
    end

    subgraph ai["YAPAY ZEKA MODULLERI"]
        M1["1 - Gorsel Aciklama<br/>nesne/ortam analizi<br/>Turkce alt metin"]
        M2["2 - Otomatik Altyazi<br/>konusma-metin - zaman kodu<br/>Turkce altyazi"]
        M3["3 - Sadelestirme NLP<br/>ozetleme - sade Turkce<br/>seslendirmeye hazirlama"]
        M4["4 - Erisilebilirlik Kontrolu<br/>kontrast - yazi boyutu - renk korlugu<br/>okunabilirlik puani"]
    end

    subgraph models["MODEL / SERVIS KATMANI"]
        VIS["Goruntu Tanima<br/>vision / captioning"]
        STT["Konusma Tanima<br/>STT"]
        LLM["Dil Modeli<br/>ozet / sadelestirme"]
        TTS["Metin-Sesi<br/>TTS"]
    end

    subgraph data["VERI KATMANI"]
        DB[("PostgreSQL<br/>kullanici - icerik - sonuc kayitlari")]
        STORE[("Dosya / Nesne Depolama<br/>gorsel - video - ses")]
    end

    UI -->|"HTTPS - REST"| GW
    GW --> AUTH
    GW --> ORCH
    ORCH --> M1
    ORCH --> M2
    ORCH --> M3
    ORCH --> M4
    M1 --> VIS
    M2 --> STT
    M3 --> LLM
    M3 --> TTS
    M4 --> LLM
    M1 -.->|"medya oku/yaz"| STORE
    M2 -.->|"medya oku/yaz"| STORE
    ORCH -->|"kayit/okuma"| DB
    ORCH -->|"sonuc - JSON"| GW
    GW -->|"erisilebilir cikti"| UI
```

## Veri akışı

1. **İstek** — Kullanıcı, erişilebilir arayüzden bir görsel, video veya metin gönderir. İstek HTTPS üzerinden backend'in API Gateway'ine ulaşır.
2. **Doğrulama & yönlendirme** — Kimlik doğrulama (JWT) geçilir; Orkestrasyon Servisi isteğin türüne göre onu ilgili yapay zeka modülüne yönlendirir.
3. **İşleme** — İlgili modül, altındaki modeli (görüntü tanıma, STT, dil modeli, TTS) çağırarak Türkçe çıktıyı üretir; medya dosyaları depolamadan okunur/yazılır.
4. **Birleştirme & kayıt** — Orkestrasyon, modül çıktısını toparlar, sonucu PostgreSQL'e kaydeder ve JSON olarak Gateway'e döndürür.
5. **Erişilebilir çıktı** — Gateway sonucu arayüze iletir; kullanıcı alt metni, altyazıyı, sade metni veya erişilebilirlik puanını erişilebilir biçimde görür.

## Teknoloji notu

Backend **FastAPI (Python)**, veritabanı **PostgreSQL** olarak planlanmıştır. Yapay zeka modülleri
backend'den bağımsız servisler olarak konumlanır; ortak bir **API sözleşmesiyle** (girdi/çıktı formatı)
Orkestrasyon Servisine bağlanır. Böylece her modül ayrı geliştirilip tek sistemde birleştirilir.

> Bu şema başlangıç mimarisidir; teknoloji seçimleri PoC aşamasında (20 Ağustos) netleştirilecektir.
