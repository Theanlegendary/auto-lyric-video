import urllib.request
import re

queries = [
    "rain%20forest",
    "rain%20nature",
    "rain%20mountain",
    "rain%20waterfall",
    "rain%20lake",
    "rain%20trees%20heavy"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

all_pixabay = []
seen = set()

for q in queries:
    url = f'https://pixabay.com/videos/search/{q}/'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        vids = re.findall(r'(https://cdn\.pixabay\.com/video/[^\"]+\.mp4)', html)
        # Filter for 1080p or medium/large
        large_vids = [v for v in vids if ('_large' in v or '_medium' in v or '1080' in v)]
        for v in large_vids:
            if v not in seen:
                seen.add(v)
                all_pixabay.append((v, q))
        print(f"Pixabay Query '{q}': found {len(large_vids)} links")
    except Exception as e:
        print(f"Pixabay Query '{q}' error:", e)

print(f"\nTotal unique Pixabay videos found: {len(all_pixabay)}")
for v, q in all_pixabay[:25]:
    print(f"('{v}'), # {q}")
