import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/28_yung_kai_blue")
words = song_dir / "whisper_words.txt"
lines = words.read_text(encoding="utf-8").splitlines()

# Print segments
for l in lines:
    if l.startswith("[") and "->" in l:
        print(l)
