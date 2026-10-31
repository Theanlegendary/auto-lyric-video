import sys
from PIL import Image, ImageFilter
import json
import os
import shutil

sys.stdout.reconfigure(encoding='utf-8')

raw_img_path = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6\sia_chandelier_wallpaper_1793326932606.jpg"
song_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\29_Sia_Chandelier"
stock_bg_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\stock_anime_bgs"
registry_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\stock_anime_bgs\bg_registry.json"

if not os.path.exists(raw_img_path):
    print(f"Error: {raw_img_path} does not exist!")
    sys.exit(1)

# Open image
img = Image.open(raw_img_path).convert('RGB')
print(f"Original size: {img.size}")

# Resize to standard 1920x1080
img_1080 = img.resize((1920, 1080), Image.Resampling.LANCZOS)
raw_out_path = os.path.join(song_dir, "chandelier_raw.png")
img_1080.save(raw_out_path, format="PNG")
print(f"Saved raw resized: {raw_out_path}")

# Apply gentle atmospheric blur (radius 6) for dreamlike depth and maximum lyric readability
blurred_img = img_1080.filter(ImageFilter.GaussianBlur(radius=6))
blurred_out_path = os.path.join(song_dir, "chandelier_blurred_master.png")
blurred_img.save(blurred_out_path, format="PNG")
print(f"Saved blurred master: {blurred_out_path}")

# Copy to stock_anime_bgs as 35_sia_chandelier_celestial_prism.png
stock_dest = os.path.join(stock_bg_dir, "35_sia_chandelier_celestial_prism.png")
shutil.copyfile(blurred_out_path, stock_dest)
print(f"Copied to stock_anime_bgs: {stock_dest}")

# Update bg_registry.json
if os.path.exists(registry_path):
    with open(registry_path, "r", encoding="utf-8") as f:
        registry = json.load(f)
    
    registry["bg_35"] = {
        "filename": "35_sia_chandelier_celestial_prism.png",
        "title": "Sia Chandelier Radiant Celestial Prism Bokeh & Penthouse Night Sky",
        "mood": "Euphoric yet melancholy, cinematic golden prism starlight rays, deep sapphire indigo twilight sky",
        "recommended_for": ["Sia - Chandelier", "anthemic pop", "party heartbreak", "night skyline"]
    }
    
    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    print("Updated bg_registry.json successfully with bg_35.")
