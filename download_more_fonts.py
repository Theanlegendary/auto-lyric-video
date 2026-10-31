import os
import sys
import urllib.request

fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
sys.stdout.reconfigure(encoding='utf-8')

urls = {
    'Gaegu-Bold.ttf': 'https://github.com/google/fonts/raw/main/ofl/gaegu/Gaegu-Bold.ttf',
    'PatrickHandSC-Regular.ttf': 'https://github.com/google/fonts/raw/main/ofl/patrickhandsc/PatrickHandSC-Regular.ttf',
    'FredokaOne-Regular.ttf': 'https://github.com/google/fonts/raw/main/ofl/fredokaone/FredokaOne-Regular.ttf',
    'ShortStack-Regular.ttf': 'https://github.com/google/fonts/raw/main/ofl/shortstack/ShortStack-Regular.ttf',
    'Itim-Regular.ttf': 'https://github.com/google/fonts/raw/main/ofl/itim/Itim-Regular.ttf',
    'Pangolin-Regular.ttf': 'https://github.com/google/fonts/raw/main/ofl/pangolin/Pangolin-Regular.ttf'
}

for name, url in urls.items():
    dest = os.path.join(fonts_dir, name)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {name}: {os.path.getsize(dest)} bytes")
    except Exception as e:
        print(f"Failed {name}: {e}")
