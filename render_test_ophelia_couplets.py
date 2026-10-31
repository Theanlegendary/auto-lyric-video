import os
import re
import subprocess
from PIL import Image, ImageFilter

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
folder = f"{base}/songs/Taylor_Swift_The_Fate_of_Ophelia"
bg_sharp = f"{base}/stock_anime_bgs/03_anime_rooftop_sunset_skyline.png"
bg_blur = f"{folder}/bg_blur.png"

# Ensure blur exists
if not os.path.exists(bg_blur):
    img = Image.open(bg_sharp)
    blurred = img.filter(ImageFilter.GaussianBlur(radius=8))
    blurred.save(bg_blur)

# Build ASS with 2-row couplets
header = """[Script Info]
Title: Taylor Swift - The Fate of Ophelia (2-Row Couplets)
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,Patrick Hand,185,&H00FFFFFF,&H000000FF,&H00121018,&H80000000,1,0,0,0,95,115,3,0,1,2.5,2,5,50,50,50,1
Style: Lyric,Patrick Hand,148,&H00FFFFFF,&H000000FF,&H00121018,&H80000000,0,0,0,0,95,115,1,0,1,2.2,1.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def to_seconds(t_str):
    parts = t_str.split(":")
    return int(parts[0]) * 60 + float(parts[1])

def to_ass_time(sec):
    sec = max(0.0, sec)
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

parsed = []
with open(f"{folder}/lyrics.lrc", "r", encoding="utf-8") as f:
    for line in f:
        m = re.match(r"\[(\d{2}:\d{2}\.\d{2})\](.*)", line.strip())
        if m:
            t = to_seconds(m.group(1))
            txt = m.group(2).strip()
            if txt:
                parsed.append((t, txt))

# 2-Row Couplet Pairing
couplets = []
i = 0
while i < len(parsed):
    l1 = parsed[i]
    if i + 1 < len(parsed):
        l2 = parsed[i+1]
        gap = l2[0] - l1[0]
        if gap <= 10.0:
            t_end = parsed[i+2][0] if i + 2 < len(parsed) else l2[0] + 4.5
            couplets.append({
                "start": l1[0],
                "end": t_end,
                "text": f"{l1[1].strip().upper()}\\N{l2[1].strip().upper()}"
            })
            i += 2
            continue
    t_end = parsed[i+1][0] if i + 1 < len(parsed) else l1[0] + 4.5
    couplets.append({
        "start": l1[0],
        "end": t_end,
        "text": l1[1].strip().upper()
    })
    i += 1

events = []
# Title card during the sharp 8.5s intro!
events.append(f"Dialogue: 0,0:00:00.60,0:00:08.50,TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(500,400)}}THE FATE OF OPHELIA\\N{{\\fs80\\fsp4}}Taylor Swift")

lead_in = 1.0
for c in couplets:
    disp_start = max(0.0, c["start"] - lead_in)
    disp_end = max(disp_start + 1.8, c["end"] - 0.2)
    events.append(f"Dialogue: 0,{to_ass_time(disp_start)},{to_ass_time(disp_end)},Lyric,,0,0,0,,{{\\pos(960,480)\\fad(200,200)}}{c['text']}")

ass_out = f"{folder}/lyrics_2row_couplets.ass"
with open(ass_out, "w", encoding="utf-8") as f:
    f.write(header + "\n".join(events))

print(f"Generated {ass_out} with {len(events)} events!")

# Render test clip for the first 25 seconds
test_mp4 = f"{base}/test/ophelia_2row_test.mp4"
ass_escaped = ass_out.replace("\\", "/").replace(":", "\\\\:")
fonts_escaped = f"{base}/fonts".replace("\\", "/").replace(":", "\\\\:")

# Background stays sharp until 8.5s, dissolves 8.5s to 11.0s
fc = (
    f"[0:v][1:v]blend=all_expr='if(lte(T,8.5),A,if(between(T,8.5,11.0),A*(1-(T-8.5)/2.5)+B*(T-8.5)/2.5,B))',"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped}[v]"
)

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-framerate", "30", "-t", "25", "-i", bg_sharp,
    "-loop", "1", "-framerate", "30", "-t", "25", "-i", bg_blur,
    "-ss", "0", "-t", "25", "-i", f"{folder}/audio.mp3",
    "-filter_complex", fc,
    "-map", "[v]", "-map", "2:a",
    "-c:v", "libx264", "-preset", "faster", "-crf", "18", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    test_mp4
]
subprocess.run(cmd, check=True)

# Extract frame at 0:12:00 (exact time from user screenshot!)
out_frame = f"{base}/test/ophelia_fixed_012s.png"
subprocess.run(["ffmpeg", "-y", "-ss", "00:00:12.500", "-i", test_mp4, "-vframes", "1", out_frame], check=True)

import shutil
shutil.copy(out_frame, f"C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/ophelia_fixed_012s.png")

print("Rendered ophelia_2row_test.mp4 and extracted ophelia_fixed_012s.png successfully!")
