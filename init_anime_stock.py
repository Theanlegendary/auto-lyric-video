import os
import shutil

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
stock_dir = f"{base}/stock_anime_bgs"
os.makedirs(stock_dir, exist_ok=True)

# Copy existing stock anime backgrounds
shutil.copy(f"{base}/light_clouds_sharp_1080.png", f"{stock_dir}/01_makoto_shinkai_clouds.png")
shutil.copy(f"{base}/dark_twilight_sharp_1080.png", f"{stock_dir}/02_lofi_twilight_starry_night.png")

print("Created stock anime folder and initialized 01 and 02!")
