# Steel Delay TIA Recognized Files

This folder contains the local Delay TIA steel-analysis templates and support streams recognized by the app. The numbered sequence now starts at `02-` and ends at `10-`.

## Required / Primary Files

1. `02- master_activity_steel_analysis.csv`
   - Activity-level steel requirement, shortage, delay duration, activity dates, responsibility, and affected activity evidence.

2. `03- employer_steel_supply.csv`
   - Employer ROYA steel delivery dates and quantities.
   - Used for steel availability and stock-out calculation.

3. `04- p6_activity_export.csv`
   - Schedule activity dates, baseline dates, float, criticality, longest path, predecessors, successors, and progress context.

4. `05- relationship_file.csv`
   - Predecessor and successor logic for causation and fragnet insertion.

5. `06- contract_library.csv`
   - Contract entitlement, notice, time bar, money impact, schedule impact, and practical evidence requirements.

## Support Delay Streams

6. `07- ifc_conflict.csv`
   - IFC/design conflict delay stream.

7. `08- payments.csv`
   - Payment/cashflow delay stream.

8. `09- rfi_status.csv`
   - RFI status delay stream.

## Visibility-Only Source

9. `10- samco_steel_supplied_at_site.csv`
    - Contractor/SAMCO steel supplied at site.
    - Display-only visibility source.
    - Excluded from employer-steel delay, stock-out, affected-activity, fragnet, and entitlement calculations.

## External Support Source

- Detailed RFI support is read from `Delay tia improvement files/upload_ready_for_delay_tia/RFI Delay.csv` when needed.

## Recognition Notes

- The app recognizes `02-` through `10-` file names first in this folder.
- The app keeps backward compatibility with the previous `01-` through `09-` names where practical.
- Dates may be in `DD-MMM-YY`, `DD-MMM-YYYY`, or Excel date format.
- Activity IDs should remain text and should match the P6 export.
- Building codes should stay consistent: `B01`, `B02`, `B03`, `B04`.
- Delay TIA should inspect columns before analysis and keep final conclusions traceable to these source files.
