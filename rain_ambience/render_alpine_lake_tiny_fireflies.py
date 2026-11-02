import cv2
import numpy as np
import subprocess
import os
import math

def main():
    in_video = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos\pure_nature_option1_alpine_lake_night_1min.mp4"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    temp_raw = os.path.join(out_dir, "temp_alpine_ff_raw.mp4")
    final_output = os.path.join(out_dir, "alpine_lake_night_tiny_fireflies_1min.mp4")

    cap = cv2.VideoCapture(in_video)
    fps = cap.get(cv2.CAP_PROP_FPS) or 29.97
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = total_frames / fps

    print(f"Input: {w}x{h} @ {fps:.2f}fps, {total_frames} frames ({duration:.2f}s)")

    # 4 Tiny Fireflies (3 to 5 total, subtle & delicate)
    # Colors: BGR format (warm golden amber, soft bioluminescent yellow-green)
    colors = [
        np.array([120, 235, 255], dtype=np.float32),  # Warm Golden Amber
        np.array([100, 255, 210], dtype=np.float32),  # Soft Bioluminescent Lime-Green
        np.array([80, 220, 255], dtype=np.float32),   # Deep Amber Gold
        np.array([130, 255, 180], dtype=np.float32),  # Delicate Forest Firefly Green
    ]

    # Carefully positioned over the lake shoreline & lower trees
    fireflies = [
        # FF 1: Left shoreline near pine branches
        {
            'base_x': w * 0.28, 'base_y': h * 0.58,
            'amp_x1': 45, 'k_x1': 2, 'amp_x2': 25, 'k_x2': 4,
            'amp_y1': 22, 'k_y1': 3, 'amp_y2': 14, 'k_y2': 1,
            'k_pulse': 16, 'pulse_phase': 0.0,
            'core_r': 1.6, 'halo_r': 6.5, 'color': colors[0], 'depth': 0.75
        },
        # FF 2: Center-left over the misty lake water
        {
            'base_x': w * 0.44, 'base_y': h * 0.68,
            'amp_x1': 55, 'k_x1': 1, 'amp_x2': 30, 'k_x2': 3,
            'amp_y1': 28, 'k_y1': 2, 'amp_y2': 15, 'k_y2': 4,
            'k_pulse': 14, 'pulse_phase': 1.5,
            'core_r': 1.8, 'halo_r': 7.5, 'color': colors[1], 'depth': 0.90
        },
        # FF 3: Right side near misty water & distant trees
        {
            'base_x': w * 0.72, 'base_y': h * 0.52,
            'amp_x1': 40, 'k_x1': 3, 'amp_x2': 20, 'k_x2': 2,
            'amp_y1': 25, 'k_y1': 1, 'amp_y2': 12, 'k_y2': 3,
            'k_pulse': 18, 'pulse_phase': 3.1,
            'core_r': 1.4, 'halo_r': 5.8, 'color': colors[2], 'depth': 0.65
        },
        # FF 4: Center-right lower lake surface
        {
            'base_x': w * 0.58, 'base_y': h * 0.76,
            'amp_x1': 50, 'k_x1': 2, 'amp_x2': 25, 'k_x2': 5,
            'amp_y1': 20, 'k_y1': 4, 'amp_y2': 10, 'k_y2': 2,
            'k_pulse': 15, 'pulse_phase': 4.5,
            'core_r': 1.7, 'halo_r': 7.0, 'color': colors[3], 'depth': 0.82
        }
    ]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(temp_raw, fourcc, fps, (w, h))

    print("Rendering frames with tiny organic fireflies...")
    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Normalized time in loop [0.0, 1.0)
        u = frame_idx / total_frames
        tau = 2.0 * math.pi * u

        glow_layer = np.zeros((h, w, 3), dtype=np.float32)

        for ff in fireflies:
            # Periodic organic drift
            cur_x = int(ff['base_x'] + ff['amp_x1'] * math.sin(ff['k_x1'] * tau) + ff['amp_x2'] * math.cos(ff['k_x2'] * tau))
            cur_y = int(ff['base_y'] + ff['amp_y1'] * math.sin(ff['k_y1'] * tau) + ff['amp_y2'] * math.cos(ff['k_y2'] * tau))

            # Periodic organic pulse (smooth sinusoidal breathing: min 0.15, max 1.0)
            raw_pulse = 0.55 + 0.45 * math.sin(ff['k_pulse'] * tau + ff['pulse_phase'])
            # Sharpen pulse curve slightly so it twinkles organically
            pulse = math.pow(raw_pulse, 1.8) * ff['depth']

            if pulse < 0.05:
                continue

            hr = int(ff['halo_r'] * 2.2)
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

            # Delicate Gaussian core (bright pinpoint) + subtle micro halo
            halo = np.exp(-d_sq / (2.0 * (ff['halo_r'] * 0.45)**2)) * 0.45 * pulse
            core = np.exp(-d_sq / (2.0 * (cr * 0.70)**2)) * 1.35 * pulse
            glow = (halo + core)[:, :, np.newaxis]

            glow_layer[y_min:y_max, x_min:x_max] += glow * col

            # Micro water reflection on lake surface (below y > h * 0.60)
            if cur_y > h * 0.58:
                refl_y = cur_y + int(18 * ff['depth'])
                if refl_y < h:
                    ry_min = max(0, refl_y - hr // 2)
                    ry_max = min(h, refl_y + hr // 2)
                    rx_min = max(0, cur_x - hr)
                    rx_max = min(w, cur_x + hr)
                    if ry_max > ry_min and rx_max > rx_min:
                        RGY, RGX = np.ogrid[ry_min-refl_y:ry_max-refl_y, rx_min-cur_x:rx_max-cur_x]
                        r_dist = (RGX * 0.8)**2 + (RGY * 2.2)**2
                        r_glow = np.exp(-r_dist / (2.0 * (ff['halo_r'] * 0.40)**2)) * 0.18 * pulse
                        glow_layer[ry_min:ry_max, rx_min:rx_max] += r_glow[:, :, np.newaxis] * col

        # Composite fireflies onto the real video frame
        composite = np.clip(frame.astype(np.float32) + glow_layer, 0, 255).astype(np.uint8)
        writer.write(composite)

        frame_idx += 1
        if frame_idx % 300 == 0:
            print(f"Processed {frame_idx}/{total_frames} frames ({frame_idx/total_frames*100:.1f}%)")

    cap.release()
    writer.release()
    print("All frames rendered. Muxing original audio and encoding with x264...")

    # Extract audio from original input video and mux into final MP4
    cmd = [
        "ffmpeg", "-y",
        "-i", temp_raw,
        "-i", in_video,
        "-map", "0:v",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "22",
        "-maxrate", "1100k", "-bufsize", "2200k",
        "-pix_fmt", "yuv420p",
        "-c:a", "copy",
        "-shortest",
        "-movflags", "+faststart",
        final_output
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if os.path.exists(temp_raw):
        os.remove(temp_raw)

    if os.path.exists(final_output):
        sz_mb = os.path.getsize(final_output) / (1024 * 1024)
        print(f"SUCCESS! Output created: {final_output} ({sz_mb:.2f} MB)")
    else:
        print("Error: output file was not created.")

if __name__ == "__main__":
    main()
