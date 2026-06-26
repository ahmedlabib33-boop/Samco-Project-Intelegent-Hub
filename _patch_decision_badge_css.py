from pathlib import Path
from datetime import datetime
import re
import sys

file = Path("dashboard.py")
text = file.read_text(encoding="utf-8", errors="replace")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = Path(f"dashboard_backup_decision_badge_css_{timestamp}.py")
backup.write_text(text, encoding="utf-8")

marker = "DECISION_DASHBOARD_BADGE_TEXT_CSS_START"

if marker in text:
    print("Patch already exists. No change applied.")
    print(f"Backup created: {backup}")
    sys.exit(0)

css_block = '''st.markdown("""
<style>
/* DECISION_DASHBOARD_BADGE_TEXT_CSS_START */
/* Decision Making Dashboard: make dark KPI badge/pill text readable */
.status-badge,
.kpi-badge,
.kpi-status,
.status-pill,
.badge,
.pill,
[class*="status-badge"],
[class*="kpi-badge"],
[class*="kpi-status"],
[class*="status-pill"] {
    color: #ffffff !important;
    font-weight: 800 !important;
}

.status-badge *,
.kpi-badge *,
.kpi-status *,
.status-pill *,
.badge *,
.pill *,
[class*="status-badge"] *,
[class*="kpi-badge"] *,
[class*="kpi-status"] *,
[class*="status-pill"] * {
    color: #ffffff !important;
    font-weight: 800 !important;
}
/* DECISION_DASHBOARD_BADGE_TEXT_CSS_END */
</style>
""", unsafe_allow_html=True)
'''

lines = text.splitlines(True)

target_index = None
for i, line in enumerate(lines):
    if "EXECUTIVE KPI CARDS" in line:
        target_index = i
        break

if target_index is None:
    print("Safe insertion point not found.")
    print("Backup created but dashboard.py was not modified.")
    print(f"Backup: {backup}")
    sys.exit(1)

indent = re.match(r"\s*", lines[target_index]).group(0)

indented_css = ""
for line in css_block.splitlines(True):
    if line.strip():
        indented_css += indent + line
    else:
        indented_css += line

lines.insert(target_index, "\n" + indented_css + "\n")

file.write_text("".join(lines), encoding="utf-8")

print("Applied Decision Making Dashboard badge text CSS fix.")
print(f"Backup created: {backup}")
