from pathlib import Path
from datetime import datetime
import re

file = Path("dashboard.py")
text = file.read_text(encoding="utf-8", errors="replace")

backup = Path(f"dashboard_backup_decision_badge_text_white_final_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py")
backup.write_text(text, encoding="utf-8")

original = text

# This patch targets KPI status/badge/pill style blocks only.
# It does NOT change card text, card background, layout, borders, or dashboard values.

def make_badge_style_white(style: str) -> str:
    style_clean = style.strip()

    # Remove existing text color declarations inside the badge style only.
    style_clean = re.sub(r'color\s*:\s*[^;]+;?', '', style_clean, flags=re.IGNORECASE)
    style_clean = re.sub(r'-webkit-text-fill-color\s*:\s*[^;]+;?', '', style_clean, flags=re.IGNORECASE)

    # Add white font color only.
    return "color:#ffffff !important; -webkit-text-fill-color:#ffffff !important; " + style_clean


def is_small_status_badge(style: str, nearby: str = "") -> bool:
    s = style.lower().replace(" ", "")
    n = nearby.lower()

    has_background = "background:" in s or "background-color:" in s
    has_rounding = "border-radius" in s

    # Avoid changing the full KPI card container.
    looks_like_big_card = (
        "box-shadow" in s
        or "min-height" in s
        or "height:160" in s
        or "height:170" in s
        or "border-left" in s
        or "grid-template" in s
        or "linear-gradient" in s
    )

    # Small status pills normally have small font/padding/rounded badge behavior.
    looks_like_small_pill = (
        "font-size:0.6" in s
        or "font-size:0.65" in s
        or "font-size:0.7" in s
        or "font-size:0.75" in s
        or "font-size:11" in s
        or "font-size:12" in s
        or "padding:0.2" in s
        or "padding:0.25" in s
        or "padding:0.3" in s
        or "padding:0.35" in s
        or "padding:0.4" in s
        or "999px" in s
        or "9999px" in s
        or "float:right" in s
        or "position:absolute" in s
        or "status" in n
        or "badge" in n
        or "pill" in n
        or "neutral" in n
        or "healthy" in n
        or "critical" in n
        or "on track" in n
        or "cost watch" in n
    )

    return has_background and has_rounding and looks_like_small_pill and not looks_like_big_card


# Patch normal HTML style="..."
def patch_normal_style(match):
    quote = match.group(1)
    style = match.group(2)
    start = max(0, match.start() - 250)
    end = min(len(text), match.end() + 250)
    nearby = text[start:end]

    if is_small_status_badge(style, nearby):
        style = make_badge_style_white(style)

    return f'style={quote}{style}{quote}'


text = re.sub(
    r'style=(["\'])(.*?)\1',
    patch_normal_style,
    text,
    flags=re.IGNORECASE | re.DOTALL
)


# Patch escaped HTML style=\"...\" if the app uses escaped strings.
def patch_escaped_style(match):
    quote = match.group(1)
    style = match.group(2)
    start = max(0, match.start() - 250)
    end = min(len(text), match.end() + 250)
    nearby = text[start:end]

    if is_small_status_badge(style, nearby):
        style = make_badge_style_white(style)

    return f'style=\\{quote}{style}\\{quote}'


text = re.sub(
    r'style=\\(["\'])(.*?)\\\1',
    patch_escaped_style,
    text,
    flags=re.IGNORECASE | re.DOTALL
)


# Final targeted replacement for known status labels when they are directly rendered in a tag.
labels = ["Neutral", "Healthy", "Critical", "On Track", "Cost Watch"]

for label in labels:
    pattern = re.compile(
        rf'(<(?:span|div|small|b|strong)\b[^>]*style=(["\'])(.*?)(\2)[^>]*>\s*)({re.escape(label)})(\s*</(?:span|div|small|b|strong)>)',
        flags=re.IGNORECASE | re.DOTALL
    )

    def patch_label_tag(m):
        opening = m.group(1)
        label_text = m.group(5)
        closing = m.group(6)

        opening = re.sub(
            r'style=(["\'])(.*?)\1',
            lambda sm: f'style={sm.group(1)}{make_badge_style_white(sm.group(2))}{sm.group(1)}',
            opening,
            count=1,
            flags=re.IGNORECASE | re.DOTALL
        )

        return opening + label_text + closing

    text = pattern.sub(patch_label_tag, text)


file.write_text(text, encoding="utf-8")

changed = text != original
white_count = text.count("color:#ffffff !important")

print("Backup created:", backup)
print("Patch applied:", changed)
print("White badge color declarations found:", white_count)

if not changed:
    print("No matching badge template was found. Run the Select-String diagnostic and send the output.")
