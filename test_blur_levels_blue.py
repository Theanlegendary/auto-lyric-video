import os
import sys
import subprocess
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
raw_bg = os.path.join(base, "stock_anime_bgs", "17_anime_clear_blue_sky_clouds.png")
song_dir = os.path.join(base, "songs", "15_Akon_Lonely")

im = Image.open(raw_bg).convert("RGB")

# Option 1: Sharp with gentle 8% scrim
scrim_dark = Image.new("RGB", (1920, 1080), (10, 20, 40))
bg_sharp_scrim = Image.blend(im, scrim_dark, 0.08)
bg_sharp_scrim.save(os.path.join(song_dir, "test_bg_blue_sharp.png"))

# Option 2: Soft Dreamy Blur (radius=12) + 8% scrim
im_blur12 = im.filter(ImageFilter.GaussianBlur(radius=12))
bg_blur12 = Image.blend(im_blur12, scrim_dark, 0.08)
bg_blur12.save(os.path.join(song_dir, "test_bg_blue_blur12.png"))

# Option 3: Deep Velvety Blur (radius=22) + 8% scrim
im_blur22 = im.filter(ImageFilter.GaussianBlur(radius=22))
bg_blur22 = Image.blend(im_blur22, scrim_dark, 0.08)
bg_blur22.save(os.path.join(song_dir, "test_bg_blue_blur22.png"))

# Now render test frame on all 3
ass_test = os.path.join(base, "test_blue_sky_style.ass").replace("\\", "/").replace(":", "\\\\:")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

for bg_name, out_name in [("test_bg_blue_sharp.png", "compare_blue_sharp.png"),
                          ("test_bg_blue_blur12.png", "compare_blue_blur12.png"),
                          ("test_bg_blue_blur22.png", "compare_blue_blur22.png")]:
    bg_p = os.path.join(song_dir, bg_name)
    out_p = os.path.join(brain, out_name)
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "10", "-i", bg_p,
        "-vf", f"subtitles={ass_test}:fontsdir={fonts_escaped}",
        "-ss", "00:00:07", "-vframes", "1",
        out_p
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered: {out_name}")

print("All 3 blur level comparisons rendered!")
