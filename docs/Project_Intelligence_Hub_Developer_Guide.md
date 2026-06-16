# Project Intelligence Hub Developer Guide

## Purpose

- This guide explains how the Project Intelligence Hub is structured, how project data is loaded, how to add or update projects, and where to change the main code safely.
- The app is a Streamlit dashboard driven mainly by CSV files. The current design keeps legacy root files available while also supporting one folder per project.

## Return Point

- A return snapshot was created before the project-folder restructure work.
- ﻿{
    "created_at":  "2026-06-15T22:53:59",
    "source":  "C:\\Users\\pc\\OneDrive\\Documents\\Project Intelligence Hub",
    "return_point":  "C:\\Users\\pc\\OneDrive\\Documents\\Project Intelligence Hub return points\\return-20260615-225349-before-project-folder-restructure",
    "note":  "Return here when user says RETURN after project folder restructure request"
}

- If you say RETURN, restore the workspace from the latest return point folder listed above.

## Main Application Files

- dashboard.py: Main Streamlit app. It contains the project selector, dashboard tabs, Delay Analysis - TIA slide, Output Studio, report exports, and the shared CSV loaders.
- src/construction_system/steel_delay_tia.py: Delay TIA calculation engine and data-processing helpers.
- src/construction_system/csv_loader.py: General CSV loading helpers used by supporting scripts/modules.
- reports/tia_director_pack_generator.py: TIA director/report generation helper.
- scripts/evaluate_delay_tia.py: Scores Delay TIA outputs.
- scripts/evaluate_output_studio.py: Scores Output Studio/report output quality.
- scripts/sync_current_to_samco.ps1: Syncs the local project into the GitHub repository and pushes to main.

## Project Folder Structure

- Master registry: data/import_templates/projects.csv. Every selectable project starts from this file.
- Per-project root: data/projects/{project_id}/.
- Operational dashboard data: data/projects/{project_id}/data/import_templates/.
- Delay Analysis - TIA files: data/projects/{project_id}/delay_analysis/steel_delay_tia_templates/.
- Baseline/fixed schedule files: data/projects/{project_id}/bl/.
- Fixed references: data/projects/{project_id}/fixed/.
- Original Excel files: data/projects/{project_id}/source_excel/.
- Evidence files: data/projects/{project_id}/evidence/.
- Generated outputs: data/projects/{project_id}/exports/ and data/projects/{project_id}/reports/.

## How The App Recognizes Project Files

- The dashboard selector sets st.session_state["active_project_id"].
- dashboard.py uses project_scoped_file(path, project_id) to resolve files.
- If the selected project has its own file, the app reads data/projects/{project_id}/... first.
- If the file does not exist in the project folder, the app falls back to the existing root file. This protects old behavior.
- projects.csv remains global and is not replaced by a per-project file because it is the master selector registry.

## Core Loader Functions In dashboard.py

- load_core_csv(path, project_id=None): Loads operational CSVs. It is cached by file path, modified time, and file size, so it is fast but still updates when files change.
- _load_core_csv_cached(path_str, modified_ns, file_size): Internal cached read function.
- project_scoped_file(path, project_id=None): Maps root files to selected project files.
- filter_active_project(df, project_id=None): Filters any dataframe with project_id to the active project.
- steel_tia_load_csv_or_empty(path): Loads Delay TIA and BL CSVs using the same project-scoped file resolution.

## Adding A New Project

- 1. Add a row in data/import_templates/projects.csv with a unique project_id.
- 2. Copy data/projects/PROJECT-02 and rename it to data/projects/{new_project_id}.
- 3. Put operational CSV files into data/projects/{new_project_id}/data/import_templates/.
- 4. Put Delay TIA files into data/projects/{new_project_id}/delay_analysis/steel_delay_tia_templates/.
- 5. Put BL schedule, critical path, float, longest path, and MEP files into data/projects/{new_project_id}/bl/.
- 6. Make sure every CSV row has the correct project_id.
- 7. Open the app, choose the project from Dashboard project, and check each tab.

## Updating Existing Project Data

- For daily work, update files inside data/projects/{project_id}/ instead of editing the fallback root files.
- Keep file names the same as the current templates. The app recognizes by file name and folder location.
- Do not remove project_id columns. The selector depends on them.
- After editing CSV/Excel converted files, refresh Streamlit. The loader detects file timestamp and size changes.

## Delay Analysis - TIA Data

- Required folder: data/projects/{project_id}/delay_analysis/steel_delay_tia_templates/.
- The app expects files such as 01-project_metadata_template.csv, 02- master_activity_steel_analysis.csv, 04- p6_activity_export.csv, 05- relationship_file.csv, and 11-concurrency_matrix_template.updated.csv.
- The BL comparison and MEP slides read from data/projects/{project_id}/bl/.
- Do not hard-code delay days. Update source files and let the TIA logic calculate from the available rows.

## Output Studio And Reports

- Output Studio is inside dashboard.py under the Output Studio tab.
- Linked executive dashboard exports use the selected project. If a setup slot has no rows, the app warns and uses the first project with actual data to avoid empty reports.
- Detailed Progress Report exports are generated from the live platform data.
- Output Studio eval command: python scripts/evaluate_output_studio.py --label your_label.

## Validation Commands

- Compile check: python -m compileall -q dashboard.py src scripts reports ui tests
- Delay TIA eval: python scripts/evaluate_delay_tia.py --label your_label
- Output Studio eval: python scripts/evaluate_output_studio.py --label your_label
- Streamlit AppTest is used in development to check default, PROJECT-02, and PROJECT-03 with zero exceptions.

## Safe Editing Rules

- Change data files first when the issue is wrong information.
- Change dashboard.py only when the issue is UI, routing, export logic, or shared loading behavior.
- Change src/construction_system/steel_delay_tia.py only when the TIA calculation itself is wrong.
- Keep root files as compatibility fallback unless you are sure every project has a complete project folder file.
- Before major changes, create a return snapshot.
