import cv2
import numpy as np
import os

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

clips = [
    ("852354", "firefly_cand_852354.jpg", "Firefly Forest Night 1"),
    ("5571751", "firefly_cand_5571751.jpg", "Firefly Forest Night 2"),
    ("7725992", "firefly_cand_7725992.jpg", "Glowing Woods 3"),
    ("10152813", "firefly_cand_10152813.jpg", "Glowing Forest 4"),
    ("9737883", "firefly_cand_9737883.jpg", "Night Glow 5"),
    ("10440011", "firefly_cand_10440011.jpg", "Dark Woods Glow 6"),
    ("18300595", "firefly_cand_18300595.jpg", "Bioluminescent Rain Woods 7"),
    ("8733059", "firefly_cand_8733059.jpg", "Deep Forest Fireflies 8"),
]

cell_w, cell_h = 480, 270
imgs = []

for vid, fn, label in clips:
    fp = os.path.join(brain, fn)
    if os.path.exists(fp):
        img = cv2.imread(fp)
        img = cv2.resize(img, (cell_w, cell_h))
        cv2.rectangle(img, (0, 0), (cell_w, 36), (0, 0, 0), -1)
        cv2.putText(img, f"ID: {vid} - {label}", (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
        imgs.append(img)

r1 = np.hstack(imgs[:4])
r2 = np.hstack(imgs[4:])
sheet = np.vstack([r1, r2])

out_sheet = os.path.join(brain, "contact_sheet_fireflies.jpg")
cv2.imwrite(out_sheet, sheet)
print("Saved firefly contact sheet:", out_sheet)
