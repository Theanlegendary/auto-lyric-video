import sys
sys.stdout.reconfigure(encoding='utf-8')

p = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html'
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''        <span style="font-weight:700;">21. Clocks</span>
        <span style="font-size:11px;opacity:0.8;">Cosmic Starlight (Spotify 50/50)</span>
      </button>'''

replacement = '''        <span style="font-weight:700;">21. Clocks</span>
        <span style="font-size:11px;opacity:0.8;">Cosmic Starlight (Spotify 50/50)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/22_Billie_Eilish_Khalid_lovely_Lyric_Video.mp4', '✨ <strong>22. lovely</strong> — Billie Eilish & Khalid<br><strong>Artwork</strong>: <em>Makoto Shinkai Ethereal Celestial Aurora Lake</em> (bg_28).<br>Direct Lyric Connection (Even if it takes all night) • Studio Zero-Lag Vocal Timing • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">22. lovely</span>
        <span style="font-size:11px;opacity:0.8;">Celestial Aurora Lake (50/50)</span>
      </button>'''

if target in content:
    content = content.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated player.html with Song 22!")
else:
    print("Target not found in player.html")
