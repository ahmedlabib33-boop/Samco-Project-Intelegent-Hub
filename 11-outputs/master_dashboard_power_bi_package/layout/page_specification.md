# Master Dashboard Power BI Build Kit

This kit recreates the Project Intelligence Hub Master Dashboard in Power BI using project-isolated exports.

## Pages
1. Project Overview: executive KPI cards, progress, dates, project health.
2. WBS: WBS hierarchy and progress.
3. Activities: activity progress, critical path, delayed activities.
4. Main Milestones: milestone register and timeline.
5. S-Curve Analysis: planned, actual, invoiced cumulative curves.
6. EVM Analysis: BAC, PV, EV, AC, SPI, CPI, SV, CV.
7. Contracts: contract values, payments, commercial status.
8. Letters Intelligence: correspondence and issue-thread data when available.
9. Risk Analysis: risk status, steel/RFI/IFC context.
10. Delay and Time Impact: delay events, responsibility, EOT exposure.

## Build Steps
1. Open Power BI Desktop.
2. Import `theme/master_dashboard_theme.json`.
3. Load all CSV files from the `data` folder.
4. Create relationships using `project_id` from Projects to every fact table.
5. Add measures from `dax/master_dashboard_measures.dax`.
6. Build pages following `layout/page_specification.md`.

## Refresh
Run `python tools/build_master_power_bi_package.py` to refresh the CSVs and ZIP from the current project folders.
