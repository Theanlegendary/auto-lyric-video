import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

w_im = Image.open(os.path.join(brain, "compare_white_poppins.png"))
b_im = Image.open(os.path.join(brain, "compare_black_poppins.png"))

# crop center
w_crop = w_im.crop((350, 360, 1570, 680))
b_crop = b_im.crop((350, 360, 1570, 680))

# combine
comp = Image.new("RGB", (1220, 660))
comp.paste(w_crop, (0, 0))
comp.paste(b_crop, (0, 340))
comp.save(os.path.join(brain, "side_by_side_color_compare.png"))
print("Saved side_by_side_color_compare.png")
