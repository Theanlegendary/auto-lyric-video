import urllib.request
import os

url = "https://videos.pexels.com/video-files/5174040/5174040-hd_1920_1080_30fps.mp4"
dest = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_5174040_alpine_lake_rain.mp4"

headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
print("Downloading Option 1 (Alpine Lake)...")
with urllib.request.urlopen(req) as resp, open(dest, "wb") as f:
    f.write(resp.read())

print("Downloaded Option 1 size:", os.path.getsize(dest) / (1024*1024), "MB")
