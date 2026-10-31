import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

cmd = ['yt-dlp', '--dump-json', 'ytsearch5:Akon Lonely Lyrics']
res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')

for line in res.stdout.strip().split('\n'):
    if line:
        try:
            d = json.loads(line)
            print(f"{d.get('id')} ::: {d.get('title')} ::: {d.get('view_count')} ::: {d.get('duration')}s ::: {d.get('channel')}")
        except Exception as e:
            pass
