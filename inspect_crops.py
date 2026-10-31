import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

# Let's inspect each crop in detail
for f in ["Sniglet", "Chewy", "BalsamiqSans", "Gaegu"]:
    cpath = os.path.join(brain, f"cloudnine_match_{f}.png")
    im = Image.open(cpath)
    # crop just CLOUD
    crop = im.crop((700, 320, 1220, 480))
    crop.save(os.path.join(brain, f"crop_cloud_{f}.png"))
    print(f"Saved crop_cloud_{f}.png")
