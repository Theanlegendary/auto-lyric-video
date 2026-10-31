import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html")
html = player_path.read_text(encoding="utf-8")

# 1. Update the Sweater Weather Pair buttons in the showdown banner
old_sweater_block = """        <!-- Sweater Weather Pair -->
        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: rgba(0, 0, 0, 0.25); padding: 8px 12px; border-radius: 10px;">
          <span style="font-size: 12px; font-weight: 800; color: #aadcff; min-width: 140px;">🧥 Sweater Weather:</span>
          <button class="tab-btn active" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(180, 120, 255, 0.85); background: rgba(180, 120, 255, 0.25);" onclick="switchOption(this, 'videos/compare_sweater_2_slowed_reverb.mp4', '🧥 <strong>The Neighbourhood — Sweater Weather (Slowed + Reverb Brand Edition)</strong><br>• <strong>1. Slowness</strong>: 118 BPM slowed to 102 BPM (0.865x), stretching the vocal longing.<br>• <strong>2. Cathedral Space</strong>: 3.0s reverberation tail simulating cold, empty coastal bluffs.<br>• <strong>3. Lowered Pitch</strong>: -2.5 semitones down, warm cassette tape lowpass (15.5kHz), inducing dreamlike dissociation.')">
            ▶ 1. Slowed + Reverb (Brand Mix)
          </button>
          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(255, 255, 255, 0.4); background: rgba(255, 255, 255, 0.08);" onclick="switchOption(this, 'videos/compare_sweater_1_original.mp4', '💿 <strong>The Neighbourhood — Sweater Weather (Original 1.0x Mix)</strong><br>Standard speed (118 BPM), original pitch, dry studio audio.')">
            ▶ 2. Original Speed (1.0x)
          </button>
        </div>"""

new_sweater_block = """        <!-- Sweater Weather Pair (Full Song Editions) -->
        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: rgba(0, 0, 0, 0.25); padding: 8px 12px; border-radius: 10px;">
          <span style="font-size: 12px; font-weight: 800; color: #aadcff; min-width: 140px;">🧥 Sweater Weather:</span>
          <button class="tab-btn active" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(180, 120, 255, 0.85); background: rgba(180, 120, 255, 0.25);" onclick="switchOption(this, 'videos/25_The_Neighbourhood_Sweater_Weather_Slowed_Reverb_Lyric_Video.mp4', '🧥 <strong>The Neighbourhood — Sweater Weather (Slowed + Reverb Brand Edition • Full 4:35)</strong><br>• <strong>1. Slowness</strong>: 118 BPM slowed to 102 BPM (0.865x), stretching the vocal longing.<br>• <strong>2. Cathedral Space</strong>: 3.0s reverberation tail simulating cold, empty coastal bluffs.<br>• <strong>3. Lowered Pitch & Tape Comfort</strong>: -2.5 semitones down, warm cassette tape shelf (15.5kHz), inducing dreamlike dissociation.<br>• <strong>Visual</strong>: Living Color Clouds & Minimal Horizon, looping cloud drift, Patrick Hand 200pt title, glowing pure white text.')">
            ▶ 1. Full Song: Slowed + Reverb (4:35)
          </button>
          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(255, 255, 255, 0.4); background: rgba(255, 255, 255, 0.08);" onclick="switchOption(this, 'videos/25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4', '💿 <strong>The Neighbourhood — Sweater Weather (Original 1.0x Normal Mix • Full 3:57)</strong><br>Standard speed (118 BPM), original pitch, dry studio audio.<br>• <strong>Visual</strong>: Living Color Clouds & Minimal Horizon, looping cloud drift, Patrick Hand 200pt title, glowing pure white text.')">
            ▶ 2. Full Song: Original Normal (3:57)
          </button>
        </div>"""

if old_sweater_block in html:
    html = html.replace(old_sweater_block, new_sweater_block)
    print("Showdown banner updated successfully.")
else:
    print("Warning: old_sweater_block not found exactly in html!")

# 2. Update Tab 25 in the discography catalog
old_tab25 = """      <button class="tab-btn" onclick="switchOption(this, 'videos/25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4', '✨ <strong>25. Sweater Weather (Living Color Clouds Edition)</strong> — The Neighbourhood<br><strong>Artwork</strong>: <em>Makoto Shinkai Living Sapphire & Violet Color Cloud Sky with Minimal Dark Pine Horizon</em> (88% Clean Reading Area).<br>User Selected Definitive Style • Seamless Real-Time Live Drifting Clouds • Patrick Hand 200pt Commanding Hook Title • Pure White Starlight Glow (&H00FFFFFF + \\blur2.0) • Generous 180px+ Side Margins • Strictly 2-Row Max Couplets • Studio Zero-Lag Timing.')">
        <span style="font-weight:700;">25. Sweater Weather</span>
        <span style="font-size:11px;opacity:0.8;">Living Color Clouds (200pt)</span>
      </button>"""

new_tab25 = """      <button class="tab-btn" onclick="switchOption(this, 'videos/25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4', '✨ <strong>25. Sweater Weather (Normal 1.0x Mix)</strong> — The Neighbourhood<br><strong>Artwork</strong>: <em>Makoto Shinkai Living Sapphire & Violet Color Cloud Sky with Minimal Dark Pine Horizon</em> (88% Clean Reading Area).<br>Full 3:57 Original Studio Mix • Seamless Looping Live Cloud Drift • Patrick Hand 200pt Hook Title • Pure White Starlight Glow (&H00FFFFFF + \\blur2.0) • Strictly 2-Row Couplets.')">
        <span style="font-weight:700;">25. Sweater Weather</span>
        <span style="font-size:11px;opacity:0.8;">Normal 1.0x (3:57)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/25_The_Neighbourhood_Sweater_Weather_Slowed_Reverb_Lyric_Video.mp4', '✨ <strong>25. Sweater Weather (Slowed + Reverb Brand Edition)</strong> — The Neighbourhood<br><strong>Artwork</strong>: <em>Makoto Shinkai Living Sapphire & Violet Color Cloud Sky with Minimal Dark Pine Horizon</em>.<br>Full 4:35 Master • 0.865x Tape Varispeed (118 &rarr; 102 BPM) • 3.0s Cathedral Reverb • 15.5kHz Analog Tape Warmth • Seamless Looping Cloud Drift • Patrick Hand 200pt Hook Title • Glowing Pure White Typography • Strictly 2-Row Couplets.')">
        <span style="font-weight:700; color:#d8b4fe;">25. Sweater Weather (Slowed)</span>
        <span style="font-size:11px;opacity:0.8; color:#e9d5ff;">Slowed + Reverb (4:35)</span>
      </button>"""

if old_tab25 in html:
    html = html.replace(old_tab25, new_tab25)
    print("Discography tabs updated successfully.")
else:
    print("Warning: old_tab25 not found exactly in html!")

player_path.write_text(html, encoding="utf-8")
print("player.html saved.")
