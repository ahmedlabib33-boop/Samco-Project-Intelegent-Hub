# Delay TIA Upload-Ready Files

Upload from this folder into the Delay TIA panel.

## Required upload panel files

1. `01- master_activity_steel_analysis.csv`
2. `02- employer_steel_supply.csv`
3. `03- p6_activity_export.csv`
4. `04- relationship_file.csv`
5. `05- contract_library.csv`
6. `06- ifc_conflict.csv`
7. `07- payments.csv`
8. `08- rfi_status.csv` - improved from RFI Delay.xlsx claim 6, with affected Activity ID and Activity Name
9. `10- samco_steel_supplied_at_site.csv` - display only, not used in delay calculation

## Extra detailed RFI file

- `RFI Delay.csv`

Copy `RFI Delay.csv` to:

```text
D:\VSC\Project Intelegent Hub\steel_delay_tia_templates\RFI Delay.csv
```

This supports the detailed concurrent-delay/final-delay logic that reads the local `RFI Delay.csv` support file.

## Rule

Activity ID and Activity Name in the RFI file are the affected activities.
