import os
from PIL import Image, ImageDraw, ImageFont

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
ids = ["9353501", "13180836", "8110359", "12717007", "11643791", "9328701", "5174040", "3134575", "4828773", "9934612", "5918481", "13446069"]

# Grid: 3 rows of 4 columns
grid_w = 400 * 4
grid_h = 225 * 3 + 80
grid_img = Image.new("RGB", (grid_w, grid_h), (10, 14, 20))
draw = ImageDraw.Draw(grid_img)

fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
font = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 20)

for idx, vid in enumerate(ids):
    frame_p = os.path.join(brain, f"wide_cand_{vid}.jpg")
    if os.path.exists(frame_p):
        im = Image.open(frame_p)
        im_thumb = im.resize((400, 225), Image.Resampling.LANCZOS)
        row = idx // 4
        col = idx % 4
        x = col * 400
        y = 50 + row * 225
        grid_img.paste(im_thumb, (x, y))
        draw.text((x + 10, y + 10), f"ID: {vid}", font=font, fill=(0, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))

draw.text((20, 15), "WIDE LANDSCAPE / BIG NATURE VIEW CANDIDATES (Pexels 1080p)", font=font, fill=(255, 255, 255))

contact_path = os.path.join(brain, "contact_sheet_wide_views.jpg")
grid_img.save(contact_path, quality=90)
print("Saved wide views contact sheet:", contact_path)
