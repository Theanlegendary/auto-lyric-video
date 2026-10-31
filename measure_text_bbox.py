import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

im = Image.open(os.path.join(brain, "sample_chewy_hook.png"))
# Find non-background pixels in center to see actual rendered text bounding box
# Background is pink/purple, text is pure white (> 240, 240, 240)
pixels = im.load()
min_x, max_x, min_y, max_y = 1920, 0, 1080, 0
for y in range(200, 900):
    for x in range(100, 1820):
        r, g, b = pixels[x, y][:3]
        if r > 230 and g > 230 and b > 230:
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

w = max_x - min_x
h = max_y - min_y
print(f"Text Bounding Box: ({min_x}, {min_y}) to ({max_x}, {max_y})")
print(f"Total Text Width: {w}px, Height: {h}px")
print(f"Center: ({min_x + w//2}, {min_y + h//2})")
