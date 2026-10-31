import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
user_ref_path = os.path.join(brain, ".user_uploaded", "media_1793006726653_eac9d068.png")
user_ref = Image.open(user_ref_path)

# 1920x1080 master comparison canvas
canvas = Image.new("RGB", (1920, 1080), (16, 12, 22))
draw = ImageDraw.Draw(canvas)

# Header
draw.rectangle((0, 0, 1920, 70), fill=(24, 18, 34))
draw.text((50, 22), "AESTHETIC DREAMY FONT MATCH & SIZE TEST (TARGET: CLOUD NINE BY FORTH & WILD)", fill=(255, 230, 200))

# Left panel: User Reference
ref_card = Image.new("RGB", (480, 960), (22, 17, 30))
rdraw = ImageDraw.Draw(ref_card)
rdraw.rectangle((0, 0, 480, 960), outline=(255, 180, 80), width=3)
rdraw.text((25, 25), "YOUR REFERENCE IMAGE", fill=(255, 200, 100))
rdraw.text((25, 55), "Cloud Nine (Dreamy Handwritten Font)", fill=(200, 200, 210))
rdraw.text((25, 80), "• Chunky, bold, rounded marker strokes", fill=(170, 170, 180))
rdraw.text((25, 105), "• Pure clean white with NO harsh outline", fill=(170, 170, 180))
rdraw.text((25, 130), "• Prominent, large display size", fill=(170, 170, 180))

# Paste user reference image
ref_w = 430
ref_h = int(user_ref.height * ref_w / user_ref.width)
ref_scaled = user_ref.resize((ref_w, ref_h), Image.Resampling.LANCZOS)
ref_card.paste(ref_scaled, (25, 180))

# Bottom note
rdraw.text((25, 780), "KEY ATTRIBUTES DETECTED:", fill=(255, 220, 150))
rdraw.text((25, 810), "1. Big, bold, pill-rounded letters", fill=(220, 220, 230))
rdraw.text((25, 840), "2. Ultra-clean floating aesthetic", fill=(220, 220, 230))
rdraw.text((25, 870), "3. Smooth soft shadow (no black stroke)", fill=(220, 220, 230))

canvas.paste(ref_card, (40, 90))

# Right panel: 4 Top Font Candidates rendering the exact text on Vibe Sky
font_cards = [
    ("Chewy (Most Playful & Chunky Bouncy Marker)", "Chewy", 560, 90),
    ("Sniglet (Puffy Cloud-Like Friendly Rounded)", "Sniglet", 1240, 90),
    ("Balsamiq Sans (Clean Handwritten Rounded)", "BalsamiqSans", 560, 570),
    ("DynaPuff (Dreamy Puffy Cloud Display)", "DynaPuff", 1240, 570),
]

for label, font_id, x, y in font_cards:
    cpath = os.path.join(brain, f"cloudnine_match_{font_id}.png")
    card = Image.new("RGB", (640, 460), (22, 17, 30))
    cdraw = ImageDraw.Draw(card)
    cdraw.rectangle((0, 0, 640, 460), outline=(100, 160, 255), width=2)
    cdraw.text((20, 15), label, fill=(180, 220, 255))
    
    if os.path.exists(cpath):
        cim = Image.open(cpath)
        # crop center
        ccrop = cim.crop((560, 240, 1360, 760)).resize((600, 390), Image.Resampling.LANCZOS)
        card.paste(ccrop, (20, 50))
    
    canvas.paste(card, (x, y))

out_path = os.path.join(brain, "master_font_cloudnine_comparison.png")
canvas.save(out_path, "PNG")
print(f"Master comparison saved: {out_path}")
