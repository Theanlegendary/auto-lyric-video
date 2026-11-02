import subprocess
import os

clips = [
    ("852354", "https://videos.pexels.com/video-files/852354/852354-hd_1920_1080_24fps.mp4"),
    ("5571751", "https://videos.pexels.com/video-files/5571751/5571751-hd_1920_1080_24fps.mp4"),
    ("7725992", "https://videos.pexels.com/video-files/7725992/7725992-hd_1920_1080_30fps.mp4"),
    ("10152813", "https://videos.pexels.com/video-files/10152813/10152813-hd_1920_1080_30fps.mp4"),
    ("9737883", "https://videos.pexels.com/video-files/9737883/9737883-hd_1920_1080_24fps.mp4"),
    ("10440011", "https://videos.pexels.com/video-files/10440011/10440011-hd_1920_1080_30fps.mp4"),
    ("18300595", "https://videos.pexels.com/video-files/18300595/18300595-hd_1920_1080_25fps.mp4"),
    ("8733059", "https://videos.pexels.com/video-files/8733059/8733059-hd_1920_1080_30fps.mp4"),
]

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

for vid, url in clips:
    out_p = os.path.join(brain, f"firefly_cand_{vid}.jpg")
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
