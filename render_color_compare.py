import os
import sys
import subprocess
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
bg_path = os.path.join(base, "stock_anime_bgs", "17_anime_clear_blue_sky_clouds.png")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

# Compare White Poppins Black Italic vs Dark Poppins Black Italic
ass_content = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: WhiteStyle,Poppins Black,92,&H00FFFFFF,&H000000FF,&H000D1526,&H60050810,1,1,0,0,100,100,1,0,1,1.5,3.0,5,50,50,50,1
Style: BlackStyle,Poppins Black,92,&H00161424,&H000000FF,&H00FFFFFF,&H40FFFFFF,1,1,0,0,100,100,1,0,1,1.5,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:05.00,WhiteStyle,,0,0,0,,{{\\pos(960,490)}}LONELY (SO LONELY)\\NI'M MR. LONELY (MR. LONELY)
Dialogue: 0,0:00:05.00,0:00:10.00,BlackStyle,,0,0,0,,{{\\pos(960,490)}}LONELY (SO LONELY)\\NI'M MR. LONELY (MR. LONELY)
"""

with open(os.path.join(base, "test_color_compare.ass"), "w", encoding="utf-8") as f:
    f.write(ass_content)

ass_escaped = os.path.join(base, "test_color_compare.ass").replace("\\", "/").replace(":", "\\\\:")

for ss, name in [("00:00:02", "compare_white_poppins.png"), ("00:00:07", "compare_black_poppins.png")]:
    out_f = os.path.join(brain, name)
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "10", "-i", bg_path,
        "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
        "-ss", ss, "-vframes", "1",
        out_f
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered {name}")

print("Done rendering color comparisons!")
