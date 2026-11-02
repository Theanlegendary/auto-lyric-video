import cv2
import numpy as np
import shutil
import os

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
dst_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail\nature_options"
os.makedirs(dst_dir, exist_ok=True)

img_japan = os.path.join(brain, "japan_forest_city_rain_house_1793608803846.jpg")
img_korea = os.path.join(brain, "korea_forest_city_rain_hanok_1793608827051.jpg")

dst_japan = os.path.join(dst_dir, "japan_forest_city_rain_house.jpg")
dst_korea = os.path.join(dst_dir, "korea_forest_city_rain_hanok.jpg")

shutil.copy2(img_japan, dst_japan)
shutil.copy2(img_korea, dst_korea)

# Build side-by-side comparison sheet
j_img = cv2.imread(dst_japan)
k_img = cv2.imread(dst_korea)

cell_w, cell_h = 960, 540
j_res = cv2.resize(j_img, (cell_w, cell_h))
k_res = cv2.resize(k_img, (cell_w, cell_h))

# Header badges
cv2.rectangle(j_res, (0, 0), (cell_w, 55), (15, 20, 28), -1)
cv2.putText(j_res, "OPTION J: Kyoto Forest Wooden House in Rain (Japan)", (20, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

cv2.rectangle(k_res, (0, 0), (cell_w, 55), (15, 20, 28), -1)
cv2.putText(k_res, "OPTION K: Mountain Hanok Overlooking Seoul in Rain (Korea)", (20, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

sheet = np.hstack([j_res, k_res]) # 1920 x 540
out_sheet = os.path.join(dst_dir, "contact_sheet_japan_korea_forest_city.jpg")
cv2.imwrite(out_sheet, sheet)
# Also copy to brain
shutil.copy2(out_sheet, os.path.join(brain, "contact_sheet_japan_korea_forest_city.jpg"))

print("Created Japan & Korea comparison sheet:", out_sheet)
