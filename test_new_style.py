import os
import subprocess
from PIL import Image, ImageFilter, ImageEnhance

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
new_bgs = f"{base}/new_bgs"
test_dir = f"{base}/test"

# 1. Generate gentle blur variants (radius=10)
bgs = ["bg_pink_sunset_island.jpg", "bg_mountain_dusk.jpg"]

for b in bgs:
    src = os.path.join(new_bgs, b)
    img = Image.open(src)
    # Gentle subtle blur (radius 10 instead of 32!)
    gentle_blur = img.filter(ImageFilter.GaussianBlur(radius=10))
    # Subtle 5% contrast boost to keep it vivid, no dark dimming
    gentle_blur = ImageEnhance.Contrast(gentle_blur).enhance(1.05)
    out_blur = os.path.join(new_bgs, f"subtle_blur_{b}")
    gentle_blur.save(out_blur, "JPEG", quality=95)
    print(f"Created subtle blur for {b}")

# 2. Create updated ASS subtitle file with BIGGER lyric font size (145 instead of 120)
ass_content = """[Script Info]
Title: That Should Be Me - Bigger Lyrics
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,Patrick Hand,185,&H002A202A,&H000000FF,&H002A202A,&H60000000,1,0,0,0,95,115,3,0,1,1.2,1.2,5,50,50,50,1
Style: Lyric,Patrick Hand,148,&H002A202A,&H000000FF,&H002A202A,&H60000000,0,0,0,0,95,115,1,0,1,0.8,0.8,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.50,0:00:04.50,TitleCard,,0,0,0,,{\\pos(960,470)\\fad(500,400)}THAT SHOULD BE ME\\N{\\fs85\\fsp4}Justin Bieber
Dialogue: 0,0:00:05.88,0:00:10.83,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}EVERYBODY'S LAUGHIN'\\NIN MY MIND
Dialogue: 0,0:00:12.33,0:00:17.73,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}RUMOURS SPREADIN' 'BOUT\\NTHIS OTHER GUY
Dialogue: 0,0:00:32.41,0:00:35.24,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}THAT SHOULD BE ME\\NHOLDIN' YOUR HAND
"""

ass_path = f"{base}/lyrics_bigger.ass"
with open(ass_path, "w", encoding="utf-8") as f:
    f.write(ass_content)

print("Saved lyrics_bigger.ass (Fontsize: 148, up from 120)")

# 3. Render test frames for comparison
ass_esc = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/lyrics_bigger.ass"
fonts_esc = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

tests = [
    # Background 1: Pink sunset island (original sharp)
    (f"{new_bgs}/bg_pink_sunset_island.jpg", f"{test_dir}/test_pink_sharp_title.png", "00:00:02"),
    # Background 1: Pink sunset island (subtle blur with bigger lyrics)
    (f"{new_bgs}/subtle_blur_bg_pink_sunset_island.jpg", f"{test_dir}/test_pink_subtle_verse1.png", "00:00:07"),
    (f"{new_bgs}/subtle_blur_bg_pink_sunset_island.jpg", f"{test_dir}/test_pink_subtle_chorus.png", "00:00:33"),
    # Background 2: Mountain dusk (subtle blur with bigger lyrics)
    (f"{new_bgs}/subtle_blur_bg_mountain_dusk.jpg", f"{test_dir}/test_mountain_subtle_verse1.png", "00:00:07")
]

for bg, out_img, ss in tests:
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "40", "-i", bg,
        "-vf", f"subtitles={ass_esc}:fontsdir={fonts_esc}",
        "-ss", ss, "-vframes", "1",
        out_img
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered: {os.path.basename(out_img)}")
