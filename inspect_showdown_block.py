import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html")
lines = player_path.read_text(encoding="utf-8").splitlines()

for i, l in enumerate(lines):
    if "Cathedral Space" in l or "Sweater Weather Pair" in l:
        for j in range(max(0, i-10), min(len(lines), i+35)):
            print(f"{j+1}: {lines[j]}")
        break
