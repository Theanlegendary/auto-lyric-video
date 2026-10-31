import sys
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

study_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\channel_study")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

for b in ["7clouds_dandelions_frame.png", "7clouds_die_with_a_smile_frame.png"]:
    img = Image.open(study_dir / b)
    # Save a copy to brain for user viewing if needed
    dest = brain / f"benchmark_{b}"
    img.save(dest)
    print(f"Saved benchmark copy: {dest}")

# Also check font characteristics on 7clouds
# Let's inspect cakes_eclairs as well
for c in ["cakes_eclairs_play_date_frame.png", "vibe_music_apt_frame.png"]:
    img = Image.open(study_dir / c)
    dest = brain / f"benchmark_{c}"
    img.save(dest)
    print(f"Saved benchmark copy: {dest}")
