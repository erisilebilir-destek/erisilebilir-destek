# N-04 – API ve Format Test Senaryoları

## 1. Testin Amacı ve Kapsamı

Bu test çalışmasının amacı; NSosyal platformuna entegre edilecek olan
“Erişilebilir Destek” backend servisinin, kullanıcı ve sistem kaynaklı
hatalı veya zararlı girdilere karşı dayanıklılığını, veri doğrulama
(validation) mekanizmalarını ve uç durum (edge case) güvenliğini
doğrulamaktır.

### Test Bilgileri

- **Test Edilen Modül:** FastAPI Backend
- **Test Edilen Uç Nokta:** `/api/v1/analyze`
- **Kullanılan Araçlar:** Python 3.13, FastAPI TestClient, Pytest, io.BytesIO
- **GitHub Test Dosyası:** `test_api_qa.py`

## 2. Test Senaryoları ve Sonuçları

| Test ID | Test Adı | Test Girdisi | Beklenen Sonuç | Gerçekleşen Sonuç | Durum |
|---|---|---|---|---|---|
| TC-01 | Eksik/Yanlış Dosya Alanı Kontrolü | `file` alanı ile görsel | HTTP 422 Unprocessable Entity | Yanlış form alanı API tarafından reddedildi ve beklenen HTTP 422 yanıtı doğrulandı. | ✅ PASS |
| TC-02 | Boş Dosya Yükleme Kontrolü | `empty.png` (0 byte) | HTTP 400 ve dosyanın boş olduğunu belirten hata mesajı | Boş dosya reddedildi; HTTP 400 ve hata kontrolü doğrulandı. | ✅ PASS |
| TC-03 | Geçerli Görsel Yükleme | `ornek.jpg` | HTTP 200; `gorsel` işlem türü, `gorsel_aciklama` modülü, alt-text ve 0–100 arası erişilebilirlik puanı | Görsel başarıyla analiz edildi ve beklenen çıktı alanları doğrulandı. | ✅ PASS |
| TC-04 | Desteklenmeyen Dosya Formatı | `malicious.exe` | HTTP 415 Unsupported Media Type | Desteklenmeyen dosya formatı reddedildi ve HTTP 415 doğrulandı. | ✅ PASS |
| TC-05 | Dosya Boyutu Sınırı | Boyut sınırını aşan görsel | HTTP 413 Payload Too Large | Boyut sınırını aşan dosya reddedildi ve HTTP 413 doğrulandı. | ✅ PASS |

## 3. Kalite Güvence Değerlendirmesi

### Sistem Kararlılığı

FastAPI backend servisi; yanlış dosya alanı, boş dosya,
desteklenmeyen dosya formatı ve dosya boyutu sınırı gibi temel uç
durumlarda beklenen HTTP yanıtlarını üretmiş ve hatalı girdileri
kontrollü şekilde reddetmiştir.

### Güvenlik ve Doğrulama

Desteklenmeyen `.exe` formatı backend seviyesinde başarıyla
filtrelenmiştir. Boş dosya, boyut sınırını aşan dosya ve yanlış form
alanı gibi geçersiz girdiler beklenen hata kodlarıyla karşılanmıştır.

## 4. Test Sonucu

N-04 kapsamında raporlanan **5 temel test senaryosunun tamamı
başarıyla sonuçlanmıştır (PASS).**

Geçerli JPEG görsel yükleme senaryosunda analiz işlemi başarıyla
tamamlanmış ve beklenen çıktı alanları doğrulanmıştır.

**Toplam Sonuç: 5/5 PASS ✅**
