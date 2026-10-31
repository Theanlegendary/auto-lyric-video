import os
import sys
import subprocess
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
song_dir = base / "songs" / "21_Coldplay_Clocks"
master_bg = song_dir / "clocks_cosmic_blurred_master.png"
ass_path = song_dir / "lyrics_spotify.ass"

ass_escaped = ass_path.as_posix().replace(":", "\\\\:")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

preview_stamps = [
    ("00:00:10", "preview_21_clocks_title.png"),
    ("00:00:32", "preview_21_clocks_verse1.png"),
    ("00:01:04", "preview_21_clocks_chorus.png"),
    ("00:03:00", "preview_21_clocks_bridge.png"),
    ("00:04:12", "preview_21_clocks_outro.png"),
]

for ss, fname in preview_stamps:
    out_p = brain / fname
    vf = f"subtitles={ass_escaped}:fontsdir={fonts_escaped}"
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "310", "-i", str(master_bg),
        "-vf", vf,
        "-ss", ss,
        "-vframes", "1",
        str(out_p)
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered preview: {fname}")

# Crop checks
crop_boxes = [
    ("preview_21_clocks_title.png", "crop_check_21_clocks_title.png", (400, 350, 1520, 730)),
    ("preview_21_clocks_verse1.png", "crop_check_21_clocks_verse1.png", (200, 380, 1720, 700)),
    ("preview_21_clocks_bridge.png", "crop_check_21_clocks_bridge.png", (200, 380, 1720, 700)),
]

for src, dst, box in crop_boxes:
    im = Image.open(brain / src)
    cr = im.crop(box)
    cr.save(brain / dst)
    print(f"Saved crop: {dst}")
