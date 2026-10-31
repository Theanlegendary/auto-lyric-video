import os
import sys
import time
import subprocess
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

song_dir = base / "songs" / "27_Joji_Glimpse_of_Us"
bg_path = song_dir / "glimpse_of_us_blurred_master.png"
cloud_path = base / "seamless_color_clouds_3840.png"
audio_path = song_dir / "audio_glimpse_of_us_slowed_reverb.mp3"
ass_path = song_dir / "lyrics_slowed_reverb.ass"
output_video = base / "videos" / "27_Joji_Glimpse_of_Us_Slowed_Reverb_Lyric_Video.mp4"

ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

duration = 270.73
t_out = 268.23

print(f"============================================================")
print(f"RENDERING FULL MASTER VIDEO: 27. Joji - Glimpse of Us (Slowed + Reverb Brand Edition)")
print(f"Audio Duration: {duration}s | Fade out: {t_out}s")
print(f"Background: {bg_path.name}")
print(f"ASS file: {ass_path.name}")
print(f"Output: {output_video.name}")
print(f"============================================================")

fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25[bg_pan];"
    f"[1:v]format=rgba[c_layer];"
    f"[bg_pan][c_layer]overlay=x='-mod(t*12, 1920)':y=15:format=auto,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=5:allf=t+u,"
    f"fade=t=out:st={t_out}:d=2.5[v]"
)
af = f"afade=t=in:ss=0:d=1.5,afade=t=out:st={t_out}:d=2.5"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", str(duration), "-i", str(bg_path),
    "-loop", "1", "-t", str(duration), "-i", str(cloud_path),
    "-i", str(audio_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-map", "2:a",
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
print(f"\nSLOWED + REVERB MASTER RENDER SUCCESSFUL in {elapsed:.1f}s ({mb:.2f} MB)")

# Extract audit frames
audit_specs = [
    ("00:00:04.50", "audit_joji_slowed_title.png", "Title Card (200pt Patrick Hand Hook)"),
    ("00:00:23.00", "audit_joji_slowed_verse1.png", "Verse 1 Couplet (World Off My Shoulders)"),
    ("00:01:12.00", "audit_joji_slowed_chorus.png", "Chorus Couplet (Glimpse of Us)"),
]

for ss, fname, label in audit_specs:
    out_img = brain / fname
    cmd_f = ["ffmpeg", "-y", "-ss", ss, "-i", str(output_video), "-vframes", "1", str(out_img)]
    subprocess.run(cmd_f, check=True)
    print(f"Extracted {fname} at {ss}")
