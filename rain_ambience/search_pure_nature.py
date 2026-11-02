import urllib.request
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

queries = [
    "rain%20forest%20river%20nature",
    "rain%20mountain%20lake%20fog",
    "waterfall%20rain%20forest",
    "heavy%20rain%20pine%20trees%20nature",
    "misty%20rainforest%20canopy%20rain",
    "rain%20wilderness%20stream%20moss"
]

all_vids = []
seen_ids = set()

for q in queries:
    url = f"https://www.pexels.com/search/videos/{q}/"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'https://videos\.pexels\.com/video-files/(\d+)/\1-hd_1920_1080_[^\"\'\s<>]+\.mp4', html)
            # Full links
            full_links = re.findall(r'(https://videos\.pexels\.com/video-files/(\d+)/\2-hd_1920_1080_[^\"\'\s<>]+\.mp4)', html)
            for fl, vid in full_links:
                if vid not in seen_ids:
                    seen_ids.add(vid)
                    all_vids.append((vid, fl))
            print(f"Query '{q}': found {len(full_links)} links")
    except Exception as e:
        print(f"Query '{q}' error:", e)

print(f"\nTotal new unique pure nature clips found: {len(all_vids)}")
for vid, fl in all_vids[:20]:
    print(f"('{vid}', '{fl}'),")
