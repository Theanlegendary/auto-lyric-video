import subprocess, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/27_Joji_Glimpse_of_Us")
video_id = "xuGaLIleROI"
video_url = f"https://www.youtube.com/watch?v={video_id}"

# 1. Download audio
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

# 2. Try downloading subtitles
print("Downloading subtitles if available...")
cmd_sub = [
    "yt-dlp",
    "--write-sub",
    "--write-auto-sub",
    "--sub-lang", "en",
    "--convert-subs", "srt",
    "--skip-download",
    "-o", str(song_dir / "sub"),
    video_url
]
res2 = subprocess.run(cmd_sub, capture_output=True, text=True, errors="ignore")
print("Subtitles download return code:", res2.returncode)

# List resulting files
for f in song_dir.glob("*"):
    print(f"  {f.name} ({f.stat().st_size} bytes)")
