import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
user_ref_path = os.path.join(brain, ".user_uploaded", "media_1793006726653_eac9d068.png")
user_ref = Image.open(user_ref_path)

# Canvas: 1920 x 1080
canvas = Image.new("RGB", (1920, 1080), (15, 12, 22))
draw = ImageDraw.Draw(canvas)

# Title banner
draw.text((60, 30), "FONT & SIZE ACCEPTANCE GRID — MATCHING USER REFERENCE", fill=(255, 220, 180))

# 1. User reference on the top-left (x=60, y=90, w=400, h=400)
ref_box = (60, 90, 480, 520)
draw.rectangle(ref_box, outline=(255, 180, 100), width=3)
ref_fit = user_ref.resize((420, int(user_ref.height * 420 / user_ref.width)), Image.Resampling.LANCZOS)
canvas.paste(ref_fit, (60, 90 + (430 - ref_fit.height)//2))
draw.text((70, 480), "USER REFERENCE (Cloud Nine)", fill=(255, 200, 120))

# 2. Top candidates around it
spots = [
    ("Chewy (Ultra-Chunky Handwritten)", "Chewy", 520, 90),
    ("Sniglet (Puffy Rounded Bold)", "Sniglet", 1220, 90),
    ("Balsamiq Sans (Clean Handwritten Sans)", "BalsamiqSans", 520, 560),
    ("Gaegu (Bouncy Korean Marker Bold)", "Gaegu", 1220, 560),
]

for label, font_id, x, y in spots:
    cpath = os.path.join(brain, f"cloudnine_match_{font_id}.png")
    if os.path.exists(cpath):
        cim = Image.open(cpath)
        ccrop = cim.crop((600, 260, 1320, 740)).resize((660, 430), Image.Resampling.LANCZOS)
        canvas.paste(ccrop, (x, y))
        draw.rectangle((x, y, x + 660, y + 430), outline=(100, 150, 255), width=2)
        draw.text((x + 20, y + 20), f"Option: {label}", fill=(255, 255, 255))

out_path = os.path.join(brain, "font_selection_grid_labeled.png")
canvas.save(out_path, "PNG")
print(f"Saved {out_path}")
