import urllib.request
import os

clips = [
    ("clip_12717007_wide_rainforest_cabin.mp4", "https://videos.pexels.com/video-files/12717007/12717007-hd_1920_1080_25fps.mp4"),
    ("clip_13446069_wide_foggy_pine_forest_rain.mp4", "https://videos.pexels.com/video-files/13446069/13446069-hd_1920_1080_30fps.mp4")
]

out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips"
os.makedirs(out_dir, exist_ok=True)

for name, url in clips:
    dest = os.path.join(out_dir, name)
    if not os.path.exists(dest):
        print(f"Downloading {name}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {name}: {os.path.getsize(dest)} bytes")
    else:
        print(f"{name} already exists: {os.path.getsize(dest)} bytes")
