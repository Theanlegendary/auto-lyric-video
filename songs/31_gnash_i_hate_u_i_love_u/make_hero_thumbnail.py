from PIL import Image, ImageDraw, ImageFont
import numpy as np

bg_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\31_gnash_i_hate_u_i_love_u\bg_clear_sky_sea_blue.png"
font_edo = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts\edosz.ttf"
font_sans = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts\Poppins-SemiBold.ttf"

base = Image.open(bg_path).convert("RGBA")
overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Exactly like Edwin McCain "I'LL BE" and "BEST PART" (65M / 245M views)
f_title = ImageFont.truetype(font_edo, 190)
f_sub = ImageFont.truetype(font_sans, 44)

text1 = "I HATE U, I LOVE U"
text2 = "GNASH ft. OLIVIA O'BRIEN"

bbox1 = draw.textbbox((0, 0), text1, font=f_title)
w1 = bbox1[2] - bbox1[0]
h1 = bbox1[3] - bbox1[1]

bbox2 = draw.textbbox((0, 0), text2, font=f_sub)
w2 = bbox2[2] - bbox2[0]

x1 = (1920 - w1) // 2
y1 = 370

x2 = (1920 - w2) // 2
y2 = y1 + h1 + 55

# Multi-pass atmospheric drop shadow for 100% legibility on mobile
for dx, dy in [(-5, -5), (5, -5), (-5, 5), (5, 5), (0, 6), (0, 10), (0, 14), (6, 6), (-6, 6)]:
    draw.text((x1 + dx, y1 + dy), text1, font=f_title, fill=(10, 20, 35, 180))
for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (0, 4), (0, 6)]:
    draw.text((x2 + dx, y2 + dy), text2, font=f_sub, fill=(10, 20, 35, 200))

# Pure white text
draw.text((x1, y1), text1, font=f_title, fill=(255, 255, 255, 255))
draw.text((x2, y2), text2, font=f_sub, fill=(255, 255, 255, 240))

final_img = Image.alpha_composite(base, overlay).convert("RGB")
out_p = r"C:\Users\DELL\.gemini\antigravity\brain\d46be2a3-51af-4b7e-8ca8-fe1d429e1056\thumbnail_official_7clouds_style.png"
final_img.save(out_p, quality=95)

# Save standard YouTube Studio 1280x720 thumbnail
thumb_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\31_gnash_i_hate_u_i_love_u\thumbnail_1280x720.jpg"
final_img.resize((1280, 720), Image.Resampling.LANCZOS).save(thumb_path, quality=95)
print("Saved thumbnail_official_7clouds_style.png and thumbnail_1280x720.jpg successfully!")
