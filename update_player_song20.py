import sys
sys.stdout.reconfigure(encoding='utf-8')

p = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html'
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''        <span style="font-weight:700;">19. A Sky Full of Stars</span>
        <span style="font-size:11px;opacity:0.8;">Cosmic Sapphire (Spotify 50/50)</span>
      </button>'''

replacement = '''        <span style="font-weight:700;">19. A Sky Full of Stars</span>
        <span style="font-size:11px;opacity:0.8;">Cosmic Sapphire (Spotify 50/50)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/20_Coldplay_Paradise_Lyric_Video.mp4', '✨ <strong>20. Paradise</strong> — Coldplay<br><strong>Artwork</strong>: <em>Makoto Shinkai Twilight Celestial Dreamscape & Solitary Overlook</em> (bg_26).<br>Direct Lyric Connection (Dreaming of Paradise) • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">20. Paradise</span>
        <span style="font-size:11px;opacity:0.8;">Twilight Dreamscape (Spotify 50/50)</span>
      </button>'''

if target in content:
    content = content.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated player.html with Song 20!")
else:
    print("Target not found in player.html")
