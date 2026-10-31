import sys, shutil
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

brain_parent = Path("C:/Users/DELL/.gemini/antigravity/brain")
curr_conv = "fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

old_convs = [
    "b20600e0-f53b-4d2b-bd72-6118c4e17a6e",
    "5c6d4828-b9b1-4898-b6f1-c6d4f714a6cc",
    "da3e96a5-30b3-4304-866a-b7cc83a0d0bd",
    "d98be58e-aff7-4925-80d6-5f5804ac675b",
    "8947e7c8-b090-4e67-8bf2-d19de0182e2f",
    "59341460-0053-45df-80cc-c3ecf49f4824",
    "e34b415c-5f22-4eb1-8568-1f2c12895056",
    "4cab1c02-912e-4531-a470-886a17cf3d95",
    "7e9e46c3-f38a-4188-8c02-5741ca9765e5",
    "4771b828-b6e2-4d44-8b1b-c91f9949925f",
    "acb08923-1b4f-4be0-86ff-5cf6eb8b0d88",
    "3fdb6160-c635-4851-9ed5-cd57b1858c7b",
    "5c721d68-2178-4326-84ec-8389ea341e4a",
    "d6aa5c91-f554-4137-b28e-588354e91080"
]

for cid in old_convs:
    p = brain_parent / cid
    if p.exists():
        shutil.rmtree(p, ignore_errors=True)
        print(f"Removed old conv {cid}")

# Also clean test/ directory
test_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/test")
if test_dir.exists():
    shutil.rmtree(test_dir, ignore_errors=True)
    print("Cleaned test/ folder.")

# Also remove obsolete compare video clips
video_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos")
for f in ["compare_skyfall_1_original.mp4", "compare_skyfall_2_slowed_reverb.mp4", 
          "compare_sweater_1_original.mp4", "compare_sweater_2_slowed_reverb.mp4",
          "demo_color_clouds_clean_horizon.mp4", "00_Justin_Bieber_That_Should_Be_Me_Lyric_Video.mp4"]:
    vp = video_dir / f
    if vp.exists():
        vp.unlink(missing_ok=True)
        print(f"Removed {f}")
