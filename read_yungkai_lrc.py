import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/28_yung_kai_blue")
lrc = (song_dir / "lyrics.lrc").read_text(encoding="utf-8")

lines = [line.strip() for line in lrc.splitlines() if line.strip() and not line.startswith("[re:") and not line.startswith("[ve:")]
for l in lines:
    print(l)
