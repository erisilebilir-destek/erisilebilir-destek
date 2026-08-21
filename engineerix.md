# NSosyal Erişilebilir Destek Projesi (Engineerix Takımı)

## 1. Projenin Kısa Tanımı

NSosyal Erişilebilir Destek; sosyal medya içeriklerinin görme, işitme, okuma ve anlama güçlüğü yaşayan kullanıcılar için daha erişilebilir hâle getirilmesini amaçlayan yapay zekâ destekli bir içerik asistanıdır.

Sistem, içerik üreticisinin hazırladığı gönderiyi paylaşılmadan önce analiz eder. Görsel, video ve metin içeriklerinde erişilebilirlik eksiklerini tespit ederek kullanıcıya otomatik öneriler sunar.

Sistem temel olarak:

* Görseller için Türkçe alternatif metin üretir.
* Videolardaki konuşmaları yapay zekâ (ASR) desteğiyle otomatik Türkçe altyazıya dönüştürerek W3C standardında WebVTT (.vtt) ve SRT formatlarında hazırlar.
* Karmaşık metinlerin daha anlaşılır bir sürümünü hazırlar.
* Renk kontrastı ve okunabilirliği kontrol ederek altyazılarda standart "opak siyah blok üstüne beyaz yazı" kuralını uygular.
* İçerik üreticilerini teşvik etmek amacıyla içeriğe 100 üzerinden erişilebilirlik puanı veren bir oyunlaştırma (oyun) sistemi sunar.
* Eksiklerin nasıl düzeltilebileceğini açıklar.
* İçerik üreticisinin önerileri düzenleyip onaylamasını sağlar.

Amaç, erişilebilirlik sorumluluğunu tamamen içerik üreticisinin teknik bilgisine bırakmadan, paylaşım sürecinin doğal bir parçası hâline getirmektir.

---

## 2. Problem Tanımı

Sosyal medya platformlarındaki içeriklerin önemli bir bölümü görsel, video ve metinlerden oluşmaktadır. Ancak bu içerikler her kullanıcı için aynı ölçüde erişilebilir değildir.

Örneğin:

* Görme engelli bir kullanıcı, görsele alternatif metin eklenmemişse içeriğin ne anlattığını anlayamayabilir.
* İşitme engelli bir kullanıcı, altyazısı bulunmayan videodaki konuşmaları takip edemeyebilir.
* Disleksi, bilişsel güçlük veya düşük dijital okuryazarlık yaşayan kullanıcılar, uzun ve karmaşık metinleri anlamakta zorlanabilir.
* Düşük renk kontrastı, küçük yazı boyutu ve karmaşık arayüzler içeriğin okunmasını zorlaştırabilir.
* İçerik üreticileri erişilebilirlik kurallarını bilseler bile her gönderiyi manuel olarak kontrol edecek zamana veya teknik bilgiye sahip olmayabilir.

Mevcut sistemlerde alternatif metin ve altyazı özellikleri bulunabilmektedir. Ancak bunlar çoğunlukla kullanıcının manuel olarak etkinleştirmesine veya içerik üreticisinin doğru şekilde hazırlamasına bağlıdır.

Bu nedenle temel problem şudur:

> Sosyal medya içerik üreticilerinin, paylaşım sırasında erişilebilirlik eksiklerini kolayca tespit edebilecekleri ve düzeltebilecekleri bütünleşik, Türkçe ve yapay zekâ destekli bir sisteme ihtiyaç duyulmaktadır.

---

## 3. Projenin Amacı

Projenin temel amacı, NSosyal’de üretilen içeriklerin daha fazla kullanıcı tarafından bağımsız ve eşit şekilde tüketilebilmesini sağlamaktır.

Alt amaçlar:

* İçerik üreticilerine erişilebilirlik konusunda rehberlik etmek
* Erişilebilir içerik hazırlama süresini azaltmak
* Türkçe içerikler için yapay zekâ desteği sunmak
* Görsel, video ve metin erişilebilirliğini tek sistemde birleştirmek
* Kullanıcıları erişilebilir içerik üretmeye teşvik etmek
* NSosyal’in kapsayıcı ve kullanıcı odaklı bir platform olarak gelişmesine katkı sağlamak
* Erişilebilirliği sonradan yapılan bir düzeltme değil, içerik üretim sürecinin bir parçası hâline getirmek

---

## 4. Projenin Hitap Ettiği Yarışma Alanları

Proje temel olarak iki yarışma temasına hitap etmektedir:

### Sosyal Yapay Zekâ

* Görsel açıklama üretimi
* Konuşmayı metne dönüştürme
* Metin sadeleştirme
* İçerik analizi
* Yapay zekâ destekli öneri oluşturma

### Kullanıcı Katılımı ve UI/UX

* Erişilebilir gönderi oluşturma deneyimi
* İçerik üreticisine gerçek zamanlı yönlendirme
* Renk ve okunabilirlik kontrolü
* Kullanıcıya açıklanabilir öneriler sunulması
* Farklı kullanıcı ihtiyaçlarına göre kişiselleştirme

Bu nedenle projeyi yalnızca “engelli bireylere yönelik bir araç” şeklinde anlatmamalıyız. Proje, NSosyal’deki bütün içerik üreticilerinin daha kapsayıcı içerik üretmesini sağlayan platform özelliğidir.

---

## 5. Hedef Kitle

### Birincil hedef kitle

* Görme engelli ve az gören kullanıcılar
* İşitme engelli ve işitme güçlüğü yaşayan kullanıcılar
* Disleksi yaşayan kullanıcılar
* Bilişsel veya öğrenme güçlüğü yaşayan kullanıcılar
* Yaşlı kullanıcılar
* Düşük dijital okuryazarlığa sahip kullanıcılar

### İkincil hedef kitle

* NSosyal içerik üreticileri (Bireysel kullanıcılar, influencer'lar ve marka yöneticileri)
* Kurumsal hesaplar
* Kamu kurumları
* Belediyeler
* Eğitim kurumları
* Haber ve medya hesapları
* Sosyal sorumluluk toplulukları
* Markalar ve profesyonel içerik ekipleri

#### İçerik Üreticilerinin Rolü ve Oyunlaştırma (Teşvik) Sistemi:
Yapay zekâ otomatik olarak alternatif metin ve altyazı üretse de, hataları (halüsinasyonları) önlemek için son onay içerik üreticisindedir. Geliştirilen 100 puanlık oyunlaştırma sistemi, içerik üreticisinin erişilebilirlik bilincini artırmayı ve süreci eğlenceli hale getirmeyi hedefler. İçerik üreticileri, paylaşımlarını erişilebilir kıldıkça puan kazanır, profillerinde erişilebilirlik rozetleri sergileyebilir ve platform içinde organik erişim avantajı elde eder.

### Dolaylı faydalanıcılar

* Sessiz ortamda video izleyen kullanıcılar
* Türkçe öğrenen kişiler
* Karmaşık metinleri hızlı anlamak isteyen kullanıcılar
* Düşük internet hızında video yerine metin okumayı tercih eden kişiler
* Arama motorları ve platform içi arama sistemleri

---

## 6. Temel Kullanıcı Senaryosu

Bir kullanıcı NSosyal’de görsel ve video içeren bir gönderi hazırlamaktadır.

1. Kullanıcı metnini yazar, görselini veya videosunu yükler.
2. “Erişilebilirliği Kontrol Et” seçeneğine basar.
3. Sistem içeriği analiz eder.
4. Görsel için Türkçe alternatif metin oluşturur.
5. Videodaki konuşmayı altyazıya dönüştürür.
6. Metnin okunabilirliğini ve karmaşıklığını kontrol eder.
7. Renk kontrastı ve görsel okunabilirlik sorunlarını belirler.
8. İçeriğe 100 üzerinden erişilebilirlik puanı verir.
9. Eksik alanları ve düzeltme önerilerini kullanıcıya gösterir.
10. Kullanıcı önerileri kabul eder, düzenler veya reddeder.
11. İçerik erişilebilir hâliyle yayımlanır.

Önemli nokta: Sistem içeriği kullanıcıdan habersiz değiştirmeyecek. Son karar her zaman içerik üreticisinde olacak.

---

## 7. Projenin Ana Modülleri

### 7.1. Görsel alternatif metin modülü

Bu modül, kullanıcının yüklediği görseli analiz ederek ekran okuyucular tarafından okunabilecek Türkçe bir açıklama oluşturur.

Örnek görsel:
> Bir parkta çizgi izleyen robot aracı test eden üç öğrenci

Sistemin üreteceği alternatif metin:
> “Açık havadaki bir parkta, yerdeki siyah çizgiyi takip eden dört tekerlekli robot aracı inceleyen üç öğrenci.”

#### Modülün yapacakları
* Görseldeki temel nesneleri belirleme
* İnsan, ortam ve eylemleri algılama
* Görselin ana bağlamını çıkarma
* Kısa ve anlaşılır Türkçe açıklama üretme
* Kullanıcıya açıklamayı düzenleme imkânı sunma

#### İlk prototipte yapılması gereken
Hazır bir görsel-dil modeli kullanılabilir. İlk aşamada sıfırdan model eğitmeye gerek yoktur. Önemli olan, çalışan bir prototip ve Türkçe çıktı gösterebilmektir.

#### Tamamlanma ölçütü
* En az 10 farklı görsel test edilmeli.
* Modelin açıklaması ile insan tarafından hazırlanan açıklama karşılaştırılmalı.
* Yanlış veya gereksiz detaylar kaydedilmeli.
* Kullanıcı üretilen açıklamayı düzenleyebilmeli.

---

### 7.2. Otomatik Türkçe altyazı modülü

Bu modül, videodaki konuşmaları otomatik ses tanıma (ASR - Automatic Speech Recognition) teknolojisi ile analiz ederek Türkçe altyazı oluşturur.

#### Modülün yapacakları
* Videodan sesi ayırma (FFmpeg ve Python kütüphaneleri ile).
* Konuşmayı ASR (Whisper) modeliyle metne dönüştürme ve kelime bazlı zaman kodu çıkarma.
* Altyazıyı W3C yerleşik standardı olan WebVTT (.vtt) ve genel kullanım için SRT formatlarında kaydetme.
* Altyazıyı kullanıcıya gösterme ve hatalı kelimeleri (özel isimler vb.) kolayca düzeltmesini sağlayan inline düzenleyici arayüzü sunma.

#### Kullanılabilecek araçlar
* Whisper
* FFmpeg
* Python
* Google Colab

#### Tamamlanma ölçütü
* Temiz sesli bir videoda altyazı oluşturulmalı.
* Gürültülü bir videoda da sistem denenmeli.
* Çıkan metin ile gerçek konuşma karşılaştırılmalı.
* Altyazı düzenlenebilir olmalı.
* En az üç farklı video formatı test edilmeli.

---

### 7.3. Metin sadeleştirme modülü

Bu modül, uzun ve karmaşık sosyal medya metinlerinin daha anlaşılır bir alternatifini oluşturur.

Örnek orijinal metin:
> “Erişilebilirlik standartlarının bütünsel biçimde uygulanması, platformların kullanıcı deneyimini sürdürülebilir şekilde geliştirmesine katkı sağlamaktadır.”

Sadeleştirilmiş metin:
> “Erişilebilirlik kurallarının uygulanması, sosyal medya platformlarının herkes için daha kolay kullanılmasını sağlar.”

#### Modülün yapacakları
* Uzun cümleleri tespit etme
* Karmaşık kelimeleri belirleme
* Daha kısa cümleler önerme
* Ana anlamı koruma
* İçerik üreticisine orijinal ve sade metni karşılaştırmalı gösterme

#### Önemli sınır
Sistem metnin anlamını, hukuki niteliğini veya önemli teknik detaylarını değiştirmemelidir. Özellikle resmî açıklamalarda kullanıcı onayı olmadan otomatik değişiklik yapılmamalıdır.

---

### 7.4. Renk kontrastı ve okunabilirlik modülü

Bu modül, gönderide kullanılan metin ve arka plan renklerini erişilebilirlik açısından kontrol eder ve altyazıların görsel okunabilirliğini artırır.

#### Kontrol edilecek noktalar
* Metin ve arka plan arasındaki kontrast (WCAG Level AA kontrast uyumu).
* Altyazıların arka planda kaybolmasını engellemek için varsayılan olarak **"opak siyah blok üstüne beyaz yazı"** standardının uygulanması.
* Kullanıcının arayüzden altyazı yazı boyutunu ve konumunu ayarlayabilmesi.
* Çok uzun paragraf kullanımı ve tamamı büyük harfle yazılmış metinlerin okunabilirlik denetimi.
* Görsel üzerine yerleştirilen yazıların okunabilirliği, bağlantı ve butonların ayırt edilebilirliği.

#### Sistem çıktısı
> “Görseldeki beyaz yazı ile açık pembe arka plan arasındaki kontrast düşük. Yazıyı koyulaştırmanız önerilir.”

Bu modül başlangıçta yapay zekâ yerine kural tabanlı olarak geliştirilebilir. Böylece daha hızlı ve güvenilir sonuç alınabilir.

---

### 7.5. Erişilebilirlik puanlama modülü

Sistem, her içeriği 100 üzerinden değerlendirer.

| Ölçüt | Puan |
| :--- | ---: |
| Görsel alternatif metni | 25 |
| Video altyazısı | 25 |
| Renk kontrastı | 20 |
| Metin okunabilirliği | 15 |
| Sade ve anlaşılır dil | 15 |
| **Toplam** | **100** |

Örnek sonuç:
> Erişilebilirlik puanı: 65/100
> Görsel açıklaması hazır. Videoda altyazı bulunmuyor. Metnin iki cümlesi gereğinden uzun. Renk kontrastı yeterli.

Puanın amacı kullanıcıyı cezalandırmak değil, eksikleri görünür hâle getirmek olmalıdır.

---

## 8. Projenin Özgün Yönü

Projenin özgünlüğü tek tek kullanılan teknolojilerden değil, bu teknolojilerin NSosyal paylaşım sürecinde birleştirilmesinden gelmektedir.

Farklılaştırıcı özellikler:
* Görsel, video, metin ve tasarım erişilebilirliğini tek sistemde birleştirmesi
* Türkçe odaklı çalışması
* İçeriği yayımlandıktan sonra değil, paylaşılmadan önce kontrol etmesi
* Kullanıcıya yalnızca hata göstermeyip çözüm üretmesi
* Açıklanabilir öneriler sunması
* İçerik üreticisinin kontrolünü koruması
* Erişilebilirliği puanlayarak gelişimi görünür hâle getirmesi
* NSosyal’in gönderi oluşturma akışına doğrudan entegre edilebilmesi

Projenin en güçlü mesajı şu olabilir:
> “Erişilebilirlik sonradan eklenen bir özellik değil, içerik üretiminin doğal bir parçasıdır.”

---

## 9. Teknik Mimari

Sistem beş temel katmandan oluşabilir.

### 9.1. Kullanıcı arayüzü
Kullanıcının:
* Metin yazdığı
* Görsel veya video yüklediği
* Erişilebilirlik kontrolünü başlattığı
* Önerileri gördüğü
* Sonuçları düzenlediği
* İçeriği yayımladığı
ekrandır.

### 9.2. Backend ve API
Backend:
* Kullanıcıdan gelen dosyaları alır.
* Dosya türünü kontrol eder.
* İçeriği ilgili yapay zekâ modülüne gönderir.
* Modüllerden gelen sonuçları birleştirir.
* Erişilebilirlik puanını hesaplar.
* Sonucu arayüze gönderir.

Kullanılabilecek teknolojiler:
* Python
* FastAPI veya Flask
* REST API
* SQLite veya PostgreSQL
* GitHub

### 9.3. Yapay zekâ servisleri
* Görsel açıklama modeli
* Konuşmayı metne dönüştürme modeli
* Metin sadeleştirme modeli
* Gerekirse Türkçe dil modeli

### 9.4. Kural tabanlı erişilebilirlik motoru
* Kontrast kontrolü
* Yazı boyutu kontrolü
* Alternatif metin kontrolü
* Altyazı bulunma kontrolü
* Okunabilirlik kontrolü
* Puan hesaplama

### 9.5. Sonuç ve öneri katmanı
Farklı modüllerden gelen sonuçlar tek bir panelde gösterilir:
* Erişilebilirlik puanı
* Tespit edilen eksikler
* Otomatik öneriler
* Kabul et/düzenle/reddet seçenekleri

---

## 10. Veri Güvenliği ve Etik İlkeler

Proje erişilebilirlik sağlamaya çalışırken kullanıcı gizliğini ihlal etmemelidir.

Temel ilkeler:
* Yüklenen içerikler kullanıcı izni olmadan model eğitimi için kullanılmamalıdır.
* İçerikler gereğinden uzun süre saklanmamalıdır.
* Kullanıcıya hangi verinin neden işlendiği açıklanmalıdır.
* Yapay zekâ çıktıları kesin doğruymuş gibi gösterilmemelidir.
* Kullanıcı, öneriyi değiştirebilmeli veya reddedebilmelidir.
* Yanlış görsel açıklamalarının oluşturabileceği riskler belirtilmelidir.
* Özel veya hassas içeriklerde ek uyarı mekanizması bulunmalıdır.
* Mümkün olan modüllerde cihaz üzerinde çalışma gelecekte değerlendirilmelidir.

---

## 11. MVP Kapsamı

İlk sürümde bütün özellikleri kusursuz geliştirmeye çalışmak riskli olur. Yarışma için çalışan en küçük ürün şu dört özelliğe odaklanmalıdır:

1. Görsel yükleme ve Türkçe alternatif metin üretme
2. Kısa video yükleme ve Türkçe altyazı oluşturma
3. Basit erişilebilirlik kontrolü
4. Erişilebilirlik puanı ve düzeltme önerileri

Metin sadeleştirme modülü hazır bir dil modeliyle eklenebilir; ancak zaman yetersiz kalırsa ikinci aşamaya bırakılabilir.

### MVP’de bulunması gereken ekranlar
* Gönderi oluşturma ekranı
* İçerik yükleme alanı
* “Erişilebilirliği Kontrol Et” butonu
* Analiz sonucu ekranı
* Alternatif metin düzenleme alanı
* Altyazı düzenleme alanı
* Erişilebilirlik puanı
* Önerileri kabul et/düzenle seçenekleri
* Son gönderi ön izlemesi

---

## 12. Prototipin Gösterim Senaryosu

Final demosunda karmaşık bir anlatım yerine tek gönderi üzerinden bütün sistem gösterilebilir.

### Demo öncesi içerik
* Alternatif metni olmayan bir görsel
* Altyazısı olmayan kısa bir video
* Uzun ve karmaşık bir açıklama
* Kontrastı düşük bir yazı

### Demo akışı
1. Kullanıcı içeriği yükler.
2. Sistem başlangıç puanını düşük gösterir.
3. Görsel için alternatif metin üretir.
4. Videoya altyazı oluşturur.
5. Metnin sade hâlini önerir.
6. Kontrast sorununu işaretler.
7. Kullanıcı önerileri kabul eder.
8. Erişilebilirlik puanı yükselir.
9. Gönderinin erişilebilir son hâli gösterilir.

Bu senaryo projenin faydasını jüriye birkaç dakika içinde anlaşılır biçimde gösterebilir.

---

## 13. Başarı Ölçütleri

### Görsel açıklama modülü
* Açıklamanın görseldeki temel konuyu doğru belirtmesi
* Gereksiz veya yanlış detay üretmemesi
* Türkçe dil kalitesinin anlaşılır olması
* Kullanıcı tarafından düzenlenebilmesi

### Altyazı modülü
* Konuşmanın doğru metne dönüştürülmesi
* Zaman kodlarının uygun olması
* Farklı ses koşullarında çalışması
* Hataların kullanıcı tarafından düzeltilebilmesi

### UI/UX
* Kullanıcının destek almadan analiz başlatabilmesi
* Önerilerin neden verildiğini anlayabilmesi
* Altyazılarda "siyah blok üstüne beyaz yazı" kontrast standardının korunması ve kullanıcı tarafından boyut/konum ayarlamalarının başarıyla yapılabilmesi
* Düzenleme (onay/red) işlemlerini tamamlayabilmesi ve oyunlaştırma puanını (0-100) görebilmesi
* Sonuç ekranını karmaşık bulmaması

### Genel ürün metrikleri
* Erişilebilirlik kontrolünün tamamlanma süresi
* Önerilerin kullanıcı tarafından kabul edilme oranı
* İçerik puanındaki ortalama artış
* Başarıyla oluşturulan alternatif metin oranı
* Başarıyla oluşturulan altyazı oranı
* Kullanıcı görevi tamamlama oranı
* Kullanıcı memnuniyeti

---

## 14. Ekip Görev Dağılımı

### Merve – takım kaptanı ve yapay zekâ lideri
* Proje kapsamını yönetmek
* Görsel alternatif metin modülünü araştırmak ve geliştirmek
* Yapay zekâ modellerini karşılaştırmak
* Projenin özgünlük ve NSosyal uyumunu yazmak
* Rapor parçalarını birleştirmek
* Final sunumunun ana anlatımını hazırlamak

### Zeynep Ecren – yazılım ve backend
* GitHub deposunu oluşturmak
* Sistem mimarisini hazırlamak
* Backend ve API geliştirmek
* Yapay zekâ modüllerini uygulamaya bağlamak
* Teknik altyapı ve model doğrulama bölümlerini yazmak
* Çalışan prototipin entegrasyonunu yapmak

### Nez – test ve kullanıcı araştırması
* Hedef kullanıcı araştırması yapmak
* Mevcut çözümleri karşılaştırmak
* Test senaryolarını hazırlamak
* API ve kullanıcı kabul testlerini yürütmek
* Hedef kitle, verimlilik ve iş modeli bölümlerini yazmak
* Raporun dil ve kanıt kontrolünü yapmak

### Beril – UI/UX ve erişilebilirlik analizi
* Erişilebilirlik gereksinimlerini çıkarmak
* Kullanıcı akışlarını hazırlamak
* Figma wireframe tasarlamak
* Erişilebilirlik puanlama mantığını oluşturmak
* UI/UX ve kullanılabilirlik yaklaşımını yazmak
* İş paketleri ve görev dağılımını hazırlamak

### Sevda – video, ses ve altyazı
* Otomatik altyazı teknolojilerini araştırmak
* Whisper ve FFmpeg ile prototip hazırlamak
* Farklı ses koşullarında test yapmak
* Toplumsal fayda bölümünü yazmak
* Sürdürülebilirlik bölümünü hazırlamak
* Kaynakları ve atıfları düzenlemek

---

## 15. Çalışma Planı

### 16–17 Ağustos: kapsam ve araştırma
* Problem ve hedef kitle netleştirilecek.
* GitHub deposu oluşturulacak.
* Erişilebilirlik gereksinimleri çıkarılacak.
* Akademik ve resmî kaynaklar toplanacak.
* Kullanılacak modeller araştırılacak.
* Proje kapsamına girmeyen özellikler belirlenecek.

### 18–19 Ağustos: tasarım ve teknik kararlar
* Sistem mimarisi hazırlanacak.
* Kullanıcı akışı çizilecek.
* Figma wireframe oluşturulacak.
* Alternatif metin modeli seçilecek.
* Whisper altyazı denemeleri yapılacak.
* Erişilebilirlik puanı kuralları belirlenecek.
* Mevcut çözüm karşılaştırması tamamlanacak.

### 20 Ağustos: prototip parçaları
* Görsel açıklama PoC’si çalıştırılacak.
* Altyazı PoC’si çalıştırılacak.
* Backend iskeleti hazırlanacak.
* Test senaryoları oluşturulacak.
* Teknik rapor bölümlerinin ilk taslakları tamamlanacak.

### 21 Ağustos: rapor parçalarının teslimi
* Her üye kendi bölümünü Merve’ye teslim edecek.
* Kaynaklar ve bağlantılar eklenecek.
* Görseller, tablolar ve mimari şema teslim edilecek.
* Merve bütün bölümleri tek raporda birleştirecek.

### 22 Ağustos: raporun tamamlanması
* Raporun tüm ana başlıkları doldurulacak.
* Eksik kaynak ve tablo bırakılmayacak.
* Yeni kapsam eklenmesi durdurulacak.
* Rapor tam sürüm olarak dondurulacak.

### 23 Ağustos: içerik kontrolü
* Değerlendirme maddeleri tek tek kontrol edilecek.
* Atıflar ve kaynakça karşılaştırılacak.
* Teknik ifadeler GitHub ile doğrulanacak.
* Tekrarlanan cümleler temizlenecek.
* Takım üye isimlerinin raporda bulunmadığı kontrol edilecek.
* Sayfa sınırı ve biçim kuralları incelenecek.

### 24 Ağustos: teslim
* Son dosya biçimi kontrol edilecek.
* Dosya adı düzenlenecek.
* KYS’ye saat 17.00’den önce yüklenecek.
* Teslim ekranının görüntüsü saklanacak.

### 25 Ağustos–1 Eylül: prototipi geliştirme
* Backend tamamlanacak.
* Modüller entegre edilecek.
* Arayüz geliştirilecek.
* Örnek veriler hazırlanacak.
* Temel hatalar giderilecek.

### 2–7 Eylül: mentörlük ve iyileştirme
* Mentör geri bildirimleri kaydedilecek.
* Zorunlu düzeltmeler önceliklendirilecek.
* Kullanıcı testleri yapılacak.
* Yapay zekâ çıktıları değerlendirilecek.
* Final kapsamı kesinleştirilecek.

### 8–13 Eylül: final hazırlığı
* Uçtan uca çalışan demo tamamlanacak.
* Kullanıcı testi sonuçları eklenecek.
* Sunum hazırlanacak.
* Demo videosu çekilecek.
* Jüri soruları prova edilecek.
* Yedek video ve ekran görüntüleri hazırlanacak.

### 14 Eylül: final sunumu teslimi
* Sunum ve gerekli dosyalar saat 17.00’den önce yüklenecek.
* Bütün bağlantılar ve videolar kontrol edilecek.

### 15–19 Eylül: canlı sunum provası
* Her üyenin konuşma süresi belirlenecek.
* Teknik ve iş modeli soruları hazırlanacak.
* Demo internet olmadan da gösterilebilecek şekilde yedeklenecek.
* Sunum birkaç kez süre tutularak prova edilecek.

### 20 Eylül: jüri ve katılımcılara canlı sunum
* Problem kısa ve güçlü şekilde anlatılacak.
* Çözüm çalışan demo üzerinden gösterilecek.
* Toplumsal fayda ile teknik uygulanabilirlik birlikte vurgulanacak.
* Sorulara ekip uzmanlıklarına göre cevap verilecek.

---

## 16. Olası Riskler ve Çözümler

| Risk | Çözüm |
| :--- | :--- |
| Yapay zekânın yanlış görsel açıklaması üretmesi | Kullanıcı düzenleme ve onay mekanizması |
| Türkçe altyazı doğruluğunun düşük olması | Gürültü testleri ve manuel düzeltme alanı |
| Proje kapsamının çok büyümesi | MVP’yi dört temel özellikle sınırlandırma |
| Kodlama yükünün Zeynep’te toplanması | Modülleri bağımsız geliştirip API üzerinden birleştirme |
| Beril ve Sevda’nın Python seviyesinin düşük olması | Hazır modeller, Colab ve açık adımlı görevler kullanma |
| Gerçek NSosyal API’sine erişilememesi | NSosyal’e benzeyen bağımsız demo arayüzü geliştirme |
| Kullanıcı testine erişilememesi | Küçük örneklem ve uzman değerlendirmesi kullanma |
| Son gün dosya problemi yaşanması | Raporu 22 Ağustos’ta dondurup erken yüklemeye hazırlama |
| Canlı demoda bağlantı sorunu | Ekran kaydı ve yerel yedek demo hazırlama |

---

## 17. Gelecek Geliştirmeler

MVP’den sonra şu özellikler eklenebilir:
* Otomatik sesli betimleme
* İşaret dili desteği
* Çok dilli altyazı ve alternatif metin
* Ekran okuyucu uyumluluğunun otomatik testi
* Kişiye özel erişilebilirlik tercihleri
* İçerik üreticileri için erişilebilirlik rozeti
* Kurumsal hesaplar için erişilebilirlik analitiği
* Canlı yayınlarda gerçek zamanlı altyazı
* Türkçe işaret dili avatarı
* Cihaz üzerinde çalışan gizlilik odaklı modeller
* NSosyal genel erişilebilirlik performans paneli

---

## 18. Projenin Tek Cümlelik Anlatımı

> NSosyal Erişilebilir Destek, görsel, video ve metin içeriklerini paylaşım öncesinde analiz ederek Türkçe alternatif metin, otomatik altyazı, sadeleştirme ve erişilebilirlik önerileri sunan yapay zekâ destekli sosyal medya asistanıdır.

### Kısa slogan seçenekleri
* **Herkes için erişilebilir sosyal medya**
* **Paylaşmadan önce erişilebilirliği kontrol et**
* **İçeriğin herkese ulaşsın**
* **NSosyal’de kimse içeriğin dışında kalmasın**
* **Bir içerik, herkes için erişilebilir**
