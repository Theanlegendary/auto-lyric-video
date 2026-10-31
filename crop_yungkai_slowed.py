import sys
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

frames = [
    "audit_yungkai_slowed_title.png",
    "audit_yungkai_slowed_verse1.png",
    "audit_yungkai_slowed_chorus.png"
]

for fname in frames:
    p = brain / fname
    if p.exists():
        im = Image.open(p)
        crop = im.crop((0, 200, 1920, 880))
        crop_path = brain / f"crop_{fname}"
        crop.save(crop_path)
        print(f"Saved crop: {crop_path.name}")
