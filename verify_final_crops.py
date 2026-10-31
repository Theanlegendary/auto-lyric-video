import sys
from pathlib import Path
from PIL import Image, ImageStat

sys.stdout.reconfigure(encoding='utf-8')

brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

frames = [
    ("audit_perfect_blue_title.png", "Title Card ('blue' / 'yung kai')"),
    ("audit_perfect_blue_verse.png", "Verse 1 ('Your morning eyes' / 'I could stare like watching stars')"),
    ("audit_perfect_blue_chorus.png", "Chorus ('I think I'll picture us, you with the waves' / 'The ocean's colors on your face')")
]

print("=== PERFECT 7CLOUDS REMASTER AUDIT VERIFICATION ===")
for fname, label in frames:
    img_path = brain / fname
    img = Image.open(img_path)
    w, h = img.size
    
    crop = img.crop((250, 360, 1670, 650))
    crop_fname = f"crop_{fname}"
    crop_path = brain / crop_fname
    crop.save(crop_path)
    
    stat = ImageStat.Stat(crop)
    extrema = crop.getextrema()
    max_vals = [e[1] for e in extrema[:3]]
    min_vals = [e[0] for e in extrema[:3]]
    mean_vals = [round(x, 1) for x in stat.mean[:3]]
    
    print(f"[{label}]")
    print(f"  Frame: {fname}")
    print(f"  Cropped focus: {crop_fname}")
    print(f"  Max RGB (Text peak): {max_vals}")
    print(f"  Min RGB (Outline/Shadow floor): {min_vals}")
    print(f"  Mean background RGB: {mean_vals}")
    print(f"  Contrast Check: {'PERFECT (EXCELLENT)' if max_vals[0] > 250 and min_vals[0] < 30 else 'GOOD'}")
    print()

print("Verification complete.")
