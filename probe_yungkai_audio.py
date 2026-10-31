import subprocess
from pathlib import Path

audio = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/28_yung_kai_blue/audio.mp3")
res = subprocess.run(["ffmpeg", "-i", str(audio)], capture_output=True, text=True, errors="ignore")
for line in res.stderr.splitlines():
    if "Duration:" in line or "Stream #0:0" in line:
        print(line.strip())
