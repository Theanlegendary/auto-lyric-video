import re
from pathlib import Path

apt_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/APT")
lrc_file = apt_dir / "lyrics.lrc"
ass_file = apt_dir / "lyrics.ass"

header = """[Script Info]
Title: APT. - ROSÉ & Bruno Mars Lyric Video
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,Patrick Hand,185,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,1,0,0,0,95,115,3,0,1,2,1,5,50,50,50,1
Style: Lyric,Patrick Hand,148,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,0,0,0,0,95,115,1,0,1,1.8,0.8,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def to_seconds(t_str):
    parts = t_str.split(":")
    m = int(parts[0])
    s = float(parts[1])
    return m * 60 + s

def to_ass_time(sec):
    sec = max(0.0, sec)
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def format_text(text):
    text = text.replace("아파트", "APATEU").replace("채영이가 좋아하는 랜덤 게임", "CHAEYOUNG'S FAVORITE RANDOM GAME")
    text = text.strip()
    # Replace comma split with newline
    if "," in text:
        idx = text.find(",")
        p1 = text[:idx].strip()
        p2 = text[idx+1:].strip()
        if len(p1) >= 5 and len(p2) >= 5:
            return f"{p1.upper()}\\N{p2.upper()}"
    words = text.split()
    if len(words) >= 5 or len(text) > 28:
        mid = len(words) // 2
        p1 = " ".join(words[:mid]).upper()
        p2 = " ".join(words[mid:]).upper()
        return f"{p1}\\N{p2}"
    return text.upper()

parsed = []
with open(lrc_file, "r", encoding="utf-8") as f:
    for line in f:
        m = re.match(r"\[(\d{2}:\d{2}\.\d{2})\](.*)", line.strip())
        if m:
            t = to_seconds(m.group(1))
            txt = m.group(2).strip()
            if txt:
                parsed.append((t, txt))

events = []
# Title card
events.append(f"Dialogue: 0,0:00:00.50,0:00:04.50,TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(400,300)}}APT.\\N{{\\fs80\\fsp4}}ROSÉ & Bruno Mars")

lead_in = 1.0
for i in range(len(parsed)):
    t_start, txt = parsed[i]
    t_end = parsed[i+1][0] if i + 1 < len(parsed) else t_start + 4.5
    
    disp_start = max(0.0, t_start - lead_in)
    disp_end = max(disp_start + 1.2, t_end - 0.2)
    
    clean_txt = format_text(txt)
    events.append(f"Dialogue: 0,{to_ass_time(disp_start)},{to_ass_time(disp_end)},Lyric,,0,0,0,,{{\\pos(960,470)\\fad(150,150)}}{clean_txt}")

with open(ass_file, "w", encoding="utf-8") as f:
    f.write(header + "\n".join(events))

print(f"Generated {ass_file} with {len(events)} events!")
