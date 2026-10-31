import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/27_Adele_Skyfall")
for f in song_dir.glob("*"):
    print(f"{f.name} ({f.stat().st_size} bytes)")
