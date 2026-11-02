import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html")
content = player_path.read_text(encoding='utf-8')

target = """      <button class="tab-btn" style="border-color: #0284c7; background: rgba(2, 132, 199, 0.18); box-shadow: 0 0 16px rgba(2, 132, 199, 0.35);" onclick="switchOption(this, 'videos/28_yung_kai_blue_80Sky_20Sea_BlueFilter_Lyric_Video.mp4', '🌊 <strong>28. blue (80% Sky • 20% Sea • Blue Filter Vibe Edition)</strong> — yung kai<br><strong>Artwork</strong>: <em>Exact 80% Open Cyan Sky & 20% Low Horizon Turquoise Ocean Waves</em> with Dreamy Cool Blue Aesthetic Filter.<br>Full 3:34 Master • Authentic 7clouds Edo SZ Formula • Sentence Case • Lower-Third Clearance • Soft Black Outer Glow & Shadow • Zero-Frame Cuts • Rest-Cut Instrumental Breathing Room.')">
        <span style="font-weight:700; color:#38bdf8;">🌊 28. blue (80% Sky / 20% Sea)</span>
        <span style="font-size:11px;opacity:0.9; color:#bae6fd;">Blue Filter Vibe (3:34)</span>
      </button>"""

new_tabs = target + """
      <button class="tab-btn" style="border-color: #06b6d4; background: rgba(6, 182, 212, 0.18); box-shadow: 0 0 16px rgba(6, 182, 212, 0.35);" onclick="switchOption(this, 'videos/30_Ed_Sheeran_Perfect_80Sky_20Sea_BlueFilter_Lyric_Video.mp4', '🌊 <strong>30. Perfect (80% Sky • 20% Sea • Authentic 7clouds Edo SZ Edition)</strong> — Ed Sheeran<br><strong>Artwork & Typography</strong>: <em>Exact 80% Vast Azure Sky & 20% Low Horizon Turquoise Ocean Waves</em> with Dreamy Cool Blue Aesthetic Filter & Authentic 7clouds Edo SZ Brush Script.<br>Full 5:05 Master • Slowed + Reverb (0.865x) • 3.0s Cathedral Hall • Sentence Case • Lower-Third Clearance (78% Down) • Soft Black Glow & Shadow • Zero-Frame Cuts • Rest-Cut Instrumental Pauses.')">
        <span style="font-weight:700; color:#22d3ee;">🌊 30. Perfect (80% Sky / 20% Sea)</span>
        <span style="font-size:11px;opacity:0.9; color:#a5f3fc;">Edo SZ • Slowed (5:05)</span>
      </button>
      <button class="tab-btn" style="border-color: #ec4899; background: rgba(236, 72, 153, 0.18); box-shadow: 0 0 16px rgba(236, 72, 153, 0.35);" onclick="switchOption(this, 'videos/30_Ed_Sheeran_Perfect_Slowed_Reverb_Pink_Edition_Lyric_Video.mp4', '🌸 <strong>30. Perfect (Pink Cotton-Candy Clouds • Authentic 7clouds Edo SZ Edition)</strong> — Ed Sheeran<br><strong>Artwork & Typography</strong>: <em>7clouds Pastel Pink Cotton-Candy Twilight Clouds</em> with Authentic Edo SZ Brush Script in Sentence Case.<br>Full 5:05 Master • Slowed + Reverb (0.865x) • Lower-Third 78% Down • Soft Black Glow & Shadow • Zero-Frame Cuts • Rest-Cut Breathing Room.')">
        <span style="font-weight:700; color:#f472b6;">🌸 30. Perfect (Pink Mode)</span>
        <span style="font-size:11px;opacity:0.9; color:#fbcfe8;">Edo SZ • Slowed (5:05)</span>
      </button>
      <button class="tab-btn" style="border-color: #f97316; background: rgba(249, 115, 22, 0.18); box-shadow: 0 0 16px rgba(249, 115, 22, 0.35);" onclick="switchOption(this, 'videos/30_Ed_Sheeran_Perfect_Slowed_Reverb_Sunset_Edition_Lyric_Video.mp4', '🌅 <strong>30. Perfect (Sunset Amber Dusk • Authentic 7clouds Edo SZ Edition)</strong> — Ed Sheeran<br><strong>Artwork & Typography</strong>: <em>7clouds Warm Golden-Amber Dusk Clouds</em> with Authentic Edo SZ Brush Script in Sentence Case.<br>Full 5:05 Master • Slowed + Reverb (0.865x) • Lower-Third 78% Down • Soft Black Glow & Shadow • Zero-Frame Cuts • Rest-Cut Breathing Room.')">
        <span style="font-weight:700; color:#fb923c;">🌅 30. Perfect (Sunset Mode)</span>
        <span style="font-size:11px;opacity:0.9; color:#fed7aa;">Edo SZ • Slowed (5:05)</span>
      </button>"""

if target in content:
    content = content.replace(target, new_tabs)
    player_path.write_text(content, encoding='utf-8')
    print("SUCCESS: Successfully added 3 Edo SZ 7clouds tabs for Ed Sheeran - Perfect to player.html!")
else:
    print("ERROR: Target tab button not found in player.html")
