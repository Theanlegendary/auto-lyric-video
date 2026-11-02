import cv2
import numpy as np
import os

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
dst_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail\nature_options"
src_img_path = os.path.join(dst_dir, "old_style_1_kyoto_edo_tea_house.jpg")

img = cv2.imread(src_img_path)
h, w = img.shape[:2]

# Convert to float 0..1
img_f = img.astype(np.float32) / 255.0

# Vignette mask to keep focus on the warm glowing tea house
Y, X = np.ogrid[:h, :w]
max_d = np.sqrt((w/2)**2 + (h/2)**2)
dist = np.sqrt((X - w*0.60)**2 + (Y - h*0.55)**2) # center slightly near house
vignette = (1.0 - 0.28 * (dist / max_d)**2)[:, :, np.newaxis]

# 1. Level A: "A Bit Darker" - Moody Dusk (-12% brightness, 1.15 contrast, boost warm lantern glow)
# Just enough to make the lantern cozy and deep, while keeping all green trees crystal clear
b, g, r = cv2.split(img_f)
# Slight cool shift in shadows, warm highlights
b_a = np.clip((b - 0.5) * 1.18 + 0.48, 0, 1)
g_a = np.clip((g - 0.5) * 1.15 + 0.47, 0, 1)
r_a = np.clip((r - 0.5) * 1.14 + 0.46, 0, 1)
level_a = cv2.merge([b_a, g_a, r_a]) * (1.0 - 0.20 * (dist / max_d)**2)[:, :, np.newaxis]
level_a = np.clip(level_a * 255.0, 0, 255).astype(np.uint8)

# 2. Level B: "Medium Darker" - Deep Twilight / Cozy Evening (-22% brightness, 1.25 contrast)
b_b = np.clip((b - 0.5) * 1.25 + 0.42 + 0.03, 0, 1) # slight twilight blue tint
g_b = np.clip((g - 0.5) * 1.22 + 0.40, 0, 1)
r_b = np.clip((r - 0.5) * 1.20 + 0.38, 0, 1)
level_b = cv2.merge([b_b, g_b, r_b]) * vignette
level_b = np.clip(level_b * 255.0, 0, 255).astype(np.uint8)

# 3. Level C: "Atmospheric Blue Hour" (-30% brightness, rich twilight mood)
b_c = np.clip((b - 0.5) * 1.30 + 0.38 + 0.06, 0, 1)
g_c = np.clip((g - 0.5) * 1.28 + 0.34 + 0.02, 0, 1)
r_c = np.clip((r - 0.5) * 1.25 + 0.30, 0, 1)
level_c = cv2.merge([b_c, g_c, r_c]) * vignette
level_c = np.clip(level_c * 255.0, 0, 255).astype(np.uint8)

# Save individual images
out_a = os.path.join(dst_dir, "kyoto_edo_darker_level_a.jpg")
out_b = os.path.join(dst_dir, "kyoto_edo_darker_level_b.jpg")
out_c = os.path.join(dst_dir, "kyoto_edo_darker_level_c.jpg")

cv2.imwrite(out_a, level_a)
cv2.imwrite(out_b, level_b)
cv2.imwrite(out_c, level_c)

# Also copy to brain
cv2.imwrite(os.path.join(brain, "kyoto_edo_darker_level_a.jpg"), level_a)
cv2.imwrite(os.path.join(brain, "kyoto_edo_darker_level_b.jpg"), level_b)
cv2.imwrite(os.path.join(brain, "kyoto_edo_darker_level_c.jpg"), level_c)

# Create comparison sheet: Original vs Level A vs Level B vs Level C
cell_w, cell_h = 480, 270
comp_orig = cv2.resize(img, (cell_w, cell_h))
comp_a = cv2.resize(level_a, (cell_w, cell_h))
comp_b = cv2.resize(level_b, (cell_w, cell_h))
comp_c = cv2.resize(level_c, (cell_w, cell_h))

for c, label in [(comp_orig, "ORIGINAL (Bright)"), 
                 (comp_a, "LEVEL A: A Bit Darker (Moody Overcast)"), 
                 (comp_b, "LEVEL B: Cozy Dusk Twilight (RECOMMENDED)"), 
                 (comp_c, "LEVEL C: Blue Hour Evening")]:
    cv2.rectangle(c, (0, 0), (cell_w, 36), (15, 20, 28), -1)
    cv2.putText(c, label, (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.48, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.rectangle(c, (0, 0), (cell_w, cell_h), (50, 70, 90), 2)

top_row = np.hstack([comp_orig, comp_a])
bot_row = np.hstack([comp_b, comp_c])
comp_grid = np.vstack([top_row, bot_row])

out_comp = os.path.join(dst_dir, "contact_sheet_kyoto_darkness_levels.jpg")
cv2.imwrite(out_comp, comp_grid)
cv2.imwrite(os.path.join(brain, "contact_sheet_kyoto_darkness_levels.jpg"), comp_grid)

print("Saved darkness comparison sheet:", out_comp)
