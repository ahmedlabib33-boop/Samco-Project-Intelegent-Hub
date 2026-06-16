# Multi-Project Dashboard Roadmap

## Current Control Rule

All active CSV files in `data/import_templates`, `steel_delay_tia_templates`, and `BL fixed` include `project_id`.

The dashboard selector reads `data/import_templates/projects.csv`. When a dataset has `project_id`, the dashboard filters it to the selected project. Shared reference files can still be used, but project records should always carry `project_id`.

Each project also has its own working folder under `data/projects/{project_id}`. When a selected project has a file in its project folder, the app reads that project-owned file first. If no project-owned file exists, the app falls back to the existing root file so older workflows continue to work.

The app is currently prepared with three selectable project records:

- `The Big -P.01-UP-20-April-26` - active project with current data.
- `PROJECT-02` - setup slot for the second project.
- `PROJECT-03` - setup slot for the third project.

If a selected project has no rows in a data table yet, the dashboard must show empty / zero values for that table. It must not fall back to another project's records.

## Project Folder Structure

```text
Project Intelligence Hub/
  data/
    import_templates/
      projects.csv                     # master project registry only
      activities.csv
      evm.csv
      contracts.csv
      payments.csv
      ...
    projects/
      The Big -P.01-UP-20-April-26/
        data/
          import_templates/
            activities.csv
            evm.csv
            contracts.csv
            payments.csv
            ...
        delay_analysis/
          steel_delay_tia_templates/
            01-project_metadata_template.csv
            ...
            13-client_steel_supply_by_dia_wide.csv
        bl/
          BL Schedule.csv
          BL critical path.csv
          BL float bath.csv
          Bl Longest bath.csv
          MEP Activities.csv
          MEP Civil Logic.csv
          MEP Schedule.csv
        fixed/
        source_excel/
        evidence/
        exports/
        reports/
        notes/
      PROJECT-02/
        data/
          import_templates/
        delay_analysis/
          steel_delay_tia_templates/
        bl/
        fixed/
        source_excel/
        evidence/
        exports/
        reports/
        notes/
      PROJECT-03/
        data/
          import_templates/
        delay_analysis/
          steel_delay_tia_templates/
        bl/
        fixed/
        source_excel/
        evidence/
        exports/
        reports/
        notes/
  steel_delay_tia_templates/
    # legacy/fallback Delay TIA source files
    01-project_metadata_template.csv
    ...
    11-concurrency_matrix_template.updated.csv
  BL fixed/
    # legacy/fallback baseline source files
    BL Schedule.csv
    BL critical path.csv
    BL float bath.csv
    Bl Longest bath.csv
```

## Adding A New Project

1. Add one row to `data/import_templates/projects.csv` with a unique `project_id`.
2. Copy the folder structure from `data/projects/PROJECT-02` or `data/projects/PROJECT-03`.
3. Put the project's operational CSV files in `data/projects/{project_id}/data/import_templates`.
4. Put the project's Delay Analysis - TIA files in `data/projects/{project_id}/delay_analysis/steel_delay_tia_templates`.
5. Put the project's baseline, longest path, float, critical path, and MEP schedule files in `data/projects/{project_id}/bl`.
6. Keep `project_id` populated in every CSV row.
7. Use the dashboard dropdown to select the active project.
8. Exports should use the selected project only.

The root folders remain as fallback and compatibility sources. For daily use, update the files inside the selected project folder.

## Future Enhancements

1. Add a project data-quality screen showing missing `project_id`, orphan project IDs, and row counts by project.
2. Add an import wizard that tags uploaded Excel/CSV files with the chosen `project_id`.
3. Add a project archive switch so closed projects remain selectable but are hidden by default.
4. Add cross-project portfolio views only after single-project filtering is stable.
