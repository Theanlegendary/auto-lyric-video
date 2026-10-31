import os
import shutil
from PIL import Image

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
stock_dir = f"{base}/stock_anime_bgs"
brain_dir = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
os.makedirs(stock_dir, exist_ok=True)

raw_sources = [
    ("01_makoto_shinkai_clouds.png", f"{base}/light_clouds_sharp_1080.png"),
    ("02_lofi_twilight_starry_night.png", f"{base}/dark_twilight_sharp_1080.png"),
    ("03_anime_rooftop_sunset_skyline.png", f"{brain_dir}/anime_lofi_sunset_skyline_1792747901996.jpg"),
    ("04_lofi_rainy_window_city_night.png", f"{brain_dir}/lofi_rainy_window_anime_bg_1792747905689.jpg")
]

for name, src in raw_sources:
    img = Image.open(src)
    w, h = img.size
    target_w, target_h = 1920, 1080
    aspect_src = w / h
    aspect_target = target_w / target_h
    if aspect_src > aspect_target:
        new_w = int(h * aspect_target)
        offset = (w - new_w) // 2
        box = (offset, 0, offset + new_w, h)
    else:
        new_h = int(w / aspect_target)
        offset = (h - new_h) // 2
        box = (0, offset, w, offset + new_h)
    cropped = img.crop(box).resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    dest_path = f"{stock_dir}/{name}"
    cropped.save(dest_path, "PNG")
    # Also copy to brain directory for artifact embedding
    cropped.save(f"{brain_dir}/{name}", "PNG")
    print(f"Processed & saved: {name}")

print("Stock anime library is 100% prepared!")
