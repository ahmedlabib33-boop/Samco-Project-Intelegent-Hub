@echo off
cd /d "%~dp0"
echo Starting full Project Intelligence Hub no-Git auto-sync watcher...
echo.
echo Required credential:
echo   Set GITHUB_TOKEN or GH_TOKEN with repo write access before running this watcher.
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\watch_project_and_push_to_samco_no_git.ps1"
