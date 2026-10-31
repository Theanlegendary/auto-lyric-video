import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

song_dir = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/15_Akon_Lonely"
lrc_path = os.path.join(song_dir, "lrclib_synced.lrc")

with open(lrc_path, "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

def to_sec(ts):
    parts = ts.split(':')
    return round(int(parts[0]) * 60 + float(parts[1]), 2)

events = []
for line in raw_lines:
    line = line.strip()
    m = re.match(r'\[(\d{2}:\d{2}\.\d{2})\]\s*(.*)', line)
    if m:
        t_sec = to_sec(m.group(1))
        text = m.group(2).strip()
        if text:
            events.append((t_sec, text))

print(f"Total events: {len(events)}")
for i, (t, txt) in enumerate(events):
    print(f"{i+1:02d} [{t:06.2f}s] {txt}")
