import urllib.request
import re
import os
import subprocess
import cv2

ids = [
    "17717129", "6507556", "6252535", "5197762", "6252550", 
    "8249126", "6107944", "4184130", "7401029", "4392382"
]

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
headers = {'User-Agent': 'Mozilla/5.0'}

print("Checking Pexels titles and thumbnails...")
for vid in ids:
    page_url = f"https://www.pexels.com/video/{vid}/"
    try:
        req = urllib.request.Request(page_url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            title_m = re.search(r'<title>(.*?)</title>', html)
            title = title_m.group(1) if title_m else "Unknown"
            # find poster image
            poster_m = re.search(r'https://images\.pexels\.com/videos/\d+/[^\"\'\s<>]+\.(?:jpg|jpeg|png)', html)
            poster = poster_m.group(0) if poster_m else None
            print(f"ID {vid}: {title}")
            if poster:
                # download poster for inspection
                poster_path = os.path.join(brain, f"pexels_thumb_{vid}.jpg")
                urllib.request.urlretrieve(poster, poster_path)
    except Exception as e:
        print(f"ID {vid} error:", e)
