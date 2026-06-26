from pathlib import Path
import re
from datetime import datetime

file = Path("dashboard.py")
text = file.read_text(encoding="utf-8")

backup = Path(f"dashboard_backup_parse_numeric_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py")
backup.write_text(text, encoding="utf-8")

new_function = r'''
def parse_numeric(value, default=0.0):
    """
    Safe numeric parser for dashboard calculations.
    Converts real numeric values to float.
    Returns default for business text such as Yes, No, Approved, Pending, N/A.
    """
    import re
    import pandas as pd

    if value is None:
        return default

    try:
        if pd.isna(value):
            return default
    except Exception:
        pass

    if isinstance(value, (int, float)):
        return float(value)

    text = str(value).strip()

    if not text:
        return default

    lowered = text.lower()

    non_numeric_values = {
        "yes", "no", "true", "false",
        "y", "n",
        "approved", "rejected", "pending",
        "open", "closed",
        "done", "not done",
        "n/a", "na", "none", "null",
        "-", "--"
    }

    if lowered in non_numeric_values:
        return default

    negative = False
    if text.startswith("(") and text.endswith(")"):
        negative = True
        text = text[1:-1]

    cleaned = re.sub(r"[^0-9.\-]", "", text)

    if cleaned in {"", "-", ".", "-.", ".-", "--"}:
        return default

    try:
        number = float(cleaned)
        return -number if negative else number
    except (ValueError, TypeError):
        return default

'''

pattern = r"def parse_numeric\(.*?\):\n(?:    .*\n|    \n)+"

match = re.search(pattern, text)

if not match:
    raise SystemExit("parse_numeric function was not found. Manual fix required.")

text = text[:match.start()] + new_function + text[match.end():]

file.write_text(text, encoding="utf-8")

print(f"Fixed parse_numeric successfully.")
print(f"Backup created: {backup}")
