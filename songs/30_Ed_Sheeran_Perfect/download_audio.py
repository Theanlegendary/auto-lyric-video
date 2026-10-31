import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\30_Ed_Sheeran_Perfect")
song_dir.mkdir(parents=True, exist_ok=True)

video_id = "kPhpHvnnn0Q"
video_url = f"https://www.youtube.com/watch?v={video_id}"

print("Downloading audio from 7clouds (kPhpHvnnn0Q)...")
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
