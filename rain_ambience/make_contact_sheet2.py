import os
from PIL import Image, ImageDraw, ImageFont

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
ids = ["4059614", "18154174", "3999402", "17843344", "7843122", "4169229", "9454925", "5091073", "4169213", "5112049", "1774955", "3700375"]

# Grid: 3 rows of 4 columns
grid_w = 400 * 4
grid_h = 225 * 3 + 80
grid_img = Image.new("RGB", (grid_w, grid_h), (12, 16, 22))
draw = ImageDraw.Draw(grid_img)

fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
font = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 20)

for idx, vid in enumerate(ids):
    frame_p = os.path.join(brain, f"cand2_frame_{vid}.jpg")
    if os.path.exists(frame_p):
        im = Image.open(frame_p)
        im_thumb = im.resize((400, 225), Image.Resampling.LANCZOS)
        row = idx // 4
        col = idx % 4
        x = col * 400
        y = 50 + row * 225
        grid_img.paste(im_thumb, (x, y))
        draw.text((x + 10, y + 10), f"ID: {vid}", font=font, fill=(0, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))

draw.text((20, 15), "REAL NATURE RAIN CANDIDATES BATCH 2 (Pexels 1080p Real Camera)", font=font, fill=(255, 255, 255))

contact_path = os.path.join(brain, "contact_sheet_batch2.jpg")
grid_img.save(contact_path, quality=90)
print("Saved contact sheet batch 2:", contact_path)
