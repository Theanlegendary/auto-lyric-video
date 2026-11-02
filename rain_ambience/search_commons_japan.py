import urllib.request
import json
import urllib.parse

endpoint = "https://commons.wikimedia.org/w/api.php"
headers = {'User-Agent': 'AntigravityVideoBot/1.0 (contact: info@antigravity.ai)'}

searches = [
    "filetype:video rain japan",
    "filetype:video rain kyoto",
    "filetype:video rain japanese house",
    "filetype:video rain temple japan",
    "filetype:video rain hanok",
    "filetype:video rain garden"
]

all_files = []
seen = set()

for q in searches:
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": q,
        "srnamespace": "6",
        "srlimit": "15"
    }
    url = endpoint + "?" + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        items = data.get("query", {}).get("search", [])
        print(f"Query '{q}': found {len(items)} items")
        for it in items:
            t = it["title"]
            if t not in seen:
                seen.add(t)
                all_files.append((t, q))
    except Exception as e:
        print(f"Error for '{q}':", e)

print(f"\nTotal unique Wikimedia Commons videos: {len(all_files)}")
for t, q in all_files:
    print(f"  {t}")
