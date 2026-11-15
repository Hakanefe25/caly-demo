# CALY — Apollo 17 Demo

Ay’da Caly ile karşılaştığın, Apollo 17’den kalan donanımın hikâyelerini keşfettiğin bağımsız bir görsel roman. Ren’Py 8.5.3 ile hazırlanmıştır. Türkçe ve İngilizce destekler.

Dört keşif bulunur: Ay Keşif Aracı, tel örgü tekerlekleri, Challenger’ın iniş kademesi ve ALSEP istasyonu. Fotoğraflardaki işaretlerden istediğin hikâyeye başlayabilir, ek sorular sorabilir ve keşiflerini arşivden yeniden açabilirsin. Demo vedalaşma ve Dünya’ya dönüş anlatımıyla biter.

## Klasörler

| Yol | İçerik |
| --- | --- |
| `caly-demo/game/` | Ren’Py kaynak kodu, Türkçe/İngilizce metinler ve oyun görselleri |
| `caly-demo/SOURCES.md` | Bilimsel iddialar ve görseller için resmî kaynak eşleştirmeleri |
| `vercel-deploy/public/` | Hazır Ren’Py WebAssembly web dağıtımı |
| `vercel-deploy/vercel.json` | Vercel statik yayın ayarları |
| `tools/Build-Web.ps1` | Kaynaklardan web dağıtımını yeniden üretme |
| `tools/serve_web.py` | Yerel HTTP önizlemesi |

## Yerel oyun

[Ren’Py 8.5.3 SDK](https://www.renpy.org/release/8.5.3) içinden `caly-demo` klasörünü proje olarak açıp çalıştırın. Windows PowerShell alternatifi:

```powershell
.\caly-demo\Launch.ps1 -Sdk 'C:\path\to\renpy-8.5.3-sdk'
```

SDK bu depoya dahil değildir. Yerel kayıtlar ve önbellekler Git’e alınmaz.

## Web ve Vercel

Hazır web dosyaları `vercel-deploy/public/` içindedir. Vercel projesinin kök dizinini **vercel-deploy**, framework ayarını **Other**, çıktı dizinini **public** seçin. Derleme komutu gerekmez. GitHub’dan içe aktarma veya CLI ile yayınlama adımları [web notlarında](vercel-deploy/README.md) bulunur.

Yerelde dosyaları `file://` ile açmayın; HTTP sunucusu kullanın:

```powershell
python .\tools\serve_web.py
```

Ardından `http://127.0.0.1:8042/` adresini açın. Python yoksa herhangi bir statik HTTP sunucusu da kullanılabilir.

Yeniden derlemek için aynı SDK’nın resmî Web desteğini kurun:

```powershell
.\tools\Build-Web.ps1 -Sdk 'C:\path\to\renpy-8.5.3-sdk'
```

## Kaynaklar ve görseller

Tarihî fotoğraflar ve bilimsel bilgiler NASA kaynaklarına dayanır. Her keşfin oyun içi kaynak bağlantıları bulunur; resmî URL’ler, görsel kredileri, dosya hash’leri ve doğrulanamayan ayrıntılar [SOURCES.md](SOURCES.md) içinde tutulur. Caly ve ziyaret hikâyesi kurgudur. Caly’nin Ay sahneleri yapay zekâyla üretilmiş kurgusal çizimlerdir; tarihî görev fotoğrafı değildir.

Depodaki görseller için toplu bir yeniden kullanım lisansı verilmez. Her varlığın kökeni ve bilinen hak bilgileri kaynak kaydında açıklanır. Oyun motoru ve üçüncü taraf bileşenleri kendi lisanslarına tabidir.

## Doğrulama durumu

Yerel Ren’Py Apollo 17 gezi testi 25/25 kontrolü geçti: dört hikâye, sekiz ek soru, hızlı kayıt/yükleme, arşiv, yeniden anlatım ve final. Web çıktısı özgün oyun kaynakları ve görsellerinden üretilmiştir. Bu sonuçlar tüm tarayıcıların veya mobil cihazların test edildiği anlamına gelmez. Kaynak sürümün bilinen kullanım ayrıntıları `caly-demo/README.md` içinde açıklanır.
