from pathlib import Path
from datetime import datetime
import re

file = Path("dashboard.py")
text = file.read_text(encoding="utf-8", errors="replace")

backup = Path(f"dashboard_backup_pylance_nat_return_type_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py")
backup.write_text(text, encoding="utf-8")

original = text

# Fix Pylance reportReturnType where functions return pd.NaT but are annotated as tuple[pd.Timestamp, pd.Timestamp].
# This is type-hint cleanup only. It does not change runtime logic.
text = text.replace(
    "-> tuple[pd.Timestamp, pd.Timestamp]:",
    "-> tuple[object, object]:"
)

text = text.replace(
    "-> Tuple[pd.Timestamp, pd.Timestamp]:",
    "-> tuple[object, object]:"
)

file.write_text(text, encoding="utf-8")

print("Backup created:", backup)
print("Patch applied:", text != original)
print("Remaining exact Timestamp tuple annotations:", text.count("tuple[pd.Timestamp, pd.Timestamp]"))
