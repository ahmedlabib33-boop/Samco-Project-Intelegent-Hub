@echo off
setlocal EnableExtensions
cd /d "%~dp0"

set "MODE=Watch"
set "INTERVAL=30"
if not "%~1"=="" set "MODE=%~1"
if not "%~2"=="" set "INTERVAL=%~2"

echo Project Intelligence Hub full-workspace no-Git synchronization
echo Mode: %MODE%  Interval: %INTERVAL% minute(s)
echo Target and deletion policy are controlled by tools\github_sync_config.json
echo Credentials are read only from GITHUB_TOKEN or GH_TOKEN.
echo Codespaces user secrets do not authenticate this local Windows process.
echo.

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0tools\github_no_git_sync.ps1" -Mode "%MODE%" -IntervalMinutes %INTERVAL%
exit /b %ERRORLEVEL%
