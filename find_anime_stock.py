import requests

url = 'https://commons.wikimedia.org/w/api.php'
queries = [
    'anime sky illustration sunset',
    'lofi anime background city night',
    'digital painting landscape anime dusk'
]
headers = {'User-Agent': 'Mozilla/5.0'}
for q in queries:
    params = {
        'action': 'query',
        'generator': 'search',
        'gsrsearch': q,
        'gsrnamespace': 6,
        'gsrlimit': 10,
        'prop': 'imageinfo',
        'iiprop': 'url|size|mime',
        'format': 'json'
    }
    r = requests.get(url, params=params, headers=headers).json()
    pages = r.get('query', {}).get('pages', {})
    print(f"=== {q} ===")
    for k, v in pages.items():
        ii = v.get('imageinfo', [{}])[0]
        w = ii.get('width', 0)
        h = ii.get('height', 0)
        mime = ii.get('mime', '')
        if w >= 1920 and 'image' in mime:
            print(f"{v.get('title')} ({w}x{h}) -> {ii.get('url')}")
