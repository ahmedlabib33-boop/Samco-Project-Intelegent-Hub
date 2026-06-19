# Developer Guide

The canonical project architecture and operating rules are maintained in `beba.md`.

Key modules:

- `dashboard.py`: Streamlit dashboard and outputs.
- `src/construction_system/project_catalog.py`: project discovery and path ownership.
- `src/construction_system/csv_loader.py`: project-aware CSV loading.
- `src/construction_system/letters_auto_ingest.py`: project inbox ingestion.
- `src/construction_system/steel_delay_tia.py`: Delay TIA calculations.
- `contract_claims_center.py`: project contract and claims processing.

Validation:

```powershell
python -m compileall -q dashboard.py contract_claims_center.py src scripts tests
python -m pytest -q tests
python scripts/evaluate_delay_tia.py --label folder_architecture
python scripts/evaluate_output_studio.py --label folder_architecture
```

Do not add shared project data under the repository root. Add it to `projects/<project_id>`.
