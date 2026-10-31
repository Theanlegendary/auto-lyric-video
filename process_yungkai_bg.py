import sys, json, shutil
from pathlib import Path
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "28_yung_kai_blue"
stock_dir = base / "stock_anime_bgs"

raw_img_path = brain / "yung_kai_blue_wallpaper_1793325920707.jpg"

if raw_img_path.exists():
    im = Image.open(raw_img_path)
    im_1080 = im.resize((1920, 1080), Image.Resampling.LANCZOS)
    raw_dest = song_dir / "blue_raw.png"
    im_1080.save(raw_dest)
    
    # Create gentle bokeh master (radius 6)
    blur_dest = song_dir / "blue_blurred_master.png"
    im_blur = im_1080.filter(ImageFilter.GaussianBlur(radius=6))
    im_blur.save(blur_dest)
    print("Saved blue_raw.png and blue_blurred_master.png in song dir.")
    
    # Save copy in stock_anime_bgs
    stock_bg = stock_dir / "34_yung_kai_blue_pastel_dawn.png"
    shutil.copy(raw_dest, stock_bg)
    print("Saved copy in stock_anime_bgs.")
    
    # Register in bg_registry.json
    reg_file = base / "bg_registry.json"
    reg_data = json.loads(reg_file.read_text(encoding="utf-8"))
    
    found = any(item.get("id") == "bg_34" for item in reg_data)
    if not found:
        new_entry = {
            "id": "bg_34",
            "file": "34_yung_kai_blue_pastel_dawn.png",
            "name": "yung kai blue Dreamy Pastel Dawn Sky & Coastal Overlook",
            "theme": "white",
            "tags": [
                "yung_kai", "blue", "pastel", "dawn", "morning", "stars",
                "shooting_star", "coastal", "ocean", "solitary", "makoto_shinkai"
            ],
            "assigned_to": "28_yung_kai_blue"
        }
        reg_data.append(new_entry)
        reg_file.write_text(json.dumps(reg_data, indent=2), encoding="utf-8")
        print("Registered bg_34 in bg_registry.json successfully.")
else:
    print("Error: raw_img_path not found:", raw_img_path)
