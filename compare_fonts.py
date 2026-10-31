import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

fonts_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

text = "Dandelion"
canvas = Image.new('RGB', (1200, 500), (30, 25, 45))
draw = ImageDraw.Draw(canvas)

font_candidates = [
    ("Poppins-Bold.ttf", 64, 40),
    ("Fredoka.ttf", 64, 140),
    ("Comfortaa.ttf", 64, 240),
    ("PatrickHand.ttf", 74, 340),
    ("Sniglet-ExtraBold.ttf", 64, 420)
]

for fname, size, y in font_candidates:
    p = fonts_dir / fname
    if p.exists():
        f = ImageFont.truetype(str(p), size)
        draw.text((50, y), f"{fname}: Cause I'm in a field of dandelions", font=f, fill=(255, 255, 255))

out_p = brain / "font_comparison_benchmark.png"
canvas.save(out_p)
print(f"Saved font comparison: {out_p}")
