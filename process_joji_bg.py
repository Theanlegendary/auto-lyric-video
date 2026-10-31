import sys
from pathlib import Path
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/27_Joji_Glimpse_of_Us")

img1_path = brain / "glimpse_of_us_wallpaper_wide_sky_1793325315330.jpg"
img2_path = brain / "glimpse_of_us_makoto_shinkai_wallpaper_1793325293989.jpg"

print("Image 1:", img1_path.exists())
if img1_path.exists():
    im1 = Image.open(img1_path)
    print("  Size:", im1.size)
    im1_1080 = im1.resize((1920, 1080), Image.Resampling.LANCZOS)
    im1_1080.save(song_dir / "glimpse_of_us_raw.png")
    
    # Create gentle bokeh master (radius 6 for ultra-crisp readable background)
    im1_blur = im1_1080.filter(ImageFilter.GaussianBlur(radius=6))
    im1_blur.save(song_dir / "glimpse_of_us_blurred_master.png")
    print("  Saved raw and blurred master for Joji.")

print("Image 2:", img2_path.exists())
if img2_path.exists():
    im2 = Image.open(img2_path)
    print("  Size:", im2.size)
