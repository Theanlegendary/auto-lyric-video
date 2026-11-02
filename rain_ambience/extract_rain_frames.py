import subprocess
from pathlib import Path
from PIL import Image

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
videos_dir = base / "videos"

samples = [
    ("bedroom", videos_dir / "rain_bedroom_1min_loop_sample.mp4"),
    ("coffeeshop", videos_dir / "rain_coffeeshop_1min_loop_sample.mp4"),
    ("cabin", videos_dir / "rain_cabin_1min_loop_sample.mp4"),
]

for label, v_path in samples:
    out = brain / f"rain_{label}_frame.png"
    crop = brain / f"crop_rain_{label}_frame.png"
    cmd = [
        "ffmpeg", "-y",
        "-ss", "00:00:15",
        "-i", str(v_path),
        "-vframes", "1",
        str(out)
    ]
    subprocess.run(cmd, capture_output=True)
    if out.exists():
        im = Image.open(out)
        # Crop center 1400x700
        crop_im = im.crop((260, 190, 1660, 890))
        crop_im.save(crop)
        print(f"Extracted {out.name} and {crop.name}")
