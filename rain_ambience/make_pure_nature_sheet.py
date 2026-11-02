import cv2
import numpy as np
import os

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

# Let's inspect the 8 most promising pure nature candidates:
items = [
    ("5174040", "wide_cand_5174040.jpg", "Alpine Mountain Lake & Pine Valley Rain"),
    ("9934612", "wide_cand_9934612.jpg", "Deep Forest Flooded Lake & Mossy Woods"),
    ("9353501", "wide_cand_9353501.jpg", "Rainforest Canopy Misty Ridge"),
    ("8110359", "wide_cand_8110359.jpg", "Dense Tropical Ferns & Deep Jungle Rain"),
    ("11643791", "wide_cand_11643791.jpg", "Giant Elephant-Ear Leaves Rainforest"),
    ("10766175", "pure_nature_10766175.jpg", "Misty Evergreen Pine Forest Ridge"),
    ("5550281", "pure_nature_5550281.jpg", "Rain Sweeping Over Wild Forest Trees"),
    ("3864101", "pure_nature_3864101.jpg", "Raindrops on Jungle Foliage"),
]

imgs = []
cell_w, cell_h = 480, 270

for vid, fn, label in items:
    fp = os.path.join(brain, fn)
    if os.path.exists(fp):
        img = cv2.imread(fp)
        img = cv2.resize(img, (cell_w, cell_h))
        # Draw dark banner
        cv2.rectangle(img, (0, 0), (cell_w, 40), (0, 0, 0), -1)
        cv2.putText(img, f"ID: {vid} - {label}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
        imgs.append(img)
    else:
        print(f"Missing {fn}")

# 2 rows x 4 cols
if len(imgs) == 8:
    r1 = np.hstack(imgs[:4])
    r2 = np.hstack(imgs[4:])
    sheet = np.vstack([r1, r2])
    out_sheet = os.path.join(brain, "contact_sheet_pure_nature_options.jpg")
    cv2.imwrite(out_sheet, sheet)
    print("Created:", out_sheet)
else:
    print(f"Total images: {len(imgs)}")
