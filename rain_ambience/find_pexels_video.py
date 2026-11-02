import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.pexels.com/search/videos/rain%20forest/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        v_links = list(set(re.findall(r'https://videos\.pexels\.com/video-files/[^\"\'\s<>]+\.mp4', html)))
        print(f"Found {len(v_links)} direct Pexels video files:")
        for v in v_links[:5]:
            print(" ", v)
except Exception as e:
    print("Error:", e)
