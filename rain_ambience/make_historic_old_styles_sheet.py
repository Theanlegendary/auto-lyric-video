import cv2
import numpy as np
import shutil
import os

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
dst_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail\nature_options"
os.makedirs(dst_dir, exist_ok=True)

files = [
    ("old_style_japan_edo_tea_house_rain_1793609128004.jpg", "old_style_1_kyoto_edo_tea_house.jpg", "1. Edo-Period Kyoto Tea House (Japan)"),
    ("old_style_japan_shirakawago_thatched_rain_1793609147891.jpg", "old_style_2_shirakawago_thatched_house.jpg", "2. Shirakawa-go Thatched Farmhouse (Japan)"),
    ("old_style_korean_historic_hanok_rain_1793609166604.jpg", "old_style_3_joseon_historic_hanok.jpg", "3. Joseon-Era Historic Mountain Hanok (Korea)")
]

cell_w, cell_h = 640, 360
cards = []

for src_name, dst_name, title in files:
    src_fp = os.path.join(brain, src_name)
    dst_fp = os.path.join(dst_dir, dst_name)
    shutil.copy2(src_fp, dst_fp)
    
    img = cv2.imread(dst_fp)
    resized = cv2.resize(img, (cell_w, cell_h))
    
    # Clean header banner
    cv2.rectangle(resized, (0, 0), (cell_w, 45), (15, 20, 28), -1)
    cv2.putText(resized, title, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.62, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.rectangle(resized, (0, 0), (cell_w, cell_h), (50, 70, 90), 2)
    cards.append(resized)

sheet = np.hstack(cards) # 1920 x 360
out_sheet = os.path.join(dst_dir, "contact_sheet_3_historic_old_styles.jpg")
cv2.imwrite(out_sheet, sheet)
shutil.copy2(out_sheet, os.path.join(brain, "contact_sheet_3_historic_old_styles.jpg"))

print("Created 3 Historic Old Styles comparison sheet:", out_sheet)
