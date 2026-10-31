import os
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
bg_path = os.path.join(base, "songs", "15_Akon_Lonely", "vibe_sky_blurred_master.png")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

more_candidates = [
    ("DynaPuff", "DynaPuff", 190),
    ("Pangolin", "Pangolin", 195),
    ("Itim", "Itim", 195),
]

for font_id, font_name, fsize in more_candidates:
    ass_text = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: CloudNineStyle,{font_name},{fsize},&H00FFFFFF,&H000000FF,&H00000000,&H40000000,1,0,0,0,100,100,2,0,1,0.5,2.0,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:05.00,CloudNineStyle,,0,0,0,,{{\\pos(960,500)}}CLOUD\\NNINE
"""
    ass_file = os.path.join(base, f"test_cloudnine_{font_id}.ass")
    with open(ass_file, "w", encoding="utf-8") as f:
        f.write(ass_text)
    
    ass_escaped = ass_file.replace("\\", "/").replace(":", "\\\\:")
    out_img = os.path.join(brain, f"cloudnine_match_{font_id}.png")
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "1", "-i", bg_path,
        "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
        "-frames:v", "1", out_img
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"Rendered cloudnine_match_{font_id}.png")
