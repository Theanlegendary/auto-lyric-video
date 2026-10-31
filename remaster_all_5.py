import os
import re
import sys
import subprocess
import time
from pathlib import Path
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
stock_dir = base / "stock_anime_bgs"
songs_dir = base / "songs"
output_dir = base / "output"
videos_dir = base / "videos"
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

def smart_format_lyric(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)
    
    # Check parenthetical ad-lib
    m_paren = re.search(r"^(.*?)\s*(\([^\)]+\))$", text)
    if m_paren:
        main_part = m_paren.group(1).strip()
        paren_part = m_paren.group(2).strip()
        if len(main_part) >= 12:
            return f"{main_part.upper()}\\N{paren_part.upper()}"
            
    # Short line threshold: Keep as 1 clean, bold line!
    words = text.split()
    if len(text) < 34 and len(words) < 8:
        return text.upper()
        
    # Natural comma split
    if "," in text:
        comma_indices = [m.start() for m in re.finditer(r",", text)]
        midpoint = len(text) / 2
        best_comma = min(comma_indices, key=lambda idx: abs(idx - midpoint))
        p1 = text[:best_comma].strip()
        p2 = text[best_comma + 1:].strip()
        if len(p1) >= 8 and len(p2) >= 8:
            return f"{p1.upper()}\\N{p2.upper()}"
            
    # Midpoint split
    mid = len(words) // 2
    p1 = " ".join(words[:mid]).strip()
    p2 = " ".join(words[mid:]).strip()
    return f"{p1.upper()}\\N{p2.upper()}"

def to_seconds(t_str):
    parts = t_str.split(":")
    return int(parts[0]) * 60 + float(parts[1])

def to_ass_time(sec):
    sec = max(0.0, sec)
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def build_smart_ass(folder, title, artist, style_type="black", lead_in=1.0):
    lrc_path = folder / "lyrics.lrc"
    ass_path = folder / "lyrics_remastered.ass"
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
    first_t = parsed[0][0] if parsed else 5.0
    
    # Title card: if first vocal is after 4.5s, display in center for the intro!
    # Else place in clean top header
    if first_t >= 4.5:
        title_end = max(4.0, first_t - 1.0)
        events.append(f"Dialogue: 0,0:00:00.60,{to_ass_time(title_end)},TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(500,400)}}{title.upper()}\\N{{\\fs80\\fsp4}}{artist}")
    else:
        events.append(f"Dialogue: 0,0:00:00.20,0:00:04.50,TitleCard,,0,0,0,,{{\\an8\\pos(960,110)\\fad(300,300)}}{title.upper()}\\N{{\\fs75\\fsp4}}{artist}")
        
    for i in range(len(parsed)):
        t_start, txt = parsed[i]
        t_end = parsed[i+1][0] if i + 1 < len(parsed) else t_start + 4.5
        disp_start = max(0.0, t_start - lead_in)
        disp_end = max(disp_start + 1.2, t_end - 0.2)
        clean_txt = smart_format_lyric(txt)
        events.append(f"Dialogue: 0,{to_ass_time(disp_start)},{to_ass_time(disp_end)},Lyric,,0,0,0,,{{\\pos(960,480)\\fad(150,150)}}{clean_txt}")
        
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(events))
    return ass_path, first_t

def remaster_song(s_info):
    title = s_info["title"]
    artist = s_info["artist"]
    folder = songs_dir / s_info["folder_name"]
    bg_sharp = stock_dir / s_info["bg_name"]
    bg_blur = folder / "bg_blur.png"
    
    if not bg_blur.exists():
        img = Image.open(str(bg_sharp))
        blurred = img.filter(ImageFilter.GaussianBlur(radius=8))
        blurred.save(str(bg_blur))
        
    # Build ASS
    if s_info.get("use_custom_ass"):
        ass_path = folder / s_info["use_custom_ass"]
        first_t = 0.11
    else:
        ass_path, first_t = build_smart_ass(folder, title, artist, s_info["style_type"])
        
    ass_escaped = str(ass_path).replace("\\", "/").replace(":", "\\\\:")
    fonts_escaped = str(stock_dir.parent / "fonts").replace("\\", "/").replace(":", "\\\\:")
    audio_path = folder / "audio.mp3"
    
    # Calculate Dynamic Blur Timing!
    # Background stays 100% SHARP for the full intro!
    if first_t <= 3.5:
        t_blur_start = 0.5
        t_blur_end = 3.0
    else:
        t_blur_start = max(1.5, first_t - 2.5)
        t_blur_end = first_t
        
    dur_blend = t_blur_end - t_blur_start
    print(f"[{title}] First vocal: {first_t:.1f}s | Sharp until: {t_blur_start:.1f}s | Dissolves {t_blur_start:.1f}s -> {t_blur_end:.1f}s")
    
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

    out_file = output_dir / f"{s_info['folder_name']}_Lyric_Video.mp4"
    dest_file = videos_dir / f"{s_info['num']}_{s_info['folder_name']}_Lyric_Video.mp4"
    
    fc = (
        f"[0:v][1:v]blend=all_expr='if(lte(T,{t_blur_start:.2f}),A,if(between(T,{t_blur_start:.2f},{t_blur_end:.2f}),A*(1-(T-{t_blur_start:.2f})/{dur_blend:.2f})+B*(T-{t_blur_start:.2f})/{dur_blend:.2f},B))',"
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
        str(out_file)
    ]
    t0 = time.time()
    subprocess.run(cmd, check=True)
    import shutil
    shutil.copy(str(out_file), str(dest_file))
    print(f"[+] Finished {title} in {time.time()-t0:.1f}s -> {dest_file.name}")

# Songs to remaster with dynamic intro blur + natural 1/2 lines:
queue = [
    {
        "num": "03",
        "folder_name": "Taylor_Swift_The_Fate_of_Ophelia",
        "title": "The Fate of Ophelia",
        "artist": "Taylor Swift",
        "bg_name": "03_anime_rooftop_sunset_skyline.png",
        "style_type": "white"
    },
    {
        "num": "04",
        "folder_name": "HUNTR_X_Golden",
        "title": "Golden",
        "artist": "HUNTR/X",
        "bg_name": "01_makoto_shinkai_clouds.png",
        "style_type": "black"
    },
    {
        "num": "05",
        "folder_name": "Billie_Eilish_BIRDS_OF_A_FEATHER",
        "title": "BIRDS OF A FEATHER",
        "artist": "Billie Eilish",
        "bg_name": "01_makoto_shinkai_clouds.png",
        "style_type": "black"
    }
]

for s in queue:
    remaster_song(s)

print("REMASTER COMPLETE FOR ALL SONGS!")
