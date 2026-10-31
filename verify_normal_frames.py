import subprocess
from pathlib import Path

video = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4")
out_dir = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

timestamps = [
    ("normal_title", "00:00:03.000"),
    ("normal_verse", "00:00:18.000"),
    ("normal_chorus", "00:01:04.000")
]

for name, ts in timestamps:
    out_file = out_dir / f"audit_verify_{name}.png"
    cmd = [
        "ffmpeg", "-y", "-ss", ts, "-i", str(video),
        "-frames:v", "1", str(out_file)
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"Extracted {name}: {out_file.name} ({out_file.stat().st_size} bytes)")
