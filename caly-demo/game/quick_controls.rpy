init offset = 10

# Keep the standard Ren'Py overlay, with one understated row for the VN scenes.
screen quick_menu():
    zorder 100
    $ vn_visible = any(renpy.get_screen(s) for s in ("caly_say", "choice", "first_artifact", "field_scene", "investigation_topics"))
    $ panel_open = any(renpy.get_screen(s) for s in ("source_terminal", "artifact_record", "archive", "mission_complete"))
    if quick_menu and not main_menu and not renpy.context()._menu and vn_visible and not panel_open:
        hbox:
            xalign .5 yalign 1.0 yoffset -1
            spacing 14
            textbutton _("Back") id "vn_back" style "vn_quick_button" action Rollback()
            textbutton _("History") id "vn_history" style "vn_quick_button" action ShowMenu("history")
            textbutton _("Skip") id "vn_skip" style "vn_quick_button" action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") id "vn_auto" style "vn_quick_button" action Preference("auto-forward", "toggle")
            textbutton _("Save") id "vn_save" style "vn_quick_button" action ShowMenu("save")
            textbutton _("Q.Save") id "vn_qsave" style "vn_quick_button" action QuickSave()
            textbutton _("Q.Load") id "vn_qload" style "vn_quick_button" action QuickLoad()
            textbutton _("Prefs") id "vn_prefs" style "vn_quick_button" action ShowMenu("preferences")

style vn_quick_button is button:
    background None
    hover_background None
    padding (3, 3)

style vn_quick_button_text is default:
    font "DejaVuSans.ttf"
    size 13
    color "#c4bdb5"
    hover_color "#ffffff"
    selected_color "#f4e5c7"
    insensitive_color "#766f69"
    outlines [(1, "#000000b0", 0, 1)]
