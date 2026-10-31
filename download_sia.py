import subprocess, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/29_Sia_Chandelier")
video_id = "joxBujMflPk"
video_url = f"https://www.youtube.com/watch?v={video_id}"

print("Downloading audio from 7clouds...")
cmd_audio = [
    "yt-dlp",
    "-x",
    "--audio-format", "mp3",
    "--audio-quality", "0",
    "-o", str(song_dir / "audio.%(ext)s"),
    video_url
]
res1 = subprocess.run(cmd_audio, capture_output=True, text=True, errors="ignore")
print("Audio download return code:", res1.returncode)

for f in song_dir.glob("*"):
    print(f"  {f.name} ({f.stat().st_size} bytes)")
