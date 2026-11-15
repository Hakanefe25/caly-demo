default story_seen = []
default topic_seen = []
default caly_pose = "welcome"
define caly = Character("Caly", screen="caly_say", color="#73e5dc", what_style="caly_dialogue", who_style="caly_name")

# Character injects its what_style into the displayable with id "what".
# Keep the standard say_dialogue's absolute textbox offsets out of this panel.
style caly_name is terminal_label:
    xpos 0
    ypos 0
    xanchor 0
    yanchor 0
    size 21
    color "#73e5dc"

style caly_dialogue is terminal_text:
    xpos 0
    ypos 0
    xanchor 0
    yanchor 0
    xsize 992
    size 20
    outlines [(1, "#000000cc", 0, 1)]
    textalign 0.0
    layout "greedy"

init python:
    def N(en, tr):
        return tr if _preferences.language == "turkish" else en
    def story_line(pair):
        return N(*pair)
    def caly_scene_art():
        return "images/story/caly_moon_reflect.png" if caly_pose == "reflect" else "images/story/caly_moon.png"

screen caly_say(who, what):
    use conversation_stage
    if location_photo_visible:
        use mission_photo_visual()
    frame:
        background Solid("#050509b0")
        padding (24, 16)
        xpos 120 ypos 548 xsize 1040 ysize 152
        vbox:
            xsize 992 spacing 8
            text (N("You", "Sen") if who == "You" else (who or "")) id "who" style "caly_name"
            text localize_dialogue(what) id "what" style "caly_dialogue"

screen conversation_stage():
    add Solid("#08070e")
    $ scene_art = caly_scene_art() if story_show_caly else story_background
    if cutscene_key and cutscene_shot != "caly":
        $ shot_loc = LOCATIONS[artifact_scene(cutscene_key)]
        $ shot_path = cutscene_alternate(cutscene_key) if cutscene_shot == "alternate" else shot_loc["image"]
        if cutscene_shot == "detail" and renpy.loadable(shot_loc["image"]):
            add Crop(ARTIFACTS[cutscene_key]["crop"], shot_loc["image"]) xysize (1280,530) fit "contain" xalign .5
        else:
            add safe_photo(shot_path) xysize (1280,530) fit "contain" xalign .5
        use archive_photo_caption(shot_path, detail=(cutscene_shot == "detail"))
    else:
        add safe_photo(scene_art) xysize (1280,720) fit "cover"
        if scene_art in PHOTO_RECORDS:
            use archive_photo_caption(scene_art)
        else:
            frame:
                xpos 25 ypos 18 background Solid("#040609aa") padding (8,5)
                text N("AI illustration · fictional landscape", "Yapay zekâ çizimi · kurgusal manzara") style "terminal_small" size 11

screen archive_photo_caption(path, detail=False):
    frame:
        xpos 25 ypos 18 xmaximum 1230 background Solid("#040609c9") padding (8,5)
        text (N("DETAIL CROP · ", "AYRINTI KESİTİ · ") if detail else "") + photo_caption(path) style "terminal_small" size 11

style conversation_button is button:
    background Solid("#0a090fc9")
    hover_background Solid("#4b4039dc")
    padding (20, 13)
    xsize 470
style conversation_button_text is terminal_text:
    size 20
    color "#eee7dc"
    hover_color "#ffffff"
    insensitive_color "#938e89"
    xsize 430

screen choice(items):
    use conversation_stage
    vbox:
        xpos 680 yalign .48 spacing 14
        for item in items:
            textbutton item.caption style "conversation_button" action item.action

label opening:
    $ caly_pose = "welcome"
    $ destination = "moon"
    $ story_background = "images/story/caly_moon.png"
    $ story_show_caly = True
    with Dissolve(.6)
    vn "[N('You step out of the lander. Grey dust shifts beneath your boots. Someone standing by a low ridge waves to you.', 'İniş aracından çıkıyorsun. Gri toz, adımlarının altında dağılıyor. Yakındaki bir sırtın yanında duran biri sana el sallıyor.')]"
    caly "[N('Hello! You look like you are about to explore.', 'Merhaba! Biraz etrafa bakınacak gibisin.')]"
    player "[N('I was not expecting to meet anyone here.', 'Burada birine rastlamayı beklemiyordum.')]"
    caly "[N('I am Caly. First visit?', 'Ben Caly. İlk gelişin mi?')]"
    player "[N('Is it that obvious?', 'O kadar belli mi oluyor?')]"
    caly "[N('You cannot take your eyes off the horizon. I remember that feeling.', 'Gözünü ufuktan alamıyorsun. O duyguyu hatırlıyorum.')]"
    $ caly_pose = "reflect"
    with Dissolve(.25)
    menu:
        "[N('What brings you here?', 'Sen burada ne yapıyorsun?')]":
            caly "[N('I study the traces of Apollo 17. Finding a machine is one thing; finding out what it did takes a little longer.', 'Apollo 17’den kalan izleri araştırıyorum. Bir makineyi bulmak başka, ne işe yaradığını öğrenmek başka. Asıl o kısmı seviyorum.')]"
            player "[N('Do you work alone?', 'Tek başına mı çalışıyorsun?')]"
            caly "[N('Usually. Today I seem to have company.', 'Genellikle. Ama bugün bana eşlik edecek biri var gibi.')]"
        "[N('What will we look at?', 'Neye bakacağız?')]":
            caly "[N('Equipment used during the landing and the surface work. I have the mission photographs with me.', 'İnişte ve yüzey araştırmalarında kullanılan donanıma. Görev fotoğrafları yanımda.')]"
            player "[N('A sort of open-air museum?', 'Bir tür açık hava müzesi yani?')]"
            caly "[N('That is how I like to think of it.', 'Ben öyle düşünmeyi seviyorum.')]"
        "[N('Let us explore.', 'Bana etrafı gösterir misin?')]":
            caly "[N('Of course. Come with me.', 'Tabii. Gel benimle.')]"
    return

label location_intro:
    $ scene_view = None
    $ location_photo_visible = True
    $ caly_pose = "welcome"
    $ story_show_caly = True
    caly "[N('This is an Apollo 17 photograph from Taurus-Littrow. The rover and Lunar Module are in this frame; the ALSEP station has its own image.', 'Bu, Apollo 17’nin Taurus-Littrow’da çekilmiş bir fotoğrafı. Araç ve Ay Modülü bu karede; ALSEP istasyonunun görseli de diğer sekmede.')]"
    $ location_photo_visible = False
    return

label investigation(key):
    $ cutscene_key = key
    $ destination = ARTIFACTS[key]["place"]
    $ scene_view = ARTIFACTS[key].get("view")
    $ cutscene_shot = "caly"
    $ story_show_caly = True
    if key not in story_seen:
        call investigation_story(key)
    label .questions:
        $ cutscene_shot = "caly"
        $ caly_pose = "reflect"
        call screen investigation_topics(key)
        $ topic = _return
        if topic == "leave":
            $ cutscene_key = None
            return
        if topic == "replay":
            call investigation_story(key)
        elif topic == "record":
            $ cutscene_shot = "wide"
            call screen artifact_record(key)
        else:
            $ selected_topic = next((t for t in FOLLOWUP_TOPICS[key] if t["id"] == topic), None)
            if selected_topic is not None and key + ":" + topic not in topic_seen:
                $ renpy.retain_after_load()
                $ cutscene_shot = selected_topic["lines"][0]["shot"]
                $ player(story_line((selected_topic["en"], selected_topic["tr"])))
                $ followup_index = 0
                while followup_index < len(selected_topic["lines"]):
                    $ current_beat = selected_topic["lines"][followup_index]
                    $ cutscene_shot = current_beat["shot"]
                    $ caly(story_line((current_beat["en"], current_beat["tr"])))
                    $ followup_index += 1
                $ topic_seen = topic_seen + [key + ":" + topic]
    jump .questions

label investigation_story(key):
    $ caly_pose = "welcome"
    $ line_index = 0
    $ renpy.retain_after_load()
    while line_index < len(STORY_BEATS[key]):
        $ current_beat = STORY_BEATS[key][line_index]
        $ cutscene_shot = current_beat["shot"]
        $ caly_pose = "reflect" if line_index >= len(STORY_BEATS[key]) // 2 else "welcome"
        if current_beat["who"] == "player":
            $ player(story_line((current_beat["en"], current_beat["tr"])))
        else:
            $ caly(story_line((current_beat["en"], current_beat["tr"])))
        $ line_index += 1
    $ story_seen = list(set(story_seen + [key]))
    $ mark_discovered(key)
    return

screen investigation_topics(key):
    modal True
    use conversation_stage
    vbox:
        xpos 650 ypos 75 spacing 12
        text tr_art(key,"name") style "terminal_title" size 28
        for item in FOLLOWUP_TOPICS[key]:
            $ heard = key + ":" + item["id"] in topic_seen
            button:
                id ("topic_" + item["id"])
                style "conversation_button"
                sensitive (not heard)
                action Return(item["id"])
                text (("✓ " if heard else "") + N(item["en"], item["tr"])) style "conversation_button_text"
        textbutton N("Replay this story", "Hikâyeyi yeniden dinle") style "conversation_button" action Return("replay")
        textbutton N("Photograph and sources", "Fotoğrafa ve kaynaklara bak") style "conversation_button" action Return("record")
        textbutton N("Investigate something else", "Diğer parçalara da bakalım") id "leave_story" style "conversation_button" action Return("leave")
    key "game_menu" action Return("leave")

screen artifact_record(key):
    modal True
    use conversation_stage
    frame:
        background Solid("#050509d9") padding (24,20)
        xpos 650 ypos 70 xsize 550 ysize 440
        vbox:
            spacing 15
            text tr_art(key,"name") style "terminal_title" size 25
            text N("Official sources", "Resmî kaynaklar") style "terminal_label"
            viewport:
                xsize 502 ysize 220 mousewheel True draggable True scrollbars "vertical"
                vbox:
                    spacing 8
                    for sid in artifact_source_ids(key):
                        textbutton (sid + " / " + SOURCES[sid][0]) style "conversation_button" xsize 460 text_xsize 420 text_size 15 action OpenURL(SOURCES[sid][1])
            textbutton N("RETURN TO CALY", "CALY’YE DÖN") style "conversation_button" action Return()
    key "game_menu" action Return()

label closing:
    $ cutscene_key = None
    $ caly_pose = "reflect"
    $ story_show_caly = True
    caly "[N('I think this is a good place to finish for today.', 'Sanırım bugünü burada noktalayabiliriz.')]"
    player "[N('I never thought one photograph would give me so many questions.', 'Bir fotoğrafa bakıp bu kadar soru soracağımı düşünmemiştim.')]"
    caly "[N('A good question makes you look a little closer.', 'İyi bir soru, insanı daha dikkatli bakmaya zorluyor.')]"
    call homecoming
    return

init 20 python:
    def localize_dialogue(value):
        lines = [b for story in STORY_BEATS.values() for b in story]
        lines += [b for topics in FOLLOWUP_TOPICS.values() for t in topics for b in t["lines"]]
        for b in lines:
            if value in (b["en"], b["tr"]):
                return N(b["en"], b["tr"])
        for topics in FOLLOWUP_TOPICS.values():
            for t in topics:
                if value in (t["en"], t["tr"]):
                    return N(t["en"], t["tr"])
        return value
