# Multi-Project Architecture

The implemented architecture uses root-level `projects/<project_id>` folders. The selector is generated from folder discovery and does not depend on a central registry.

## Scale

Discovery has no fixed project limit. Automated coverage validates 25 simultaneous project folders. Data volume, rather than the selector, is the practical scaling constraint.

## Isolation

Each project owns operational data, Delay TIA files, baseline files, correspondence, contracts, evidence, exports, reports, branding, and metadata. Core CSVs are aggregated only for the explicit `All projects` portfolio view.

## New Project

Copy `projects/_PROJECT_TEMPLATE`, rename the copy, update `project.json` and the copied `projects.csv`, then add project files. Refreshing Streamlit detects the folder.

See `beba.md` for the complete folder map and operating procedure.
