import subprocess
import os

new_clips = [
    ("3864101", "https://videos.pexels.com/video-files/3864101/3864101-hd_1920_1080_25fps.mp4"),
    ("10766175", "https://videos.pexels.com/video-files/10766175/10766175-hd_1920_1080_30fps.mp4"),
    ("5550281", "https://videos.pexels.com/video-files/5550281/5550281-hd_1920_1080_25fps.mp4"),
    ("8119721", "https://videos.pexels.com/video-files/8119721/8119721-hd_1920_1080_30fps.mp4"),
    ("15598348", "https://videos.pexels.com/video-files/15598348/15598348-hd_1920_1080_30fps.mp4"),
    ("8497411", "https://videos.pexels.com/video-files/8497411/8497411-hd_1920_1080_28fps.mp4"),
    ("1321140", "https://videos.pexels.com/video-files/1321140/1321140-hd_1920_1080_30fps.mp4"),
]

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

for vid, url in new_clips:
    out_p = os.path.join(brain, f"pure_nature_{vid}.jpg")
    cmd = [
        "ffmpeg", "-y",
        "-ss", "00:00:03",
        "-headers", "User-Agent: Mozilla/5.0\r\n",
        "-i", url,
        "-vframes", "1",
        "-vf", "scale=960:540",
        out_p
    ]
    p = subprocess.run(cmd, capture_output=True)
    if os.path.exists(out_p):
        print(f"Captured {vid}: {os.path.getsize(out_p)} bytes")
    else:
        print(f"Failed {vid}")
