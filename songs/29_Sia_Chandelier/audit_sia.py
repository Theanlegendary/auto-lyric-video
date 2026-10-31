import os
import sys
import subprocess
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

normal_vid = base / "videos" / "29_Sia_Chandelier_Lyric_Video.mp4"
slowed_vid = base / "videos" / "29_Sia_Chandelier_Slowed_Reverb_Lyric_Video.mp4"

def extract_and_crop(vid_path, prefix, stamps):
    if not vid_path.exists():
        print(f"Video {vid_path} does not exist yet.")
        return
    for name, t in stamps.items():
        out_frame = brain / f"audit_sia_{prefix}_{name}.png"
        cmd = [
            "ffmpeg", "-y", "-ss", str(t), "-i", str(vid_path),
            "-vframes", "1", str(out_frame)
        ]
        subprocess.run(cmd, capture_output=True)
        print(f"Extracted {out_frame.name} at {t}s")
        
        # Crop center typography area
        if out_frame.exists():
            img = Image.open(out_frame)
            # Center crop (x: 460 to 1460, y: 350 to 750)
            crop_box = (460, 320, 1460, 760)
            cropped = img.crop(crop_box)
            crop_path = brain / f"crop_audit_sia_{prefix}_{name}.png"
            cropped.save(crop_path)
            print(f"Saved crop: {crop_path.name}")

if __name__ == "__main__":
    if normal_vid.exists():
        print("Extracting Normal video audit frames...")
        extract_and_crop(normal_vid, "normal", {"title": 2.5, "verse": 15.0, "chorus": 38.0})
    if slowed_vid.exists():
        print("Extracting Slowed video audit frames...")
        extract_and_crop(slowed_vid, "slowed", {"title": 2.9, "verse": 17.3, "chorus": 44.0})
