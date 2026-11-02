import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

queries = [
    "rain%20forest",
    "rain%20on%20roof",
    "rain%20drops%20nature"
]

all_1080p = []

for q in queries:
    url = f"https://www.pexels.com/search/videos/{q}/?orientation=landscape"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            links = set(re.findall(r'https://videos\.pexels\.com/video-files/[^\"\'\s<>]+\.mp4', html))
            for l in links:
                if "1920_1080" in l or "hd_1920" in l:
                    all_1080p.append(l)
    except Exception as e:
        print(f"Error on {q}:", e)

all_1080p = list(set(all_1080p))
print(f"Found {len(all_1080p)} 1080p landscape nature rain video links:")
for i, l in enumerate(all_1080p[:10]):
    print(f"{i}: {l}")
