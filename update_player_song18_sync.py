import sys
sys.stdout.reconfigure(encoding='utf-8')

p = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html'
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

target = "switchOption(this, 'videos/18_Coldplay_Yellow_Lyric_Video.mp4', '✨ <strong>18. Yellow</strong> — Coldplay<br><strong>Artwork</strong>: <em>Coldplay Yellow Celestial Starry Night & Reflective Beach</em> (bg_24).<br>Direct Lyric Connection (Look at the Stars) • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')"

replacement = "switchOption(this, 'videos/18_Coldplay_Yellow_Lyric_Video.mp4', '✨ <strong>18. Yellow (Studio Zero-Lag Sync Edition)</strong> — Coldplay<br><strong>Artwork</strong>: <em>Coldplay Yellow Celestial Starry Night & Reflective Beach</em> (bg_24).<br>Direct Lyric Connection (Look at the Stars) • Studio-Aligned Zero-Lag Vocal Timing • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')"

if target in content:
    content = content.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated player.html description for Song 18!")
else:
    print("Target not found in player.html")
