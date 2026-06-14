# SAMCO Egypt - Projects Intelligence Hub

Integrated project controls dashboard built in Streamlit for executive reporting, project controls, contract administration, delay analysis, risk monitoring, time impact review, S-curve reporting, activity review, and flexible dashboard export.

## Main App

- Dashboard entry file: `dashboard.py`
- Data source folder: `data/import_templates`
- Database file: `construction_system.db`
- Core logic: `src/construction_system`
- Utility scripts: `scripts`

## Dashboard Features

### 1. Overview

- Project start date from `projects.csv`
- Project finish date from `projects.csv`
- Project duration in days
- Duration elapsed %
- Remaining duration %
- Overall progress %
- Planned progress %
- Contract value
- Total activities
- Critical activities
- WBS cost visualization
- Live alert engine from linked issue threads

### 2. EVM Analysis

- BAC from `evm.csv`
- AC from `evm.csv`
- EV from `evm.csv`
- PV from `evm.csv`
- Schedule variance
- Cost variance
- EAC
- TCPI
- Full EVM table view

### 3. Contract Management

- Total contracts from `contracts.csv`
- Total active contract value
- Total certified from `payments.csv`
- Total paid from `payments.csv`
- Contract value vs certified vs paid column chart
- Contracts table
- Payments table

### 4. Letters Intelligence

- SAMCO outgoing letters
- ACE incoming letters
- Linked correspondence tables
- Issue threads
- Alert-driven correspondence review
- Risk-oriented linked letter tracking

### 5. Delay Analysis

- Delay events from `delay_events.csv`
- Total delay days
- Employer delays
- EOT potential count
- Open delays
- Closed delays
- Delay responsibility x status matrix
- Full delay register table

### 6. Risk Analysis

- Main risk register from `risks.csv`
- Steel delay status table
- RFI status table
- IFC conflict table
- Risk status and category analysis

### 7. Milestones & Change Orders

- Milestones table from `milestones.csv`
- Change orders table from `change_orders.csv`

### 8. Activities Analysis

- Total activities
- Critical path activities
- Most deviated activities
- RFT activities
- Critical path review
- Deviation review
- RFT activity review

### 9. Time Impact Analysis

- Integrated time impact engine
- Uses dashboard data as input
- Critical path impact count
- Near-critical impact count
- RFT-linked event count
- Commercial gap review
- Input matrix
- Causation and responsibility matrix
- Integrated event register

### 10. S-Curve

- Driven from `s_curve.csv`
- Planned total
- Actual total
- Invoiced total
- Last actual month
- Cumulative curve analysis

### 11. Contract Clauses

- Clause search
- Clause matching engine
- Delay event to clause matching
- AI clause brief support
- Contract terms review

### 12. Output Studio

Two different output paths:

#### Original Presentation Print-Only

- Downloads the original attached presentation as-is
- No redesign
- No structural change

#### Canva-Style Flexible Dashboard

- Select any subject from the dashboard data
- Select any information source
- Select rows down to a single line
- Combine lines from different sources
- Build smart charts
- Export printable HTML dashboard pack
- Export flexible PPTX dashboard
- Branded premium logo header strip

### 13. Steel Delay TIA

Professional feature:

- `Client Free-Issue Steel Delay Analyzer & TIA Fragnet Recommender`
- Live steel stock-out analysis from delivery and reinforcement demand data
- Internal pages for:
  - Executive Dashboard
  - Upload & Data Mapping
  - P6 Schedule Validation
  - Steel Delivery / Stock Register
  - Steel Balance Analysis
  - Stock-Out Detection
  - Affected Activity Finder
  - TIA Fragnet Recommendation
  - Contractual Delay Assessment
  - Download Reports
- Daily steel balance engine
- First stock-out date detection
- Usability lag day control
- Critical / near-critical affected activity scoring
- First affected RFT / reinforcement activity recommendation
- Fragnet insertion recommendation before the affected activity
- Contract library support matching using:
  - Clause / Topic
  - Location
  - Plain English Meaning
  - Research the Lines
  - Who Holds Leverage
  - Notice / Time Bar
  - Money Impact
  - Schedule Impact
  - Practical Action / Evidence
- Contract support scoring
- Rebuttal matrix
- Contract action & evidence tracker
- Professional delay narrative
- Report outputs:
  - Excel report
  - HTML dashboard report
  - CSV zip exports
  - Executive Summary Delay Report PPTX
  - Detailed Contract-Supported Claim Report PPTX
  - Combined Dashboard Claim Deck PPTX

## Input Files Used by the Dashboard

- `projects.csv`
- `activities.csv`
- `evm.csv`
- `contracts.csv`
- `payments.csv`
- `delay_events.csv`
- `risks.csv`
- `milestones.csv`
- `change_orders.csv`
- `s_curve.csv`
- `steel_delay_status_mployer_free_issue_material.csv`
- `Delivered_steel_site.csv`
- `rft_qtys.csv`
- `steel_activities_relationship.csv`
- `rfi_ status.csv`
- `ifc_conflict.csv`
- letters workbook from Downloads
- contract clause library workbook
- overall contract PDF
- presentation template PPTX

## Supporting Assets

- SAMCO dashboard logo in `assets`
- Flexible export header logos:
  - PRE Group
  - Roya
  - ACE-PM
  - Prime
  - Samco

## Utility Scripts

- `scripts/import_csv_data.py`
  - imports CSV data into the local system

- `scripts/verify_data.py`
  - checks imported data and key totals

- `scripts/init_database.py`
  - initializes the local database

- `scripts/generate_html_report.py`
  - generates an HTML report

- `scripts/fix_and_check.py`
  - helper check/fix script

## Requirements

Main packages:

- `streamlit`
- `pandas`
- `plotly`
- `pytest`
- `openpyxl`
- `python-pptx`
- `reportlab`
- `numpy`
- `xlsxwriter`
- `python-dateutil`
- `Pillow`
- `matplotlib`
- `kaleido`

## Running Prompts

Use these prompts/commands from PowerShell.

### 1. Go to the program folder

If the folder location is known:

```powershell
cd "C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub"
```

If the folder location changed, search for it first:

```powershell
Get-ChildItem "C:\Users\pc" -Recurse -Directory -Filter "Project Intelegent Hub" -ErrorAction SilentlyContinue | Select-Object FullName
```

Then open the returned path:

```powershell
cd "FULL_PATH_RETURNED_HERE"
```

### 2. Create the virtual environment if needed

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate
```

### 4. Install or update dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Confirm the project interpreter

Use this interpreter in VS Code / Pylance if imports are still flagged:

```text
C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\.venv\Scripts\python.exe
```

### 6. If `openpyxl` is still missing, install it directly

```powershell
python -m pip install openpyxl
```

### 7. Import the CSV data

```powershell
python scripts\import_csv_data.py
```

### 8. Verify the imported data

```powershell
python scripts\verify_data.py
```

### 9. Run a fast syntax check

```powershell
python -m py_compile dashboard.py
```

### 10. Run tests

```powershell
python -m pytest -q
```

### 11. Start the dashboard

```powershell
python -m streamlit run dashboard.py --server.address 127.0.0.1 --server.port 8501
```

### 12. Open in browser

```text
http://127.0.0.1:8501
```

### 13. Normal daily run

Use this when the environment and packages are already ready:

```powershell
cd "C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub"
.venv\Scripts\Activate
python -m streamlit run dashboard.py --server.address 127.0.0.1 --server.port 8501
```

### 14. Full refresh run

Use this when CSV data changed and you want the dashboard fully refreshed:

```powershell
cd "C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub"
.venv\Scripts\Activate
python -m pip install -r requirements.txt
python scripts\import_csv_data.py
python scripts\verify_data.py
python -m py_compile dashboard.py
python -m pytest -q
python -m streamlit run dashboard.py --server.address 127.0.0.1 --server.port 8501
```

### 15. Full reset and re-import

Use this when you want to rebuild the local database from scratch:

```powershell
cd "C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub"
.venv\Scripts\Activate
python scripts\import_csv_data.py --reset
python scripts\verify_data.py
python -m streamlit run dashboard.py --server.address 127.0.0.1 --server.port 8501
```

### 16. Steel Delay TIA feature usage

Use the default live steel-delay files already linked in the program:

```powershell
cd "C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub"
.venv\Scripts\Activate
python -m streamlit run dashboard.py --server.address 127.0.0.1 --server.port 8501
```

Then open:

- `Steel Delay TIA` tab
- adjust:
  - `Usability Lag Days`
  - `Near-Critical Float Threshold`
  - `Data Date`
- optionally upload replacement files for:
  - P6 Activity Export
  - Steel Delivery / Site Stock Register
  - Activity Steel Requirement File
  - Relationship File
  - Contract Library

The feature will then answer:

1. When did steel quantity become zero?
2. Which steel type / diameter was affected?
3. Which building was affected?
4. Which activity was first impacted?
5. Where should the TIA fragnet be inserted?
6. What is the fragment start date?
7. What is the fragment finish date?
8. What is the fragment duration?
9. Is the delay critical, near-critical, concurrent, or non-driving?
10. Is the delay likely Employer / Client risk or Contractor risk?

## Failure Checking Prompts

If something fails, use these checks.

### Check current folder

```powershell
Get-Location
```

### Check if dashboard file exists

```powershell
Get-ChildItem dashboard.py
```

### Check if virtual environment exists

```powershell
Get-ChildItem .venv
```

### Check if required scripts exist

```powershell
Get-ChildItem .\scripts
```

### Check Python version

```powershell
python --version
```

### Check installed packages

```powershell
python -m pip list
```

### Check the exact interpreter in use

```powershell
python -c "import sys; print(sys.executable)"
```

### Reinstall requirements if package import fails

```powershell
python -m pip install -r requirements.txt --upgrade
```

### Install `openpyxl` directly if workbook export is blocked

```powershell
python -m pip install openpyxl
```

### Check syntax again after any edit

```powershell
python -m py_compile dashboard.py
```

### Run tests again after any fix

```powershell
python -m pytest -q
```

### Check CSV source files

```powershell
Get-ChildItem .\data\import_templates
```

### Check if the presentation template exists

```powershell
Get-ChildItem "C:\Users\pc\OneDrive\Desktop\Presentation\08-Presentations the big - 11.5.2026.pptx"
```

### Check if the external logos exist

```powershell
Get-ChildItem "C:\Users\pc\OneDrive\Desktop\01 Letters\labib tia folders\Logos"
```

### If Streamlit does not open, run it again on the same port

```powershell
python -m streamlit run dashboard.py --server.address 127.0.0.1 --server.port 8501
```

### If you want one compact full run flow

```powershell
cd "C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub"
.venv\Scripts\Activate
python -m pip install -r requirements.txt
python scripts\import_csv_data.py
python scripts\verify_data.py
python -m py_compile dashboard.py
python -m pytest -q
python -m streamlit run dashboard.py --server.address 127.0.0.1 --server.port 8501
```
