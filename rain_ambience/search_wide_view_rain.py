import urllib.request
import re
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

queries = [
    "rain%20forest%20landscape%20wide",
    "heavy%20rain%20nature%20landscape",
    "rain%20cabin%20forest%20wide",
    "rain%20storm%20mountains%20forest",
    "rain%20valley%20nature"
]

all_vids = []
for q in queries:
    url = f"https://www.pexels.com/search/videos/{q}/"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            v_links = re.findall(r'https://videos\.pexels\.com/video-files/\d+/\d+-hd_1920_1080_[^\"\'\s<>]+\.mp4', html)
            for v in v_links:
                if v not in all_vids:
                    all_vids.append(v)
            print(f"Query {q}: found {len(v_links)}")
    except Exception as e:
        print(f"Query {q} error:", e)

print(f"\nTotal unique 1080p wide view clips: {len(all_vids)}")
for v in all_vids[:20]:
    print(" ", v)
