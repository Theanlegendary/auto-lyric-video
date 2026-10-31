import os
import re
import subprocess
import time
from pathlib import Path
from PIL import Image, ImageFilter

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
stock_dir = base / "stock_anime_bgs"
songs_dir = base / "songs"
output_dir = base / "output"
fonts_dir = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

styles_white = """[Script Info]
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

styles_black = """[Script Info]
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
    return int(parts[0]) * 60 + float(parts[1])

def to_ass_time(sec):
    sec = max(0.0, sec)
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def format_text(text):
    text = text.strip()
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

def build_ass(song_folder, title, artist, style_type="black", lead_in=1.0):
    lrc_path = song_folder / "lyrics.lrc"
    ass_path = song_folder / "lyrics.ass"
    header = styles_black if style_type == "black" else styles_white
    
    parsed = []
    with open(lrc_path, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\[(\d{2}:\d{2}\.\d{2})\](.*)", line.strip())
            if m:
                t = to_seconds(m.group(1))
                txt = m.group(2).strip()
                if txt:
                    parsed.append((t, txt))
    
    events = []
    # If first lyric is after 4s, put TitleCard in center; else put TitleCard in top header
    first_t = parsed[0][0] if parsed else 5.0
    if first_t >= 4.0:
        events.append(f"Dialogue: 0,0:00:00.60,0:00:04.50,TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(500,400)}}{title.upper()}\\N{{\\fs80\\fsp4}}{artist}")
    else:
        events.append(f"Dialogue: 0,0:00:00.20,0:00:04.50,TitleCard,,0,0,0,,{{\\an8\\pos(960,110)\\fad(300,300)}}{title.upper()}\\N{{\\fs75\\fsp4}}{artist}")
        
    for i in range(len(parsed)):
        t_start, txt = parsed[i]
        t_end = parsed[i+1][0] if i + 1 < len(parsed) else t_start + 4.5
        disp_start = max(0.0, t_start - lead_in)
        disp_end = max(disp_start + 1.2, t_end - 0.2)
        clean_txt = format_text(txt)
        events.append(f"Dialogue: 0,{to_ass_time(disp_start)},{to_ass_time(disp_end)},Lyric,,0,0,0,,{{\\pos(960,480)\\fad(150,150)}}{clean_txt}")
        
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(events))
    print(f"Generated ASS for {title}")
    return ass_path

def render_song(s_info):
    title = s_info["title"]
    artist = s_info["artist"]
    folder = songs_dir / s_info["folder_name"]
    bg_sharp = stock_dir / s_info["bg_name"]
    bg_blur = folder / "bg_blur.png"
    
    # 1. Create soft 8px blur if not exists
    if not bg_blur.exists():
        img = Image.open(str(bg_sharp))
        blurred = img.filter(ImageFilter.GaussianBlur(radius=8))
        blurred.save(str(bg_blur))
        
    # 2. Build ASS
    ass_path = build_ass(folder, title, artist, s_info["style_type"])
    ass_escaped = str(ass_path).replace("\\", "/").replace(":", "\\\\:")
    fonts_escaped = str(stock_dir.parent / "fonts").replace("\\", "/").replace(":", "\\\\:")
    
    audio_path = folder / "audio.mp3"
    out_video = output_dir / f"{s_info['folder_name']}_Lyric_Video.mp4"
    
    # Check duration
    p_dur = subprocess.run(["ffmpeg", "-i", str(audio_path)], capture_output=True, text=True)
    dur_str = "210"
    for line in p_dur.stderr.splitlines():
        if "Duration:" in line:
            m = re.search(r"Duration:\s*(\d{2}):(\d{2}):(\d{2}\.\d{2})", line)
            if m:
                total_s = int(m.group(1))*3600 + int(m.group(2))*60 + float(m.group(3))
                dur_str = str(round(total_s, 1))
                break
                
    print(f"[*] Rendering {title} by {artist} ({dur_str}s)...")
    t0 = time.time()
    
    fc = (
        "[0:v][1:v]blend=all_expr='if(lte(T,2.8),A,if(between(T,2.8,5.5),A*(1-(T-2.8)/2.7)+B*(T-2.8)/2.7,B))',"
        f"subtitles={ass_escaped}:fontsdir={fonts_escaped}[v]"
    )
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-framerate", "30", "-t", dur_str, "-i", str(bg_sharp),
        "-loop", "1", "-framerate", "30", "-t", dur_str, "-i", str(bg_blur),
        "-i", str(audio_path),
        "-filter_complex", fc,
        "-map", "[v]", "-map", "2:a",
        "-c:v", "libx264", "-preset", "faster", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(out_video)
    ]
    subprocess.run(cmd, check=True)
    
    # Copy to root directory for easy access
    root_out = base / f"{s_info['folder_name']}_Lyric_Video.mp4"
    import shutil
    shutil.copy(str(out_video), str(root_out))
    
    print(f"[+] Render finished in {time.time()-t0:.1f}s -> {out_video.name}")
    return root_out

queue = [
    {
        "folder_name": "Taylor_Swift_The_Fate_of_Ophelia",
        "title": "The Fate of Ophelia",
        "artist": "Taylor Swift",
        "bg_name": "03_anime_rooftop_sunset_skyline.png",
        "style_type": "white"
    },
    {
        "folder_name": "HUNTR_X_Golden",
        "title": "Golden",
        "artist": "HUNTR/X",
        "bg_name": "01_makoto_shinkai_clouds.png",
        "style_type": "black"
    },
    {
        "folder_name": "Billie_Eilish_BIRDS_OF_A_FEATHER",
        "title": "BIRDS OF A FEATHER",
        "artist": "Billie Eilish",
        "bg_name": "01_makoto_shinkai_clouds.png",
        "style_type": "black"
    }
]

for s in queue:
    render_song(s)

print("ALL 3 SONGS RENDERED SUCCESSFULLY!")
