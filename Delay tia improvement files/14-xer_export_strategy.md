# XER Export Strategy

## Objective
Produce Primavera-ready outputs without generating an unreliable `.xer`.

## Stage 1: XER-ready export pack
Generate:
- fragnet activities table,
- activity relationship table,
- WBS mapping table,
- calendar mapping table,
- import instructions,
- field mapping sheet.

This stage is mandatory before any real `.xer` writer.

## Stage 2: true XER builder
Only start after stage 1 is validated against a real Primavera import cycle.

Requirements:
- sample accepted XER from the same project family,
- stable project ID and WBS mapping,
- activity ID rule,
- relationship code rule,
- calendar rule,
- validation checklist against Primavera import behavior.

## Rule
Do not generate a true `.xer` until the import-grade CSV pack is proven.
