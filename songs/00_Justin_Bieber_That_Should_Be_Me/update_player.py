import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html")
content = player_path.read_text(encoding='utf-8')

target = """      <button class="tab-btn" onclick="switchOption(this, 'videos/29_Sia_Chandelier_Slowed_Reverb_Lyric_Video.mp4', '✨ <strong>29. Chandelier (Slowed + Reverb Brand Edition)</strong> — Sia<br><strong>Artwork</strong>: <em>Radiant Celestial Prism Bokeh & Penthouse Night Sky</em> (bg_35).<br>Full 4:06 Master • 0.865x Tape Varispeed (117 &rarr; 101.2 BPM) • 3.0s Cathedral Reverb Hall • -2.5 Semitones Pitch Drop • 15.5kHz Warm Tape Shelf • Live Shimmering Lights Behind Lyrics.')">
        <span style="font-weight:700; color:#d8b4fe;">29. Chandelier (Slowed)</span>
        <span style="font-size:11px;opacity:0.8; color:#e9d5ff;">Slowed + Reverb (4:06)</span>
      </button>"""

new_buttons = target + """
      <button class="tab-btn" onclick="switchOption(this, 'videos/00_Justin_Bieber_That_Should_Be_Me_Lyric_Video.mp4', '☁️ <strong>00. That Should Be Me (7clouds Aesthetic Master)</strong> — Justin Bieber<br><strong>Artwork</strong>: <em>7clouds Twilight Heartbreak Clouds</em>.<br>Full 3:36 Master • Patrick Hand Handwriting Font • Strictly 2-Row Couplets • Pure White Typography with Deep Charcoal Border • High Contrast & Emotional Sky.')">
        <span style="font-weight:700; color:#38bdf8;">00. That Should Be Me</span>
        <span style="font-size:11px;opacity:0.8; color:#7dd3fc;">Normal 1.0x (3:36)</span>
      </button>
      <button class="tab-btn" style="border-color: #f59e0b; background: rgba(245, 158, 11, 0.15); box-shadow: 0 0 14px rgba(245, 158, 11, 0.25);" onclick="switchOption(this, 'videos/00_Justin_Bieber_That_Should_Be_Me_20Min_5x_Replay_Lyric_Video.mp4', '🔁 <strong>00. That Should Be Me (20+ Minutes • 5 Times Replay Loop Edition)</strong> — Justin Bieber<br><strong>Aesthetic Formula</strong>: <em>Signature 7clouds Twilight Sky + Seamless 5x Replay Loop</em>.<br>Full 21:38 Master • 6 Iterations (1 Original + 5 Continuous Replays) • Replay Index Hook Cards ([1/5] to [5/5]) • Optimized for High YouTube Watch-Time, Study & Sleep Sessions.')">
        <span style="font-weight:700; color:#fbbf24;">🔁 00. That Should Be Me (20-Min)</span>
        <span style="font-size:11px;opacity:0.9; color:#fde68a;">5x Replay Loop (21:38)</span>
      </button>"""

if target in content:
    content = content.replace(target, new_buttons)
    player_path.write_text(content, encoding='utf-8')
    print("SUCCESS: Added That Should Be Me single and 20-min loop buttons to player.html!")
else:
    print("ERROR: Target string not found in player.html")
