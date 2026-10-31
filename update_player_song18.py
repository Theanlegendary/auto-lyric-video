p = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html'
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''        <span style="font-weight:700;">17. The One That Got Away</span>
        <span style="font-size:11px;opacity:0.8;">Mustang Sunset (Spotify 50/50)</span>
      </button>'''

replacement = '''        <span style="font-weight:700;">17. The One That Got Away</span>
        <span style="font-size:11px;opacity:0.8;">Mustang Sunset (Spotify 50/50)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/18_Coldplay_Yellow_Lyric_Video.mp4', '✨ <strong>18. Yellow</strong> — Coldplay<br><strong>Artwork</strong>: <em>Coldplay Yellow Celestial Starry Night & Reflective Beach</em> (bg_24).<br>Direct Lyric Connection (Look at the Stars) • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">18. Yellow</span>
        <span style="font-size:11px;opacity:0.8;">Starry Beach (Spotify 50/50)</span>
      </button>'''

if target in content:
    content = content.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated player.html with Song 18!")
else:
    print("Target not found in player.html")
