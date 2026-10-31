import json
import sys
from pathlib import Path
from PIL import Image, ImageFilter

sys.path.insert(0, str(Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")))
import bg_manager

artifacts_dir = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
stock_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/stock_anime_bgs")

new_items = [
    {
        "id": "bg_07",
        "raw_file": artifacts_dir / "sakura_pathway_background_1792810474389.jpg",
        "target_file": "07_cherry_blossom_spring_pathway.png",
        "name": "Romantic Cherry Blossom Pathway",
        "theme": "white",
        "tags": ["sakura", "spring", "romantic", "blossoms", "soft"],
        "assigned_to": None
    },
    {
        "id": "bg_08",
        "raw_file": artifacts_dir / "summer_coastal_cafe_terrace_1792810476654.jpg",
        "target_file": "08_summer_coastal_cafe_terrace.png",
        "name": "Summer Coastal Cafe Terrace",
        "theme": "black",
        "tags": ["cafe", "terrace", "summer", "coastal", "pop", "bright"],
        "assigned_to": None
    },
    {
        "id": "bg_09",
        "raw_file": artifacts_dir / "makoto_shinkai_mountain_dawn_png_1792810482715.jpg",
        "target_file": "09_dramatic_mountain_alpine_dawn.png",
        "name": "Dramatic Mountain Alpine Dawn",
        "theme": "white",
        "tags": ["mountains", "dawn", "sunbeams", "epic", "dramatic"],
        "assigned_to": None
    },
    {
        "id": "bg_10",
        "raw_file": artifacts_dir / "nostalgic_80s_anime_skyline_1792810487366.jpg",
        "target_file": "10_retro_80s_neon_twilight_skyline.png",
        "name": "Retro 80s Neon Twilight Skyline",
        "theme": "white",
        "tags": ["retro", "80s", "neon", "synthwave", "twilight", "car"],
        "assigned_to": None
    }
]

for item in new_items:
    img = Image.open(item["raw_file"]).resize((1920, 1080), Image.Resampling.LANCZOS)
    out_sharp = stock_dir / item["target_file"]
    img.save(out_sharp, "PNG")
    
    # Register in bg_manager
    bg_manager.register_new_background(
        item["id"],
        item["target_file"],
        item["name"],
        item["theme"],
        item["tags"]
    )
    print(f"Processed and registered [{item['id']}] {item['name']} -> {out_sharp.name}")

reg = bg_manager.load_registry()
print(f"\nSuccessfully populated Background Registry with {len(reg)} distinct 1080p anime artworks!")
