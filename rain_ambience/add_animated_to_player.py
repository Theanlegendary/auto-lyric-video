import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html")
content = player_path.read_text(encoding='utf-8')

target = '<!-- RAIN AMBIENCE SHOWCASE -->'

hero_button = """<!-- ANIMATED RAIN & LIGHT THUNDER HERO SHOWCASE -->
      <button class="tab-btn" style="border-color: #10b981; background: rgba(16, 185, 129, 0.25); box-shadow: 0 0 20px rgba(16, 185, 129, 0.50); border-width: 2px;" onclick="switchOption(this, 'videos/cozy_forest_light_rain_thunder_animated_loop.mp4', '🌲🌧️ <strong>Featured Master: Cozy Forest Cabin (Active Animated Rain & Light Thunder • 1:00 Loop)</strong><br><strong>Visuals</strong>: <em>Active Animated Falling Rain Streaks + Window Glass Trickling Rivulets + Synchronized Distant Lightning Flash + Lush Misty Pine Forest</em>.<br><strong>Audio</strong>: <em>Gentle Light Rain Patter + Soothing Soft Pine Drizzle + 2 Mellow Low-Frequency Rolling Thunder Rumbles</em> • <strong>100% Mathematically Seamless Equal-Power Loop</strong>.<br>Full 1080p 60fps Master • Deep Sleep, Focus & Relax Sanctuary.')">
        <span style="font-weight:800; color:#34d399;">🌲🌧️ Forest Cabin (Animated Rain)</span>
        <span style="font-size:11px;opacity:0.95; color:#a7f3d0;">Light Rain + Thunder (1:00)</span>
      </button>

      <!-- RAIN AMBIENCE SHOWCASE -->"""

if target in content:
    content = content.replace(target, hero_button)
    player_path.write_text(content, encoding='utf-8')
    print("SUCCESS: Added Featured Animated Forest Rain tab to player.html!")
else:
    print("ERROR: Target not found in player.html")
