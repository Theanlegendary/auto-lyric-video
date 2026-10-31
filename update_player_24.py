import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """      <button class="tab-btn" onclick="switchOption(this, 'videos/23_OneRepublic_Counting_Stars_Lyric_Video.mp4', '✨ <strong>23. Counting Stars</strong> — OneRepublic<br><strong>Artwork</strong>: <em>Makoto Shinkai Celestial Shooting Star Night & Grassy Ridge</em> (bg_29).<br>Direct Lyric Connection (We\\'ll Be Counting Stars) • Hooked Title Intro (170pt) • Studio Zero-Lag Vocal Timing • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">23. Counting Stars</span>
        <span style="font-size:11px;opacity:0.8;">Shooting Stars (Spotify 50/50)</span>
      </button>"""

replacement = target + """
      <button class="tab-btn" onclick="switchOption(this, 'videos/24_Lord_Huron_The_Night_We_Met_Lyric_Video.mp4', '✨ <strong>24. The Night We Met</strong> — Lord Huron<br><strong>Artwork</strong>: <em>Makoto Shinkai Cosmic Midnight Starlit Sky, Misty Pine Valley & Solitary Ridge Traveler</em> (bg_30).<br>Direct Lyric Connection (Take me back to the night we met) • Hooked Title Intro (170pt) • Studio Zero-Lag Vocal Timing • Spotify Poppins Bold • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">24. The Night We Met</span>
        <span style="font-size:11px;opacity:0.8;">Celestial Ridge (Spotify 50/50)</span>
      </button>"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated player.html successfully with Tab 24!")
else:
    print("Target not found!")
