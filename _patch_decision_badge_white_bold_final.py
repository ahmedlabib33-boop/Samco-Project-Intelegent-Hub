from pathlib import Path
from datetime import datetime
import re

file = Path("dashboard.py")
text = file.read_text(encoding="utf-8", errors="replace")

backup = Path(f"dashboard_backup_decision_badge_white_bold_final_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py")
backup.write_text(text, encoding="utf-8")

original = text

# 1) Force the decision_status_badge foreground return value to pure white.
text = text.replace('return status, "#123F3D", "#50D5B7"', 'return status, "#123F3D", "#FFFFFF"')
text = text.replace('return status, "#4E3D12", "#D4A017"', 'return status, "#4E3D12", "#FFFFFF"')
text = text.replace('return status, "#4B1D22", "#F05D5E"', 'return status, "#4B1D22", "#FFFFFF"')
text = text.replace('return status, "#173B63", "#69A7D8"', 'return status, "#173B63", "#FFFFFF"')

# Also cover if previous patch already made them white.
text = text.replace('style=\'background:{badge_bg};color:{badge_fg}\'', 'style=\'background:{badge_bg};color:#FFFFFF !important;-webkit-text-fill-color:#FFFFFF !important;font-weight:900 !important;\'')
text = text.replace('style="background:{badge_bg};color:{badge_fg}"', 'style="background:{badge_bg};color:#FFFFFF !important;-webkit-text-fill-color:#FFFFFF !important;font-weight:900 !important;"')

# 2) Strengthen the CSS class itself, but only the decision badge text.
old_css = ".decision-badge{display:inline-block;border-radius:999px;padding:5px 9px;font-size:10px;font-weight:900;white-space:nowrap;max-width:118px;overflow:hidden;text-overflow:ellipsis}"
new_css = ".decision-badge{display:inline-block;border-radius:999px;padding:5px 9px;font-size:10px;font-weight:900!important;white-space:nowrap;max-width:118px;overflow:hidden;text-overflow:ellipsis;color:#FFFFFF!important;-webkit-text-fill-color:#FFFFFF!important;text-shadow:0 1px 1px rgba(0,0,0,.35)}"

text = text.replace(old_css, new_css)

# 3) If CSS was formatted differently, add a safe override inside the Decision Dashboard style block.
marker = "DECISION_BADGE_WHITE_BOLD_FINAL_OVERRIDE"
if marker not in text:
    inject = """
        /* DECISION_BADGE_WHITE_BOLD_FINAL_OVERRIDE */
        .decision-badge,
        .decision-badge *{
            color:#FFFFFF!important;
            -webkit-text-fill-color:#FFFFFF!important;
            font-weight:900!important;
            text-shadow:0 1px 1px rgba(0,0,0,.35);
        }
"""
    css_anchor = ".decision-delta{font-size:11px;font-weight:800}"
    text = text.replace(css_anchor, inject + "\n        " + css_anchor)

file.write_text(text, encoding="utf-8")

print("Backup created:", backup)
print("Patch applied:", text != original)
print("White badge declarations:", text.count("#FFFFFF"))
print("Final override exists:", "DECISION_BADGE_WHITE_BOLD_FINAL_OVERRIDE" in text)
