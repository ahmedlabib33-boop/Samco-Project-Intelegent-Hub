from pathlib import Path
from datetime import datetime
import re

file = Path("dashboard.py")
text = file.read_text(encoding="utf-8", errors="replace")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = Path(f"dashboard_backup_badge_text_white_only_{timestamp}.py")
backup.write_text(text, encoding="utf-8")

labels = [
    "Neutral",
    "Healthy",
    "Critical",
    "On Track",
    "Cost Watch"
]

def force_white_on_label_tag(match):
    tag = match.group(0)

    if "color:#ffffff" in tag.replace(" ", "").lower() or "color: #ffffff" in tag.lower():
        return tag

    if "style=" in tag.lower():
        tag = re.sub(
            r'style=(["\'])(.*?)\1',
            lambda m: f'style={m.group(1)}color:#ffffff !important; -webkit-text-fill-color:#ffffff !important; {m.group(2)}{m.group(1)}',
            tag,
            count=1,
            flags=re.IGNORECASE | re.DOTALL
        )
    else:
        tag = re.sub(
            r'^<(\w+)',
            r'<\1 style="color:#ffffff !important; -webkit-text-fill-color:#ffffff !important;"',
            tag,
            count=1
        )

    return tag

for label in labels:
    pattern = re.compile(
        rf'<(span|div|button|small|strong|b)\b[^>]*>\s*{re.escape(label)}\s*</\1>',
        re.IGNORECASE | re.DOTALL
    )
    text = pattern.sub(force_white_on_label_tag, text)

file.write_text(text, encoding="utf-8")

print("Applied: badge/status text font changed to white only.")
print(f"Backup created: {backup}")
