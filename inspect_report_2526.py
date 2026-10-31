import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

report = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/final_verification_report.md")
lines = report.read_text(encoding="utf-8").splitlines()

for i, l in enumerate(lines):
    if "**25" in l or "**26" in l:
        print(f"{i+1}: {l}")
