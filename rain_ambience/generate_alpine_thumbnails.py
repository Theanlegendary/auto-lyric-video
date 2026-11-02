import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

def create_thumbnails():
    base_img_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail\nature_options\alpine_lake_tiny_fireflies_preview.jpg"
    thumb_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail"
    brain_dir = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
    fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"

    if not os.path.exists(base_img_path):
        print(f"Error: {base_img_path} not found!")
        return

    base_cv = cv2.imread(base_img_path)
    base_cv = cv2.resize(base_cv, (1280, 720))

    font_heavy = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 54)
    font_sub = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 26)
    font_badge = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 18)

    # -------------------------------------------------------------
    # THUMBNAIL 1: "FALL ASLEEP IN 3 MINUTES" (CTR MAGNET)
    # -------------------------------------------------------------
    # Deepen left side with smooth gradient for maximum text readability
    t1_cv = base_cv.copy()
    grad_mask = np.zeros((720, 1280), dtype=np.float32)
    for x in range(1280):
        # Darker on the left where text sits
        grad_mask[:, x] = max(0.0, 1.0 - (x / 750.0))
    for c in range(3):
        t1_cv[:, :, c] = np.clip(t1_cv[:, :, c] * (1.0 - 0.75 * grad_mask), 0, 255).astype(np.uint8)

    t1_pil = Image.fromarray(cv2.cvtColor(t1_cv, cv2.COLOR_BGR2RGB))
    draw1 = ImageDraw.Draw(t1_pil)

    # Top Badge
    draw1.rounded_rectangle([50, 48, 360, 92], radius=8, fill=(2, 132, 199))
    draw1.text((70, 56), "3 HOURS • DEEP SLEEP", font=font_badge, fill=(255, 255, 255))

    # Main Headline
    draw1.text((50, 120), "FALL ASLEEP", font=font_heavy, fill=(255, 255, 255), stroke_width=4, stroke_fill=(5, 11, 20))
    draw1.text((50, 185), "IN 3 MINUTES", font=font_heavy, fill=(56, 189, 248), stroke_width=4, stroke_fill=(5, 11, 20))

    # Subtitle
    draw1.text((52, 275), "Heavy Rain on Alpine Lake • Gentle Fireflies", font=font_sub, fill=(226, 232, 240), stroke_width=2, stroke_fill=(5, 11, 20))
    draw1.text((52, 315), "Instant Insomnia & Anxiety Relief", font=font_sub, fill=(251, 191, 36), stroke_width=2, stroke_fill=(5, 11, 20))

    # Bottom Pill Badges
    pills = [("✨ 4K MOUNTAIN RAIN", (30, 41, 59)), ("💤 BLACK SCREEN SOUND", (15, 23, 42)), ("🌿 100% RELAXING", (6, 78, 59))]
    cur_x = 50
    for text, bg in pills:
        draw1.rounded_rectangle([cur_x, 620, cur_x + 230, 665], radius=6, fill=bg, outline=(56, 189, 248), width=1)
        draw1.text((cur_x + 16, 630), text, font=font_badge, fill=(255, 255, 255))
        cur_x += 245

    t1_path = os.path.join(thumb_dir, "alpine_lake_thumb_deep_sleep_magnet.jpg")
    t1_pil.save(t1_path, quality=95)
    t1_pil.save(os.path.join(brain_dir, "alpine_lake_thumb_deep_sleep_magnet.jpg"), quality=95)
    print("Saved Thumbnail 1:", t1_path)

    # -------------------------------------------------------------
    # THUMBNAIL 2: "CALMED BY NATURE" CLEAN AESTHETIC
    # -------------------------------------------------------------
    t2_cv = base_cv.copy()
    # Subtle vignette
    Y, X = np.ogrid[:720, :1280]
    dist = np.sqrt((X - 640)**2 + (Y - 360)**2)
    vign = np.clip(1.0 - 0.45 * (dist / 735)**2, 0.2, 1.0)[:, :, np.newaxis]
    t2_cv = np.clip(t2_cv * vign, 0, 255).astype(np.uint8)

    t2_pil = Image.fromarray(cv2.cvtColor(t2_cv, cv2.COLOR_BGR2RGB))
    draw2 = ImageDraw.Draw(t2_pil)

    # Centered / Bottom cinematic styling
    draw2.rounded_rectangle([50, 48, 300, 92], radius=8, fill=(16, 185, 129))
    draw2.text((68, 56), "🌿 NATURAL HEALING", font=font_badge, fill=(255, 255, 255))

    draw2.text((50, 120), "NIGHT RAIN", font=font_heavy, fill=(255, 255, 255), stroke_width=4, stroke_fill=(5, 11, 20))
    draw2.text((50, 185), "ON ALPINE LAKE", font=font_heavy, fill=(251, 191, 36), stroke_width=4, stroke_fill=(5, 11, 20))

    draw2.text((52, 275), "Gentle Fireflies & Pure Water Droplets", font=font_sub, fill=(226, 232, 240), stroke_width=2, stroke_fill=(5, 11, 20))
    draw2.text((52, 315), "3 Hours of Deep Peace & Natural Calm", font=font_sub, fill=(147, 197, 253), stroke_width=2, stroke_fill=(5, 11, 20))

    t2_path = os.path.join(thumb_dir, "alpine_lake_thumb_calmed_by_nature.jpg")
    t2_pil.save(t2_path, quality=95)
    t2_pil.save(os.path.join(brain_dir, "alpine_lake_thumb_calmed_by_nature.jpg"), quality=95)
    print("Saved Thumbnail 2:", t2_path)

if __name__ == "__main__":
    create_thumbnails()
