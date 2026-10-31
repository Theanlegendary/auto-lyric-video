import sys
sys.stdout.reconfigure(encoding='utf-8')

p = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html'
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''        <span style="font-weight:700;">18. Yellow</span>
        <span style="font-size:11px;opacity:0.8;">Starry Beach (Spotify 50/50)</span>
      </button>'''

replacement = '''        <span style="font-weight:700;">18. Yellow</span>
        <span style="font-size:11px;opacity:0.8;">Starry Beach (Spotify 50/50)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/19_Coldplay_A_Sky_Full_of_Stars_Lyric_Video.mp4', '✨ <strong>19. A Sky Full of Stars</strong> — Coldplay<br><strong>Artwork</strong>: <em>Makoto Shinkai Cosmic Sapphire Starlit Sky & Solitary Overlook</em> (bg_25).<br>Direct Lyric Connection (\'Cause you\'re a sky full of stars) • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">19. A Sky Full of Stars</span>
        <span style="font-size:11px;opacity:0.8;">Cosmic Sapphire (Spotify 50/50)</span>
      </button>'''

if target in content:
    content = content.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated player.html with Song 19!")
else:
    print("Target not found in player.html")
