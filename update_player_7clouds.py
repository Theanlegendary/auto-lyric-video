import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html")
content = player_path.read_text(encoding='utf-8')

# 1. Update the showcase button for yung kai blue
old_btn_showcase = """          <!-- yung kai blue Pair -->
          <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: rgba(0, 0, 0, 0.25); padding: 8px 12px; border-radius: 10px;">
            <span style="font-size: 12px; font-weight: 800; color: #38bdf8; min-width: 140px;">🎵 yung kai blue:</span>
            <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(56, 189, 248, 0.85); background: rgba(56, 189, 248, 0.25);" onclick="switchOption(this, 'videos/28_yung_kai_blue_Slowed_Reverb_Lyric_Video.mp4', '🎵 <strong>yung kai — blue (Slowed + Reverb Brand Edition • Full 4:08)</strong><br>• <strong>1. Slowness</strong>: 0.865x tape varispeed slowdown, stretching romantic longing.<br>• <strong>2. Cathedral Space</strong>: 3.0s acoustic diffusion simulating dawn ocean cliffs.<br>• <strong>3. Cassette Tape Comfort</strong>: -2.5 semitones pitch drop, warm 15.5kHz tape shelf.<br>• <strong>Visual</strong>: Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook (`bg_34`).')">
              ▶ 1. Full Song: Slowed + Reverb (4:08)
            </button>
            <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(255, 255, 255, 0.4); background: rgba(255, 255, 255, 0.08);" onclick="switchOption(this, 'videos/28_yung_kai_blue_Lyric_Video.mp4', '🎧 <strong>yung kai — blue (Original 1.0x Mix • Full 3:34)</strong><br>Standard speed, original acoustic guitar mix.<br>• <strong>Visual</strong>: Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook (`bg_34`).')">
              ▶ 2. Full Song: Original Normal (3:34)
            </button>
          </div>"""

# Replace with clean 7clouds Remaster card
new_btn_showcase = """          <!-- yung kai blue 7clouds Remaster -->
          <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: rgba(56, 189, 248, 0.12); padding: 8px 12px; border-radius: 10px; border: 1px solid rgba(56, 189, 248, 0.4);">
            <span style="font-size: 12px; font-weight: 800; color: #38bdf8; min-width: 140px;">☁️ yung kai blue (7clouds Style):</span>
            <button class="tab-btn active" style="width: auto; padding: 8px 16px; margin: 0; border-color: #38bdf8; background: rgba(56, 189, 248, 0.35);" onclick="switchOption(this, 'videos/28_yung_kai_blue_Lyric_Video.mp4', '☁️ <strong>yung kai — blue (7clouds Clean Aesthetic Remaster • 3:34)</strong><br>• <strong>Formula</strong>: Authentic 7clouds style — breathtaking pastel dawn clouds & sky wallpaper.<br>• <strong>Motion</strong>: Subtle, organic camera drift (zoompan) — zero clunky sliding sprites or blurry foreground particles.<br>• <strong>Typography</strong>: Pure white handwriting with crisp dark outline & soft shadow for razor-sharp legibility.<br>• <strong>Audio</strong>: Original 1.0x Full Mix.')">
              ▶ 7clouds Aesthetic Remaster (3:34) [RECOMMENDED]
            </button>
            <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(255, 255, 255, 0.2); background: rgba(255, 255, 255, 0.05); opacity: 0.6;" onclick="switchOption(this, 'videos/28_yung_kai_blue_Slowed_Reverb_Lyric_Video.mp4', '⏮️ <em>Previous Archive: yung kai — blue (Old Slowed + Reverb 4:08)</em>')">
              ⏮ Archive: Old Slowed (4:08)
            </button>
          </div>"""

# Replace in content if matched, or do regex replace
import re

# Update track list button
old_track_btn = """        <button class="tab-btn" onclick="switchOption(this, 'videos/28_yung_kai_blue_Lyric_Video.mp4', '🎧 <strong>28. blue (Normal 1.0x Mix)</strong> — yung kai<br><strong>Artwork</strong>: <em>Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook</em> (bg_34).<br>Full 3:34 Master • Patrick Hand 200pt Hook Title • Glowing Pure White Typography • Strictly 2-Row Couplets • Seamless Looping Live Cloud Drift.')">
          <span style="font-weight:700;">28. blue</span>
          <span style="font-size:11px;opacity:0.8;">Normal 1.0x (3:34)</span>
        </button>"""

new_track_btn = """        <button class="tab-btn" onclick="switchOption(this, 'videos/28_yung_kai_blue_Lyric_Video.mp4', '☁️ <strong>28. blue (7clouds Aesthetic Remaster)</strong> — yung kai<br><strong>Artwork</strong>: <em>7clouds Aesthetic Pastel Dawn Sky</em> (bg_34).<br>Full 3:34 Master • Patrick Hand Hook Title • Crisp White Typography with Dark Border • Strictly 2-Row Couplets • Subtle Clean Zoompan Drift.')">
          <span style="font-weight:700; color:#38bdf8;">28. blue (7clouds)</span>
          <span style="font-size:11px;opacity:0.8; color:#7dd3fc;">Normal 1.0x (3:34)</span>
        </button>"""

if old_btn_showcase in content:
    content = content.replace(old_btn_showcase, new_btn_showcase)
    print("Replaced showcase pair successfully.")
else:
    # Try finding with regex
    content = re.sub(
        r'<!-- yung kai blue Pair -->.*?(<!-- Sia Chandelier Pair -->|<div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: rgba\(0, 0, 0, 0\.25\); padding: 8px 12px; border-radius: 10px;">\s*<span style="font-size: 12px; font-weight: 800; color: #f43f5e;)',
        new_btn_showcase + r'\n\1',
        content,
        flags=re.DOTALL
    )
    print("Replaced showcase pair via regex.")

if old_track_btn in content:
    content = content.replace(old_track_btn, new_track_btn)
    print("Replaced track button successfully.")
else:
    # regex for 28. blue normal button
    content = re.sub(
        r'<button class="tab-btn" onclick="switchOption\(this, \'videos/28_yung_kai_blue_Lyric_Video\.mp4\'.*?<\/button>',
        new_track_btn.strip(),
        content,
        flags=re.DOTALL
    )
    print("Replaced track button via regex.")

player_path.write_text(content, encoding='utf-8')
print("player.html updated successfully!")
