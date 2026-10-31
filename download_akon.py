import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
song_dir = os.path.join(base, "songs", "15_Akon_Lonely")
os.makedirs(song_dir, exist_ok=True)

# 1. Download official subtitles from 6EEW-9NDM5k
print("Downloading official subtitles from 6EEW-9NDM5k...")
cmd_sub = [
    'yt-dlp',
    '--sub-lang', 'en-nP7-2PuUl7o,en',
    '--write-sub',
    '--convert-subs', 'srt',
    '--skip-download',
    '-o', os.path.join(song_dir, 'official_sub'),
    'https://www.youtube.com/watch?v=6EEW-9NDM5k'
]
res = subprocess.run(cmd_sub, capture_output=True, text=True, errors='ignore')
print(res.stdout)
print(res.stderr)

# 2. Download audio from 7clouds (clean studio audio upload, no MV skits)
print("Downloading 7clouds audio (w4RXGsLyfXU)...")
cmd_audio_7c = [
    'yt-dlp',
    '-x',
    '--audio-format', 'mp3',
    '--audio-quality', '0',
    '-o', os.path.join(song_dir, 'audio_7clouds.mp3'),
    'https://www.youtube.com/watch?v=w4RXGsLyfXU'
]
res = subprocess.run(cmd_audio_7c, capture_output=True, text=True, errors='ignore')
print(res.stdout)
print(res.stderr)

# 3. Check files in song_dir
print("Files in song_dir:", os.listdir(song_dir))
