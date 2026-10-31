import os
import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path('C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video')

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

# Clean lyric text and handle Korean romanization
def clean_lyric_line(txt: str) -> str:
    txt = txt.strip()
    # Replacements for HUNTR/X Golden Korean lines to Patrick Hand Latin characters
    replacements = {
        "어두워진 (hah) 압길속에 (ah)": "EODUWOJIN (HAH) APGIL SOGE (AH)",
        "끝없이 on stage": "KKEUTEOPSEI ON STAGE",
        "영원히 깨질 수 없는": "YEONGWONHI KKAEJIL SU EOMNEUN",
        "밝게 빛나는 우린": "BALKGE BITNANEUN URIN",
    }
    for k, v in replacements.items():
        if k in txt:
            txt = txt.replace(k, v)
            
    # Generic cleanup
    txt = re.sub(r"\s+", " ", txt)
    return txt.upper()

def parse_and_group_couplets(lrc_path, max_gap=10.0):
    parsed = []
    with open(lrc_path, 'r', encoding='utf-8') as f:
        for line in f:
            m = re.match(r'\[(\d{2}:\d{2}\.\d{2})\](.*)', line.strip())
            if m:
                t = to_seconds(m.group(1))
                txt = clean_lyric_line(m.group(2))
                if txt:
                    parsed.append((t, txt))
                    
    couplets = []
    i = 0
    while i < len(parsed):
        l1 = parsed[i]
        if i + 1 < len(parsed):
            l2 = parsed[i+1]
            gap = l2[0] - l1[0]
            # If two lines are within max_gap, pair them as Row 1 and Row 2
            if gap <= max_gap:
                couplets.append({
                    'lines': [l1, l2],
                    'vocal_start': l1[0],
                    'text': f"{l1[1]}\\N{l2[1]}"
                })
                i += 2
                continue
        # Single line if last line or huge gap
        couplets.append({
            'lines': [l1],
            'vocal_start': l1[0],
            'text': l1[1]
        })
        i += 1
    return couplets

def schedule_events(couplets, song_duration, title, artist, title_end_time):
    events = []
    
    # Title Card event during sharp intro
    events.append(
        f"Dialogue: 0,0:00:00.60,{to_ass_time(title_end_time)},TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(500,400)}}{title.upper()}\\N{{\\fs80\\fsp4}}{artist}"
    )
    
    scheduled_items = []
    n = len(couplets)
    for idx in range(n):
        c = couplets[idx]
        v_start = c['vocal_start']
        
        # Display Start
        if idx == 0:
            disp_start = max(title_end_time + 0.1, v_start - 0.35)
        else:
            prev_end = scheduled_items[-1]['end']
            ideal_start = max(0.0, v_start - 0.35)
            # Guarantee zero overlap: must be strictly >= prev_end + 0.05
            disp_start = max(prev_end + 0.05, ideal_start)
            
        # Display End
        if idx + 1 < n:
            next_v_start = couplets[idx+1]['vocal_start']
            gap = next_v_start - v_start
            if gap > 6.0:
                # Long instrumental break: hold text for 3.2s after last line in couplet, then clear screen
                last_line_t = c['lines'][-1][0]
                disp_end = min(last_line_t + 3.2, next_v_start - 0.40)
            else:
                # Flow to next couplet: end 0.15s before next vocal start
                disp_end = max(disp_start + 1.6, next_v_start - 0.15)
        else:
            last_line_t = c['lines'][-1][0]
            disp_end = min(song_duration - 0.5, last_line_t + 4.0)
            
        if disp_end <= disp_start:
            disp_end = disp_start + 1.5
            
        scheduled_items.append({
            'start': disp_start,
            'end': disp_end,
            'text': c['text']
        })
        
    for item in scheduled_items:
        s_str = to_ass_time(item['start'])
        e_str = to_ass_time(item['end'])
        events.append(
            f"Dialogue: 0,{s_str},{e_str},Lyric,,0,0,0,,{{\\pos(960,490)\\fad(180,180)}}{item['text']}"
        )
        
    return events, scheduled_items

# Test on 3, 4, 5
test_configs = [
    {
        'folder': 'Taylor_Swift_The_Fate_of_Ophelia',
        'title': 'The Fate of Ophelia',
        'artist': 'Taylor Swift',
        'duration': 229.7,
        'title_end': 8.5,
        'style': 'white'
    },
    {
        'folder': 'HUNTR_X_Golden',
        'title': 'Golden',
        'artist': 'HUNTR/X (KPop Demon Hunters)',
        'duration': 191.0,
        'title_end': 13.0,
        'style': 'black'
    },
    {
        'folder': 'Billie_Eilish_BIRDS_OF_A_FEATHER',
        'title': 'BIRDS OF A FEATHER',
        'artist': 'Billie Eilish',
        'duration': 211.1,
        'title_end': 3.0,
        'style': 'black'
    }
]

for cfg in test_configs:
    lrc = base / 'songs' / cfg['folder'] / 'lyrics.lrc'
    couplets = parse_and_group_couplets(lrc)
    events, items = schedule_events(couplets, cfg['duration'], cfg['title'], cfg['artist'], cfg['title_end'])
    
    # Audit for overlaps
    overlaps = []
    for i in range(len(items) - 1):
        if items[i+1]['start'] < items[i]['end']:
            overlaps.append((i, items[i]['end'] - items[i+1]['start'], items[i], items[i+1]))
            
    header = styles_white if cfg['style'] == 'white' else styles_black
    ass_path = base / 'songs' / cfg['folder'] / 'lyrics_couplets_final.ass'
    with open(ass_path, 'w', encoding='utf-8') as f:
        f.write(header + "\n".join(events))
        
    print(f"[{cfg['title']}]")
    print(f"  Couplets: {len(couplets)} | ASS Events: {len(events)} | Overlaps: {len(overlaps)}")
    if overlaps:
        print(f"  ERROR: Found {len(overlaps)} overlaps!")
    else:
        print(f"  VERIFIED: 100% Collision-Free! Written to {ass_path.name}")
