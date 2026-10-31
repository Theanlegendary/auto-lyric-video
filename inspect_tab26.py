import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html")
lines = player.read_text(encoding="utf-8").splitlines()

for i, l in enumerate(lines):
    if "26. Another Love" in l:
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f"{j+1}: {lines[j]}")
        break
