import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

# Create a wide seamless or soft-edged fluffy anime cloud texture (2500x400)
cloud_w, cloud_h = 2400, 450
img = Image.new("RGBA", (cloud_w, cloud_h), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw clusters of soft organic cloud shapes
import random
random.seed(42)

for _ in range(35):
    cx = random.randint(100, cloud_w - 100)
    cy = random.randint(100, cloud_h - 100)
    rx = random.randint(120, 260)
    ry = random.randint(60, 140)
    # Ethereal soft white/lavender cloud color with low opacity
    alpha = random.randint(25, 60)
    draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(230, 240, 255, alpha))

# Apply heavy Gaussian blur to make them ultra fluffy and ethereal like Makoto Shinkai mist
cloud_soft = img.filter(ImageFilter.GaussianBlur(radius=35))
cloud_path = base / "cloud_layer_soft.png"
cloud_soft.save(cloud_path)
print(f"Saved cloud layer: {cloud_path} ({cloud_soft.size})")
