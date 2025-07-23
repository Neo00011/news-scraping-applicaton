# Haber Başlıkları ve Linkleri Web Scraping Uygulaması

Bu Python uygulaması, belirlenen bir haber sitesinden güncel haber başlıklarını, yayınlanma zamanlarını ve doğrudan haber linklerini çeker. Çekilen veriler, kolayca incelenebilir ve analiz edilebilir bir `.csv` (Comma Separated Values) dosyasına kaydedilir.

## Ne Yapar?

* **Haber Bilgileri Çekimi:** Hedef haber sitesindeki makale başlıklarını, yayınlanma tarihlerini/saatlerini ve ilgili haberin detay sayfasına giden linklerini toplar.
* **Veri Kaydı (CSV):** Çekilen tüm haber verilerini düzenli bir `.csv` dosyasına kaydeder. Bu format, Excel gibi tablolaştırma programlarında kolayca açılabilir ve işlenebilir.
* **Güncel Bilgi Erişimi:** Haber sitelerinin statik veya yarı-dinamik içeriklerinden hızlı ve etkin veri çekimi sağlar.

## Neden Önemli?

Medya takibi, pazar analizi, trend belirleme veya belirli bir konu hakkındaki gelişmeleri izleme gibi alanlarda güncel haber verileri hayati öneme sahiptir. Bu uygulama:

* **Medya İzleme:** Belirli anahtar kelimeler veya konular etrafındaki haberleri otomatik olarak takip etme potansiyeli sunar.
* **Pazar Trendleri:** Sektörünüzle ilgili haberleri takip ederek piyasa trendlerini ve duyuruları yakalamaya yardımcı olur.
* **Zaman ve İş Gücü Tasarrufu:** Manuel olarak haber sitelerini tarama ve veri toplama zahmetini ortadan kaldırır.

## Kullanılan Teknolojiler

* **Python:** Uygulamanın geliştirildiği ana programlama dili.
* **`requests` Kütüphanesi:** Web sitelerinden HTML içeriği almak için kullanılır.
* **`BeautifulSoup` Kütüphanesi:** Çekilen HTML içeriğini kolayca ayrıştırmak ve veri ayıklamak için kullanılır.
* **`csv` Modülü (Python Yerleşik):** Toplanan verileri standart CSV formatında dosyaya yazmak için kullanılır.

## Nasıl Çalışır?

1.  Uygulama, belirlenen haber sitesine HTTP isteği gönderir ve sayfanın HTML içeriğini alır.
2.  `BeautifulSoup` kullanarak bu HTML içeriğini analiz eder.
3.  Her bir haber öğesi için başlık, yayınlanma zamanı ve haber linki gibi bilgileri tespit eder ve çeker.
4.  Çekilen tüm verileri listeler halinde toplar.
5.  Toplanan verileri, Python'ın `csv` modülü aracılığıyla `haber_verileri.csv` adında bir CSV dosyasına satır satır yazar.
