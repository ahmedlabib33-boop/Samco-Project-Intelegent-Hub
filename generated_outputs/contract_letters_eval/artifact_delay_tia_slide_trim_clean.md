# Contract & Claims / Letters Eval Artifact

Generated: 2026-06-15T06:54:18.364727+00:00

## Contract Center Status

{
  "contract_loaded": true,
  "last_analysis_date": "2026-06-15T06:54:17+00:00",
  "total_clauses": 66,
  "contract_version": "v1",
  "knowledge_base_status": "Ready",
  "reprocessed": true,
  "detected_files": [
    "Overall Contract.pdf",
    "Overall_Contract_clause_library.xlsx"
  ],
  "analysis_files": [
    "Overall_Contract_clause_library.xlsx"
  ],
  "supporting_files": [
    "Overall Contract.pdf"
  ],
  "source_warnings": [
    "Curated contract clause library is the active analysis source; non-library contract files are retained as source references.",
    "Overall Contract.pdf appears scanned or image-based with no extractable text; page rendering is available, but OCR is not installed. Install Tesseract and pytesseract for direct scanned-PDF clause extraction."
  ],
  "extraction_issue": "Curated contract clause library is the active analysis source; non-library contract files are retained as source references.; Overall Contract.pdf appears scanned or image-based with no extractable text; page rendering is available, but OCR is not installed. Install Tesseract and pytesseract for direct scanned-PDF clause extraction."
}

## Overall Contract PDF Readiness

{
  "exists": true,
  "pages": 34,
  "extractable_text_chars": 0,
  "is_scanned_or_image_based": true,
  "path": "C:\\Users\\pc\\OneDrive\\Desktop\\01 Letters\\Data analysis\\01-Contract\\Overall Contract.pdf",
  "diagnostics": {
    "file_name": "Overall Contract.pdf",
    "pages": 34,
    "extractable_text": false,
    "is_scanned_or_image_based": true,
    "render_preview_available": true,
    "render_engine": "pypdfium2",
    "ocr_available": false,
    "tesseract_path": "",
    "pytesseract_available": false
  }
}

## Contract Question Output

Decision: YES
Risk: Critical
Evidence strength: Very Strong (90/100)
Short answer: YES. The current contract library contains relevant clause support under EOT Entitlements, Risk Clauses, Evidence Requirements. The present evidence strength is Very Strong (90/100), so entitlement, proof, programme impact, and notice compliance must be addressed together.
Contractor interpretation: Delay from late drawings/instructions must be claimed under the notice procedure. Failure to comply with claim notice requirements is an irrevocable waiver and release of Employer/Engineer from claims. Contractor must submit shop drawings, as-built drawings, and source files where required. Contractor must submit a separate monthly account of all claims and variations; claims not included may not be considered.
Required evidence: Keep request dates, required-by dates, late response proof, and critical path analysis.; Maintain a live claims register and send protective notices early.; Maintain drawing register, revision history, approvals, and transmittals.; Use monthly claim account with status, amount, time, evidence, and updated particulars.; Update EOT register and forecast exposure weekly.
Missing evidence: Potential entitlement exists, but evidence is incomplete.; Daily/site records exist
Likely rejection: Delay is not critical, not on longest path, or not proven to affect completion.; The clause does not create the entitlement being claimed.; Claim is not substantiated.; No notice; Not on critical path; Concurrent delay; No programme impact; No causation
Contractor rebuttal: The event may be Employer-risk, but it is not automatically payable or excusable unless notice and particulars are on time.; This is one of the strongest clauses. A good claim can die if the notice procedure is missed.; Late or incomplete drawings can stop approvals, inspections, and taking-over.; A notice alone is not enough. Every month, live claims must be repeated and updated.; Even part of a week counts. Employer can use this as strong pressure once completion is late without EOT.
Next action: Validate notice compliance, assemble the missing evidence items, and tie the event to critical or near-critical activities before finalizing the claim position.
Claim strategy: Separate the analysis into five tracks: contractual entitlement, factual proof, delay causation, cost substantiation, and rebuttal strategy. Use the matched clauses first, then connect the event chronology, correspondence, and programme impact records.

## Client Rebuttal Output

Client argument summary: No notice, Contractor delay
Contractual risk: Critical
Contractor counterargument: This is one of the strongest clauses. A good claim can die if the notice procedure is missed.; Even a real Employer-caused delay can be lost if notice, particulars, monthly updates, or critical path proof are missing.; The event may be Employer-risk, but it is not automatically payable or excusable unless notice and particulars are on time.; A variation without a timely proposal and monthly claim account may become hard to recover later.; A steel delay claim needs proof that Contractor requested correctly, was ready to use it, and the delay hit critical path.; This protects against delay damages but blocks prolongation cost where Contractor and Employer delays overlap.; If the delay is Contractor-caused, recovery is usually at Contractor cost.; Even a real Employer-caused delay can be lost if notice, particulars, monthly updates, or critical path proof are missing.; Price adjustment is conditional. If Employer/Engineer says the Contractor caused the delay, the adjustment may be rejected.; A steel delay claim needs proof that Contractor requested correctly, was ready to use it, and the delay hit critical path.
Evidence needed: Maintain a live claims register and send protective notices early.; Maintain delay event register, notices, particulars, updates, and delay analysis.; Keep request dates, required-by dates, late response proof, and critical path analysis.; Use a variation register with instruction date, notice date, proposal date, status, and monthly update.; Keep approved programme, requisitions, delivery notes, stock records, and activity impacts.; Delay analysis must separate Employer delay, Contractor delay, and concurrent periods.; Keep productivity records and separate Contractor delay from Employer delay.; Maintain delay event register, notices, particulars, updates, and delay analysis.; Prepare CAPMAS index comparison, baseline prices, procurement dates, and delay responsibility analysis.; Keep approved programme, requisitions, delivery notes, stock records, and activity impacts.
Recommended response wording: The rejection based on 'No notice' is not conclusive. The contractor position is to rely on the contract wording, contemporaneous records, and the event chronology to defeat that defense. This is one of the strongest clauses. A good claim can die if the notice procedure is missed. Even a real Employer-caused delay can be lost if notice, particulars, monthly updates, or critical path proof are missing.

The rejection based on 'Contractor delay' is not conclusive. The contractor position is to rely on the contract wording, contemporaneous records, and the event chronology to defeat that defense. This protects against delay damages but blocks prolongation cost where Contractor and Employer delays overlap. If the delay is Contractor-caused, recovery is usually at Contractor cost.
Probability of success: High

## Claim Draft Output

Narrative: This draft claim addresses Late IFC drawings and delayed Engineer RFI response. It relies on the selected contractual clauses and the uploaded project evidence to establish entitlement, factual basis, and the required response strategy.
Contractual basis: - Clause : Revit and CAD deliverables -> Structural modeling must use Revit source files; other engineering is AutoCAD ASD unless stated.
- Clause : Rate of progress -> If progress is too slow, Contractor may be required to revise methods or accelerate.
- Clause : Concurrent delay rule -> For concurrent delays, Contractor may get EOT but no cost for the concurrent period if compliant.
Factual background: The claim arises from the event described as: Late IFC drawings and delayed Engineer RFI response. Supporting documents are listed below.
Cause and effect: The event 'Late IFC drawings and delayed Engineer RFI response' is presented as a EOT / Delay Claim matter. The selected clauses provide the contractual path, and the selected records are the factual basis required to prove cause, effect, and entitlement.
Evidence list: - eval_late_ifc_notice.txt (Letters Intelligence)
Entitlement statement: The contractor position is that entitlement under EOT / Delay Claim is at least potentially available subject to final substantiation.
Time impact statement: Time impact must be supported by CPM logic, TIA / window analysis, or other accepted schedule methodology where relevant.
Cost impact statement: Cost impact must be supported by contractual basis, valuation records, payment / procurement records, or measured variation data where relevant.
Rebuttal section: Client rejection summary: No notice, Contractor delay
Contractor counterargument: This is one of the strongest clauses. A good claim can die if the notice procedure is missed.; Even a real Employer-caused delay can be lost if notice, particulars, monthly updates, or critical path proof are missing.; A variation without a timely proposal and monthly claim account may become hard to recover later.; The event may be Employer-risk, but it is not automatically payable or excusable unless notice and particulars are on time.; A steel delay claim needs proof that Contractor requested correctly, was ready to use it, and the delay hit critical path.; This protects against delay damages but blocks prolongation cost where Contractor and Employer delays overlap.; If the delay is Contractor-caused, recovery is usually at Contractor cost.; Even a real Employer-caused delay can be lost if notice, particulars, monthly updates, or critical path proof are missing.; A steel delay claim needs proof that Contractor requested correctly, was ready to use it, and the delay hit critical path.; Price adjustment is conditional. If Employer/Engineer says the Contractor caused the delay, the adjustment may be rejected.
Evidence needed: Maintain a live claims register and send protective notices early.; Maintain delay event register, notices, particulars, updates, and delay analysis.; Use a variation register with instruction date, notice date, proposal date, status, and monthly update.; Keep request dates, required-by dates, late response proof, and critical path analysis.; Keep approved programme, requisitions, delivery notes, stock records, and activity impacts.; Delay analysis must separate Employer delay, Contractor delay, and concurrent periods.; Keep productivity records and separate Contractor delay from Employer delay.; Maintain delay event register, notices, particulars, updates, and delay analysis.; Keep approved programme, requisitions, delivery notes, stock records, and activity impacts.; Prepare CAPMAS index comparison, baseline prices, procurement dates, and delay responsibility analysis.
Recommended response: The rejection based on 'No notice' is not conclusive. The contractor position is to rely on the contract wording, contemporaneous records, and the event chronology to defeat that defense. This is one of the strongest clauses. A good claim can die if the notice procedure is missed. Even a real Employer-caused delay can be lost if notice, particulars, monthly updates, or critical path proof are missing.

The rejection based on 'Contractor delay' is not conclusive. The contractor position is to rely on the contract wording, contemporaneous records, and the event chronology to defeat that defense. This protects against delay damages but blocks prolongation cost where Contractor and Employer delays overlap. If the delay is Contractor-caused, recovery is usually at Contractor cost.
Attachment checklist: - Relevant contract clauses
- Notices and correspondence
- Event chronology
- Schedule / delay analysis support
- Commercial / cost support where applicable
- Contemporaneous records and approvals

## Letters Notice Register

Letters workbook: C:\Users\pc\Downloads\01-SAMCO-ACEPM_letters_linked (Final).xlsx
Notice Ref | Date | From Party | To Party | Type | Subject | Thread | Predicted Delay Type | Predicted Status | Reply Received | Reply Ref | Reply Date | Predicted Activity Text | Priority | Next Action
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
BD-CW-SAMCO-ACE-LET-STR-001 | 20-May-2025 | SAMCO | ACEPM | Delegation | Delegation of Authority | Delegation / administration | General correspondence | Open | No |  |  | Project administration |  | Record authorized representative
BD-CW-SAMCO-ACE-LET-STR-002 | 30-Jun-2025 | SAMCO | ACEPM | Delegation | Delegation of Authority | Delegation / administration | General correspondence | Open | No |  |  | Project administration |  | Update correspondence matrix
BD-CW-SAMCO-ACE-LET-STR-003 | 30-Jun-2025 | SAMCO | ACEPM | Response / Reservation | RE: Outstanding Deliverables - Urgent Response Required | Outstanding deliverables / tower cranes | General delay / EOT | Replied | Yes | BD-ACEPM-SAMCO-LET-001; BD-ACEPM-SAMCO-LET-002 | 24-Jun-2025; 25-Jun-2025 | Tower cranes, baseline program, shop drawings, soil replacement, steel inventory | High | Confirm closed deliverables and baseline dependency
BD-CW-SAMCO-ACE-LET-STR-004 | 28-Aug-2025 | SAMCO | ACEPM | Notice / Site Condition | RE: Site Survey Findings and Allocation of Concrete Batching Plant | Survey / batching plant / Zone 2 | General correspondence | Replied | Yes | BD-ACEPM-SAMCO-LET-003 | 31-Aug-2025 | Boundary excavation, ramp works, batching plant, Zone 2 works | Medium | Close survey/ramp/batching plant decisions
BD-CW-SAMCO-ACE-LET-STR-005 | 10-Sep-2025 | SAMCO | ACEPM | Notice of Delay / Site Obstacle | RE: Documentation of Site Obstacles Affecting Project Progress | Site obstacles / water leakage | General delay / EOT | Replied | Yes | BD-ACEPM-SAMCO-LET-005 | 17-Sep-2025 | DCPT, open pits, tank survey, excavation | High | Repair leakage, document affected period, update recovery plan
BD-CW-SAMCO-ACE-LET-STR-006 | 22-Sep-2025 | SAMCO | ACEPM | Response | RE: Response to Letter No. BD-ACEPM-SAMCO-LET-004 | Contractual submissions | General correspondence | Replied | Yes | BD-ACEPM-SAMCO-LET-004 | 17-Sep-2025 | Pre-construction submittals and reporting | Medium | Submit remaining contractual documents
BD-CW-SAMCO-ACE-LET-STR-007 | 24-Sep-2025 | SAMCO | ACEPM | Response / Reservation | RE: Response to Letter No. BD-ACEPM-SAMCO-LET-005 | Site obstacles / water leakage | General correspondence | Replied | Yes | BD-ACEPM-SAMCO-LET-005 | 17-Sep-2025 | Soil tests, grid leveling, excavation drawings, reporting | Medium | Track approvals and submit any claim with particulars
BD-CW-SAMCO-ACE-LET-STR-008 | 24-Sep-2025 | SAMCO | ACEPM | Claim Notice / Reservation | Response Regarding Site Ramp Modification Works | Ramp / access route | General correspondence | Replied | Yes | BD-ACEPM-SAMCO-LET-008 | 28-Sep-2025 | Service ramp, material access, site logistics | High | Determine access-route cost/time responsibility

## Relevant Clauses

clause_number | clause_title | section_name | claim_type | risk_level | claim_strength | notice_required | time_impact | cost_impact | required_evidence | recommended_action
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
 | Revit and CAD deliverables | Contractor Counterarguments | Counterargument / Exception | Medium | Medium | Yes | Yes | Yes | Maintain source files, model issue log, drawing register, and transmittals. | Maintain source files, model issue log, drawing register, and transmittals.
 | Rate of progress | Contractor Rights | General Contractor Entitlement | High | Strong | Yes | Yes | Yes | Keep productivity records and separate Contractor delay from Employer delay. | Keep productivity records and separate Contractor delay from Employer delay.
 | Concurrent delay rule | Contractor Rights | General Contractor Entitlement | Critical | Strong | Yes | Yes | Yes | Delay analysis must separate Employer delay, Contractor delay, and concurrent periods. | Delay analysis must separate Employer delay, Contractor delay, and concurrent periods.
 | No DAB and court route | Dispute Resolution | Dispute Resolution | Medium | Strong | Yes | Yes | Yes | Preserve full contemporaneous records and avoid relying on informal promises. | Preserve full contemporaneous records and avoid relying on informal promises.
 | Minimum IPC threshold | EOT Entitlements | Extension of Time | Medium | Strong | Yes | Yes | Yes | Align monthly valuation with approved cash flow and explain any shortfall. | Align monthly valuation with approved cash flow and explain any shortfall.
 | Delay damages | EOT Entitlements | Extension of Time | Critical | Medium | Yes | Yes | Yes | Update EOT register and forecast exposure weekly. | Update EOT register and forecast exposure weekly.
 | Document priority | EOT Entitlements | Extension of Time | High | Strong | Yes | Yes | Yes | Maintain discrepancy notices and Engineer responses. | Maintain discrepancy notices and Engineer responses.
 | Works shown in any document | EOT Entitlements | Extension of Time | Medium | Strong | Yes | Yes | Yes | Search all contract documents before asserting missing scope. | Search all contract documents before asserting missing scope.

## Late Drawing Search Ranking

clause_title | section_name | claim_type | risk_level | claim_strength | search_score
--- | --- | --- | --- | --- | ---
Delayed drawings or instructions | EOT Entitlements | Extension of Time | High | Strong | 96
Claims time bar | EOT Entitlements | Extension of Time | Critical | Strong | 66
Shop drawings and as-builts | Risk Clauses | General Contract Risk | Low | Weak | 66
Monthly claim and variation account | Evidence Requirements | Evidence / Substantiation | High | Strong | 58
Delay damages | EOT Entitlements | Extension of Time | Critical | Medium | 55
Extension of time | EOT Entitlements | Extension of Time | Critical | Strong | 52
Employer equipment and free-issue materials | EOT Entitlements | Extension of Time | High | Strong | 47
Force majeure | Evidence Requirements | Evidence / Substantiation | Critical | Strong | 44

## Evidence Mappings

id | evidence_document_id | clause_id | claim_category | mapping_score | mapping_basis | missing_evidence_items | created_at | updated_at | file_name | clause_number | clause_title | section_name
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
1 | 1 | 26 | Extension of Time | 31.0 | Evidence file 'eval_late_ifc_notice.txt' mapped by keyword/title overlap, late design/RFI signal, notice/time-bar signal, programme impact signal, records/mitigation signal to clause Delayed drawings or instructions. |  | 2026-06-15T06:54:18+00:00 | 2026-06-15T06:54:18+00:00 | eval_late_ifc_notice.txt |  | Delayed drawings or instructions | EOT Entitlements
2 | 1 | 19 | Extension of Time | 24.0 | Evidence file 'eval_late_ifc_notice.txt' mapped by keyword/title overlap, late design/RFI signal, notice/time-bar signal, programme impact signal to clause Document priority. |  | 2026-06-15T06:54:18+00:00 | 2026-06-15T06:54:18+00:00 | eval_late_ifc_notice.txt |  | Document priority | EOT Entitlements
4 | 1 | 25 | Notice Compliance | 23.0 | Evidence file 'eval_late_ifc_notice.txt' mapped by keyword/title overlap, late design/RFI signal, notice/time-bar signal, programme impact signal to clause Contractor documents timing. |  | 2026-06-15T06:54:18+00:00 | 2026-06-15T06:54:18+00:00 | eval_late_ifc_notice.txt |  | Contractor documents timing | Notice Requirements
3 | 1 | 43 | Extension of Time | 23.0 | Evidence file 'eval_late_ifc_notice.txt' mapped by keyword/title overlap, notice/time-bar signal, programme impact signal, records/mitigation signal to clause Extension of time. |  | 2026-06-15T06:54:18+00:00 | 2026-06-15T06:54:18+00:00 | eval_late_ifc_notice.txt |  | Extension of time | EOT Entitlements
5 | 1 | 50 | Variation / Change | 21.0 | Evidence file 'eval_late_ifc_notice.txt' mapped by keyword/title overlap, programme impact signal, cost/valuation signal, records/mitigation signal to clause Right to vary. |  | 2026-06-15T06:54:18+00:00 | 2026-06-15T06:54:18+00:00 | eval_late_ifc_notice.txt |  | Right to vary | Variation Entitlements
6 | 1 | 36 | Variation / Change | 20.0 | Evidence file 'eval_late_ifc_notice.txt' mapped by keyword/title overlap, notice/time-bar signal, programme impact signal, cost/valuation signal to clause Progress reports. |  | 2026-06-15T06:54:18+00:00 | 2026-06-15T06:54:18+00:00 | eval_late_ifc_notice.txt |  | Progress reports | Variation Entitlements
7 | 1 | 59 | Extension of Time | 18.0 | Evidence file 'eval_late_ifc_notice.txt' mapped by keyword/title overlap, notice/time-bar signal, programme impact signal to clause Claims time bar. |  | 2026-06-15T06:54:18+00:00 | 2026-06-15T06:54:18+00:00 | eval_late_ifc_notice.txt |  | Claims time bar | EOT Entitlements
8 | 1 | 33 | Extension of Time | 17.0 | Evidence file 'eval_late_ifc_notice.txt' mapped by keyword/title overlap, notice/time-bar signal, programme impact signal to clause Unforeseeable physical conditions. |  | 2026-06-15T06:54:18+00:00 | 2026-06-15T06:54:18+00:00 | eval_late_ifc_notice.txt |  | Unforeseeable physical conditions | EOT Entitlements

## Methodology Text Evidence

1.    INTRODUCTION
Changes can occur on almost every project and they often lead to delays and other negative impacts to the schedule and cost of a project. Large and complex engineering, procurement, and construction (EPC) projects are particularly susceptible to the negative impacts caused by changes. Changes can cause delay and disruption to engineering, procurement, fabrication, transportation and delivery, installation, and/or commissioning and startup activities. It is not unusual for an engineering change to cause a knock-on impact to successor procurement, fabrication, and installation work activities.
A change order or other impact can be modeled in a project CPM schedule using: 1) a group of added schedule activities, or fragnets; 2) adjustments to the durations of existing activities; 3) the insertion of lags or leads; and/or 4) imposed constraints. The overall objective of adding changes to a baseline or statused CPM schedule is to determine whether the overall completion date is improved, delayed, or remains the same as a result of the change. A well-known and widely utilized schedule delay analysis methodology is the Time Impact Analysis (TIA) or Update Impact Analysis (UIA), which is well suited for large and highly impacted projects and generally accepted as the preferred method to demonstrate a Contractor’s entitlement to a time extension or the Owner’s justification for receiving liquidated damages.
This article examines the various complexities in analyzing the schedule impact of multiple changes, with most examples drawn from a sample gas plant project. However, the topics that are discussed relate to a schedule delay analysis on any large, complex project. The sample gas plant project spanned several years and experienced approximately 16 months of delay and hundreds of alleged impacts. Retrospectively, the Owner had to determine a reasonable amount of time extension to grant an EPC Contractor due to 90 approved change orders. The authors utilized a TIA with multiple analysis windows1 to assess the approved change order delays.
2.    MANY EPC CONTRACTS REQUIRE IMPACTS TO BE INCORPORATED INTO THE SCHEDULE
Many EPC contracts require approved change orders and other impacts to be included in the CPM project execution schedules when these events occur. The main reason for a contemporaneous schedule impact analysis is to determine the magnitude of time impact, if any, that the change order or other type of impact would have on the overall r