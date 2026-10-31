import subprocess, sys

sys.stdout.reconfigure(encoding='utf-8')

cmd = [
    "yt-dlp",
    "ytsearch5:Sia Chandelier lyrics 7clouds",
    "--print", "%(id)s | %(title)s | %(duration_string)s | %(channel)s"
]

res = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
print(res.stdout)
