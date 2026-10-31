import json
import os

reg_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\bg_registry.json"

with open(reg_path, "r", encoding="utf-8") as f:
    registry = json.load(f)

# Update bg_16 to unassigned/backup, add bg_17
for item in registry:
    if item["id"] == "bg_16":
        item["assigned_to"] = "15_Akon_Lonely_Vibe_Pink_Alt"

new_entry = {
    "id": "bg_17",
    "file": "17_anime_clear_blue_sky_clouds.png",
    "name": "Makoto Shinkai Clear Blue Anime Sky & Towering Clouds",
    "theme": "white",
    "tags": ["blue", "sky", "clouds", "daytime", "anime", "makoto_shinkai", "clean", "bright"],
    "assigned_to": "15_Akon_Lonely"
}

# Check if bg_17 already exists
exists = False
for item in registry:
    if item["id"] == "bg_17":
        item.update(new_entry)
        exists = True
        break

if not exists:
    registry.append(new_entry)

with open(reg_path, "w", encoding="utf-8") as f:
    json.dump(registry, f, indent=2)

print("Updated bg_registry.json with bg_17!")
