testcase demo_journey:
    assert eval config.save_directory == "caly-demo-apollo17-v1"
    assert eval set(ARTIFACTS) == {"rover", "wheels", "descent", "alsep"}
    assert eval len(PHOTO_RECORDS) == 3 and set(LOCATIONS) == {"moon", "alsep"}
    run Language("turkish")
    run Preference("text speed", 0)
    run ShowMenu("main_menu")
    screenshot "qa/demo_menu_tr.png"
    click id "start_exploration"
    advance until screen "choice"
    screenshot "qa/demo_choices_tr.png"
    click "Bana etrafı gösterir misin?"
    advance until screen "first_artifact"
    click "ALSEP istasyonu"
    click id "first_alsep"
    pause .3
    run QuickSave()
    click pos (1000, 500)
    run QuickLoad(confirm=False)
    pause .3
    assert eval "alsep" not in found
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval found == ["alsep"]
    click id "topic_composite"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval "alsep:composite" in topic_seen
    click id "topic_data_loss"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval not renpy.get_widget("investigation_topics", "topic_data_loss").is_sensitive()
    click "Fotoğrafa ve kaynaklara bak"
    assert screen "artifact_record"
    screenshot "qa/demo_record_tr.png"
    click "CALY’YE DÖN"
    click id "leave_story"
    assert screen "field_scene"
    click "Araç / Modül"
    screenshot "qa/demo_photo_tr.png"
    click id "hotspot_wheels"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval "wheels" in found and destination == "moon"
    click id "topic_visible_frame"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval "wheels:visible_frame" in topic_seen
    click id "topic_wheel_condition"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval not renpy.get_widget("investigation_topics", "topic_wheel_condition").is_sensitive()
    click id "leave_story"
    click id "hotspot_rover"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval "rover" in found
    click id "topic_photo_moment"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval "rover:photo_moment" in topic_seen
    click id "topic_preservation"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    run QuickSave()
    run QuickLoad(confirm=False)
    pause .3
    assert eval not renpy.get_widget("investigation_topics", "topic_preservation").is_sensitive()
    screenshot "qa/demo_topics_tr.png"
    click "Fotoğrafa ve kaynaklara bak"
    assert screen "artifact_record"
    screenshot "qa/demo_rover_sources_tr.png"
    click "CALY’YE DÖN"
    click id "leave_story"
    click id "hotspot_descent"
    click pos (1000, 500) until eval cutscene_shot == "alternate" timeout 30.0
    assert eval cutscene_alternate(cutscene_key) == "images/moon/PIA12920.jpg"
    screenshot "qa/demo_orbital_tr.png"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval len(found) == TOTAL_ARTIFACTS == 4 and destination == "moon"
    click id "topic_return_route"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval "descent:return_route" in topic_seen
    click id "topic_orbital_date"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval len(topic_seen) == 8
    click id "leave_story"
    advance until screen "mission_complete"
    assert eval journey_complete and finale_seen
    pause .4
    screenshot "qa/demo_complete_tr.png"
    click "YENİDEN KEŞFET"
    click "ARŞİV 4/4"
    assert screen "archive"
    pause .3
    screenshot "qa/demo_archive_tr.png"
    click "Apollo 17 ALSEP istasyonu"
    assert screen "investigation_topics"
    click "Hikâyeyi yeniden dinle"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval len(found) == 4
    assert eval len(topic_seen) == 8
    click id "leave_story"
    run Show("source_terminal")
    screenshot "qa/demo_credits_tr.png"
    click "KAPAT"

testcase demo_english:
    run Language(None)
    run Preference("text speed", 0)
    run ShowMenu("main_menu")
    click id "start_exploration"
    advance until screen "choice"
    click "Let us explore."
    advance until screen "first_artifact"
    click id "first_descent"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    assert eval found == ["descent"]
    click id "leave_story"
    assert screen "field_scene"
    screenshot "qa/demo_photo_en.png"
    run Show("archive")
    assert screen "archive"
    click "RETURN"
    run ShowMenu("preferences")
    click "Türkçe"
    assert eval _preferences.language == "turkish"

testcase demo_defaults:
    assert eval _preferences.language == "turkish"
    assert eval persistent.caly_found == []
    assert eval config.name == "CALY — APOLLO 17 DEMO"
    assert eval config.save_directory == "caly-demo-apollo17-v1"

testcase demo_opening_questions:
    run Language("turkish")
    run Preference("text speed", 0)
    run ShowMenu("main_menu")
    click id "start_exploration"
    advance until screen "choice"
    click "Sen burada ne yapıyorsun?"
    advance until screen "first_artifact"
    assert screen "first_artifact"
    run ShowMenu("main_menu")
    click id "start_exploration"
    pause .5
    advance until screen "choice" timeout 30.0
    click "Neye bakacağız?"
    advance until screen "first_artifact"
    assert screen "first_artifact"

testcase demo_legacy_resume:
    run Language("turkish")
    run Preference("text speed", 0)
    run ShowMenu("main_menu")
    click id "start_exploration"
    advance until screen "choice"
    click "Bana etrafı gösterir misin?"
    advance until screen "first_artifact"
    click id "first_rover"
    click pos (1000, 500) until screen "investigation_topics" timeout 30.0
    click id "leave_story"
    click id "hotspot_wheels"
    pause .3
    run SetVariable("dialogue_revision", 0)
    run QuickSave()
    run QuickLoad(confirm=False)
    pause .3
    assert screen "field_scene"
    assert eval dialogue_revision == 2
    assert eval found == ["rover"]
    assert eval story_seen == ["rover"]
    assert eval cutscene_key is None and not location_photo_visible

testcase demo_quick_controls:
    run Language(None)
    run Preference("text speed", 0)
    run ShowMenu("main_menu")
    click id "start_exploration"
    pause 1.0
    assert screen "caly_say"
    screenshot "qa/quick_controls_en.png"
    click id "vn_history"
    assert screen "history"
    click "Return"
    click id "vn_save"
    assert screen "save"
    click "Return"
    click id "vn_prefs"
    assert screen "preferences"
    click "Return"
    click id "vn_auto"
    assert eval _preferences.afm_enable
    click id "vn_auto"
    assert eval not _preferences.afm_enable
    click id "vn_qsave"
    click pos (1000, 500)
    click id "vn_qload"
    assert screen "confirm"
    click "Yes"
    pause .3
    assert screen "caly_say"
    assert eval found == [] and quick_menu
    run Language("turkish")
    advance until screen "choice"
    screenshot "qa/quick_controls_tr.png"
    click "Bana etrafı gösterir misin?"
    advance until screen "first_artifact"
    run Show("source_terminal")
    pause .3
    screenshot "qa/credits_simplified_tr.png"
    assert screen "source_terminal"
    click "KAPAT"
