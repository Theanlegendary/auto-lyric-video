import cv2
import numpy as np
import subprocess
import os
import math

def main():
    bg_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail\nature_options\kyoto_edo_darker_level_b.jpg"
    audio_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\tin_roof_rain_thunder_60s_loop.wav"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    os.makedirs(out_dir, exist_ok=True)
    
    temp_avi = os.path.join(out_dir, "temp_kyoto_raw.mp4")
    final_mp4 = os.path.join(out_dir, "kyoto_edo_tea_house_rain_living_loop_1min.mp4")

    img = cv2.imread(bg_path)
    h, w = img.shape[:2]
    fps = 30.0
    
    # 15s forward, then reverse for 30s ping-pong, loop twice = 60s
    num_fwd = int(15.0 * fps) # 450 frames

    # Generate 120 falling rain streaks with random depth and speed
    np.random.seed(99)
    num_streaks = 140
    streaks = []
    for _ in range(num_streaks):
        streaks.append({
            'x': np.random.uniform(0, w),
            'y': np.random.uniform(-h, h),
            'speed': np.random.uniform(22, 45),
            'len': np.random.uniform(25, 60),
            'thick': np.random.choice([1, 1, 2]),
            'alpha': np.random.uniform(0.15, 0.45)
        })

    # Lantern position in image (around x=740, y=650 in 1920x1080)
    # Let's find exact coordinates
    lx, ly = int(w * 0.385), int(h * 0.60) # around the lantern

    # Pre-render 450 forward frames
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(temp_avi, fourcc, fps, (w, h))

    print("Generating Kyoto Tea House living rain animation (15s forward)...")
    fwd_frames = []
    for i in range(num_fwd):
        t = i / fps
        # Slow organic camera zoom (1.000 to 1.035)
        scale = 1.0 + 0.035 * (0.5 - 0.5 * math.cos(math.pi * i / num_fwd))
        nw, nh = int(w * scale), int(h * scale)
        # Center slightly toward the tea house (around x=0.6, y=0.5)
        scaled = cv2.resize(img, (nw, nh), interpolation=cv2.INTER_LINEAR)
        
        cx = int((nw - w) * 0.62)
        cy = int((nh - h) * 0.52)
        frame = scaled[cy:cy+h, cx:cx+w].copy()

        # Animate falling rain streaks
        rain_overlay = np.zeros_like(frame)
        for s in streaks:
            cur_y = (s['y'] + s['speed'] * i) % (h + 100) - 50
            cur_x = (s['x'] + 0.25 * cur_y) % w # slight wind angle
            
            pt1 = (int(cur_x), int(cur_y))
            pt2 = (int(cur_x + s['len'] * 0.22), int(cur_y + s['len']))
            
            b = int(220 * s['alpha'])
            g = int(235 * s['alpha'])
            r = int(245 * s['alpha'])
            cv2.line(rain_overlay, pt1, pt2, (b, g, r), s['thick'], cv2.LINE_AA)

        # Subtle warm breathing lantern pulse
        pulse = 0.85 + 0.15 * math.sin(2.0 * math.pi * t * 0.5)
        # Draw soft amber glow on the lantern
        cv2.circle(rain_overlay, (lx, ly), int(35), (20, 90, 140), -1) # subtle warm glow
        cv2.GaussianBlur(rain_overlay, (3, 3), 0, dst=rain_overlay)

        # Composite rain
        composite = cv2.add(frame, rain_overlay)
        fwd_frames.append(composite)

    print("Writing 60-second seamless ping-pong loop (forward + reverse x 2)...")
    # 15s forward + 15s reverse + 15s forward + 15s reverse = 60.0 seconds
    for _ in range(2):
        for f in fwd_frames:
            writer.write(f)
        for f in reversed(fwd_frames):
            writer.write(f)

    writer.release()
    print("Raw video written. Muxing audio & optimizing with FFmpeg...")

    cmd_ffmpeg = [
        "ffmpeg", "-y",
        "-i", temp_avi,
        "-i", audio_path,
        "-c:v", "libx264", "-preset", "medium", "-crf", "22",
        "-maxrate", "1100k", "-bufsize", "2200k",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k",
        "-t", "60.0",
        "-movflags", "+faststart",
        final_mp4
    ]
    p = subprocess.run(cmd_ffmpeg, capture_output=True, text=True)
    if os.path.exists(temp_avi):
        os.remove(temp_avi)
        
    if p.returncode == 0:
        sz = os.path.getsize(final_mp4)
        print(f"SUCCESS! Kyoto Tea House Living Rain Video Ready: {final_mp4} ({sz/(1024*1024):.2f} MB)")
    else:
        print("FFmpeg error:", p.stderr[-400:])

if __name__ == "__main__":
    main()
