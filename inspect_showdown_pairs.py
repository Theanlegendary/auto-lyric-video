import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html")
lines = player.read_text(encoding="utf-8").splitlines()

for i, l in enumerate(lines):
    if "PSYCHOLOGICAL BRAND SHOWDOWN" in l or "The Psychology of Slowed" in l:
        for j in range(i, min(len(lines), i+45)):
            print(f"{j+1}: {lines[j]}")
        break
