import sys
import requests

sys.stdout.reconfigure(encoding='utf-8')

queries = [
    "APT. ROSE Bruno Mars",
    "Die With A Smile Lady Gaga Bruno Mars",
    "BIRDS OF A FEATHER Billie Eilish",
    "Golden HUNTR/X",
    "The Fate of Ophelia Taylor Swift"
]

for q in queries:
    r = requests.get("https://lrclib.net/api/search", params={"q": q}, headers={"User-Agent": "FadeReplay/1.0"}).json()
    if r:
        item = r[0]
        has_lrc = bool(item.get("syncedLyrics"))
        print(f"[{q}] -> Match: '{item.get('trackName')}' by '{item.get('artistName')}' (Synced: {has_lrc})")
    else:
        print(f"[{q}] -> Not found directly on LRCLIB")
