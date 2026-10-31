import os
import sys
import re
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path('C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video')
songs = [
    {
        'id': '01',
        'folder': 'APT',
        'title': 'APT.',
        'artist': 'ROSÉ & Bruno Mars',
        'theme': 'black',
        'bg_sharp': 'stock_anime_bgs/01_makoto_shinkai_clouds.png'
    },
    {
        'id': '02',
        'folder': 'Die_With_A_Smile',
        'title': 'Die With A Smile',
        'artist': 'Lady Gaga & Bruno Mars',
        'theme': 'white',
        'bg_sharp': 'stock_anime_bgs/02_lofi_twilight_starry_night.png'
    },
    {
        'id': '03',
        'folder': 'Taylor_Swift_The_Fate_of_Ophelia',
        'title': 'The Fate of Ophelia',
        'artist': 'Taylor Swift',
        'theme': 'white',
        'bg_sharp': 'stock_anime_bgs/03_anime_rooftop_sunset_skyline.png'
    },
    {
        'id': '04',
        'folder': 'HUNTR_X_Golden',
        'title': 'Golden',
        'artist': 'HUNTR/X (KPop Demon Hunters)',
        'theme': 'black',
        'bg_sharp': 'stock_anime_bgs/01_makoto_shinkai_clouds.png'
    },
    {
        'id': '05',
        'folder': 'Billie_Eilish_BIRDS_OF_A_FEATHER',
        'title': 'BIRDS OF A FEATHER',
        'artist': 'Billie Eilish',
        'theme': 'black',
        'bg_sharp': 'stock_anime_bgs/01_makoto_shinkai_clouds.png'
    }
]

for s in songs:
    fpath = base / 'songs' / s['folder']
    audio_path = fpath / 'audio.mp3'
    lrc_path = fpath / 'lyrics.lrc'
    
    # ffmpeg duration
    p = subprocess.run([
        'ffmpeg', '-i', str(audio_path)
    ], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors='ignore')
    m_dur = re.search(r"Duration:\s*(\d{2}):(\d{2}):(\d{2}\.\d+)", p.stderr)
    duration = 0.0
    if m_dur:
        duration = int(m_dur.group(1)) * 3600 + int(m_dur.group(2)) * 60 + float(m_dur.group(3))
    
    lines = []
    with open(lrc_path, 'r', encoding='utf-8') as f:
        for l in f:
            m = re.match(r'\[(\d{2}:\d{2}\.\d{2})\](.*)', l.strip())
            if m:
                parts = m.group(1).split(':')
                t = int(parts[0]) * 60 + float(parts[1])
                txt = m.group(2).strip()
                if txt:
                    lines.append((t, txt))
    first_vocal = lines[0][0] if lines else 0.0
    first_text = lines[0][1] if lines else ''
    print(f"{s['id']}. {s['title']} | Artist: {s['artist']} | Duration: {duration:.1f}s | First Vocal: {first_vocal:.2f}s ('{first_text}') | Total Lines: {len(lines)}")
