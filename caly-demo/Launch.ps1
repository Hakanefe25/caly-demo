param([string]$Sdk=$env:RENPY_SDK)
$ErrorActionPreference='Stop'
if (-not $Sdk) { throw 'Supply -Sdk or set RENPY_SDK to your RenPy 8.5.3 SDK directory.' }
$runner=Join-Path $Sdk 'lib\py3-windows-x86_64\pythonw.exe'
if (-not (Test-Path -LiteralPath $runner)) { throw 'RenPy SDK Windows runner not found.' }
& $runner (Join-Path $Sdk 'renpy.py') $PSScriptRoot
