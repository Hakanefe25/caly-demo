# Each spoken line has one authoring location and an explicit photograph cue.
init python:
    def beat(who, shot, en, tr, *sources):
        return dict(who=who, shot=shot, en=en, tr=tr, sources=list(sources))

    STORY_BEATS = {
        "rover": [
            beat("caly", "wide", "The driver is Eugene Cernan, Apollo 17's commander. This was photographed during the mission's first moonwalk.", "Direksiyondaki kişi Apollo 17’nin komutanı Eugene Cernan. Fotoğraf, görevin ilk Ay yürüyüşünde çekilmiş.", "M1"),
            beat("player", "wide", "An actual car on the Moon. Somehow that is the detail that gets me.", "Ay’da gerçekten araba sürmüşler. Nedense en çok buna şaşırıyorum.", "M1"),
            beat("caly", "detail", "A battery-powered exploration vehicle. The crew used it while surveying the terrain and collecting rock and soil samples.", "Bataryayla çalışan bir keşif aracı bu. Astronotlar araziyi incelerken, kaya ve toprak örnekleri toplarken kullanıyordu.", "M5", "M6"),
            beat("player", "detail", "So it was part of their fieldwork.", "Yani gezintiye çıkmıyorlardı; bildiğin saha çalışması yapıyorlardı.", "M6"),
            beat("caly", "wide", "Yes. And the samples and photographic records came back to Earth, where they could be studied.", "Evet. Topladıkları örnekler ve çektikleri fotoğraflar da Dünya’ya döndü; araştırmalar orada sürdü.", "M2", "M6"),
            beat("player", "caly", "What was the rover's last job?", "Peki aracın son görevi ne olmuş?"),
            beat("caly", "wide", "Cernan parked it at its final position before departure. From there, its television camera showed the crew lifting off.", "Cernan, ayrılmadan önce aracı son park yerine götürmüş. Üzerindeki televizyon kamerası da oradan ekibin Ay’dan havalanışını görüntülemiş.", "M6"),
            beat("player", "caly", "It even watched them leave.", "Gidişlerine de tanıklık etmiş yani.")
        ],
        "wheels": [
            beat("caly", "detail", "Look at the wheel's texture. It is quite different from a normal road tire.", "Tekerleğin dokusuna bak. Bildiğimiz otomobil lastiklerine pek benzemiyor.", "M1", "M3"),
            beat("player", "detail", "Is that wire mesh?", "Tel örgü mü o?"),
            beat("caly", "detail", "Yes, flexible wire mesh. A stiff inner frame limits how far it can bend.", "Evet, esnek bir tel örgü. İçindeki sert çerçeve de fazla bükülmesini önlüyor.", "M3"),
            beat("player", "detail", "And those narrow strips on the outside?", "Dışındaki ince şeritler ne işe yarıyor?"),
            beat("caly", "detail", "They help the wheel travel over soft lunar soil. The mesh, frame and tread strips each contribute something different.", "Tekerleğin yumuşak Ay toprağında ilerlemesine yardımcı oluyorlar. Örgünün, çerçevenin ve bu şeritlerin ayrı ayrı işi var.", "M3"),
            beat("player", "caly", "I would probably have looked straight past it.", "Ben olsam bakıp geçerdim."),
            beat("caly", "caly", "I nearly always start with the small parts. An occupational habit.", "Ben de hep küçük parçalara takılıyorum. Meslek alışkanlığı diyelim.")
        ],
        "descent": [
            beat("caly", "wide", "The structure behind the rover is Challenger, Apollo 17's Lunar Module.", "Aracın arkasındaki yapı, Apollo 17’nin Ay Modülü Challenger.", "M1", "M5"),
            beat("player", "wide", "It looks like a single spacecraft.", "Fotoğrafta tek parça gibi duruyor."),
            beat("caly", "detail", "It had two stages. The lower one handled the descent and landing. The upper ascent stage later carried the astronauts back into lunar orbit.", "Aslında iki kademeden oluşuyordu. Alttaki kademe alçalma ve iniş içindi. Üstteki yükseliş kademesi de daha sonra astronotları Ay yörüngesine çıkardı.", "M2", "M5"),
            beat("player", "detail", "So the gold-colored lower structure stayed here.", "Demek şu altın rengindeki alt bölüm burada kalmış.", "N1"),
            beat("caly", "alternate", "Here is a later view from the Lunar Reconnaissance Orbiter, LRO. We are looking down at the site from orbit.", "Bu da daha sonra Ay Keşif Yörünge Aracı LRO’nun çektiği görüntü. Bu kez aynı yere yörüngeden bakıyoruz.", "N1"),
            beat("player", "alternate", "The bright shape in the middle?", "Ortadaki parlak şekil mi?"),
            beat("caly", "alternate", "NASA identifies it as Challenger's descent stage. Without the image record, I would not identify such a small shape on appearance alone.", "NASA o şekli Challenger’ın iniş kademesi olarak tanımlıyor. Görüntünün kaydı olmasa, bu kadar küçük bir şekle bakıp ne olduğunu söyleyemezdim.", "N1"),
            beat("player", "caly", "I would never have connected those two pictures on my own.", "Bu iki fotoğrafın aynı yeri gösterdiğini tek başıma anlayamazdım.")
        ],
        "alsep": [
            beat("caly", "wide", "The instruments in the surface inset belong to Apollo 17's ALSEP station.", "Sağdaki yüzey fotoğrafında gördüğün cihazlar, Apollo 17’nin ALSEP istasyonuna ait.", "N2"),
            beat("player", "detail", "ALSEP is the name of the whole group?", "ALSEP bütün bu cihazların ortak adı mı?"),
            beat("caly", "detail", "Yes. The Apollo Lunar Surface Experiments Package: a set of scientific instruments deployed on the Moon.", "Evet. Apollo Ay Yüzeyi Deney Paketi’nin kısaltması. Ay yüzeyine yerleştirilen bir grup bilimsel cihazdan söz ediyoruz.", "N3"),
            beat("player", "detail", "Did someone have to stay with them?", "Başlarında birinin durması gerekmiyor muydu?"),
            beat("caly", "detail", "They continued taking measurements after the astronauts left, and their data were transmitted to Earth.", "Astronotlar ayrıldıktan sonra da ölçüm yaptılar. Topladıkları veriler Dünya’ya iletiliyordu.", "N3"),
            beat("player", "caly", "For how long?", "Ne zamana kadar?"),
            beat("caly", "wide", "The ALSEP program ended in September 1977. The hardware was not brought home.", "ALSEP programı Eylül 1977’de sona erdi. Donanım Dünya’ya getirilmedi.", "N3", "N2"),
            beat("player", "caly", "And what happened to the measurements?", "Peki toplanan ölçümler ne oldu?"),
            beat("caly", "wide", "Researchers later recovered and restored old ALSEP recordings and added them to the archives. The work on those records continued beyond the instruments' working lives.", "Araştırmacılar yıllar sonra eski ALSEP kayıtlarının bir bölümünü bulup kurtardı ve arşivlere ekledi. Cihazların işi bitmişti ama kayıtlar üzerindeki çalışma sürüyordu.", "N3")
        ]
    }

    FOLLOWUP_TOPICS = {
        "rover": [
            dict(id="photo_moment", en="Is this its final parking place?", tr="Bu fotoğraf son park yerinde mi çekilmiş?", lines=[
                beat("caly", "wide", "No. NASA describes this frame as the early part of the first moonwalk. The final parking happened later; we should not confuse the two moments.", "Hayır. NASA’nın açıklamasına göre bu kare, ilk Ay yürüyüşünün başlarında çekilmiş. Son park yeriyle bu fotoğraftaki konumu birbirine karıştırmayalım.", "M1", "M6")]),
            dict(id="preservation", en="Why examine it through photographs?", tr="Neden fotoğraflar üzerinden inceliyoruz?", lines=[
                beat("caly", "caly", "NASA has published recommendations for preserving the historical and scientific value of lunar equipment. I prefer examining the photographs without disturbing what is there.", "NASA, Ay’daki donanımın tarihî ve bilimsel değerini korumak için öneriler yayımlamış. Ben de oradaki hiçbir şeyi yerinden oynatmadan, fotoğraflardan incelemeyi tercih ediyorum.", "M4")])
        ],
        "wheels": [
            dict(id="visible_frame", en="Can we see the inner frame here?", tr="İçteki çerçeve bu fotoğrafta görünüyor mu?", lines=[
                beat("caly", "detail", "This crop does not show it clearly enough. The structural description comes from NASA Glenn's technical explanation, rather than a guess based on these pixels.", "Bu kesitte onu açıkça seçemiyoruz. İç yapısını anlatırken fotoğraftan tahmin yürütmüyorum; NASA Glenn’in teknik açıklamasına dayanıyorum.", "M3")]),
            dict(id="wheel_condition", en="Do we know every wheel is still intact?", tr="Tekerleklerin hâlâ sağlam olduğunu biliyor muyuz?", lines=[
                beat("caly", "wide", "We know the rover was parked on the Moon. Its wheels were attached, so we infer they stayed with it. That does not give us a separate later condition report for each one.", "Aracın Ay’da park edildiğini biliyoruz. Tekerlekler de ona bağlı olduğu için birlikte kaldıklarını düşünüyoruz. Ama bu bilgi, her tekerleğin bugünkü durumunu bildiğimiz anlamına gelmiyor.", "M1", "M6")])
        ],
        "descent": [
            dict(id="return_route", en="Did the upper stage go all the way to Earth?", tr="Üst bölüm Dünya’ya kadar mı döndü?", lines=[
                beat("caly", "wide", "No. It docked with the command and service module in lunar orbit. The crew and samples transferred across; the ascent stage was then separated. It was not their vehicle for the journey to Earth.", "Hayır. Ay yörüngesinde komuta ve hizmet modülüyle kenetlendi. Astronotlar ve örnekler oraya aktarıldı; yükseliş kademesi daha sonra ayrıldı. Dünya’ya dönüşü onunla yapmadılar.", "M2", "M5")]),
            dict(id="orbital_date", en="Was the orbital image taken in 1972 too?", tr="Yörünge görüntüsü de 1972’den mi?", lines=[
                beat("caly", "alternate", "No, this is a later LRO image. NASA's catalog gives an addition date of October 28, 2009. That is not necessarily the date of the exposure, so I do not label it as one.", "Hayır, bu LRO’nun daha sonraki bir görüntüsü. NASA kataloğuna 28 Ekim 2009’da eklenmiş. Ama eklenme tarihiyle çekim tarihi aynı şey değil; o yüzden bunu fotoğrafın çekildiği gün diye sunmuyorum.", "N1")])
        ],
        "alsep": [
            dict(id="composite", en="Why are there two views in this image?", tr="Bu görselde neden iki ayrı görüntü var?", lines=[
                beat("caly", "wide", "NASA combined an orbital view with a surface inset to explain the station. It is an annotated composite, not a single camera frame. I have not verified a separate original photo ID for the inset.", "NASA, istasyonu anlatmak için yörünge görüntüsüyle bir yüzey fotoğrafını birleştirmiş. Yani tek kare değil, açıklamalı bir görsel. Köşedeki fotoğrafın ayrı arşiv numarasını doğrulayamadım.", "N2")]),
            dict(id="data_loss", en="Were all the measurements preserved?", tr="Ölçümlerin hepsi korunabilmiş mi?", lines=[
                beat("caly", "wide", "Not all of them were archived at the time. NASA's historical account describes missing tapes and metadata, followed by efforts to find and restore the records. We should not call it a complete, uninterrupted archive.", "Verilerin bir bölümü zamanında arşivlenmemiş. NASA’nın tarihçesi, kaybolan bantlardan ve onlara ait bilgileri yeniden bulma çalışmalarından söz ediyor. Elimizde hiç eksilmeden korunmuş bir arşiv varmış gibi düşünmeyelim.", "N3")])
        ]
    }

    def artifact_source_ids(key):
        ids = list(ARTIFACTS[key]["sources"])
        lines = STORY_BEATS[key] + [b for t in FOLLOWUP_TOPICS[key] for b in t["lines"]]
        for b in lines:
            for source in b["sources"]:
                if source not in ids:
                    ids.append(source)
        return ids
