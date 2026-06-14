# README - TIA Director Report Automation for Codex

## 1. Purpose

This README explains what information is available in the **Time Impact Analysis (TIA) Director-Level Word Report** and how Codex should place program outputs into the correct report sections, workbook sheets, and chart assets.

Main artifacts already created:

- `TIA_Director_Level_Word_Report_Template.docx`  
  Premium Word report template for directors, owners, senior management, Employer/Engineer submission, and EOT claim presentation.

- `TIA_Director_Report_Data_Input_Workbook.xlsx`  
  Editable workbook containing structured input tables and dashboard data that can drive the report visuals.

- `tia_report_assets/`  
  Chart/image folder used by the Word report. Existing assets include delay bars, cumulative delay curve, milestone variance, fragnet diagram, activity window/Gantt view, and criticality heatmap.

- `create_tia_report.py`  
  Original Python generator script that builds the Word report and chart assets from sample data.

---

## 2. What kind of information is available in the report

The report is designed as a complete TIA / EOT decision package, not only a schedule printout. It contains the following information categories:

### 2.1 Cover and report identification

Purpose: identify the package and make it suitable for formal management submission.

Available information:

- Report title
- Project name placeholder
- Contract number placeholder
- Data date placeholder
- Revision placeholder
- Executive purpose statement
- Template status / sample-data warning
- Confidential footer

Program output should populate:

- Project name
- Contract number
- Employer / Client
- Contractor
- Data date
- Baseline reference
- Impacted update reference
- Report revision
- Prepared by / checked by / approved by, if available

---

### 2.2 Report map and usage protocol

Purpose: explain to non-planning stakeholders how to read the report.

Available information:

- Executive dashboard purpose
- Data readiness purpose
- Delay event register purpose
- Fragnet logic purpose
- Impact calculation purpose
- Criticality and causation purpose
- EOT claim position purpose

Program output should not usually overwrite this section except if the methodology or report structure changes.

---

### 2.3 Executive TIA dashboard

Purpose: give directors a fast decision view.

Available information:

- Total recorded working delay days
- Potential EOT days
- Number of critical / longest path events
- Number of missing evidence items
- Executive conclusion narrative
- Delay contribution by event chart
- Source table showing event, working days, and classification

Program output should populate:

- `total_recorded_working_delay_days`
- `potential_eot_days`
- `critical_delay_events_count`
- `missing_evidence_items_count`
- Executive conclusion paragraph
- Delay contribution chart from event-level working days

---

### 2.4 Project, contract, and schedule control data

Purpose: prove the TIA is linked to the correct contract and programme.

Available information:

- Project name
- Employer / Client
- Contractor
- Contract form / EOT clause
- Accepted baseline programme
- Impacted update
- Data date
- Calendars
- Criticality rule
- Analysis period

Program output should populate:

- `project_metadata.json` or equivalent fields
- P6/XER file names
- Baseline revision
- Update revision
- Data date
- Calendar basis
- Critical path / longest path rule
- Analysis cut-off period

---

### 2.5 Data readiness matrix

Purpose: show whether the TIA is evidence-backed or still weak.

Available information:

- Accepted baseline / approved update status
- Native P6/XER file status
- Activity export status
- Relationship export status
- Progress records status
- Delay notice status
- RFI / drawing / instruction records status
- Site records status
- Mitigation records status

Program output should populate:

- Data input name
- Priority level
- Reason for TIA
- Status: Complete / Missing / Partial / Pending Verification

---

### 2.6 TIA methodology

Purpose: explain the logic used to calculate delay impact.

Available information:

- Define delay event
- Select correct programme
- Build fragnet
- Insert fragnet into CPM logic
- Recalculate schedule
- Compare pre-impact and impacted forecast completion
- Test criticality / longest path
- Confirm entitlement and evidence

Program output should not overwrite this section unless the analysis method changes. It should only insert project-specific methodology assumptions where required.

---

### 2.7 Delay event register and classification

Purpose: list every delay event and classify whether it is valid for TIA.

Available information:

- Event ID
- Event description
- Responsible party
- WBS / area
- Affected activity ID
- Impact start
- Impact finish
- Calendar days
- Working days
- Fragnet ID
- Critical / longest path status
- Delay type
- Notice / letter reference
- Evidence status
- Claim decision

Program output should populate this section from the `delay_events` table.

---

### 2.8 Fragnet design requirements and fragnet logic

Purpose: show the inserted logic that models the delay event in the CPM schedule.

Available information:

- Fragnet ID
- Fragnet activity ID
- Fragnet activity description
- Duration
- Predecessor activity
- Relationship / lag
- Successor activity
- Logic rationale
- Evidence / record reference
- Fragnet diagram
- Fragnet quality gates

Program output should populate this section from the `fragnet_logic` table and generate/update the fragnet diagram.

---

### 2.9 Impact calculation: baseline vs pre-impact vs impacted

Purpose: show exactly how delay days were calculated.

Available information:

- Baseline completion date
- Pre-impact forecast completion date
- Impacted forecast completion date
- Net impact days
- Potential EOT position
- Pre-impact vs impacted activity finish window chart
- Milestone variance chart
- Calculation formula narrative

Program output should populate:

- Baseline completion
- Pre-impact completion
- Impacted completion
- Net delay days
- Milestone variance table
- Activity comparison chart

Core formula:

```text
Net Delay = Impacted Forecast Finish - Pre-Impact Forecast Finish
```

---

### 2.10 Affected activities, criticality, and longest path review

Purpose: prove whether each impacted activity is critical or only locally delayed.

Available information:

- Activity ID
- Activity name
- WBS
- Baseline finish
- Pre-impact forecast finish
- Impacted forecast finish
- Finish delta days
- Total float before
- Total float after
- Critical / longest path flag
- Downstream milestone
- Impact note
- Criticality heatmap

Program output should populate this section from the `activity_impact` table.

---

### 2.11 Downstream delay and cumulative delay trend

Purpose: show how delay exposure accumulated over time.

Available information:

- Period / date
- Cumulative delay days
- Cumulative delay chart
- Management note explaining that CPM causation still governs the final EOT days

Program output should populate this section from the `milestone_trend` or `cumulative_delay_trend` table.

---

### 2.12 Causation, concurrency, and entitlement matrix

Purpose: separate valid delay entitlement from commercial pressure, contractor risk, or unsupported events.

Available information:

- Event ID
- Cause
- Critical impact proven
- Concurrency / risk test
- Claim treatment
- Required action

Program output should populate this section from a `causation_matrix` table or derive it from `delay_events`, `activity_impact`, and `evidence_register`.

---

### 2.13 Primavera P6 / CPM calculation control sheet

Purpose: make the analysis repeatable and auditable.

Available information:

- Schedule file name
- Data date
- Schedule options
- Longest path / critical path basis
- Retained logic / progress override
- Out-of-sequence progress handling
- Constraints
- Calendars
- Open ends
- Negative float
- Required attachments list

Program output should populate this section from `p6_controls.csv` or `p6_controls.json`.

---

### 2.14 EOT claim position and director decision matrix

Purpose: convert schedule analysis into a management decision.

Available information:

- Decision bucket
- Events included
- Delay days treatment
- Management action
- Director decision cards:
  - Approve for EOT narrative
  - Close evidence gap
  - Exclude from EOT

Program output should populate:

- Valid TIA events
- Supporting-only events
- Commercial-only events
- Not suitable events
- Not enough data events
- Total accepted days for EOT narrative
- Required management actions

---

### 2.15 Appendices: evidence checklist and glossary

Purpose: control completeness before submission.

Available information:

- Notice status
- Cause status
- Activity affected status
- Critical / longest path effect status
- Downstream milestone delay status
- Concurrency review status
- Mitigation documentation status
- Claim value separation status
- Glossary of TIA terms

Program output should populate checklist status values and evidence references.

---

## 3. Existing workbook structure

The workbook contains these sheets:

1. `Dashboard`
2. `Delay Event Register`
3. `Activity Impact`
4. `Fragnet Logic`
5. `Evidence Register`
6. `Categories`

### 3.1 `Dashboard`

Used for executive KPIs and chart source tables.

Expected blocks:

- `A3:D10` - KPI summary
- `A13:D18` - milestone variance table
- `F3:H10` - event delay contribution source table
- `J3:K10` - cumulative delay trend source table

### 3.2 `Delay Event Register`

Primary event-level input table.

Columns:

```text
Event ID
Event Description
Responsible Party
WBS / Area
Affected Activity ID
Impact Start
Impact Finish
Calendar Days
Working Days
Fragnet ID
Critical / Longest Path?
Delay Type
Notice / Letter Ref.
Evidence Status
Claim Decision
```

### 3.3 `Activity Impact`

Activity-level before/after schedule impact table.

Columns:

```text
Activity ID
Activity Name
WBS
Baseline Finish
Pre-Impact Forecast Finish
Impacted Forecast Finish
Finish Delta (days)
Total Float Before
Total Float After
Critical / LP?
Downstream Milestone
Impact Note
```

### 3.4 `Fragnet Logic`

Digital fragnet insertion logic table.

Columns:

```text
Fragnet ID
Fragnet Activity ID
Fragnet Activity Description
Duration (days)
Predecessor Activity
Relationship / Lag
Successor Activity
Logic Rationale
Record Reference
```

### 3.5 `Evidence Register`

Evidence and causation support table.

Columns:

```text
Evidence ID
Related Event
Document Type
Document Ref.
Date
Key Fact Proven
Causation Link
Strength
Missing Item
Action Owner
```

### 3.6 `Categories`

Dropdown / classification reference sheet.

Available category lists:

- Responsible Party
- Delay Type
- Evidence Status
- Claim Decision

---

## 4. Recommended input folder structure for Codex

Codex should expect structured program outputs in this folder:

```text
/mnt/data/tia_program_output/
  project_metadata.json
  kpis.json
  delay_events.csv
  activity_impact.csv
  fragnet_logic.csv
  evidence_register.csv
  causation_matrix.csv
  p6_controls.csv
  readiness_matrix.csv
  milestone_variance.csv
  cumulative_delay_trend.csv
  charts/
    delay_contribution.png
    cumulative_delay.png
    milestone_variance.png
    fragnet_diagram.png
    activity_finish_window.png
    criticality_heatmap.png
```

If the program exports Excel instead of CSV, keep the same logical table names as sheet names.

---

## 5. Required output-to-report placement map

Use the section title as the main anchor. Do not rely only on Word table numbers because table numbers can change after editing.

| Program Output | Word Report Section | Workbook Sheet | Chart / Visual |
|---|---|---|---|
| `project_metadata.json` | Cover; Section 3; Section 12 | Dashboard / manual metadata cells if added | None |
| `kpis.json` | Section 2 Executive TIA Dashboard | Dashboard `A3:D10` | Optional KPI cards |
| `delay_events.csv` | Section 2 source table; Section 6; Section 11; Section 13 | Delay Event Register | `delay_contribution.png` |
| `activity_impact.csv` | Section 8; Section 9 | Activity Impact | `activity_finish_window.png`, `criticality_heatmap.png` |
| `fragnet_logic.csv` | Section 7 | Fragnet Logic | `fragnet_diagram.png` |
| `evidence_register.csv` | Section 4; Section 11; Section 14 | Evidence Register | Evidence completeness indicators |
| `causation_matrix.csv` | Section 11 | Optional new sheet: Causation Matrix | None |
| `p6_controls.csv` | Section 3; Section 12 | Optional new sheet: P6 Controls | None |
| `readiness_matrix.csv` | Section 4; Section 14 | Optional new sheet: Readiness Matrix | Evidence readiness status |
| `milestone_variance.csv` | Section 8; Dashboard | Dashboard `A13:D18` | `milestone_variance.png` |
| `cumulative_delay_trend.csv` | Section 10; Dashboard | Dashboard `J3:K10` | `cumulative_delay.png` |

---

## 6. Data schema for program outputs

### 6.1 `project_metadata.json`

```json
{
  "project_name": "Project Name",
  "contract_no": "Contract Number",
  "employer": "Employer / Client",
  "contractor": "Contractor",
  "contract_form_or_clause": "EOT clause reference",
  "accepted_baseline_programme": "Baseline Rev / Date",
  "impacted_update": "Update Rev / Date",
  "data_date": "YYYY-MM-DD",
  "calendar_basis": "Project calendar basis",
  "criticality_rule": "Longest Path or Total Float threshold",
  "analysis_period": "From / To",
  "prepared_by": "Name",
  "checked_by": "Name",
  "approved_by": "Name"
}
```

### 6.2 `kpis.json`

```json
{
  "total_recorded_working_delay_days": 64,
  "potential_eot_days": 37,
  "critical_delay_events_count": 3,
  "missing_evidence_items_count": 1,
  "events_with_complete_evidence": 3,
  "commercial_only_items": 1,
  "non_excusable_items": 1,
  "executive_conclusion": "Clear director-level narrative based on the calculated TIA outputs."
}
```

### 6.3 `delay_events.csv`

Required columns:

```text
Event ID,Event Description,Responsible Party,WBS / Area,Affected Activity ID,Impact Start,Impact Finish,Calendar Days,Working Days,Fragnet ID,Critical / Longest Path?,Delay Type,Notice / Letter Ref.,Evidence Status,Claim Decision
```

Allowed values for `Claim Decision`:

```text
Valid for TIA
Supporting Evidence Only
Not Suitable
Not Enough Data
Commercial Only
```

Recommended decision logic:

- `Valid for TIA`: delay event has causation, evidence, affected activity, and critical / longest path impact.
- `Supporting Evidence Only`: useful context, but critical project delay is not fully proven.
- `Not Suitable`: no valid TIA basis, non-excusable, or not linked to CPM impact.
- `Not Enough Data`: potentially valid, but mandatory records are missing.
- `Commercial Only`: commercial/cashflow issue unless schedule causation is proven.

### 6.4 `activity_impact.csv`

Required columns:

```text
Activity ID,Activity Name,WBS,Baseline Finish,Pre-Impact Forecast Finish,Impacted Forecast Finish,Finish Delta (days),Total Float Before,Total Float After,Critical / LP?,Downstream Milestone,Impact Note
```

### 6.5 `fragnet_logic.csv`

Required columns:

```text
Fragnet ID,Fragnet Activity ID,Fragnet Activity Description,Duration (days),Predecessor Activity,Relationship / Lag,Successor Activity,Logic Rationale,Record Reference
```

### 6.6 `evidence_register.csv`

Required columns:

```text
Evidence ID,Related Event,Document Type,Document Ref.,Date,Key Fact Proven,Causation Link,Strength,Missing Item,Action Owner
```

Allowed values for `Strength`:

```text
High
Medium
Low
Pending
```

### 6.7 `causation_matrix.csv`

Required columns:

```text
Event,Cause,Critical Impact Proven?,Concurrency / Risk Test,Claim Treatment,Required Action
```

### 6.8 `p6_controls.csv`

Required columns:

```text
Control Item,Recorded Value,Why It Must Be Shown
```

Minimum control items:

```text
Schedule file name
Data date
Schedule options
Longest path / critical path basis
Retained logic / progress override
Out-of-sequence progress handling
Constraints
Calendars
Open ends
Negative float
```

### 6.9 `readiness_matrix.csv`

Required columns:

```text
Data Input,Priority,Reason for TIA,Status
```

Allowed values for `Priority`:

```text
Mandatory
High
Medium
Low
```

Allowed values for `Status`:

```text
Complete
Partial
Missing
Pending Verification
Not Required
```

### 6.10 `milestone_variance.csv`

Required columns:

```text
Milestone,Baseline Date,Impacted Date,Variance Days
```

### 6.11 `cumulative_delay_trend.csv`

Required columns:

```text
Period,Cumulative Delay Days
```

---

## 7. Chart generation requirements

Every visual must be backed by a visible editable table in the workbook or report.

Required charts:

1. `delay_contribution.png`
   - Source: `delay_events.csv`
   - X-axis: Event ID
   - Y-axis: Working Days
   - Color grouping: Claim Decision

2. `cumulative_delay.png`
   - Source: `cumulative_delay_trend.csv`
   - X-axis: Period
   - Y-axis: Cumulative Delay Days

3. `milestone_variance.png`
   - Source: `milestone_variance.csv`
   - X-axis: Variance Days
   - Y-axis: Milestone

4. `fragnet_diagram.png`
   - Source: `fragnet_logic.csv`
   - Must show predecessor, fragnet activities, successor, duration, and logical flow.

5. `activity_finish_window.png`
   - Source: `activity_impact.csv`
   - Compare baseline / pre-impact dates against impacted dates.

6. `criticality_heatmap.png`
   - Source: `activity_impact.csv`
   - Show finish delta, total float before, and total float after by activity.

---

## 8. Recommended Codex workflow

1. Read all source outputs from `/mnt/data/tia_program_output/`.
2. Validate mandatory columns before generating anything.
3. Normalize dates to `DD-MMM-YYYY` for Word and real date values for Excel.
4. Calculate KPI values from the source tables, not manually.
5. Update the workbook first.
6. Generate charts from the updated workbook/source tables.
7. Update Word tables and images by section anchor.
8. Preserve the corporate color palette.
9. Export final files using clear names:

```text
/mnt/data/TIA_Director_Level_Word_Report_Final.docx
/mnt/data/TIA_Director_Report_Data_Input_Workbook_Final.xlsx
/mnt/data/tia_report_assets/*.png
```

---

## 9. Corporate color palette to preserve

Use these colors consistently:

```text
NAVY       #0B1F3A
BLUE       #1F4E79
TEAL       #00A6A6
GOLD       #C9A227
LIGHT_BLUE #EAF4FB
LIGHT_TEAL #EAF7F7
LIGHT_GOLD #FFF7E0
LIGHT_GRAY #F3F6F8
MID_GRAY   #D9E2EC
DARK_TEXT  #1F2937
RED        #C00000
GREEN      #1A7F37
ORANGE     #F59E0B
WHITE      #FFFFFF
```

---

## 10. Validation rules before final report issue

Codex should stop and report a validation issue if any of the following are missing:

- No accepted baseline or approved update reference
- No data date
- Delay event has no affected activity ID
- Event classified as `Valid for TIA` but `Critical / Longest Path?` is not `Yes`
- Event classified as `Valid for TIA` but evidence status is `Missing`
- Fragnet activity has no predecessor or successor
- Activity impact has no pre-impact forecast finish or impacted forecast finish
- Net delay days cannot be calculated
- P6 schedule settings are not recorded

Codex may still generate a report, but it must mark the affected item as:

```text
NOT ENOUGH DATA - potentially valid but missing evidence
```

or

```text
YES, but only as supporting evidence
```

as appropriate.

---

## 11. Director-level decision logic

Use these decision rules when classifying events:

### Valid for TIA

Use when all are true:

- Cause is defined
- Responsible party is not contractor-risk unless contract says otherwise
- Affected activity is identified
- Fragnet logic exists
- Critical / longest path impact is proven
- Downstream milestone or project completion movement exists
- Evidence is complete or strong enough

### Supporting evidence only

Use when event is real but one of these is weak:

- Local activity delay only
- Criticality not proven
- Float still available
- Downstream completion movement not shown
- Evidence is partial

### Not suitable

Use when one of these applies:

- Contractor-owned productivity issue
- No CPM activity impact
- No causation link
- No fragnet / no logical insertion basis
- Event is already absorbed by available float

### Not enough data

Use when the event may be valid but mandatory records are missing.

### Commercial only

Use when the issue is payment, cashflow, cost, procurement cost, or valuation-related, unless programme causation and critical delay are proven.

---

## 12. Practical implementation notes for Codex

- Use section titles as anchors, not page numbers.
- Keep every visual traceable to a visible source table.
- Do not hide missing evidence; show it as a management action.
- Do not mix cost entitlement with time entitlement.
- Use working days for delay calculations unless the contract specifically requires calendar days.
- Keep the original premium styling and landscape layout.
- Preserve the wording quality: director-level, clear, technical but understandable.
- Replace sample values completely before formal issue.
- Do not delete the glossary or evidence checklist; they help non-planning stakeholders understand the TIA.

---

## 13. Final deliverable checklist

Before finishing, confirm:

```text
[ ] Word report updated
[ ] Workbook updated
[ ] All charts regenerated
[ ] All sample values replaced or clearly marked as sample
[ ] Delay days reconcile between Word and workbook
[ ] Event classifications reconcile with evidence status
[ ] Critical / longest path activities are clearly identified
[ ] Fragnet logic table is complete
[ ] P6 calculation settings are recorded
[ ] Executive conclusion matches the numbers
[ ] Final files saved in /mnt/data
```
