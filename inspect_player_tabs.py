import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html")
with open(player_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's search for tab25 or sweater in player.html
idx = text.find("Sweater Weather")
while idx != -1:
    start = max(0, idx - 150)
    end = min(len(text), idx + 250)
    print("--- MATCH AT", idx, "---")
    print(text[start:end])
    idx = text.find("Sweater Weather", idx + 1)
