import cv2
import numpy as np
import os

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

# Curate the 12 best, brightest, most diverse natural rain scenery candidates:
candidates = [
    # (ID, filename, title, description)
    ("5174040", "wide_cand_5174040.jpg", "Alpine Lake & Pine Valley", "Vast mountain lake, gentle rain ripples, rocky alpine peaks"),
    ("9934612", "wide_cand_9934612.jpg", "Flooded Mossy Woodland", "Calm woodland water, rain patter, ancient mossy tree reflections"),
    ("9353501", "wide_cand_9353501.jpg", "Rainforest Canopy Overlook", "Vast mountain ridge, lush green rainforest canopy, rolling mist"),
    ("8110359", "wide_cand_8110359.jpg", "Deep Tropical Ferns & Forest", "Vibrant emerald green jungle foliage in steady downpour"),
    ("11643791", "wide_cand_11643791.jpg", "Giant Elephant-Ear Leaves", "Lush rainforest undergrowth, glistening rain trickling off leaves"),
    ("13180836", "wide_cand_13180836.jpg", "Misty Old-Growth Woods", "Heavy rain in dense green woods with ancient tree trunk & ferns"),
    ("10766175", "pure_nature_10766175.jpg", "Evergreen Pine Forest Rain", "Tall pine trees in misty mountain rain, fresh pine needles"),
    ("5918481", "wide_cand_5918481.jpg", "Open Meadow & Distant Forest", "Expansive open green valley, rain falling across grassy fields"),
    ("9328701", "wide_cand_9328701.jpg", "Jungle Canopy & Palm Fronds", "Lush green wild palm trees in tropical rainforest rain"),
    ("4828773", "wide_cand_4828773.jpg", "Green Garden Foliage & Rain", "Heavy raindrops splashing onto vibrant fresh green leaves"),
    ("13446069", "wide_cand_13446069.jpg", "Misty Pacific Pine Forest", "Atmospheric fog rolling through towering mountain pines"),
    ("12717007", "wide_cand_12717007.jpg", "Rainforest Cabin Vista (Day)", "Cozy wooden cabin nestled among lush green banana trees")
]

cell_w, cell_h = 480, 270
cards = []

for vid, fn, title, desc in candidates:
    fp = os.path.join(brain, fn)
    if os.path.exists(fp):
        img = cv2.imread(fp)
        img = cv2.resize(img, (cell_w, cell_h))
        
        # Add clean top banner with ID and Title
        cv2.rectangle(img, (0, 0), (cell_w, 42), (15, 20, 28), -1)
        cv2.putText(img, f"ID: {vid} - {title}", (10, 26), cv2.FONT_HERSHEY_SIMPLEX, 0.52, (0, 255, 255), 1, cv2.LINE_AA)
        # Add subtle border
        cv2.rectangle(img, (0, 0), (cell_w, cell_h), (40, 50, 70), 2)
        cards.append(img)
    else:
        print(f"Missing {fn}")

# 3 rows x 4 columns = 12 cards (1920 x 810)
if len(cards) == 12:
    r1 = np.hstack(cards[0:4])
    r2 = np.hstack(cards[4:8])
    r3 = np.hstack(cards[8:12])
    sheet = np.vstack([r1, r2, r3])
    out_sheet = os.path.join(brain, "contact_sheet_12_bright_nature_ids.jpg")
    cv2.imwrite(out_sheet, sheet)
    print("Created 12-ID Bright Nature Contact Sheet:", out_sheet)
else:
    print(f"Total cards: {len(cards)}")
