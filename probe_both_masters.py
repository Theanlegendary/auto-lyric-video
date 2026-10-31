import subprocess
from pathlib import Path

v1 = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4")
v2 = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/25_The_Neighbourhood_Sweater_Weather_Slowed_Reverb_Lyric_Video.mp4")

for v in [v1, v2]:
    print(f"File: {v.name} ({v.stat().st_size / (1024*1024):.2f} MB)")
    res = subprocess.run(["ffmpeg", "-i", str(v)], capture_output=True, text=True, errors="ignore")
    for line in res.stderr.splitlines():
        if "Duration:" in line or "Stream #0:0" in line or "Stream #0:1" in line:
            print(" ", line.strip())
