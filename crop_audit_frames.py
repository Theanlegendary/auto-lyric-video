import sys
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

frames = [
    "audit_sweater_slowed_full_title.png",
    "audit_sweater_slowed_full_chorus.png",
    "audit_sweater_slowed_full_verse1.png"
]

for fname in frames:
    p = brain / fname
    if p.exists():
        im = Image.open(p)
        # Crop center 1920x600 (y from 240 to 840)
        crop = im.crop((0, 200, 1920, 880))
        crop_path = brain / f"crop_{fname}"
        crop.save(crop_path)
        print(f"Saved cropped preview: {crop_path.name} ({crop_path.stat().st_size} bytes)")
