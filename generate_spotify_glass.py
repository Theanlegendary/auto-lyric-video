#!/usr/bin/env python3
"""
Generate Spotify Modern Glass Frosted Backgrounds
Formula from Justin_Bieber_That_Should_Be_Me_Spotify_Glass:
- GaussianBlur(radius=32)
- Brightness(0.82) -> 18% dimming for soft contrast
- Contrast(1.15) -> 15% saturation & contrast boost
"""

import sys
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent
GLASS_DIR = BASE_DIR / "spotify_glass_bgs"
GLASS_DIR.mkdir(parents=True, exist_ok=True)

sources = [
    ("dwas", BASE_DIR / "stock_anime_bgs" / "02_lofi_twilight_starry_night.png"),
    ("ophelia", BASE_DIR / "stock_anime_bgs" / "03_anime_rooftop_sunset_skyline.png"),
    ("apt", BASE_DIR / "light_clouds_sharp_1080.png"),
    ("golden", BASE_DIR / "stock_anime_bgs" / "01_makoto_shinkai_clouds.png"),
    ("birds", BASE_DIR / "stock_anime_bgs" / "01_makoto_shinkai_clouds.png"),
    ("rainy_city", BASE_DIR / "stock_anime_bgs" / "04_lofi_rainy_window_city_night.png"),
    ("justin_bieber", BASE_DIR / "clean_bg_1080.png"),
]

print("Generating Spotify Modern Glass backgrounds (radius=32, brightness=0.82, contrast=1.15)...")
for key, src in sources:
    if not src.exists():
        print(f"Skipping {key}: {src} missing")
        continue
    img = Image.open(src).convert("RGB")
    blur = img.filter(ImageFilter.GaussianBlur(radius=32))
    blur = ImageEnhance.Brightness(blur).enhance(0.82)
    blur = ImageEnhance.Contrast(blur).enhance(1.15)
    out_path = GLASS_DIR / f"bg_spotify_glass_{key}.png"
    blur.save(out_path)
    print(f"[OK] Created {out_path.name} ({out_path.stat().st_size} bytes)")

print("All Spotify Glass backgrounds generated successfully!")
