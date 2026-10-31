import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
song_dir = os.path.join(base, "songs", "15_Akon_Lonely")
fonts_dir = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

# 1. White font ASS (with dark contrast outline + shadow)
ass_white = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Lyric,Patrick Hand,138,&H00FFFFFF,&H000000FF,&H00181020,&H70000000,1,0,0,0,95,115,2,0,1,2.5,2.0,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:10.00,Lyric,,0,0,0,,{{\\pos(960,490)}}LONELY, I'M MR. LONELY\\NI HAVE NOBODY FOR MY OWN
"""

# 2. Black font ASS (with soft white halo)
ass_black = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Lyric,Patrick Hand,138,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,0,0,0,0,95,115,1,0,1,1.8,0.8,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:10.00,Lyric,,0,0,0,,{{\\pos(960,490)}}LONELY, I'M MR. LONELY\\NI HAVE NOBODY FOR MY OWN
"""

# 3. Clean Modern DMSans White font ASS
ass_dmsans = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Lyric,DM Sans,125,&H00FFFFFF,&H000000FF,&H00181020,&H70000000,1,0,0,0,95,115,2,0,1,2.5,2.0,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:10.00,Lyric,,0,0,0,,{{\\pos(960,490)}}LONELY, I'M MR. LONELY\\NI HAVE NOBODY FOR MY OWN
"""

p_white = os.path.join(song_dir, "test_white.ass")
p_black = os.path.join(song_dir, "test_black.ass")
p_dmsans = os.path.join(song_dir, "test_dmsans.ass")

with open(p_white, "w", encoding="utf-8") as f: f.write(ass_white)
with open(p_black, "w", encoding="utf-8") as f: f.write(ass_black)
with open(p_dmsans, "w", encoding="utf-8") as f: f.write(ass_dmsans)

# Render frames
tests = [
    ("blur22_black", os.path.join(song_dir, "test_blur22.png"), p_black),
    ("blur22_white", os.path.join(song_dir, "test_blur22.png"), p_white),
    ("blur22_scrim_white", os.path.join(song_dir, "test_blur22_scrim.png"), p_white),
    ("blur22_scrim_dmsans", os.path.join(song_dir, "test_blur22_scrim.png"), p_dmsans),
]

for label, bg, ass_f in tests:
    out_img = os.path.join(brain, f"test_akon_{label}.png")
    ass_escaped = ass_f.replace("\\", "/").replace(":", "\\\\:")
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "1", "-i", bg,
        "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_dir}",
        "-vframes", "1",
        out_img
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered: {label}")
