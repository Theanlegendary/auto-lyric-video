import cv2
import numpy as np
import subprocess
import wave
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
rain_dir = base / "rain_ambience"
videos_dir = base / "videos"

bg_path = brain / "cozy_rain_porch_wallpaper_1793589475079.jpg"
ref_audio_path = brain / "danny_louis_audio.wav"
out_audio_path = rain_dir / "tin_roof_rain_thunder_60s_loop.wav"
out_video = videos_dir / "tin_roof_rain_forest_danny_louis_style.mp4"

print("=" * 70)
print("BUILDING DANNY LOUIS 70M-VIEW REPLICA MASTER (1080p • 60s)")
print("Style: Tin Roof Eaves Overhang + Cascading Streams + Murky Foggy Rainforest")
print("=" * 70)

# 1. BUILD 60-SECOND SEAMLESS AUDIO LOOP FROM AUTHENTIC TIN ROOF AUDIO
with wave.open(str(ref_audio_path), 'rb') as wf:
    sr = wf.getframerate()
    ch = wf.getnchannels()
    n_frames = wf.getnframes()
    raw = wf.readframes(n_frames)
    audio = np.frombuffer(raw, dtype=np.int16).reshape(-1, ch).T # shape: (2, N)

# Loop to 68 seconds with equal-power crossfade
target_len = int(60.0 * sr)
fade_len = int(4.0 * sr)
ext_len = target_len + fade_len

# Repeat audio to cover ext_len
n_repeats = (ext_len // n_frames) + 2
tiled = np.tile(audio, (1, n_repeats))[:, :ext_len]

# Apply equal-power crossfade from [target_len, ext_len] into [0, fade_len]
main_a = tiled[:, :target_len].astype(np.float32)
tail_a = tiled[:, target_len:ext_len].astype(np.float32)
t_fade = np.linspace(0, 1, fade_len)
fade_in = np.sin(t_fade * np.pi / 2)
fade_out = np.cos(t_fade * np.pi / 2)
main_a[:, :fade_len] = main_a[:, :fade_len] * fade_in + tail_a * fade_out

# Save 60s loop WAV
main_a = np.clip(main_a, -32767, 32767).astype(np.int16)
interleaved = np.empty((main_a.shape[1] * 2,), dtype=np.int16)
interleaved[0::2] = main_a[0]
interleaved[1::2] = main_a[1]
with wave.open(str(out_audio_path), 'wb') as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sr)
    wf.writeframes(interleaved.tobytes())
print(f"Generated 60s Tin Roof Audio Loop: {out_audio_path.name}")

# 2. VIDEO RENDERING WITH ROOF EAVES CASCADING WATER STREAMS
bg_img = cv2.imread(str(bg_path))
bg_base = cv2.resize(bg_img, (1920, 1080), interpolation=cv2.INTER_LANCZOS4)

fps = 25
total_frames = int(fps * 60.0)
width, height = 1920, 1080

# Rain in forest (starts BELOW the roof, so rain does NOT fall on the roof/inside shelter!)
# Roof occupies roughly the top 220px of the frame.
roof_bottom_y = 210

np.random.seed(88)
n_drops = 350
# Rain falls in the open air from Y=roof_bottom_y downwards!
rain_x = np.random.uniform(0, width, n_drops)
rain_y = np.random.uniform(roof_bottom_y, height, n_drops)
rain_speed = np.random.uniform(25, 48, n_drops)
rain_len = rain_speed * 1.3
rain_alpha = np.random.uniform(0.15, 0.40, n_drops)

# Cascading water streams dripping off the corrugated roof ridges (15 distinct drip points)
# Points along the roof edge:
drip_x_points = np.linspace(80, width - 80, 24)
n_drips = len(drip_x_points)

cmd = [
    "ffmpeg", "-y",
    "-f", "rawvideo",
    "-vcodec", "rawvideo",
    "-s", f"{width}x{height}",
    "-pix_fmt", "bgr24",
    "-r", str(fps),
    "-i", "-",
    "-i", str(out_audio_path),
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "18",
    "-g", "50",
    "-keyint_min", "25",
    "-c:a", "aac",
    "-b:a", "320k",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    "-t", "60.0",
    str(out_video)
]

proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
t0 = time.time()

for f in range(total_frames):
    t_sec = f / fps

    # Subtle slow camera drift
    zoom = 1.0 + 0.015 * (f / total_frames)
    new_w = int(width / zoom)
    new_h = int(height / zoom)
    x1 = (width - new_w) // 2
    y1 = (height - new_h) // 2
    frame = cv2.resize(bg_base[y1:y1+new_h, x1:x1+new_w], (width, height), interpolation=cv2.INTER_LINEAR)

    overlay = np.zeros_like(frame)

    # 1. Falling rain streaks (strictly OUTSIDE below the roof edge)
    for i in range(n_drops):
        y_start = rain_y[i]
        x_start = rain_x[i]
        y_end = y_start + rain_len[i]
        x_end = x_start + rain_len[i] * 0.12

        c = int(255 * rain_alpha[i])
        cv2.line(overlay, (int(x_start), int(y_start)), (int(x_end), int(y_end)), (c, c, c), 1, cv2.LINE_AA)

        rain_y[i] += rain_speed[i]
        rain_x[i] += rain_speed[i] * 0.12
        if rain_y[i] > height:
            rain_y[i] = roof_bottom_y + np.random.uniform(0, 50)
            rain_x[i] = np.random.uniform(0, width)

    # 2. Water cascading and dripping off the tin roof edge
    for idx, dx in enumerate(drip_x_points):
        # Varying cycle for each drip stream
        cycle_t = (t_sec * 3.5 + idx * 0.7) % 1.0
        # Continuous thin stream from roof edge (Y: 200 to 250)
        cv2.line(overlay, (int(dx), 195), (int(dx), 245), (140, 160, 180), 1, cv2.LINE_AA)
        # Big falling drop detachment
        drop_fall_y = 245 + cycle_t * 500
        drop_fall_x = dx + cycle_t * 20
        if drop_fall_y < height:
            cv2.circle(overlay, (int(drop_fall_x), int(drop_fall_y)), 3, (210, 230, 255), -1, cv2.LINE_AA)

    # Blend overlay onto outdoor region
    frame = cv2.add(frame, overlay)

    proc.stdin.write(frame.tobytes())

proc.stdin.close()
stdout, stderr = proc.communicate()
dt = time.time() - t0

if proc.returncode == 0 and out_video.exists():
    sz = out_video.stat().st_size / (1024 * 1024)
    print("=" * 70)
    print(f"SUCCESS: Rendered {out_video.name} in {dt:.1f}s | Size: {sz:.2f} MB")
    print("=" * 70)
else:
    print(f"ERROR:\n{stderr.decode('utf-8', errors='ignore')[-500:]}")
