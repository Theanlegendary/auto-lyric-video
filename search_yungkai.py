import subprocess, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

cmd = [
    "yt-dlp",
    "ytsearch5:yung kai blue lyrics",
    "--print", "%(id)s | %(title)s | %(duration_string)s | %(channel)s"
]

res = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
print(res.stdout)
