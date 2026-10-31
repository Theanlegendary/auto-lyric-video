import syncedlyrics, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/29_Sia_Chandelier")
lrc = syncedlyrics.search("Sia - Chandelier")

if lrc:
    out_file = song_dir / "lyrics.lrc"
    out_file.write_text(lrc, encoding="utf-8")
    print("Saved lyrics.lrc:")
    print(lrc[:500])
else:
    print("syncedlyrics found nothing.")
