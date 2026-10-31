import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

song_dir = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/15_Akon_Lonely"
audio_path = os.path.join(song_dir, "audio_7clouds.mp3")

# Check intro 0-10s
print("Checking intro slice...")
cmd = ['ffmpeg', '-y', '-ss', '0', '-t', '10', '-i', audio_path, '-f', 'null', '-']
res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')
print("Intro check OK")

# Check vocal transition at 24s ("Yo! This one here...")
cmd = ['ffmpeg', '-y', '-ss', '23', '-t', '5', '-i', audio_path, '-f', 'null', '-']
res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')
print("Vocal entrance check OK")
