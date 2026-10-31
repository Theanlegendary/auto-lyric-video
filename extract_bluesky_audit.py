import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
video_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos\15_Akon_Lonely_Lyric_Video.mp4"

stamps = [
    ("00:00:05", "audit_15_Akon_Lonely_bluesky_title.png"),
    ("00:00:15", "audit_15_Akon_Lonely_bluesky_intro_hook.png"),
    ("00:00:28", "audit_15_Akon_Lonely_bluesky_spoken.png"),
    ("00:00:46", "audit_15_Akon_Lonely_bluesky_verse1.png"),
    ("00:01:09", "audit_15_Akon_Lonely_bluesky_chorus.png"),
    ("00:03:41", "audit_15_Akon_Lonely_bluesky_outro.png"),
]

for ss, fname in stamps:
    out_f = os.path.join(brain, fname)
    cmd = ["ffmpeg", "-y", "-ss", ss, "-i", video_path, "-vframes", "1", out_f]
    subprocess.run(cmd, check=True)
    print(f"Extracted: {fname} ({os.path.getsize(out_f)} bytes)")

print("All blue sky audit frames extracted successfully!")
