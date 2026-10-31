import os
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
sys.path.insert(0, str(base))

from auto_producer import produce_song

queue = [
    {
        "num": 8,
        "title": "Good Luck, Babe!",
        "artist": "Chappell Roan",
        "vibe": "retro"
    },
    {
        "num": 9,
        "title": "Lose Control",
        "artist": "Teddy Swims",
        "vibe": "rain"
    },
    {
        "num": 10,
        "title": "Dandelions",
        "artist": "Ruth B.",
        "vibe": "sakura"
    }
]

print("=================================================================")
print("STARTING BATCH PRODUCTION: SONGS 8, 9, 10")
print("=================================================================")

total_t0 = time.time()
results = []

for item in queue:
    t_start = time.time()
    print(f"\n>>> Launching Song #{item['num']}: '{item['title']}' by {item['artist']}...")
    try:
        res = produce_song(item['num'], item['title'], item['artist'], preferred_vibe=item['vibe'])
        results.append(res)
        print(f">>> Successfully completed #{item['num']} in {time.time()-t_start:.1f}s!")
    except Exception as e:
        print(f"ERROR producing #{item['num']}: {e}")
        sys.exit(1)

total_elapsed = time.time() - total_t0
print("\n=================================================================")
print(f"ALL SONGS (8, 9, 10) SUCCESSFULLY PRODUCED IN {total_elapsed:.1f}s!")
print("=================================================================")
for r in results:
    print(f"  • Song #{r['num']:02d}: {r['title']} - {r['artist']} | Artwork: '{r['bg_name']}' | Size: {r['size_mb']:.1f} MB")
