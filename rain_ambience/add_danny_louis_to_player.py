import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html")
content = player_path.read_text(encoding='utf-8')

target = '<!-- ANIMATED RAIN & LIGHT THUNDER HERO SHOWCASE -->'

new_btn = """<!-- 70M-VIEW DANNY LOUIS TIN ROOF STYLE SHOWCASE -->
      <button class="tab-btn" style="border-color: #f59e0b; background: rgba(245, 158, 11, 0.30); box-shadow: 0 0 24px rgba(245, 158, 11, 0.60); border-width: 2px;" onclick="switchOption(this, 'videos/tin_roof_rain_forest_danny_louis_style.mp4', '⛈️ <strong>Viral 70M-View Style: Heavy Rain on Tin Roof in Foggy Rainforest</strong> (Danny Louis Replica)<br><strong>Camera POV</strong>: <em>Underneath Weathered Tin Roof Overhang looking out at Misty Murky Rainforest — Zero \\'Rain Inside\\' Issue</em>.<br><strong>Visual FX</strong>: <em>Active Water Streams & Droplets Cascading off Corrugated Metal Roof Eaves + Rain Pouring Across Forest</em>.<br><strong>Acoustics</strong>: <em>Authentic Metallic Tin Roof Clatter + Deep Rolling Thunder Growls</em> • <strong>100% Seamless Looping</strong>.')">
        <span style="font-weight:900; color:#fbbf24;">⛈️ 70M-View Style: Tin Roof Rain</span>
        <span style="font-size:11px;opacity:0.95; color:#fde68a;">Danny Louis Replica (1:00)</span>
      </button>

      <!-- ANIMATED RAIN & LIGHT THUNDER HERO SHOWCASE -->"""

if target in content:
    content = content.replace(target, new_btn)
    player_path.write_text(content, encoding='utf-8')
    print("SUCCESS: Added Danny Louis 70M-View Style tab to player.html!")
else:
    print("ERROR: Target not found in player.html")
