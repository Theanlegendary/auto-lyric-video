import subprocess
import os

candidates = [
    ("9353501", "https://videos.pexels.com/video-files/9353501/9353501-hd_1920_1080_25fps.mp4"),
    ("13180836", "https://videos.pexels.com/video-files/13180836/13180836-hd_1920_1080_30fps.mp4"),
    ("8110359", "https://videos.pexels.com/video-files/8110359/8110359-hd_1920_1080_30fps.mp4"),
    ("12717007", "https://videos.pexels.com/video-files/12717007/12717007-hd_1920_1080_25fps.mp4"),
    ("11643791", "https://videos.pexels.com/video-files/11643791/11643791-hd_1920_1080_50fps.mp4"),
    ("9328701", "https://videos.pexels.com/video-files/9328701/9328701-hd_1920_1080_30fps.mp4"),
    ("5174040", "https://videos.pexels.com/video-files/5174040/5174040-hd_1920_1080_30fps.mp4"),
    ("3134575", "https://videos.pexels.com/video-files/3134575/3134575-hd_1920_1080_24fps.mp4"),
    ("4828773", "https://videos.pexels.com/video-files/4828773/4828773-hd_1920_1080_25fps.mp4"),
    ("9934612", "https://videos.pexels.com/video-files/9934612/9934612-hd_1920_1080_30fps.mp4"),
    ("5918481", "https://videos.pexels.com/video-files/5918481/5918481-hd_1920_1080_30fps.mp4"),
    ("13446069", "https://videos.pexels.com/video-files/13446069/13446069-hd_1920_1080_30fps.mp4")
]

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

for vid, url in candidates:
    out_p = os.path.join(brain, f"wide_cand_{vid}.jpg")
    cmd = [
        "ffmpeg", "-y",
        "-ss", "00:00:03",
        "-headers", "User-Agent: Mozilla/5.0\r\n",
        "-i", url,
        "-vframes", "1",
        "-vf", "scale=960:540",
        out_p
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(out_p):
        print(f"Captured {vid}: {os.path.getsize(out_p)} bytes")
    else:
        print(f"Failed {vid}")
