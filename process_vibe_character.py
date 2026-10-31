import os
import sys
import subprocess
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
raw_jpg = os.path.join(brain, "solitary_desert_sunset_lonely_1793068061795.jpg")
stock_dir = os.path.join(base, "stock_anime_bgs")
song_dir = os.path.join(base, "songs", "15_Akon_Lonely")

# 1. Convert to 1920x1080 PNG
im = Image.open(raw_jpg).convert("RGB").resize((1920, 1080), Image.Resampling.LANCZOS)
sharp_png = os.path.join(stock_dir, "19_lonely_guy_desert_sunset_vibe.png")
im.save(sharp_png, "PNG")
print(f"Saved sharp artwork: {sharp_png}")

# 2. Prepare soft bokeh / blur version (radius=14) with subtle warm contrast scrim
im_blur = im.filter(ImageFilter.GaussianBlur(radius=14))
scrim = Image.new("RGB", (1920, 1080), (24, 12, 10))
bg_soft = Image.blend(im_blur, scrim, 0.08)
blurred_master = os.path.join(song_dir, "vibe_character_blurred_master.png")
bg_soft.save(blurred_master, "PNG")
print(f"Saved blurred master: {blurred_master}")

# 3. Render side-by-side comparison with Spotify 50/50 lyrics
ass_path = os.path.join(song_dir, "lyrics_spotify_rdr_orange.ass")
ass_escaped = ass_path.replace("\\", "/").replace(":", "\\\\:")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

# Render on Sharp background
out_sharp = os.path.join(brain, "vibe_concept_sharp_with_lyrics.png")
cmd1 = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", "5", "-i", sharp_png,
    "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
    "-ss", "00:00:15", "-vframes", "1",
    out_sharp
]
subprocess.run(cmd1, check=True)
print(f"Rendered: {out_sharp}")

# Render on Soft-Blurred background (Frosted Depth of Field)
out_soft = os.path.join(brain, "vibe_concept_softblur_with_lyrics.png")
cmd2 = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", "5", "-i", blurred_master,
    "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
    "-ss", "00:00:15", "-vframes", "1",
    out_soft
]
subprocess.run(cmd2, check=True)
print(f"Rendered: {out_soft}")

# Also render Title card on the new artwork
out_title = os.path.join(brain, "vibe_concept_title.png")
cmd3 = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", "5", "-i", sharp_png,
    "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
    "-ss", "00:00:05", "-vframes", "1",
    out_title
]
subprocess.run(cmd3, check=True)
print(f"Rendered: {out_title}")

print("All concept preview frames successfully generated!")
