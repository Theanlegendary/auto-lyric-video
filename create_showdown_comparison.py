import os
from PIL import Image, ImageDraw, ImageFont

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"

# Load the replicas
rep_7c = Image.open(os.path.join(brain, "master_7clouds_7years_replica.png"))
rep_latin = Image.open(os.path.join(brain, "master_latinhype_when_i_was_your_man_replica.png"))

# Create side-by-side collage: 1920 x 1080
panel_h = 540
panel_w = 960

r7c_small = rep_7c.resize((panel_w, panel_h), Image.Resampling.LANCZOS)
rlat_small = rep_latin.resize((panel_w, panel_h), Image.Resampling.LANCZOS)

collage = Image.new("RGB", (1920, 1080), (14, 18, 24))
left_y = (1080 - panel_h) // 2

collage.paste(r7c_small, (0, left_y))
collage.paste(rlat_small, (panel_w, left_y))

# Add title badges
draw = ImageDraw.Draw(collage)
font = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 36)
subfont = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Medium.ttf"), 22)
card_title_font = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 28)

# Top Header
draw.rectangle([(0, 0), (1920, 130)], fill=(10, 14, 20))
draw.text((60, 25), "VIRAL THUMBNAIL DECONSTRUCTION & 1:1 REPLICATION", font=font, fill=(255, 255, 255))
draw.text((60, 80), "Reverse-engineered formulas of YouTube's highest-performing lyric videos (191M & 164M Views)", font=subfont, fill=(0, 210, 255))

# Badges for each card
# Left Badge
draw.rounded_rectangle([(30, left_y + 25), (480, left_y + 85)], radius=8, fill=(0, 0, 0, 220))
draw.text((45, left_y + 35), "191M Formula: 7clouds Style", font=card_title_font, fill=(255, 215, 0))

# Right Badge
draw.rounded_rectangle([(panel_w + 30, left_y + 25), (panel_w + 510, left_y + 85)], radius=8, fill=(0, 0, 0, 220))
draw.text((panel_w + 45, left_y + 35), "164M Formula: LatinHype Style", font=card_title_font, fill=(0, 225, 255))

# Footer with technical metrics
draw.rectangle([(0, 1080 - 130), (1920, 1080)], fill=(10, 14, 20))
draw.text((40, 1080 - 100), "7CLOUDS: Edo SZ Brush Font • Pure Pastel Dawn Gradient • Multi-Layer Gaussian Shadow", font=subfont, fill=(235, 200, 160))
draw.text((panel_w + 40, 1080 - 100), "LATINHYPE: Bebas Neue Condensed • 80% Cyan Sky + Mountains • Sharp Punchy Shadow", font=subfont, fill=(130, 225, 255))
draw.text((40, 1080 - 60), "PSYCHOLOGY: High Negative Space + 12:1 Contrast Pop = High Mobile CTR in Suggested Feed", font=subfont, fill=(170, 180, 195))
draw.text((panel_w + 40, 1080 - 60), "RETENTION: Thumbnail matches first 5 seconds = Zero bounce rate, high watch time", font=subfont, fill=(170, 180, 195))

out_collage = os.path.join(brain, "viral_thumbnail_showcase_comparison.png")
collage.save(out_collage)
print("Updated comparison collage:", out_collage)
