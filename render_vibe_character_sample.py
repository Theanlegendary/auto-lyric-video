import os
import sys
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "15_Akon_Lonely"
audio_path = song_dir / "audio_7clouds.mp3"
bg_vibe = song_dir / "vibe_character_blurred_master.png"
ass_path = song_dir / "lyrics_spotify_rdr_orange.ass"
out_video = base / "videos" / "15_Akon_Lonely_Sample_Vibe_Character.mp4"

fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

# 25-second sample
fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=5:allf=t+u[v]"
)

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", "25", "-i", str(bg_vibe),
    "-i", str(audio_path),
    "-t", "25",
    "-filter_complex", fc,
    "-map", "[v]",
    "-map", "1:a",
    "-af", "afade=t=in:ss=0:d=1.8",
    "-c:v", "libx264", "-preset", "ultrafast", "-crf", "18",
    "-c:a", "aac", "-b:a", "320k",
    str(out_video)
]

print("Rendering 25s Vibe Character video sample...")
res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')
if res.returncode == 0:
    print(f"Rendered: {out_video.name} ({out_video.stat().st_size / (1024*1024):.2f} MB)")
else:
    print(f"Failed: {res.stderr[-200:]}")
