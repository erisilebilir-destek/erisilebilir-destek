# N-04 – API ve Format Test Senaryoları

## 1. Testin Amacı ve Kapsamı

Bu test çalışmasının amacı, NSosyal platformuna entegre edilecek olan Erişilebilir Destek backend servisinin kullanıcı ve sistem kaynaklı hatalı veya zararlı girdilere karşı dayanıklılığını, veri doğrulama mekanizmalarını ve uç durum (edge case) güvenliğini doğrulamaktır.

**Test edilen modül:**
- FastAPI Backend
- `/api/v1/analyze` uç noktası
- Gönderi ve kullanıcı uç noktaları

**Kullanılan araçlar:**
- Python 3.13
- FastAPI TestClient
- Pytest
- io.BytesIO
- Geçici SQLite test veritabanı
- Geçici yükleme dizini

**GitHub test dosyası:**  
`backend/test_api_qa.py`

---

## 2. Test Senaryoları ve Sonuçları

| Test ID | Test Adı | Test Girişi | Beklenen Sonuç | Gerçekleşen Sonuç | Durum |
|---|---|---|---|---|---|
| TC-01 | Sistem Sağlığı (Health Check) | `GET /` | HTTP 200 OK dönmeli ve sistemin çalıştığı doğrulanmalıdır. | HTTP 200 OK yanıtı alındı ve sistemin çalıştığı doğrulandı. | ✅ PASS |
| TC-02 | Eksik/Yanlış Dosya Alanı | `file` alanıyla dosya gönderimi | API'nin beklediği `dosya` alanı bulunmadığı için HTTP 422 dönmelidir. | HTTP 422 yanıtı doğrulandı. | ✅ PASS |
| TC-03 | Boş Dosya Yükleme Kontrolü | `empty.png` – 0 Byte | Boş dosya kabul edilmemeli ve HTTP 400 dönmelidir. | HTTP 400 yanıtı ve boş dosya doğrulaması doğrulandı. | ✅ PASS |
| TC-04 | Desteklenmeyen Dosya Formatı | `malicious.exe` | Desteklenmeyen dosya türü reddedilmeli ve HTTP 415 dönmelidir. | HTTP 415 Unsupported Media Type yanıtı doğrulandı. | ✅ PASS |
| TC-05 | Dosya Boyutu Sınırı | Boyut sınırını aşan görsel | Boyut sınırı aşıldığında HTTP 413 dönmelidir. | HTTP 413 yanıtı doğrulandı. | ✅ PASS |
| TC-06 | Geçerli Görsel Yükleme | `ornek.jpg` | Görsel kabul edilmeli, analiz edilmeli ve erişilebilirlik çıktıları üretilmelidir. | HTTP 200 yanıtı alındı; görsel analiz akışı başarıyla tamamlandı. | ✅ PASS |
| TC-07 | Metin Yükleme ve Sadeleştirme | `metin.txt` | Metin kabul edilmeli ve metin işleme/sadeleştirme akışı çalışmalıdır. | HTTP 200 yanıtı alındı ve işlem türünün metin olduğu doğrulandı. | ✅ PASS |
| TC-08 | Video Yükleme ve Altyazı Oluşturma | `video.mp4` | Video kabul edilmeli ve `.vtt` altyazı dosyası oluşturulmalıdır. | HTTP 200 yanıtı alındı ve `.vtt` altyazı yolu oluşturuldu. | ✅ PASS |
| TC-09 | Dosya Adı Güvenliği / Dizin Atlatma | `../../kotucul.jpg` | Dosya yükleme klasörünün dışına çıkmamalı ve güvenli bir dosya yolu kullanılmalıdır. | Test sırasında oluşturulan yolun yükleme dizini sınırları içinde kalmadığı tespit edildi. | ❌ FAIL |
| TC-10 | Aynı İsimli Dosyaların Üzerine Yazılmaması | İki kez `ayni_ad.jpg` | İki yükleme için benzersiz dosya yolları oluşturulmalı ve dosyalar birbirini ezmemelidir. | İki yüklemenin aynı dosya yolunu kullandığı tespit edildi. | ❌ FAIL |
| TC-11 | Var Olmayan İçeriğin Yayınlanması | Geçersiz `content_id` | Var olmayan içerik yayınlanamamalı ve HTTP 404 dönmelidir. | HTTP 404 yanıtı doğrulandı. | ✅ PASS |
| TC-12 | Yayınlanan Gönderinin Akışta Görünmesi | Geçerli görsel ve yayınlama isteği | Yayınlanan gönderi `/api/v1/posts` akışında bulunmalıdır. | Yayınlanan içeriğin gönderi akışında bulunduğu doğrulandı. | ✅ PASS |
| TC-13 | Var Olmayan Kullanıcı Skoru | Geçersiz kullanıcı | Var olmayan kullanıcı için HTTP 404 dönmelidir. | HTTP 404 yanıtı doğrulandı. | ✅ PASS |

---

## 3. Test Sonuç Özeti

Toplam **13 test senaryosu** çalıştırılmıştır.

- ✅ **11 test PASS**
- ❌ **2 test FAIL**
- **Başarı oranı: %84,6**

Başarısız olan testler:

- **TC-09 – Dosya Adı Güvenliği / Dizin Atlatma**
- **TC-10 – Aynı İsimli Dosyaların Üzerine Yazılmaması**

Bu iki test, dosya saklama ve dosya adı yönetimi mekanizmasında iyileştirilmesi gereken noktalar bulunduğunu göstermektedir.

---

## 4. Kalite Güvence Değerlendirmesi ve Sonuç

**Sistem Kararlılığı:** Geliştirilen FastAPI backend mimarisi temel uç durumlarda başarılı sonuç vermiştir. Bununla birlikte gerçekleştirilen testlerde dosya adı güvenliği/dizin atlatma ve aynı isimli dosyaların birbirinin üzerine yazılmaması kontrollerinde iki hata tespit edilmiştir. Bu bulgular iyileştirilmesi gereken noktalar olarak değerlendirilmiştir.

**Güvenlik Doğrulaması:** Desteklenmeyen dosya formatı, boş dosya, dosya boyutu sınırı, eksik form alanı ve geçersiz içerik/kullanıcı gibi hata senaryoları backend seviyesinde başarıyla kontrol edilmiştir.

**Test Sonucu:** N-04 kapsamında toplam 13 test senaryosu çalıştırılmış; 11 test başarıyla geçmiş (PASS), 2 test başarısız olmuştur (FAIL). Başarısız olan senaryolar dosya adı güvenliği/dizin atlatma kontrolü ile aynı isimli dosyaların birbirinin üzerine yazılmaması kontrolleridir.

Bu sonuçlar doğrultusunda N-04 test çalışması, sistemin başarılı çalışan kontrollerini ve geliştirilmesi gereken iki dosya güvenliği alanını ortaya koymuştur.
