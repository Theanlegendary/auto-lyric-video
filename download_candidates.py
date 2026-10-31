import urllib.request
from PIL import Image
import os

candidates = [
    {
        "name": "bg_mountain_dusk.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Mountainous_landscape_at_dusk_%28Unsplash%29.jpg"
    },
    {
        "name": "bg_pink_sunset_island.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Silhouette_of_an_island_at_sunset_with_blue_sky_pink_and_yellow_clouds_in_Don_Det_Si_Phan_Don_Laos.jpg"
    },
    {
        "name": "bg_dusk_sky.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Dusk_Sunset_Sky.jpg"
    },
    {
        "name": "bg_fuji_sunset.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Silhouette_of_Mount_Fuji_%28149103993%29.jpg"
    }
]

out_dir = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/new_bgs"
os.makedirs(out_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for c in candidates:
    target_raw = os.path.join(out_dir, "raw_" + c["name"])
    target_1080 = os.path.join(out_dir, c["name"])
    print(f"Downloading {c['name']}...")
    req = urllib.request.Request(c['url'], headers=headers)
    try:
        with urllib.request.urlopen(req) as resp, open(target_raw, 'wb') as f:
            f.write(resp.read())
        
        # Crop & resize to exact 1920x1080 keeping aspect ratio
        img = Image.open(target_raw)
        # target ratio 16:9
        target_w, target_h = 1920, 1080
        src_w, src_h = img.size
        
        # calculate crop box
        aspect_src = src_w / src_h
        aspect_target = target_w / target_h
        
        if aspect_src > aspect_target:
            # wider than 16:9, crop sides
            new_w = int(src_h * aspect_target)
            offset = (src_w - new_w) // 2
            box = (offset, 0, offset + new_w, src_h)
        else:
            # taller than 16:9, crop top/bottom
            new_h = int(src_w / aspect_target)
            offset = (src_h - new_h) // 2
            box = (0, offset, src_w, offset + new_h)
            
        cropped = img.crop(box).resize((target_w, target_h), Image.Resampling.LANCZOS)
        cropped.save(target_1080, "JPEG", quality=95)
        print(f"Successfully processed {c['name']} (1920x1080)!")
    except Exception as e:
        print(f"Error {c['name']}: {e}")
