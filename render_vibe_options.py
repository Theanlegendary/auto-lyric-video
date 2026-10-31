import os
import subprocess
from PIL import Image, ImageFilter

brain_dir = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
base_dir = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
test_dir = f"{base_dir}/test"

# Paths to generated images
light_img_raw = f"{brain_dir}/pastel_anime_clouds_lyric_bg_1792744825684.jpg"
dark_img_raw = f"{brain_dir}/lofi_twilight_lyric_bg_clean_1792744849177.jpg"

def process_bg(src, name_prefix):
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
    
    sharp_path = f"{base_dir}/{name_prefix}_sharp_1080.png"
    blur_path = f"{base_dir}/{name_prefix}_blur_1080.png"
    
    cropped.save(sharp_path, "PNG")
    # Soft, gentle blur (radius 8 - preserves sky beauty)
    blurred = cropped.filter(ImageFilter.GaussianBlur(radius=8))
    blurred.save(blur_path, "PNG")
    return sharp_path, blur_path

light_sharp, light_blur = process_bg(light_img_raw, "light_clouds")
dark_sharp, dark_blur = process_bg(dark_img_raw, "dark_twilight")
print("Processed light and dark background images.")

# Render test frames for comparison
ass_black = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/lyrics_black_text.ass"
ass_white = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/lyrics_white_text.ass"
fonts_dir = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

renders = [
    # Light option with black lyrics
    (light_sharp, ass_black, f"{test_dir}/vibe_light_title_sharp.png", "00:00:02"),
    (light_blur, ass_black, f"{test_dir}/vibe_light_verse1_blur.png", "00:00:07"),
    (light_blur, ass_black, f"{test_dir}/vibe_light_chorus_blur.png", "00:00:33"),
    # Dark option with white lyrics
    (dark_sharp, ass_white, f"{test_dir}/vibe_dark_title_sharp.png", "00:00:02"),
    (dark_blur, ass_white, f"{test_dir}/vibe_dark_verse1_blur.png", "00:00:07"),
    (dark_blur, ass_white, f"{test_dir}/vibe_dark_chorus_blur.png", "00:00:33"),
]

for bg, ass_f, out_f, ss in renders:
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "40", "-i", bg,
        "-vf", f"subtitles={ass_f}:fontsdir={fonts_dir}",
        "-ss", ss, "-vframes", "1",
        out_f
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered: {os.path.basename(out_f)}")

import shutil
for f in ["vibe_light_verse1_blur.png", "vibe_light_chorus_blur.png", "vibe_dark_verse1_blur.png", "vibe_dark_chorus_blur.png"]:
    shutil.copy(f"{test_dir}/{f}", f"{brain_dir}/{f}")
print("Copied frames to artifact directory!")
