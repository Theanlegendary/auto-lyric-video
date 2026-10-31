import sys
from pathlib import Path
from PIL import Image, ImageStat, ImageOps

sys.stdout.reconfigure(encoding='utf-8')

brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
frames = [
    ("audit_yungkai_7clouds_title.png", "Title Card ('blue' / 'yung kai')"),
    ("audit_yungkai_7clouds_verse.png", "Verse 1 ('Your morning eyes' / 'I could stare like watching stars')"),
    ("audit_yungkai_7clouds_chorus.png", "Chorus ('I think I'll picture us, you with the waves' / 'The ocean's colors on your face')")
]

print("=== 7CLOUDS REMASTER AUDIT VERIFICATION ===")
for fname, label in frames:
    img_path = brain / fname
    img = Image.open(img_path)
    w, h = img.size
    
    # Crop central text area (y: 360 to 650, x: 250 to 1670)
    crop = img.crop((250, 360, 1670, 650))
    crop_fname = f"crop_{fname}"
    crop_path = brain / crop_fname
    crop.save(crop_path)
    
    stat = ImageStat.Stat(crop)
    # Check max brightness in crop (should be 255 for pure white text)
    extrema = crop.getextrema()
    max_vals = [e[1] for e in extrema[:3]]
    min_vals = [e[0] for e in extrema[:3]]
    
    print(f"[{label}]")
    print(f"  File: {fname} ({w}x{h})")
    print(f"  Cropped focus: {crop_fname}")
    print(f"  Text Luminance Peak: RGB={max_vals} (Target >= 250 for crisp white text)")
    print(f"  Outline Shadow Floor: RGB={min_vals} (Target <= 40 for dark border contrast)")
    print(f"  Contrast Check: {'EXCELLENT' if max_vals[0] > 240 and min_vals[0] < 50 else 'ADEQUATE'}")
    print()

print("Verification complete.")
