# Project Intelligence Hub - Run and Sync Commands

Open PowerShell in:

```text
C:\Users\pc\OneDrive\Documents\Project Intelligence Hub
```

## Start the Dashboard

```powershell
.\RUN_APP.bat
```

Local URL:

```text
http://127.0.0.1:8755
```

## Start the Public Tunnel

```powershell
.\RUN_TUNNEL.bat
```

Keep the tunnel window open while people use the public link.

## Manually Sync the Complete Project to GitHub

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync_current_to_samco.ps1 -Message "Update Project Intelligence Hub"
```

Target repository:

```text
https://github.com/ahmedlabib33-boop/Samco-Project-Intelegent-Hub
```

## Start Automatic Full-Project Sync

```powershell
.\RUN_FULL_PROJECT_NO_GIT_SYNC.bat
```

This watches the complete project folder and synchronizes detected changes to the GitHub repository. `GITHUB_TOKEN` or `GH_TOKEN` must be configured with repository write access.

## Start Excel and CSV Sync Only

```powershell
.\RUN_LIVE_EXCEL_SYNC.bat
```

This watches Excel and CSV data locations and runs the Git-based synchronization script when data changes.

## Recommended Complete Startup

Run each command in a separate PowerShell window:

```powershell
.\RUN_APP.bat
```

```powershell
.\RUN_FULL_PROJECT_NO_GIT_SYNC.bat
```

```powershell
.\RUN_TUNNEL.bat
```

## Health Check

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8755/_stcore/health
```

The expected response is:

```text
ok
```
