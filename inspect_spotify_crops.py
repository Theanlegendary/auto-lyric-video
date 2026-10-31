import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

h_im = Image.open(os.path.join(brain, "preview_spotify_orange_hook.png"))
v_im = Image.open(os.path.join(brain, "preview_spotify_orange_verse.png"))

# crop center
hcrop = h_im.crop((400, 360, 1520, 680))
vcrop = v_im.crop((400, 360, 1520, 680))

hcrop.save(os.path.join(brain, "crop_check_spotify_hook.png"))
vcrop.save(os.path.join(brain, "crop_check_spotify_verse.png"))
print("Saved crops for inspection!")
