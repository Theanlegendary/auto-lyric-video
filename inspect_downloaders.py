import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
for py in ["download_candidates.py", "download_akon.py", "process_song26.py"]:
    p = base / py
    if p.exists():
        print(f"--- {py} ---")
        print(p.read_text(encoding="utf-8")[:600])
