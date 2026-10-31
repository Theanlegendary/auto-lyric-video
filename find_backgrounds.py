import requests

url = 'https://commons.wikimedia.org/w/api.php'
params = {
    'action': 'query',
    'generator': 'search',
    'gsrsearch': 'sunset silhouette landscape dusk',
    'gsrnamespace': 6,
    'gsrlimit': 25,
    'prop': 'imageinfo',
    'iiprop': 'url|size|mime',
    'format': 'json'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
r = requests.get(url, params=params, headers=headers)
data = r.json()
pages = data.get('query', {}).get('pages', {})
print(f"Found {len(pages)} candidate files.")
for k, v in pages.items():
    ii = v.get('imageinfo', [{}])[0]
    w = ii.get('width', 0)
    h = ii.get('height', 0)
    mime = ii.get('mime', '')
    url_img = ii.get('url', '')
    if w >= 1920 and h >= 1080 and ('jpeg' in mime or 'png' in mime or 'jpg' in mime):
        print(f"TITLE: {v.get('title')}")
        print(f"SIZE: {w}x{h}")
        print(f"URL: {url_img}")
        print("-" * 40)
