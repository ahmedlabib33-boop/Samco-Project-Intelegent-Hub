# Delay TIA Improvement Pack

This folder contains the implementation pack required to harden the current Delay TIA module without removing any existing feature.

Rules:
- additive only,
- no feature cancellation,
- current outputs remain available,
- new internal datasets and outputs are added on top of the existing system.

Main files:
1. `TIA delay analysis improvement.md` -> master improvement note
2. `01-10` CSV templates -> required canonical datasets
3. `11-field_mapping_matrix.csv` -> source-to-canonical mapping
4. `12-implementation_backlog.csv` -> execution sequence
5. `13-acceptance_criteria.md` -> definition of done
6. `14-xer_export_strategy.md` -> XER staging strategy
7. `15-director_report_section_mapping.csv` -> report section binding
8. `16-docx_data_binding_matrix.csv` -> DOCX binding source map

Use:
- fill these templates from the current program outputs and uploaded files,
- then implement the code changes against the canonical dataset model,
- then bind all outputs to the canonical datasets.
