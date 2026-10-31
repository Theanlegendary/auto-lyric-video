import shutil
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
bg_dir = os.path.join(base, "stock_anime_bgs")
reg_path = os.path.join(base, "bg_registry.json")

src_bg = os.path.join(bg_dir, "14_anime_clear_pink_aesthetic_twilight_sky.png")
dst_bg = os.path.join(bg_dir, "16_anime_vibe_pink_twilight_sky.png")

if not os.path.exists(dst_bg):
    shutil.copy(src_bg, dst_bg)
    print("Copied to 16_anime_vibe_pink_twilight_sky.png")

with open(reg_path, "r", encoding="utf-8") as f:
    reg = json.load(f)

# Check if bg_16 already exists
existing = [x for x in reg if x['id'] == 'bg_16']
if not existing:
    reg.append({
        "id": "bg_16",
        "file": "16_anime_vibe_pink_twilight_sky.png",
        "name": "Aesthetic Vibe Sunset Sky & Pine Ridge (Deep Blur)",
        "theme": "white",
        "tags": ["pink", "sunset", "vibe", "aesthetic", "lofi", "amber", "pine", "sky"],
        "assigned_to": "15_Akon_Lonely"
    })
    with open(reg_path, "w", encoding="utf-8") as f:
        json.dump(reg, f, indent=2)
    print("Added bg_16 to bg_registry.json")
else:
    print("bg_16 already in registry")

print(f"Total backgrounds registered: {len(reg)}")
