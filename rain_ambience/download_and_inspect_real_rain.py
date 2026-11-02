import urllib.request
import subprocess
from pathlib import Path
from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

out_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips")
out_dir.mkdir(parents=True, exist_ok=True)
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

urls = [
    ("clip_roof_rain_5210318.mp4", "https://videos.pexels.com/video-files/5210318/5210318-hd_1920_1080_24fps.mp4"),
    ("clip_nature_rain_4779387.mp4", "https://videos.pexels.com/video-files/4779387/4779387-hd_1920_1080_30fps.mp4"),
    ("clip_forest_rain_4112834.mp4", "https://videos.pexels.com/video-files/4112834/4112834-hd_1920_1080_30fps.mp4"),
]

for name, url in urls:
    dest = out_dir / name
    if not dest.exists():
        print(f"Downloading {name}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        print(f"  Downloaded {name}: {dest.stat().st_size / 1024 / 1024:.2f} MB")
    else:
        print(f"  Already exists: {name}")

    # Extract test frame
    frame_path = brain / f"real_{dest.stem}_frame.png"
    subprocess.run(["ffmpeg", "-y", "-ss", "00:00:03", "-i", str(dest), "-vframes", "1", str(frame_path)], capture_output=True)
    if frame_path.exists():
        im = Image.open(frame_path)
        print(f"  Frame extracted: {frame_path.name} {im.size}")
