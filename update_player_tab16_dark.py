p = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html'
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''      <button class="tab-btn" onclick="switchOption(this, 'videos/16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4', '✨ <strong>16. Love Yourself</strong> — Justin Bieber<br><strong>Artwork</strong>: <em>Sunlit Coastal Terrace & Acoustic Guitar Breeze</em> (bg_21).<br>Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">16. Love Yourself</span>
        <span style="font-size:11px;opacity:0.8;">Acoustic Terrace (Spotify 50/50)</span>
      </button>'''

replacement = '''      <button class="tab-btn" onclick="switchOption(this, 'videos/16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4', '✨ <strong>16. Love Yourself (Clean Dark Celestial Sky Edition)</strong> — Justin Bieber<br><strong>Artwork</strong>: <em>Clean Dark Celestial Starry Night Sky & Solitary Ridge</em> (bg_23).<br>Requested Dark Sky • High Contrast for White Typography • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">16. Love Yourself</span>
        <span style="font-size:11px;opacity:0.8;">Clean Dark Starry Sky (50/50)</span>
      </button>'''

if target in content:
    content = content.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated player.html for Love Yourself Dark Sky Edition!")
else:
    print("Target not found in player.html")
