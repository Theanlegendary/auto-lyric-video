import os
import sys
import time
import subprocess
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

song_dir = base / "songs" / "28_yung_kai_blue"
bg_path = song_dir / "blue_7clouds_master.png"
audio_path = song_dir / "audio.mp3"
ass_path = song_dir / "lyrics_7clouds_clean.ass"
output_video = base / "videos" / "28_yung_kai_blue_Lyric_Video.mp4"

ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

duration = 214.61
t_out = 212.11

print("=" * 60)
print("RENDERING 7CLOUDS REMASTER: 28. yung kai - blue")
print(f"Background: {bg_path.name}")
print(f"ASS Subtitles: {ass_path.name}")
print(f"Output: {output_video.name}")
print("Formula: Aesthetic dawn sky wallpaper + subtle zoompan drift + crisp pure white text with dark outline & soft shadow (NO heavy overlays)")
print("=" * 60)

# 7clouds formula:
# Smooth slow zoompan on the scenic wallpaper itself, subtitles on top, subtle film grain
fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=4:allf=t+u,"
    f"fade=t=out:st={t_out}:d=2.5[v]"
)
af = f"afade=t=in:ss=0:d=1.5,afade=t=out:st={t_out}:d=2.5"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", str(duration), "-i", str(bg_path),
    "-i", str(audio_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-map", "1:a",
    "-af", af,
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "18",
    "-g", "50",
    "-keyint_min", "25",
    "-c:a", "aac",
    "-b:a", "320k",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    str(output_video)
]

t0 = time.time()
res = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
elapsed = time.time() - t0

if res.returncode != 0:
    print(f"RENDER FAILED with code {res.returncode}")
    print("\n".join(res.stderr.splitlines()[-30:]))
    sys.exit(1)

mb = output_video.stat().st_size / (1024 * 1024)
print(f"\n7CLOUDS MASTER RENDER COMPLETE in {elapsed:.1f}s ({mb:.2f} MB)")

# Extract audit frames from the rendered output video
audit_specs = [
    ("00:00:04.00", "audit_yungkai_7clouds_title.png", "Title Card: 'blue' / 'yung kai'"),
    ("00:00:21.00", "audit_yungkai_7clouds_verse.png", "Verse 1: 'Your morning eyes' / 'I could stare like watching stars'"),
    ("00:00:50.00", "audit_yungkai_7clouds_chorus.png", "Chorus: 'I think I'll picture us, you with the waves' / 'The ocean's colors on your face'"),
]

for ss, fname, label in audit_specs:
    out_img = brain / fname
    cmd_f = ["ffmpeg", "-y", "-ss", ss, "-i", str(output_video), "-vframes", "1", str(out_img)]
    subprocess.run(cmd_f, check=True)
    print(f"Extracted audit frame: {fname} at {ss} - {label}")

print("\nAll audit frames successfully extracted and saved to brain directory.")
