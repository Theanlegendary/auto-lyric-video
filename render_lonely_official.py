import os
import sys
import time
import shutil
import subprocess
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "14_Justin_Bieber_Lonely"
audio_path = song_dir / "audio.mp3"
bg_sharp = base / "stock_anime_bgs" / "04_lofi_rainy_window_city_night.png"
bg_blur = song_dir / "bg_blur.png"
ass_path = song_dir / "lyrics_couplets_final.ass"
fonts_dir = base / "fonts"

fonts_escaped = fonts_dir.as_posix().replace(":", "\\\\:")
ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

duration = 149.42
t_sharp = 10.0
t_blur = 12.2
dt = round(t_blur - t_sharp, 2)
t_out = duration - 3.0

# Official Lyric Video Filtergraph:
# 1. Slow Ken Burns zoom on sharp background: zoompan
# 2. Blur intro cross-fade into sharp background
# 3. Fade in from black at 00:00 (1.5s)
# 4. Burn-in official ASS subtitles
# 5. 35mm film grain breathing
# 6. Fade out to black at end (3.0s)
# 7. Audio lead-in and lead-out waveform fading
fc = (
    f"[0:v]zoompan=z='min(zoom+0.00015,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30,"
    f"format=yuva420p,fade=t=out:st={t_sharp}:d={dt}:alpha=1[sharp];"
    f"[1:v][sharp]overlay=0:0:enable='lte(t,{t_blur})',"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=c0s=16:c0f=t+u,"
    f"fade=t=out:st={t_out:.2f}:d=3.0[v];"
    f"[2:a]afade=t=in:ss=0:d=1.8,afade=t=out:st={t_out:.2f}:d=3.0[a]"
)

out_video = base / "videos" / "14_Justin_Bieber_Lonely_Lyric_Video.mp4"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-framerate", "30", "-t", str(duration), "-i", str(bg_sharp),
    "-loop", "1", "-framerate", "30", "-t", str(duration), "-i", str(bg_blur),
    "-i", str(audio_path),
    "-filter_complex", fc,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-preset", "faster", "-b:v", "6M", "-maxrate", "8M", "-bufsize", "12M", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest",
    str(out_video)
]

print("Rendering Official-Grade Lyric Video with FFmpeg...")
t0 = time.time()
subprocess.run(cmd, check=True)
print(f"Render complete in {time.time() - t0:.1f}s! Size: {out_video.stat().st_size / (1024*1024):.2f} MB")

# Extract audit frames
brain_dir = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
f_title = brain_dir / "audit_unique_bg_14_Justin_Bieber_Lonely_title.png"
f_verse = brain_dir / "audit_unique_bg_14_Justin_Bieber_Lonely.png"
f_chorus = brain_dir / "audit_unique_bg_14_Justin_Bieber_Lonely_chorus.png"

subprocess.run(["ffmpeg", "-y", "-ss", "00:00:06.00", "-i", str(out_video), "-vframes", "1", str(f_title)], check=True)
subprocess.run(["ffmpeg", "-y", "-ss", "00:00:15.00", "-i", str(out_video), "-vframes", "1", str(f_verse)], check=True)
subprocess.run(["ffmpeg", "-y", "-ss", "00:00:40.00", "-i", str(out_video), "-vframes", "1", str(f_chorus)], check=True)
print("Extracted verified audit frames!")
