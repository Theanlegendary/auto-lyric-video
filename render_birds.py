import os
import sys
import time
import shutil
import subprocess
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "05_Billie_Eilish_BIRDS_OF_A_FEATHER_Pink_Edition"
audio_path = song_dir / "audio.mp3"
bg_sharp = base / "stock_anime_bgs" / "15_anime_birds_of_a_feather_pink_sunset_sky.png"
bg_blur = song_dir / "bg_blur.png"
ass_path = song_dir / "lyrics_couplets_final.ass"
fonts_dir = base / "fonts"

fonts_escaped = fonts_dir.as_posix().replace(":", "\\\\:")
ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

duration = 210.48
t_sharp = 2.25
t_blur = 3.45
dt = round(t_blur - t_sharp, 2)
t_out = duration - 3.0

fc = (
    f"[0:v]format=yuva420p,fade=t=out:st={t_sharp}:d={dt}:alpha=1[sharp];"
    f"[1:v][sharp]overlay=0:0:enable='lte(t,{t_blur})',"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=c0s=22:c0f=t+u[v];"
    f"[2:a]afade=t=in:ss=0:d=1.8,afade=t=out:st={t_out:.2f}:d=3.0[a]"
)

out_video = base / "videos" / "05_Billie_Eilish_BIRDS_OF_A_FEATHER_Pink_Edition_Lyric_Video.mp4"

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

print("Rendering perfected video with FFmpeg...")
t0 = time.time()
subprocess.run(cmd, check=True)
print(f"Render complete in {time.time() - t0:.1f}s!")

# Extract audit frame of clean title card
brain_dir = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
f1 = brain_dir / "audit_birds_clean_title.png"
f2 = brain_dir / "audit_birds_clean_verse1.png"
subprocess.run(["ffmpeg", "-y", "-ss", "00:00:02.00", "-i", str(out_video), "-vframes", "1", str(f1)], check=True)
subprocess.run(["ffmpeg", "-y", "-ss", "00:00:07.00", "-i", str(out_video), "-vframes", "1", str(f2)], check=True)
print("Extracted verified audit frames!")
