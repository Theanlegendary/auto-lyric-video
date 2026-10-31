import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
img_path = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6\.user_uploaded\media_1793006726653_eac9d068.png"

im = Image.open(img_path)
print(f"Image Size: {im.size}, Mode: {im.mode}")
