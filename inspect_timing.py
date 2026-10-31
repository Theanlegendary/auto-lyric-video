import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

song_dir = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/15_Akon_Lonely"
srt_path = os.path.join(song_dir, "official_sub.en-nP7-2PuUl7o.srt")

with open(srt_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("First 35 lines of official .srt:")
for l in lines[:35]:
    print(l.rstrip())
