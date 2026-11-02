import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import cv2

def regenerate_night_thumbs():
    fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
    brain_dir = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
    thumb_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail"
    video_p = os.path.join(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos", "real_nature_tin_roof_night_1min_sample.mp4")

    cap = cv2.VideoCapture(video_p)
    cap.set(cv2.CAP_PROP_POS_MSEC, 10000)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Failed to read frame")
        return

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    base = Image.fromarray(frame_rgb)
    W, H = base.size

    # Dark overlay to give title 14:1 contrast pop
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    vd.rectangle([(0, 0), (W, H)], fill=(0, 5, 10, 50))
    base = Image.alpha_composite(base.convert("RGBA"), vignette)

    # =========================================================================
    # THUMBNAIL A: 7clouds Style (Edo SZ Brush Font)
    # =========================================================================
    thumb_7c = base.copy()
    edo_font = ImageFont.truetype(os.path.join(fonts_dir, "edosz.ttf"), 140)
    sub_font = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 48)

    title = "RAIN ON TIN ROOF AT NIGHT"
    sub = "HEAVY RAIN & DEEP THUNDER • DARK SCREEN FOR SLEEP"

    draw_d = ImageDraw.Draw(thumb_7c)
    bbox_t = draw_d.textbbox((0, 0), title, font=edo_font)
    tw, th = bbox_t[2] - bbox_t[0], bbox_t[3] - bbox_t[1]
    bbox_s = draw_d.textbbox((0, 0), sub, font=sub_font)
    sw, sh = bbox_s[2] - bbox_s[0], bbox_s[3] - bbox_s[1]

    gap = 32
    total_h = th + gap + sh
    start_y = (H - total_h) // 2 - 15
    tx = (W - tw) // 2 - bbox_t[0]
    sx = (W - sw) // 2 - bbox_s[0]

    s_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(s_layer)
    sd.text((tx + 8, start_y + 12), title, font=edo_font, fill=(0, 0, 0, 245))
    sd.text((sx + 5, start_y + th + gap + 7), sub, font=sub_font, fill=(0, 0, 0, 220))
    s_layer = s_layer.filter(ImageFilter.GaussianBlur(5))
    thumb_7c = Image.alpha_composite(thumb_7c, s_layer)

    t_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    td = ImageDraw.Draw(t_layer)
    td.text((tx, start_y), title, font=edo_font, fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(5, 10, 20, 180))
    td.text((sx, start_y + th + gap), sub, font=sub_font, fill=(235, 245, 255, 245), stroke_width=1, stroke_fill=(5, 10, 20, 150))
    thumb_7c = Image.alpha_composite(thumb_7c, t_layer).convert("RGB")

    out_7c = os.path.join(brain_dir, "night_rain_thumb_7clouds.jpg")
    thumb_7c.save(out_7c, quality=95)
    thumb_7c.save(os.path.join(thumb_dir, "night_rain_thumb_7clouds.jpg"), quality=95)
    thumb_7c.resize((960, 540), Image.Resampling.LANCZOS).save(os.path.join(brain_dir, "preview_night_rain_thumb_7clouds.jpg"))
    print("Regenerated 7clouds Night Thumbnail:", out_7c)

    # =========================================================================
    # THUMBNAIL B: LatinHype Style (Bebas Neue Condensed)
    # =========================================================================
    thumb_lh = base.copy()
    bebas_font = ImageFont.truetype(os.path.join(fonts_dir, "BebasNeue-Regular.ttf"), 165)

    title_lh = "HEAVY RAIN ON TIN ROOF AT NIGHT"
    sub_lh = "DARK SCREEN FOR SLEEP • INSOMNIA RELIEF"

    bbox_tlh = draw_d.textbbox((0, 0), title_lh, font=bebas_font)
    tlw, tlh = bbox_tlh[2] - bbox_tlh[0], bbox_tlh[3] - bbox_tlh[1]
    bbox_slh = draw_d.textbbox((0, 0), sub_lh, font=sub_font)
    slw, slh = bbox_slh[2] - bbox_slh[0], bbox_slh[3] - bbox_slh[1]

    total_hlh = tlh + gap + slh
    start_ylh = (H - total_hlh) // 2 - 15
    tlx = (W - tlw) // 2 - bbox_tlh[0]
    slx = (W - slw) // 2 - bbox_slh[0]

    s_layer2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd2 = ImageDraw.Draw(s_layer2)
    sd2.text((tlx + 7, start_ylh + 9), title_lh, font=bebas_font, fill=(0, 5, 10, 245))
    sd2.text((slx + 5, start_ylh + tlh + gap + 7), sub_lh, font=sub_font, fill=(0, 5, 10, 220))
    s_layer2 = s_layer2.filter(ImageFilter.GaussianBlur(1.5))
    thumb_lh = Image.alpha_composite(thumb_lh, s_layer2)

    t_layer2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    td2 = ImageDraw.Draw(t_layer2)
    td2.text((tlx, start_ylh), title_lh, font=bebas_font, fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(5, 10, 20, 180))
    td2.text((slx, start_ylh + tlh + gap), sub_lh, font=sub_font, fill=(235, 245, 255, 245), stroke_width=1, stroke_fill=(5, 10, 20, 150))
    thumb_lh = Image.alpha_composite(thumb_lh, t_layer2).convert("RGB")

    out_lh = os.path.join(brain_dir, "night_rain_thumb_latinhype.jpg")
    thumb_lh.save(out_lh, quality=95)
    thumb_lh.save(os.path.join(thumb_dir, "night_rain_thumb_latinhype.jpg"), quality=95)
    thumb_lh.resize((960, 540), Image.Resampling.LANCZOS).save(os.path.join(brain_dir, "preview_night_rain_thumb_latinhype.jpg"))
    print("Regenerated LatinHype Night Thumbnail:", out_lh)

if __name__ == "__main__":
    regenerate_night_thumbs()
