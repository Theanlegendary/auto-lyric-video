import subprocess
import time
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
bg_path = base / "stock_anime_bgs" / "14_anime_clear_pink_aesthetic_twilight_sky.png"
out_test = base / "test_official_motion.mp4"

# In zoompan:
# z='min(zoom+0.0002, 1.08)' -> slow 8% push-in over time
# x and y center the zoom
# d=1 means calculate per frame
fc = "zoompan=z='min(zoom+0.0002,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30,noise=c0s=16:c0f=t+u[v]"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-framerate", "30", "-t", "8",
    "-i", str(bg_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-c:v", "libx264", "-preset", "faster", "-pix_fmt", "yuv420p",
    str(out_test)
]

print("Running 8-second test...")
t0 = time.time()
subprocess.run(cmd, check=True)
print(f"Test finished in {time.time() - t0:.2f}s! File size: {out_test.stat().st_size} bytes")
