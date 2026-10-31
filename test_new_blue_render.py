import sys
from pathlib import Path
from PIL import Image
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

raw_img_path = brain / "yung_kai_blue_7clouds_twilight_wallpaper_1793330937570.jpg"
song_dir = base / "songs" / "28_yung_kai_blue"

# 1. Resize to 1920x1080 with high quality Lanczos
img = Image.open(raw_img_path).convert('RGB')
img_1080 = img.resize((1920, 1080), Image.Resampling.LANCZOS)
master_twilight_path = song_dir / "blue_7clouds_twilight_master.png"
img_1080.save(master_twilight_path)
print(f"Saved 1080p master: {master_twilight_path}")

# 2. Check ASS file
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
ass_path = song_dir / "lyrics_7clouds_clean.ass"
ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

out_title = brain / "perfect_blue_7clouds_title.png"
out_chorus = brain / "perfect_blue_7clouds_chorus.png"

# Filter complex with 7clouds smooth subtle zoompan
fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=4:allf=t+u[v]"
)

# Render short 5-second clip to get title frame at 4.0s
subprocess.run([
    "ffmpeg", "-y",
    "-loop", "1", "-t", "6",
    "-i", str(master_twilight_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-ss", "4.0",
    "-vframes", "1",
    str(out_title)
], check=True)
print(f"Rendered Title audit: {out_title}")

# Render short clip for chorus at 48.0s
# To get exact timestamp, start loop from 0 to 52s, extract at 49.0s
subprocess.run([
    "ffmpeg", "-y",
    "-loop", "1", "-t", "52",
    "-i", str(master_twilight_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-ss", "49.0",
    "-vframes", "1",
    str(out_chorus)
], check=True)
print(f"Rendered Chorus audit: {out_chorus}")
