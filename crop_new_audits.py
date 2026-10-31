import sys
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

frames = [
    "audit_joji_normal_title.png",
    "audit_joji_normal_chorus.png",
    "audit_joji_slowed_title.png",
    "audit_joji_slowed_chorus.png",
    "audit_yungkai_normal_title.png",
    "audit_yungkai_normal_chorus.png",
]

for fname in frames:
    p = brain / fname
    if p.exists():
        im = Image.open(p)
        # Crop center 1920x680 (y from 200 to 880)
        crop = im.crop((0, 200, 1920, 880))
        crop_path = brain / f"crop_{fname}"
        crop.save(crop_path)
        print(f"Saved crop: {crop_path.name}")
