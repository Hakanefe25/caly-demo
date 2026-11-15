screen first_artifact():
    modal True
    use mission_photo_picker(return_event=False)


init python:
    def picker_geometry():
        view = LOCATIONS[active_scene()]
        w,h = view["size"]
        scale = min(630.0/w,350.0/h)
        return (int(600+(630-w*scale)/2), int(115+(350-h*scale)/2), int(w*scale), int(h*scale))

screen mission_photo_visual(interactive=False, return_event=False):
    $ view = LOCATIONS[active_scene()]
    $ px,py,pw,ph = picker_geometry()
    add Solid("#040609bd") xpos 590 ypos 105 xysize (650,370)
    add safe_photo(view["image"]) xpos px ypos py xysize (pw,ph)
    if not renpy.loadable(view["image"]):
        text N("ARCHIVE PHOTO MISSING", "ARŞİV FOTOĞRAFI EKSİK") xpos 620 ypos 270 style "terminal_small"
    for key in [k for k in view["ids"] if artifact_scene(k)==active_scene()]:
        $ rx,ry,rw,rh = ARTIFACTS[key]["rect"]
        $ hx,hy,hw,hh = int(px+rx*pw),int(py+ry*ph),int(rw*pw),int(rh*ph)
        if interactive:
            button:
                id (("hotspot_" if return_event else "first_")+key)
                xpos hx ypos hy xsize hw ysize hh padding (0,0)
                background Solid("#66f2df25") hover_background Solid("#66f2df66")
                action Return(("story",key) if return_event else key)
                tooltip tr_art(key,"name")
                text ("✓" if key in found else "+") align (.5,.5) size 24 color "#baffef"
        else:
            add Solid("#66f2df25") xpos hx ypos hy xysize (hw,hh)
            text "+" xpos (hx+hw//2) ypos (hy+hh//2) anchor (.5,.5) size 24 color "#baffef"
    text photo_caption(view["image"]) xpos 600 ypos 480 xsize 630 style "terminal_small" size 10

screen mission_photo_picker(return_event=False):
    use conversation_stage
    use mission_photo_visual(interactive=True, return_event=return_event)
    hbox:
        xpos 600 ypos 55 spacing 10
        for view_id, en, tr in [("moon","Rover / LM","Araç / Modül"),("alsep","ALSEP station","ALSEP istasyonu")]:
            textbutton N(en,tr) style "conversation_button" xsize 250 text_xsize 210 text_size 16 action SetVariable("scene_view",view_id if view_id!=destination else None)
    if return_event:
        hbox:
            xpos 600 ypos 10 spacing 8
            textbutton N("ARCHIVE [len(found)]/4", "ARŞİV [len(found)]/4") style "conversation_button" xsize 180 text_xsize 140 text_size 14 action Show("archive")
    frame:
        background Solid("#050509b0") padding (24,16)
        xpos 120 ypos 548 xsize 1040 ysize 152
        vbox:
            spacing 8 xsize 992
            text "Caly" style "caly_name"
            if not found:
                text N("Which part would you like to examine first? Click a marked region in the photograph.", "İlk olarak hangi parçaya bakmak istersin? Fotoğraftaki işaretli bölgelerden birini seç.") style "caly_dialogue"
            elif len(found) < TOTAL_ARTIFACTS:
                text N("Anything else catch your eye? We can look at another part.", "Başka merak ettiğin bir parça var mı? Ona da bakalım.") style "caly_dialogue"
            else:
                text N("You can revisit a story through the archive whenever you like.", "İstediğin zaman arşivden bir hikâyeyi yeniden açabilirsin.") style "caly_dialogue"
            if GetTooltip():
                text GetTooltip() style "terminal_small"
