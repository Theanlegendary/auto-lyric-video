import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

def create_7clouds_thumbnail(out_path):
    W, H = 1920, 1080
    fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
    
    # 1. 7clouds Signature Sunset/Sunrise Pastel Horizon Gradient
    # Top: Slate blue-gray (#70889B)
    # Mid (45%): Soft dusty rose/peach (#C8A599)
    # 70%: Warm apricot / cream (#E9BA9C)
    # Bottom: Golden dusk haze (#D8906E)
    stops = [
        (0.00, np.array([112, 136, 155], dtype=float)),
        (0.40, np.array([170, 158, 154], dtype=float)),
        (0.68, np.array([230, 186, 156], dtype=float)),
        (1.00, np.array([216, 144, 110], dtype=float))
    ]
    
    arr = np.zeros((H, W, 3), dtype=np.uint8)
    for y in range(H):
        pos = y / float(H - 1)
        for i in range(len(stops) - 1):
            p0, c0 = stops[i]
            p1, c1 = stops[i+1]
            if p0 <= pos <= p1:
                t = (pos - p0) / (p1 - p0)
                t_smooth = (1 - np.cos(t * np.pi)) / 2.0
                c = c0 + (c1 - c0) * t_smooth
                arr[y, :] = c.astype(np.uint8)
                break
                
    base = Image.fromarray(arr).convert("RGBA")
    
    # 2. Typography
    # Edo SZ is the exact brush font used by 7clouds
    edo_font = ImageFont.truetype(os.path.join(fonts_dir, "edosz.ttf"), 220)
    # Artist font: Poppins SemiBold or Barlow
    artist_font = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-SemiBold.ttf"), 68)
    
    title_text = "7 YEARS"
    artist_text = "LUKAS GRAHAM"
    
    draw_dummy = ImageDraw.Draw(base)
    bbox_t = draw_dummy.textbbox((0, 0), title_text, font=edo_font)
    tw = bbox_t[2] - bbox_t[0]
    th = bbox_t[3] - bbox_t[1]
    
    bbox_a = draw_dummy.textbbox((0, 0), artist_text, font=artist_font)
    aw = bbox_a[2] - bbox_a[0]
    ah = bbox_a[3] - bbox_a[1]
    
    # Vertical placement: center block with perfect spacing
    gap = 48
    total_h = th + gap + ah
    start_y = (H - total_h) // 2 - 25
    
    tx = (W - tw) // 2 - bbox_t[0]
    ax = (W - aw) // 2 - bbox_a[0]
    
    # 3. Drop Shadows (Gaussian blurred multi-pass)
    shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_layer)
    
    # Deep shadow for 7 YEARS
    s_draw.text((tx + 10, start_y + 14), title_text, font=edo_font, fill=(20, 20, 25, 230))
    # Soft shadow for LUKAS GRAHAM
    s_draw.text((ax + 6, start_y + th + gap + 8), artist_text, font=artist_font, fill=(20, 20, 25, 200))
    
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(5))
    base = Image.alpha_composite(base, shadow_layer)
    
    # 4. Foreground text with subtle edge enhancement
    text_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    t_draw = ImageDraw.Draw(text_layer)
    
    # Subtle dark stroke for crisp definition
    t_draw.text((tx, start_y), title_text, font=edo_font, fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(30, 30, 35, 140))
    t_draw.text((ax, start_y + th + gap), artist_text, font=artist_font, fill=(255, 255, 255, 245), stroke_width=1, stroke_fill=(30, 30, 35, 120))
    
    final_img = Image.alpha_composite(base, text_layer).convert("RGB")
    final_img.save(out_path, quality=95)
    print("7clouds replica saved:", out_path)

def create_latinhype_thumbnail(out_path):
    W, H = 1920, 1080
    fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
    brain_dir = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
    
    # 1. Background: Vibrant electric cyan sky (top 75%) + Mountain ridges (bottom 25%)
    sky_top = np.array([0, 178, 224], dtype=float)    # Vivid cyan
    sky_mid = np.array([0, 152, 202], dtype=float)    # Deep azure
    
    arr = np.zeros((H, W, 3), dtype=np.uint8)
    for y in range(H):
        t = y / float(H - 1)
        c = sky_top + (sky_mid - sky_top) * t
        arr[y, :] = c.astype(np.uint8)
        
    base = Image.fromarray(arr).convert("RGBA")
    
    # Load mountain photo, crop the mountain ridge and place at bottom
    mountain_path = os.path.join(brain_dir, "latinhype_ref_mountain.jpg")
    if os.path.exists(mountain_path):
        m_img = Image.open(mountain_path).convert("RGBA")
        # Increase saturation and contrast of mountains
        enh_color = ImageEnhance.Color(m_img)
        m_img = enh_color.enhance(1.35)
        enh_con = ImageEnhance.Contrast(m_img)
        m_img = enh_con.enhance(1.20)
        
        # Take the mountain horizon band
        mw, mh = m_img.size
        # Crop region containing the snow peaks and green hills
        crop_box = (0, int(mh * 0.28), mw, int(mh * 0.85))
        m_crop = m_img.crop(crop_box)
        target_h = int(H * 0.26)
        m_crop = m_crop.resize((W, target_h), Image.Resampling.LANCZOS)
        
        # Feather the top edge so it blends into the cyan sky seamlessly
        alpha_mask = Image.new("L", (W, target_h), 255)
        mask_draw = ImageDraw.Draw(alpha_mask)
        for y in range(35):
            val = int(255 * (y / 35.0))
            mask_draw.line([(0, y), (W, y)], fill=val)
            
        m_crop.putalpha(alpha_mask)
        base.paste(m_crop, (0, H - target_h), m_crop)
        
    # 2. Typography
    bebas_font = ImageFont.truetype(os.path.join(fonts_dir, "BebasNeue-Regular.ttf"), 200)
    artist_font = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 68)
    
    title_text = "WHEN I WAS YOUR MAN"
    artist_text = "BRUNO MARS"
    
    draw_dummy = ImageDraw.Draw(base)
    bbox_t = draw_dummy.textbbox((0, 0), title_text, font=bebas_font)
    tw = bbox_t[2] - bbox_t[0]
    th = bbox_t[3] - bbox_t[1]
    
    bbox_a = draw_dummy.textbbox((0, 0), artist_text, font=artist_font)
    aw = bbox_a[2] - bbox_a[0]
    ah = bbox_a[3] - bbox_a[1]
    
    # LatinHype places title in upper-mid clear sky area (around 32% down)
    start_y = int(H * 0.33)
    gap = 24
    
    tx = (W - tw) // 2 - bbox_t[0]
    ax = (W - aw) // 2 - bbox_a[0]
    
    # 3. Solid Sharp Drop Shadow (LatinHype signature)
    shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_layer)
    
    # Sharp offset shadow
    dx, dy = 8, 10
    s_draw.text((tx + dx, start_y + dy), title_text, font=bebas_font, fill=(5, 25, 40, 240))
    s_draw.text((ax + 5, start_y + th + gap + 7), artist_text, font=artist_font, fill=(5, 25, 40, 220))
    
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(1.5))
    base = Image.alpha_composite(base, shadow_layer)
    
    # 4. Foreground text
    text_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    t_draw = ImageDraw.Draw(text_layer)
    
    # Slight stroke for extra boldness
    t_draw.text((tx, start_y), title_text, font=bebas_font, fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(15, 30, 45, 180))
    t_draw.text((ax, start_y + th + gap), artist_text, font=artist_font, fill=(255, 255, 255, 245), stroke_width=1, stroke_fill=(15, 30, 45, 140))
    
    final_img = Image.alpha_composite(base, text_layer).convert("RGB")
    final_img.save(out_path, quality=95)
    print("LatinHype replica saved:", out_path)

if __name__ == "__main__":
    brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
    create_7clouds_thumbnail(os.path.join(brain, "master_7clouds_7years_replica.png"))
    create_latinhype_thumbnail(os.path.join(brain, "master_latinhype_when_i_was_your_man_replica.png"))
