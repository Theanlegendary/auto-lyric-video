import subprocess
import json
import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

song_dir = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/15_Akon_Lonely"
audio_path = os.path.join(song_dir, "audio_7clouds.mp3")

# Probe duration with ffmpeg
cmd = ['ffmpeg', '-i', audio_path]
res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')
dur_match = re.search(r'Duration:\s*(\d+):(\d+):(\d+\.\d+)', res.stderr)
if dur_match:
    h, m, s = dur_match.groups()
    total_sec = int(h)*3600 + int(m)*60 + float(s)
    print("7clouds duration (seconds):", total_sec)

# Check for synced lyrics via lrclib API
import urllib.request
import urllib.parse

url = f"https://lrclib.net/api/get?artist_name={urllib.parse.quote('Akon')}&track_name={urllib.parse.quote('Lonely')}"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("Track Name:", data.get('trackName'))
        print("Duration in API:", data.get('duration'))
        print("Synced lyrics found:", bool(data.get('syncedLyrics')))
        if data.get('syncedLyrics'):
            with open(os.path.join(song_dir, "lrclib_synced.lrc"), "w", encoding="utf-8") as lf:
                lf.write(data['syncedLyrics'])
            print("\nFirst 25 lines of lrclib_synced.lrc:")
            for l in data['syncedLyrics'].split('\n')[:25]:
                print(l)
except Exception as e:
    print("Error fetching lrclib:", e)
