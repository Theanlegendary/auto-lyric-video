import os
import sys
import subprocess
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
song_dir = base / "songs" / "25_The_Neighbourhood_Sweater_Weather"
master_bg = song_dir / "sweater_weather_blurred_master.png"
ass_path = song_dir / "lyrics_spotify.ass"

ass_escaped = ass_path.as_posix().replace(":", "\\\\:")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

preview_stamps = [
    ("00:00:03", "preview_25_sweater_weather_intro.png"),
    ("00:00:18", "preview_25_sweater_weather_verse1.png"),
    ("00:01:05", "preview_25_sweater_weather_chorus1.png"),
    ("00:02:26", "preview_25_sweater_weather_bridge_title.png"),
    ("00:03:15", "preview_25_sweater_weather_chorus3.png"),
]

for ss, fname in preview_stamps:
    out_p = brain / fname
    vf = f"subtitles={ass_escaped}:fontsdir={fonts_escaped}"
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "250", "-i", str(master_bg),
        "-vf", vf,
        "-ss", ss,
        "-vframes", "1",
        str(out_p)
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered preview: {fname}")

# Crop checks
crop_boxes = [
    ("preview_25_sweater_weather_bridge_title.png", "crop_check_25_sweater_weather_title.png", (250, 280, 1670, 800)),
    ("preview_25_sweater_weather_verse1.png", "crop_check_25_sweater_weather_verse1.png", (200, 380, 1720, 700)),
    ("preview_25_sweater_weather_chorus1.png", "crop_check_25_sweater_weather_chorus.png", (200, 380, 1720, 700)),
]

for src, dst, box in crop_boxes:
    im = Image.open(brain / src)
    cr = im.crop(box)
    cr.save(brain / dst)
    print(f"Saved crop: {dst}")
