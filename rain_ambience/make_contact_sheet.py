import os
from PIL import Image, ImageDraw, ImageFont

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
ids = ["17717129", "6507556", "6252535", "5197762", "6252550", "8249126", "6107944", "4184130", "7401029", "4392382"]

# Grid: 2 rows of 5 columns
# Each thumb: 384 x 216
grid_w = 384 * 5
grid_h = 216 * 2 + 80
grid_img = Image.new("RGB", (grid_w, grid_h), (15, 20, 25))
draw = ImageDraw.Draw(grid_img)

fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
font = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 20)

for idx, vid in enumerate(ids):
    frame_p = os.path.join(brain, f"cand_frame_{vid}.jpg")
    if os.path.exists(frame_p):
        im = Image.open(frame_p)
        im_thumb = im.resize((384, 216), Image.Resampling.LANCZOS)
        row = idx // 5
        col = idx % 5
        x = col * 384
        y = 50 + row * 216
        grid_img.paste(im_thumb, (x, y))
        draw.text((x + 10, y + 10), f"ID: {vid}", font=font, fill=(0, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))

draw.text((20, 15), "REAL NATURE RAIN CANDIDATES (Pexels 1080p Real Camera Footage)", font=font, fill=(255, 255, 255))

contact_path = os.path.join(brain, "contact_sheet_candidates.jpg")
grid_img.save(contact_path, quality=90)
print("Saved contact sheet:", contact_path)
