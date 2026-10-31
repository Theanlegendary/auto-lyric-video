import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

report = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/final_verification_report.md")
content = report.read_text(encoding="utf-8")

old_str = """<!-- slide -->
![Song 25: Sweater Weather (The Neighbourhood) — Living Color Clouds Title Hook (200pt)](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_25_color_clouds_title.png)
<!-- slide -->
![Song 25: Sweater Weather (The Neighbourhood) — Living Color Clouds Chorus (Max 2 Rows, Zero Clutter)](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_25_color_clouds_chorus.png)"""

new_str = """<!-- slide -->
![Song 25A: Sweater Weather (Normal 1.0x) — Living Color Clouds Title Hook (200pt)](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_25_color_clouds_title.png)
<!-- slide -->
![Song 25A: Sweater Weather (Normal 1.0x) — Living Color Clouds Chorus](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_25_color_clouds_chorus.png)
<!-- slide -->
![Song 25B: Sweater Weather (Slowed + Reverb Brand Master) — Title Hook (200pt)](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/crop_audit_sweater_slowed_full_title.png)
<!-- slide -->
![Song 25B: Sweater Weather (Slowed + Reverb Brand Master) — Chorus Couplet (Glowing White)](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/crop_audit_sweater_slowed_full_chorus.png)"""

content = content.replace("\r\n", "\n")
old_str = old_str.replace("\r\n", "\n")
new_str = new_str.replace("\r\n", "\n")

if old_str in content:
    content = content.replace(old_str, new_str)
    report.write_text(content, encoding="utf-8")
    print("Report carousel updated successfully.")
else:
    print("Warning: old_str not found in report!")
