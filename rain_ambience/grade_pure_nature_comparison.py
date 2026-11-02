import cv2
import numpy as np
import os

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

# Night grading parameters (same as our master video)
# rr=0.38:rg=0.08:rb=0.0:gr=0.05:gg=0.45:gb=0.20:br=0.10:bg=0.25:bb=0.95
# brightness=-0.07, contrast=1.28, saturation=0.82

def apply_night_grade(img_bgr):
    # Convert to float 0..1
    b, g, r = cv2.split(img_bgr.astype(np.float32) / 255.0)
    
    # colorchannelmixer
    r_out = 0.38*r + 0.08*g + 0.0*b
    g_out = 0.05*r + 0.45*g + 0.20*b
    b_out = 0.10*r + 0.25*g + 0.95*b

    merged = cv2.merge([b_out, g_out, r_out])
    
    # eq: brightness=-0.07, contrast=1.28
    # contrast: (x - 0.5) * 1.28 + 0.5 - 0.07
    graded = (merged - 0.5) * 1.28 + 0.5 - 0.07
    
    # saturation: convert to hsv in float
    graded = np.clip(graded, 0.0, 1.0)
    hsv = cv2.cvtColor((graded * 255).astype(np.uint8), cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 0.85, 0, 255)
    result = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    
    # Vignette
    h, w = result.shape[:2]
    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - w/2)**2 + (Y - h/2)**2)
    max_dist = np.sqrt((w/2)**2 + (h/2)**2)
    vignette = 1.0 - 0.35 * (dist_from_center / max_dist)**2
    result = np.clip(result.astype(np.float32) * vignette[:, :, np.newaxis], 0, 255).astype(np.uint8)
    return result

options = [
    ("5174040", "wide_cand_5174040.jpg", "1. Alpine Mountain Lake & Rain Ripples (Epic Vista)"),
    ("9934612", "wide_cand_9934612.jpg", "2. Deep Flooded Forest & Ancient Mossy Trees"),
    ("10766175", "pure_nature_10766175.jpg", "3. Misty Evergreen Pine Forest Ridge in Heavy Rain"),
    ("9353501", "wide_cand_9353501.jpg", "4. Rainforest Mountain Canopy & Foggy Ridge"),
    ("12717007", "wide_cand_12717007.jpg", "5. Secluded Cabin in Wild Rainforest (Current)")
]

cell_w, cell_h = 640, 360
graded_imgs = []

for vid, fn, label in options:
    fp = os.path.join(brain, fn)
    if os.path.exists(fp):
        raw = cv2.imread(fp)
        graded = apply_night_grade(raw)
        graded_resized = cv2.resize(graded, (cell_w, cell_h))
        
        # Save individual preview
        single_path = os.path.join(brain, f"pure_nature_night_{vid}.jpg")
        cv2.imwrite(single_path, graded)
        
        # Add label overlay
        cv2.rectangle(graded_resized, (0, 0), (cell_w, 48), (10, 15, 25), -1)
        cv2.putText(graded_resized, label, (12, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.rectangle(graded_resized, (0, 0), (cell_w, cell_h), (50, 70, 100), 2)
        graded_imgs.append(graded_resized)

# Assemble into comparison grid
# 2 rows: 3 on top row, 2 centered or padded on bottom row
top_row = np.hstack(graded_imgs[:3]) # 1920 x 360
# For bottom row, let's put 2 images + a black tile
black_tile = np.zeros((cell_h, cell_w, 3), dtype=np.uint8)
bottom_row = np.hstack([graded_imgs[3], graded_imgs[4], black_tile])
full_grid = np.vstack([top_row, bottom_row])

out_grid = os.path.join(brain, "contact_sheet_pure_nature_night_graded.jpg")
cv2.imwrite(out_grid, full_grid)
print("Saved night graded sheet:", out_grid)
