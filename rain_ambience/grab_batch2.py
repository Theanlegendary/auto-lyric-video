import subprocess
import os

cdn_links = [
    ("4059614", "https://videos.pexels.com/video-files/4059614/4059614-hd_1920_1080_30fps.mp4"),
    ("18154174", "https://videos.pexels.com/video-files/18154174/18154174-hd_1920_1080_30fps.mp4"),
    ("3999402", "https://videos.pexels.com/video-files/3999402/3999402-hd_1920_1080_24fps.mp4"),
    ("17843344", "https://videos.pexels.com/video-files/17843344/17843344-hd_1920_1080_24fps.mp4"),
    ("7843122", "https://videos.pexels.com/video-files/7843122/7843122-hd_1920_1080_30fps.mp4"),
    ("4169229", "https://videos.pexels.com/video-files/4169229/4169229-hd_1920_1080_25fps.mp4"),
    ("9454925", "https://videos.pexels.com/video-files/9454925/9454925-hd_1920_1080_24fps.mp4"),
    ("5091073", "https://videos.pexels.com/video-files/5091073/5091073-hd_1920_1080_30fps.mp4"),
    ("4169213", "https://videos.pexels.com/video-files/4169213/4169213-hd_1920_1080_25fps.mp4"),
    ("5112049", "https://videos.pexels.com/video-files/5112049/5112049-hd_1920_1080_25fps.mp4"),
    ("1774955", "https://videos.pexels.com/video-files/1774955/1774955-hd_1920_1080_25fps.mp4"),
    ("3700375", "https://videos.pexels.com/video-files/3700375/3700375-hd_1920_1080_25fps.mp4")
]

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

for vid, url in cdn_links:
    out_p = os.path.join(brain, f"cand2_frame_{vid}.jpg")
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
