init python:
    TURKISH_ART = {'rover': ['Ay Keşif Aracı', '01 / AY’DA SAHA ÇALIŞMASI', 'Apollo 17 · Aralık 1972'],
     'wheels': ['Tel örgü tekerlekler', '02 / TEL ÖRGÜDEN TEKERLEKLER', 'Apollo 17 · Aralık 1972'],
     'descent': ['Challenger iniş kademesi', '03 / İNİŞ KADEMESİ', 'Apollo 17 · Aralık 1972'],
     'alsep': ['Apollo 17 ALSEP istasyonu',
               '04 / EKİPTEN SONRA DA ÇALIŞAN CİHAZLAR',
               '1972’de kuruldu · ALSEP programı 1977’de sona erdi']}

init python:
    def tr_art(key, field):
        fields = ["name", "tag", "date"]
        return TURKISH_ART[key][fields.index(field)] if _preferences.language == "turkish" else ARTIFACTS[key][field]
