import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html")
content = player_path.read_text(encoding='utf-8')

target = """      <button class="tab-btn" style="border-color: #f97316; background: rgba(249, 115, 22, 0.18); box-shadow: 0 0 16px rgba(249, 115, 22, 0.35);" onclick="switchOption(this, 'videos/30_Ed_Sheeran_Perfect_Slowed_Reverb_Sunset_Edition_Lyric_Video.mp4', '🌅 <strong>30. Perfect (Sunset Amber Dusk • Authentic 7clouds Edo SZ Edition)</strong> — Ed Sheeran<br><strong>Artwork & Typography</strong>: <em>7clouds Warm Golden-Amber Dusk Clouds</em> with Authentic Edo SZ Brush Script in Sentence Case.<br>Full 5:05 Master • Slowed + Reverb (0.865x) • Lower-Third 78% Down • Soft Black Glow & Shadow • Zero-Frame Cuts • Rest-Cut Breathing Room.')">
        <span style="font-weight:700; color:#fb923c;">🌅 30. Perfect (Sunset Mode)</span>
        <span style="font-size:11px;opacity:0.9; color:#fed7aa;">Edo SZ • Slowed (5:05)</span>
      </button>"""

rain_buttons = target + """
      <!-- RAIN AMBIENCE SHOWCASE -->
      <button class="tab-btn" style="border-color: #6366f1; background: rgba(99, 102, 241, 0.22); box-shadow: 0 0 16px rgba(99, 102, 241, 0.40);" onclick="switchOption(this, 'videos/rain_bedroom_1min_loop_sample.mp4', '🌧️ <strong>Sample A: Cozy Bedroom at Night (Rain on Window & Distant Thunder)</strong><br><strong>Audio Engineering</strong>: <em>3D Spatial Binaural Rain</em> • Delicate Droplet Taps on Glass • Soothing Steady Downpour • Low-Frequency Cinematic Rolling Thunder • <strong>100% Seamless Equal-Power Loop (Zero Clicks / Zero Volume Dips)</strong>.<br>Full 1080p Master • Lo-Fi Bedroom Lamp Aesthetic • Perfect for Sleep, Studying & Night Relaxation.')">
        <span style="font-weight:700; color:#818cf8;">🌧️ Rain: Cozy Bedroom</span>
        <span style="font-size:11px;opacity:0.9; color:#c7d2fe;">Seamless Loop (1:00)</span>
      </button>
      <button class="tab-btn" style="border-color: #06b6d4; background: rgba(6, 182, 212, 0.22); box-shadow: 0 0 16px rgba(6, 182, 212, 0.40);" onclick="switchOption(this, 'videos/rain_coffeeshop_1min_loop_sample.mp4', '☕ <strong>Sample B: Late Night Tokyo Coffee Shop (Rain on Glass & Neon Bokeh)</strong><br><strong>Audio Engineering</strong>: <em>Warm Indoor Acoustic Rain</em> • Soft Raindrops on Awning • Low-Pass Interior Filter • Warm 130Hz Room Resonance • <strong>100% Seamless Equal-Power Loop</strong>.<br>Full 1080p Master • Steaming Coffee Mug & Blurred Rainy Tokyo Street Neon • Ultimate Coding / Focus Vibe.')">
        <span style="font-weight:700; color:#22d3ee;">☕ Rain: Tokyo Cafe</span>
        <span style="font-size:11px;opacity:0.9; color:#a5f3fc;">Seamless Loop (1:00)</span>
      </button>
      <button class="tab-btn" style="border-color: #f59e0b; background: rgba(245, 158, 11, 0.22); box-shadow: 0 0 16px rgba(245, 158, 11, 0.40);" onclick="switchOption(this, 'videos/rain_cabin_1min_loop_sample.mp4', '🔥 <strong>Sample C: Forest Wooden Cabin (Rain on Tin Roof & Crackling Fireplace)</strong><br><strong>Audio Engineering</strong>: <em>Cozy Hearth & Nature Soundscape</em> • Dense Rain Pattering on Pine Needles & Tin Roof • Authentic Burning Log Ember Crackles & Micro-Pops • Warm Fireplace Low Rumble • <strong>100% Seamless Equal-Power Loop</strong>.<br>Full 1080p Master • Stone Fireplace Glow & Rainy Evergreen Forest Sanctuary.')">
        <span style="font-weight:700; color:#fbbf24;">🔥 Rain: Forest Cabin</span>
        <span style="font-size:11px;opacity:0.9; color:#fde68a;">Seamless Loop (1:00)</span>
      </button>"""

if target in content:
    content = content.replace(target, rain_buttons)
    player_path.write_text(content, encoding='utf-8')
    print("SUCCESS: Added 3 Rain Ambience tabs to player.html!")
else:
    print("ERROR: Target button not found in player.html")
