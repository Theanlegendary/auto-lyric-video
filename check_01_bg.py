import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

p = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\stock_anime_bgs\01_makoto_shinkai_clouds.png"
im = Image.open(p)
print("01_makoto_shinkai_clouds size:", im.size)

# Also let's check subagent image-generator capability:
print("Can generate fresh blue sky if needed")
