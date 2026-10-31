import subprocess
import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

for fsz in [105, 115, 125]:
    ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Verse,Chewy,{fsz},&H00FFFFFF,&H000000FF,&H00100818,&H50000000,1,0,0,0,100,100,1,0,1,0.8,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:01.00,Verse,,0,0,0,,{{\\pos(960,500)}}THAT GOT THAT ONE GOOD GIRL WHO'S ALWAYS BEEN THERE MAN, LIKE\\NTOOK ALL THE BULLSHIT
"""
    ass_path = os.path.join(base, f"test_verse_sz_{fsz}.ass")
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass)
    
    ass_escaped = ass_path.replace("\\", "/").replace(":", "\\\\:")
    out_img = os.path.join(base, f"test_verse_sz_{fsz}.png")
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=black:s=1920x1080:d=1",
        "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
        "-frames:v", "1", out_img
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    
    im = Image.open(out_img)
    pix = im.load()
    min_x, max_x = 1920, 0
    for y in range(300, 700):
        for x in range(0, 1920):
            if pix[x, y][0] > 100:
                if x < min_x: min_x = x
                if x > max_x: max_x = x
    w = max_x - min_x
    print(f"FontSize {fsz} -> Text Width: {w}px, Margins: {min_x}px left, {1920 - max_x}px right")
