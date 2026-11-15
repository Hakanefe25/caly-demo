# caly-demo — Apollo 17 kaynak kaydı

Demoda kullanılan NASA sayfaları 14 Kasım 2026 tarihinde bu çalışma oturumunda resmî içerikleri üzerinden doğrulandı. Bu dosya yalnızca demo kapsamındaki iddia ve görselleri kapsar. Caly, oyuncu, ziyaret, diyalogların kişisel bölümleri, vedalaşma ve dönüş yolculuğu kurgudur; tarihî tanıklık veya gerçek insanlı uzay turizmi betimlemesi değildir.

## Resmî kaynaklar

| Anahtar | NASA kaynağı | Demoda desteklediği bilgi |
|---|---|---|
| M1 | [Apollo 17: Gene Cernan in Lunar Roving Vehicle](https://science.nasa.gov/resource/apollo-17-gene-cernan-in-lunar-roving-vehicle/) | Taurus-Littrow; ilk Ay yürüyüşünde aracı süren Eugene Cernan; arka plandaki Ay Modülü; sayfanın tarihî fotoğraf tarihi 11 Aralık 1972; NASA/Harrison Schmitt kredisi. |
| M2 | [Apollo 17 özeti / NASA SP-4029](https://www.nasa.gov/wp-content/uploads/static/history/SP-4029/Apollo_17a_Summary.htm) | Aralık 1972 görevi, araç kullanımı, jeolojik incelemeler ve örnek toplama, ALSEP kurulması; yükseliş kademesinin CSM ile kenetlenmesi, ekip ve örneklerin aktarılması ve Dünya’ya dönüş için CSM’nin hazırlanması. Son park yeri için M6 kullanılır. |
| M3 | [Reinventing the Wheel / NASA Glenn](https://www3.nasa.gov/specials/wheels/) | Tarihî LRV bölümü: esnek tel örgü tekerlekler, aşırı bükülmeyi sınırlayan iç çerçeve, yumuşak zeminde ilerlemeye yardımcı şeritler. Sayfadaki güncel araç durumuna ilişkin eski ifadeler kullanılmaz. |
| M4 | [Human Artifacts on the Moon](https://www.nasa.gov/wp-content/uploads/static/history/humanartifacts.html) | Ay donanımının tarihî ve bilimsel değeri; koruma yaklaşımı. |
| M5 | [Apollo 17 Mission Details](https://www.nasa.gov/missions/apollo/apollo-17-mission-details/) | Batarya ile çalışan LRV; Challenger adı; Ay Modülü’nün yükseliş kademesinin ekip ile Ay yörüngesine çıkması ve CSM ile kenetlenmesi. Sayfalar arasındaki farklı sayısal özetler nedeniyle mesafe/hız istatistiği kullanılmaz. |
| M6 | [50 Years Ago: Apollo 17 Lands at Taurus-Littrow](https://www.nasa.gov/history/50-years-ago-apollo-17-lands-at-taurus-littrow/) | Yüzey araştırmaları, örnekler ve fotoğraf kayıtları; Cernan’ın aracı ayrılmadan önce son VIP park yerine götürmesi ve oradan kalkışın televizyonda gösterilmesi. |
| N1 | [Exploring the Apollo 17 Site / PIA12920](https://science.nasa.gov/photojournal/exploring-the-apollo-17-site/) | LRO’nun sonradan görüntülediği Challenger iniş kademesi. Görüntü sayfasının eklenme tarihi çekim tarihi olarak sunulmaz. |
| N2 | [NASA SVS 10818](https://svs.gsfc.nasa.gov/10818/) | Apollo 17 ALSEP’in yörünge görüntüsü ile yüzey fotoğrafını birleştiren açıklamalı görselleştirme; Chris Smith / NASA SVS. |
| N3 | [Recovery, Restoration and Archiving of Previously Lost ALSEP Data / NTRS 20190032593](https://ntrs.nasa.gov/citations/20190032593) | Beş görevde ALSEP kurulması, ekipler ayrıldıktan sonra ölçüm yapılması, programın Eylül 1977’de bitmesi, eski veri ve üstverilerin kurtarılıp arşivlenmesi. Her cihazın kesintisiz çalıştığı iddia edilmez. |

## İddia eşleştirmesi

İngilizce ve Türkçe konuşmalar aynı bilimsel iddiaları taşır. 0.2 sürümünde dört hikâyenin toplam 32 satırı ve sekiz ek sorunun cevapları `game/story_data.rpy` içindedir. Her satır konuşmacısını, gösterilecek kareyi ve bilimsel bilgi içeriyorsa resmî kaynak anahtarlarını taşır. Aşağıdaki tablo bu konuşmaları kapsar. Artık kullanılmayan genel açıklama/özet metinleri kaldırılmıştır.

| Keşif | İddialar ve kaynaklar | Görsel bölgesi / sınırlar |
|---|---|---|
| Ay Keşif Aracı | Sürücü, ilk yürüyüş, Ay Modülü ve konum: M1. Batarya: M5. Araştırma, örnek toplama ve kayıtlar: M2/M6. Son park ve kalkışın görüntülenmesi: M6. Ek sorular: ilk yürüyüş/son park ayrımı M1/M6; koruma önerileri M4. | M1 fotoğrafında aracın koltuk/ekip bölgesi. Fotoğraf ilk yürüyüşe aittir; son park anını gösterdiği söylenmez. Son görev anlatılırken aynı fotoğraf gösterilir; bunun son park konumunu belgelemediği ek soruda açıkça belirtilir. |
| Tel örgü tekerlekler | Yapı ve işlev: M3. Ek sorular: iç çerçeve açıklaması M3’ten gelir, piksel yorumundan değil; araca bağlı tekerleklerin kaldığı çıkarımı M1/M6. | Ön plandaki yakın tekerlek. İç çerçevenin bu kesitte açıkça görüldüğü iddia edilmez. Her tekerleğin güncel durumunu belgeleyen ayrı bir inceleme varmış gibi anlatılmaz. |
| Challenger iniş kademesi | İniş/yükseliş bölümleri ve Ay yörüngesine çıkış: M2/M5; geride kalan alt bölümün yörüngeden tanımlanması: N1. Ek sorular: ekip ve örneklerin CSM’ye aktarılması M2/M5; N1 katalog eklenme tarihi 28 Ekim 2009’dur, çekim tarihi olarak kullanılmaz. | Altın rengindeki alt yapı ve iniş ayakları işaretlidir; üst kabin dahil edilmez. Kaplamanın maddesi hakkında renk üzerinden iddia üretilmez. Yüzey fotoğrafı ayrılmadan önceki durumu, N1 sonraki yörünge görüntüsünü gösterir. |
| Apollo 17 ALSEP istasyonu | Cihazlar, ekip ayrıldıktan sonra ölçümler ve Dünya’ya veri iletimi, Eylül 1977 program sonu, veri kurtarma: N3; görüntü ve sonraki yüzeyde kalan donanım: N2. Ek sorular: birleşik görsel N2; zamanında arşivlenmeyen veriler, kaybolan bantlar ve üstveriler N3. | Birleşik görselin sağındaki yüzey fotoğrafında cihaz grubu. Tek bir kamera karesi değildir. Alt fotoğrafın bağımsız orijinal kimliği doğrulanamadı; kimlik uydurulmadı. |

Başlangıç, karşılaşma, kişisel sorular, vedalaşma ve oyuncunun dönüşü kurgudur. Caly’nin tercihleri ve oyuncunun şaşırması tarihî tanıklık değildir. Kapanış artık dört hikâyeyi yeniden özetlemez. Bilinmeyen hasar nedenleri, ölçüler veya maliyet gerekçeleri üretilmez.

## Paketlenen NASA görselleri

| Yerel dosya | Resmî indirme | SHA-256 |
|---|---|---|
| `game/images/moon/apollo17.jpg` — NASA/Harrison Schmitt; yüzey sahnesi ve araç/tekerlek/iniş kademesi kesitleri | [NASA JPEG](https://assets.science.nasa.gov/dynamicimage/assets/science/psd/lunar-science/2023/09/eugene_cernan-full-a.jpg?w=1600) | `7bbe8df72123f711725e6ce164018c25b7214ed0b21969ca622ea1f82ee6c8f5` |
| `game/images/moon/PIA12920.jpg` — NASA/GSFC/Arizona State University; sonraki yörünge görünümü | [NASA JPEG](https://assets.science.nasa.gov/dynamicimage/assets/science/psd/photojournal/pia/pia12/pia12920/PIA12920.jpg?w=1200) | `1e58609db13023b77f5320241aed759af1e012fc564dc40c608ec259caaf0f04` |
| `game/images/moon/alsep.jpg` — NASA SVS 10818; açıklamalı birleşik görsel | [NASA JPEG](https://svs.gsfc.nasa.gov/vis/a010000/a010800/a010818/apollo_17_alsep_ipod_lg.00127_print.jpg) | `ac2c18d0cc4bbe5f79c74dc61430f7dce2b7a2e63021601f376dbbaf20735f77` |

M1 sayfası bir fotoğraf kimliği belirtmez; bu dosyaya başka bir arşiv kimliği atanmaz. Görseller önceki doğrulanmış indirmelerden birebir kopyalanmıştır. Kesitler çalışma anında üretilir ve kesit olarak etiketlenir; fotoğraflara donanım eklenmez veya silinmez. İşaretler tıklama kolaylığı içindir, bilimsel sınır ölçümü değildir. Arşiv sahneleri en-boy oranını korur; ana menüde fotoğraf dekoratif arka plan olarak kırpılır ve karartılır.

NASA içeriğinin kullanımı [resmî medya kullanım koşullarına](https://www.nasa.gov/nasa-brand-center/images-and-media/) dayanır; NASA kredileri gösterilir, destek/onay izlenimi verilmez. Her NASA sitesindeki içeriğin her ülkede sınırsız telifsiz olduğu iddia edilmez.

## 0.2 yeniden doğrulaması

Dokuz resmî kaynak kaydı tekrar açılarak konuşmalardaki iddialarla karşılaştırıldı. NTRS sayfasının sonraki istekleri zaman aşımına uğradığı için N3 ayrıca aynı belgenin [resmî NASA API kaydı](https://ntrs.nasa.gov/api/citations/20190032593) üzerinden kontrol edildi: belge kimliği, başlık ve özet; Eylül 1977, kayıp kayıtlar ve kurtarma çalışmalarıyla eşleşiyor. Üç görselin resmî URL’lerinden yeniden alınan baytların SHA-256 değerleri yerel dosyalarla aynı. `tools/nasa-recheck.json` bu kontrolün sonucunu kaydeder.

Tarih sınırı: M1 fotoğraf sayfası tarihî tarih olarak 11 Aralık 1972 verir; M5 zaman çizelgesinde Cernan’ın yüzeye çıkışı 12 Aralık olarak yer alır. Saat dilimi ve fotoğrafın tam çekim zamanı ayrıca kesinleştirilmediğinden oyunun etiketi yalnızca **Aralık 1972 / ilk Ay yürüyüşü** der. Kaynak sayfasındaki tarih, doğrulanmış kesin çekim günü olarak genişletilmez.

Her konuşma satırıyla kaynak ve kare eşleştirmesi `tools/DIALOGUE_REVIEW.md` çıktısında incelenebilir. Bu düzenleme yeni tarihî fotoğraf veya yapay zekâyla üretilmiş donanım eklemez.

## Kurgusal ve diğer görseller

- `game/images/story/caly_moon.png` ve `caly_moon_reflect.png`: önceki çalışmada OpenAI ImageGen ile oluşturulmuş kurgusal Ay sahneleri; karakter kaynağı kullanıcı tarafından sağlanan anlatıcı görselidir. Gerçek Taurus-Littrow topografyasının, ışığın veya tarihî görevin yeniden yapımı değildir. Caly’nin kıyafeti ve varlığı bilimsel iddia oluşturmaz. Oyun içinde kurgusal manzara etiketi gösterilir.
- `game/images/caly/caly_narrator.png`: kullanıcının sağladığı kurgusal karakter görseli. NASA fotoğrafı değildir. Sanatçısı, ilk üretim yöntemi ve yeniden dağıtım hakları doğrulanamadı.
- Arayüz, işaretler ve geçişler Ren’Py bileşenleridir. Standart GUI görselleri ve yazı tipi mevcut Ren’Py projesinden kopyalanmıştır; bilimsel görsel değildir.
- Programlama, arayüz ve kaynaklara dayalı metin düzenlemesinde OpenAI Codex desteği kullanılmıştır. Yapay zekâ ile tarihî görev fotoğrafı üretilmemiştir.
