import os
import sys
import time
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
rain_dir = base / "rain_ambience"
videos_dir = base / "videos"

samples = [
    {
        "id": "bedroom",
        "title": "Cozy Bedroom Rain & Distant Thunder",
        "bg": brain / "cozy_anime_bedroom_wallpaper_1793588427416.jpg",
        "audio": rain_dir / "rain_bedroom_loop.wav",
        "video": videos_dir / "rain_bedroom_1min_loop_sample.mp4",
        "tag": "Cozy Bedroom • Rain on Glass & Distant Thunder"
    },
    {
        "id": "coffeeshop",
        "title": "Late Night Tokyo Cafe Rainy Window",
        "bg": brain / "cozy_tokyo_cafe_rainy_night_1793588431156.jpg",
        "audio": rain_dir / "rain_coffeeshop_loop.wav",
        "video": videos_dir / "rain_coffeeshop_1min_loop_sample.mp4",
        "tag": "Tokyo Coffee Shop • Rain on Glass & Neon Bokeh"
    },
    {
        "id": "cabin",
        "title": "Forest Wooden Cabin & Fireplace Rain",
        "bg": brain / "cozy_rainy_cabin_wallpaper_1793588440503.jpg",
        "audio": rain_dir / "rain_cabin_loop.wav",
        "video": videos_dir / "rain_cabin_1min_loop_sample.mp4",
        "tag": "Forest Cabin • Rain on Tin Roof & Crackling Fire"
    }
]

duration = 60.0

for s in samples:
    print("=" * 70)
    print(f"RENDERING 1-MIN RAIN SAMPLE: {s['title']}")
    print(f"Background: {s['bg'].name}")
    print(f"Audio Loop: {s['audio'].name}")
    print(f"Output: {s['video'].name}")
    print("=" * 70)
    t0 = time.time()

    # Smooth subtle drone camera drift: slow zoom in from 1.00 to 1.03 over 60s
    fc = (
        f"[0:v]format=yuv420p,"
        f"scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
        f"zoompan=z='min(zoom+0.00004,1.03)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
        f"noise=alls=3:allf=t+u[v]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", str(duration), "-i", str(s["bg"]),
        "-i", str(s["audio"]),
        "-filter_complex", fc,
        "-map", "[v]",
        "-map", "1:a",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-g", "50",
        "-keyint_min", "25",
        "-c:a", "aac",
        "-b:a", "320k",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        str(s["video"])
    ]

    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    dt = time.time() - t0
    if res.returncode == 0 and s["video"].exists():
        sz = s["video"].stat().st_size / (1024 * 1024)
        print(f"  [SUCCESS] Rendered {s['video'].name} in {dt:.1f}s | Size: {sz:.2f} MB\n")
    else:
        print(f"  [ERROR] Render failed:\n{res.stderr[-400:]}\n")

print("All 3 rain samples rendered successfully!")
