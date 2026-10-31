import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

raw_path = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6\desert_sunset_sky_1793067507315.jpg"
target_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\stock_anime_bgs\18_rdr_vegas_clear_orange_sky.png"

im = Image.open(raw_path).convert("RGB")
im_1080 = im.resize((1920, 1080), Image.Resampling.LANCZOS)
im_1080.save(target_path, "PNG")

print(f"Saved 18_rdr_vegas_clear_orange_sky.png (1920x1080) at {target_path}")
