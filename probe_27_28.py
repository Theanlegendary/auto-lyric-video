import subprocess
from pathlib import Path

v_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos")
videos = [
    "27_Joji_Glimpse_of_Us_Lyric_Video.mp4",
    "27_Joji_Glimpse_of_Us_Slowed_Reverb_Lyric_Video.mp4",
    "28_yung_kai_blue_Lyric_Video.mp4",
    "28_yung_kai_blue_Slowed_Reverb_Lyric_Video.mp4"
]

for vname in videos:
    p = v_dir / vname
    if p.exists():
        mb = p.stat().st_size / (1024 * 1024)
        print(f"File: {vname} ({mb:.2f} MB)")
        res = subprocess.run(["ffmpeg", "-i", str(p)], capture_output=True, text=True, errors="ignore")
        for line in res.stderr.splitlines():
            if "Duration:" in line or "Stream #0:0" in line:
                print(" ", line.strip())
    else:
        print(f"Missing: {vname}")
