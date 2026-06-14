from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parents[1]
LEGACY_WORKBOOK = Path(r"C:\Users\pc\Downloads\01-SAMCO-ACEPM_letters_linked (Final).xlsx")
UPDATED_WORKBOOK = PROJECT_DIR / "data" / "letters" / "01-SAMCO-ACEPM_letters_linked_updated.xlsx"
REPORT_PATH = PROJECT_DIR / "reports" / "letters_intelligence_ingest_report.md"
DOCS_DIR = PROJECT_DIR / "docs"
OCR_DIR = PROJECT_DIR / "tmp_letters_ocr"

SAMCO_SHEET = "From SAMCO to ACE"
ACE_SHEET = "From ACE to SAMCO"
SAMCO_LINKS_SHEET = "SAMCO to ACE Links"
ACE_LINKS_SHEET = "ACE to SAMCO Links"
THREADS_SHEET = "Issue Threads"


NEW_SAMCO_ROWS: dict[str, dict[str, str]] = {
    "BD-CW-SAMCO-ACE-LET-STR-070": {
        "Date": "25-Apr-2026",
        "Type": "Payment Submission",
        "Subject": "Submission of Interim Payment Certificate No. 6",
        "Main Purpose": "Submit IPC No. 6 for review and approval",
        "Key Requests": "Review and approve IPC 6",
        "Scope Impact": "No scope impact",
        "Responsibility": "Engineer / Employer for certification/payment",
        "Affected Activities": "Payment certification",
        "Start Dependency": "IPC submission",
        "Sequence Impact": "Low schedule, cash-flow impact",
        "Commercial Impact": "Payment due under contract",
        "Risk Type": "Commercial / Payment",
        "Risk Owner": "Employer / Engineer",
        "Delay Risk": "Low",
        "EOT Potential": "Conditional",
        "Claim Strength": "",
        "Required Actions": "Certify and pay IPC 6",
        "Thread": "Payments / IPCs / breakdown",
        "ACE Ref": "",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "Same IPC / payment thread; no direct ACE response in current source table",
        "Confidence": "Medium",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Review, certify, and pay IPC 6 within the contractual period",
    },
    "BD-CW-SAMCO-ACE-LET-STR-072": {
        "Date": "27-Apr-2026",
        "Type": "Submission / Meeting Minutes",
        "Subject": "Submission of Minutes of Meetings - MEP Works (First Fix).",
        "Main Purpose": "Submit MEP first-fix meeting minutes and preserve rights over missing information and design conflicts",
        "Key Requests": "Take note of the MOMs and issue any missing information / clarifications required for execution",
        "Scope Impact": "First-fix MEP works prior to concrete casting",
        "Responsibility": "Engineer / Design parties for information; SAMCO for execution only",
        "Affected Activities": "MEP first fix, embedded items, concrete casting interfaces",
        "Start Dependency": "Approved drawings and coordinated details before casting",
        "Sequence Impact": "Design conflicts and missing details can block first-fix execution and concrete casting sequence",
        "Commercial Impact": "Potential time and cost consequences expressly reserved",
        "Risk Type": "Interface / Design coordination",
        "Risk Owner": "Engineer / Employer",
        "Delay Risk": "High",
        "EOT Potential": "Moderate",
        "Claim Strength": "Moderate to Strong",
        "Required Actions": "Confirm MOM instructions, close design conflicts, and issue clarifications before casting",
        "Thread": "MEP / first fix / flanges / VI-0003",
        "ACE Ref": "",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "Same MEP first-fix coordination thread; no direct ACE response identified in the current source table",
        "Confidence": "Medium",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Formalize first-fix responsibilities and close outstanding design conflicts",
    },
    "BD-CW-SAMCO-ACE-LET-STR-073": {
        "Date": "28-Apr-2026",
        "Type": "Clarification / Technical Notice",
        "Subject": "Scope Clarification - Internal Tank Waterproofing.",
        "Main Purpose": "Request clarification on internal tank waterproofing scope and execution arrangement",
        "Key Requests": "Confirm status, responsible scope, and final execution arrangement for internal waterproofing",
        "Scope Impact": "Potential interface between structural scope, architectural scope, and internal tank waterproofing system",
        "Responsibility": "Engineer / Employer clarification on final scope",
        "Affected Activities": "Water tank internal waterproofing, repair / injection sequence, final lining works",
        "Start Dependency": "Architectural package issuance and Engineer instruction",
        "Sequence Impact": "Unclear waterproofing scope can delay the final tank execution sequence",
        "Commercial Impact": "Potential variation, warranty, and scope implications",
        "Risk Type": "Technical / Scope clarification",
        "Risk Owner": "Engineer / Employer",
        "Delay Risk": "Medium",
        "EOT Potential": "Conditional",
        "Claim Strength": "Moderate",
        "Required Actions": "Issue formal clarification on waterproofing scope and execution arrangement",
        "Thread": "Waterproofing materials",
        "ACE Ref": "",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "No direct ACE response in current source table",
        "Confidence": "Low",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Locate Engineer decision on internal waterproofing system and execution route",
    },
    "BD-CW-SAMCO-ACE-LET-STR-074": {
        "Date": "29-Apr-2026",
        "Type": "Response / Reporting Compliance",
        "Subject": "Re: Non-Compliance with Submission of Weekly Progress Reports.",
        "Main Purpose": "Respond to weekly reporting non-compliance notice and confirm recovery submissions",
        "Key Requests": "Allow one week to submit backlog and align a unified reporting format",
        "Scope Impact": "No scope impact; controls and reporting compliance",
        "Responsibility": "SAMCO for reporting; project-framework alignment is shared",
        "Affected Activities": "Weekly reporting, baseline monitoring, progress documentation",
        "Start Dependency": "Stable agreed reporting format and project phasing context",
        "Sequence Impact": "No direct physical delay, but contractual administration and reporting visibility are affected",
        "Commercial Impact": "Possible withholding / compliance exposure if unresolved",
        "Risk Type": "Controls / Contract compliance",
        "Risk Owner": "SAMCO / Shared",
        "Delay Risk": "Medium",
        "EOT Potential": "Low",
        "Claim Strength": "Weak to Moderate",
        "Required Actions": "Submit outstanding weekly reports and agree a unified reporting template",
        "Thread": "Contractual submissions / reports",
        "ACE Ref": "BD-ACEPM-SAMCO-LET-032",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "Direct response to ACE weekly reporting notice; ACE source letter is not available in the current workbook",
        "Confidence": "High",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Submit the overdue weekly reports and close the reporting-compliance issue formally",
    },
    "BD-CW-SAMCO-ACE-LET-STR-075": {
        "Date": "30-Apr-2026",
        "Type": "Commercial Response / Reservation",
        "Subject": "Re: BD-ACEPM-SAMCO-LET-031",
        "Main Purpose": "Respond to IPC settlement clarification and reserve rights due to project constraints",
        "Key Requests": "Continue timely certification and payment of IPCs under the Contract",
        "Scope Impact": "No scope impact but payment administration is affected by project constraints",
        "Responsibility": "Employer / Engineer for certification and payment; external constraints affecting progress are beyond SAMCO control",
        "Affected Activities": "IPCs, valuation of executed works, commercial administration",
        "Start Dependency": "Certification cycle and removal of steel/design/approval constraints",
        "Sequence Impact": "Reduced progress and valuation because of employer / engineer-driven constraints",
        "Commercial Impact": "Cash-flow exposure and reserved EOT / cost entitlement",
        "Risk Type": "Commercial / Payment",
        "Risk Owner": "Employer / Engineer",
        "Delay Risk": "Medium",
        "EOT Potential": "Conditional",
        "Claim Strength": "Moderate",
        "Required Actions": "Facilitate certification / payment and address the delaying constraints",
        "Thread": "Payments / IPCs / breakdown",
        "ACE Ref": "BD-ACEPM-SAMCO-LET-031",
        "ACE Date": "19-Apr-2026",
        "ACE Subject": "IPC settlement follow-up",
        "Relationship": "Direct response to ACE IPC clarification / threshold letter",
        "Confidence": "High",
        "ACE Claim Strength": "Contractor weak",
        "ACE Delay Risk": "Low",
        "Recommended Follow-up": "Reconcile IPC thresholds, due dates, and the constraint-driven reduction in certified values",
    },
    "BD-CW-SAMCO-ACE-LET-STR-076": {
        "Date": "09-May-2026",
        "Type": "Notice of Claim / Design Discrepancy",
        "Subject": "Notice of Claim - Impact of Revised Structural Drawings on Project Progress [Sub-Clause 1.9 / 8.4 / 20.1]",
        "Main Purpose": "Notify a claim for delay caused by revised structural packages and conflicting instructions",
        "Key Requests": "Acknowledge the delay event and assess EOT / cost implications",
        "Scope Impact": "Columns, shuttering, slabs, shop drawings, and construction sequence",
        "Responsibility": "Engineer / Employer design management",
        "Affected Activities": "Columns, shuttering, slab elements, shop drawing development",
        "Start Dependency": "Final coordinated structural package and consistent instructions",
        "Sequence Impact": "Works were suspended from 24-Mar-2026 until 30-Apr-2026 and the critical path was disrupted",
        "Commercial Impact": "Direct and indirect cost claim; prolongation exposure",
        "Risk Type": "Design coordination / Claim",
        "Risk Owner": "Engineer / Employer",
        "Delay Risk": "High",
        "EOT Potential": "High",
        "Claim Strength": "Strong",
        "Required Actions": "Recognize the hold period, issue a clear coordinated design basis, and assess the claim",
        "Thread": "Site progress / steel supply / RFI 17 / structural package discrepancy",
        "ACE Ref": "",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "Follow-on design package claim within the same structural discrepancy thread; no direct ACE reply in the current source table",
        "Confidence": "Medium",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Convert the design discrepancy chronology into a full cause-effect claim with hold period evidence",
    },
    "BD-CW-SAMCO-ACE-LET-STR-077": {
        "Date": "11-May-2026",
        "Type": "Variation Notice / Reservation of Rights",
        "Subject": "Notice of Variation and Reservation of Rights - Backfilling Works Behind Retaining Wall.",
        "Main Purpose": "Treat retaining-wall backfilling as a variation and preserve time / cost entitlement",
        "Key Requests": "Issue a Variation Order covering cost, time, and measurement procedure",
        "Scope Impact": "Additional backfilling methodology beyond original BOQ scope",
        "Responsibility": "Employer / Engineer to issue VO and confirm valuation route",
        "Affected Activities": "Retaining wall backfilling and dependent structural / earthworks activities",
        "Start Dependency": "Variation Order or written instruction",
        "Sequence Impact": "Delay in VO / instruction can affect execution and the critical path",
        "Commercial Impact": "Direct cost, overhead / profit, prolongation, and measurement entitlement",
        "Risk Type": "Variation / Commercial",
        "Risk Owner": "Employer / Engineer",
        "Delay Risk": "High",
        "EOT Potential": "High",
        "Claim Strength": "Strong",
        "Required Actions": "Issue the VO or written instruction and confirm valuation / time treatment",
        "Thread": "Retaining wall backfilling variation",
        "ACE Ref": "",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "No direct ACE response in current source table",
        "Confidence": "Low",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Issue VO, measure the work, and assess the critical-path impact of delayed instruction",
    },
    "BD-CW-SAMCO-ACE-LET-STR-078": {
        "Date": "11-May-2026",
        "Type": "Meeting Minutes Submission",
        "Subject": "Submission of MOM - Site Meeting for Mechanical Works (First Fix) Held on Wednesday 06/05/2026.",
        "Main Purpose": "Submit first-fix MEP site meeting minutes for record",
        "Key Requests": "Review the MOM and issue comments or amendments if any",
        "Scope Impact": "MEP first-fix coordination and execution records",
        "Responsibility": "Shared coordination between SAMCO, Engineer, and MEP stakeholders",
        "Affected Activities": "First-fix mechanical works and related coordination items",
        "Start Dependency": "Site coordination decisions and recorded action closure",
        "Sequence Impact": "Unresolved coordination items can delay first-fix and related civil sequencing",
        "Commercial Impact": "Potential indirect time / coordination consequences",
        "Risk Type": "Coordination / Interface",
        "Risk Owner": "Shared",
        "Delay Risk": "Medium",
        "EOT Potential": "Conditional",
        "Claim Strength": "Moderate",
        "Required Actions": "Close the MOM action items and confirm the first-fix coordination route",
        "Thread": "MEP / first fix / flanges / VI-0003",
        "ACE Ref": "",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "Same MEP first-fix coordination thread; no direct ACE response identified in the current source table",
        "Confidence": "Medium",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Track closure of MEP first-fix action items and preserve interface records",
    },
    "BD-CW-SAMCO-ACE-LET-STR-079": {
        "Date": "24-May-2026",
        "Type": "Procurement Delay / EOT Response",
        "Subject": "Reply to Notification of Reinforcement Steel Supply Status and Entitlement to Time Extensions",
        "Main Purpose": "Rebut the steel supply status notice and confirm delayed employer steel caused actual delay",
        "Key Requests": "Acknowledge the time impact and confirm the status of outstanding steel supply",
        "Scope Impact": "No scope change; employer free-issue steel delivery affected execution sequence",
        "Responsibility": "Employer / Client steel supply",
        "Affected Activities": "Reinforcement works and steel-dependent structural activities",
        "Start Dependency": "Full and timely delivery of steel batches",
        "Sequence Impact": "Delayed second batch and revised third batch requirements disrupted the planned construction sequence",
        "Commercial Impact": "Time-impact claim and mitigation cost exposure",
        "Risk Type": "Procurement / Delay",
        "Risk Owner": "Employer",
        "Delay Risk": "High",
        "EOT Potential": "High",
        "Claim Strength": "Strong",
        "Required Actions": "Finalize third-batch details, confirm prior supplies, and assess the time impact",
        "Thread": "Reinforcement steel supply",
        "ACE Ref": "BD-ACEPM-SAMCO-LET-035",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "Direct response to ACE steel supply / time-extension notification; ACE source letter is not available in the current workbook",
        "Confidence": "High",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Reconcile delivery dates, pending quantities, and the updated time-impact narrative",
    },
    "BD-CW-SAMCO-ACE-LET-STR-080": {
        "Date": "24-May-2026",
        "Type": "Delay Notice Response / Reservation",
        "Subject": "Response to Notice - Alleged Failure to Achieve Section (1) Milestone",
        "Main Purpose": "Respond to the milestone-failure notice and explain the combined steel, IFC, and RFI impacts",
        "Key Requests": "Assess the milestone position in the proper contractual context and accept a revised plan",
        "Scope Impact": "Section (1) milestone and critical structural activities",
        "Responsibility": "Employer (steel) / Engineer (IFC and RFI response)",
        "Affected Activities": "Steel-dependent critical activities, suspended IFC-affected works, Section (1) milestone",
        "Start Dependency": "Timely steel supply, resolved IFC conflicts, and timely RFI responses",
        "Sequence Impact": "Progress was disrupted from 18-Mar-2026 and milestone recovery now depends on the revised plan",
        "Commercial Impact": "Potential EOT and claim rights expressly preserved",
        "Risk Type": "Schedule / Design / Supply",
        "Risk Owner": "Employer / Engineer",
        "Delay Risk": "High",
        "EOT Potential": "High",
        "Claim Strength": "Strong",
        "Required Actions": "Assess impacted activities, review the revised plan, and evaluate entitlement",
        "Thread": "Site progress / steel supply / RFI 17 / structural package discrepancy",
        "ACE Ref": "BD-ACEPM-SAMCO-LET-036",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "Direct response to ACE milestone notice; ACE source letter is not available in the current workbook",
        "Confidence": "High",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Tie the milestone miss to explicit steel, IFC, and RFI cause-effect records and submit the revised plan",
    },
    "BD-CW-SAMCO-ACE-LET-STR-081": {
        "Date": "24-May-2026",
        "Type": "Payment Submission",
        "Subject": "Submission of Interim Payment Certificate No. 7",
        "Main Purpose": "Submit IPC No. 7 for review and approval",
        "Key Requests": "Review and approve IPC 7",
        "Scope Impact": "No scope impact",
        "Responsibility": "Engineer / Employer for certification/payment",
        "Affected Activities": "Payment certification",
        "Start Dependency": "IPC submission",
        "Sequence Impact": "Low schedule, cash-flow impact",
        "Commercial Impact": "Payment due under contract",
        "Risk Type": "Commercial / Payment",
        "Risk Owner": "Employer / Engineer",
        "Delay Risk": "Low",
        "EOT Potential": "Conditional",
        "Claim Strength": "",
        "Required Actions": "Certify and pay IPC 7",
        "Thread": "Payments / IPCs / breakdown",
        "ACE Ref": "",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "Same IPC / payment thread; no direct ACE response in current source table",
        "Confidence": "Medium",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Review, certify, and pay IPC 7 within the contractual period",
    },
    "BD-CW-SAMCO-ACE-LET-STR-082": {
        "Date": "25-May-2026",
        "Type": "Clarification / Claim Notice",
        "Subject": "Clarification on Internal Waterproofing System, Execution Sequence and Performance Warranty - Water Tank.",
        "Main Purpose": "Clarify the water-tank waterproofing system and reserve claim rights over delayed instruction",
        "Key Requests": "Confirm the final approved waterproofing system and responsible executing party",
        "Scope Impact": "Tank waterproofing, repair / injection sequence, and warranty responsibility",
        "Responsibility": "Engineer / Employer / architectural scope clarification",
        "Affected Activities": "Water tank repair works, internal waterproofing, and warranty completion path",
        "Start Dependency": "Engineer clarification, approved system, and coordinated architectural information",
        "Sequence Impact": "Tank works sequence and warranty path remain blocked without final instruction",
        "Commercial Impact": "Potential additional cost and EOT claim due to delayed clarification",
        "Risk Type": "Technical / Contractual entitlement",
        "Risk Owner": "Engineer / Employer",
        "Delay Risk": "High",
        "EOT Potential": "High",
        "Claim Strength": "Moderate to Strong",
        "Required Actions": "Issue the final instruction on the waterproofing system and assess entitlement effects",
        "Thread": "Waterproofing materials",
        "ACE Ref": "",
        "ACE Date": "",
        "ACE Subject": "",
        "Relationship": "No direct ACE response in current source table; this is a follow-on clarification / claim notice to STR-073 and the tank RFI",
        "Confidence": "Medium",
        "ACE Claim Strength": "",
        "ACE Delay Risk": "",
        "Recommended Follow-up": "Resolve the waterproofing system decision and preserve the sequence / warranty claim record",
    },
}


THREAD_UPDATES = {
    "Contractual submissions / reports": {
        "samco": ["STR-074"],
        "ace": ["LET-032"],
        "main_link": "Submittals, programme, and periodic reporting compliance",
        "priority": "High",
        "next_action": "Agree reporting baseline, submit overdue weekly reports, and close the reporting-compliance issue.",
    },
    "MEP / first fix / flanges / VI-0003": {
        "samco": ["STR-072", "STR-078"],
        "ace": [],
        "main_link": "Scope dispute and first-fix coordination evolving into conditional execution under VO and MOM instructions",
        "priority": "High",
        "next_action": "Finalize VO, BOQ, supervision, first-fix responsibilities, and close MOM action items.",
    },
    "Payments / IPCs / breakdown": {
        "samco": ["STR-070", "STR-075", "STR-081"],
        "ace": ["LET-031"],
        "main_link": "IPC submissions and payment-delay allegations versus ACE threshold response and project-constraint reservation",
        "priority": "High",
        "next_action": "Reconcile IPC thresholds, due dates, certification timing, deductions, and interest exposure.",
    },
    "Waterproofing materials": {
        "samco": ["STR-073", "STR-082"],
        "ace": [],
        "main_link": "Clarification and claim path on internal tank waterproofing scope, sequence, and warranty",
        "priority": "High",
        "next_action": "Issue a final waterproofing decision and document its sequence, scope, and entitlement effects.",
    },
    "Reinforcement steel supply": {
        "samco": ["STR-079"],
        "ace": ["LET-035"],
        "main_link": "Owner steel supply delay, mitigation deliveries, and time-impact entitlement",
        "priority": "High",
        "next_action": "Reconcile delivery dates, mitigation quantities, third-batch requirements, and time impact.",
    },
    "Site progress / steel supply / RFI 17 / structural package discrepancy": {
        "samco": ["STR-076", "STR-080"],
        "ace": ["LET-033", "LET-036"],
        "main_link": "SAMCO claim chain on structural-package discrepancies, steel supply, delayed technical response, and milestone impact",
        "priority": "High",
        "next_action": "Convert the notice chain into a compliant substantiated claim with critical-path, milestone, and cause-effect evidence.",
    },
    "Retaining wall backfilling variation": {
        "samco": ["STR-077"],
        "ace": [],
        "main_link": "Variation notice for retaining-wall backfilling with no ACE response in the current source table",
        "priority": "High",
        "next_action": "Issue the VO, confirm valuation, and assess any critical-path effect from delayed instruction.",
    },
}


def suffix_number(value: str) -> int:
    match = re.search(r"(\d{3})$", str(value))
    return int(match.group(1)) if match else 999999


def normalize_list_string(value: str) -> list[str]:
    text = str(value or "").strip()
    if not text or text.lower() == "nan":
        return []
    return [item.strip() for item in text.split(";") if item.strip()]


def join_unique(items: list[str]) -> str:
    seen: list[str] = []
    for item in items:
        clean = str(item).strip()
        if clean and clean not in seen:
            seen.append(clean)
    return "; ".join(seen)


def build_sheet_row_map(df: pd.DataFrame, key_col: str) -> dict[str, int]:
    return {str(value).strip(): idx + 2 for idx, value in enumerate(df[key_col].tolist()) if str(value).strip()}


def update_issue_threads(threads_df: pd.DataFrame) -> pd.DataFrame:
    thread_map = {str(row["Thread"]).strip(): idx for idx, row in threads_df.iterrows()}
    for thread_name, payload in THREAD_UPDATES.items():
        samco_refs = join_unique(normalize_list_string(threads_df.loc[thread_map[thread_name], "SAMCO Ref(s)"]) + payload["samco"]) if thread_name in thread_map else join_unique(payload["samco"])
        ace_refs = join_unique(normalize_list_string(threads_df.loc[thread_map[thread_name], "6"]) + payload["ace"]) if thread_name in thread_map else join_unique(payload["ace"])
        row = {
            "Thread": thread_name,
            "SAMCO Ref(s)": samco_refs,
            "6": ace_refs,
            "Main Link": payload["main_link"],
            "Priority": payload["priority"],
            "Next Action": payload["next_action"],
        }
        if thread_name in thread_map:
            for col, value in row.items():
                threads_df.loc[thread_map[thread_name], col] = value
        else:
            threads_df = pd.concat([threads_df, pd.DataFrame([row])], ignore_index=True)
    return threads_df


def main() -> None:
    if not LEGACY_WORKBOOK.exists():
        raise FileNotFoundError(f"Legacy workbook not found: {LEGACY_WORKBOOK}")

    UPDATED_WORKBOOK.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    sheets = pd.read_excel(LEGACY_WORKBOOK, sheet_name=None)
    samco_df = sheets[SAMCO_SHEET].copy()
    ace_df = sheets[ACE_SHEET].copy()
    samco_links_df = sheets[SAMCO_LINKS_SHEET].copy()
    ace_links_df = sheets[ACE_LINKS_SHEET].copy()
    threads_df = sheets[THREADS_SHEET].copy()

    existing_refs = set(samco_df["Ref No"].astype(str).str.strip())
    for ref_no, row in NEW_SAMCO_ROWS.items():
        if ref_no in existing_refs:
            continue
        samco_row = {"Ref No": ref_no}
        for column in samco_df.columns:
            if column == "Ref No":
                continue
            samco_row[column] = row.get(column, "")
        samco_df = pd.concat([samco_df, pd.DataFrame([samco_row])], ignore_index=True)

    samco_df["__sort"] = samco_df["Ref No"].map(suffix_number)
    samco_df = samco_df.sort_values("__sort").drop(columns="__sort").reset_index(drop=True)

    samco_row_map = build_sheet_row_map(samco_df, "Ref No")
    ace_row_map = build_sheet_row_map(ace_df, "Ref No")

    existing_link_refs = set(samco_links_df["SAMCO Ref No"].astype(str).str.strip())
    new_link_rows = []
    for ref_no, row in NEW_SAMCO_ROWS.items():
        if ref_no in existing_link_refs:
            continue
        new_link_rows.append(
            {
                "Thread": row["Thread"],
                "SAMCO Ref No": ref_no,
                "SAMCO Sheet Row": samco_row_map.get(ref_no, ""),
                "SAMCO Date": row["Date"],
                "SAMCO Type": row["Type"],
                "SAMCO Subject": row["Subject"],
                "Related ACE Ref No(s)": row["ACE Ref"],
                "ACE Sheet Row(s)": ace_row_map.get(row["ACE Ref"], "") if row["ACE Ref"] else "",
                "ACE Date(s)": row["ACE Date"],
                "ACE Subject(s)": row["ACE Subject"],
                "Relationship": row["Relationship"],
                "Confidence": row["Confidence"],
                "SAMCO Claim Strength": row["Claim Strength"],
                "ACE Claim Strength": row["ACE Claim Strength"],
                "SAMCO Delay Risk": row["Delay Risk"],
                "ACE Delay Risk": row["ACE Delay Risk"],
                "Recommended Follow-up": row["Recommended Follow-up"],
            }
        )
    if new_link_rows:
        samco_links_df = pd.concat([samco_links_df, pd.DataFrame(new_link_rows)], ignore_index=True)

    samco_links_df["SAMCO Sheet Row"] = samco_links_df["SAMCO Ref No"].astype(str).map(samco_row_map).fillna("")
    samco_links_df["ACE Sheet Row(s)"] = samco_links_df["Related ACE Ref No(s)"].astype(str).map(ace_row_map).fillna(samco_links_df["ACE Sheet Row(s)"])

    direct_ace_updates = {
        "BD-ACEPM-SAMCO-LET-031": ["BD-CW-SAMCO-ACE-LET-STR-075"],
    }
    ace_subject_map = {str(row["Ref No"]).strip(): str(row["Subject"]).strip() for _, row in samco_df.iterrows()}
    for ace_ref, related_samco_refs in direct_ace_updates.items():
        match = ace_links_df["ACE Ref No"].astype(str).str.strip().eq(ace_ref)
        if not match.any():
            continue
        idx = ace_links_df[match].index[0]
        current_refs = normalize_list_string(ace_links_df.loc[idx, "Related SAMCO Ref No(s)"])
        merged_refs = join_unique(current_refs + related_samco_refs)
        merged_rows = join_unique([str(samco_row_map.get(ref, "")) for ref in normalize_list_string(merged_refs)])
        merged_subjects = join_unique([f"{ref} - {ace_subject_map.get(ref, '')}".strip(" -") for ref in normalize_list_string(merged_refs)])
        current_threads = normalize_list_string(ace_links_df.loc[idx, "Thread(s)"])
        thread_names = [NEW_SAMCO_ROWS[ref]["Thread"] for ref in related_samco_refs if ref in NEW_SAMCO_ROWS]
        ace_links_df.loc[idx, "Related SAMCO Ref No(s)"] = merged_refs
        ace_links_df.loc[idx, "SAMCO Sheet Row(s)"] = merged_rows
        ace_links_df.loc[idx, "SAMCO Subject(s)"] = merged_subjects
        ace_links_df.loc[idx, "Thread(s)"] = join_unique(current_threads + thread_names)

    threads_df = update_issue_threads(threads_df)

    folder_refs: dict[str, list[str]] = {}
    for pdf in DOCS_DIR.rglob("*.pdf"):
        folder_refs.setdefault(pdf.stem, []).append(pdf.parent.name)
    duplicate_conflicts = {ref: folders for ref, folders in folder_refs.items() if len(folders) > 1}

    report_lines = [
        "# Letters Intelligence Ingest Report",
        "",
        f"- Source workbook: `{LEGACY_WORKBOOK}`",
        f"- Updated workbook: `{UPDATED_WORKBOOK}`",
        f"- Source docs folder: `{DOCS_DIR}`",
        "",
        "## Findings",
        "",
        f"- New SAMCO letters added to the intelligence workbook: {len(NEW_SAMCO_ROWS)}",
        f"- New ACEPM letters added: 0",
        "- The folder named `From ACEPM to Slamco` contains PDFs whose content, letterhead, reference pattern, and addressee show they are SAMCO-to-ACEPM letters, not ACEPM-to-SAMCO letters.",
        "- Therefore, no new rows were added to `From ACE to SAMCO` from these folders, to avoid misleading directionality.",
        "- The references `BD-ACEPM-SAMCO-LET-032`, `BD-ACEPM-SAMCO-LET-035`, and `BD-ACEPM-SAMCO-LET-036` are cited by the new SAMCO letters but their source ACEPM letters are not present in the current workbook or provided folders.",
        "",
        "## Duplicate Reference Conflicts",
        "",
    ]
    if duplicate_conflicts:
        for ref, folders in sorted(duplicate_conflicts.items()):
            report_lines.append(f"- `{ref}` appears in multiple folders: {', '.join(sorted(folders))}")
    else:
        report_lines.append("- No duplicate reference conflicts detected.")

    report_lines.extend(
        [
            "",
            "## New SAMCO References Added",
            "",
        ]
    )
    for ref, row in NEW_SAMCO_ROWS.items():
        report_lines.append(f"- `{ref}` | `{row['Date']}` | `{row['Subject']}` | Thread: `{row['Thread']}`")

    REPORT_PATH.write_text("\n".join(report_lines), encoding="utf-8")

    with pd.ExcelWriter(UPDATED_WORKBOOK, engine="openpyxl") as writer:
        samco_df.to_excel(writer, sheet_name=SAMCO_SHEET, index=False)
        ace_df.to_excel(writer, sheet_name=ACE_SHEET, index=False)
        samco_links_df.to_excel(writer, sheet_name=SAMCO_LINKS_SHEET, index=False)
        ace_links_df.to_excel(writer, sheet_name=ACE_LINKS_SHEET, index=False)
        threads_df.to_excel(writer, sheet_name=THREADS_SHEET, index=False)

    print(f"Updated workbook written to: {UPDATED_WORKBOOK}")
    print(f"Report written to: {REPORT_PATH}")


if __name__ == "__main__":
    main()
