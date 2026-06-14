# Codex Prompt — Super Premium Interactive Construction Progress Report Platform

Act as a senior full-stack developer, Power BI data modeler, and professional planning engineer. Build a super-premium interactive construction project progress reporting platform that generates both monthly and weekly reports from the same unified data model.

## 1. Business Objective
Create a construction project progress reporting system that satisfies executive management, consultant, PMO, and client requirements. The monthly report must be detailed and forensic. The weekly report must be linked to the monthly report but lighter, operational, and focused on immediate control actions.

The platform must generate:
1. Excel report workbook with many structured tabs.
2. Power BI-ready data model from named Excel tables.
3. Executive dashboard page.
4. Weekly dashboard page.
5. Exportable report pack for monthly and weekly reporting.

## 2. Non-Negotiable Design Standard
The output must be super premium, modern, clean, and executive-grade. Avoid old Excel-style visualizations. Use strong but comfortable colors, professional spacing, card-based KPIs, modern typography, and clear hierarchy.

Use a dark executive header with soft light backgrounds. Suggested palette:
- Navy: #0B1220
- Midnight: #111827
- Slate: #344054
- Background: #F4F7FB
- White cards: #FFFFFF
- Cyan accent: #00A6A6
- Blue: #2563EB
- Green: #12B76A
- Amber: #F59E0B
- Red: #F04438
- Muted text: #667085

Do not over-design. The dashboard must be interactive, attractive, and readable.

## 3. Workbook Structure
Generate an Excel workbook with the following sheets in the same order:
1. 01 POWER BI DASHBOARD
2. 02 WEEKLY DASHBOARD
3. 03 Report Control
4. 04 Project Overview
5. 05 Executive Summary
6. 06 Milestones
7. 07 Progress Activities
8. 08 Deliverables
9. 09 Schedule Paths
10. 10 Deviated Activities
11. 11 Cost & EVA
12. 12 Manpower
13. 13 Equipment
14. 14 S-Curve
15. 15 Shop Drawings
16. 16 Procurement
17. 17 Invoices
18. 18 Risks & Issues
19. 19 Mitigation Plan
20. 20 HSE & QAQC
21. 21 Correspondence
22. 22 Photos Register
23. 23 Weekly Data
24. 24 Power BI Model
25. 99 Lists

Each analytical sheet must be formatted as an Excel Table with a clear table name suitable for Power BI import. Avoid merged cells inside data tables. Use formulas for derived values. Do not hard-code calculated outputs.

## 4. Monthly Dashboard Requirements
The first sheet must work as the executive monthly dashboard/control tower. It must include:
- Project identity and reporting period.
- KPI cards for overall progress, planned progress, progress variance, SPI, CPI, PV, EV, AC, EAC, forecast finish, open risks, overdue shop drawings, delayed procurement packages, unpaid invoices, safety indicators, and critical actions.
- S-curve comparing baseline planned progress, actual earned progress from Primavera, and invoiced/submitted monthly progress.
- Earned value trend: PV vs EV vs AC.
- Manpower histogram planned vs actual.
- Equipment histogram planned vs actual.
- Critical path / longest path / float path summary.
- Top deviated activities ranked by negative variance or forecast delay.
- Risk and issue heat map.
- Procurement status summary.
- Shop drawing status summary.
- Invoice/payment status summary.
- Management decision log.

Dashboard design must be modern, not crowded, and arranged in blocks:
1. Header and filter bar.
2. Executive KPI cards.
3. Progress and cost control visuals.
4. Resource pressure visuals.
5. Risk/action control panel.

## 5. Weekly Dashboard Requirements
The second sheet must be linked to the same data model but simplified. It must show:
- Weekly progress achieved.
- Weekly lookahead.
- Critical activities this week.
- Work-front blockers.
- Risks/issues requiring action.
- Required management decisions.
- Current SPI/CPI snapshot.
- Weekly manpower and equipment pulse.
- Weekly action owner and due date.

The weekly dashboard must be less detailed than the monthly dashboard but still suitable for executive, consultant, PMO, and client review.

## 6. Data Tables and Columns
### 6.1 Report Control
Include report number, revision, reporting period, data date, baseline version, update version, prepared by, reviewed by, approved by, issue date, distribution list, and confidentiality status.

### 6.2 Project Overview
Include contract value, approved variations, revised contract value, original duration, elapsed duration, remaining duration, baseline finish, forecast finish, project phase, main scope, client, consultant, contractor, PMO, and key narrative.

### 6.3 Executive Summary
Include all executive KPIs with status, trend, threshold, owner, and management note.

### 6.4 Milestones
Columns:
Milestone ID, Milestone Name, Planned Start, Planned Finish, Forecast Finish, Actual Start, Actual Finish, Baseline Status, Current Status, Variance Days.

### 6.5 Progress Activities
Columns:
Activity ID, Activity Name, WBS, Discipline, Area, Previous Progress %, Current Period Progress %, Total Progress %, Planned Progress %, Progress Variance %, Planned Start, Planned Finish, Forecast Start, Forecast Finish, Actual Start, Actual Finish, Critical Flag, Longest Path Flag, Float Days, Responsible Party, Remarks.

### 6.6 Deliverables
Columns:
Deliverable ID, Deliverable Name, Discipline, Planned Quantity, Actual Quantity, Planned %, Actual %, Variance %, Status, Remarks.

### 6.7 Schedule Paths
Columns:
Path ID, Path Type, Activity ID, Activity Name, Planned Start, Planned Finish, Forecast Start, Forecast Finish, Total Float, Free Float, Driving Logic, Delay Days, Responsibility, Mitigation Required.

### 6.8 Deviated Activities
Columns:
Rank, Activity ID, Activity Name, WBS, Planned %, Actual %, Variance %, Forecast Delay Days, Impact Category, Root Cause, Required Action, Owner, Due Date.

### 6.9 Cost & Earned Value Analysis
Columns:
Period, PV, EV, AC, SV, CV, SPI, CPI, BAC, EAC, ETC, VAC, Cost Status, Comment.

Use formulas:
SV = EV - PV
CV = EV - AC
SPI = EV / PV
CPI = EV / AC
EAC = BAC / CPI where appropriate
ETC = EAC - AC
VAC = BAC - EAC

### 6.10 Manpower
Columns:
Period, Discipline, Direct/Indirect, Planned Manpower, Actual Manpower, Planned Man-hours, Actual Man-hours, Variance, Variance %, Productivity Note.

### 6.11 Equipment
Columns:
Period, Equipment Type, Planned Units, Actual Units, Planned Hours, Actual Hours, Variance, Variance %, Utilization Status, Remarks.

### 6.12 S-Curve
Columns:
Period, Planned Progress % Baseline, Actual Earned Progress % Primavera, Invoiced Submitted %, Planned Cost, Earned Value, Actual Cost, Planned Man-hours, Actual Man-hours, Forecast Progress %.

### 6.13 Shop Drawings
Columns:
Submittal ID, Package, Discipline, Title, Planned Submission, Actual Submission, Consultant Response Due, Actual Response, Status, Revision, Delay Days, Responsible Party, Action Required.

### 6.14 Procurement
Columns:
Package ID, Item/Package, Supplier, PO Status, Planned Delivery, Forecast Delivery, Actual Delivery, Status, Delay Days, Linked Activity, Mitigation Action, Owner.

### 6.15 Invoices
Columns:
Invoice No, Period, Submitted Amount, Certified Amount, Paid Amount, Outstanding Amount, Submission Date, Certification Date, Payment Due Date, Payment Status, Aging Days, Remarks.

### 6.16 Risks & Issues
Columns:
ID, Type, Category, Description, Probability, Impact, Score, Severity, Owner, Status, Mitigation Strategy, Due Date, Linked Activity, Cost Impact, Schedule Impact.

Use probability × impact scoring and classify:
- 1–7 Low
- 8–14 Medium
- 15–25 High

### 6.17 Mitigation Plan
Columns:
Action ID, Linked Risk/Issue, Action Description, Owner, Due Date, Status, Effectiveness, Required Escalation, Management Decision.

### 6.18 HSE & QAQC
Columns:
Period, Man-hours, LTI, Near Miss, NCRs Open, NCRs Closed, Inspections, Pass Rate %, Key Concern.

### 6.19 Correspondence
Columns:
Reference, Date, From, To, Subject, Type, Status, Delay Related, Claim Related, Required Response Date, Actual Response Date, Overdue Days, Linked Activity, Key Evidence.

### 6.20 Photos Register
Columns:
Photo ID, Date, Area, Description, Activity ID, Before/Current/After, File Path, Comment.

### 6.21 Weekly Data
Columns:
Week Ending, Weekly Planned %, Weekly Actual %, Weekly Variance %, Activities Completed, Activities Planned Next Week, Constraints, Required Decisions.

### 6.22 Power BI Model
Include table mapping, relationships, DAX measures, refresh instructions, and dashboard page design.

### 6.23 Lists
Include allowed statuses, severity values, disciplines, package categories, parties, and RAG thresholds.

## 7. Power BI Data Model
Create a star-schema-ready model:
- Calendar dimension related to all period/date fields.
- Project dimension.
- WBS/Activity dimension.
- Discipline dimension.
- FactProgress.
- FactCostEVA.
- FactManpower.
- FactEquipment.
- FactRiskIssue.
- FactShopDrawing.
- FactProcurement.
- FactInvoices.

All Excel data tables must be cleanly named. Power BI should import named tables, not random worksheet ranges.

## 8. Power BI Measures
Generate DAX measures for:
- Overall Progress %
- Planned Progress %
- Progress Variance %
- PV
- EV
- AC
- SV
- CV
- SPI
- CPI
- BAC
- EAC
- ETC
- VAC
- Open Risks
- High Risks
- Overdue Shop Drawings
- Delayed Procurement Packages
- Outstanding Invoices
- Critical Activities Count
- Average Float
- Delayed Activities Count

## 9. Interactivity
Implement slicers/filters for:
- Reporting Period
- Discipline
- Area
- WBS
- Responsible Party
- Status
- Risk Severity
- Procurement Package
- Shop Drawing Status

In Excel, use dropdowns only if they are stable and do not break workbook validation. In Power BI, implement slicers natively.

## 10. Visualizations
Use visuals carefully:
- KPI Cards for executive status.
- Line charts for S-curves and EVM trends.
- Clustered column charts for manpower/equipment planned vs actual.
- Bar chart for most deviated activities.
- Matrix/table for critical activities and management actions.
- Heat map for risk severity.
- Donut charts only for simple status distributions.
- Avoid excessive pie charts.
- Use conditional formatting for RAG status.

## 11. Export and Quality Checks
Before final output:
- Verify workbook opens in Microsoft Excel without recovery messages.
- Verify all named tables exist.
- Verify no #REF!, #DIV/0!, #VALUE!, #NAME?, or #N/A errors.
- Verify dashboard charts are linked to source tables.
- Verify Power BI can detect all tables.
- Verify formulas are formula-driven and not hard-coded.
- Verify no merged cells are inside data tables.
- Verify dashboard is readable at 100% zoom.
- Verify monthly and weekly reports are connected to the same data source.

## 12. Files to Generate
Generate:
1. Excel workbook: Super_Premium_Construction_Progress_Report_PowerBI_Ready.xlsx
2. Optional Power BI template: Construction_Progress_Report_Template.pbix or .pbit if supported by the environment
3. README file explaining update workflow, Power BI connection, refresh process, and governance rules

## 13. Final Response Format
Return:
- Download link to the generated workbook.
- List of generated tabs.
- Power BI connection steps.
- Any assumptions or limitations.
- Confirmation of validation checks.
