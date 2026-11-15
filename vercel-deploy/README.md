# CALY — Apollo 17 Web

`public/` gerçek Ren’Py 8.5.3 WebAssembly dağıtımıdır. Kaynak proje `../caly-demo/` altındadır. Bu depo yalnızca Apollo 17 demosunu içerir.

## Vercel’e bağlama

Vercel’de bu GitHub deposunu içe aktarın. Root Directory: **vercel-deploy**. Framework: **Other**. Output Directory: **public**. Build Command: boş. `vercel.json` statik dosya ve WASM ayarlarını içerir.

CLI alternatifi (Vercel hesabınıza kendi oturumunuzla giriş yapın):

```powershell
cd vercel-deploy
npx vercel login
npx vercel --prod
```

`.vercel` hesap/proje bağlantısı ve giriş bilgileri depoya dahil edilmez. Mevcut canlı yayını bu depoya bağlamak için Vercel projesinin Git ayarlarından ilgili depoyu seçebilirsiniz.

## Güncelleme

Önce `caly-demo/game` kaynaklarını güncelleyin. Resmî Web desteği kurulu Ren’Py 8.5.3 SDK ile depo kökünden çalıştırın:

```powershell
.\tools\Build-Web.ps1 -Sdk 'C:\path\to\renpy-8.5.3-sdk'
```

Sonra kaynak değişiklikleriyle birlikte güncellenmiş `public/` çıktısını commit edin. Vercel hazır statik çıktıyı yayımlar. Bilimsel iddia veya fotoğraf değiştiğinde `SOURCES.md` kaydını da güncelleyin.

Kaydetme/yükleme tarayıcıya ve site adresine bağlıdır. Farklı tarayıcıya veya farklı adrese otomatik taşınmaz. Tarayıcı verilerinin temizlenmesi yerel kayıtları silebilir.
