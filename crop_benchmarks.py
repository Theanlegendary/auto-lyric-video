import sys
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

for name in ["benchmark_7clouds_dandelions_frame.png", "benchmark_7clouds_die_with_a_smile_frame.png"]:
    img = Image.open(brain / name)
    w, h = img.size
    # crop text area in 720p: center is (300, 250, 980, 500)
    crop = img.crop((w * 0.15, h * 0.35, w * 0.85, h * 0.65))
    crop_name = f"crop_{name}"
    crop.save(brain / crop_name)
    print(f"Saved crop: {crop_name}")
