import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
for p in base.glob("*"):
    if p.is_dir():
        print(p.name)
