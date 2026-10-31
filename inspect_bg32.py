import sys, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
reg = json.loads((base / "bg_registry.json").read_text(encoding="utf-8"))
for item in reg:
    if item["id"] == "bg_32":
        print(item)
