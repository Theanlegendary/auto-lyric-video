import cv2
import numpy as np
import random
import math
import os

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

def render_fireflies_on_image(bg_path, out_path, num_fireflies=45, seed=42):
    random.seed(seed)
    np.random.seed(seed)
    
    bg = cv2.imread(bg_path)
    h, w = bg.shape[:2]
    
    # Firefly glow layer
    glow_layer = np.zeros((h, w, 3), dtype=np.float32)
    
    # Color palette for magical fireflies:
    # Warm golden-amber: (30, 210, 255) in BGR
    # Soft bioluminescent lime-emerald: (50, 255, 180) in BGR
    # Moonlit cyan-green: (140, 255, 120) in BGR
    colors = [
        np.array([40, 220, 255], dtype=np.float32),  # Golden Amber
        np.array([60, 255, 190], dtype=np.float32),  # Warm Lime
        np.array([120, 255, 150], dtype=np.float32), # Emerald Glow
        np.array([50, 240, 255], dtype=np.float32),  # Sun Gold
    ]
    
    for i in range(num_fireflies):
        # Position
        x = random.randint(int(w * 0.05), int(w * 0.95))
        # Fireflies concentrate in the lower 70% (near water, under trees)
        y = random.randint(int(h * 0.20), int(h * 0.90))
        
        # Depth: size & brightness
        # depth 0.3 (far away) to 1.0 (foreground)
        depth = random.uniform(0.3, 1.0)
        core_radius = int(2 + 3 * depth)
        halo_radius = int(12 + 25 * depth)
        intensity = random.uniform(0.6, 1.0) * depth
        
        color = random.choice(colors)
        
        # Draw soft Gaussian glow
        y_min = max(0, y - halo_radius)
        y_max = min(h, y + halo_radius)
        x_min = max(0, x - halo_radius)
        x_max = min(w, x + halo_radius)
        
        if y_max <= y_min or x_max <= x_min:
            continue
            
        Y, X = np.ogrid[y_min-y:y_max-y, x_min-x:x_max-x]
        dist_sq = X*X + Y*Y
        
        # Dual-layer Gaussian: wide soft halo + intense bright core
        halo = np.exp(-dist_sq / (2.0 * (halo_radius * 0.4)**2)) * 0.65 * intensity
        core = np.exp(-dist_sq / (2.0 * (core_radius * 0.8)**2)) * 1.0 * intensity
        glow = halo + core
        
        # Add to glow layer
        for c in range(3):
            glow_layer[y_min:y_max, x_min:x_max, c] += glow * color[c]
            
        # Add soft water reflection if near bottom
        if y > h * 0.60:
            refl_y = y + int(random.uniform(15, 45) * depth)
            if refl_y < h:
                refl_h_min = max(0, refl_y - halo_radius // 2)
                refl_h_max = min(h, refl_y + halo_radius // 2)
                refl_w_min = max(0, x - int(halo_radius * 1.5))
                refl_w_max = min(w, x + int(halo_radius * 1.5))
                
                if refl_h_max > refl_h_min and refl_w_max > refl_w_min:
                    RY, RX = np.ogrid[refl_h_min-refl_y:refl_h_max-refl_y, refl_w_min-x:refl_w_max-x]
                    refl_dist = (RX / 2.0)**2 + (RY * 1.5)**2
                    refl_glow = np.exp(-refl_dist / (2.0 * (halo_radius * 0.5)**2)) * 0.25 * intensity
                    for c in range(3):
                        glow_layer[refl_h_min:refl_h_max, refl_w_min:refl_w_max, c] += refl_glow * color[c]

    # Screen blend / additive blend
    bg_float = bg.astype(np.float32)
    # Additive glow with soft saturation curve
    composite = bg_float + glow_layer
    composite = np.clip(composite, 0, 255).astype(np.uint8)
    
    cv2.imwrite(out_path, composite)
    print("Rendered fireflies on:", out_path)

# Test on 3 backgrounds:
bg1 = os.path.join(brain, "pure_nature_night_9934612.jpg") # Flooded Ancient Forest
bg2 = os.path.join(brain, "pure_nature_night_5174040.jpg") # Alpine Mountain Lake
bg3 = os.path.join(brain, "pure_nature_night_12717007.jpg") # Rainforest Cabin

render_fireflies_on_image(bg1, os.path.join(brain, "fireflies_flooded_forest.jpg"), num_fireflies=55, seed=101)
render_fireflies_on_image(bg2, os.path.join(brain, "fireflies_alpine_lake.jpg"), num_fireflies=50, seed=202)
render_fireflies_on_image(bg3, os.path.join(brain, "fireflies_rainforest_cabin.jpg"), num_fireflies=45, seed=303)
