param([string]$Sdk=$env:RENPY_SDK)
$ErrorActionPreference='Stop'
if (-not $Sdk) { throw 'Supply -Sdk or set RENPY_SDK to your RenPy 8.5.3 SDK directory.' }
$workspace = Split-Path -Parent $PSScriptRoot
New-Item -ItemType Directory -Path (Join-Path $workspace 'tools\web-support') -Force | Out-Null
$project = Join-Path $workspace 'caly-demo'
$stage = Join-Path $workspace 'tools\web-project'
$deploy = Join-Path $workspace 'vercel-deploy'
$public = Join-Path $deploy 'public'
$runner = Join-Path $Sdk 'lib\py3-windows-x86_64\python.exe'
$entry = Join-Path $Sdk 'renpy.py'
if (-not (Test-Path -LiteralPath (Join-Path $Sdk 'web\renpy.wasm'))) { throw 'Install the official RenPy 8.5.3 web support package first.' }
# Both this script and Ren'Py's web builder clear their generated targets.
# Resolve and bound the exact targets before allowing either operation.
$workspaceFull = [IO.Path]::GetFullPath($workspace)
foreach ($target in @($stage,$public)) {
    $resolved = [IO.Path]::GetFullPath($target)
    if (Test-Path -LiteralPath $target) { $resolved=(Resolve-Path -LiteralPath $target).Path }
    if (-not $resolved.StartsWith($workspaceFull+'\',[StringComparison]::OrdinalIgnoreCase)) { throw ('Unsafe output path: '+$resolved) }
}
if (Test-Path -LiteralPath $stage) { Remove-Item -LiteralPath $stage -Recurse -Force }
New-Item -ItemType Directory -Path (Join-Path $stage 'game'),$deploy -Force | Out-Null
$gameRoot = Join-Path $project 'game'
Get-ChildItem -LiteralPath $gameRoot -Recurse -File | Where-Object {
    $_.FullName -notmatch '\\(saves|cache)\\' -and $_.Name -notlike 'testcases.*' -and $_.Extension -ne '.rpyc'
} | ForEach-Object {
    $relative=$_.FullName.Substring($gameRoot.Length+1)
    $destination=Join-Path (Join-Path $stage 'game') $relative
    New-Item -ItemType Directory -Path (Split-Path -Parent $destination) -Force | Out-Null
    Copy-Item -LiteralPath $_.FullName -Destination $destination
}
# These build-only rules never enter the source game or the browser runtime.
@'
init 1000 python:
    build.classify("game/**.rpy", None)
    build.classify("game/web_package.rpyc", None)
    build.classify("web-presplash.jpg", None)
'@ | Set-Content -LiteralPath (Join-Path $stage 'game\web_package.rpy') -Encoding utf8
@'
# Keep startup GUI, portrait and first archive frame available immediately.
- image game/gui/**
- image game/images/caly/caly_narrator.png
- image game/images/moon/apollo17.jpg
+ image game/images/**
'@ | Set-Content -LiteralPath (Join-Path $stage 'progressive_download.txt') -Encoding ascii
# Reuse the existing verified NASA photograph without altering its pixels.
Copy-Item -LiteralPath (Join-Path $gameRoot 'images\moon\apollo17.jpg') -Destination (Join-Path $stage 'web-presplash.jpg')
$env:RENPY_PATH_TO_SAVES=Join-Path $workspace 'tools\web-support\build-saves'
& $runner $entry (Join-Path $Sdk 'launcher') web_build $stage --destination $public *> (Join-Path $workspace 'tools\web-support\build.log')
if ($LASTEXITCODE -ne 0) { Get-Content (Join-Path $workspace 'tools\web-support\build.log') -Tail 30; throw 'Official web_build failed.' }
if (Test-Path -LiteralPath ($public+'.zip')) {
    Move-Item -LiteralPath ($public+'.zip') -Destination (Join-Path $workspace 'tools\web-support\caly-web.zip') -Force
}
Copy-Item -LiteralPath (Join-Path $project 'SOURCES.md') -Destination (Join-Path $public 'SOURCES.md')
@'

## Web distribution provenance

`web-presplash.jpg` is an unchanged copy of `game/images/moon/apollo17.jpg` (M1); its NASA source URL and SHA-256 are listed above. It illustrates the loading screen, not a new landing or a new historical moment.

`renpy.js`, `renpy.wasm`, `renpy.data`, `renpy-pre.js`, the HTML loader, service worker, manifest and SDK-generated icons come from the [official RenPy 8.5.3 web package](https://www.renpy.org/dl/8.5.3/renpy-8.5.3-web.zip), verified against [official checksums](https://www.renpy.org/dl/8.5.3/checksums.txt). The package SHA-256 is `954db897e65f51ea63cb2fb7b203d02be0447f4e22069514020bbe6c6691fdfc`. These are engine/interface assets, not scientific photographs. The game uses the official WebAssembly target described in [RenPy's web documentation](https://www.renpy.org/doc/html/web.html).
'@ | Add-Content -LiteralPath (Join-Path $public 'SOURCES.md') -Encoding utf8
$files=Get-ChildItem -LiteralPath $public -Recurse -File
$total=($files | Measure-Object Length -Sum).Sum
$report=@{bytes=$total;file_count=$files.Count;largest=@($files | Sort-Object Length -Descending | Select-Object -First 10 @{Name='path';Expression={$_.FullName.Substring($public.Length+1)}},Length)}
$report | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $workspace 'tools\web-support\size-report.json') -Encoding utf8
if ($total -ge 100000000) { throw ('Public output exceeds conservative 100 MB upload budget: '+$total) }
Write-Output ('Official web build ready: '+$public)
Write-Output ('Public bytes: '+$total+'; files: '+$files.Count)
