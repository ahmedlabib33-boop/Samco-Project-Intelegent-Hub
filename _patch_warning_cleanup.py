from pathlib import Path
from datetime import datetime
import re

file = Path("dashboard.py")
text = file.read_text(encoding="utf-8", errors="replace")

backup = Path(f"dashboard_backup_warning_cleanup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py")
backup.write_text(text, encoding="utf-8")

# Fix Streamlit deprecation:
# use_container_width=True  -> width="stretch"
# use_container_width=False -> width="content"
text = text.replace("use_container_width=True", 'width="stretch"')
text = text.replace("use_container_width=False", 'width="content"')

# Fix pandas date warning on planned_start / planned_finish if the old lines exist
old_start = 'valid_start = pd.to_datetime(projects_df.get("planned_start", pd.Series(dtype=object)), errors="coerce")'
new_start = 'valid_start = pd.to_datetime(projects_df.get("planned_start", pd.Series(dtype=object)), errors="coerce", dayfirst=True)'

old_finish = 'valid_finish = pd.to_datetime(projects_df.get("planned_finish", pd.Series(dtype=object)), errors="coerce")'
new_finish = 'valid_finish = pd.to_datetime(projects_df.get("planned_finish", pd.Series(dtype=object)), errors="coerce", dayfirst=True)'

text = text.replace(old_start, new_start)
text = text.replace(old_finish, new_finish)

file.write_text(text, encoding="utf-8")

print("Warnings cleanup patch applied.")
print(f"Backup created: {backup}")
