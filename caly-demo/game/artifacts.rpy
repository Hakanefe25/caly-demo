init python:
    SOURCES = {'M1': ('Apollo 17: Gene Cernan in Lunar Roving Vehicle',
            'https://science.nasa.gov/resource/apollo-17-gene-cernan-in-lunar-roving-vehicle/'),
     'M2': ('Apollo 17 mission summary / NASA SP-4029',
            'https://www.nasa.gov/wp-content/uploads/static/history/SP-4029/Apollo_17a_Summary.htm'),
     'M3': ('Reinventing the Wheel / NASA Glenn', 'https://www3.nasa.gov/specials/wheels/'),
     'M4': ('Human Artifacts on the Moon',
            'https://www.nasa.gov/wp-content/uploads/static/history/humanartifacts.html'),
     'M5': ('Apollo 17 Mission Details', 'https://www.nasa.gov/missions/apollo/apollo-17-mission-details/'),
     'M6': ('NASA / Apollo 17 exploration and rover parking',
            'https://www.nasa.gov/history/50-years-ago-apollo-17-lands-at-taurus-littrow/'),
     'N1': ('NASA / Apollo 17 descent stage / PIA12920',
            'https://science.nasa.gov/photojournal/exploring-the-apollo-17-site/'),
     'N2': ('NASA SVS / Apollo 17 ALSEP', 'https://svs.gsfc.nasa.gov/10818/'),
     'N3': ('NASA / ALSEP data and history', 'https://ntrs.nasa.gov/citations/20190032593')}
    LOCATIONS = {'moon': {'title': 'Tracks at Taurus-Littrow',
              'subtitle': 'MOON / APOLLO 17 / DECEMBER 1972',
              'image': 'images/moon/apollo17.jpg',
              'size': (1600, 856),
              'credit': 'NASA / Harrison Schmitt · Apollo 17 / December 1972 / EVA 1',
              'ids': ['rover', 'wheels', 'descent']},
     'alsep': {'title': 'ALSEP',
               'subtitle': 'APOLLO 17 / ALSEP',
               'image': 'images/moon/alsep.jpg',
               'size': (1024, 576),
               'credit': 'NASA SVS / 10818 / Apollo 17 ALSEP · annotated visualization',
               'ids': ['alsep']}}
    ARTIFACTS = {'rover': {'name': 'Lunar Roving Vehicle',
               'tag': '01 / A FIELD LAB WITH WHEELS',
               'place': 'moon',
               'date': 'Apollo 17 · December 1972',
               'rect': (0.245, 0.62, 0.18, 0.15),
               'crop': (190, 385, 740, 460),
               'sources': ['M1', 'M5', 'M6']},
     'wheels': {'name': 'Wire-mesh wheels',
                'tag': '02 / ENGINEERING THE CONTACT PATCH',
                'place': 'moon',
                'date': 'Apollo 17 · December 1972',
                'rect': (0.42, 0.78, 0.105, 0.19),
                'crop': (625, 610, 280, 235),
                'sources': ['M3', 'M6', 'M4']},
     'descent': {'name': 'Challenger descent stage',
                 'tag': '03 / THE LOWER STAGE',
                 'place': 'moon',
                 'view': 'moon',
                 'date': 'Apollo 17 · December 1972',
                 'rect': (0.57, 0.46, 0.28, 0.33),
                 'crop': (850, 390, 590, 300),
                 'sources': ['M1', 'M2', 'M5', 'N1']},
     'alsep': {'name': 'Apollo 17 ALSEP station',
               'tag': '04 / SCIENCE AFTER DEPARTURE',
               'place': 'moon',
               'view': 'alsep',
               'date': 'Deployed in 1972 · ALSEP program ended in 1977',
               'rect': (0.5, 0.16, 0.29, 0.55),
               'crop': (500, 90, 315, 325),
               'sources': ['N2', 'N3', 'M2']}}
    ARTIFACT_ORDER = ['rover', 'wheels', 'descent', 'alsep']
    TOTAL_ARTIFACTS = 4
    PHOTO_RECORDS = {'images/moon/apollo17.jpg': ('Taurus-Littrow / Apollo 17 / Dec 1972 / first moonwalk',
                                  'Taurus-Littrow / Apollo 17 / Aralık 1972 / ilk Ay yürüyüşü',
                                  'NASA/Harrison Schmitt',
                                  'M1'),
     'images/moon/PIA12920.jpg': ('Taurus-Littrow / LRO / PIA12920 / later orbital view',
                                  'Taurus-Littrow / LRO / PIA12920 / sonradan çekilen yörünge görüntüsü',
                                  'NASA/GSFC/Arizona State University',
                                  'N1'),
     'images/moon/alsep.jpg': ('Apollo 17 ALSEP / SVS 10818 / annotated composite',
                               'Apollo 17 ALSEP / SVS 10818 / açıklamalı birleşik görsel',
                               'NASA SVS',
                               'N2')}

init python:
    def safe_photo(path):
        return path if renpy.loadable(path) else Solid("#08070e")
    def mark_discovered(key):
        if key not in found:
            store.found = found + [key]
        if key not in persistent.caly_found:
            persistent.caly_found = persistent.caly_found + [key]
        renpy.save_persistent()
    def active_scene():
        return "alsep" if scene_view == "alsep" else "moon"
    def artifact_scene(key):
        return ARTIFACTS[key].get("view", "moon")
    def cutscene_alternate(key):
        return {"descent":"images/moon/PIA12920.jpg", "alsep":"images/moon/alsep.jpg"}.get(key, "images/moon/apollo17.jpg")
    def photo_caption(path):
        en, tr, credit, source = PHOTO_RECORDS[path]
        return N(en, tr) + " · " + credit

default scene_view = None
default cutscene_key = None
default cutscene_shot = "caly"
default location_photo_visible = False
