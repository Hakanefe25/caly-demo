init offset = 5

style terminal_text is default:
    font "DejaVuSans.ttf"
    size 20
    color "#e1edf1"
style terminal_small is terminal_text:
    size 14
    color "#9cb5c3"
style terminal_label is terminal_text:
    size 15
    color "#73e5dc"
    kerning 2
style terminal_title is terminal_text:
    size 38
style terminal_button is button:
    background Solid("#112b3bea")
    hover_background Solid("#245668")
    selected_background Solid("#245668")
    padding (18, 12)
style terminal_button_text is terminal_text:
    size 17
    hover_color "#a4fff3"
    insensitive_color "#657681"
style terminal_panel is frame:
    background Solid("#0b1b29f5")
    padding (28, 24)

transform arrive:
    alpha 0.0
    linear .22 alpha 1.0

screen caly_portrait(w=260, h=380):
    if renpy.loadable("images/caly/caly_narrator.png"):
        add "images/caly/caly_narrator.png" xysize (w,h) fit "contain"
    else:
        text _("CALY / SIGNAL ONLINE") style "terminal_label"

# Generated screens.rpy remains intact for save/load, settings and accessibility.
screen main_menu():
    tag menu
    add Solid("#07101d")
    add safe_photo("images/moon/apollo17.jpg") xysize (1280,720) fit "cover" alpha .30
    add Solid("#06111bb0") xsize 710
    add Solid("#56e3d1") xpos 64 ypos 69 xsize 48 ysize 3
    vbox:
        xpos 64 ypos 100 spacing 14
        text _("UHRET / EXPLORATION ARCHIVE") style "terminal_label"
        text _("CALY") style "terminal_title" size 88 kerning 12
        text N("APOLLO 17 · DEMO", "APOLLO 17 · DEMO") style "terminal_title" size 44 kerning 6
        text N("One mission. Four stories left on the Moon.", "Tek görev. Ay’da kalan dört hikâye.") style "terminal_small" size 19
        null height 18
        textbutton _("START EXPLORATION →") id "start_exploration" style "terminal_button" xsize 365 action Start()
        if FileLoadable(1, page="quick"):
            textbutton _("CONTINUE") id "continue_expedition" style "terminal_button" xsize 365 action QuickLoad()
        textbutton _("MISSION ARCHIVE") style "terminal_button" xsize 365 action Show("archive", journal=True)
        hbox:
            spacing 12
            textbutton _("SETTINGS") style "terminal_button" action ShowMenu("preferences")
            textbutton _("CREDITS / SOURCES") style "terminal_button" action Show("source_terminal")
    frame:
        xpos 830 ypos 145 xsize 340 ysize 330
        background Solid("#0d2432a0")
        use caly_portrait(330,310)
    text _("CALY / EXTRATERRESTRIAL MACHINERY SPECIALIST") xpos 800 ypos 500 style "terminal_label" size 12
    text _("Caly's Check Engine Club – UHRET") xpos 64 ypos 672 style "terminal_small"
    text "APOLLO 17 / DEMO" xpos 900 ypos 678 style "terminal_small" size 12

screen field_scene():
    use mission_photo_picker(return_event=True)
    if len(found) == TOTAL_ARTIFACTS and not finale_seen:
        timer .3 action Return("finish")
    key "game_menu" action ShowMenu("preferences")

# Compatibility entry for older saves: all investigations now use the VN flow.
screen artifact_inspection(key, reviewing=False):
    modal True
    timer .01 action [Hide("artifact_inspection"), Call("investigation", key)]

screen archive(journal=False):
    modal True
    zorder 40
    $ entries = persistent.caly_found if journal else found
    add Solid("#06101bf5")
    frame at arrive:
        style "terminal_panel" xpos 80 ypos 50 xsize 1120 ysize 620
        vbox:
            spacing 8
            text N("APOLLO 17 ARCHIVE / [len(entries)] OF 4", "APOLLO 17 ARŞİVİ / [len(entries)] / 4") style "terminal_label"
            text _("Machines with a past.") style "terminal_title"
            text (_("Lifetime journal · preserved between expeditions") if journal else _("Current expedition · select a discovery to review")) style "terminal_small"
            for key in ARTIFACT_ORDER:
                hbox:
                    spacing 16
                    text (_("LOGGED") if key in entries else _("UNSCANNED")) style "terminal_label" xsize 140 yalign .5
                    textbutton tr_art(key, "name") style "terminal_button" xsize 700 ypadding 7 sensitive key in entries action [Hide("archive"), Call("investigation", key)]
            hbox:
                spacing 12
                textbutton _("RETURN") style "terminal_button" action Hide("archive")
                if not journal:
                    textbutton _("MOON") style "terminal_button" action [SetVariable("destination","moon"),Hide("archive")]
                    textbutton _("MISSION SUMMARY") style "terminal_button" sensitive len(found)==TOTAL_ARTIFACTS action [Hide("archive"), Show("mission_complete")]
    key "game_menu" action Hide("archive")

screen mission_complete():
    modal True
    zorder 60
    add Solid("#06121ff5")
    frame:
        xpos 90 ypos 170 xsize 280 ysize 260
        background Solid("#102d3b")
        use caly_portrait(260,240)
    vbox at arrive:
        xpos 450 ypos 120 xsize 720 spacing 24
        text N("APOLLO 17 DEMO COMPLETE / 4 OF 4", "APOLLO 17 DEMOSU TAMAMLANDI / 4 / 4") style "terminal_label"
        text _("Left behind.\nStill telling stories.") style "terminal_title" size 48
        text N("Thank you for playing the Apollo 17 demo.", "Apollo 17 demosunu oynadığınız için teşekkür ederiz.") style "terminal_text" size 23
        text N("Dialogue is fictional. Historical sources are linked in each discovery.", "Diyaloglar kurgusaldır. Tarihî kaynaklara her keşfin içinden ulaşabilirsin.") style "terminal_small"
        hbox:
            spacing 12
            textbutton _("EXPLORE AGAIN") style "terminal_button" action (Hide("mission_complete") if renpy.get_screen("field_scene") else Return())
            textbutton _("CREDITS / SOURCES") style "terminal_button" action Show("source_terminal")

screen source_terminal():
    modal True
    zorder 80
    add Solid("#050e1afa")
    frame:
        style "terminal_panel" xpos 70 ypos 35 xsize 1140 ysize 650
        vbox:
            spacing 16
            text _("CREDITS / SOURCE REGISTER") style "terminal_label"
            text _("Built with curiosity. Grounded in records.") style "terminal_title" size 32
            viewport:
                xsize 1080 ysize 450 mousewheel True draggable True scrollbars "vertical"
                vbox:
                    xsize 1030 spacing 13
                    text _("Caly's Check Engine Club – UHRET\nAI assistance: OpenAI Codex assisted programming, interface design, and source-based writing. No AI-generated historical images were used.") style "terminal_text" size 19
                    text N("Apollo 17 surface photo: NASA/Harrison Schmitt. Orbital view: PIA12920, NASA/GSFC/Arizona State University. ALSEP composite: NASA SVS 10818.", "Apollo 17 yüzey fotoğrafı: NASA/Harrison Schmitt. Yörünge görüntüsü: PIA12920, NASA/GSFC/Arizona State University. ALSEP birleşik görseli: NASA SVS 10818.") style "terminal_text" size 18
                    for sid, entry in SOURCES.items():
                        textbutton (sid + " / " + entry[0]) style "terminal_button" text_size 15 action OpenURL(entry[1])
            textbutton _("CLOSE") style "terminal_button" action Hide("source_terminal")
    key "game_menu" action Hide("source_terminal")
