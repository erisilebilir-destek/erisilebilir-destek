# N-04 – API ve Format Test Senaryoları

## 1. Testin Amacı ve Kapsamı

Bu test çalışmasının amacı, NSosyal platformuna entegre edilecek olan Erişilebilir Destek backend servisinin kullanıcı ve sistem kaynaklı hatalı veya zararlı girdilere karşı dayanıklılığını, veri doğrulama mekanizmalarını ve uç durum güvenliğini doğrulamaktır.

Test edilen modül:

- FastAPI Backend
- `/api/v1/analyze` uç noktası

Kullanılan araçlar:

- Python 3.13
- FastAPI TestClient
- Pytest
- io.BytesIO

GitHub test dosyası:

`backend/test_api_qa.py`

## 2. Test Senaryoları ve Sonuçları

| Test ID | Test Adı | Test Girişi | Beklenen Sonuç | Gerçekleşen Sonuç | Durum |
|---|---|---|---|---|---|
| TC-01 | Sistem Sağlığı (Health Check) | GET `/` | HTTP 200 OK yanıtı alınmalı ve sistemin aktif olduğu doğrulanmalıdır. | HTTP 200 OK yanıtı alındı. Sistem aktif olarak yanıt verdi. | ✅ PASS |
| TC-02 | Boş Dosya Yükleme Kontrolü | `empty_file.png` – 0 Byte | Sistem çökmemeli ve boş dosya girişini reddeden uygun bir hata yanıtı döndürmelidir. | HTTP 422 Unprocessable Entity yanıtı alındı. Sistem boş dosyayı güvenli şekilde reddetti. | ✅ PASS |
| TC-03 | Desteklenmeyen Dosya Formatı | `malicious.exe` | Sistem desteklenmeyen dosya formatını kabul etmemeli ve uygun bir hata yanıtı döndürmelidir. | HTTP 400 Bad Request yanıtı alındı. Sistem `.exe` formatındaki dosyayı reddetti. | ✅ PASS |
| TC-04 | Geçerli Görsel Yükleme | `valid_image.png` | Sistem görsel dosyasını kabul etmeli ve analiz işlemini başarıyla gerçekleştirmelidir. | HTTP 200 OK yanıtı alındı. Görsel başarıyla kabul edildi ve analiz işlemi gerçekleştirildi. | ✅ PASS |
| TC-05 | Boş Metin Girdisi Kontrolü | Boş metin `""` | Sistem boş metin girdisini kabul etmemeli ve uygun bir doğrulama hatası döndürmelidir. | HTTP 422 Unprocessable Entity yanıtı alındı. Sistem boş metin girdisini reddetti. | ✅ PASS |

## 3. Kalite Güvence Değerlendirmesi

### Sistem Kararlılığı

Geliştirilen FastAPI backend mimarisi, boş dosya, desteklenmeyen uzantı ve geçersiz parametre gibi uç durumlarda sunucu çökmesi yaşamadan kontrollü HTTP hata yanıtları üretmiştir.

### Güvenlik Doğrulaması

Desteklenmeyen `.exe` ve hatalı medya formatları backend seviyesinde filtrelenmiştir.

### Test Sonucu

N-04 görevi kapsamında raporlanan test senaryolarının tamamı başarıyla sonuçlanmıştır.

Resmî test paketi repository içerisinde aşağıdaki dosyada bulunmaktadır:

`backend/test_api_qa.py`

## 4. Çalıştırma

Test paketi aşağıdaki komut ile çalıştırılabilir:

```bash
pytest -q
