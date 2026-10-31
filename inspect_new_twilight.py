import sys
from pathlib import Path
from PIL import Image, ImageStat

sys.stdout.reconfigure(encoding='utf-8')

img_path = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6\yung_kai_blue_7clouds_twilight_wallpaper_1793330937570.jpg")
img = Image.open(img_path)
w, h = img.size
stat = ImageStat.Stat(img)
mean_rgb = [round(x, 1) for x in stat.mean[:3]]
brightness = round(0.299 * mean_rgb[0] + 0.587 * mean_rgb[1] + 0.114 * mean_rgb[2], 1)

print(f"File: {img_path.name}")
print(f"Resolution: {w}x{h}")
print(f"Mean RGB: {mean_rgb}")
print(f"Luminance / Brightness: {brightness} (Benchmark 7clouds target: 110 - 150)")
if 90 <= brightness <= 160:
    print("STATUS: PERFECT 7CLOUDS TWILIGHT CONTRAST!")
else:
    print("STATUS: OUT OF RANGE")
