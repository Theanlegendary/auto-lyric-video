import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import cv2

def create_thumbnails():
    fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
    brain_dir = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
    thumb_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail"
    os.makedirs(thumb_dir, exist_ok=True)

    # 1. Extract a high-res frame from our tin roof video
    video_raw = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\danny_louis_60s_raw.mp4"
    cap = cv2.VideoCapture(video_raw)
    cap.set(cv2.CAP_PROP_POS_MSEC, 15000)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Failed to capture frame")
        return

    # Convert BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    base_bg = Image.fromarray(frame_rgb)
    
    # Apply cinematic color grading: boost contrast & deep moody blue saturation
    enh_con = ImageEnhance.Contrast(base_bg)
    base_bg = enh_con.enhance(1.30)
    enh_col = ImageEnhance.Color(base_bg)
    base_bg = enh_col.enhance(1.25)
    
    # Darken slightly with a subtle vignette / top-bottom gradient so text pops with 15:1 contrast
    W, H = base_bg.size # 1920, 1080
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    v_draw = ImageDraw.Draw(vignette)
    # Center dark overlay for readability
    v_draw.rectangle([(0, 0), (W, H)], fill=(10, 15, 25, 60))
    base_bg = Image.alpha_composite(base_bg.convert("RGBA"), vignette)

    # =========================================================================
    # THUMBNAIL 1: 7CLOUDS STYLE FOR OUR RAIN (191M Formula)
    # Font: Edo SZ (Brush Stencil), soft Gaussian drop shadow
    # =========================================================================
    thumb_7c = base_bg.copy()
    edo_font = ImageFont.truetype(os.path.join(fonts_dir, "edosz.ttf"), 180)
    sub_font_7c = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 58)

    title_1 = "RAIN ON TIN ROOF"
    sub_1 = "HEAVY RAIN & DEEP THUNDER FOR SLEEP"

    draw_d = ImageDraw.Draw(thumb_7c)
    bbox_t1 = draw_d.textbbox((0, 0), title_1, font=edo_font)
    t1_w, t1_h = bbox_t1[2] - bbox_t1[0], bbox_t1[3] - bbox_t1[1]

    bbox_s1 = draw_d.textbbox((0, 0), sub_1, font=sub_font_7c)
    s1_w, s1_h = bbox_s1[2] - bbox_s1[0], bbox_s1[3] - bbox_s1[1]

    gap = 40
    total_h1 = t1_h + gap + s1_h
    start_y1 = (H - total_h1) // 2 - 20
    t1_x = (W - t1_w) // 2 - bbox_t1[0]
    s1_x = (W - s1_w) // 2 - bbox_s1[0]

    # Multi-layer Gaussian shadow
    shadow_layer1 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_draw1 = ImageDraw.Draw(shadow_layer1)
    s_draw1.text((t1_x + 8, start_y1 + 12), title_1, font=edo_font, fill=(0, 0, 0, 240))
    s_draw1.text((s1_x + 5, start_y1 + t1_h + gap + 7), sub_1, font=sub_font_7c, fill=(0, 0, 0, 220))
    shadow_layer1 = shadow_layer1.filter(ImageFilter.GaussianBlur(5))
    thumb_7c = Image.alpha_composite(thumb_7c, shadow_layer1)

    # Foreground white text with subtle dark rim
    text_layer1 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    t_draw1 = ImageDraw.Draw(text_layer1)
    t_draw1.text((t1_x, start_y1), title_1, font=edo_font, fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(15, 20, 30, 160))
    t_draw1.text((s1_x, start_y1 + t1_h + gap), sub_1, font=sub_font_7c, fill=(240, 245, 255, 245), stroke_width=1, stroke_fill=(15, 20, 30, 140))
    thumb_7c = Image.alpha_composite(thumb_7c, text_layer1).convert("RGB")

    out_7c_brain = os.path.join(brain_dir, "our_rain_thumbnail_7clouds_style.png")
    out_7c_thumb = os.path.join(thumb_dir, "our_rain_thumbnail_7clouds_style.png")
    thumb_7c.save(out_7c_brain, quality=95)
    thumb_7c.save(out_7c_thumb, quality=95)
    print("Saved 7clouds-style rain thumbnail:", out_7c_brain)

    # =========================================================================
    # THUMBNAIL 2: LATINHYPE STYLE FOR OUR RAIN (164M Formula)
    # Font: Bebas Neue (Tall Condensed Bold), sharp solid drop shadow
    # =========================================================================
    thumb_lh = base_bg.copy()
    bebas_font = ImageFont.truetype(os.path.join(fonts_dir, "BebasNeue-Regular.ttf"), 190)
    sub_font_lh = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 58)

    title_2 = "HEAVY RAIN ON TIN ROOF"
    sub_2 = "RELAXING SLEEP SOUNDS • INSOMNIA RELIEF"

    bbox_t2 = draw_d.textbbox((0, 0), title_2, font=bebas_font)
    t2_w, t2_h = bbox_t2[2] - bbox_t2[0], bbox_t2[3] - bbox_t2[1]

    bbox_s2 = draw_d.textbbox((0, 0), sub_2, font=sub_font_lh)
    s2_w, s2_h = bbox_s2[2] - bbox_s2[0], bbox_s2[3] - bbox_s2[1]

    total_h2 = t2_h + gap + s2_h
    start_y2 = (H - total_h2) // 2 - 20
    t2_x = (W - t2_w) // 2 - bbox_t2[0]
    s2_x = (W - s2_w) // 2 - bbox_s2[0]

    # Sharp solid drop shadow
    shadow_layer2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_draw2 = ImageDraw.Draw(shadow_layer2)
    s_draw2.text((t2_x + 7, start_y2 + 9), title_2, font=bebas_font, fill=(0, 5, 15, 245))
    s_draw2.text((s2_x + 5, start_y2 + t2_h + gap + 7), sub_2, font=sub_font_lh, fill=(0, 5, 15, 220))
    shadow_layer2 = shadow_layer2.filter(ImageFilter.GaussianBlur(1.5))
    thumb_lh = Image.alpha_composite(thumb_lh, shadow_layer2)

    # Foreground white text
    text_layer2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    t_draw2 = ImageDraw.Draw(text_layer2)
    t_draw2.text((t2_x, start_y2), title_2, font=bebas_font, fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(10, 15, 25, 180))
    t_draw2.text((s2_x, start_y2 + t2_h + gap), sub_2, font=sub_font_lh, fill=(240, 245, 255, 245), stroke_width=1, stroke_fill=(10, 15, 25, 150))
    thumb_lh = Image.alpha_composite(thumb_lh, text_layer2).convert("RGB")

    out_lh_brain = os.path.join(brain_dir, "our_rain_thumbnail_latinhype_style.png")
    out_lh_thumb = os.path.join(thumb_dir, "our_rain_thumbnail_latinhype_style.png")
    thumb_lh.save(out_lh_brain, quality=95)
    thumb_lh.save(out_lh_thumb, quality=95)
    print("Saved LatinHype-style rain thumbnail:", out_lh_brain)

if __name__ == "__main__":
    create_thumbnails()
