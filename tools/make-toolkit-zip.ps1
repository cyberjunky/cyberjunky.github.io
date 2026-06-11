# Regenerates assets/downloads/ghost-to-jekyll-toolkit.zip from the current
# source files. Run from the repo root:  pwsh tools\make-toolkit-zip.ps1
$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent
$stage = Join-Path $env:TEMP ("g2j_" + [System.IO.Path]::GetRandomFileName().Replace('.',''))
New-Item -ItemType Directory -Path (Join-Path $stage ".github\workflows") -Force | Out-Null

$files = @("ghost_to_jekyll.py","requirements.txt","_config.yml","Gemfile",
           ".env.example",".gitignore","README.md","index.html")
foreach ($f in $files) { Copy-Item (Join-Path $root $f) (Join-Path $stage $f) }
Copy-Item (Join-Path $root ".github\workflows\jekyll.yml") (Join-Path $stage ".github\workflows\jekyll.yml")

$downloads = Join-Path $root "assets\downloads"
New-Item -ItemType Directory -Path $downloads -Force | Out-Null
$zip = Join-Path $downloads "ghost-to-jekyll-toolkit.zip"
Compress-Archive -Path (Join-Path $stage "*") -DestinationPath $zip -Force
Remove-Item $stage -Recurse -Force
"Rebuilt $zip"
