import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/player.html")
html = player.read_text(encoding="utf-8")

# Target insertion point right after tab 26
old_tab26 = """      <button class="tab-btn" onclick="switchOption(this, 'videos/26_Tom_Odell_Another_Love_Lyric_Video.mp4', '✨ <strong>26. Another Love</strong> — Tom Odell<br><strong>Artwork</strong>: <em>Makoto Shinkai Clear Pink Aesthetic Sunset & Pine Ridge</em> (bg_32).<br>Direct Lyric Connection (All my tears have been used up) • Until I Found You Clean Style • Patrick Hand Large Typography (102-114pt) • 175pt Title Card • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">26. Another Love</span>
        <span style="font-size:11px;opacity:0.8;">Pink Sunset (Clean Big Text)</span>
      </button>"""

new_tabs = """      <button class="tab-btn" onclick="switchOption(this, 'videos/26_Tom_Odell_Another_Love_Lyric_Video.mp4', '✨ <strong>26. Another Love</strong> — Tom Odell<br><strong>Artwork</strong>: <em>Makoto Shinkai Clear Pink Aesthetic Sunset & Pine Ridge</em> (bg_32).<br>Direct Lyric Connection (All my tears have been used up) • Until I Found You Clean Style • Patrick Hand Large Typography (102-114pt) • 175pt Title Card • 50/50 Balanced Couplets • Dreamy Bokeh (radius 10) • Ken Burns Camera Drift • Zero Collision Holding Sync.')">
        <span style="font-weight:700;">26. Another Love</span>
        <span style="font-size:11px;opacity:0.8;">Pink Sunset (Clean Big Text)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/27_Joji_Glimpse_of_Us_Lyric_Video.mp4', '✨ <strong>27. Glimpse of Us (Normal 1.0x Mix)</strong> — Joji<br><strong>Artwork</strong>: <em>Makoto Shinkai Moody Indigo Twilight Sky & Solitary Rain Ledge</em> (bg_33).<br>Full 3:53 Master • Patrick Hand 200pt Hook Title • Glowing Pure White Typography • Strictly 2-Row Couplets • Seamless Looping Live Cloud Drift.')">
        <span style="font-weight:700;">27. Glimpse of Us</span>
        <span style="font-size:11px;opacity:0.8;">Normal 1.0x (3:53)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/27_Joji_Glimpse_of_Us_Slowed_Reverb_Lyric_Video.mp4', '✨ <strong>27. Glimpse of Us (Slowed + Reverb Brand Edition)</strong> — Joji<br><strong>Artwork</strong>: <em>Makoto Shinkai Moody Indigo Twilight Sky & Solitary Rain Ledge</em> (bg_33).<br>Full 4:30 Master • 0.865x Tape Varispeed (85 &rarr; 73.5 BPM) • 3.0s Cathedral Reverb • 15.5kHz Tape Warmth • Patrick Hand 200pt Hook Title • Strictly 2-Row Couplets.')">
        <span style="font-weight:700; color:#d8b4fe;">27. Glimpse of Us (Slowed)</span>
        <span style="font-size:11px;opacity:0.8; color:#e9d5ff;">Slowed + Reverb (4:30)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/28_yung_kai_blue_Lyric_Video.mp4', '✨ <strong>28. blue (Normal 1.0x Mix)</strong> — yung kai<br><strong>Artwork</strong>: <em>Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook</em> (bg_34).<br>Full 3:34 Master • Patrick Hand 200pt Hook Title • Glowing Pure White Typography • Strictly 2-Row Couplets • Seamless Looping Live Cloud Drift.')">
        <span style="font-weight:700;">28. blue</span>
        <span style="font-size:11px;opacity:0.8;">Normal 1.0x (3:34)</span>
      </button>
      <button class="tab-btn" onclick="switchOption(this, 'videos/28_yung_kai_blue_Slowed_Reverb_Lyric_Video.mp4', '✨ <strong>28. blue (Slowed + Reverb Brand Edition)</strong> — yung kai<br><strong>Artwork</strong>: <em>Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook</em> (bg_34).<br>Full 4:08 Master • 0.865x Tape Varispeed • 3.0s Cathedral Reverb • 15.5kHz Tape Warmth • Patrick Hand 200pt Hook Title • Strictly 2-Row Couplets.')">
        <span style="font-weight:700; color:#d8b4fe;">28. blue (Slowed)</span>
        <span style="font-size:11px;opacity:0.8; color:#e9d5ff;">Slowed + Reverb (4:08)</span>
      </button>"""

if old_tab26 in html:
    html = html.replace(old_tab26, new_tabs)
    player.write_text(html, encoding="utf-8")
    print("player.html tabs updated successfully.")
else:
    print("Warning: old_tab26 not found.")
