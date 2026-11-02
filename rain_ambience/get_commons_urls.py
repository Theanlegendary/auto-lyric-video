import urllib.request
import json
import urllib.parse

titles = [
    "File:Rain chain at japanese temple - july 4 2021.webm",
    "File:Rain drops - Japan -2016 July 20.webm",
    "File:Rain cats and dogs at TOUDEN-GOYA(mountain hut) in OZE.webm"
]

endpoint = "https://commons.wikimedia.org/w/api.php"
headers = {'User-Agent': 'AntigravityVideoBot/1.0 (contact: info@antigravity.ai)'}

for t in titles:
    params = {
        "action": "query",
        "titles": t,
        "prop": "imageinfo",
        "iiprop": "url|size|mime",
        "format": "json"
    }
    url = endpoint + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    pages = data.get("query", {}).get("pages", {})
    for pid, pinfo in pages.items():
        ii = pinfo.get("imageinfo", [{}])[0]
        print(t)
        print("  URL:", ii.get("url"))
        print("  Dimensions:", ii.get("width"), "x", ii.get("height"))
