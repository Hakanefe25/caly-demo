# CALY — Apollo 17 Demo

A standalone visual novel about meeting Caly on the Moon and discovering the stories behind equipment left by Apollo 17. Built with Ren’Py 8.5.3, with English and Turkish dialogue and interface options.

Explore marked regions in NASA archive photographs, ask Caly follow-up questions, and revisit discoveries through the archive. The demo covers four subjects:

- The Lunar Roving Vehicle
- Its wire-mesh wheels
- Challenger’s descent stage
- The Apollo 17 ALSEP station

The visit ends with a farewell and a narrated return to Earth. Caly and the visit are fictional; historical information is mapped to official NASA sources.

## Run the demo

Download the [Ren’Py 8.5.3 SDK](https://www.renpy.org/release/8.5.3), select `caly-demo` as a project in the Ren’Py Launcher, and launch it. On Windows, you can also run:

```powershell
.\caly-demo\Launch.ps1 -Sdk 'C:\path\to\renpy-8.5.3-sdk'
```

Alternatively, set `RENPY_SDK` to your SDK directory. A fresh player profile starts in Turkish; select **English** in Settings to switch languages.

## Repository contents

| Path | Contents |
| --- | --- |
| `caly-demo/game/` | Ren’Py scripts, English/Turkish dialogue, interface assets, and images |
| `caly-demo/Launch.ps1` | Windows launcher for an installed Ren’Py SDK |
| `caly-demo/README.md` | Demo flow, controls, and save behavior |
| [SOURCES.md](SOURCES.md) | Official references, claim mapping, image credits, hashes, and verification limits |

The repository contains the source project. Generated web deployments, the SDK, player saves, and local account settings are excluded.

## Sources and artwork

Historical photographs and scientific information use NASA sources. Each discovery includes links to its references. Caly’s lunar scenes are AI-generated fictional illustrations, rather than photographs of the historical landing site. Asset provenance and unresolved attribution details are documented in [SOURCES.md](SOURCES.md).

No blanket reuse license is granted for the included images. The engine and third-party components retain their respective licenses.

## Validation

The native Apollo 17 journey test passed 25 assertions covering all four stories, eight follow-up questions, quick save/load, the archive, story replay, and the ending. Test definitions are in `caly-demo/game/testcases.rpy`. These results do not establish compatibility with every browser or mobile device.
