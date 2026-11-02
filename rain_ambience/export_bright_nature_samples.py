import cv2
import shutil
import os

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
dst_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail\nature_options"
os.makedirs(dst_dir, exist_ok=True)

# Copy sheet
sheet_src = os.path.join(brain, "contact_sheet_12_bright_nature_ids.jpg")
shutil.copy2(sheet_src, os.path.join(dst_dir, "contact_sheet_12_bright_nature_ids.jpg"))

candidates = [
    ("5174040", "wide_cand_5174040.jpg", "Alpine Lake & Mountain Pine Valley", "Crystal-clear mountain lake with thousands of rain ripples, rocky alpine peaks, and pine forest valley."),
    ("9934612", "wide_cand_9934612.jpg", "Flooded Ancient Mossy Forest", "Serene woodland pool with gentle rain patter and reflections of ancient mossy tree trunks."),
    ("9353501", "wide_cand_9353501.jpg", "Vast Rainforest Canopy Overlook", "High mountain ridge overlooking endless lush green tropical trees and drifting mist."),
    ("8110359", "wide_cand_8110359.jpg", "Deep Tropical Jungle Foliage", "Dense emerald jungle ferns and tropical plants in heavy soothing rainfall."),
    ("11643791", "wide_cand_11643791.jpg", "Giant Elephant-Ear Leaves Rainforest", "Vibrant green rainforest undergrowth with water streaming off large shiny leaves."),
    ("13180836", "wide_cand_13180836.jpg", "Misty Old-Growth Forest & Ferns", "Ancient forest tree with rain cascading through fresh green leaves and ferns."),
    ("10766175", "pure_nature_10766175.jpg", "Tall Mountain Pine Ridge in Rain", "Dense evergreen pines with heavy mountain rain streaming through needles."),
    ("5918481", "wide_cand_5918481.jpg", "Open Meadow & Distant Forest Rain", "Expansive open green valley and meadow in heavy downpour."),
    ("9328701", "wide_cand_9328701.jpg", "Jungle Canopy & Wild Palm Fronds", "Tropical wild palm trees swaying in heavy monsoon rainfall."),
    ("4828773", "wide_cand_4828773.jpg", "Green Garden Foliage & Heavy Rain", "Heavy raindrops splashing onto fresh vibrant green vine leaves."),
    ("13446069", "wide_cand_13446069.jpg", "Misty Pacific Pine Forest", "Dense mountain fog rolling through tall evergreen pines in gentle rain."),
    ("12717007", "wide_cand_12717007.jpg", "Rainforest Cabin Vista (Natural Light)", "Cozy wooden cabin surrounded by lush banana trees in natural daylight rain.")
]

for vid, fn, title, desc in candidates:
    src_fp = os.path.join(brain, fn)
    if os.path.exists(src_fp):
        img = cv2.imread(src_fp)
        # Save a clean 1280x720 version with ID header
        resized = cv2.resize(img, (1280, 720))
        # Draw clean header banner
        cv2.rectangle(resized, (0, 0), (1280, 60), (15, 20, 28), -1)
        cv2.putText(resized, f"ID: {vid} | {title}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2, cv2.LINE_AA)
        
        dst_fn = f"bright_nature_{vid}.jpg"
        dst_fp = os.path.join(dst_dir, dst_fn)
        cv2.imwrite(dst_fp, resized)
        # Also copy to brain
        cv2.imwrite(os.path.join(brain, dst_fn), resized)
        print(f"Saved {dst_fn}")

print("All bright nature samples prepared!")
