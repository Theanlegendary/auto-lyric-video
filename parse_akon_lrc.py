import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

song_dir = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/15_Akon_Lonely"
lrc_path = os.path.join(song_dir, "lrclib_synced.lrc")

with open(lrc_path, "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

def to_sec(ts):
    # ts is mm:ss.xx
    parts = ts.split(':')
    m = int(parts[0])
    s = float(parts[1])
    return round(m * 60 + s, 2)

parsed = []
for line in raw_lines:
    line = line.strip()
    m = re.match(r'\[(\d{2}:\d{2}\.\d{2})\]\s*(.*)', line)
    if m:
        t_str, text = m.groups()
        t_sec = to_sec(t_str)
        text = text.strip()
        if text:
            parsed.append((t_sec, text))

print(f"Parsed {len(parsed)} vocal events.")
for i in range(min(15, len(parsed))):
    print(f"{parsed[i][0]:.2f}s: {parsed[i][1]}")
