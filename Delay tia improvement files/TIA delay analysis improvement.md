# TIA Delay Analysis Improvement

## Purpose

This document defines the exact additive steps required to implement the attached TIA logic in the current Project Intelligence Hub program without removing or cancelling any existing feature.

Constraint:
- no current feature is to be removed,
- no current workflow is to be disabled,
- all changes must be additive,
- current outputs must remain available,
- stronger TIA logic, stronger report quality, and additional Primavera/XER-ready outputs must be added on top of the current program.

## Source logic captured from the attached TIA methodology

The attached DOCX establishes these core rules:

1. a fragnet is a focused schedule fragment inserted into the programme,
2. it must model:
   - the actual delay event,
   - the start point,
   - the recovery point,
   - and the effect on the affected activity sequence,
3. a fragnet must not be inserted randomly,
4. it should only be recommended when the logic can prove:
   - a real delay event or shortage condition,
   - a first affected activity,
   - a causal path into the affected activity,
   - a downstream schedule effect,
5. TIA must compare:
   - BL Critical Path,
   - Current Critical Path,
6. a valid TIA conclusion depends on:
   - factual event evidence,
   - activity linkage,
   - baseline/current path relevance,
   - delay duration logic,
   - contract support.

This is consistent with the direction already present in the current Delay TIA module. The improvement work is therefore not a redesign. It is a hardening and completion exercise.

## Current program position

The current program already has:

- `Delay TIA` module,
- required uploaded files,
- employer-only steel delay logic,
- BL Critical Path comparison,
- affected activity finder,
- TIA fragnet recommendation,
- contractual delay assessment,
- predicted notice register,
- Excel / HTML / CSV / DOCX outputs,
- Primavera fragnet CSV output.

So the foundation is already built.

What is still needed for a more complete and more defensible TIA implementation is:

1. stronger evidence normalization,
2. stronger event-to-activity linkage,
3. explicit pre-impact vs impacted schedule logic,
4. explicit claimed delay duration calculation,
5. report-grade causation matrices,
6. Primavera import-grade output,
7. XER production strategy.

## Required target outputs

The improved implementation should produce all current outputs and add the following stronger outputs:

1. Director DOCX TIA report with fully populated methodology and impact sections
2. Formal delay event register
3. Formal activity impact register
4. Formal fragnet logic register
5. Claimed delay duration register
6. Causation and concurrency matrix
7. Evidence register
8. Primavera fragnet import sheet
9. Primavera XER support output path

## Exact implementation steps

## Step 1. Preserve the current module and freeze the current outputs

Do not remove:
- current `Delay TIA` tabs,
- current CSV/HTML/XLSX exports,
- current docx export button,
- current SAMCO display-only logic,
- current upload persistence behavior.

Implementation action:
- treat the current behavior as baseline,
- add new derived tables behind the existing views,
- expand outputs instead of replacing them.

Why:
- this avoids breaking user workflow,
- this keeps the current program operational while improving quality.

## Step 2. Normalize Delay TIA into explicit internal datasets

The current module already reads the uploaded files, but it should internally produce a formal set of canonical datasets before analysis.

Add these internal datasets:

1. `project_metadata_df`
2. `delay_event_register_df`
3. `activity_impact_df`
4. `fragnet_logic_df`
5. `claimed_delay_df`
6. `causation_matrix_df`
7. `concurrency_matrix_df`
8. `evidence_register_df`
9. `primavera_fragnet_import_df`
10. `xer_build_context`

Why:
- the methodology in the DOCX is not just about a recommendation table,
- it needs structured proof layers,
- these layers should drive all downstream reports.

## Step 3. Create a formal delay event register

Current program state:
- stock-out events and support delay streams exist,
- but they need to be formalized into one event register.

Add a unified event register with these fields:

- `Event ID`
- `Event Type`
- `Source File`
- `Cause Description`
- `Evidence Date`
- `Impact Start Date`
- `Recovery Date`
- `Working Delay Days`
- `Responsible Party`
- `Linked Activity ID`
- `Linked Building / Zone`
- `Criticality Context`
- `Contract Support Topic`
- `Evidence Strength`

Logic:
- steel events come from employer-only supply and master activity shortage logic,
- IFC/RFI/payment events come from their uploaded streams,
- each event becomes one normalized row.

Why:
- this gives the required “real delay event” base,
- this is the first hard requirement in the attached logic.

## Step 4. Create a formal first-affected-activity engine

Current program state:
- affected activity finder exists,
- but it should be hardened into a scored, traceable engine.

Each candidate activity should be assessed using:

1. incomplete or historically blocked status,
2. requirement / shortage relevance,
3. BL Start and current Start/Finish context,
4. Total Float / Critical / Longest Path state,
5. predecessor readiness,
6. successor exposure,
7. event-to-activity timing match,
8. responsibility consistency.

Add explicit fields:

- `Candidate Score`
- `First Affected Flag`
- `Reason Selected`
- `Predecessor Ready`
- `Successor Exposed`
- `Current Path State`
- `BL Path State`

Why:
- the attached logic requires a proven first affected activity,
- not only a probable one.

## Step 5. Create explicit causal path logic

Current program state:
- relationship file is used,
- but the causal path should become a formal derived object.

Add a causal path builder:

- `Event -> Predecessor -> First Affected Activity -> Successor / Milestone`

Add fields:

- `Causal Path Proven`
- `Driving Relationship Type`
- `Driving Lag`
- `Downstream Successor`
- `Downstream Milestone Impact`

Why:
- the DOCX requires a causal path into the affected activity and downstream effect,
- this is currently implicit and must become explicit.

## Step 6. Create explicit pre-impact vs impacted schedule logic

Current program state:
- fragment dates and recommendation exist,
- but claimed delay duration must be defended through schedule states.

Add for each claimed activity:

- `BL Finish`
- `Pre-Impact Forecast Finish`
- `Impacted Forecast Finish`
- `Claimed Delay Duration (days)`

Calculation rule:

`Claimed Delay Duration = Impacted Forecast Finish - Pre-Impact Forecast Finish`

Fallback rule only if exact dates cannot be derived:
- use fragnet duration,
- mark row as `Inferred Duration Basis`.

Why:
- the attached methodology explicitly depends on delay duration logic,
- this is the core of a stronger claim-grade output.

## Step 7. Build a formal fragnet logic dataset

Current program state:
- Primavera fragnet CSV exists,
- but it should be elevated into a full formal fragnet dataset.

Add these fields:

- `Fragnet ID`
- `Delay Event ID`
- `Fragnet Activity ID`
- `Fragnet Activity Name`
- `Fragnet Insert Before`
- `Predecessor Activity ID`
- `Predecessor Relationship Type`
- `Successor Activity ID`
- `Successor Relationship Type`
- `Fragment Start`
- `Fragment Finish`
- `Fragment Duration`
- `Logic Rationale`
- `Record Reference`
- `Evidence Reference`
- `Claimed Delay Duration`

Why:
- this becomes the single source for:
  - CSV export,
  - DOCX report,
  - future XER generation logic.

## Step 8. Build a formal BL vs current path comparison engine

Current program state:
- BL Critical Path Comparison exists,
- but it should feed the TIA conclusion directly.

Use the fixed BL files and current Activities analysis to produce:

- `BL Critical Flag`
- `Current Critical Flag`
- `BL Float`
- `Current Float`
- `BL Only`
- `Current Only`
- `Matched Critical`
- `Historically Critical`

Then tie these values into:

- event scoring,
- affected activity scoring,
- contractual output,
- final TIA conclusion.

Why:
- the attached logic explicitly requires BL vs current comparison,
- not just display.

## Step 9. Build a formal causation and concurrency matrix

The improved system must separate:

- primary driving delay,
- support delay,
- concurrent delay,
- non-driving event,
- historically relevant event.

Add matrix fields:

- `Event ID`
- `Activity ID`
- `Primary Cause`
- `Concurrent With`
- `Employer Risk`
- `Contractor Risk`
- `Excusable Potential`
- `Compensable Potential`
- `Needs More Evidence`

Why:
- this is required to make the TIA conclusion defensible,
- especially when IFC/RFI/payment streams are active.

## Step 10. Build a formal evidence register

The improved system should compile evidence references used by each event and each fragnet recommendation.

Add fields:

- `Evidence Ref`
- `Event ID`
- `Activity ID`
- `Evidence Type`
- `Source File`
- `Source Row`
- `Document Date`
- `Description`
- `Used In Report`

Why:
- the attached logic requires factual event evidence,
- the report should show traceability, not only conclusions.

## Step 11. Strengthen the DOCX report without changing its design

Constraint:
- keep the Word template design unchanged,
- fill only the required information.

Implementation action:
- map the new internal datasets into the current DOCX generator,
- do not change style/layout,
- only improve population quality.

Sections to populate from the new datasets:

1. executive summary from `delay_event_register_df`
2. methodology from fixed TIA logic text
3. event register from `delay_event_register_df`
4. activity impact from `activity_impact_df`
5. fragnet logic from `fragnet_logic_df`
6. claimed delay duration from `claimed_delay_df`
7. causation/concurrency from `causation_matrix_df`
8. contractual support from current contract library + assessment
9. appendix from `evidence_register_df`

Why:
- this gives the report the same design but stronger content integrity.

## Step 12. Add Primavera import-grade output

Current state:
- the program generates `Primavera Fragnet Sheet (.csv)`

Improve it so it becomes import-grade, not only report-grade.

Required columns:

- `Activity ID`
- `Activity Name`
- `WBS`
- `Original Duration`
- `Start`
- `Finish`
- `Calendar`
- `Activity Type`
- `Predecessor Activity ID`
- `Predecessor Relationship Type`
- `Lag`
- `Successor Activity ID`
- `Successor Relationship Type`
- `Responsible Party`
- `Delay Event ID`
- `Claimed Delay Duration`
- `Notes`

Why:
- this allows the output to be prepared for Primavera logic insertion workflows.

## Step 13. Add XER output strategy

Important technical point:
- generating a true valid Primavera `.xer` file is not the same as generating a CSV,
- a true `.xer` must reproduce Primavera table structure, IDs, and relationships correctly.

Best implementation path:

### Stage 1: XER-ready export pack
Produce:
- fragnet activities table,
- activity relationship table,
- optional code/resource table,
- import instructions,
- field mapping sheet.

This gives the planner a clean package to insert into Primavera quickly.

### Stage 2: true XER builder
Only after stage 1 is stable, add:
- a structured XER template builder,
- a controlled XER write engine,
- validation against a sample working Primavera XER.

Required inputs for a true XER builder:

- sample accepted XER from the same project,
- project calendar mapping,
- activity type mapping,
- relationship code mapping,
- WBS and project ID consistency rules.

Why this staged path is correct:
- it reduces risk,
- avoids producing invalid XER,
- and still gets the user a usable Primavera deliverable quickly.

## Step 14. Add new Delay TIA output tabs without removing old ones

Keep all current tabs.

Add new tabs or report sections for:

1. `Delay Event Register`
2. `Activity Impact Register`
3. `Claimed Delay Durations`
4. `Causation / Concurrency Matrix`
5. `Evidence Register`
6. `Primavera Import Pack`
7. `XER Export Preparation`

Why:
- user workflow remains intact,
- stronger analysis becomes visible instead of hidden.

## Step 15. Map each uploaded file to the improved TIA logic

### `01- master_activity_steel_analysis.csv`
Use for:
- activity-level shortage evidence,
- activity dates,
- quantities,
- responsibility,
- blocked condition,
- claimed activity duration context,
- recorded steel-delay duration from `Delayed duration in days due to steel un avilability in site` where populated.

### `02- employer_steel_supply.csv`
Use for:
- employer delivery timing,
- stock-out/recovery timing,
- event start and recovery basis.

### `03- p6_activity_export.csv`
Use for:
- current schedule dates,
- actual dates,
- remaining duration,
- float,
- criticality,
- longest path,
- path-state comparisons.

### `04- relationship_file.csv`
Use for:
- driving logic path,
- predecessor/successor proof,
- fragnet insertion logic.

### `05- contract_library.csv`
Use for:
- entitlement framing,
- notice/time-bar interpretation,
- contractual support section.

### `06- ifc_conflict.csv`
Use for:
- support delay event register,
- concurrency review.

### `07- payments.csv`
Use for:
- support delay event register,
- concurrency review.

### `08- rfi_status.csv`
Use for:
- support delay event register,
- concurrency review.

### Letters workbook
Use for:
- predicted notice register,
- correspondence support,
- evidence references.

### BL fixed files
Use for:
- baseline criticality and historical path state.

## Step 16. Exact implementation sequence in code

To implement this safely in the current program, the coding order should be:

1. add canonical dataframe builders,
2. add delay event register builder,
3. add activity impact builder,
4. add claimed delay duration builder,
5. add fragnet logic builder,
6. add causation/concurrency builder,
7. add evidence register builder,
8. upgrade DOCX generator to use these builders,
9. upgrade Excel/HTML outputs to use the same builders,
10. upgrade Primavera CSV export,
11. add XER-ready pack,
12. later add true XER builder.

Why this order:
- it avoids breaking current output,
- it centralizes logic,
- it makes all reports consistent.

## Step 17. Definition of “most perfect way” in this project

For this program, the most correct implementation is not to invent a new TIA theory. It is to make the current system satisfy the methodology fully by:

1. proving event evidence,
2. proving first affected activity,
3. proving causal path,
4. proving downstream effect,
5. measuring claimed delay duration,
6. comparing BL and current path,
7. preserving all current outputs,
8. expanding toward Primavera import and XER support.

That is the correct perfection target for this codebase.

## Final recommendation

Implement this in two delivery phases.

### Phase A: strengthen the existing Delay TIA without changing the user workflow
- canonical datasets,
- delay event register,
- activity impact register,
- claimed delay duration,
- stronger DOCX,
- stronger Primavera CSV,
- evidence and causation matrices.

### Phase B: add Primavera/XER maturity
- Primavera import-grade pack,
- XER-ready export pack,
- true XER builder only after template validation.

This is the safest and highest-quality path.
