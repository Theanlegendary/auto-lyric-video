import sys, glob
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

for f in ["tracklist.txt", "songs.txt", "playlist.txt", "queue.txt", "manifest.json", "bg_registry.json"]:
    p = Path(f"C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/{f}")
    if p.exists():
        print(f"Found {f}:")
        print(p.read_text(encoding="utf-8")[:1000])
        print("="*40)
