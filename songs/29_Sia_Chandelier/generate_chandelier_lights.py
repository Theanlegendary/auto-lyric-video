import numpy as np
import cv2
import math
import sys
import random

sys.stdout.reconfigure(encoding='utf-8')

width, height = 1920, 1080
fps = 25
duration = 20  # 20 seconds seamless loop
total_frames = fps * duration

output_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\29_Sia_Chandelier\live_chandelier_lights.mp4"

# Set deterministic random seed for beautiful aesthetic distribution
random.seed(101)
np.random.seed(101)

num_particles = 55
particles = []

for i in range(num_particles):
    # Initial properties
    x0 = random.uniform(50, width - 50)
    y0 = random.uniform(50, height - 50)
    radius = random.uniform(10, 38)
    
    # Upward vertical speed: loops exactly an integer number of heights over the 20 seconds,
    # or wraps seamlessly using modulo
    speed_y = random.uniform(15, 45) # pixels per second upwards
    
    # Horizontal drift
    drift_amp = random.uniform(20, 60)
    drift_freq = random.choice([1, 2, 3]) # integer cycles over 20s
    drift_phase = random.uniform(0, 2 * math.pi)
    
    # Pulse frequency (integer cycles over 20s for seamless loop)
    pulse_cycles = random.randint(2, 6)
    pulse_phase = random.uniform(0, 2 * math.pi)
    base_alpha = random.uniform(0.18, 0.45)
    
    # Warm golden/champagne/celestial palette
    color_choice = random.choice([
        (255, 230, 160),  # warm gold
        (255, 245, 200),  # champagne starlight
        (255, 210, 130),  # amber chandelier glow
        (230, 220, 255),  # subtle prism violet
        (255, 255, 255),  # pure bright sparkle
    ])
    
    particles.append({
        'x0': x0,
        'y0': y0,
        'radius': radius,
        'speed_y': speed_y,
        'drift_amp': drift_amp,
        'drift_freq': drift_freq,
        'drift_phase': drift_phase,
        'pulse_cycles': pulse_cycles,
        'pulse_phase': pulse_phase,
        'base_alpha': base_alpha,
        'color': color_choice
    })

# Pre-render soft bokeh gaussian kernels
def make_bokeh_kernel(radius, color):
    r_int = int(math.ceil(radius * 2.2))
    size = r_int * 2 + 1
    y, x = np.ogrid[-r_int:r_int+1, -r_int:r_int+1]
    dist_sq = x*x + y*y
    
    # Soft bokeh disc with smooth gaussian falloff at edge
    sigma = radius * 0.75
    kernel = np.exp(-dist_sq / (2 * sigma * sigma))
    
    # Normalize kernel peak to 1.0
    kernel = kernel.astype(np.float32)
    
    # Create 3-channel colored patch (BGR for OpenCV)
    # color is RGB
    bgr = (color[2] / 255.0, color[1] / 255.0, color[0] / 255.0)
    patch = np.zeros((size, size, 3), dtype=np.float32)
    for c in range(3):
        patch[:, :, c] = kernel * bgr[c]
    return patch, r_int

# Precompute particle kernels
kernels = []
for p in particles:
    k, r_int = make_bokeh_kernel(p['radius'], p['color'])
    kernels.append((k, r_int))

print(f"Generating {total_frames} frames of live chandelier bokeh lights...")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

for f in range(total_frames):
    t = f / fps
    frame = np.zeros((height, width, 3), dtype=np.float32)
    
    for idx, p in enumerate(particles):
        # Y position with seamless modulo wrap
        # Total distance traveled over 20s
        y = (p['y0'] - p['speed_y'] * t) % height
        
        # X position with sinusoidal drift (integer cycles ensures seamless loop)
        x = p['x0'] + p['drift_amp'] * math.sin(2 * math.pi * p['drift_freq'] * (t / duration) + p['drift_phase'])
        x = x % width
        
        # Pulse brightness (integer cycles ensures seamless loop)
        pulse = 0.6 + 0.4 * math.sin(2 * math.pi * p['pulse_cycles'] * (t / duration) + p['pulse_phase'])
        alpha = p['base_alpha'] * pulse
        
        patch, r_int = kernels[idx]
        
        # Coordinates for bounding box
        ix, iy = int(x), int(y)
        x1 = max(0, ix - r_int)
        y1 = max(0, iy - r_int)
        x2 = min(width, ix + r_int + 1)
        y2 = min(height, iy + r_int + 1)
        
        kx1 = x1 - (ix - r_int)
        ky1 = y1 - (iy - r_int)
        kx2 = kx1 + (x2 - x1)
        ky2 = ky1 + (y2 - y1)
        
        if x2 > x1 and y2 > y1 and kx2 > kx1 and ky2 > ky1:
            frame[y1:y2, x1:x2] += patch[ky1:ky2, kx1:kx2] * alpha

    # Clip to [0, 1] and convert to uint8
    frame = np.clip(frame, 0.0, 1.0) * 255.0
    frame_uint8 = frame.astype(np.uint8)
    out.write(frame_uint8)

out.release()
print(f"Successfully generated: {output_path} ({duration}s, 1920x1080 @ 25fps)")
