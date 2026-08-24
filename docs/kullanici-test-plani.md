# N-03 – Kullanıcı Test Planı ve Kabul Kriterleri

## 1. Testin Amacı

Bu kullanıcı testinin amacı, NSosyal Erişilebilir Destek prototipinde sunulan erişilebilirlik özelliklerinin kullanıcılar tarafından anlaşılabilir, kullanılabilir ve görev odaklı biçimde tamamlanabilir olup olmadığını değerlendirmektir.

Test kapsamında kullanıcıların içerik yükleme, görsel için alternatif metin oluşturma, video için otomatik altyazı oluşturma, karmaşık metni sadeleştirme, erişilebilirlik sonucunu inceleme ve yapay zekâ tarafından üretilen çıktıyı düzenleyip onaylama adımlarındaki deneyimleri gözlemlenecektir.

Kullanıcı performansı aşağıdaki ölçütler üzerinden değerlendirilecektir:

- Görev başarısı
- Görev tamamlama süresi
- Hata sayısı
- Yardım ihtiyacı
- Kullanıcı memnuniyeti ve kullanım kolaylığı

## 2. Test Kapsamı

Kullanıcı testi, NSosyal Erişilebilir Destek prototipinde içerik oluşturma ve erişilebilirlik desteği alma sürecinin temel adımlarını kapsamaktadır.

Test sırasında kullanıcıların aşağıdaki işlemleri gerçekleştirmesi beklenecektir:

- İçerik yükleme
- Görsel içerik için alternatif metin (alt-text) oluşturma
- Video içeriği için otomatik altyazı oluşturma
- Karmaşık bir metni sadeleştirme
- İçeriğin erişilebilirlik kontrolü sonucunu inceleme
- Yapay zekâ tarafından oluşturulan çıktıyı kontrol etme
- Gerekli gördüğü durumda çıktıyı düzenleme ve onaylama

## 3. Test Katılımcıları

Kullanıcı testlerinin, N-01 Hedef Kullanıcı ve Erişilebilirlik İhtiyacı Araştırması kapsamında belirlenen kullanıcı profilleri dikkate alınarak gerçekleştirilmesi planlanmaktadır.

Testlerde mümkün olduğunca farklı erişilebilirlik ihtiyaçlarını temsil eden kullanıcıların yer alması hedeflenmektedir:

- Ekran okuyucu kullanan görme engelli kullanıcı
- Az gören kullanıcı
- İşitme engelli veya az işiten kullanıcı
- Disleksi veya okuma güçlüğü yaşayan kullanıcı
- İçerik üreticisi / standart kullanıcı

## 4. Test Yöntemi

Kullanıcı testleri görev temelli kullanılabilirlik testi yöntemiyle gerçekleştirilecektir.

Her katılımcıya prototip üzerinde tamamlaması gereken belirli görevler verilecek ve katılımcının görevi mümkün olduğunca test yürütücüsünün müdahalesi olmadan tamamlaması beklenecektir.

Test sırasında aşağıdaki ölçümler kaydedilecektir:

- **Görev başarısı:** Başarılı / Kısmen başarılı / Başarısız
- **Tamamlama süresi:** Görevin başlangıcından tamamlanmasına kadar geçen süre
- **Hata sayısı:** Yanlış seçim, yanlış işlem veya görevi tamamlamayı engelleyen kullanıcı hatalarının sayısı
- **Yardım ihtiyacı:** Kullanıcının test yürütücüsünden yönlendirme isteyip istemediği
- **Memnuniyet / kullanım kolaylığı:** Görevler tamamlandıktan sonra 1–5 arasında verilen değerlendirme puanı

## 5. Kullanıcı Test Görevleri

Test sırasında katılımcılara prototipteki temel kullanıcı akışlarını temsil eden 10 görev verilecektir.

### Görev 1 – İçerik Yükleme
Kullanıcıdan erişilebilirlik açısından değerlendirmek istediği bir içeriği sisteme yüklemesi istenir.

### Görev 2 – Görsel Açıklaması Oluşturma
Kullanıcıdan yüklenen bir görsel için yapay zekâ destekli alternatif metin (alt-text) oluşturması istenir.

### Görev 3 – Görsel Açıklamasını Kontrol Etme ve Düzenleme
Kullanıcıdan oluşturulan alternatif metni incelemesi, gerekli görürse düzenlemesi ve çıktıyı onaylaması istenir.

### Görev 4 – Otomatik Altyazı Oluşturma
Kullanıcıdan yüklenen video içeriğindeki konuşmalar için otomatik altyazı oluşturması istenir.

### Görev 5 – Altyazıyı Kontrol Etme ve Düzenleme
Kullanıcıdan oluşturulan altyazıları incelemesi, gerekli gördüğü bir bölümü düzenlemesi ve sonucu onaylaması istenir.

### Görev 6 – Altyazı Çıktısı Alma
Kullanıcıdan oluşturulan altyazıyı SRT veya WebVTT formatlarından birinde çıktı olarak alması istenir.

### Görev 7 – Metin Sadeleştirme
Kullanıcıdan verilen karmaşık bir metni daha açık ve anlaşılır hâle getirmek için metin sadeleştirme özelliğini kullanması istenir.

### Görev 8 – Erişilebilirlik Kontrolü Yapma
Kullanıcıdan yüklediği içeriğin erişilebilirlik kontrolünü çalıştırması ve sistem tarafından verilen 0–100 erişilebilirlik puanını bulması istenir.

### Görev 9 – Erişilebilirlik Sorunlarını Belirleme
Kullanıcıdan erişilebilirlik kontrolü sonucunda sistemin tespit ettiği eksiklikleri incelemesi ve hangi alanların düzeltilmesi gerektiğini belirlemesi istenir.

### Görev 10 – Düzenleme ve Son Onay
Kullanıcıdan yapay zekâ tarafından oluşturulan çıktıları ve erişilebilirlik önerilerini inceleyerek gerekli son düzenlemeleri yapması ve içeriği onaylaması istenir.

## 6. Görev Bazlı Kabul Kriterleri

| Görev | Süre Kriteri | Hata Kriteri | Yardım Kriteri |
|---|---:|---:|---|
| 1. İçerik Yükleme | ≤ 60 sn | En fazla 1 hata | Yardım almadan |
| 2. Görsel Açıklaması Oluşturma | ≤ 60 sn | En fazla 1 hata | Yardım almadan |
| 3. Görsel Açıklamasını Düzenleme | ≤ 90 sn | En fazla 1 hata | Yardım almadan |
| 4. Otomatik Altyazı Oluşturma | ≤ 90 sn | En fazla 1 hata | Yardım almadan |
| 5. Altyazıyı Düzenleme | ≤ 120 sn | En fazla 2 hata | En fazla 1 yönlendirme |
| 6. Altyazı Çıktısı Alma | ≤ 60 sn | En fazla 1 hata | Yardım almadan |
| 7. Metin Sadeleştirme | ≤ 60 sn | En fazla 1 hata | Yardım almadan |
| 8. Erişilebilirlik Kontrolü | ≤ 60 sn | En fazla 1 hata | Yardım almadan |
| 9. Erişilebilirlik Sorunlarını Belirleme | ≤ 90 sn | En fazla 1 hata | Yardım almadan |
| 10. Düzenleme ve Son Onay | ≤ 120 sn | En fazla 2 hata | En fazla 1 yönlendirme |

> **Not:** Otomatik altyazının sistem tarafından işlenme süresi kullanıcı performansından ayrı değerlendirilecektir. Süre kriteri, kullanıcının ilgili işlevi bulması ve işlemi doğru şekilde başlatması için geçen süreyi ifade eder.

## 7. Kullanıcı Değerlendirmesi

Görevlerin tamamlanmasının ardından kullanıcı deneyimi ve prototipin kullanılabilirliği aşağıdaki konular üzerinden değerlendirilecektir:

- İçerik yükleme işleminin kullanım kolaylığı
- Alternatif metin oluşturma özelliğinin bulunabilirliği ve kullanım kolaylığı
- Alternatif metnin düzenlenip onaylanmasının anlaşılabilirliği
- Otomatik altyazı oluşturma ve düzenleme işlemlerinin kullanım kolaylığı
- SRT veya WebVTT altyazı çıktısının anlaşılabilirliği
- Metin sadeleştirme özelliğinin kullanım ve sonuçlarının anlaşılabilirliği
- 0–100 erişilebilirlik puanının anlaşılabilirliği
- Erişilebilirlik sorunları ve düzeltme önerilerinin anlaşılabilirliği
- Genel kullanım kolaylığı
- Kullanıcının zorlandığı veya değiştirilmesini istediği alanlar

## 8. Genel Kabul Kriterleri

Prototipin kullanılabilirlik açısından başarılı kabul edilebilmesi için aşağıdaki başlangıç eşikleri belirlenmiştir:

- **Görev başarı oranı:** Temel görevlerin en az %80'inin kullanıcılar tarafından başarıyla tamamlanması
- **Bağımsız kullanım:** Görevlerin en az %80'inin test yürütücüsünün yönlendirmesi olmadan tamamlanması
- **Hata oranı:** Görev başına ortalama 2'den fazla kritik olmayan hata yapılmaması ve görevin tamamlanmasını engelleyen kritik hataların tekrarlanmaması
- **Kullanım kolaylığı:** 1–5 ölçekli değerlendirmelerde genel kullanım kolaylığı puanının ortalama en az 4/5 olması
- **Anlaşılabilirlik:** Alt-text, altyazı, sadeleştirme ve erişilebilirlik sonuçlarına ilişkin değerlendirmelerde kullanıcıların en az %80'inin “Evet” yanıtını vermesi
- **Erişilebilirlik puanının anlaşılması:** Kullanıcıların en az %80'inin 0–100 erişilebilirlik puanının içeriğin erişilebilirlik durumunu gösterdiğini doğru biçimde anlaması
- **Kritik kullanılabilirlik problemi:** Bir kullanıcının temel bir görevi tamamlamasını tamamen engelleyen ve birden fazla katılımcıda tekrarlanan kritik kullanılabilirlik sorununun bulunmaması

## 9. Test Sonuçlarının Kaydedilmesi

Her katılımcının görev bazlı performansı aşağıdaki bilgiler kullanılarak kayıt altına alınacaktır:

| Katılımcı | Görev No | Sonuç | Süre | Hata Sayısı | Yardım İhtiyacı | Gözlem / Not |
|---|---|---|---|---|---|---|
| K1 | G1 |  |  |  |  |  |
| K1 | G2 |  |  |  |  |  |
| K1 | G3 |  |  |  |  |  |
| K1 | G4 |  |  |  |  |  |
| K1 | G5 |  |  |  |  |  |
| K1 | G6 |  |  |  |  |  |
| K1 | G7 |  |  |  |  |  |
| K1 | G8 |  |  |  |  |  |
| K1 | G9 |  |  |  |  |  |
| K1 | G10 |  |  |  |  |  |

## 10. Test Uygulama Prosedürü

Kullanıcı testlerinin tüm katılımcılar için mümkün olduğunca aynı koşullarda uygulanması hedeflenmektedir.

1. **Test öncesi bilgilendirme:** Katılımcıya testin amacı ve yaklaşık uygulama süreci açıklanır.
2. **Başlangıç hazırlığı:** Prototip başlangıç ekranında hazır hâle getirilir. Katılımcının ihtiyaç duyduğu ekran okuyucu, büyütme veya benzeri yardımcı teknolojileri kullanmasına izin verilir.
3. **Görevlerin verilmesi:** Belirlenen görevler katılımcıya tek tek verilir.
4. **Müdahalesiz gözlem:** Test yürütücüsü kullanıcının izlediği yolu gözlemler ancak mümkün olduğunca müdahale etmez.
5. **Performans kaydı:** Her görev için başarı durumu, tamamlama süresi, hata sayısı, yardım ihtiyacı ve önemli kullanıcı davranışları kayıt altına alınır.
6. **Kullanıcı değerlendirmesi:** Görevler tamamlandıktan sonra kullanıcı değerlendirme soruları katılımcıya yöneltilir.
7. **Sonuçların değerlendirilmesi:** Sonuçlar görev bazlı ve genel kabul kriterleriyle karşılaştırılır. Kabul kriterlerini karşılamayan veya birden fazla kullanıcıda tekrarlanan sorunlar prototipte iyileştirilmesi gereken alanlar olarak kayıt altına alınır.
