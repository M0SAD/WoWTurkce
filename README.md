<p align="center"><img src="docs/banner.png" alt="WoWTürkçe"></p>

# WoWTürkçe — World of Warcraft Türkçe Yama

**World of Warcraft'ı neredeyse %100 Türkçe oyna.** Görevlerden NPC konuşmalarına, büyülerden eşya ipuçlarına, arayüzden başarımlara kadar oyunda gördüğün yazıların büyük çoğunluğu Türkçe.

Desteklenen sürümler: **Classic Era**, **Classic (Forever)** ve **Retail (Midnight)**.

![Kapsam](docs/kapsam.png)

## Çeviri tarzı

- Oyuncu, sınıf, ırk, NPC, bölge ve fraksiyon adları orijinal (İngilizce) kalır; yani oyundaki isimleri tanımakta zorlanmazsın.
- Genel terimler tutarlı Türkçe karşılıklarla kullanılır (Lonca, Zindan, Müzayede Evi, Başarım, Mitik, Arkan, Ün, Savaş Grubu vb.).
- Metinler oyun içi bağlama göre, doğal ve akıcı Türkçe ile çevrilir.

![Önce / Sonra](docs/ornek.png)

## Kurulum

![Kurulum](docs/kurulum.png)

### 1) Kurulum programı (önerilen)

[`WoWTurkce-Kurulum.exe`](WoWTurkce-Kurulum.exe) dosyasını indirip çalıştırman yeterli.

- Bilgisayarındaki WoW sürüm klasörlerini (`_retail_`, `_classic_era_`, `_forever_` gibi) kendisi bulur ve addon'u hepsine kurar.
- Windows ile birlikte açılır, sistem tepsisinde çalışır.
- **Yeni sürüm çıktığında addon dosyalarını otomatik olarak günceller.** Sen hiçbir şey yapmazsın.
- Retail'e özel dosyalar yalnızca `_retail_` klasörüne kurulur.
- Dosyanın Özellikler → Ayrıntılar sekmesinde addon sürümü yazar.

> Windows "bilinmeyen yayıncı" uyarısı verebilir; program imzasız olduğu için bu normaldir. Program yalnızca bu depodan addon dosyalarını indirip WoW klasörlerine yazar.

### 2) Elle kurulum (ZIP)

Kurulum programını kullanmak istemiyorsan:

1. [`WoWTurkce.zip`](WoWTurkce.zip) dosyasını indir.
2. İçindeki **`WoWTurkce`** klasörünü şu klasöre kopyala:
   - Retail: `...\World of Warcraft\_retail_\Interface\AddOns\`
   - Classic Era: `...\World of Warcraft\_classic_era_\Interface\AddOns\`
   - Classic (Forever): `...\World of Warcraft\_forever_\Interface\AddOns\`
3. Oyunu aç, karakter seçim ekranında **Eklentiler** bölümünden *WoWTürkçe*'nin açık olduğundan emin ol.

> ⚠️ **ZIP ile kurulumda otomatik güncelleme yoktur.** Yeni sürümlerde ZIP'i tekrar indirip aynı yere atman gerekir. Otomatik güncelleme istiyorsan kurulum programını kullan.

## Eksik veya İngilizce bir yer mi gördün?

Çeviri sürekli büyüyor; oyun çok büyük olduğu için bazı metinler hâlâ İngilizce kalmış olabilir. Böyle bir yer görürsen lütfen bize bildir, bir sonraki sürümde çevirelim:

1. Bu sayfanın üstündeki **Issues** sekmesinden yeni bir konu aç.
2. Metnin **ekran görüntüsünü** ekle ve nerede gördüğünü kısaca yaz (hangi sürüm, hangi pencere, hangi görev/NPC/eşya).
3. Mümkünse ekran görüntüsünde karakter adın ve özel bilgilerin görünmediğinden emin ol.

Kurulum programının arka plan izleme (`--izle`) özelliğini açarsan, oyundan çıkınca çevirisi eksik **oyun metinlerinin** kodları toplanır ve istersen otomatik gönderilir. Sohbet ve kişisel veri bu kodlara girmez; göndermeyi kapatmak için programın yanındaki `WoWTurkce.json` dosyasında `"gonder": false` yapabilirsin.

## Sık sorulanlar

**Oyun güncellenince bozulur mu?** Oyun yamasından sonra yeni içerik İngilizce görünebilir; çeviriler yeni sürümlerle eklenir. Kurulum programı varsa güncellemeler otomatik gelir.

**Kaldırmak istersem?** `Interface\AddOns\WoWTurkce` klasörünü sil (ve kurulum programını tepsiden çıkarıp kaldır).

## Benzer bir proje: WoWTR

Türkçe yama alanında [WoWTR](https://www.curseforge.com/wow/addons/wowtr) adında (Platine & Hakan YILMAZ) başka bir proje de var. **WoWTürkçe, WoWTR'den bağımsız, sıfırdan yazılmış bir projedir.** WoWTR'den hiçbir dosya, çeviri veya kod alınmadı; bu projeye başladıktan sonra WoWTR'nin varlığından haberim oldu. Her iki proje de aynı amaca hizmet ediyor; oyuncular için seçenek olması güzel.

Merak edenler için, WoWTR'nin `v26.1103` arşivini inceleyip kendi arşivimle karşılaştırdım (sayılar yaklaşık, girdi sayısıyla):

| Alan | WoWTR v26.1103 | WoWTürkçe |
|---|---|---|
| Görevler | ~36 bin | ~38 bin |
| NPC konuşmaları, diyaloglar, altyazılar | ~207 bin | ~75 bin (artıyor) |
| Eşya ve büyü metinleri | ~158 bin | ~240 bin |
| Arayüz (menüler, paneller, GlobalStrings) | ayrı veri seti görmedim | ~81 bin |
| Eşya, NPC, bölge ve zindan adları | — | ~61 bin |
| Kitaplar | ~14 bin | ~1,4 bin |
| **Toplam** | **~417 bin** | **~500 bin** |

Toplamda daha fazla çeviri ve daha geniş bir kapsam var; arayüz, adlar, Müzayede Evi'nde Türkçe arama, Konut (Housing) gibi alanlar yalnızca WoWTürkçe'de. Karşılaştırma için örneklem aldığımda iki projenin çevirileri neredeyse hiç örtüşmedi (yüzde 1'in biraz üstü), yani çeviriler birbirinden bağımsız. NPC konuşmaları ve kitaplar gibi alanlarda ise WoWTR'nin veritabanı şu an daha dolu; bu alanları da hızla büyütüyorum. Amacım oyunu **%100 Türkçe** oynanabilir hale getirmek.

## Geliştirici hakkında

Merhaba, ben **Erkin Azcan**. Mesleğim öğretmenlik; boş zamanlarımda WoW oynuyorum ve oyunu Türkçe oynamak istedim. Bu yamayı bu yüzden yaptım. Proje [Claude](https://claude.ai) (Anthropic) ile birlikte geliştirildi; ama arkasında çok fazla emek ve zaman var: çeviri kaynaklarının derlenmesi, terimlerin tutarlı hale getirilmesi, her güncellemenin üç oyun sürümünde tek tek denenmesi... Hâlâ gelişiyor.

Web sitem: [erkinazcan.com](https://erkinazcan.com)

---

Hazırlayan: **Erkin Azcan**
