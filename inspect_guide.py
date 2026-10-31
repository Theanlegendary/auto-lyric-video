import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

guide = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/Fade_Replay_YouTube_Upload_Guide.txt")
text = guide.read_text(encoding="utf-8")

# Let's search for Song 24 or Song 25 in the guide
idx = text.find("SONG 25")
if idx == -1:
    idx = text.find("Sweater Weather")
if idx != -1:
    print(text[idx:idx+1500])
else:
    print("Sweater Weather not found in guide. Showing last 1000 characters:")
    print(text[-1000:])
