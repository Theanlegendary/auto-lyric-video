import subprocess
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
video = base / "videos" / "25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4"

cmd = ["ffmpeg", "-i", str(video)]
res = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
for line in res.stderr.splitlines():
    if "Duration:" in line or "Stream #" in line:
        print(line.strip())
