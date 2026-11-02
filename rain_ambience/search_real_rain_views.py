import urllib.request
import re
import os
import sys

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

queries = [
    "rain%20forest%20cabin",
    "cozy%20rain%20nature",
    "heavy%20rain%20trees",
    "rain%20window%20forest",
    "rain%20on%20roof%20forest"
]

all_vids = []

for q in queries:
    url = f"https://www.pexels.com/search/videos/{q}/"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # find 1080p links: e.g. -hd_1920_1080
            v_links = re.findall(r'https://videos\.pexels\.com/video-files/\d+/\d+-hd_1920_1080_[^\"\'\s<>]+\.mp4', html)
            for v in v_links:
                if v not in all_vids:
                    all_vids.append(v)
            print(f"Query {q}: found {len(v_links)} 1080p clips")
    except Exception as e:
        print(f"Query {q} error:", e)

print(f"\nTotal unique 1080p clips found: {len(all_vids)}")
for v in all_vids[:15]:
    print(" ", v)
