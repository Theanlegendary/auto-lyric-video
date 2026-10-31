import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html")
html = player.read_text(encoding="utf-8")

old_skyfall_pair = """        <!-- Skyfall Pair -->
        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: rgba(0, 0, 0, 0.25); padding: 8px 12px; border-radius: 10px;">
          <span style="font-size: 12px; font-weight: 800; color: #f472b6; min-width: 140px;">🌫️ Adele Skyfall:</span>
          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(244, 114, 182, 0.8); background: rgba(244, 114, 182, 0.2);" onclick="switchOption(this, 'videos/compare_skyfall_2_slowed_reverb.mp4', '🔮 <strong>Adele — Skyfall (Slowed + Reverb Brand Edition)</strong><br>• <strong>1. Slowness</strong>: 76 BPM slowed to 65.7 BPM, elongated orchestral sorrow.<br>• <strong>2. Cathedral Space</strong>: 3.0s cavern echo, feelings of doom & isolation.<br>• <strong>3. Lowered Pitch</strong>: -2.5 semitones pitch drop, warm analog cassette tape sound.')">
            ▶ 1. Slowed + Reverb (Brand Mix)
          </button>
          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(255, 255, 255, 0.4); background: rgba(255, 255, 255, 0.08);" onclick="switchOption(this, 'videos/compare_skyfall_1_original.mp4', '💿 <strong>Adele — Skyfall (Original 1.0x Studio Mix)</strong><br>Standard speed (76 BPM), original pitch, dry studio acoustics.')">
            ▶ 2. Original Speed (1.0x)
          </button>
        </div>"""

new_pairs = """        <!-- Joji Glimpse of Us Pair -->
        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: rgba(0, 0, 0, 0.25); padding: 8px 12px; border-radius: 10px;">
          <span style="font-size: 12px; font-weight: 800; color: #818cf8; min-width: 140px;">🌧️ Joji Glimpse of Us:</span>
          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(129, 140, 248, 0.85); background: rgba(129, 140, 248, 0.25);" onclick="switchOption(this, 'videos/27_Joji_Glimpse_of_Us_Slowed_Reverb_Lyric_Video.mp4', '🌧️ <strong>Joji — Glimpse of Us (Slowed + Reverb Brand Edition • Full 4:30)</strong><br>• <strong>1. Slowness</strong>: 85 BPM slowed to 73.5 BPM (0.865x).<br>• <strong>2. Cathedral Space</strong>: 3.0s reverberation tail simulating lonely rain-slicked city ledges.<br>• <strong>3. Cassette Tape Comfort</strong>: -2.5 semitones pitch drop, warm 15.5kHz tape shelf.<br>• <strong>Visual</strong>: Makoto Shinkai Moody Indigo Twilight Sky & Solitary Rain Ledge (`bg_33`).')">
            ▶ 1. Full Song: Slowed + Reverb (4:30)
          </button>
          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(255, 255, 255, 0.4); background: rgba(255, 255, 255, 0.08);" onclick="switchOption(this, 'videos/27_Joji_Glimpse_of_Us_Lyric_Video.mp4', '💿 <strong>Joji — Glimpse of Us (Original 1.0x Mix • Full 3:53)</strong><br>Standard speed (85 BPM), original pitch, dry studio acoustics.<br>• <strong>Visual</strong>: Makoto Shinkai Moody Indigo Twilight Sky & Solitary Rain Ledge (`bg_33`).')">
            ▶ 2. Full Song: Original Normal (3:53)
          </button>
        </div>

        <!-- yung kai blue Pair -->
        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: rgba(0, 0, 0, 0.25); padding: 8px 12px; border-radius: 10px;">
          <span style="font-size: 12px; font-weight: 800; color: #38bdf8; min-width: 140px;">🌊 yung kai blue:</span>
          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(56, 189, 248, 0.85); background: rgba(56, 189, 248, 0.25);" onclick="switchOption(this, 'videos/28_yung_kai_blue_Slowed_Reverb_Lyric_Video.mp4', '🌊 <strong>yung kai — blue (Slowed + Reverb Brand Edition • Full 4:08)</strong><br>• <strong>1. Slowness</strong>: 0.865x tape varispeed slowdown, stretching romantic longing.<br>• <strong>2. Cathedral Space</strong>: 3.0s acoustic diffusion simulating dawn ocean cliffs.<br>• <strong>3. Cassette Tape Comfort</strong>: -2.5 semitones pitch drop, warm 15.5kHz tape shelf.<br>• <strong>Visual</strong>: Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook (`bg_34`).')">
            ▶ 1. Full Song: Slowed + Reverb (4:08)
          </button>
          <button class="tab-btn" style="width: auto; padding: 8px 16px; margin: 0; border-color: rgba(255, 255, 255, 0.4); background: rgba(255, 255, 255, 0.08);" onclick="switchOption(this, 'videos/28_yung_kai_blue_Lyric_Video.mp4', '💿 <strong>yung kai — blue (Original 1.0x Mix • Full 3:34)</strong><br>Standard speed, original acoustic guitar mix.<br>• <strong>Visual</strong>: Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook (`bg_34`).')">
            ▶ 2. Full Song: Original Normal (3:34)
          </button>
        </div>"""

if old_skyfall_pair in html:
    html = html.replace(old_skyfall_pair, new_pairs)
    print("Replaced Skyfall demo with Joji and yung kai pairs.")

html = html.replace("Full Discography Catalog (Songs 1–26):", "Full Discography Catalog (Songs 1–28):")
player.write_text(html, encoding="utf-8")
print("player.html saved with updated showdown banner and count.")
