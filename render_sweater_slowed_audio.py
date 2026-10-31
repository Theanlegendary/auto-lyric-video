import subprocess
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "25_The_Neighbourhood_Sweater_Weather"
src_audio = song_dir / "audio.mp3"
out_audio = song_dir / "audio_sweater_weather_slowed_reverb.mp3"

af = (
    "asetrate=48000*0.865,aresample=44100,"
    "asplit=2[dry][wet_in];"
    "[wet_in]highpass=f=200,lowpass=f=8500,"
    "aecho=0.85:0.78:55|110|220|350|520|750:0.45|0.38|0.30|0.22|0.15|0.08,"
    "volume=0.40[wet];"
    "[dry][wet]amix=inputs=2:weights=1.0 0.55:dropout_transition=0,"
    "lowpass=f=15500,"
    "equalizer=f=150:t=q:w=1.0:g=1.5,"
    "alimiter=limit=0.95"
)

cmd = [
    "ffmpeg", "-y",
    "-i", str(src_audio),
    "-filter_complex", af,
    "-c:a", "libmp3lame",
    "-b:a", "320k",
    str(out_audio)
]

print("Rendering Master Slowed + Reverb Audio for Sweater Weather...")
res = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
print("Return code:", res.returncode)

if res.returncode == 0:
    print(f"File size: {out_audio.stat().st_size / (1024*1024):.2f} MB")
    # Probe duration
    p = subprocess.run(["ffmpeg", "-i", str(out_audio)], capture_output=True, text=True, errors="ignore")
    for line in p.stderr.splitlines():
        if "Duration:" in line:
            print(line.strip())
else:
    print("Error:", res.stderr)
