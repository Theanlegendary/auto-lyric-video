import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

song_dir = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/15_Akon_Lonely"
lrc_path = os.path.join(song_dir, "lrclib_synced.lrc")

with open(lrc_path, "r", encoding="utf-8") as f:
    text = f.read()

print(f"Total lines in LRC: {len(text.splitlines())}")
for idx, l in enumerate(text.splitlines()):
    print(f"{idx+1:02d}: {l}")
