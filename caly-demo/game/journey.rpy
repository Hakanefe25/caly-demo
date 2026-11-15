default story_background = "images/moon/apollo17.jpg"
default story_show_caly = True
default journey_complete = False
define vn = Character(None, screen="caly_say", what_style="caly_dialogue")
define player = Character("You", screen="caly_say", what_style="caly_dialogue", who_style="caly_name")

label lunar_arrival:
    $ story_show_caly = False
    $ story_background = "images/moon/apollo17.jpg"
    with Dissolve(.5)
    $ renpy.retain_after_load()
    vn "[N('The landing is close. You take one last look at an Apollo 17 archive photograph before putting it away and preparing to leave the cabin.', 'İniş yaklaşıyor. Apollo 17 arşivinden bir fotoğrafa son kez bakıp onu kaldırıyorsun. Kabinden çıkmak için hazırlanma vakti.')]"
    return

label homecoming:
    caly "[N('Your ship will be leaving soon. We should get you back.', 'Geminin kalkış saati yaklaşıyor. Seni geri götürelim.')]"
    player "[N('Will I find you here if I come back?', 'Tekrar gelirsem seni burada bulabilir miyim?')]"
    caly "[N('I am usually around. Give me a shout.', 'Büyük ihtimalle buralarda olurum. Gelince seslen.')]"
    $ story_show_caly = False
    $ story_background = "images/moon/apollo17.jpg"
    with Dissolve(.6)
    vn "[N('On the way back to Earth, you add your notes beside the archive photograph. The visit is over; you still have a few questions for next time.', 'Dünya’ya dönerken notlarını arşiv fotoğrafının yanına ekliyorsun. Gezi bitti. Bir sonraki görüşmeniz için aklında hâlâ birkaç soru var.')]"
    $ journey_complete = True
    return
