Steel Delay TIA Upload Templates

Files in this folder:

1. `sample_p6_activity_export.csv`
   Required for the schedule engine.

2. `sample_steel_delivery_register.csv`
   Required for stock / delivery / balance analysis.

3. `sample_activity_steel_requirement.csv`
   Optional if steel quantities are not already usable from the P6 export.

4. `sample_relationship_file.csv`
   Optional if predecessor / successor data is not reliable in the P6 export.

5. `sample_contract_library.csv`
   Optional but recommended for contractual assessment.

Upload order inside the program:

1. P6 Activity Export
2. Steel Delivery / Site Stock Register
3. Activity Steel Requirement File
4. Relationship File
5. Contract Library Excel / CSV

Notes:

- Dates can be in `DD-MMM-YY`, `DD-MMM-YYYY`, or Excel date format.
- Activity IDs should stay text.
- Building codes should be consistent: `B01`, `B02`, `B03`, `B04`.
- Steel types / diameters should be consistent across schedule, requirement, and stock files.
