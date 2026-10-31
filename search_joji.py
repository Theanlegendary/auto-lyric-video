import subprocess, sys, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# Search for Joji - Glimpse of Us (7clouds, official, or high quality lyric video)
cmd = [
    "yt-dlp",
    "ytsearch5:Joji Glimpse of Us 7clouds",
    "--print", "%(id)s | %(title)s | %(duration_string)s | %(channel)s"
]

res = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
print(res.stdout)
