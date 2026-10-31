import syncedlyrics, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/27_Joji_Glimpse_of_Us")
lrc = syncedlyrics.search("Joji - Glimpse of Us")

if lrc:
    out_file = song_dir / "lyrics.lrc"
    out_file.write_text(lrc, encoding="utf-8")
    print("Saved lyrics.lrc:")
    print(lrc[:500])
else:
    print("syncedlyrics found nothing.")
