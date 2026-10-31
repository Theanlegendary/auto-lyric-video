import os
import sys
from PIL import Image, ImageFilter, ImageEnhance
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
vibe_sky_path = os.path.join(base, "stock_anime_bgs", "14_anime_clear_pink_aesthetic_twilight_sky.png")

img = Image.open(vibe_sky_path).convert("RGB")
img = img.resize((1920, 1080), Image.Resampling.LANCZOS)

# Test 3 blur radiuses: 16, 22, 28
blur16 = img.filter(ImageFilter.GaussianBlur(radius=16))
blur22 = img.filter(ImageFilter.GaussianBlur(radius=22))
blur28 = img.filter(ImageFilter.GaussianBlur(radius=28))

# Also test atmospheric scrim (slight darkening/vignette for white text pop)
# 15% dark scrim
scrim = Image.new("RGB", (1920, 1080), (20, 15, 30))
blur22_scrim = Image.blend(blur22, scrim, 0.18)

out_dir = os.path.join(base, "songs", "15_Akon_Lonely")
os.makedirs(out_dir, exist_ok=True)

blur16.save(os.path.join(out_dir, "test_blur16.png"))
blur22.save(os.path.join(out_dir, "test_blur22.png"))
blur28.save(os.path.join(out_dir, "test_blur28.png"))
blur22_scrim.save(os.path.join(out_dir, "test_blur22_scrim.png"))

print("Saved test blur backgrounds.")
