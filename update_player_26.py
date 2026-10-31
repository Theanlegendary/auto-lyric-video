import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """      <button class="tab-btn" onclick="switchOption(this, 'videos/25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4', '✨ <strong>25. Sweater Weather</strong> — The Neighbourhood<br><strong>Artwork</strong>: <em>Makoto Shinkai Celestial Coastal Twilight & Solitary Knit Sweater Silhouette</em> (bg_31).<br>Direct Lyric Connection (Use the sleeves of my sweater / Too cold for you here) • Hooked Title Intro (170pt) • Studio Zero-Lag Vocal Timing • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">25. Sweater Weather</span>
        <span style="font-size:11px;opacity:0.8;">Coastal Overlook (Spotify 50/50)</span>
      </button>"""

replacement = target + """
      <button class="tab-btn" onclick="switchOption(this, 'videos/26_Tom_Odell_Another_Love_Lyric_Video.mp4', '✨ <strong>26. Another Love</strong> — Tom Odell<br><strong>Artwork</strong>: <em>Makoto Shinkai Clear Pink Aesthetic Sunset & Pine Ridge</em> (bg_32).<br>Direct Lyric Connection (All my tears have been used up) • Until I Found You Clean Style • Patrick Hand Large Typography (102-114pt) • 175pt Title Card • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">26. Another Love</span>
        <span style="font-size:11px;opacity:0.8;">Pink Sunset (Clean Big Text)</span>
      </button>"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated player.html successfully with Tab 26!")
else:
    print("Target not found!")
