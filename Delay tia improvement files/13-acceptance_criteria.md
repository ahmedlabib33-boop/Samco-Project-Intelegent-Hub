# Acceptance Criteria

## Non-negotiable rules
- no existing feature removed,
- no existing export removed,
- existing Delay TIA tabs remain available,
- SAMCO remains display-only in steel delay calculations.

## Functional acceptance
1. The system builds all canonical datasets listed in the improvement note.
2. Every stock-out / steel delay event becomes a row in `delay_event_register_df`.
3. Every claimed delayed activity has:
   - pre-impact forecast finish,
   - impacted forecast finish,
   - claimed delay duration.
4. Every fragnet recommendation has:
   - predecessor,
   - successor,
   - start,
   - finish,
   - rationale,
   - evidence reference.
5. BL vs current path state is used in TIA conclusions, not only displayed.
6. The DOCX report is filled without changing the original template design.
7. Primavera fragnet output is import-grade.
8. XER stage-1 export pack is generated.

## Quality acceptance
1. No current dashboard section breaks.
2. Upload-driven Delay TIA still works.
3. The same source logic feeds CSV, XLSX, HTML, and DOCX outputs.
4. All new tables are exportable.
5. Every conclusion can be traced back to evidence.
