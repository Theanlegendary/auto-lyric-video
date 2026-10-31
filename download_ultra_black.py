import os
import sys
import urllib.request

fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
sys.stdout.reconfigure(encoding='utf-8')

urls = {
    'Ultra-Regular.ttf': 'https://github.com/google/fonts/raw/main/ofl/ultra/Ultra-Regular.ttf',
    'Montserrat-BlackItalic.ttf': 'https://github.com/google/fonts/raw/main/ofl/montserrat/Montserrat-BlackItalic.ttf',
    'Nunito-BlackItalic.ttf': 'https://github.com/google/fonts/raw/main/ofl/nunito/Nunito-BlackItalic.ttf',
    'Poppins-BlackItalic.ttf': 'https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-BlackItalic.ttf',
    'Rubik-BlackItalic.ttf': 'https://github.com/google/fonts/raw/main/ofl/rubik/Rubik-BlackItalic.ttf',
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
