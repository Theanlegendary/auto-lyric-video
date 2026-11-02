import cv2
import numpy as np
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
rain_dir = base / "rain_ambience"
videos_dir = base / "videos"

bg_path = brain / "cozy_rainy_cabin_forest_wallpaper_1793588838085.jpg"
audio_path = rain_dir / "light_rain_forest_thunder_loop.wav"
out_video = videos_dir / "cozy_forest_light_rain_thunder_animated_loop.mp4"

print("=" * 70)
print("RENDERING ANIMATED RAIN & THUNDER MASTER (1080p • 60s)")
print(f"Background: {bg_path.name}")
print(f"Audio Track: {audio_path.name}")
print(f"Target Output: {out_video.name}")
print("=" * 70)

# Load and resize background to 1920x1080
bg_img = cv2.imread(str(bg_path))
if bg_img is None:
    raise FileNotFoundError(f"Could not load image {bg_path}")
bg_base = cv2.resize(bg_img, (1920, 1080), interpolation=cv2.INTER_LANCZOS4)

# Parameters
fps = 25
duration = 60.0
total_frames = int(fps * duration)
width, height = 1920, 1080

# Initialize Falling Rain particles (slanted streaks)
# Parallax: 3 depth layers
np.random.seed(42)
n_drops = 450
rain_x = np.random.uniform(-100, width + 100, n_drops)
rain_y = np.random.uniform(0, height, n_drops)
# Speed in pixels per frame: 25 to 55 px/frame (approx 625 to 1375 px/sec)
rain_speed = np.random.uniform(28, 52, n_drops)
rain_len = rain_speed * 1.4 # streak length proportional to speed
rain_alpha = np.random.uniform(0.18, 0.45, n_drops)
# Wind slant angle: dx/dy = 0.15 (falling slightly to the right)
rain_slant = 0.14

# Initialize Sliding Window Glass Droplets
n_window_drops = 90
win_x = np.random.uniform(80, width - 80, n_window_drops)
win_y = np.random.uniform(50, height - 50, n_window_drops)
win_radius = np.random.uniform(2.0, 5.0, n_window_drops)
# Some drops are stationary, 20% slowly slide down
is_sliding = np.random.rand(n_window_drops) < 0.22
slide_speed = np.random.uniform(1.2, 3.5, n_window_drops)

# FFmpeg Pipe setup for encoding
cmd = [
    "ffmpeg", "-y",
    "-f", "rawvideo",
    "-vcodec", "rawvideo",
    "-s", f"{width}x{height}",
    "-pix_fmt", "bgr24",
    "-r", str(fps),
    "-i", "-", # Pipe stdin
    "-i", str(audio_path),
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "18",
    "-g", "50",
    "-keyint_min", "25",
    "-c:a", "aac",
    "-b:a", "320k",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    "-t", str(duration),
    str(out_video)
]

proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

t0 = time.time()
print("Compositing animated rain, water droplets & distant lightning swells...")

for f in range(total_frames):
    t_sec = f / fps

    # 1. Subtle camera drift (gentle breathing zoom from 1.000 to 1.020)
    zoom = 1.0 + 0.020 * (f / total_frames)
    new_w = int(width / zoom)
    new_h = int(height / zoom)
    x1 = (width - new_w) // 2
    y1 = (height - new_h) // 2
    crop_bg = bg_base[y1:y1+new_h, x1:x1+new_w]
    frame = cv2.resize(crop_bg, (width, height), interpolation=cv2.INTER_LINEAR)

    # 2. Distant Lightning Swell (subtle cloud flash at t=15.5s and t=43.5s)
    # Flash 1 (peaks at 15.6s)
    f_flash1 = np.exp(-((t_sec - 15.6) ** 2) / 0.06)
    # Flash 2 (peaks at 43.6s)
    f_flash2 = np.exp(-((t_sec - 43.6) ** 2) / 0.08)
    total_flash = f_flash1 * 0.16 + f_flash2 * 0.18
    if total_flash > 0.01:
        frame = cv2.addWeighted(frame, 1.0, np.full_like(frame, 255), total_flash, 0)

    # 3. Create transparent rain overlay
    rain_overlay = np.zeros_like(frame)

    # Update falling rain
    for i in range(n_drops):
        y_start = rain_y[i]
        x_start = rain_x[i]
        y_end = y_start + rain_len[i]
        x_end = x_start + rain_len[i] * rain_slant
        
        c = int(255 * rain_alpha[i])
        cv2.line(rain_overlay, (int(x_start), int(y_start)), (int(x_end), int(y_end)), (c, c, c), 1, cv2.LINE_AA)

        # Move drop down
        rain_y[i] += rain_speed[i]
        rain_x[i] += rain_speed[i] * rain_slant
        # Wrap around periodically
        if rain_y[i] > height:
            rain_y[i] -= height
            rain_x[i] = np.random.uniform(-50, width + 50)

    # Update window droplets
    for j in range(n_window_drops):
        wx = int(win_x[j])
        wy = int(win_y[j])
        r = int(win_radius[j])
        # Draw translucent droplet: dark refraction rim + bright white specular dot
        cv2.circle(rain_overlay, (wx, wy), r, (120, 130, 140), -1, cv2.LINE_AA)
        cv2.circle(rain_overlay, (wx - 1, wy - 1), max(1, r - 2), (230, 240, 255), -1, cv2.LINE_AA)

        if is_sliding[j]:
            win_y[j] += slide_speed[j]
            # Leave tiny water trail behind sliding drop
            cv2.line(rain_overlay, (wx, max(0, wy - 12)), (wx, wy), (90, 100, 110), 1, cv2.LINE_AA)
            if win_y[j] > height - 30:
                win_y[j] = np.random.uniform(50, 200)
                win_x[j] = np.random.uniform(80, width - 80)

    # 4. Blend rain overlay onto frame using screen/add blend mode
    frame = cv2.add(frame, rain_overlay)

    # Pipe frame to FFmpeg
    proc.stdin.write(frame.tobytes())

    if (f + 1) % 250 == 0 or f == total_frames - 1:
        pct = (f + 1) / total_frames * 100
        print(f"  Progress: {pct:5.1f}% ({f+1}/{total_frames} frames)")

proc.stdin.close()
stdout, stderr = proc.communicate()
dt = time.time() - t0

if proc.returncode == 0 and out_video.exists():
    sz = out_video.stat().st_size / (1024 * 1024)
    print("=" * 70)
    print(f"SUCCESS: Rendered {out_video.name} in {dt:.1f}s | Size: {sz:.2f} MB")
    print("=" * 70)
else:
    print(f"ERROR: Encoding failed:\n{stderr.decode('utf-8', errors='ignore')[-500:]}")
