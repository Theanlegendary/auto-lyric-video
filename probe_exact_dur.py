import subprocess
from pathlib import Path

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/25_The_Neighbourhood_Sweater_Weather")
audio_file = song_dir / "audio_sweater_weather_slowed_reverb.mp3"

res = subprocess.run(["ffmpeg", "-i", str(audio_file)], capture_output=True, text=True, errors="ignore")
for line in res.stderr.splitlines():
    if "Duration:" in line:
        print(line.strip())
