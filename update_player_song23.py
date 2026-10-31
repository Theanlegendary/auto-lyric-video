import sys
sys.stdout.reconfigure(encoding='utf-8')

p = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html'
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''        <span style="font-weight:700;">22. lovely</span>
        <span style="font-size:11px;opacity:0.8;">Celestial Aurora Lake (50/50)</span>
      </button>'''

replacement = '''        <span style="font-weight:700;">22. lovely</span>
        <span style="font-size:11px;opacity:0.8;">Celestial Aurora Lake (50/50)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/23_OneRepublic_Counting_Stars_Lyric_Video.mp4', '✨ <strong>23. Counting Stars</strong> — OneRepublic<br><strong>Artwork</strong>: <em>Makoto Shinkai Celestial Shooting Star Night & Grassy Ridge</em> (bg_29).<br>Direct Lyric Connection (We\\'ll Be Counting Stars) • Hooked Title Intro (170pt) • Studio Zero-Lag Vocal Timing • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">23. Counting Stars</span>
        <span style="font-size:11px;opacity:0.8;">Shooting Stars (Spotify 50/50)</span>
      </button>'''

if target in content:
    content = content.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated player.html with Song 23!")
else:
    print("Target not found in player.html")
