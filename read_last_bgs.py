import sys, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

bg_reg = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/bg_registry.json")
data = json.loads(bg_reg.read_text(encoding="utf-8"))

for item in data[-10:]:
    print(item)
