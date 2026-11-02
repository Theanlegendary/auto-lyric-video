import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

queries = [
    "rain%20forest%20waterfall%20green",
    "rain%20stream%20moss%20forest",
    "rain%20mountain%20landscape%20green",
    "rain%20on%20lake%20green%20forest",
    "bamboo%20rain%20forest",
    "misty%20forest%20rain%20daylight"
]

results = []
seen = set()

for q in queries:
    url = f"https://www.pexels.com/search/videos/{q}/"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'(https://videos\.pexels\.com/video-files/(\d+)/\2-hd_1920_1080_[^\"\'\s<>]+\.mp4)', html)
            for fl, vid in matches:
                if vid not in seen:
                    seen.add(vid)
                    results.append((vid, fl, q))
            print(f"Query '{q}': found {len(matches)}")
    except Exception as e:
        print(f"Query '{q}' error:", e)

print(f"\nTotal bright nature clips found: {len(results)}")
for vid, fl, q in results[:20]:
    print(f"('{vid}', '{fl}'), # {q}")
