import urllib.request
import os

top_clips = [
    ("clip_7843122_tin_roof_forest_rain.mp4", "https://videos.pexels.com/video-files/7843122/7843122-hd_1920_1080_30fps.mp4"),
    ("clip_4169229_corrugated_tin_pine_forest.mp4", "https://videos.pexels.com/video-files/4169229/4169229-hd_1920_1080_25fps.mp4"),
    ("clip_6252550_roof_trees_heavy_rain.mp4", "https://videos.pexels.com/video-files/6252550/6252550-hd_1920_1080_30fps.mp4")
]

out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips"
os.makedirs(out_dir, exist_ok=True)

for name, url in top_clips:
    dest = os.path.join(out_dir, name)
    if not os.path.exists(dest):
        print(f"Downloading {name}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {name}: {os.path.getsize(dest)} bytes")
    else:
        print(f"{name} already exists: {os.path.getsize(dest)} bytes")
