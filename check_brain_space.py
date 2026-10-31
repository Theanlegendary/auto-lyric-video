import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

brain_parent = Path("C:/Users/DELL/.gemini/antigravity/brain")
curr_conv = "fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

for d in brain_parent.iterdir():
    if d.is_dir() and d.name != curr_conv:
        sz = sum(f.stat().st_size for f in d.rglob("*") if f.is_file()) / (1024 * 1024)
        print(f"Other conv {d.name}: {sz:.2f} MB")
