import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import cv2

def create_real_nature_thumbnails():
    fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
    brain_dir = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
    thumb_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail"
    clips_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips"

    # =========================================================================
    # 1. Primary Real Nature: Tin Roof Eaves Forest Rain (7843122)
    # =========================================================================
    clip_1 = os.path.join(clips_dir, "clip_7843122_tin_roof_forest_rain.mp4")
    cap = cv2.VideoCapture(clip_1)
    cap.set(cv2.CAP_PROP_POS_MSEC, 5000)
    ret, frame1 = cap.read()
    cap.release()

    if ret:
        frame_rgb = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
        base_1 = Image.fromarray(frame_rgb)
        
        # Color grade: contrast 1.28, rich green saturation
        base_1 = ImageEnhance.Contrast(base_1).enhance(1.28)
        base_1 = ImageEnhance.Color(base_1).enhance(1.22)

        W, H = base_1.size
        # Dark vignette for 12:1 text contrast
        vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        vd = ImageDraw.Draw(vignette)
        vd.rectangle([(0, 0), (W, H)], fill=(5, 10, 15, 65))
        base_1 = Image.alpha_composite(base_1.convert("RGBA"), vignette)

        # Style A: 7clouds Brush Stencil (191M Formula)
        thumb_7c = base_1.copy()
        edo_font = ImageFont.truetype(os.path.join(fonts_dir, "edosz.ttf"), 175)
        sub_font = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 54)

        title = "RAIN ON TIN ROOF"
        sub = "REAL NATURE SOUNDS FOR DEEP SLEEP & RELAXATION"

        draw_d = ImageDraw.Draw(thumb_7c)
        bbox_t = draw_d.textbbox((0, 0), title, font=edo_font)
        tw, th = bbox_t[2] - bbox_t[0], bbox_t[3] - bbox_t[1]
        bbox_s = draw_d.textbbox((0, 0), sub, font=sub_font)
        sw, sh = bbox_s[2] - bbox_s[0], bbox_s[3] - bbox_s[1]

        gap = 36
        total_h = th + gap + sh
        start_y = (H - total_h) // 2 - 15
        tx = (W - tw) // 2 - bbox_t[0]
        sx = (W - sw) // 2 - bbox_s[0]

        # Multi-layer Gaussian shadow
        s_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(s_layer)
        sd.text((tx + 8, start_y + 12), title, font=edo_font, fill=(0, 0, 0, 240))
        sd.text((sx + 5, start_y + th + gap + 7), sub, font=sub_font, fill=(0, 0, 0, 220))
        s_layer = s_layer.filter(ImageFilter.GaussianBlur(5))
        thumb_7c = Image.alpha_composite(thumb_7c, s_layer)

        # White foreground text
        t_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        td = ImageDraw.Draw(t_layer)
        td.text((tx, start_y), title, font=edo_font, fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(15, 20, 25, 160))
        td.text((sx, start_y + th + gap), sub, font=sub_font, fill=(240, 250, 255, 245), stroke_width=1, stroke_fill=(15, 20, 25, 140))
        thumb_7c = Image.alpha_composite(thumb_7c, t_layer).convert("RGB")

        out_7c = os.path.join(brain_dir, "real_nature_rain_thumb_7clouds.jpg")
        thumb_7c.save(out_7c, quality=95)
        thumb_7c.save(os.path.join(thumb_dir, "real_nature_rain_thumb_7clouds.jpg"), quality=95)
        print("Saved real nature 7clouds thumbnail:", out_7c)

        # Style B: LatinHype Tall Bold Sans (164M Formula)
        thumb_lh = base_1.copy()
        bebas_font = ImageFont.truetype(os.path.join(fonts_dir, "BebasNeue-Regular.ttf"), 185)

        title_lh = "HEAVY RAIN ON TIN ROOF"
        sub_lh = "REAL FOREST AMBIENCE • INSOMNIA RELIEF"

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
        td2.text((tlx, start_ylh), title_lh, font=bebas_font, fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(10, 15, 20, 180))
        td2.text((slx, start_ylh + tlh + gap), sub_lh, font=sub_font, fill=(240, 250, 255, 245), stroke_width=1, stroke_fill=(10, 15, 20, 150))
        thumb_lh = Image.alpha_composite(thumb_lh, t_layer2).convert("RGB")

        out_lh = os.path.join(brain_dir, "real_nature_rain_thumb_latinhype.jpg")
        thumb_lh.save(out_lh, quality=95)
        thumb_lh.save(os.path.join(thumb_dir, "real_nature_rain_thumb_latinhype.jpg"), quality=95)
        print("Saved real nature LatinHype thumbnail:", out_lh)

if __name__ == "__main__":
    create_real_nature_thumbnails()
