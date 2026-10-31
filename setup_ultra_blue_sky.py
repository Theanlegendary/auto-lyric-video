import os
import sys
import urllib.request
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
stock_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\stock_anime_bgs"

# 1. Download Ultra
urls = {
    'Ultra-Regular.ttf': 'https://github.com/google/fonts/raw/main/apache/ultra/Ultra-Regular.ttf',
    'Montserrat-BlackItalic.ttf': 'https://github.com/google/fonts/raw/main/ofl/montserrat/static/Montserrat-BlackItalic.ttf',
    'Inter-BlackItalic.ttf': 'https://github.com/google/fonts/raw/main/ofl/inter/static/Inter_28pt-BlackItalic.ttf',
}

for name, url in urls.items():
    dest = os.path.join(fonts_dir, name)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {name}: {os.path.getsize(dest)} bytes")
    except Exception as e:
        print(f"Failed {name}: {e}")

# 2. Convert and resize generated blue sky
gen_sky = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6\17_anime_clear_blue_sky_clouds_1793066730911.jpg"
target_sky = os.path.join(stock_dir, "17_anime_clear_blue_sky_clouds.png")

if os.path.exists(gen_sky):
    im = Image.open(gen_sky).convert("RGB")
    im_1080 = im.resize((1920, 1080), Image.Resampling.LANCZOS)
    im_1080.save(target_sky, "PNG")
    print(f"Saved 1080p anime blue sky: {target_sky}")
