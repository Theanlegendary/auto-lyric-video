#!/usr/bin/env python3
"""
Test Cinematic Background Video Render
Combines:
- Preset Background (e.g. Twilight Night or Rainy City Night)
- Ken Burns motion (smooth slow zoom 1.00 -> 1.05 over duration)
- Restrained color grade & subtle 35mm organic film grain
- Adaptive contrast lyrics (Cormorant Garamond SemiBold, soft white #F7F5F2)
- Zero overlaps & upward settle
"""

import sys
import subprocess
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))
from lyric_engine import LyricLayoutEngine

engine = LyricLayoutEngine(1920, 1080)
fonts_dir = BASE_DIR / "fonts"
output_dir = BASE_DIR / "output"

song_dir = BASE_DIR / "songs" / "Die_With_A_Smile"
audio_path = song_dir / "audio.mp3"
lrc_path = song_dir / "lyrics.lrc"
bg_image = BASE_DIR / "cinematic_bgs" / "twilight_night.png"
ass_path = song_dir / "lyrics_cinematic_test.ass"
out_video = output_dir / "Die_With_A_Smile_Cinematic_Motion_Preview.mp4"

# 1. Generate Subtitle with Cormorant Garamond
engine.generate_ass_file(
    lrc_path=lrc_path,
    out_ass_path=ass_path,
    bg_image_path=bg_image,
    title="Die With A Smile",
    artist="Lady Gaga & Bruno Mars",
    preset_key="cinematic",
    vertical_ratio=0.60
)

# 2. FFmpeg Escape
ass_esc = str(ass_path).replace("\\", "/").replace(":", "\\\\:")
fonts_esc = str(fonts_dir).replace("\\", "/").replace(":", "\\\\:")

# 3. Ken Burns Slow Zoom + 35mm Organic Film Grain + Restrained Grade + Subtitle Overlay
# 25-second preview encompassing Opening Sequence (0-5s) and first lyric entry (7.8s)
duration = 25.0
total_frames = int(duration * 30)

filter_complex = (
    f"[0:v]zoompan=z='min(zoom+0.00018,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,"
    f"eq=contrast=1.02:brightness=-0.02:saturation=0.96,"
    f"noise=alls=6:allf=t+u,"
    f"subtitles={ass_esc}:fontsdir={fonts_esc}[v]"
)

cmd = [
    "ffmpeg", "-nostdin", "-y",
    "-loop", "1", "-framerate", "30", "-t", str(duration), "-i", str(bg_image),
    "-ss", "0", "-t", str(duration), "-i", str(audio_path),
    "-filter_complex", filter_complex,
    "-map", "[v]", "-map", "1:a",
    "-c:v", "libx264", "-preset", "ultrafast", "-crf", "19", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest",
    str(out_video)
]

print("Rendering 25s Cinematic Motion Preview with Ken Burns Zoom & Film Grain...")
t0 = time.time()
p = subprocess.run(cmd, capture_output=True, text=True, stdin=subprocess.DEVNULL)
print(f"Exit code: {p.returncode} | Took: {time.time()-t0:.1f}s")
if p.returncode == 0:
    print(f"Success! Output: {out_video.name} ({out_video.stat().st_size / (1024*1024):.2f} MB)")
else:
    print("FFmpeg error:", p.stderr[-600:])
