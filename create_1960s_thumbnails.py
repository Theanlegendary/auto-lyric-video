import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
out_dir = base / "thumbnail_1960s"
out_dir.mkdir(parents=True, exist_ok=True)

# Base background: Stephen Sanchez pink sunset & pine ridge
bg_path = base / "stock_anime_bgs" / "14_anime_clear_pink_aesthetic_twilight_sky.png"
orig_img = Image.open(bg_path).convert("RGBA").resize((1280, 720), Image.Resampling.LANCZOS)

# Fonts
font_bookman_bold = "C:/Windows/Fonts/BOOKOSB.TTF"
font_bookman = "C:/Windows/Fonts/BOOKOS.TTF"
font_georgia_bold = "C:/Windows/Fonts/georgiab.ttf"
font_fredoka = str(base / "fonts" / "Fredoka.ttf")
font_patrick = str(base / "fonts" / "PatrickHand.ttf")

def apply_1960s_kodachrome_grading(im):
    # Convert to RGB numpy array
    arr = np.array(im.convert("RGB"), dtype=np.float32)
    # 1960s warm Technicolor/Kodachrome curve:
    # Boost reds and warm amber in midtones, rich cyan/indigo in shadows, compress highlights
    arr[:, :, 0] = np.clip(arr[:, :, 0] * 1.08 + 8, 0, 255) # Red boost
    arr[:, :, 1] = np.clip(arr[:, :, 1] * 1.02 + 2, 0, 255) # Green warm
    arr[:, :, 2] = np.clip(arr[:, :, 2] * 0.90 - 4, 0, 255) # Blue drop for honey warmth
    # Add subtle vintage warm film fade (lift blacks slightly)
    arr = arr * 0.92 + 18.0
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    graded = Image.fromarray(arr).convert("RGBA")
    
    # Add subtle warm film vignette
    vignette = Image.new("L", (1280, 720), 0)
    draw_v = ImageDraw.Draw(vignette)
    for r in range(400, 850, 15):
        alpha = int(((r - 400) / 450.0) ** 1.8 * 140)
        draw_v.ellipse((640 - r, 360 - int(r*0.65), 640 + r, 360 + int(r*0.65)), outline=alpha, width=16)
    vignette = vignette.filter(ImageFilter.GaussianBlur(radius=30))
    vig_layer = Image.new("RGBA", (1280, 720), (18, 10, 8, 0))
    vig_layer.putalpha(vignette)
    
    return Image.alpha_composite(graded, vig_layer)

print("1. Creating Mockup A: 1960s 45-RPM Vinyl Record Jacket...")
# -------------------------------------------------------------------------
# MOCKUP A: 1960s 45-RPM Vinyl Record Jacket
# -------------------------------------------------------------------------
canvas_a = Image.new("RGBA", (1280, 720), (22, 18, 26, 255))

# Draw Vinyl Record peeking out from the right (X: 820 to 1340)
vinyl_center_x = 1080
vinyl_center_y = 360
vinyl_radius = 330
vinyl_layer = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
draw_vinyl = ImageDraw.Draw(vinyl_layer)

# Black vinyl disc
draw_vinyl.ellipse((vinyl_center_x - vinyl_radius, vinyl_center_y - vinyl_radius,
                    vinyl_center_x + vinyl_radius, vinyl_center_y + vinyl_radius), fill=(16, 16, 18, 255))

# Vinyl sound grooves (subtle concentric rings)
for r in range(145, 320, 4):
    opacity = 18 if r % 12 == 0 else 8
    draw_vinyl.ellipse((vinyl_center_x - r, vinyl_center_y - r,
                        vinyl_center_x + r, vinyl_center_y + r), outline=(255, 255, 255, opacity), width=1)

# Vinyl center label (classic orange/yellow 1960s Columbia/RCA Victor label)
label_radius = 125
draw_vinyl.ellipse((vinyl_center_x - label_radius, vinyl_center_y - label_radius,
                    vinyl_center_x + label_radius, vinyl_center_y + label_radius), fill=(235, 75, 45, 255))
# Inner white ring
draw_vinyl.ellipse((vinyl_center_x - 110, vinyl_center_y - 110,
                    vinyl_center_x + 110, vinyl_center_y + 110), outline=(255, 240, 200, 200), width=2)
# Center spindle hole
draw_vinyl.ellipse((vinyl_center_x - 24, vinyl_center_y - 24,
                    vinyl_center_x + 24, vinyl_center_y + 24), fill=(22, 18, 26, 255), outline=(100, 100, 100, 255), width=2)

# Label text
font_label_sm = ImageFont.truetype(font_georgia_bold, 14)
font_label_xs = ImageFont.truetype(font_bookman, 11)
draw_vinyl.text((vinyl_center_x - 55, vinyl_center_y - 75), "FADE REPLAY", fill=(255, 255, 255), font=font_label_sm)
draw_vinyl.text((vinyl_center_x - 30, vinyl_center_y - 50), "45 R.P.M.", fill=(255, 240, 200), font=font_label_xs)
draw_vinyl.text((vinyl_center_x - 45, vinyl_center_y + 40), "HIGH FIDELITY", fill=(255, 255, 255), font=font_label_xs)

canvas_a = Image.alpha_composite(canvas_a, vinyl_layer)

# Now paste the Album Sleeve Jacket on the left (X: 30 to 860, Y: 30 to 690)
sleeve_w = 830
sleeve_h = 660
sleeve_x = 35
sleeve_y = 30

# Crop and grade anime artwork for sleeve
art_graded = apply_1960s_kodachrome_grading(orig_img)
sleeve_art = art_graded.crop((0, 30, 1100, 690)).resize((sleeve_w, sleeve_h), Image.Resampling.LANCZOS)

# Create sleeve base with aged cardboard border
sleeve = Image.new("RGBA", (sleeve_w, sleeve_h), (242, 236, 222, 255))
# Paste art inside 14px cream frame
inner_art = sleeve_art.crop((14, 14, sleeve_w - 14, sleeve_h - 14))
sleeve.paste(inner_art, (14, 14))

# Add classic 1960s "STEREO 360 SOUND" top banner across jacket
draw_sleeve = ImageDraw.Draw(sleeve)
banner_h = 58
draw_sleeve.rectangle((14, 14, sleeve_w - 14, 14 + banner_h), fill=(244, 238, 224, 240))
# Stereo arrows
font_banner = ImageFont.truetype(font_georgia_bold, 20)
font_banner_sub = ImageFont.truetype(font_bookman, 11)
draw_sleeve.text((35, 28), "◄◄◄ STEREO 360 SOUND ►►►", fill=(25, 20, 28), font=font_banner)
draw_sleeve.text((sleeve_w - 220, 33), "CS 9140 • HIGH FIDELITY", fill=(80, 70, 75), font=font_banner_sub)

# Subtle vinyl ring wear impression on cardboard sleeve
ring_wear = Image.new("RGBA", (sleeve_w, sleeve_h), (0, 0, 0, 0))
draw_rw = ImageDraw.Draw(ring_wear)
draw_rw.ellipse((-80, -40, 750, 700), outline=(255, 255, 255, 22), width=35)
draw_rw.ellipse((-90, -50, 760, 710), outline=(0, 0, 0, 18), width=25)
ring_wear = ring_wear.filter(ImageFilter.GaussianBlur(radius=8))
sleeve = Image.alpha_composite(sleeve, ring_wear)

# Main 1960s Album Typography on Jacket
draw_sleeve = ImageDraw.Draw(sleeve)
font_title = ImageFont.truetype(font_bookman_bold, 54)
font_artist = ImageFont.truetype(font_georgia_bold, 32)
font_hook = ImageFont.truetype(font_bookman, 18)

# Title: UNTIL I FOUND YOU (in warm cream with dark chocolate drop shadow)
t_text = "UNTIL I FOUND YOU"
a_text = "STEPHEN SANCHEZ"
h_text = "FEATURING THE HIT ROMANTIC BALLAD • ORIGINAL 1960s RECORDING"

# Drop shadow
draw_sleeve.text((43, 443), t_text, fill=(20, 12, 18, 230), font=font_title)
draw_sleeve.text((40, 440), t_text, fill=(255, 245, 220, 255), font=font_title)

# Artist in golden mustard
draw_sleeve.text((42, 517), a_text, fill=(20, 12, 18, 230), font=font_artist)
draw_sleeve.text((40, 515), a_text, fill=(255, 195, 75, 255), font=font_artist)

# Vintage badge at bottom
draw_sleeve.rectangle((40, 580, sleeve_w - 40, 618), fill=(25, 18, 28, 220))
draw_sleeve.text((55, 590), h_text, fill=(240, 230, 215), font=font_hook)

# Paste sleeve onto canvas with shadow
sleeve_shadow = Image.new("RGBA", (sleeve_w + 30, sleeve_h + 30), (0, 0, 0, 0))
draw_ss = ImageDraw.Draw(sleeve_shadow)
draw_ss.rectangle((10, 10, sleeve_w + 20, sleeve_h + 20), fill=(0, 0, 0, 140))
sleeve_shadow = sleeve_shadow.filter(ImageFilter.GaussianBlur(radius=15))

canvas_a.paste(sleeve_shadow, (sleeve_x - 10, sleeve_y - 10), sleeve_shadow)
canvas_a.paste(sleeve, (sleeve_x, sleeve_y))

# Save Mockup A
out_a = out_dir / "thumbnail_1960s_vinyl_jacket.png"
canvas_a.save(out_a)
canvas_a.save(brain / "thumbnail_1960s_vinyl_jacket.png")
print("  -> Saved Mockup A:", out_a)

print("2. Creating Mockup B: 1960s 35mm Kodachrome Slide Transparency...")
# -------------------------------------------------------------------------
# MOCKUP B: 1960s Kodachrome Slide Film Mount
# -------------------------------------------------------------------------
# Authentic cardboard 35mm slide mount: off-white cream border with red Kodak stamp
canvas_b = Image.new("RGBA", (1280, 720), (28, 24, 22, 255))

# Outer cardboard mount (X: 140 to 1140, Y: 30 to 690)
mount_w = 1000
mount_h = 660
mount_x = 140
mount_y = 30

mount = Image.new("RGBA", (mount_w, mount_h), (246, 241, 230, 255))
draw_m = ImageDraw.Draw(mount)

# Inner window for the transparency film (X: 70 to 930, Y: 100 to 580)
win_x = 65
win_y = 95
win_w = mount_w - 130
win_h = mount_h - 190

# Transparency image: Kodachrome color graded with rich saturation
slide_art = apply_1960s_kodachrome_grading(orig_img).resize((win_w, win_h), Image.Resampling.LANCZOS)
mount.paste(slide_art, (win_x, win_y))

# Inner border bevel/shadow
draw_m.rectangle((win_x, win_y, win_x + win_w, win_y + win_h), outline=(120, 110, 100, 180), width=3)
draw_m.rectangle((win_x - 3, win_y - 3, win_x + win_w + 3, win_y + win_h + 3), outline=(40, 35, 30, 60), width=2)

# Top Stamps: Classic Red "KODACHROME TRANSPARENCY"
font_stamp_lg = ImageFont.truetype(font_georgia_bold, 24)
font_stamp_sm = ImageFont.truetype(font_bookman, 13)
draw_m.text((win_x + 10, 35), "KODACHROME", fill=(195, 35, 25), font=font_stamp_lg)
draw_m.text((win_x + 225, 42), "TRANSPARENCY", fill=(80, 75, 70), font=font_stamp_sm)
draw_m.text((mount_w - 230, 40), "OCT 65 • ROLL 12", fill=(110, 100, 95), font=font_stamp_sm)

# Bottom Stamps: Song details typed on cardboard mount
font_typed = ImageFont.truetype(font_bookman_bold, 21)
font_typed_sub = ImageFont.truetype(font_bookman, 14)
draw_m.text((win_x + 10, mount_h - 70), "STEPHEN SANCHEZ — \"UNTIL I FOUND YOU\"", fill=(30, 25, 25), font=font_typed)
draw_m.text((win_x + 10, mount_h - 40), "PROCESSED BY FADE REPLAY LABS • 35MM COLOR FILM", fill=(120, 110, 105), font=font_typed_sub)
draw_m.text((mount_w - 180, mount_h - 55), "MADE IN U.S.A.", fill=(150, 140, 135), font=font_typed_sub)

# Lyric hook on transparency inside the slide
draw_art = ImageDraw.Draw(mount)
font_art_title = ImageFont.truetype(font_fredoka, 48)
draw_art.text((win_x + 38, win_y + win_h - 98), "\"I WOULD NEVER FALL IN LOVE AGAIN...\"", fill=(20, 10, 15, 200), font=font_art_title)
draw_art.text((win_x + 35, win_y + win_h - 100), "\"I WOULD NEVER FALL IN LOVE AGAIN...\"", fill=(255, 245, 220, 255), font=font_art_title)

# Paste mount onto dark vintage studio desk
mount_shadow = Image.new("RGBA", (mount_w + 40, mount_h + 40), (0, 0, 0, 0))
draw_ms = ImageDraw.Draw(mount_shadow)
draw_ms.rectangle((15, 15, mount_w + 25, mount_h + 25), fill=(0, 0, 0, 180))
mount_shadow = mount_shadow.filter(ImageFilter.GaussianBlur(radius=20))

canvas_b.paste(mount_shadow, (mount_x - 15, mount_y - 15), mount_shadow)
canvas_b.paste(mount, (mount_x, mount_y))

# Save Mockup B
out_b = out_dir / "thumbnail_1960s_kodachrome_slide.png"
canvas_b.save(out_b)
canvas_b.save(brain / "thumbnail_1960s_kodachrome_slide.png")
print("  -> Saved Mockup B:", out_b)

print("3. Creating Mockup C: 1960s French New Wave / Retro Cinema Poster...")
# -------------------------------------------------------------------------
# MOCKUP C: 1960s Retro Cinema Poster / Tri-Color Mid-Century Book Cover
# -------------------------------------------------------------------------
canvas_c = apply_1960s_kodachrome_grading(orig_img)
draw_c = ImageDraw.Draw(canvas_c)

# Add 1960s Halftone Paper & Edge Wear
# Top retro header bar (deep wine red / crimson)
header_h = 75
draw_c.rectangle((0, 0, 1280, header_h), fill=(140, 24, 45, 235))
draw_c.line((0, header_h, 1280, header_h), fill=(255, 215, 120, 255), width=3)

font_c_top = ImageFont.truetype(font_georgia_bold, 22)
font_c_sub = ImageFont.truetype(font_bookman, 13)
draw_c.text((45, 25), "A FADE REPLAY RETRO SOUNDSTAGE SELECTION", fill=(255, 245, 225), font=font_c_top)
draw_c.text((1280 - 240, 28), "SERIES 1965 • VOL. IV", fill=(255, 215, 120), font=font_c_sub)

# Vintage 1960s Motel Starburst Neon Badge on Top-Right
badge_layer = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
draw_bg = ImageDraw.Draw(badge_layer)
# Diamond badge
badge_center = (1120, 220)
bw = 110
bh = 70
pts = [
    (badge_center[0], badge_center[1] - bh),
    (badge_center[0] + bw, badge_center[1]),
    (badge_center[0], badge_center[1] + bh),
    (badge_center[0] - bw, badge_center[1])
]
draw_bg.polygon(pts, fill=(245, 185, 40, 230), outline=(255, 255, 255, 255))
font_badge_1 = ImageFont.truetype(font_georgia_bold, 16)
font_badge_2 = ImageFont.truetype(font_bookman_bold, 13)
draw_bg.text((badge_center[0] - 50, badge_center[1] - 25), "ORIGINAL", fill=(20, 15, 20), font=font_badge_1)
draw_bg.text((badge_center[0] - 38, badge_center[1] - 3), "1960s", fill=(140, 24, 45), font=font_badge_1)
draw_bg.text((badge_center[0] - 44, badge_center[1] + 18), "DOO-WOP", fill=(20, 15, 20), font=font_badge_2)

canvas_c = Image.alpha_composite(canvas_c, badge_layer)
draw_c = ImageDraw.Draw(canvas_c)

# Bold 1960s Typography at Center-Left
font_main_title = ImageFont.truetype(font_bookman_bold, 76)
font_main_artist = ImageFont.truetype(font_georgia_bold, 38)
font_main_lyrics = ImageFont.truetype(font_fredoka, 28)

# Layered text with 1960s warm offset drop shadow
title_str = "UNTIL I FOUND YOU"
artist_str = "STEPHEN SANCHEZ"
lyrics_str = "♪ \"I would never fall in love until I found her...\""

# 3D Block shadow
for offset in range(5, 0, -1):
    draw_c.text((50 + offset, 440 + offset), title_str, fill=(35, 15, 25, 255), font=font_main_title)

# Main title face in creamy vintage eggshell
draw_c.text((50, 440), title_str, fill=(255, 250, 235, 255), font=font_main_title)

# Artist in glowing amber
draw_c.text((53, 538), artist_str, fill=(20, 10, 15, 220), font=font_main_artist)
draw_c.text((50, 535), artist_str, fill=(255, 205, 70, 255), font=font_main_artist)

# Lyric caption strip
draw_c.rectangle((45, 605, 820, 655), fill=(20, 12, 22, 220), outline=(255, 215, 120, 150), width=2)
draw_c.text((65, 615), lyrics_str, fill=(255, 245, 230), font=font_main_lyrics)

# Save Mockup C
out_c = out_dir / "thumbnail_1960s_cinema_poster.png"
canvas_c.save(out_c)
canvas_c.save(brain / "thumbnail_1960s_cinema_poster.png")
print("  -> Saved Mockup C:", out_c)

print("\nALL 3 1960s THUMBNAIL MOCKUPS SUCCESSFULLY GENERATED!")
