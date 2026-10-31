p = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html'
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''        <span style="font-weight:700;">15. Lonely (Akon)</span>
        <span style="font-size:11px;opacity:0.8;">Spotify Clear Orange (50/50)</span>
      </button>'''

replacement = '''        <span style="font-weight:700;">15. Lonely (Akon)</span>
        <span style="font-size:11px;opacity:0.8;">80% Night / 20% Sunset Vibe</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4', '✨ <strong>16. Love Yourself</strong> — Justin Bieber<br><strong>Artwork</strong>: <em>Sunlit Coastal Terrace & Acoustic Guitar Breeze</em> (bg_21).<br>Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">16. Love Yourself</span>
        <span style="font-size:11px;opacity:0.8;">Acoustic Terrace (Spotify 50/50)</span>
      </button>'''

if target in content:
    content = content.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated player.html with Song 16!")
else:
    print("Target not found in player.html")
