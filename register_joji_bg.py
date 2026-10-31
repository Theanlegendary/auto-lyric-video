import sys, json, shutil
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "27_Joji_Glimpse_of_Us"
stock_dir = base / "stock_anime_bgs"

raw_bg = song_dir / "glimpse_of_us_raw.png"
dest_bg = stock_dir / "33_joji_glimpse_of_us_moody_indigo_sky.png"
shutil.copy(raw_bg, dest_bg)

reg_file = base / "bg_registry.json"
reg_data = json.loads(reg_file.read_text(encoding="utf-8"))

found = False
for item in reg_data:
    if item.get("id") == "bg_33":
        found = True
        break

if not found:
    new_entry = {
        "id": "bg_33",
        "file": "33_joji_glimpse_of_us_moody_indigo_sky.png",
        "name": "Joji Glimpse of Us Moody Indigo Twilight Sky & Solitary Rain Ledge",
        "theme": "white",
        "tags": [
            "joji", "glimpse_of_us", "rain", "piano", "ballad", "moody",
            "twilight", "sapphire", "indigo", "solitary", "makoto_shinkai"
        ],
        "assigned_to": "27_Joji_Glimpse_of_Us"
    }
    reg_data.append(new_entry)
    reg_file.write_text(json.dumps(reg_data, indent=2), encoding="utf-8")
    print("Registered bg_33 in bg_registry.json successfully.")
else:
    print("bg_33 already registered.")
