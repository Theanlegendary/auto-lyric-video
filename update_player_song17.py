p = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html'
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''        <span style="font-weight:700;">16. Love Yourself</span>
        <span style="font-size:11px;opacity:0.8;">Acoustic Terrace (Spotify 50/50)</span>
      </button>'''

replacement = '''        <span style="font-weight:700;">16. Love Yourself</span>
        <span style="font-size:11px;opacity:0.8;">Acoustic Terrace (Spotify 50/50)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/17_Katy_Perry_The_One_That_Got_Away_Lyric_Video.mp4', '✨ <strong>17. The One That Got Away</strong> — Katy Perry<br><strong>Artwork</strong>: <em>Mustang Coastal Cliff & Radiant Summer Sunset (Radiohead Vibe)</em> (bg_22).<br>Direct Lyric Connection (Mustang to Radiohead) • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">17. The One That Got Away</span>
        <span style="font-size:11px;opacity:0.8;">Mustang Sunset (Spotify 50/50)</span>
      </button>'''

if target in content:
    content = content.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated player.html with Song 17!")
else:
    print("Target not found in player.html")
