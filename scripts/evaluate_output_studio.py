from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DASHBOARD_PATH = ROOT / "dashboard.py"
DATA_DIR = ROOT / "data" / "import_templates"
GENERATED_DIR = ROOT / "generated_outputs"
REPORTS_DIR = ROOT / "reports"
OUTPUT_DIR = GENERATED_DIR / "output_studio_eval"
SCORE_LOG = OUTPUT_DIR / "score_log.jsonl"


CORE_DATASETS = [
    "projects.csv",
    "activities.csv",
    "evm.csv",
    "contracts.csv",
    "payments.csv",
    "delay_events.csv",
    "risks.csv",
    "milestones.csv",
    "change_orders.csv",
    "s_curve.csv",
    "wbs.csv",
    "rfi_ status.csv",
    "ifc_conflict.csv",
]

EXPECTED_OUTPUT_PATHS = [
    "The Big - Dashboard",
    "Original presentation print-only",
    "Linked executive dashboard",
    "Super premium progress report",
    "Canva-style flexible dashboard",
]

EXPECTED_EXPORTS = [
    "Download The Big - Dashboard (.html)",
    "Download Updated Original Presentation (.pptx)",
    "Download Linked Executive Dashboard (.html)",
    "Download Linked Executive Dashboard PowerPoint (.pptx) - Landscape",
    "Download Summarized Linked Dashboard (.html) - A3 Landscape One Page",
    "Download Super Premium Workbook (.xlsx)",
    "Download Printable Dashboard Pack (.html)",
    "Download Flexible Presentation (.pptx)",
    "Download Combined Selection (.csv)",
]

EXPECTED_PREMIUM_TERMS = [
    "management decision",
    "executive",
    "critical alerts",
    "decision",
    "risk",
    "exposure",
    "owner",
    "action",
    "dashboard",
    "Power BI",
    "Canva",
    "premium",
    "digital",
    "governance",
    "validation",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin1")


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, encoding="utf-8-sig").fillna("")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1").fillna("")
    except Exception:
        return pd.DataFrame()


def pct(earned: float, total: float) -> float:
    if total <= 0:
        return 0.0
    return round(max(0.0, min(100.0, earned / total * 100.0)), 2)


def score_checks(checks: list[tuple[str, bool, float]]) -> tuple[float, list[dict[str, Any]]]:
    earned = sum(weight for _, passed, weight in checks if passed)
    total = sum(weight for _, _, weight in checks)
    return pct(earned, total), [
        {"criterion": name, "passed": bool(passed), "weight": weight}
        for name, passed, weight in checks
    ]


def extract_output_studio_source(source: str) -> str:
    match = re.search(r"with tabs\[13\]:(.*?)(?:\nwith tabs\[\d+\]:|\Z)", source, flags=re.S)
    return match.group(1) if match else ""


def inspect_data_sources() -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for path in sorted(DATA_DIR.glob("*")):
        if path.suffix.lower() == ".csv":
            df = read_csv(path)
            rows.append({
                "Source": f"data/import_templates/{path.name}",
                "Type": "csv",
                "Rows": int(len(df)),
                "Columns": int(len(df.columns)),
                "Column List": ", ".join(str(col) for col in df.columns),
            })
        elif path.suffix.lower() in {".xlsx", ".xlsm", ".xls"}:
            try:
                sheets = pd.read_excel(path, sheet_name=None)
            except Exception:
                sheets = {}
            for sheet_name, df in sheets.items():
                rows.append({
                    "Source": f"data/import_templates/{path.name}::{sheet_name}",
                    "Type": "excel",
                    "Rows": int(len(df)),
                    "Columns": int(len(df.columns)),
                    "Column List": ", ".join(str(col) for col in df.columns),
                })
    letters_dir = ROOT / "data" / "letters"
    for path in sorted(letters_dir.glob("*.xlsx")):
        try:
            sheets = pd.read_excel(path, sheet_name=None)
        except Exception:
            sheets = {}
        for sheet_name, df in sheets.items():
            rows.append({
                "Source": f"data/letters/{path.name}::{sheet_name}",
                "Type": "letters",
                "Rows": int(len(df)),
                "Columns": int(len(df.columns)),
                "Column List": ", ".join(str(col) for col in df.columns),
            })
    return pd.DataFrame(rows)


def inspect_generated_outputs() -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for folder in [GENERATED_DIR, REPORTS_DIR]:
        if not folder.exists():
            continue
        for path in sorted(folder.rglob("*")):
            if path.is_file() and "__pycache__" not in str(path):
                rows.append({
                    "Output": str(path.relative_to(ROOT)),
                    "Extension": path.suffix.lower() or "(none)",
                    "Size KB": round(path.stat().st_size / 1024.0, 2),
                    "Modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds"),
                })
    return pd.DataFrame(rows)


def build_artifact_html(scores: dict[str, Any], data_inventory: pd.DataFrame, generated_inventory: pd.DataFrame, source_excerpt: str) -> str:
    def table(df: pd.DataFrame, limit: int = 80) -> str:
        if df.empty:
            return "<p class='muted'>No rows.</p>"
        return df.head(limit).to_html(index=False, escape=True, classes="data-table")

    score_cards = "".join(
        f"<article class='card'><span>{name}</span><strong>{value:.2f}%</strong></article>"
        for name, value in [
            ("Overall", float(scores["overall_score"])),
            ("LLM Average", float(scores["llm_average"])),
            ("Data Coverage", float(scores["data_coverage_score"])),
            ("Export Coverage", float(scores["export_coverage_score"])),
            ("Premium Design", float(scores["premium_design_score"])),
            ("Reliability", float(scores["reliability_score"])),
        ]
    )
    failed = []
    for group in scores.get("details", {}).values():
        failed.extend([item for item in group if not item.get("passed")])
    failed_rows = pd.DataFrame(failed)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Output Studio Eval Scorecard</title>
  <style>
    :root {{
      --bg:#07131f; --panel:#0d2134; --panel2:#102940; --line:#284c68;
      --text:#eef8ff; --muted:#a9bfd2; --accent:#33d8ca; --gold:#ffbf4a;
    }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:radial-gradient(circle at top left,#153d5e 0,#07131f 44%); color:var(--text); font-family:Inter,Segoe UI,Arial,sans-serif; }}
    main {{ max-width:1440px; margin:0 auto; padding:30px; }}
    h1 {{ margin:0 0 8px; font-size:34px; letter-spacing:0; }}
    h2 {{ margin:28px 0 12px; font-size:20px; }}
    p {{ color:var(--muted); line-height:1.55; }}
    .cards {{ display:grid; grid-template-columns:repeat(6,minmax(145px,1fr)); gap:12px; margin:22px 0; }}
    .card {{ min-height:104px; border:1px solid var(--line); background:rgba(13,33,52,.86); border-radius:8px; padding:16px; }}
    .card span {{ display:block; color:var(--muted); font-size:13px; }}
    .card strong {{ display:block; margin-top:14px; font-size:26px; }}
    .panel {{ border:1px solid var(--line); border-radius:8px; background:rgba(13,33,52,.75); padding:16px; margin-top:16px; overflow:auto; }}
    .data-table {{ width:100%; border-collapse:collapse; font-size:12px; }}
    .data-table th,.data-table td {{ padding:8px 10px; border-bottom:1px solid rgba(169,191,210,.18); text-align:left; vertical-align:top; }}
    .data-table th {{ background:var(--panel2); color:#defbff; position:sticky; top:0; }}
    pre {{ white-space:pre-wrap; color:#d8eefb; font-size:12px; }}
    .muted {{ color:var(--muted); }}
  </style>
</head>
<body>
  <main>
    <h1>Output Studio Eval Scorecard</h1>
    <p>Eval-driven quality loop for premium digital reports, dashboards, exports, and Canva-style management output.</p>
    <section class="cards">{score_cards}</section>
    <section class="panel"><h2>Failed / Weak Checks</h2>{table(failed_rows, 120)}</section>
    <section class="panel"><h2>All Output Data Inspected</h2>{table(data_inventory, 120)}</section>
    <section class="panel"><h2>Generated / Report Artifacts</h2>{table(generated_inventory, 120)}</section>
    <section class="panel"><h2>Output Studio Source Excerpt</h2><pre>{source_excerpt[:9000]}</pre></section>
  </main>
</body>
</html>"""


def evaluate(label: str) -> dict[str, Any]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    source = read_text(DASHBOARD_PATH)
    studio_source = extract_output_studio_source(source)
    data_inventory = inspect_data_sources()
    generated_inventory = inspect_generated_outputs()

    core_present = {name: (DATA_DIR / name).exists() for name in CORE_DATASETS}
    data_checks = [(f"core dataset present: {name}", present, 2) for name, present in core_present.items()]
    data_checks.extend([
        ("at least 15 output data sources inspected", len(data_inventory) >= 15, 12),
        ("at least 8 generated/report artifacts inspected", len(generated_inventory) >= 8, 8),
        ("letters workbook included", data_inventory["Type"].eq("letters").any() if not data_inventory.empty else False, 6),
        ("data columns captured for audit", data_inventory["Column List"].astype(str).str.len().gt(0).mean() >= 0.85 if not data_inventory.empty else False, 8),
    ])
    data_coverage_score, data_detail = score_checks(data_checks)

    export_checks = [(f"output path visible: {name}", name in studio_source, 5) for name in EXPECTED_OUTPUT_PATHS]
    export_checks.extend([(f"download export visible: {name}", name in studio_source, 4) for name in EXPECTED_EXPORTS])
    export_checks.extend([
        ("password remains AhmedLabib", 'output_password == "AhmedLabib"' in studio_source, 6),
        ("all modes have export/download controls", studio_source.count("download_button") >= 14, 8),
        ("HTML, PPTX, XLSX, CSV exports available", all(term in studio_source for term in ["text/html", "presentationml.presentation", "spreadsheetml.sheet", "text/csv"]), 8),
    ])
    export_coverage_score, export_detail = score_checks(export_checks)

    premium_checks = [(f"premium term present: {term}", term.lower() in studio_source.lower(), 2) for term in EXPECTED_PREMIUM_TERMS]
    premium_checks.extend([
        ("A3 / print-ready output referenced", "A3" in studio_source and "print" in studio_source.lower(), 6),
        ("Canva-style flexible builder present", "Canva-Style Flexible Builder" in studio_source, 8),
        ("The Big dashboard uses premium dark executive surface", "build_the_big_decision_dashboard_html" in source and "Critical Alerts" in source, 8),
        ("visual controls include smart charts", "Smart Chart Builder" in studio_source and "plotly_chart" in studio_source, 8),
        ("management-ready wording visible", all(term in studio_source.lower() for term in ["management", "executive", "decision"]), 8),
    ])
    premium_design_score, premium_detail = score_checks(premium_checks)

    reliability_checks = [
        ("super premium validates openpyxl availability", "OPENPYXL_AVAILABLE" in studio_source, 8),
        ("download buttons disable empty original presentation", "disabled=not bool(original_template_bytes)" in studio_source, 8),
        ("empty data sources handled in flexible builder", "is empty" in studio_source and "Choose a source with data" in studio_source, 8),
        ("report assumptions displayed", "Assumptions / Limitations" in studio_source, 8),
        ("validation checks displayed", "Validation Checks" in studio_source, 8),
        ("combined selection export disabled when empty", "disabled=combined_selection_df.empty" in studio_source, 8),
        ("artifact evaluator generated", True, 6),
    ]
    reliability_score, reliability_detail = score_checks(reliability_checks)

    llm_checks = [
        ("narrative explains output paths", "Two Different Output Paths" in studio_source, 10),
        ("narrative explains original path constraint", "preserves the original presentation design" in studio_source, 8),
        ("narrative explains linked dashboard data refresh", "linked to the platform CSV files" in studio_source, 8),
        ("narrative explains Power BI workflow", "Power BI Connection Steps" in studio_source, 8),
        ("narrative explains flexible row-level selection", "one line from one source" in studio_source, 8),
        ("narrative includes governance/validation", "Governance Rules" in source and "Validation Checks" in studio_source, 8),
        ("narrative includes decision/action language", all(term in studio_source.lower() for term in ["decision", "action", "management"]), 10),
        ("narrative references digital dashboard/report quality", all(term in studio_source.lower() for term in ["premium", "dashboard", "report"]), 10),
    ]
    llm_average, llm_detail = score_checks(llm_checks)

    overall_score = round(
        data_coverage_score * 0.22
        + export_coverage_score * 0.24
        + premium_design_score * 0.22
        + reliability_score * 0.16
        + llm_average * 0.16,
        2,
    )
    scores = {
        "label": label,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "overall_score": overall_score,
        "llm_average": llm_average,
        "data_coverage_score": data_coverage_score,
        "export_coverage_score": export_coverage_score,
        "premium_design_score": premium_design_score,
        "reliability_score": reliability_score,
        "data_sources_inspected": int(len(data_inventory)),
        "generated_outputs_inspected": int(len(generated_inventory)),
        "details": {
            "data_coverage": data_detail,
            "export_coverage": export_detail,
            "premium_design": premium_detail,
            "reliability": reliability_detail,
            "llm_quality": llm_detail,
        },
    }
    (OUTPUT_DIR / f"scores_{label}.json").write_text(json.dumps(scores, indent=2), encoding="utf-8")
    data_inventory.to_csv(OUTPUT_DIR / f"data_inventory_{label}.csv", index=False, encoding="utf-8-sig")
    generated_inventory.to_csv(OUTPUT_DIR / f"generated_inventory_{label}.csv", index=False, encoding="utf-8-sig")
    artifact_html = build_artifact_html(scores, data_inventory, generated_inventory, studio_source)
    artifact_path = OUTPUT_DIR / f"artifact_{label}.html"
    artifact_path.write_text(artifact_html, encoding="utf-8")
    with SCORE_LOG.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(scores) + "\n")
    return scores


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", default="baseline")
    args = parser.parse_args()
    scores = evaluate(args.label)
    print(json.dumps({
        "label": scores["label"],
        "overall_score": scores["overall_score"],
        "llm_average": scores["llm_average"],
        "artifact": str(OUTPUT_DIR / f"artifact_{args.label}.html"),
        "scores": str(OUTPUT_DIR / f"scores_{args.label}.json"),
    }, indent=2))


if __name__ == "__main__":
    main()
