import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/27_Joji_Glimpse_of_Us")
words_file = song_dir / "whisper_words.txt"

with open(words_file, "r", encoding="utf-8") as f:
    lines = [f.readline() for _ in range(35)]
    print("".join(lines))
