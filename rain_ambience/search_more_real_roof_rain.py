import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
queries = [
    "rain%20pouring%20roof",
    "heavy%20rain%20cabin",
    "rain%20porch",
    "rain%20forest%20trees"
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

print(f"\nTotal new 1080p clips: {len(all_vids)}")
for v in all_vids[:15]:
    print(" ", v)
