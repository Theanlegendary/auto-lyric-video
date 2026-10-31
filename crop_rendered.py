import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
p = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6\audit_15_Akon_Lonely_chorus1.png"
im = Image.open(p)
# crop center
crop = im.crop((400, 350, 1520, 650))
crop.save(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\test_crop_rendered.png")
print("Saved crop")
