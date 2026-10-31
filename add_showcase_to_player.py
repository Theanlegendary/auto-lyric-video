import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

showcase_html = """    <!-- 5 SPOTIFY STYLE CHOICES (1-MIN COMPARISONS) -->
    <div style="background: linear-gradient(135deg, rgba(29, 185, 84, 0.15), rgba(15, 10, 25, 0.8)); border: 1px solid rgba(29, 185, 84, 0.4); border-radius: 16px; padding: 20px; margin-bottom: 25px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 12px; flex-wrap:wrap; gap:8px;">
        <span style="background:#1db954; color:#000; font-weight:800; font-size:12px; padding:5px 12px; border-radius:12px; text-transform:uppercase; letter-spacing:0.5px;">Spotify Style Showdown • 1-Min Comparisons</span>
        <span style="font-size:13px; color:#1db954; font-weight:600;">Choose Your Favorite 1-Minute Spotify Look</span>
      </div>
      <div class="tabs" style="grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); margin-bottom: 0;">
        <button class="tab-btn active" style="border-color: rgba(29, 185, 84, 0.6);" onclick="switchOption(this, 'videos/choice1_spotify_max_pro.mp4', '🟢 <strong>Option 1: Spotify Max Pro</strong><br><strong>Typography</strong>: Poppins Bold 96-106pt (Pure White, Crisp Dark Outline, 175pt Title).<br>Major-label standard, maximum readability, zero clutter on Makoto Shinkai Coastal Twilight.')">
          <span style="font-weight:700;">1. Spotify Max Pro</span>
          <span style="font-size:11px;opacity:0.8;">Poppins Bold 96pt (Clean White)</span>
        </button>
        <button class="tab-btn" style="border-color: rgba(255, 165, 0, 0.6);" onclick="switchOption(this, 'videos/choice2_spotify_amber_glow.mp4', '🟠 <strong>Option 2: Spotify Amber Glow</strong><br><strong>Typography</strong>: Poppins Bold 96-106pt with warm amber halo outline & shadow.<br>Cozy, sunset-lit ember aesthetic on Cosmic Midnight Ridge.')">
          <span style="font-weight:700;">2. Spotify Amber Glow</span>
          <span style="font-size:11px;opacity:0.8;">Poppins Bold (Warm Ember Halo)</span>
        </button>
        <button class="tab-btn" style="border-color: rgba(120, 220, 255, 0.6);" onclick="switchOption(this, 'videos/choice3_spotify_modern_floating.mp4', '🔵 <strong>Option 3: Spotify Modern Floating</strong><br><strong>Typography</strong>: Inter Bold 94-104pt with wide character tracking (\\\\fsp2).<br>Airy, ultra-sleek, Apple Music / Spotify Canvas hybrid aesthetic on Aurora Lake.')">
          <span style="font-weight:700;">3. Modern Floating</span>
          <span style="font-size:11px;opacity:0.8;">Inter Bold 94pt (Wide Spacing)</span>
        </button>
        <button class="tab-btn" style="border-color: rgba(255, 120, 200, 0.6);" onclick="switchOption(this, 'videos/choice4_spotify_handwritten_hybrid.mp4', '🟣 <strong>Option 4: Spotify Handwritten Hybrid</strong><br><strong>Typography</strong>: Patrick Hand 104-116pt (from Until I Found You) in pure white on dark night sky.<br>Intimate, handwritten diary aesthetic on Celestial Starlit Beach.')">
          <span style="font-weight:700;">4. Handwritten Hybrid</span>
          <span style="font-size:11px;opacity:0.8;">Patrick Hand 106pt (Pure White)</span>
        </button>
        <button class="tab-btn" style="border-color: rgba(200, 100, 255, 0.6);" onclick="switchOption(this, 'videos/choice5_spotify_cinematic_rounded.mp4', '🟣 <strong>Option 5: Spotify Cinematic Rounded</strong><br><strong>Typography</strong>: Fredoka Rounded Bold 95-106pt with deep shadow.<br>Punchy, friendly geometric sans on Twilight Dreamscape Crescent Moon.')">
          <span style="font-weight:700;">5. Cinematic Rounded</span>
          <span style="font-size:11px;opacity:0.8;">Fredoka Bold 95pt (Deep Shadow)</span>
        </button>
      </div>
    </div>

    <div style="font-size:14px; font-weight:700; color:var(--text-muted); margin-bottom:10px; text-transform:uppercase; letter-spacing:0.8px;">Full Discography Catalog (Songs 1–26):</div>
"""

target = '<p class="subtitle">Every single song receives its own unique 1080p anime artwork, 2-row couplets, dynamic intro blur timing, and subtle 35mm lofi grain.</p>\n\n    <div class="tabs">'
replacement = '<p class="subtitle">Every single song receives its own unique 1080p anime artwork, 2-row couplets, dynamic intro blur timing, and subtle 35mm lofi grain.</p>\n\n' + showcase_html + '    <div class="tabs">'

if target in content:
    content = content.replace(target, replacement, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Spotify Showdown section to player.html successfully!")
else:
    print("Target not found in player.html")
