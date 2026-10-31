import os
import sys
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding='utf-8')

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
user_ref_path = os.path.join(brain, ".user_uploaded", "media_1793006726653_eac9d068.png")
user_ref = Image.open(user_ref_path)

# Canvas 1920x1080
canvas = Image.new("RGB", (1920, 1080), (14, 10, 20))
draw = ImageDraw.Draw(canvas)

# Top Bar
draw.rectangle((0, 0, 1920, 80), fill=(22, 16, 32))
draw.text((60, 26), "CLOUD NINE COMPARISON: HOOK CHORUS 'LONELY / I'M MR. LONELY' (BIG & CLEAN)", fill=(255, 225, 180))

# Left side: User Reference (w=420, h=450)
ref_w = 420
ref_h = int(user_ref.height * ref_w / user_ref.width)
ref_scaled = user_ref.resize((ref_w, ref_h), Image.Resampling.LANCZOS)
canvas.paste(ref_scaled, (50, 110))
draw.rectangle((50, 110, 50 + ref_w, 110 + ref_h), outline=(255, 180, 80), width=3)
draw.text((50, 110 + ref_h + 15), "YOUR REFERENCE: Cloud Nine", fill=(255, 200, 120))
draw.text((50, 110 + ref_h + 40), "• Chunky, bold, rounded handwritten", fill=(180, 180, 190))
draw.text((50, 110 + ref_h + 65), "• Pure glowing white on sky background", fill=(180, 180, 190))
draw.text((50, 110 + ref_h + 90), "• Giant display size", fill=(180, 180, 190))

# Right side: 3 Full Hook Renders (Chewy, Sniglet, Balsamiq Sans)
# We can show 3 horizontal panels or cards
options = [
    ("OPTION A: CHEWY (Bouncy Chunky Marker — Closest Hand-Lettered Match)", "Chewy", 510, 110),
    ("OPTION B: SNIGLET EXTRABOLD (Puffy Cloud Rounded — Ultra Soft & Friendly)", "Sniglet", 510, 420),
    ("OPTION C: BALSAMIQ SANS BOLD (Clean Rounded Sans — High Symmetry)", "BalsamiqSans", 510, 730),
]

for title, fid, x, y in options:
    im_path = os.path.join(brain, f"akon_bigclean_{fid}_hook.png")
    if os.path.exists(im_path):
        frame = Image.open(im_path)
        # Crop center (w=1500, h=650) from 1920x1080 and resize to w=1360, h=270
        crop = frame.crop((210, 240, 1710, 840)).resize((1360, 270), Image.Resampling.LANCZOS)
        canvas.paste(crop, (x, y))
        draw.rectangle((x, y, x + 1360, y + 270), outline=(100, 160, 255), width=2)
        # Label pill
        draw.rectangle((x, y, x + 850, y + 35), fill=(20, 24, 45))
        draw.text((x + 15, y + 8), title, fill=(200, 230, 255))

out_comp = os.path.join(brain, "side_by_side_hook_comparison.png")
canvas.save(out_comp, "PNG")
print(f"Saved {out_comp}")
