from pathlib import Path
from datetime import datetime

file = Path("dashboard.py")
text = file.read_text(encoding="utf-8", errors="replace")

backup = Path(f"dashboard_backup_decision_badge_text_white_exact_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py")
backup.write_text(text, encoding="utf-8")

original = text

# Decision Making Dashboard badge text only.
# Keep badge background colors unchanged.
# Change only the foreground/text color returned by decision_status_badge() to white.
text = text.replace('return status, "#123F3D", "#50D5B7"', 'return status, "#123F3D", "#FFFFFF"')
text = text.replace('return status, "#4E3D12", "#D4A017"', 'return status, "#4E3D12", "#FFFFFF"')
text = text.replace('return status, "#4B1D22", "#F05D5E"', 'return status, "#4B1D22", "#FFFFFF"')
text = text.replace('return status, "#173B63", "#69A7D8"', 'return status, "#173B63", "#FFFFFF"')

file.write_text(text, encoding="utf-8")

print("Backup created:", backup)
print("Patch applied:", text != original)
print("White text returns:", text.count('"#FFFFFF"'))
