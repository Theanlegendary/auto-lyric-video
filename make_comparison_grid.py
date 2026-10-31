import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
user_ref_path = os.path.join(brain, ".user_uploaded", "media_1793006726653_eac9d068.png")
user_ref = Image.open(user_ref_path)

print(f"User Reference Size: {user_ref.size}")

candidates = ["Sniglet", "Chewy", "BalsamiqSans", "Gaegu", "LilitaOne", "ShortStack"]

# Let's create a combined visual comparison image
# Width 1920, Height = 1080 + 300
# Place user ref on left, and candidate crops on right
comp = Image.new("RGB", (1800, 1200), (20, 20, 25))

# Resize user ref to height 500
ref_resized = user_ref.resize((int(user_ref.width * 500 / user_ref.height), 500), Image.Resampling.LANCZOS)
comp.paste(ref_resized, (50, 50))

# For each candidate, crop center (600, 250, 1320, 750)
coords = [
    (550, 50),
    (1150, 50),
    (550, 600),
    (1150, 600),
    (50, 600),
]

for idx, font_id in enumerate(candidates[:5]):
    cpath = os.path.join(brain, f"cloudnine_match_{font_id}.png")
    if os.path.exists(cpath):
        cim = Image.open(cpath)
        ccrop = cim.crop((650, 300, 1270, 700)).resize((550, 350), Image.Resampling.LANCZOS)
        # paste
        x, y = coords[idx]
        comp.paste(ccrop, (x, y))
        print(f"Pasted {font_id} at {x}, {y}")

comp_path = os.path.join(brain, "comparison_font_reference_grid.png")
comp.save(comp_path, "PNG")
print("Saved comparison_font_reference_grid.png")
