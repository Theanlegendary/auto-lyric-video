import sys, subprocess, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/25_The_Neighbourhood_Sweater_Weather")

def probe_audio(path):
    cmd = [
        "ffmpeg", "-i", str(path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
    for line in res.stderr.splitlines():
        if "Duration:" in line or "Stream #0:0" in line:
            print("  ", line.strip())

print("Normal Audio:")
probe_audio(song_dir / "audio.mp3")

print("\nSlowed Reverb Audio:")
probe_audio(song_dir / "audio_sweater_weather_slowed_reverb.mp3")
