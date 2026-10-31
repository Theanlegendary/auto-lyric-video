import os
import sys
import re
import json
import time
import shutil
import requests
import subprocess
from pathlib import Path
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
sys.path.insert(0, str(base))
import bg_manager

fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
artifacts_dir = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

styles_white = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,Patrick Hand,175,&H00FFFFFF,&H000000FF,&H00121018,&H80000000,1,0,0,0,95,115,3,0,1,2.5,2,5,50,50,50,1
Style: Lyric,Patrick Hand,135,&H00FFFFFF,&H000000FF,&H00121018,&H80000000,0,0,0,0,95,115,1,0,1,2.2,1.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

styles_cloud = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,Sniglet,165,&H00FFFFFF,&H000000FF,&H00181228,&H70000000,1,0,0,0,100,100,3,0,1,3.0,2.5,5,50,50,50,1
Style: Lyric,Sniglet,130,&H00FFFFFF,&H000000FF,&H00181228,&H70000000,1,0,0,0,100,100,2,0,1,2.8,2.0,5,50,50,50,1

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
Style: TitleCard,Patrick Hand,175,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,1,0,0,0,95,115,3,0,1,2,1,5,50,50,50,1
Style: Lyric,Patrick Hand,135,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,0,0,0,0,95,115,1,0,1,1.8,0.8,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def to_seconds(t_str):
    parts = t_str.split(':')
    return int(parts[0]) * 60 + float(parts[1])

def to_ass_time(sec):
    sec = max(0.0, sec)
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def fetch_lrc(query):
    url = "https://lrclib.net/api/search"
    resp = requests.get(url, params={"q": query}, headers={"User-Agent": "FadeReplay/1.0"}).json()
    if resp:
        for item in resp:
            if item.get("syncedLyrics"):
                return item["syncedLyrics"]
    return None

def download_audio(query, out_mp3):
    # Method from 'That Should Be Me': search top community lyric channels (e.g. Cakes & Eclairs, 7clouds)
    # rather than raw official topic master tracks to obtain pre-cleared audio with 0 territory blocks
    cmd = [
        "yt-dlp",
        "--default-search", "ytsearch",
        "-x", "--audio-format", "mp3",
        "--audio-quality", "0",
        "-o", str(out_mp3),
        f"{query} lyrics"
    ]
    subprocess.run(cmd, check=True)

def parse_and_group_couplets(lrc_text, max_gap=10.0):
    parsed = []
    for line in lrc_text.strip().split("\n"):
        m = re.match(r'\[(\d{2}:\d{2}\.\d{2})\](.*)', line.strip())
        if m:
            t = to_seconds(m.group(1))
            txt = re.sub(r"\s+", " ", m.group(2).strip().upper())
            if txt:
                parsed.append((t, txt))
                
    couplets = []
    i = 0
    while i < len(parsed):
        l1 = parsed[i]
        if i + 1 < len(parsed):
            l2 = parsed[i+1]
            gap = l2[0] - l1[0]
            if gap <= max_gap:
                couplets.append({
                    'lines': [l1, l2],
                    'vocal_start': l1[0],
                    'text': f"{l1[1]}\\N{l2[1]}"
                })
                i += 2
                continue
        couplets.append({
            'lines': [l1],
            'vocal_start': l1[0],
            'text': l1[1]
        })
        i += 1
    return couplets

def schedule_events(couplets, song_duration, title, artist, title_end_time):
    events = []
    events.append(
        f"Dialogue: 0,0:00:00.60,{to_ass_time(title_end_time)},TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(500,400)}}{title.upper()}\\N{{\\fs80\\fsp4}}{artist}"
    )
    scheduled_items = []
    n = len(couplets)
    for idx in range(n):
        c = couplets[idx]
        v_start = c['vocal_start']
        last_v = c['lines'][-1][0]
        
        ideal_start = max(0.0, v_start - 0.35)
        if idx == 0:
            disp_start = max(title_end_time + 0.1, ideal_start)
        else:
            prev_end = scheduled_items[-1]['end']
            disp_start = max(prev_end + 0.05, ideal_start)
            
        if idx + 1 < n:
            next_v_start = couplets[idx+1]['vocal_start']
            gap = next_v_start - last_v
            if gap > 7.5:
                # Extended pause or instrumental break: hold comfortably through vocal tail
                disp_end = min(last_v + 5.5, next_v_start - 0.25)
            else:
                # Continuous singing: hold until right before the next couplet arrives
                disp_end = max(disp_start + 1.8, next_v_start - 0.20)
        else:
            # Final couplet: hold until outro
            disp_end = min(song_duration - 1.0, last_v + 6.0)
            
        if disp_end <= disp_start:
            disp_end = disp_start + 2.0
            
        scheduled_items.append({'start': disp_start, 'end': disp_end, 'text': c['text']})
        
    for item in scheduled_items:
        s_str = to_ass_time(item['start'])
        e_str = to_ass_time(item['end'])
        events.append(
            f"Dialogue: 0,{s_str},{e_str},Lyric,,0,0,0,,{{\\pos(960,490)\\fad(180,120)}}{item['text']}"
        )
    return events

def produce_song(song_num, title, artist, preferred_vibe=None, display_title=None):
    shown_title = display_title if display_title else title
    clean_artist = re.sub(r'[^a-zA-Z0-9_]', '', artist.replace(' ', '_'))
    clean_title = re.sub(r'[^a-zA-Z0-9_]', '', title.replace(' ', '_'))
    folder_name = f"{song_num:02d}_{clean_artist}_{clean_title}"
    song_dir = base / "songs" / folder_name
    song_dir.mkdir(parents=True, exist_ok=True)
    audio_path = song_dir / "audio.mp3"
    
    print(f"\n=======================================================")
    print(f"PRODUCING SONG #{song_num}: {title} by {artist}")
    print(f"=======================================================")
    
    # 1. Fetch LRC
    print("1. Fetching synced LRC lyrics...")
    lrc_file = song_dir / "lyrics.lrc"
    if lrc_file.exists():
        with open(lrc_file, "r", encoding="utf-8") as f:
            lrc_text = f.read()
        print("  -> Using cached synced LRC lyrics.")
    else:
        lrc_text = fetch_lrc(f"{artist} {title}")
        if not lrc_text:
            raise RuntimeError(f"Could not find synced LRC for {title} by {artist}")
        with open(lrc_file, "w", encoding="utf-8") as f:
            f.write(lrc_text)
        print("  -> Synced LRC lyrics downloaded.")
    
    # 2. Download audio if not exists
    if not audio_path.exists():
        print(f"2. Downloading audio via yt-dlp...")
        download_audio(f"{artist} {title}", audio_path)
        print("  -> Audio download complete.")
    else:
        print("2. Audio already exists.")
        
    # 3. Detect Duration & First Vocal
    p = subprocess.run([
        'ffmpeg', '-i', str(audio_path)
    ], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors='ignore')
    m_dur = re.search(r"Duration:\s*(\d{2}):(\d{2}):(\d{2}\.\d+)", p.stderr)
    duration = 200.0
    if m_dur:
        duration = int(m_dur.group(1)) * 3600 + int(m_dur.group(2)) * 60 + float(m_dur.group(3))
        
    couplets = parse_and_group_couplets(lrc_text)
    first_vocal = couplets[0]['vocal_start'] if couplets else 5.0
    print(f"  -> Duration: {duration:.1f}s | First vocal: {first_vocal:.2f}s | Total couplets: {len(couplets)}")
    
    # 4. Get NEVER-USED UNIQUE BACKGROUND from registry
    print("3. Querying Background Registry for an unused unique background...")
    reg = bg_manager.load_registry()
    existing_bg = next((b for b in reg if b.get("assigned_to") == folder_name), None)
    if existing_bg:
        bg_entry = existing_bg
        print(f"  -> Reusing existing assigned [{bg_entry['id']}]: '{bg_entry['name']}' ({bg_entry['theme'].upper()})")
    else:
        bg_entry = bg_manager.get_fresh_background(preferred_tag=preferred_vibe)
        bg_id = bg_entry["id"]
        bg_manager.assign_background_to_song(bg_id, folder_name)
        print(f"  -> Assigned [{bg_id}]: '{bg_entry['name']}' ({bg_entry['theme'].upper()}) to this song!")
    bg_sharp = base / "stock_anime_bgs" / bg_entry["file"]
    theme = bg_entry["theme"]
    
    # 5. Create 8px Gaussian blur
    bg_blur = song_dir / "bg_blur.png"
    img = Image.open(str(bg_sharp))
    img.filter(ImageFilter.GaussianBlur(radius=8)).save(str(bg_blur))
    
    # 6. Intro timing
    if first_vocal >= 4.0:
        t_blur = first_vocal
        t_sharp = max(2.0, first_vocal - 1.2)
        title_end = t_sharp
    else:
        t_sharp = 2.0
        t_blur = max(3.0, first_vocal)
        title_end = 2.0
        
    # 7. Generate ASS
    if theme == "cloud":
        header = styles_cloud
    elif theme == "black":
        header = styles_black
    else:
        header = styles_white
    events = schedule_events(couplets, duration, shown_title, artist, title_end)
    ass_path = song_dir / "lyrics_couplets_final.ass"
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(events))
    print(f"4. Created 2-row couplet ASS with 0 collisions ({len(events)} events).")
    
    # 8. Render Video with Medium Aesthetic Lofi Film Grain
    print("5. Rendering 1080p video with Medium Aesthetic Lofi Grain (c0s=22)...")
    t0 = time.time()
    dt = round(t_blur - t_sharp, 2)
    ass_escaped = ass_path.as_posix().replace(":", "\\\\:")
    t_out = max(1.0, duration - 3.0)
    fc = (
        f"[0:v]format=yuva420p,fade=t=out:st={t_sharp}:d={dt}:alpha=1[sharp];"
        f"[1:v][sharp]overlay=0:0:enable='lte(t,{t_blur})',"
        f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
        f"noise=c0s=22:c0f=t+u[v];"
        f"[2:a]afade=t=in:ss=0:d=1.8,afade=t=out:st={t_out:.2f}:d=3.0[a]"
    )
    
    out_filename = f"{song_num:02d}_{clean_artist}_{clean_title}_Lyric_Video.mp4"
    out_video = base / "videos" / out_filename
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-framerate", "30", "-t", str(duration), "-i", str(bg_sharp),
        "-loop", "1", "-framerate", "30", "-t", str(duration), "-i", str(bg_blur),
        "-i", str(audio_path),
        "-filter_complex", fc,
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "faster", "-b:v", "6M", "-maxrate", "8M", "-bufsize", "12M", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(out_video)
    ]
    subprocess.run(cmd, check=True)
    
    render_time = time.time() - t0
    size_mb = os.path.getsize(out_video) / (1024 * 1024)
    print(f"  -> Render finished in {render_time:.1f}s | Size: {size_mb:.2f} MB")
    
    # Master copy stored in videos/
    print(f"  -> Video ready in videos/{out_filename}")
    
    # Extract audit frame
    frame_name = f"audit_unique_bg_{folder_name}.png"
    frame_path = base / "test" / frame_name
    sample_t = to_ass_time(first_vocal + 10.0)
    subprocess.run([
        "ffmpeg", "-y", "-ss", sample_t, "-i", str(out_video),
        "-vframes", "1", str(frame_path)
    ], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    shutil.copy(frame_path, artifacts_dir / frame_name)
    print(f"  -> Extracted audit frame: {frame_name} at {sample_t}")
    
    return {
        "num": song_num,
        "title": title,
        "artist": artist,
        "video_path": out_video,
        "bg_name": bg_entry["name"],
        "frame_name": frame_name,
        "size_mb": size_mb
    }

if __name__ == "__main__":
    res = produce_song(6, "Espresso", "Sabrina Carpenter", preferred_vibe="cafe")
    print(f"\nSUCCESSFULLY PRODUCED SONG 6: {res['title']} by {res['artist']}!")
