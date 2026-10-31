import subprocess
import os
import sys
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
vibe_sky_path = os.path.join(base, "stock_anime_bgs", "14_anime_clear_pink_aesthetic_twilight_sky.png")

# Prepare deep blur background (radius=24)
img = Image.open(vibe_sky_path).convert("RGB").resize((1920, 1080), Image.Resampling.LANCZOS)
blurred = img.filter(ImageFilter.GaussianBlur(radius=24))

# Subtle 12% darkening scrim so white text pops effortlessly with soft glow
scrim = Image.new("RGB", (1920, 1080), (18, 12, 24))
bg_final = Image.blend(blurred, scrim, 0.12)

song_dir = os.path.join(base, "songs", "15_Akon_Lonely")
bg_path = os.path.join(song_dir, "vibe_sky_blurred_master.png")
bg_final.save(bg_path, "PNG")

fonts_dir = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

def make_ass(font_name, font_size, outline, shadow):
    return f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,{font_name},160,&H00FFFFFF,&H000000FF,&H00181020,&H70000000,1,0,0,0,95,115,3,0,1,2.8,2.2,5,50,50,50,1
Style: Lyric,{font_name},{font_size},&H00FFFFFF,&H000000FF,&H00181020,&H70000000,1,0,0,0,95,115,2,0,1,{outline},{shadow},5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:05.00,TitleCard,,0,0,0,,{{\\pos(960,470)}}LONELY\\N{{\\fs75\\fsp4}}Akon
Dialogue: 0,0:00:05.00,0:00:10.00,Lyric,,0,0,0,,{{\\pos(960,490)}}LONELY, I'M MR. LONELY\\NI HAVE NOBODY FOR MY OWN
"""

fonts = [
    ("Comfortaa", "Comfortaa", 120, 2.4, 1.8),
    ("DMSans", "DM Sans", 125, 2.5, 2.0),
    ("PatrickHand", "Patrick Hand", 138, 2.4, 1.8),
]

for label, fname, fsize, outl, shad in fonts:
    ass_content = make_ass(fname, fsize, outl, shad)
    ass_path = os.path.join(song_dir, f"test_{label}.ass")
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_content)
    
    ass_escaped = ass_path.replace("\\", "/").replace(":", "\\\\:")
    # Render Title frame (00:02) and Chorus frame (00:07)
    for ss, frame_label in [("00:00:02", "title"), ("00:00:07", "chorus")]:
        out_f = os.path.join(brain, f"preview_akon_{label}_{frame_label}.png")
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-t", "10", "-i", bg_path,
            "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_dir}",
            "-ss", ss, "-vframes", "1",
            out_f
        ]
        subprocess.run(cmd, check=True)
        print(f"Rendered: {label}_{frame_label}")
