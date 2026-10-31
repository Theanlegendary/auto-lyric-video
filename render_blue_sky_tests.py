import os
import sys
import subprocess
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
bg_path = os.path.join(base, "stock_anime_bgs", "17_anime_clear_blue_sky_clouds.png")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

# Let's test two color themes:
# Theme 1: Luminous White text with deep blue-slate ambient shadow (cleanest aesthetic)
# Theme 2: Deep Midnight / Slate text with soft glow

test_ass_white = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleUltra,Ultra,145,&H00FFFFFF,&H000000FF,&H000F172A,&H600A1020,1,1,0,0,100,100,2,0,1,1.5,3.0,5,50,50,50,1
Style: LyricPoppins,Poppins Black,92,&H00FFFFFF,&H000000FF,&H000F172A,&H600A1020,1,1,0,0,100,100,1,0,1,1.2,2.5,5,50,50,50,1
Style: LyricBarlow,Barlow,94,&H00FFFFFF,&H000000FF,&H000F172A,&H600A1020,1,1,0,0,100,100,1,0,1,1.2,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:01.00,0:00:05.00,TitleUltra,,0,0,0,,{{\\pos(960,470)\\t(0,200,\\fscx108\\fscy108)\\t(200,350,\\fscx100\\fscy100)}}✧ LONELY ✧\\N{{\\fs70\\fsp4\\i1}}✦ Akon ✦
Dialogue: 0,0:00:05.00,0:00:10.00,LyricPoppins,,0,0,0,,{{\\pos(960,490)\\t(0,180,\\fscx106\\fscy106)\\t(180,300,\\fscx100\\fscy100)}}LONELY (SO LONELY)\\NI'M MR. LONELY (MR. LONELY)
Dialogue: 0,0:00:10.00,0:00:15.00,LyricBarlow,,0,0,0,,{{\\pos(960,490)\\t(0,180,\\fscx106\\fscy106)\\t(180,300,\\fscx100\\fscy100)}}LONELY (SO LONELY)\\NI'M MR. LONELY (MR. LONELY)
"""

test_ass_file = os.path.join(base, "test_blue_sky_style.ass")
with open(test_ass_file, "w", encoding="utf-8") as f:
    f.write(test_ass_white)

ass_escaped = test_ass_file.replace("\\", "/").replace(":", "\\\\:")

# Render Title (00:03), Poppins (00:07), Barlow (00:12)
renders = [
    ("00:00:03", "test_blue_sky_ultra_title.png"),
    ("00:00:07", "test_blue_sky_poppins_hook.png"),
    ("00:00:12", "test_blue_sky_barlow_hook.png"),
]

for ss, out_name in renders:
    out_p = os.path.join(brain, out_name)
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "15", "-i", bg_path,
        "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
        "-ss", ss, "-vframes", "1",
        out_p
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered: {out_name}")

print("Test renders complete!")
