import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

im = Image.open(os.path.join(brain, "sample_chewy_hook.png"))
# crop center
crop = im.crop((300, 300, 1620, 780))
crop.save(os.path.join(brain, "crop_chewy_hook_check.png"))
print("Saved crop_chewy_hook_check.png")
