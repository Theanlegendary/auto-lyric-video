import subprocess
import os

cdn_links = [
    ("17717129", "https://videos.pexels.com/video-files/17717129/17717129-hd_1920_1080_60fps.mp4"),
    ("6507556", "https://videos.pexels.com/video-files/6507556/6507556-hd_1920_1080_25fps.mp4"),
    ("6252535", "https://videos.pexels.com/video-files/6252535/6252535-hd_1920_1080_25fps.mp4"),
    ("5197762", "https://videos.pexels.com/video-files/5197762/5197762-hd_1920_1080_25fps.mp4"),
    ("6252550", "https://videos.pexels.com/video-files/6252550/6252550-hd_1920_1080_30fps.mp4"),
    ("8249126", "https://videos.pexels.com/video-files/8249126/8249126-hd_1920_1080_24fps.mp4"),
    ("6107944", "https://videos.pexels.com/video-files/6107944/6107944-hd_1920_1080_25fps.mp4"),
    ("4184130", "https://videos.pexels.com/video-files/4184130/4184130-hd_1920_1080_25fps.mp4"),
    ("7401029", "https://videos.pexels.com/video-files/7401029/7401029-hd_1920_1080_30fps.mp4"),
    ("4392382", "https://videos.pexels.com/video-files/4392382/4392382-hd_1920_1080_25fps.mp4")
]

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

for vid, url in cdn_links:
    out_p = os.path.join(brain, f"cand_frame_{vid}.jpg")
    cmd = [
        "ffmpeg", "-y",
        "-ss", "00:00:03",
        "-headers", "User-Agent: Mozilla/5.0\r\n",
        "-i", url,
        "-vframes", "1",
        "-vf", "scale=960:540",
        out_p
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out_p):
        print(f"Captured frame for {vid}: {os.path.getsize(out_p)} bytes")
    else:
        print(f"Failed {vid}")
