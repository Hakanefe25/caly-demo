default destination = "moon"
default found = []
default persistent.caly_found = []
default finale_seen = False
default dialogue_revision = 0

label start:
    $ dialogue_revision = 2
    $ found = []
    $ story_seen = []
    $ topic_seen = []
    $ finale_seen = False
    $ journey_complete = False
    $ destination = "moon"
    $ scene_view = None
    $ cutscene_key = None
    $ quick_menu = True
    window hide
    call lunar_arrival
    call opening
    call location_intro
    call screen first_artifact
    if _return is not None:
        call investigation(_return)
    jump expedition

label expedition:
    $ renpy.retain_after_load()
    call screen field_scene
    $ event = _return
    if isinstance(event, tuple) and event[0] == "story":
        call investigation(event[1])
    elif event == "finish":
        $ finale_seen = True
        call closing
        call screen mission_complete
    jump expedition

label after_load:
    $ quick_menu = True
    # Old saves may point into the retired summary/note loop. Resume at the
    # photographs with completed discoveries intact, rather than repeating it.
    if dialogue_revision < 2:
        $ dialogue_revision = 2
        $ story_seen = list(found)
        $ topic_seen = []
        $ cutscene_key = None
        $ location_photo_visible = False
        $ story_show_caly = True
        $ destination = "moon"
        $ scene_view = "alsep" if scene_view == "alsep" else None
        $ finale_seen = journey_complete
        jump expedition
    if len(found) < TOTAL_ARTIFACTS:
        $ finale_seen = False
    return
