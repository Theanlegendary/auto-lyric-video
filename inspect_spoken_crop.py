import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

im = Image.open(os.path.join(brain, "audit_15_Akon_Lonely_spotify_rdr_spoken.png"))
crop = im.crop((350, 360, 1570, 680))
crop.save(os.path.join(brain, "crop_check_spoken_5050.png"))
print("Saved crop_check_spoken_5050.png")
