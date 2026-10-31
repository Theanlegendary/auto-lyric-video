import os
import sys
import subprocess
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
song_dir = base / "songs" / "23_OneRepublic_Counting_Stars"
master_bg = song_dir / "counting_stars_blurred_master.png"
ass_path = song_dir / "lyrics_spotify.ass"

ass_escaped = ass_path.as_posix().replace(":", "\\\\:")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

preview_stamps = [
    ("00:00:05", "preview_23_counting_stars_intro.png"),
    ("00:00:28", "preview_23_counting_stars_title.png"),
    ("00:00:42", "preview_23_counting_stars_verse1.png"),
    ("00:01:22", "preview_23_counting_stars_chorus.png"),
    ("00:03:06", "preview_23_counting_stars_bridge.png"),
]

for ss, fname in preview_stamps:
    out_p = brain / fname
    vf = f"subtitles={ass_escaped}:fontsdir={fonts_escaped}"
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "260", "-i", str(master_bg),
        "-vf", vf,
        "-ss", ss,
        "-vframes", "1",
        str(out_p)
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered preview: {fname}")

# Crop checks
crop_boxes = [
    ("preview_23_counting_stars_title.png", "crop_check_23_counting_stars_title.png", (300, 300, 1620, 780)),
    ("preview_23_counting_stars_chorus.png", "crop_check_23_counting_stars_chorus.png", (200, 380, 1720, 700)),
    ("preview_23_counting_stars_bridge.png", "crop_check_23_counting_stars_bridge.png", (200, 380, 1720, 700)),
]

for src, dst, box in crop_boxes:
    im = Image.open(brain / src)
    cr = im.crop(box)
    cr.save(brain / dst)
    print(f"Saved crop: {dst}")
