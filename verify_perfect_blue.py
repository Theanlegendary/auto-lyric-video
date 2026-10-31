import sys
from pathlib import Path
from PIL import Image, ImageStat

sys.stdout.reconfigure(encoding='utf-8')

brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

for name in ["perfect_blue_7clouds_title.png", "perfect_blue_7clouds_chorus.png"]:
    p = brain / name
    img = Image.open(p)
    w, h = img.size
    crop = img.crop((w * 0.15, h * 0.35, w * 0.85, h * 0.65))
    crop_name = f"crop_{name}"
    crop.save(brain / crop_name)
    stat = ImageStat.Stat(crop)
    extrema = crop.getextrema()
    print(f"[{name}]")
    print(f"  Cropped focus: {crop_name}")
    print(f"  Max RGB (Text peak): {[e[1] for e in extrema[:3]]}")
    print(f"  Min RGB (Outline/Shadow floor): {[e[0] for e in extrema[:3]]}")
    print(f"  Mean background RGB: {[round(x, 1) for x in stat.mean[:3]]}")
