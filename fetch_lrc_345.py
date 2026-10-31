import sys
import os
import requests
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

songs = [
    {
        "id": 3,
        "name": "Taylor_Swift_The_Fate_of_Ophelia",
        "title": "The Fate of Ophelia",
        "artist": "Taylor Swift",
        "yt_id": "rbmdfEQODOw",
        "lrc_query": "The Fate of Ophelia Taylor Swift",
        "bg_name": "03_anime_rooftop_sunset_skyline.png",
        "text_color": "white"
    },
    {
        "id": 4,
        "name": "HUNTR_X_Golden",
        "title": "Golden",
        "artist": "HUNTR/X",
        "yt_id": "BvYZXYPuuos",
        "lrc_query": "Golden HUNTR/X",
        "bg_name": "01_makoto_shinkai_clouds.png",
        "text_color": "black"
    },
    {
        "id": 5,
        "name": "Billie_Eilish_BIRDS_OF_A_FEATHER",
        "title": "BIRDS OF A FEATHER",
        "artist": "Billie Eilish",
        "yt_id": "d5gf9dXbPi0",
        "lrc_query": "BIRDS OF A FEATHER Billie Eilish",
        "bg_name": "01_makoto_shinkai_clouds.png",
        "text_color": "black"
    }
]

base_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs")

for s in songs:
    s_dir = base_dir / s["name"]
    s_dir.mkdir(parents=True, exist_ok=True)
    
    r = requests.get("https://lrclib.net/api/search", params={"q": s["lrc_query"]}, headers={"User-Agent": "FadeReplay/1.0"}).json()
    if r:
        lrc_text = r[0].get("syncedLyrics") or r[0].get("plainLyrics")
        with open(s_dir / "lyrics.lrc", "w", encoding="utf-8") as f:
            f.write(lrc_text)
        print(f"[{s['title']}] Saved LRC ({len(lrc_text.splitlines())} lines)")
    else:
        print(f"[{s['title']}] No LRC found on LRCLIB!")
