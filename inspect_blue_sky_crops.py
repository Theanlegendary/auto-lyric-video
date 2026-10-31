import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

t_im = Image.open(os.path.join(brain, "test_blue_sky_ultra_title.png"))
p_im = Image.open(os.path.join(brain, "test_blue_sky_poppins_hook.png"))

# crop center
tcrop = t_im.crop((400, 300, 1520, 700))
pcrop = p_im.crop((400, 350, 1520, 650))

tcrop.save(os.path.join(brain, "crop_check_ultra_title.png"))
pcrop.save(os.path.join(brain, "crop_check_poppins_hook.png"))
print("Saved crops for inspection!")
