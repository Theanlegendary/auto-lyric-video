import cv2
import numpy as np
import subprocess
import os
import math
import sys

def main():
    clip_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_9934612_flooded_forest_rain.mp4"
    audio_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\tin_roof_rain_thunder_60s_loop.wav"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    temp_raw_avi = os.path.join(out_dir, "temp_fireflies_raw.mp4")
    final_mp4 = os.path.join(out_dir, "magical_fireflies_rain_forest_night_sample.mp4")

    cap = cv2.VideoCapture(clip_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # We will render 15 seconds forward, then reverse for seamless loop (total 30s)
    num_fwd_frames = int(15.0 * fps)
    
    # Pre-read 15s of frames
    raw_frames = []
    for _ in range(num_fwd_frames):
        ret, frame = cap.read()
        if not ret:
            break
        raw_frames.append(frame)
    cap.release()

    if len(raw_frames) < num_fwd_frames:
        num_fwd_frames = len(raw_frames)

    print(f"Read {num_fwd_frames} frames ({num_fwd_frames/fps:.1f}s) at {w}x{h} @ {fps:.1f} fps")

    # Initialize 45 fireflies with realistic physics
    np.random.seed(42)
    num_ff = 45
    
    colors = [
        np.array([40, 220, 255], dtype=np.float32),  # Golden Amber
        np.array([60, 255, 190], dtype=np.float32),  # Warm Lime
        np.array([120, 255, 150], dtype=np.float32), # Emerald
        np.array([50, 240, 255], dtype=np.float32),  # Warm Sun
    ]
    
    fireflies = []
    for i in range(num_ff):
        base_x = np.random.uniform(w * 0.05, w * 0.95)
        base_y = np.random.uniform(h * 0.25, h * 0.88)
        depth = np.random.uniform(0.35, 1.0)
        core_r = int(2 + 3 * depth)
        halo_r = int(14 + 22 * depth)
        color = colors[i % len(colors)]
        
        # Drift parameters (different frequencies for natural motion)
        freq_x1 = np.random.uniform(0.3, 0.8)
        freq_x2 = np.random.uniform(0.8, 1.5)
        amp_x = np.random.uniform(15, 45) * depth
        
        freq_y1 = np.random.uniform(0.4, 0.9)
        amp_y = np.random.uniform(10, 30) * depth
        
        pulse_freq = np.random.uniform(1.2, 2.5)
        pulse_phase = np.random.uniform(0, 2 * math.pi)
        
        fireflies.append({
            'base_x': base_x, 'base_y': base_y, 'depth': depth,
            'core_r': core_r, 'halo_r': halo_r, 'color': color,
            'freq_x1': freq_x1, 'freq_x2': freq_x2, 'amp_x': amp_x,
            'freq_y1': freq_y1, 'amp_y': amp_y,
            'pulse_freq': pulse_freq, 'pulse_phase': pulse_phase
        })

    # Prepare VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(temp_raw_avi, fourcc, fps, (w, h))

    # Precalculate vignette mask
    Y_grid, X_grid = np.ogrid[:h, :w]
    max_d = np.sqrt((w/2)**2 + (h/2)**2)
    dist = np.sqrt((X_grid - w/2)**2 + (Y_grid - h/2)**2)
    vignette = (1.0 - 0.32 * (dist / max_d)**2)[:, :, np.newaxis]

    processed_frames = []

    print("Processing forward frames with night grade and firefly simulation...")
    for idx, frame in enumerate(raw_frames):
        t = idx / fps
        
        # 1. Apply night color grade
        # colorchannelmixer: rr=0.38, gg=0.45, bb=0.95
        b, g, r = cv2.split(frame.astype(np.float32) / 255.0)
        r_out = 0.38*r + 0.08*g
        g_out = 0.05*r + 0.45*g + 0.20*b
        b_out = 0.10*r + 0.25*g + 0.95*b
        merged = cv2.merge([b_out, g_out, r_out])
        
        # Contrast & brightness
        graded = np.clip((merged - 0.5) * 1.28 + 0.5 - 0.06, 0.0, 1.0) * 255.0
        graded = graded * vignette

        # 2. Firefly glow layer
        glow_layer = np.zeros((h, w, 3), dtype=np.float32)

        for ff in fireflies:
            # Calculate organic position at time t
            cur_x = int(ff['base_x'] + ff['amp_x'] * math.sin(ff['freq_x1'] * t) + (ff['amp_x'] * 0.4) * math.cos(ff['freq_x2'] * t))
            cur_y = int(ff['base_y'] + ff['amp_y'] * math.sin(ff['freq_y1'] * t))
            
            # Pulse intensity between 0.15 and 1.0
            pulse = 0.55 + 0.45 * math.sin(ff['pulse_freq'] * t + ff['pulse_phase'])
            intensity = pulse * ff['depth']
            
            hr = ff['halo_r']
            cr = ff['core_r']
            col = ff['color']
            
            y_min = max(0, cur_y - hr)
            y_max = min(h, cur_y + hr)
            x_min = max(0, cur_x - hr)
            x_max = min(w, cur_x + hr)
            
            if y_max <= y_min or x_max <= x_min:
                continue
                
            GY, GX = np.ogrid[y_min-cur_y:y_max-cur_y, x_min-cur_x:x_max-cur_x]
            d_sq = GX*GX + GY*GY
            
            halo = np.exp(-d_sq / (2.0 * (hr * 0.38)**2)) * 0.60 * intensity
            core = np.exp(-d_sq / (2.0 * (cr * 0.75)**2)) * 1.10 * intensity
            glow = (halo + core)[:, :, np.newaxis]
            
            glow_layer[y_min:y_max, x_min:x_max] += glow * col
            
            # Subtle water reflection if in lower half
            if cur_y > h * 0.62:
                refl_y = cur_y + int(25 * ff['depth'])
                if refl_y < h:
                    ry_min = max(0, refl_y - hr // 2)
                    ry_max = min(h, refl_y + hr // 2)
                    rx_min = max(0, cur_x - hr)
                    rx_max = min(w, cur_x + hr)
                    if ry_max > ry_min and rx_max > rx_min:
                        RGY, RGX = np.ogrid[ry_min-refl_y:ry_max-refl_y, rx_min-cur_x:rx_max-cur_x]
                        r_dist = (RGX * 0.7)**2 + (RGY * 1.8)**2
                        r_glow = np.exp(-r_dist / (2.0 * (hr * 0.4)**2)) * 0.22 * intensity
                        glow_layer[ry_min:ry_max, rx_min:rx_max] += r_glow[:, :, np.newaxis] * col

        composite = np.clip(graded + glow_layer, 0, 255).astype(np.uint8)
        processed_frames.append(composite)

    print("Writing forward + reverse ping-pong loop (30 seconds total)...")
    # Write Forward
    for f in processed_frames:
        writer.write(f)
    # Write Reverse for 100% seamless continuity
    for f in reversed(processed_frames):
        writer.write(f)
        
    writer.release()
    print("Raw video written. Muxing audio & optimizing with FFmpeg...")

    # Mux with audio and encode to x264
    cmd_ffmpeg = [
        "ffmpeg", "-y",
        "-i", temp_raw_avi,
        "-i", audio_path,
        "-c:v", "libx264", "-preset", "medium", "-crf", "22",
        "-maxrate", "1100k", "-bufsize", "2200k",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k",
        "-t", "30.0",
        "-movflags", "+faststart",
        final_mp4
    ]
    p = subprocess.run(cmd_ffmpeg, capture_output=True, text=True)
    if os.path.exists(temp_raw_avi):
        os.remove(temp_raw_avi)
        
    if p.returncode == 0:
        sz = os.path.getsize(final_mp4)
        print(f"SUCCESS! Magical Firefly Rain Video Ready: {final_mp4} ({sz/(1024*1024):.2f} MB)")
    else:
        print("FFmpeg error:", p.stderr[-400:])

if __name__ == "__main__":
    main()
