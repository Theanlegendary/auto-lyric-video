import json
import os
from pathlib import Path
from PIL import Image, ImageFilter

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
registry_file = base / "bg_registry.json"
stock_dir = base / "stock_anime_bgs"

DEFAULT_BACKGROUNDS = [
    {
        "id": "bg_01",
        "file": "01_makoto_shinkai_clouds.png",
        "name": "Pastel Cotton-Candy Clouds",
        "theme": "black",
        "tags": ["pastel", "clouds", "daytime", "pop", "bright"],
        "assigned_to": "01_ROSE_Bruno_Mars_APT"
    },
    {
        "id": "bg_02",
        "file": "02_lofi_twilight_starry_night.png",
        "name": "Deep Indigo Starry Twilight Night",
        "theme": "white",
        "tags": ["night", "stars", "twilight", "lofi", "ballad", "dark"],
        "assigned_to": "02_Lady_Gaga_Bruno_Mars_Die_With_A_Smile"
    },
    {
        "id": "bg_03",
        "file": "03_anime_rooftop_sunset_skyline.png",
        "name": "Anime Sunset Rooftop Skyline & Powerlines",
        "theme": "white",
        "tags": ["sunset", "rooftop", "golden_hour", "city", "skyline"],
        "assigned_to": "03_Taylor_Swift_The_Fate_of_Ophelia"
    },
    {
        "id": "bg_04",
        "file": "04_lofi_rainy_window_city_night.png",
        "name": "Cozy Rainy Window City Bokeh",
        "theme": "white",
        "tags": ["rain", "window", "night", "city", "lofi", "cozy"],
        "assigned_to": None
    },
    {
        "id": "bg_05",
        "file": "05_golden_hour_celestial_overlook.png",
        "name": "Radiant Golden Hour Celestial Overlook",
        "theme": "black",
        "tags": ["golden_hour", "sunbeams", "epic", "mountains", "amber"],
        "assigned_to": "04_HUNTR_X_Golden"
    },
    {
        "id": "bg_06",
        "file": "06_coastal_ocean_soaring_birds.png",
        "name": "Serene Pastel Ocean Beach & Soaring Birds",
        "theme": "black",
        "tags": ["ocean", "beach", "birds", "pastel", "indie", "peaceful"],
        "assigned_to": "05_Billie_Eilish_BIRDS_OF_A_FEATHER"
    }
]

def load_registry():
    if not registry_file.exists():
        save_registry(DEFAULT_BACKGROUNDS)
        return DEFAULT_BACKGROUNDS
    with open(registry_file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_registry(data):
    with open(registry_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def register_new_background(bg_id, filename, name, theme, tags):
    registry = load_registry()
    for item in registry:
        if item["id"] == bg_id or item["file"] == filename:
            item["name"] = name
            item["theme"] = theme
            item["tags"] = tags
            save_registry(registry)
            return item
    new_item = {
        "id": bg_id,
        "file": filename,
        "name": name,
        "theme": theme,
        "tags": tags,
        "assigned_to": None
    }
    registry.append(new_item)
    save_registry(registry)
    return new_item

def get_fresh_background(preferred_theme=None, preferred_tag=None):
    registry = load_registry()
    available = [b for b in registry if b["assigned_to"] is None]
    
    if not available:
        raise RuntimeError("No unassigned backgrounds available! Please generate a new background.")
        
    if preferred_tag:
        for b in available:
            if preferred_tag in b["tags"]:
                return b
                
    if preferred_theme:
        for b in available:
            if b["theme"] == preferred_theme:
                return b
                
    return available[0]

def assign_background_to_song(bg_id, song_identifier):
    registry = load_registry()
    for b in registry:
        if b["id"] == bg_id:
            b["assigned_to"] = song_identifier
            save_registry(registry)
            return b
    raise ValueError(f"Background ID {bg_id} not found in registry.")

if __name__ == "__main__":
    reg = load_registry()
    print(f"Loaded Background Registry: {len(reg)} backgrounds.")
    for b in reg:
        status = f"Assigned to: {b['assigned_to']}" if b['assigned_to'] else "AVAILABLE"
        print(f"  • [{b['id']}] {b['name']} ({b['theme'].upper()}) -> {status}")
