import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

def make_gradient_7clouds(width, height):
    """
    Creates the exact 7clouds pastel horizon dawn/sunset gradient:
    Cool slate blue at top -> warm soft cream/peach -> golden dawn glow at bottom
    """
    img = Image.new("RGBA", (width, height))
    # Colors:
    # 0%: Cool slate blue (105, 126, 142)
    # 45%: Soft pastel grayish peach (175, 170, 168)
    # 70%: Warm apricot / peach cream (235, 195, 165)
    # 100%: Earthy warm golden horizon (210, 145, 105)
    
    stops = [
        (0.0, np.array([105, 126, 142], dtype=float)),
        (0.40, np.array([168, 165, 162], dtype=float)),
        (0.70, np.array([232, 192, 160], dtype=float)),
        (1.0, np.array([210, 145, 105], dtype=float))
    ]
    
    arr = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        pos = y / float(height - 1)
        # find segment
        for i in range(len(stops) - 1):
            p0, c0 = stops[i]
            p1, c1 = stops[i+1]
            if p0 <= pos <= p1:
                t = (pos - p0) / (p1 - p0)
                # smooth cosine interpolation
                t_smooth = (1 - np.cos(t * np.pi)) / 2.0
                c = c0 + (c1 - c0) * t_smooth
                arr[y, :] = c.astype(np.uint8)
                break
                
    return Image.fromarray(arr, "RGB").convert("RGBA")

def make_latinhype_background(width, height):
    """
    Creates the LatinHype saturated cyan sky with mountain ridges at bottom:
    80% Electric Cyan Sky -> 20% Mountain range with snowy peaks & green slopes
    """
    img = Image.new("RGBA", (width, height))
    
    # Cyan sky gradient (top to 78%)
    sky_top = np.array([0, 175, 215], dtype=float)    # Bright vibrant cyan
    sky_bottom = np.array([0, 140, 185], dtype=float) # Slightly deeper cyan
    
    arr = np.zeros((height, width, 3), dtype=np.uint8)
    mountain_y = int(height * 0.76)
    
    for y in range(mountain_y):
        t = y / float(mountain_y)
        c = sky_top + (sky_bottom - sky_top) * t
        arr[y, :] = c.astype(np.uint8)
        
    sky_img = Image.fromarray(arr, "RGB").convert("RGBA")
    draw = ImageDraw.Draw(sky_img)
    
    # Draw stylized mountain silhouette and ridge
    # Layer 1: Dark green rolling ridges
    ridge_points = [
        (0, height),
        (0, int(height * 0.82)),
        (int(width * 0.15), int(height * 0.77)),
        (int(width * 0.35), int(height * 0.81)),
        (int(width * 0.50), int(height * 0.75)),
        (int(width * 0.70), int(height * 0.79)),
        (int(width * 0.88), int(height * 0.74)),
        (width, int(height * 0.78)),
        (width, height)
    ]
    draw.polygon(ridge_points, fill=(20, 95, 75, 255))
    
    # Layer 2: Rocky crags with snow dusting at the base
    rock_points = [
        (0, height),
        (0, int(height * 0.90)),
        (int(width * 0.10), int(height * 0.87)),
        (int(width * 0.25), int(height * 0.92)),
        (int(width * 0.42), int(height * 0.86)),
        (int(width * 0.65), int(height * 0.91)),
        (int(width * 0.82), int(height * 0.85)),
        (width, int(height * 0.89)),
        (width, height)
    ]
    draw.polygon(rock_points, fill=(45, 55, 65, 255))
    
    # Snow patches
    snow_points = [
        (int(width * 0.05), int(height * 0.91)),
        (int(width * 0.09), int(height * 0.88)),
        (int(width * 0.13), int(height * 0.91)),
    ]
    draw.polygon(snow_points, fill=(225, 235, 245, 220))
    
    snow_points2 = [
        (int(width * 0.38), int(height * 0.89)),
        (int(width * 0.42), int(height * 0.86)),
        (int(width * 0.47), int(height * 0.90)),
    ]
    draw.polygon(snow_points2, fill=(225, 235, 245, 220))
    
    snow_points3 = [
        (int(width * 0.78), int(height * 0.88)),
        (int(width * 0.82), int(height * 0.85)),
        (int(width * 0.87), int(height * 0.89)),
    ]
    draw.polygon(snow_points3, fill=(225, 235, 245, 220))

    return sky_img

def draw_text_with_shadow(img, text, font, pos, fill=(255, 255, 255, 255), shadow_color=(20, 20, 20, 220), offset=(8, 12), blur_radius=3):
    """
    Draws text with high-end blurred drop shadow + subtle stroke for maximum CTR
    """
    w, h = img.size
    # Shadow layer
    shadow_mask = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw_s = ImageDraw.Draw(shadow_mask)
    
    x, y = pos
    dx, dy = offset
    draw_s.text((x + dx, y + dy), text, font=font, fill=shadow_color)
    if blur_radius > 0:
        shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(blur_radius))
        
    img.alpha_composite(shadow_mask)
    
    # Text layer
    text_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw_t = ImageDraw.Draw(text_layer)
    # Subtle dark edge stroke
    draw_t.text((x, y), text, font=font, fill=fill, stroke_width=2, stroke_fill=(30, 30, 30, 160))
    img.alpha_composite(text_layer)

def main():
    fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
    brain_dir = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
    thumb_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail"
    os.makedirs(thumb_dir, exist_ok=True)
    
    W, H = 1920, 1080
    
    # ==========================================
    # 1. 7CLOUDS STYLE: LUKAS GRAHAM - 7 YEARS
    # ==========================================
    bg_7clouds = make_gradient_7clouds(W, H)
    
    # Font choice: PermanentMarker or edosz
    marker_font_path = os.path.join(fonts_dir, "PermanentMarker-Regular.ttf")
    if not os.path.exists(marker_font_path):
        marker_font_path = os.path.join(fonts_dir, "edosz.ttf")
    
    sans_font_path = os.path.join(fonts_dir, "Poppins-Bold.ttf")
    
    title_font_7c = ImageFont.truetype(marker_font_path, 210)
    artist_font_7c = ImageFont.truetype(sans_font_path, 72)
    
    draw_temp = ImageDraw.Draw(bg_7clouds)
    
    title_7c = "7 YEARS"
    artist_7c = "LUKAS GRAHAM"
    
    # Measure
    bbox_title = draw_temp.textbbox((0, 0), title_7c, font=title_font_7c)
    t_w = bbox_title[2] - bbox_title[0]
    t_h = bbox_title[3] - bbox_title[1]
    
    bbox_artist = draw_temp.textbbox((0, 0), artist_7c, font=artist_font_7c)
    a_w = bbox_artist[2] - bbox_artist[0]
    a_h = bbox_artist[3] - bbox_artist[1]
    
    total_block_h = t_h + 35 + a_h
    start_y = (H - total_block_h) // 2 - 20
    
    t_x = (W - t_w) // 2
    a_x = (W - a_w) // 2
    
    # Draw Title
    draw_text_with_shadow(bg_7clouds, title_7c, title_font_7c, (t_x, start_y), 
                          fill=(255, 255, 255, 255), shadow_color=(25, 25, 30, 220), offset=(10, 14), blur_radius=4)
    # Draw Artist
    draw_text_with_shadow(bg_7clouds, artist_7c, artist_font_7c, (a_x, start_y + t_h + 35), 
                          fill=(255, 255, 255, 240), shadow_color=(25, 25, 30, 200), offset=(6, 8), blur_radius=3)
    
    out_7c_brain = os.path.join(brain_dir, "replica_7clouds_7years_191m.png")
    out_7c_thumb = os.path.join(thumb_dir, "replica_7clouds_7years_191m.png")
    bg_7clouds.save(out_7c_brain)
    bg_7clouds.save(out_7c_thumb)
    print("Saved 7clouds replica:", out_7c_brain)
    
    # ==========================================
    # 2. LATINHYPE STYLE: BRUNO MARS - WHEN I WAS YOUR MAN
    # ==========================================
    bg_latin = make_latinhype_background(W, H)
    
    bebas_path = os.path.join(fonts_dir, "BebasNeue-Regular.ttf")
    title_font_latin = ImageFont.truetype(bebas_path, 210)
    artist_font_latin = ImageFont.truetype(sans_font_path, 72)
    
    title_latin = "WHEN I WAS YOUR MAN"
    artist_latin = "BRUNO MARS"
    
    bbox_tl = draw_temp.textbbox((0, 0), title_latin, font=title_font_latin)
    tl_w = bbox_tl[2] - bbox_tl[0]
    tl_h = bbox_tl[3] - bbox_tl[1]
    
    bbox_al = draw_temp.textbbox((0, 0), artist_latin, font=artist_font_latin)
    al_w = bbox_al[2] - bbox_al[0]
    al_h = bbox_al[3] - bbox_al[1]
    
    total_block_latin_h = tl_h + 30 + al_h
    start_latin_y = int(H * 0.32) # In upper 45% where cyan sky is maximum
    
    tl_x = (W - tl_w) // 2
    al_x = (W - al_w) // 2
    
    # Draw Title with sharp solid shadow (LatinHype signature)
    draw_text_with_shadow(bg_latin, title_latin, title_font_latin, (tl_x, start_latin_y),
                          fill=(255, 255, 255, 255), shadow_color=(10, 25, 35, 240), offset=(8, 10), blur_radius=1)
    
    # Draw Artist
    draw_text_with_shadow(bg_latin, artist_latin, artist_font_latin, (al_x, start_latin_y + tl_h + 30),
                          fill=(255, 255, 255, 240), shadow_color=(10, 25, 35, 220), offset=(5, 7), blur_radius=1)
                          
    out_latin_brain = os.path.join(brain_dir, "replica_latinhype_when_i_was_your_man_164m.png")
    out_latin_thumb = os.path.join(thumb_dir, "replica_latinhype_when_i_was_your_man_164m.png")
    bg_latin.save(out_latin_brain)
    bg_latin.save(out_latin_thumb)
    print("Saved LatinHype replica:", out_latin_brain)

if __name__ == "__main__":
    main()
