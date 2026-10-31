import sys
from pathlib import Path
from PIL import Image, ImageStat, ImageOps

sys.stdout.reconfigure(encoding='utf-8')

study_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\channel_study")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

benchmarks = ["7clouds_dandelions_frame.png", "7clouds_die_with_a_smile_frame.png"]

print("=== 7CLOUDS CHANNEL STUDY BENCHMARKS ===")
for b in benchmarks:
    p = study_dir / b
    img = Image.open(p)
    w, h = img.size
    # Crop central text area
    crop = img.crop((w*0.1, h*0.35, w*0.9, h*0.65))
    stat = ImageStat.Stat(crop)
    print(f"File: {b} ({w}x{h})")
    print(f"  Mean RGB: {[round(x, 1) for x in stat.mean[:3]]}")
    print(f"  Extrema: {crop.getextrema()[:3]}")

print("\n=== OUR CURRENT YUNG KAI 7CLOUDS AUDIT FRAMES ===")
ours = ["audit_yungkai_7clouds_title.png", "audit_yungkai_7clouds_verse.png", "audit_yungkai_7clouds_chorus.png"]
for o in ours:
    p = brain / o
    img = Image.open(p)
    w, h = img.size
    crop = img.crop((w*0.1, h*0.35, w*0.9, h*0.65))
    stat = ImageStat.Stat(crop)
    print(f"File: {o} ({w}x{h})")
    print(f"  Mean RGB: {[round(x, 1) for x in stat.mean[:3]]}")
    print(f"  Extrema: {crop.getextrema()[:3]}")
