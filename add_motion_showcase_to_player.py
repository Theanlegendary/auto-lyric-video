import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

motion_section = """    <!-- 5 MOTION / ENTRANCE CHOICES (1-MIN COMPARISONS) -->
    <div style="background: linear-gradient(135deg, rgba(255, 77, 141, 0.15), rgba(20, 10, 30, 0.85)); border: 1px solid rgba(255, 77, 141, 0.5); border-radius: 16px; padding: 20px; margin-bottom: 25px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 12px; flex-wrap:wrap; gap:8px;">
        <span style="background:linear-gradient(45deg, #ff4d8d, #ff8da6); color:#000; font-weight:800; font-size:12px; padding:5px 12px; border-radius:12px; text-transform:uppercase; letter-spacing:0.5px;">🔥 How the Music Plays & Lyrics Come In (Motion Showdown)</span>
        <span style="font-size:13px; color:#ff8da6; font-weight:600;">Click to Watch Each 1-Minute Transition Style</span>
      </div>
      <div class="tabs" style="grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); margin-bottom: 0;">
        <button class="tab-btn active" style="border-color: rgba(255, 77, 141, 0.6);" onclick="switchOption(this, 'videos/motion1_spotify_word_glow.mp4', '🎤 <strong>Motion 1: Real-Time Karaoke Word Glow (\\\\kf)</strong><br>Words appear in soft gray, and light up in pure glowing white in real-time sync with the singer\\'s voice!')">
          <span style="font-weight:700;">1. Karaoke Word Glow</span>
          <span style="font-size:11px;opacity:0.8;">Real-Time Word Highlight (\\\\kf)</span>
        </button>
        <button class="tab-btn" style="border-color: rgba(29, 185, 84, 0.6);" onclick="switchOption(this, 'videos/motion2_spotify_teleprompter.mp4', '📱 <strong>Motion 2: Spotify Vertical Teleprompter</strong><br>Authentic Spotify app UI: Active singing line is bright white & enlarged in the center; past and upcoming lines are dimmed gray, smoothly scrolling upward!')">
          <span style="font-weight:700;">2. Spotify Teleprompter</span>
          <span style="font-size:11px;opacity:0.8;">Active Line Highlight & Scroll</span>
        </button>
        <button class="tab-btn" style="border-color: rgba(120, 220, 255, 0.6);" onclick="switchOption(this, 'videos/motion3_kinetic_slide_up.mp4', '🌊 <strong>Motion 3: Kinetic Smooth Slide-Up Float (\\\\move)</strong><br>Couplets glide smoothly upward into the center with an optical ease-out curve, breathing naturally with the beat!')">
          <span style="font-weight:700;">3. Smooth Slide-Up</span>
          <span style="font-size:11px;opacity:0.8;">Kinetic Upward Float (\\\\move)</span>
        </button>
        <button class="tab-btn" style="border-color: rgba(255, 180, 0, 0.6);" onclick="switchOption(this, 'videos/motion4_progressive_2step.mp4', '🪜 <strong>Motion 4: Progressive 2-Step Line Drop-In</strong><br>Line 1 appears first on vocal onset; Line 2 drops in below it right when the second line begins singing!')">
          <span style="font-weight:700;">4. Progressive 2-Step</span>
          <span style="font-size:11px;opacity:0.8;">Line 1 then Line 2 Drop-In</span>
        </button>
        <button class="tab-btn" style="border-color: rgba(180, 100, 255, 0.6);" onclick="switchOption(this, 'videos/motion5_optical_bloom_pulse.mp4', '✨ <strong>Motion 5: Optical Bloom Pulse on Beat</strong><br>Text punches in with a subtle scale bloom (90% to 100%) on the vocal beat attack, then holds firmly in place!')">
          <span style="font-weight:700;">5. Optical Bloom Pulse</span>
          <span style="font-size:11px;opacity:0.8;">Scale Bloom on Beat (90->100%)</span>
        </button>
      </div>
    </div>
"""

target = '<!-- 5 SPOTIFY STYLE CHOICES (1-MIN COMPARISONS) -->'
if target in content:
    content = content.replace(target, motion_section + '\n    ' + target, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Motion Showdown section to player.html successfully!")
else:
    print("Target not found in player.html")
