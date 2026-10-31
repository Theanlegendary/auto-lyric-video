import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

video_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos")
files = sorted(video_dir.glob("*.mp4"), key=lambda x: x.stat().st_size, reverse=True)

total = 0
for f in files:
    sz = f.stat().st_size / (1024 * 1024)
    total += sz
    print(f"{f.name}: {sz:.2f} MB")

print(f"Total video size: {total:.2f} MB")
