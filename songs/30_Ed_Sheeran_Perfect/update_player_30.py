import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html")
content = player_path.read_text(encoding='utf-8')

target = """      <button class="tab-btn" style="border-color: #f59e0b; background: rgba(245, 158, 11, 0.15); box-shadow: 0 0 14px rgba(245, 158, 11, 0.25);" onclick="switchOption(this, 'videos/00_Justin_Bieber_That_Should_Be_Me_20Min_5x_Replay_Lyric_Video.mp4', '🔁 <strong>00. That Should Be Me (20+ Minutes • 5 Times Replay Loop Edition)</strong> — Justin Bieber<br><strong>Aesthetic Formula</strong>: <em>Signature 7clouds Twilight Sky + Seamless 5x Replay Loop</em>.<br>Full 21:38 Master • 6 Iterations (1 Original + 5 Continuous Replays) • Replay Index Hook Cards ([1/5] to [5/5]) • Optimized for High YouTube Watch-Time, Study & Sleep Sessions.')">
        <span style="font-weight:700; color:#fbbf24;">🔁 00. That Should Be Me (20-Min)</span>
        <span style="font-size:11px;opacity:0.9; color:#fde68a;">5x Replay Loop (21:38)</span>
      </button>"""

new_buttons = target + """
      <button class="tab-btn" style="border-color: #f472b6; background: rgba(244, 114, 182, 0.15); box-shadow: 0 0 14px rgba(244, 114, 182, 0.25);" onclick="switchOption(this, 'videos/30_Ed_Sheeran_Perfect_Slowed_Reverb_Pink_Edition_Lyric_Video.mp4', '🌸 <strong>30. Perfect (Pink Mode Edition • Slowed + Reverb)</strong> — Ed Sheeran<br><strong>Artwork</strong>: <em>7clouds Pastel Pink Cotton-Candy Twilight Clouds</em> (bg_30_pink).<br>Full 5:05 Master • 0.865x Tape Varispeed • 3.0s Cathedral Reverb Hall • 15.5kHz Warm Tape Shelf • Patrick Hand 2-Row Couplets • Pure Romantic Pink Aesthetic.')">
        <span style="font-weight:700; color:#f472b6;">🌸 30. Perfect (Pink Mode)</span>
        <span style="font-size:11px;opacity:0.9; color:#fbcfe8;">Slowed + Reverb (5:05)</span>
      </button>
      <button class="tab-btn" style="border-color: #f97316; background: rgba(249, 115, 22, 0.15); box-shadow: 0 0 14px rgba(249, 115, 22, 0.25);" onclick="switchOption(this, 'videos/30_Ed_Sheeran_Perfect_Slowed_Reverb_Sunset_Edition_Lyric_Video.mp4', '🌅 <strong>30. Perfect (Sunset Mode Edition • Slowed + Reverb)</strong> — Ed Sheeran<br><strong>Artwork</strong>: <em>7clouds Warm Golden-Amber & Coral Dusk Clouds</em> (bg_30_sunset).<br>Full 5:05 Master • 0.865x Tape Varispeed • 3.0s Cathedral Reverb Hall • 15.5kHz Warm Tape Shelf • Patrick Hand 2-Row Couplets • Deep Nostalgic Golden Hour.')">
        <span style="font-weight:700; color:#fb923c;">🌅 30. Perfect (Sunset Mode)</span>
        <span style="font-size:11px;opacity:0.9; color:#fed7aa;">Slowed + Reverb (5:05)</span>
      </button>"""

if target in content:
    content = content.replace(target, new_buttons)
    player_path.write_text(content, encoding='utf-8')
    print("SUCCESS: Added Ed Sheeran Perfect Pink & Sunset tabs to player.html!")
else:
    print("ERROR: Target string not found in player.html")
