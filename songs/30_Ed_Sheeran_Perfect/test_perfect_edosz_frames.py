import os
import sys
import subprocess
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
song_dir = base / "songs" / "30_Ed_Sheeran_Perfect"
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

ass_path = song_dir / "lyrics_edosz_slowed.ass"
ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

editions = [
    {
        "id": "80sky_sea",
        "name": "80% Blue Sky / 20% Sea (Blue Filter)",
        "bg": song_dir / "perfect_80sky_20sea_bluefilter.png",
    },
    {
        "id": "pink_mode",
        "name": "Pink Mode (Cotton-Candy Clouds)",
        "bg": song_dir / "perfect_pink_master.png",
    },
    {
        "id": "sunset_mode",
        "name": "Sunset Mode (Warm Amber Dusk)",
        "bg": song_dir / "perfect_sunset_master.png",
    }
]

# Timestamps in seconds for Slowed + Reverb:
# Intro: 4.0s
# Verse 1: 12.0s (I found a love for me, Darling just dive right in)
# Chorus: 80.0s (Baby I'm dancing in the dark With you between my arms)
test_points = [
    ("intro", 4.0),
    ("verse", 12.0),
    ("chorus", 80.0)
]

for ed in editions:
    print(f"\n--- Testing Edition: {ed['name']} ---")
    for label, ts in test_points:
        out_frame = brain / f"audit_perfect_edosz_{ed['id']}_{label}.png"
        crop_frame = brain / f"crop_perfect_edosz_{ed['id']}_{label}.png"

        vf = f"setpts=PTS+{ts}/TB,subtitles={ass_escaped}:fontsdir={fonts_escaped}"
        cmd = [
            "ffmpeg", "-y",
            "-i", str(ed["bg"]),
            "-vf", vf,
            "-vframes", "1",
            str(out_frame)
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0 and out_frame.exists():
            im = Image.open(out_frame)
            # Crop lower third where text is centered (Y: 600 to 1020, X: 200 to 1720)
            crop_im = im.crop((200, 600, 1720, 1040))
            crop_im.save(crop_frame)
            print(f"  [OK] {label} frame at {ts}s -> {out_frame.name} & {crop_frame.name}")
        else:
            print(f"  [FAIL] {label} frame at {ts}s: {res.stderr[:200]}")
