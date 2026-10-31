import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")

for d in base.iterdir():
    if d.is_dir() and d.name != "videos":
        sz = sum(f.stat().st_size for f in d.rglob("*") if f.is_file()) / (1024 * 1024)
        if sz > 5:
            print(f"{d.name}: {sz:.2f} MB")
