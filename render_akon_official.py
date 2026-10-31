import os
import sys
import time
import shutil
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "15_Akon_Lonely"
audio_path = song_dir / "audio_7clouds.mp3"
bg_blur = song_dir / "vibe_sky_blurred_master.png"
ass_path = song_dir / "lyrics_couplets_final.ass"
videos_dir = base / "videos"
videos_dir.mkdir(exist_ok=True)
out_video = videos_dir / "15_Akon_Lonely_Lyric_Video.mp4"

fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

duration = 235.13
t_out = round(duration - 3.0, 2)

# Filtergraph:
# 1. Slow Ken Burns push-in zoompan
# 2. Fade in from black at 00:00 (1.5s)
# 3. Burn-in official ASS subtitles
# 4. Subtle 35mm film grain breathing (noise=alls=6:allf=t+u)
# 5. Fade out to black at end (3.0s)
fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=6:allf=t+u,"
    f"fade=t=out:st={t_out}:d=3.0[v]"
)

af = f"afade=t=in:ss=0:d=1.8,afade=t=out:st={t_out}:d=3.0"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", str(duration), "-i", str(bg_blur),
    "-i", str(audio_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-map", "1:a",
    "-af", af,
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "18",
    "-c:a", "aac",
    "-b:a", "320k",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    str(out_video)
]

print("Starting official lyric video render for Akon - Lonely...")
start_time = time.time()
res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')
elapsed = time.time() - start_time

if res.returncode == 0:
    size_mb = out_video.stat().st_size / (1024 * 1024)
    print(f"SUCCESS! Rendered {out_video.name} in {elapsed:.1f}s ({size_mb:.2f} MB)")
else:
    print(f"FAILED with returncode {res.returncode}")
    print("Stderr tail:")
    print("\n".join(res.stderr.splitlines()[-30:]))
