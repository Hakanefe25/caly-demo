# caly-demo — Apollo 17

Ana oyundan bağımsız Ren’Py projesi. Sürüm: **0.3-demo**.

Yalnızca Ay’daki Apollo 17 bölümü bulunur. Dört keşif: Ay Keşif Aracı, tel örgü tekerlekleri, Challenger’ın iniş kademesi ve Apollo 17 ALSEP istasyonu. Başka gezegenlere geçiş veya başka görevlere ait keşif bulunmaz.

Akış: Apollo 17 arşiv fotoğrafıyla açılış → Ay’da Caly ile karşılaşma → işaretli fotoğraflardan serbest keşif → dört hikâyenin tamamlanması → vedalaşma ve Dünya’ya dönüş anlatımı → demo finali. Her hikâyede tam fotoğraf, ayrıntı kesiti ve uygun arşiv görüntüsü kullanılır. Tamamlanan hikâyeler arşivden tekrar dinlenebilir.

0.2 sürümünde konuşmalar yeniden düzenlendi: dört hikâyede toplam 32 karşılıklı konuşma satırı, her keşfe özel ikişer ek soru bulunur. Genel açıklamaların ardından aynı bilgiyi tekrar okuyan eski özet döngüsü kaldırıldı. Okunan ek sorular işaretlenir ve devre dışı kalır; ana hikâye yalnızca “Hikâyeyi yeniden dinle” seçildiğinde yeniden anlatılır. Soruların cevaplarında geçen kaynaklar da keşfin kaynak ekranına eklenir. Açılış ve kapanışta aynı bilgilerin yeniden özetlenmesi kaldırıldı.

Demo yeni profilde Türkçe başlar. Ayarlardan İngilizce seçilebilir. Kayıt dizini `caly-demo-apollo17-v1` olduğundan ana oyunun kayıtlarına veya arşivine dokunmaz. Fotoğraftaki tıklanacak bölgeler sürekli işaretlidir. Konuşma ve seçim ekranlarının alt ortasında sade bir hızlı erişim satırı bulunur: Geri, Geçmiş, Atla, Otomatik, Kaydet, Hızlı Kaydet, Hızlı Yükle ve Ayarlar. Kaynakça ve oyun menülerinde bu satır gizlenir.

0.1 sürümünden bir kayıt yüklenirse tamamlanan keşifler korunur; eski konuşma döngüsünün ortasında kalınmaması için fotoğraf seçim ekranından devam edilir. Yeni sürümde alınan kayıtlar konuşmanın kaldığı yerden açılır.

## Çalıştırma

- Kaynak projeyi çalıştırmak için: bu klasörde `powershell -ExecutionPolicy Bypass -File .\Launch.ps1`. SDK yolunu `-Sdk` ile verin veya `RENPY_SDK` ortam değişkenini ayarlayın.
- Ren’Py Launcher üzerinden de bu klasör proje olarak seçilebilir; `game/` doğrudan bu klasörün altındadır.

## Kaynaklar ve doğrulama

Bu demoya ait bilimsel iddia ve görsel eşleştirmeleri `SOURCES.md` içindedir. Yalnızca üç NASA bilim/arşiv görseli paketlenir. Caly’nin iki Ay sahnesi kurgusal AI çizimidir; gerçek iniş alanının birebir görüntüsü değildir. Sağlanan anlatıcı portresi de tarihî fotoğraf değildir.

`tools/check_demo.py` görsel bütünlüğünü, kapsam dışı içeriğin bulunmadığını ve ana oyunun kaynaklarının değişmediğini denetler. `tools/VALIDATION.md` test sonuçlarını içerir. Test kayıtları ve ekran görüntüleri dağıtım paketine dahil edilmez.

Resmî Ren’Py WebAssembly çıktısı `../vercel-deploy/public` klasöründe hazırlanmıştır. Yeniden derleme, Vercel giriş/yayın komutları ve gerçekleşen/engelli testler için `../vercel-deploy/README.md` dosyasına bakın. Vercel yayını proje sahibi tarafından yapılmıştır; hesap bağlantısı bu depoya dahil değildir.
