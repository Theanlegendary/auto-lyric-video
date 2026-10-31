import os
import sys
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding='utf-8')

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

# 1920x1080 comparison canvas
canvas = Image.new("RGB", (1920, 1080), (14, 10, 18))
draw = ImageDraw.Draw(canvas)

# Header
draw.rectangle((0, 0, 1920, 80), fill=(24, 14, 10))
draw.text((60, 26), "CONCEPT EVALUATION: MINIMAL SKY vs. EMOTIONAL VIBE CHARACTER (SPOTIFY 50/50 STYLE)", fill=(255, 210, 160))

# Left side: Clear Sunset Sky (no character)
p_sky = os.path.join(brain, "preview_spotify_orange_hook.png")
if os.path.exists(p_sky):
    im_sky = Image.open(p_sky).resize((880, 495), Image.Resampling.LANCZOS)
    canvas.paste(im_sky, (60, 110))
    draw.rectangle((60, 110, 940, 605), outline=(255, 160, 80), width=3)
    draw.rectangle((60, 110, 450, 150), fill=(20, 12, 10))
    draw.text((75, 122), "OPTION 1: PURE CLEAR SKY (RDR Orange)", fill=(255, 200, 120))

# Right side: Solitary Character Vibe (Guy on ledge watching sunset)
p_char = os.path.join(brain, "vibe_concept_sharp_with_lyrics.png")
if os.path.exists(p_char):
    im_char = Image.open(p_char).resize((880, 495), Image.Resampling.LANCZOS)
    canvas.paste(im_char, (980, 110))
    draw.rectangle((980, 110, 1860, 605), outline=(100, 180, 255), width=3)
    draw.rectangle((980, 110, 1420, 150), fill=(10, 20, 35))
    draw.text((995, 122), "OPTION 2: VIBE CHARACTER (Solitary Guy on Ledge)", fill=(180, 220, 255))

# Bottom row: Soft-blurred Frosted Bokeh Character
p_soft = os.path.join(brain, "vibe_concept_softblur_with_lyrics.png")
if os.path.exists(p_soft):
    im_soft = Image.open(p_soft).resize((880, 400), Image.Resampling.LANCZOS)
    canvas.paste(im_soft, (60, 630))
    draw.rectangle((60, 630, 940, 1030), outline=(200, 120, 255), width=2)
    draw.rectangle((60, 630, 480, 670), fill=(30, 15, 40))
    draw.text((75, 642), "OPTION 2B: FROSTED BOKEH VIBE CHARACTER", fill=(240, 200, 255))

# Bottom Right: Title Card with Vibe Character
p_title = os.path.join(brain, "vibe_concept_title.png")
if os.path.exists(p_title):
    im_title = Image.open(p_title).resize((880, 400), Image.Resampling.LANCZOS)
    canvas.paste(im_title, (980, 630))
    draw.rectangle((980, 630, 1860, 1030), outline=(255, 220, 100), width=2)
    draw.rectangle((980, 630, 1400, 670), fill=(35, 30, 10))
    draw.text((995, 642), "TITLE CARD WITH VIBE CHARACTER", fill=(255, 230, 150))

out_path = os.path.join(brain, "vibe_character_concept_showcase.png")
canvas.save(out_path, "PNG")
print(f"Saved master showcase: {out_path}")
