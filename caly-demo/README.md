# caly-demo — Apollo 17

A standalone Ren’Py project. Version: **0.3-demo**.

The demo takes place on the Moon and covers four Apollo 17 discoveries: the Lunar Roving Vehicle, its wire-mesh wheels, Challenger’s descent stage, and the ALSEP station.

## Story and exploration

An Apollo 17 archive photograph introduces the landing. After meeting Caly, choose marked regions in the photographs to explore the four stories in any order. Each story uses full photographs, detail crops, and relevant archive imagery. Completing the discoveries leads to a farewell, a narrated return to Earth, and the ending screen.

The four main stories contain 32 dialogue lines, with two optional follow-up questions per discovery. Answered questions are marked and disabled for the current playthrough. The main story plays again only when you select its replay option. Completed discoveries can be revisited from the archive.

## Language and controls

A new profile starts in Turkish. Select **English** in Settings to switch languages.

Clickable regions remain marked. A bottom-center quick menu provides Back, History, Skip, Auto, Save, Quick Save, Quick Load, and Preferences. It is hidden while source panels and game menus are open.

## Running the source project

Select this directory in the Ren’Py 8.5.3 Launcher; `game/` is directly inside it. On Windows, from this directory:

```powershell
.\Launch.ps1 -Sdk 'C:\path\to\renpy-8.5.3-sdk'
```

You can also set `RENPY_SDK` instead of passing `-Sdk`.

## Saves

The save directory is `caly-demo-apollo17-v1`, separate from the full game. Current saves resume at the saved line. When loading a version 0.1 save, completed discoveries are retained and exploration resumes at the photograph picker to avoid the retired dialogue loop.

## Provenance

[SOURCES.md](SOURCES.md) maps the demo’s scientific claims and photographs to official references. Three NASA archive/scientific images are included. Caly’s two lunar scenes are fictional AI-generated illustrations. The supplied narrator portrait is also fictional character artwork.
