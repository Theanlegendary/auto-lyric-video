import os
import re

player_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"

def update_player():
    with open(player_path, "r", encoding="utf-8") as f:
        html = f.read()

    if "real_nature_tin_roof_night_1min_sample" in html:
        print("Night tab already added")
        return

    top_btn = '        <button class="tab-btn active" onclick="openTab(event, \'tab-night-edition-rain\')">🌙 🌧️ NIGHT FOCUS: Heavy Rain on Tin Roof at Night (Dark Screen for Sleep)</button>\n'
    
    html = html.replace('class="tab-btn active"', 'class="tab-btn"')

    if '<div class="tabs-nav">' in html:
        html = html.replace('<div class="tabs-nav">', '<div class="tabs-nav">\n' + top_btn)

    tab_content = '''
    <div id="tab-night-edition-rain" class="tab-content" style="display:block;">
        <div class="video-card">
            <h2>🌙 🌧️ NIGHT FOCUS: Heavy Rain on Tin Roof at Night (Dark Screen for Sleep)</h2>
            <p class="desc">Engineered specifically for dark bedrooms and deep insomnia relief. Real live camera footage graded into a deep midnight blue palette with glistening silver raindrops streaming down from the roof eaves. Zero bright daylight glare to protect your melatonin and circadian rhythm.</p>
            <div class="video-wrapper">
                <video controls loop autoplay muted preload="auto" poster="thumbnail/night_rain_thumb_7clouds.jpg">
                    <source src="videos/real_nature_tin_roof_night_1min_sample.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            
            <h3 style="margin-top:25px; color:#00e5ff;">🎯 Night-Optimized Viral Thumbnails (High CTR in YouTube Dark Mode)</h3>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
                <div style="background:#161d27; padding:15px; border-radius:10px; border:1px solid #2a3749;">
                    <h4 style="color:#ffd700; margin-bottom:8px;">191M Formula (7clouds Edo SZ Brush Style)</h4>
                    <img src="thumbnail/night_rain_thumb_7clouds.jpg" style="width:100%; border-radius:6px;" alt="7clouds Night Style">
                    <p style="font-size:13px; color:#aaa; margin-top:8px;">Font: <strong>Edo SZ</strong> | Fill: White | Shadow: Multi-layer Gaussian blur | Midnight Atmosphere</p>
                </div>
                <div style="background:#161d27; padding:15px; border-radius:10px; border:1px solid #2a3749;">
                    <h4 style="color:#00e5ff; margin-bottom:8px;">164M Formula (LatinHype Bebas Neue Style)</h4>
                    <img src="thumbnail/night_rain_thumb_latinhype.jpg" style="width:100%; border-radius:6px;" alt="LatinHype Night Style">
                    <p style="font-size:13px; color:#aaa; margin-top:8px;">Font: <strong>Bebas Neue</strong> | Fill: White | Shadow: Sharp 3D Solid Cut-Out | Dark Mode Pop</p>
                </div>
            </div>

            <div class="specs-grid" style="margin-top:20px;">
                <div class="spec-item"><strong>Visual Atmosphere:</strong> Deep Midnight Blue Moonlit Trees & Silver Raindrops</div>
                <div class="spec-item"><strong>Eye Comfort:</strong> Low Luminance (No Glare, Safe for Bedroom Screens)</div>
                <div class="spec-item"><strong>Loop Precision:</strong> 10s Fwd + 10s Rev x 3 = 60.0s (Zero Seam Ping-Pong)</div>
                <div class="spec-item"><strong>Audio Mastering:</strong> Binaural Tin Roof Clatter + Deep Distant Thunder</div>
            </div>
        </div>
    </div>
'''

    html = re.sub(r'class="tab-content"\s+style="display:block;"', 'class="tab-content" style="display:none;"', html)
    html = html.replace("</body>", tab_content + "\n</body>")

    with open(player_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Added Night Focus tab to player.html!")

if __name__ == "__main__":
    update_player()
