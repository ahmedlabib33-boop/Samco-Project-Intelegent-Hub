# Project Intelligence Hub

## What this dashboard is

Project Intelligence Hub is a data-driven project controls dashboard for construction planning, commercial review, correspondence intelligence, risk visibility, and delay analysis.  
It consolidates schedule, cost, contract, letter, delay, and TIA workflows into one operational application instead of distributing them across disconnected spreadsheets and manual reports.

The dashboard is already beyond prototype stage. The main design, logic structure, exports, and presentation paths are already built. That matters because rolling this out on other company projects is no longer a design exercise. The heavy work is already done. New project rollout is mainly a matter of feeding the correct datasets and, where needed, adjusting mappings rather than rebuilding the tool.

## Why it is beneficial

### 1. One operational source instead of fragmented reporting
- P6, cost, letters, contracts, delays, risks, and TIA evidence are brought into one interface.
- This reduces manual reconciliation between planning, commercial, and contractual records.

### 2. Faster management reporting
- The dashboard already contains executive views, detailed analytical views, and export paths.
- Teams can move from raw input files to management-ready outputs faster and with less manual formatting.

### 3. Better delay and claim preparation
- Delay TIA is not just a table viewer. It builds:
  - shortage logic,
  - affected activity logic,
  - fragnet recommendation,
  - contractual delay assessment,
  - output reports,
  - Primavera fragnet export,
  - director-level DOCX report output.

### 4. Reusable across company projects
- The platform architecture is already implemented.
- Most future project setup is data preparation, not software redesign.
- New features should be relatively rare because the current platform already covers the major planning / controls / reporting workflows.
- If additions are needed, they are generally extensions to an existing module, not a new system from zero.

## Why it can be deployed on other company projects easily

The difficult part has already been completed:
- dashboard structure,
- metric calculations,
- report layouts,
- export paths,
- delay TIA workflow,
- output studio logic,
- linked presentation generation,
- document generation,
- local app launcher,
- Cloudflare sharing path.

To adapt it to another project, the normal work is:
1. prepare the project input files,
2. map them into the same expected structure,
3. validate the outputs,
4. adjust only project-specific logic if genuinely necessary.

This means future implementation effort is mainly:
- data onboarding,
- field mapping,
- quality control,
- minor tuning.

It is not a full redevelopment task.

## Main program capabilities

The live program currently contains these main modules:

1. `Overview`
2. `WBS`
3. `Activities`
4. `Milestones`
5. `S-Curve`
6. `EVM Analysis`
7. `Contracts`
8. `Contract Clauses`
9. `Letters Intelligence`
10. `Delays`
11. `Time Impact`
12. `Risks`
13. `Delay TIA`
14. `Output Studio`

## What each module does

### Overview
- overall project KPIs,
- progress summary,
- duration summary,
- commercial headline values.

### WBS
- breakdown of project scope and structure,
- progress visibility at WBS level.

### Activities
- schedule activity analysis,
- activity progress, dates, and path logic,
- current critical path context used by TIA comparisons.

### Milestones
- milestone dates,
- milestone status,
- variance visibility.

### S-Curve
- planned versus actual progress trend,
- cumulative performance tracking.

### EVM Analysis
- BAC, AC, EV, PV,
- SV, CV, EAC, TCPI,
- performance interpretation and exportable reporting views.

### Contracts
- contract-level register and values.

### Contract Clauses
- searchable contractual library,
- schedule and money impact interpretation,
- notice / time-bar / leverage context.

### Letters Intelligence
- linked correspondence review,
- issue threads,
- notice and reply linkage,
- support for predicted notice register inside Delay TIA.

### Delays
- delay item visibility,
- delay category and tracking context.

### Time Impact
- time-related review views outside the dedicated Delay TIA workflow.

### Risks
- project risk visibility and summary logic.

### Delay TIA
Delay TIA is the specialist delay-analysis engine. It currently contains:

1. `Executive Dashboard`
2. `TIA Methodology`
3. `Dependency Schema`
4. `File Priority`
5. `BL Critical Path Comparison`
6. `IFC Delay Input`
7. `Payment Delay Input`
8. `RFI Delay Input`
9. `Steel supplied AT SITE`
10. `01 Master Activity Steel Analysis`
11. `Stock-Out Detection`
12. `Affected Activity Finder`
13. `TIA Fragnet Recommendation`
14. `Contractual Delay Assessment`
15. `Predicted Notice Register`
16. `Download Reports`

### Output Studio
Output Studio is the report and presentation production area. It currently supports:
- original presentation print-only path,
- linked executive dashboard export path,
- super premium progress report path,
- Canva-style flexible dashboard path,
- PPTX export,
- HTML export,
- linked executive presentation generation.

## Delay TIA exact capability

Delay TIA can currently:
- force required uploads before analysis,
- persist uploaded files across refresh until cancelled,
- compare baseline and current critical-path context,
- analyze employer-only steel supply timing,
- ignore SAMCO steel in delay calculations while still displaying it separately,
- assess IFC, payment, and RFI support delay streams,
- detect stock-out / insufficiency events,
- identify affected activities,
- recommend fragnet placement,
- generate contractual delay assessment,
- predict a draft notice register from Letters Intelligence,
- generate:
  - Excel output pack,
  - detailed HTML report,
  - Primavera fragnet CSV,
  - summary CSV,
  - director-level DOCX report.

## How the information is driven

The program is data-driven. The major logic drivers are:

### Core dashboard data
- imported project CSV files,
- schedule and progress datasets,
- contract datasets,
- risk datasets,
- delay datasets,
- letters workbook.

### Delay TIA required files

1. `01- master_activity_steel_analysis.csv`
- primary activity-level steel evidence,
- shortage / requirement proof,
- activity dates, quantities, and responsibility context.

2. `02- employer_steel_supply.csv`
- employer ROYA supply timing,
- delivery quantity basis,
- steel delay supply curve used in calculations.

3. `03- p6_activity_export.csv`
- activity dates,
- float,
- criticality,
- longest path,
- schedule context.

4. `04- relationship_file.csv`
- predecessor / successor logic,
- fragnet insertion context,
- sequence impact.

5. `05- contract_library.csv`
- contractual support,
- notice / time-bar logic,
- money and schedule effect interpretation.

6. `06- ifc_conflict.csv`
- IFC-related support delay input.

7. `07- payments.csv`
- payment-related support delay input.

8. `08- rfi_status.csv`
- RFI-related support delay input.

### Delay TIA local baseline comparison sources

Delay TIA also reads the fixed BL comparison files automatically from:
- `BL fixed\BL Schedule.csv`
- `BL fixed\BL float bath.csv`
- `BL fixed\Bl Longest bath.csv`
- `BL fixed\BL critical path.csv`

These are used for BL critical-path and path-state comparison and do not need separate upload for that comparison.

### Delay TIA display-only SAMCO source

`10- samco_steel_supplied_at_site.csv`
- displayed in Delay TIA,
- counted in dashboard visibility,
- deliberately excluded from steel delay calculations.

## Delay TIA methodology logic

The current TIA logic follows this sequence:

1. load the required uploaded files,
2. establish employer supply timing,
3. establish activity-level steel requirement / shortage evidence,
4. establish schedule readiness and criticality from P6,
5. establish predecessor / successor logic,
6. establish the first factual delay event,
7. identify the first affected activity,
8. compare current criticality with BL critical-path context,
9. recommend fragnet position before the first affected activity,
10. measure fragment start and finish,
11. assess contractual support and entitlement context,
12. generate reports and export files.

Important rule:
- only employer ROYA steel is used in steel delay calculations,
- SAMCO steel is display-only,
- IFC / payments / RFI can be included or excluded as support delay streams.

## Output Studio exact capability

Output Studio currently supports these output paths:

### 1. Original presentation print-only
- keeps the original presentation design,
- refreshes linked content from live dashboard data,
- exports updated PPTX for print/presentation use.

### 2. Linked executive dashboard
- generates the executive dark-style dashboard output,
- tied to live program data,
- supports export outputs.

### 3. Super premium progress report
- extended reporting path for higher-finish reporting outputs.

### 4. Canva-style flexible dashboard
- flexible output mode where selected information from different sources can be combined into one reporting surface.

## Supported app start

The supported way to run the app is:

```powershell


```

This is the preferred launcher because:
- it uses the local project `.venv`,
- it starts the dashboard from its own folder,
- it keeps the app on port `8755`,
- it still works if the whole project folder is moved.

## Run the app from the project folder

If you are already inside the project folder:

```powershell
.\RUN_APP.bat
```

Then open:

```text
http://127.0.0.1:8755
```

## Run the app even if the project location changed

If the project folder was moved and you do not want to rely on a fixed path, use:

```powershell
$project = Get-ChildItem "$env:USERPROFILE" -Recurse -File -Filter "RUN_APP.bat" -ErrorAction SilentlyContinue |
  Where-Object { Test-Path (Join-Path $_.DirectoryName "dashboard.py") } |
  Select-Object -First 1 -ExpandProperty DirectoryName
Set-Location $project
.\RUN_APP.bat
```

Why this works:
- the command discovers the project folder dynamically,
- `RUN_APP.bat` uses its own folder as the working directory,
- no fixed absolute location is required.

## Full refresh run

Use this when you want to refresh dependencies, re-import, verify, compile, test, and run:

```powershell
$project = Get-ChildItem "$env:USERPROFILE" -Recurse -File -Filter "RUN_APP.bat" -ErrorAction SilentlyContinue |
  Where-Object { Test-Path (Join-Path $_.DirectoryName "dashboard.py") } |
  Select-Object -First 1 -ExpandProperty DirectoryName
Set-Location $project
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv\Scripts\python.exe" scripts\import_csv_data.py
& ".\.venv\Scripts\python.exe" scripts\verify_data.py
& ".\.venv\Scripts\python.exe" -m py_compile dashboard.py
& ".\.venv\Scripts\python.exe" -m pytest -q
.\RUN_APP.bat
```

## Full reset and re-import

Use this when you want to rebuild imported data from zero:

```powershell
$project = Get-ChildItem "$env:USERPROFILE" -Recurse -File -Filter "RUN_APP.bat" -ErrorAction SilentlyContinue |
  Where-Object { Test-Path (Join-Path $_.DirectoryName "dashboard.py") } |
  Select-Object -First 1 -ExpandProperty DirectoryName
Set-Location $project
& ".\.venv\Scripts\python.exe" scripts\import_csv_data.py --reset
& ".\.venv\Scripts\python.exe" scripts\verify_data.py
.\RUN_APP.bat
```

## Confirm the Python interpreter for VS Code / Pylance

Use the interpreter inside the same project folder:

```powershell
$project = Get-ChildItem "$env:USERPROFILE" -Recurse -File -Filter "RUN_APP.bat" -ErrorAction SilentlyContinue |
  Where-Object { Test-Path (Join-Path $_.DirectoryName "dashboard.py") } |
  Select-Object -First 1 -ExpandProperty DirectoryName
Join-Path $project ".venv\Scripts\python.exe"
```

## Cloudflare access

The local dashboard port is:

```text
8755
```

### Step 1: start the local app

```powershell
$project = Get-ChildItem "$env:USERPROFILE" -Recurse -File -Filter "RUN_APP.bat" -ErrorAction SilentlyContinue |
  Where-Object { Test-Path (Join-Path $_.DirectoryName "dashboard.py") } |
  Select-Object -First 1 -ExpandProperty DirectoryName
Set-Location $project
.\RUN_APP.bat
```

### Step 2: start the Cloudflare tunnel

```powershell
Set-Location $project
.\RUN_TUNNEL.bat
```

Current tunnel command:

```bat
cloudflared tunnel --url http://127.0.0.1:8755
```

This publishes the local dashboard through Cloudflare without changing the app itself.

## Operational conclusion

This dashboard is already a company-level reusable platform, not a single-project experiment.

Its value is:
- centralizing planning and controls workflows,
- reducing manual reporting effort,
- improving delay-analysis structure,
- improving output quality,
- making future project rollout much easier because the core platform is already built.

The expected future effort is mostly:
- data onboarding,
- field validation,
- light project-specific adjustment.

The expected future effort is not:
- redesigning the platform,
- rebuilding the modules,
- recreating the outputs from zero.
