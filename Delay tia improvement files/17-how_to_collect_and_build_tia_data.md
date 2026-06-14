# How To Collect And Build The TIA Data

This guide explains the easiest practical way to build the new TIA datasets using the files and records you already have.

The objective is not to redesign your workflow. The objective is to get reliable TIA inputs fast, with the least extra work, while preserving the old files and keeping the current program structure.

## 1. Working Rule

Use this order:

1. Keep the old files as source files.
2. Use the populated improvement files as the new canonical TIA files.
3. Fill blanks only where the old files do not already prove the value.
4. Do not invent data.
5. If a value is not proven by a source, leave it blank and note the missing evidence.

That is the safest way to reach a defensible output quickly.

## 2. What You Already Have

Old source files already available:

- `C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\steel_delay_tia_templates\01- master_activity_steel_analysis.csv`
- `C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\steel_delay_tia_templates\02- employer_steel_supply.csv`
- `C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\steel_delay_tia_templates\03- p6_activity_export.csv`
- `C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\steel_delay_tia_templates\04- relationship_file.csv`
- `C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\steel_delay_tia_templates\05- contract_library.csv`
- `C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\steel_delay_tia_templates\06- ifc_conflict.csv`
- `C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\steel_delay_tia_templates\07- payments.csv`
- `C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\steel_delay_tia_templates\08- rfi_status.csv`
- `C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\data\letters\01-SAMCO-ACEPM_letters_linked_updated.xlsx`

The new canonical improvement files already created and partially filled are in:

- `C:\Users\pc\OneDrive\Documents\Codex\2026-05-20\Project Intelegent Hub\Delay tia improvement files`

## 3. Fastest Submission Strategy

If time is limited, do not try to perfect every file equally.

Focus in this exact order:

1. `02-delay_event_register_template.csv`
2. `03-activity_impact_register_template.csv`
3. `04-fragnet_logic_register_template.csv`
4. `05-claimed_delay_register_template.csv`
5. `08-evidence_register_template.csv`
6. `09-primavera_fragnet_import_template.csv`

These six files drive most of the report quality.

## 4. File By File Collection Method

## 4.1 `01-project_metadata_template.csv`

Purpose:
- cover page
- project identification
- baseline/update identification
- report metadata

Already available from current sources:
- partial project context from the current dashboard and file names

Best source to complete it:
- contract front page
- project cover sheet
- monthly report header
- baseline schedule title block

Easiest method:
1. Open the contract or official project summary.
2. Copy project name, contract number, employer, contractor, consultant, baseline name, update name, data date, and report date.
3. Fill one row only.

Minimum required fields:
- project name
- contract number
- employer
- contractor
- consultant
- baseline schedule name
- update schedule name
- report date

Responsible person:
- planning engineer or contracts engineer

## 4.2 `02-delay_event_register_template.csv`

Purpose:
- the master register of all claimed and supporting delay events
- the main table for the delay narrative

Already available from current sources:
- steel shortage events from `01- master_activity_steel_analysis.csv`
- employer supply timing from `02- employer_steel_supply.csv`
- IFC issues from `06- ifc_conflict.csv`
- RFI issues from `08- rfi_status.csv`
- payment issues from `07- payments.csv`
- letters chronology from the letters workbook

Easiest method:
1. Use the current populated file as the base.
2. Review each row one by one.
3. Keep only events that can be evidenced.
4. For each event, make sure these fields are correct:
   - event type
   - event start date
   - event finish date
   - event cause
   - affected activity text
   - source reference

How to collect missing values:
- `event start date`:
  - steel: first shortage/relevant employer delivery date
  - RFI/IFC: submission date or blocking start date
  - payment: invoice date, due date, or non-payment recognition date
- `event finish date`:
  - steel: recovery date or next effective supply date
  - RFI/IFC: reply date or issue close date
  - payment: paid date or recovery date
- `source reference`:
  - use delivery refs, RFI numbers, letter refs, invoice numbers

Minimum practical standard:
- every row must have date, cause, source reference, and at least a text description of the affected work

Responsible person:
- planning engineer with support from site engineer and commercial team

## 4.3 `03-activity_impact_register_template.csv`

Purpose:
- prove which activities were impacted
- quantify schedule effect at activity level

Already available from current sources:
- activity IDs and dates from `03- p6_activity_export.csv`
- steel shortage evidence from `01- master_activity_steel_analysis.csv`
- recorded activity delay days from `Delayed duration in days due to steel un avilability in site` in `01- master_activity_steel_analysis.csv`
- relationship context from `04- relationship_file.csv`

Easiest method:
1. Start from the populated rows already there.
2. For each claimed activity, verify:
   - activity ID
   - activity name
   - baseline start/finish
   - current start/finish
   - total float
   - critical/longest path status
   - reason for impact
3. If the activity is only narratively mentioned in letters, do not add it unless it can be tied to P6.

How to collect missing values:
- use `03- p6_activity_export.csv` for dates and float
- use `01- master_activity_steel_analysis.csv` for steel quantity evidence
- use `04- relationship_file.csv` for predecessor/successor logic

Most important fields:
- `Activity ID`
- `Pre-Impact Finish`
- `Impacted Finish`
- `Claimed Delay Duration`
- `Impact Cause`

Rule for `Claimed Delay Duration`:
- if `Delayed duration in days due to steel un avilability in site` is populated in the master activity file, use it first
- convert negative recorded values to positive day counts
- use finish-delta or inferred fragnet duration only when the master column is blank

Responsible person:
- planning engineer

## 4.4 `04-fragnet_logic_register_template.csv`

Purpose:
- define exactly how the fragnet is inserted
- show the time impact logic clearly

Already available from current sources:
- current TIA engine output
- `04- relationship_file.csv`
- `03- p6_activity_export.csv`

Easiest method:
1. Start with the populated fragnet rows.
2. Check each fragnet candidate against the real predecessor and successor logic.
3. Confirm:
   - insert before
   - insert after
   - predecessor relationship type
   - successor relationship type
   - fragnet start
   - fragnet finish
   - duration
   - logic rationale

How to collect missing values:
- relationship type from P6 or the relationship file
- logic rationale from the actual cause:
  - no available steel
  - missing IFC
  - delayed RFI response
  - payment blockage

Most important rule:
- do not create a fragnet without a defendable link to a real schedule activity

Responsible person:
- planning engineer

## 4.5 `05-claimed_delay_register_template.csv`

Purpose:
- the formal claimed days table
- the table most likely to be challenged

Already available from current sources:
- delay event register
- activity impact register
- fragnet logic register
- recorded activity delay days from the master activity steel file where populated

Easiest method:
1. First check whether the activity has a populated value in `Delayed duration in days due to steel un avilability in site` in the master activity file.
2. If yes, use that value as the primary claimed duration after converting it to a positive day count.
3. Only if it is blank, use the inferred duration logic already in the improvement pack.

1. Use only rows where claimed delay can be tied to:
   - event window
   - impacted activity
   - schedule logic
2. For each claimed row, check:
   - event reference
   - activity ID
   - claimed start
   - claimed finish
   - claimed duration
   - entitlement position

How to collect missing values:
- `claimed duration`:
  - best method: difference between pre-impact and impacted finish
  - fallback: fragnet duration if schedule delta is not explicit
- `entitlement position`:
  - from `05- contract_library.csv`

Most important rule:
- claimed duration must be automatic or clearly derivable from dates

Responsible person:
- planning engineer and contracts engineer together

## 4.6 `06-causation_matrix_template.csv`

Purpose:
- explain why the delay happened
- connect event to activity and activity to project impact

Already available from current sources:
- delay register
- activity impact
- contract support
- letters

Easiest method:
1. One row per claimed cause path.
2. Fill:
   - cause event
   - direct impacted activity
   - downstream effect
   - contractual category
   - strength of proof

How to collect missing values:
- use letters for narrative cause
- use P6 for impacted activity
- use contract library for contractual position

Minimum standard:
- every cause row needs one event source and one schedule source

Responsible person:
- planning + contracts

## 4.7 `07-concurrency_matrix_template.csv`

Purpose:
- show whether other delays overlap the claimed delay
- protect the steel claim from concurrency attacks

Already available from current sources:
- RFI
- IFC
- payments
- fragnet windows

Easiest method:
1. Check whether non-steel events overlap the claimed steel window.
2. For each overlap, record:
   - overlap start
   - overlap finish
   - overlap days
   - whether it is true concurrency or only background noise

How to collect missing values:
- compare dates between:
  - delay event register
  - fragnet logic register
  - RFI/IFC/payment files

Important rule:
- not every overlapping event is real concurrency
- concurrency needs both timing overlap and real workface relevance

Responsible person:
- planning engineer

## 4.8 `08-evidence_register_template.csv`

Purpose:
- the supporting document index for the report and claim

Already available from current sources:
- employer steel supply
- master activity steel analysis
- letters workbook
- RFI/IFC/payment files

Easiest method:
1. Keep one row per evidence item.
2. Record:
   - evidence type
   - reference
   - date
   - linked event
   - linked activity
   - short description

Best document sources:
- delivery notes
- MIRs
- site logs
- letters
- RFIs
- IFC issue lists
- invoices and payment records

Minimum standard:
- every major claimed event should have at least one evidence row

Responsible person:
- planning, site, QA/QC, contracts

## 4.9 `09-primavera_fragnet_import_template.csv`

Purpose:
- build the import-grade fragnet activity set
- support manual Primavera insertion now
- support later XER generation

Already available from current sources:
- fragnet output from the TIA engine
- P6 export
- relationship file

Easiest method:
1. Use the current populated rows.
2. For each row, verify:
   - activity ID
   - name
   - duration
   - start
   - finish
   - predecessor ID
   - successor ID
   - relationship types

How to collect missing values:
- from `03- p6_activity_export.csv`
- from `04- relationship_file.csv`

Important rule:
- keep this file clean and import-like
- avoid narrative-only fields unless needed for notes

Responsible person:
- planning engineer

## 4.10 `10-xer_build_context_template.csv`

Purpose:
- hold the project-level context required for later XER generation

Already available from current sources:
- limited current context only

Easiest method:
1. Fill only one row.
2. Add:
   - source project name
   - EPS if known
   - project ID if known
   - calendar name if known
   - default relationship type conventions
   - baseline version reference

How to collect missing values:
- from Primavera project properties
- from a sample XER if available

Responsible person:
- planning engineer / Primavera operator

## 5. Easiest Real Data Sources By Discipline

## Planning engineer

Use for:
- activity IDs
- baseline/current dates
- float
- critical path
- predecessor/successor logic
- fragnet structure

Source files:
- `03- p6_activity_export.csv`
- `04- relationship_file.csv`

## Site engineer

Use for:
- actual blocking periods
- workface readiness
- when steel absence actually stopped the work
- field confirmation that an issue affected an activity

Typical records:
- daily reports
- site diaries
- lookahead meeting notes

## Material controller / store

Use for:
- employer steel delivery dates
- quantities
- delivery references
- sequence of supply

Source files and records:
- `02- employer_steel_supply.csv`
- delivery notes
- store receiving log

## QA/QC

Use for:
- MIR references
- acceptance/inspection timing
- whether material was usable or still under hold

## Contracts / commercial

Use for:
- payment delay proof
- contract clause support
- notices
- formal claim language

Source files:
- `05- contract_library.csv`
- `07- payments.csv`
- letters workbook

## 6. Minimum Data You Must Manually Review

Even if most files are auto-filled, these items should still be manually reviewed before submission:

1. claimed delay durations
2. fragnet insert positions
3. concurrency conclusions
4. contractual entitlement language
5. evidence references

These are the highest-risk items.

## 7. Practical Collection Workflow For Speed

If you need the fastest reliable workflow, use this sequence:

1. Open `02-delay_event_register_template.csv`
   - remove weak events
   - correct dates and sources
2. Open `03-activity_impact_register_template.csv`
   - confirm only real impacted activities
3. Open `04-fragnet_logic_register_template.csv`
   - confirm predecessor/successor insertion points
4. Open `05-claimed_delay_register_template.csv`
   - confirm claimed days
5. Open `08-evidence_register_template.csv`
   - make sure every major event has evidence
6. Open `09-primavera_fragnet_import_template.csv`
   - make sure the fragnet rows can be inserted cleanly in Primavera

That is the shortest route to a stronger TIA package.

## 8. What Not To Do

Do not:

- rebuild the old files from zero
- mix SAMCO steel into employer steel delay calculations
- add activities that are not tied to P6
- claim days that cannot be tied to dates
- write perfect narratives before the tables are correct

The tables must be correct first.

## 9. Final Rule

The easiest correct method is:

- old files remain the evidence base
- new improvement files become the structured TIA layer
- fill only what can be proven
- review the six high-priority files first

That gives the highest reliability with the least extra work.
