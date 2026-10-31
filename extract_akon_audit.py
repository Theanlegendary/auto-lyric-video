import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
video_path = os.path.join(base, "videos", "15_Akon_Lonely_Lyric_Video.mp4")
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

audit_frames = [
    ("title", "00:00:05.000"),
    ("intro_hook", "00:00:15.000"),
    ("verse1", "00:00:46.000"),
    ("chorus1", "00:01:06.000"),
    ("outro", "00:03:40.000"),
]

for label, ts in audit_frames:
    out_f = os.path.join(brain, f"audit_15_Akon_Lonely_{label}.png")
    cmd = [
        "ffmpeg", "-y",
        "-ss", ts,
        "-i", video_path,
        "-vframes", "1",
        out_f
    ]
    subprocess.run(cmd, check=True)
    print(f"Extracted audit frame: {label} at {ts}")
