import os
import sys
import time
import subprocess
from pathlib import Path
from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

song_dir = base / "songs" / "25_The_Neighbourhood_Sweater_Weather"
bg_path = song_dir / "sweater_weather_color_clouds_blurred.png"
cloud_path = base / "seamless_color_clouds_3840.png"
audio_path = song_dir / "audio_sweater_weather_slowed_reverb.mp3"
ass_path = song_dir / "lyrics_slowed_reverb.ass"
output_video = base / "videos" / "25_The_Neighbourhood_Sweater_Weather_Slowed_Reverb_Lyric_Video.mp4"

ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

duration = 275.04
t_out = 272.54

print(f"============================================================")
print(f"RENDERING FULL MASTER VIDEO: 25. Sweater Weather (Slowed + Reverb Brand Edition)")
print(f"Audio Duration: {duration}s | Fade out: {t_out}s")
print(f"Background: {bg_path.name}")
print(f"Cloud Texture: {cloud_path.name} (Seamless Looping Drift)")
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
print(f"\nRENDER SUCCESSFUL in {elapsed:.1f}s ({mb:.2f} MB)")

# Extract audit frames directly from master
audit_specs = [
    ("00:00:03.50", "audit_sweater_slowed_full_title.png", "Title Card (200pt Patrick Hand Hook)"),
    ("00:00:21.00", "audit_sweater_slowed_full_verse1.png", "Verse 1 Couplet (In California)"),
    ("00:00:28.00", "audit_sweater_slowed_full_adventure.png", "Verse Couplet (Sleeves of My Sweater)"),
    ("00:01:15.00", "audit_sweater_slowed_full_chorus.png", "Chorus Couplet (Both Your Hands)"),
    ("00:01:31.00", "audit_sweater_slowed_full_bridge.png", "Bridge Couplet (Goosebumps / Left Hand)"),
    ("00:02:44.00", "audit_sweater_slowed_full_title_mid.png", "Mid-Song Hook Title Break (200pt)"),
    ("00:04:20.00", "audit_sweater_slowed_full_outro.png", "Outro Couplet (Holes of My Sweater)"),
]

print(f"\n--- Extracting and Analyzing Final Audit Frames ---")
for ss, fname, label in audit_specs:
    out_img = brain / fname
    cmd_f = ["ffmpeg", "-y", "-ss", ss, "-i", str(output_video), "-vframes", "1", str(out_img)]
    subprocess.run(cmd_f, check=True)
    
    img = Image.open(out_img).convert("RGB")
    arr = np.array(img)
    white_core = (arr[:, :, 0] > 240) & (arr[:, :, 1] > 240) & (arr[:, :, 2] > 240)
    glow_halo = (arr[:, :, 0] > 170) & (arr[:, :, 1] > 170) & (arr[:, :, 2] > 170) & (~white_core)
    text_mask = (arr[:, :, 0] > 180) | (arr[:, :, 1] > 180) | (arr[:, :, 2] > 180)
    y_idx, x_idx = np.where(text_mask)
    
    if len(x_idx) > 0:
        min_x = int(np.min(x_idx))
        max_x = int(np.max(x_idx))
        left_m = min_x
        right_m = 1920 - max_x
        width = max_x - min_x
    else:
        left_m, right_m, width = 0, 0, 0
        
    core_pct = np.mean(white_core) * 100
    halo_pct = np.mean(glow_halo) * 100
    
    print(f"\n[{fname}] ({label})")
    print(f"  Timestamp: {ss}")
    print(f"  Pure White Core: {core_pct:.2f}% | Starlight Halo Glow: {halo_pct:.2f}%")
    print(f"  Margins: Left {left_m}px | Right {right_m}px | Width {width}px")
    print(f"  Margin Verification: {'PASS (>=170px)' if min(left_m, right_m) >= 170 else 'CHECK'}")
