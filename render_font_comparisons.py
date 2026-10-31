import os
import sys
import subprocess
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
bg_path = os.path.join(base, "songs", "15_Akon_Lonely", "vibe_sky_blurred_master.png")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

candidates = [
    ("Sniglet", "Sniglet", "ExtraBold", 175),
    ("Chewy", "Chewy", "Regular", 185),
    ("BalsamiqSans", "Balsamiq Sans", "Bold", 170),
    ("Gaegu", "Gaegu", "Bold", 190),
    ("LilitaOne", "Lilita One", "Regular", 170),
    ("ShortStack", "Short Stack", "Regular", 175),
    ("PatrickHand", "Patrick Hand", "Regular", 180),
]

# We will generate a test frame for each font with pure white, no harsh outline, just a clean soft shadow
for font_id, font_name, weight, fsize in candidates:
    ass_text = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: LyricClean,{font_name},{fsize},&H00FFFFFF,&H000000FF,&H00150F1E,&H55000000,1,0,0,0,100,100,1,0,1,1.5,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:05.00,LyricClean,,0,0,0,,{{\\pos(960,500)}}LONELY\\NI'M MR. LONELY
"""
    ass_file = os.path.join(base, f"test_clean_{font_id}.ass")
    with open(ass_file, "w", encoding="utf-8") as f:
        f.write(ass_text)
    
    ass_escaped = ass_file.replace("\\", "/").replace(":", "\\\\:")
    out_img = os.path.join(brain, f"compare_font_{font_id}.png")
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "1", "-i", bg_path,
        "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
        "-frames:v", "1", out_img
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')
    if res.returncode == 0:
        print(f"Rendered compare_font_{font_id}.png")
    else:
        print(f"Failed {font_id}: {res.stderr[-200:]}")

print("All candidate frames rendered!")
