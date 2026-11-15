# caly-demo — Apollo 17 source record

The NASA references used in the demo were verified against official source content on November 14, 2026. This record covers the demo’s claims and images. Caly, the player, the visit, personal dialogue, farewell, and return journey are fiction, rather than historical testimony or an actual crewed tourism mission.

Paths below are relative to the `caly-demo/` project directory.

## Official references

| Key | Official NASA source | Information supported in the demo |
| --- | --- | --- |
| M1 | [Apollo 17: Gene Cernan in Lunar Roving Vehicle](https://science.nasa.gov/resource/apollo-17-gene-cernan-in-lunar-roving-vehicle/) | Taurus-Littrow; Eugene Cernan driving during the first moonwalk; the Lunar Module in the background; the page’s historical date of December 11, 1972; NASA/Harrison Schmitt credit. |
| M2 | [Apollo 17 summary / NASA SP-4029](https://www.nasa.gov/wp-content/uploads/static/history/SP-4029/Apollo_17a_Summary.htm) | The December 1972 mission, rover use, geological investigation, samples, ALSEP deployment, ascent-stage docking with the CSM, crew/sample transfer, and preparation for Earth return. M6 supports the final parking position. |
| M3 | [Reinventing the Wheel / NASA Glenn](https://www3.nasa.gov/specials/wheels/) | Historical LRV section: flexible wire-mesh wheels, an internal frame limiting excessive deflection, and strips aiding traction on soft ground. Outdated current-vehicle-status statements are not used. |
| M4 | [Human Artifacts on the Moon](https://www.nasa.gov/wp-content/uploads/static/history/humanartifacts.html) | The historical and scientific value of lunar equipment and the preservation approach. |
| M5 | [Apollo 17 Mission Details](https://www.nasa.gov/missions/apollo/apollo-17-mission-details/) | Battery-powered LRV; Challenger’s name; the ascent stage carrying the crew to lunar orbit and docking with the CSM. Distance/speed statistics are omitted because source summaries differ. |
| M6 | [50 Years Ago: Apollo 17 Lands at Taurus-Littrow](https://www.nasa.gov/history/50-years-ago-apollo-17-lands-at-taurus-littrow/) | Surface exploration, samples, photographic records, Cernan driving the rover to its final VIP parking site, and television coverage of liftoff from that site. |
| N1 | [Exploring the Apollo 17 Site / PIA12920](https://science.nasa.gov/photojournal/exploring-the-apollo-17-site/) | The Challenger descent stage imaged later by LRO. The catalog date is not presented as the image acquisition date. |
| N2 | [NASA SVS 10818](https://svs.gsfc.nasa.gov/10818/) | An annotated visualization combining an orbital view with an Apollo 17 ALSEP surface inset; Chris Smith / NASA SVS. |
| N3 | [Recovery, Restoration and Archiving of Previously Lost ALSEP Data / NTRS 20190032593](https://ntrs.nasa.gov/citations/20190032593) | ALSEP on five missions, measurements after crew departure, the September 1977 program ending, and recovery/archiving of historical data and metadata. Uninterrupted operation of every instrument is not claimed. |

## Claim mapping

English and Turkish dialogue carry the same scientific claims. `game/story_data.rpy` contains 32 main-story lines across four stories and answers to eight optional questions. Each line records its speaker, shot, and official source keys when it contains factual information. Retired generic summaries have been removed.

| Discovery | Claims and references | Image region and limits |
| --- | --- | --- |
| Lunar Roving Vehicle | Driver, first moonwalk, Lunar Module, and location: M1. Battery: M5. Research, samples, and records: M2/M6. Final parking and liftoff coverage: M6. Follow-ups: first-moonwalk/final-parking distinction M1/M6; preservation M4. | Seating/crew area in M1. The photograph shows the first moonwalk, not final parking. The same image accompanies the final-task account; an optional answer explains that it does not document the final parking position. |
| Wire-mesh wheels | Construction/function: M3. Internal-frame explanation: M3, not pixel interpretation. The inference that attached wheels remained with the vehicle: M1/M6. | The nearest foreground wheel. The internal frame is not claimed to be clearly visible in the crop. No current inspection of each wheel is implied. |
| Challenger descent stage | Descent/ascent sections and ascent to lunar orbit: M2/M5. Later identification of the remaining lower stage: N1. Crew/sample transfer to the CSM: M2/M5. N1’s October 28, 2009 catalog date is not an asserted acquisition date. | Gold-colored lower structure and landing legs, excluding the upper cabin. Material is not inferred from color. The surface photo precedes departure; N1 shows a later orbital view. |
| Apollo 17 ALSEP station | Instruments, post-departure measurements, data transmission, September 1977 program ending, and data recovery: N3. Image/equipment remaining on the surface: N2. Composite: N2. Unarchived data, missing tapes, and metadata: N3. | Instrument group in the right-hand surface inset. This is a composite, not a single camera frame. The inset’s independent original photo ID could not be verified; none has been invented. |

The opening, encounter, personal questions, farewell, and return are fiction. Caly’s preferences and the player’s reactions are not historical testimony. The ending does not repeat all four stories. Unknown damage causes, dimensions, or cost explanations are not invented.

## Included NASA images

| Local file and credit | Official download | SHA-256 |
| --- | --- | --- |
| `game/images/moon/apollo17.jpg` — NASA/Harrison Schmitt; surface scene and rover/wheel/descent-stage crops | [NASA JPEG](https://assets.science.nasa.gov/dynamicimage/assets/science/psd/lunar-science/2023/09/eugene_cernan-full-a.jpg?w=1600) | `7bbe8df72123f711725e6ce164018c25b7214ed0b21969ca622ea1f82ee6c8f5` |
| `game/images/moon/PIA12920.jpg` — NASA/GSFC/Arizona State University; later orbital view | [NASA JPEG](https://assets.science.nasa.gov/dynamicimage/assets/science/psd/photojournal/pia/pia12/pia12920/PIA12920.jpg?w=1200) | `1e58609db13023b77f5320241aed759af1e012fc564dc40c608ec259caaf0f04` |
| `game/images/moon/alsep.jpg` — NASA SVS 10818; annotated composite | [NASA JPEG](https://svs.gsfc.nasa.gov/vis/a010000/a010800/a010818/apollo_17_alsep_ipod_lg.00127_print.jpg) | `ac2c18d0cc4bbe5f79c74dc61430f7dce2b7a2e63021601f376dbbaf20735f77` |

M1 does not supply a photo ID; no unrelated identifier is assigned. Files were copied byte-for-byte from verified downloads. Runtime detail crops are labeled; no equipment is added to or removed from historical photographs. Clickable markers are navigation aids, not scientific boundaries. Archive scenes preserve aspect ratio; the main menu crops and darkens the photograph for decoration.

NASA content use follows the [official media usage guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/). Credits are displayed without implying endorsement. No claim is made that every NASA website asset is unrestricted in every jurisdiction.

## Verification history and limits

During the version 0.2 review, nine official records were compared with the dialogue. When later NTRS page requests timed out, N3 was also checked through its [official NASA API record](https://ntrs.nasa.gov/api/citations/20190032593): the identifier, title, and abstract supported the September 1977, missing-record, and recovery statements. Official image downloads were fetched again and their SHA-256 hashes matched the local files. The original workspace retains the verification reports; those reports are not bundled here.

Date limit: M1 lists December 11, 1972 as its historical date, while M5 places Cernan’s surface egress on December 12. The time zone and exact exposure time were not separately established. The game therefore labels the image **December 1972 / first moonwalk**, without asserting a verified exact exposure date.

Source keys and shot assignments remain alongside dialogue in `game/story_data.rpy`. No new historical photographs or AI-generated historical equipment were introduced in that review.

## Fictional and other assets

- `game/images/story/caly_moon.png` and `caly_moon_reflect.png`: fictional lunar scenes generated with OpenAI ImageGen using the user-supplied narrator image as the character reference. They do not reconstruct actual Taurus-Littrow terrain, lighting, or historical mission activity. Caly’s clothing and presence are fictional. The game labels the landscape as fictional.
- `game/images/caly/caly_narrator.png`: user-supplied fictional character artwork, not a NASA photograph. Its artist, original production method, and redistribution rights could not be verified.
- Interface elements, markers, and transitions use Ren’Py components. Standard GUI assets and the font were copied from the existing Ren’Py project; they are not scientific imagery.
- OpenAI Codex assisted with programming, interface work, and source-based text editing. Historical mission photographs were not generated with AI.
