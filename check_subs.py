import subprocess
import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

for vid in ['w4RXGsLyfXU', '6EEW-9NDM5k']:
    print(f"=== Checking subtitles for {vid} ===")
    cmd = ['yt-dlp', '--list-subs', f'https://www.youtube.com/watch?v={vid}']
    res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')
    print(res.stdout)
