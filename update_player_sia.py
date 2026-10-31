import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html")
content = player_path.read_text(encoding='utf-8')

# 1. Add Tabs 29 and 29B
target_tab = """      <button class="tab-btn" onclick="switchOption(this, 'videos/28_yung_kai_blue_Slowed_Reverb_Lyric_Video.mp4', '✨ <strong>28. blue (Slowed + Reverb Brand Edition)</strong> — yung kai<br><strong>Artwork</strong>: <em>Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook</em> (bg_34).<br>Full 4:08 Master • 0.865x Tape Varispeed • 3.0s Cathedral Reverb • 15.5kHz Tape Warmth • Patrick Hand 200pt Hook Title • Strictly 2-Row Couplets.')">
        <span style="font-weight:700; color:#d8b4fe;">28. blue (Slowed)</span>
        <span style="font-size:11px;opacity:0.8; color:#e9d5ff;">Slowed + Reverb (4:08)</span>
      </button>"""

new_tabs = target_tab + """
      <button class="tab-btn" onclick="switchOption(this, 'videos/29_Sia_Chandelier_Lyric_Video.mp4', '✨ <strong>29. Chandelier (Normal 1.0x Mix)</strong> — Sia<br><strong>Artwork</strong>: <em>Radiant Celestial Prism Bokeh & Penthouse Night Sky</em> (bg_35).<br>Full 3:32 Master • Patrick Hand 200pt Hook Title • Glowing Pure White Typography • Strictly 2-Row Couplets • Seamless Looping Live Clouds & Golden Chandelier Bokeh Lights (Layered Strictly Behind Lyrics).')">
        <span style="font-weight:700;">29. Chandelier</span>
        <span style="font-size:11px;opacity:0.8;">Normal 1.0x (3:32)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/29_Sia_Chandelier_Slowed_Reverb_Lyric_Video.mp4', '✨ <strong>29. Chandelier (Slowed + Reverb Brand Edition)</strong> — Sia<br><strong>Artwork</strong>: <em>Radiant Celestial Prism Bokeh & Penthouse Night Sky</em> (bg_35).<br>Full 4:06 Master • 0.865x Tape Varispeed (117 &rarr; 101.2 BPM) • 3.0s Cathedral Reverb Hall • -2.5 Semitones Pitch Drop • 15.5kHz Warm Tape Shelf • Live Shimmering Lights Behind Lyrics.')">
        <span style="font-weight:700; color:#d8b4fe;">29. Chandelier (Slowed)</span>
        <span style="font-size:11px;opacity:0.8; color:#e9d5ff;">Slowed + Reverb (4:06)</span>
      </button>"""

if target_tab in content:
    content = content.replace(target_tab, new_tabs, 1)
    print("Successfully added Song 29 tabs.")
else:
    print("Error: target_tab not found!")
    sys.exit(1)

# 2. Add Showdown block for Song 29
target_showdown = """          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(255, 255, 255, 0.4); background: rgba(255, 255, 255, 0.08);" onclick="switchOption(this, 'videos/28_yung_kai_blue_Lyric_Video.mp4', '💿 <strong>yung kai — blue (Original 1.0x Mix • Full 3:34)</strong><br>Standard speed, original acoustic guitar mix.<br>• <strong>Visual</strong>: Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook (`bg_34`).')">
            ▶ 2. Full Song: Original Normal (3:34)
          </button>
        </div>"""

new_showdown = target_showdown + """
        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: rgba(0, 0, 0, 0.25); padding: 8px 12px; border-radius: 10px;">
          <span style="font-size: 12px; font-weight: 800; color: #f43f5e; min-width: 140px;">💎 Sia Chandelier:</span>
          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(244, 63, 94, 0.85); background: rgba(244, 63, 94, 0.25);" onclick="switchOption(this, 'videos/29_Sia_Chandelier_Slowed_Reverb_Lyric_Video.mp4', '💎 <strong>Sia — Chandelier (Slowed + Reverb Brand Edition • Full 4:06)</strong><br>• <strong>1. Slowness</strong>: 0.865x tape varispeed (117 &rarr; 101.2 BPM), stretching out the emotional sorrow.<br>• <strong>2. Cathedral Space</strong>: 3.0s reverberation simulating a vast ballroom echo.<br>• <strong>3. Cassette Warmth</strong>: -2.5 semitones pitch drop, warm 15.5kHz tape shelf.<br>• <strong>Visual</strong>: Live shimmering golden chandelier prism bokeh lights drifting strictly <em>behind</em> glowing pure white lyrics (`bg_35`).')">
            ▶ 1. Full Song: Slowed + Reverb (4:06)
          </button>
          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(255, 255, 255, 0.4); background: rgba(255, 255, 255, 0.08);" onclick="switchOption(this, 'videos/29_Sia_Chandelier_Lyric_Video.mp4', '💿 <strong>Sia — Chandelier (Original 1.0x Mix • Full 3:32)</strong><br>Standard 117 BPM tempo, euphoric electropop beat.<br>• <strong>Visual</strong>: Live shimmering lights and clouds drifting behind lyrics (`bg_35`).')">
            ▶ 2. Full Song: Original Normal (3:32)
          </button>
        </div>"""

if target_showdown in content:
    content = content.replace(target_showdown, new_showdown, 1)
    print("Successfully added Song 29 Showdown buttons.")
else:
    print("Error: target_showdown not found!")
    sys.exit(1)

player_path.write_text(content, encoding='utf-8')
print("player.html updated successfully!")
