import os
import re

player_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"

with open(player_path, "r", encoding="utf-8") as f:
    html = f.read()

# Button to add at the very top of tabs
top_btn = '        <button class="tab-btn active" onclick="openTab(event, \'tab-real-nature-70m-sound\')">🌧️ 🌿 REAL NATURE: Tin Roof Rain (Real Live Camera • 70M Channel Sound)</button>\n'

# Deactivate existing active tab buttons
html = html.replace('class="tab-btn active"', 'class="tab-btn"')

# Insert new button right after <div class="tabs-nav">
if '<div class="tabs-nav">' in html:
    html = html.replace('<div class="tabs-nav">', '<div class="tabs-nav">\n' + top_btn)

# Tab content HTML
tab_content = '''
    <div id="tab-real-nature-70m-sound" class="tab-content" style="display:block;">
        <div class="video-card">
            <h2>🌧️ Real Live Camera: Tin Roof Rain with Authentic 70M-View Channel Sound</h2>
            <p class="desc">100% Real live-action camera footage of heavy rain pouring and dripping off corrugated tin roof eaves overlooking a lush green forest with dreamy natural bokeh. Graded with deep cinematic contrast, engineered with a 60-second seamless ping-pong loop (zero jump cut seam), and paired with the <strong>authentic 70M-view Danny Louis rain on stale tin roof & deep thunder channel audio</strong>.</p>
            <div class="video-wrapper">
                <video controls loop autoplay muted preload="auto" poster="thumbnail/real_nature_rain_thumb_7clouds.jpg">
                    <source src="videos/real_nature_tin_roof_rain_70m_channel_sound.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            
            <h3 style="margin-top:25px; color:#00e5ff;">🎯 Viral Thumbnails for Our Real Nature Video (191M & 164M CTR Formulas)</h3>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
                <div style="background:#161d27; padding:15px; border-radius:10px; border:1px solid #2a3749;">
                    <h4 style="color:#ffd700; margin-bottom:8px;">191M Formula (7clouds Edo SZ Brush Style)</h4>
                    <img src="thumbnail/real_nature_rain_thumb_7clouds.jpg" style="width:100%; border-radius:6px;" alt="7clouds style">
                    <p style="font-size:13px; color:#aaa; margin-top:8px;">Font: <strong>Edo SZ</strong> | Fill: Crisp White | Shadow: Multi-layer Gaussian blur | High Contrast</p>
                </div>
                <div style="background:#161d27; padding:15px; border-radius:10px; border:1px solid #2a3749;">
                    <h4 style="color:#00e5ff; margin-bottom:8px;">164M Formula (LatinHype Bebas Neue Style)</h4>
                    <img src="thumbnail/real_nature_rain_thumb_latinhype.jpg" style="width:100%; border-radius:6px;" alt="LatinHype style">
                    <p style="font-size:13px; color:#aaa; margin-top:8px;">Font: <strong>Bebas Neue</strong> | Fill: Crisp White | Shadow: Sharp 3D Solid Cut-Out | Mobile Pop</p>
                </div>
            </div>

            <div class="specs-grid" style="margin-top:20px;">
                <div class="spec-item"><strong>Visuals:</strong> 100% Real Live-Action Camera (Corrugated Tin Roof in Forest Rain)</div>
                <div class="spec-item"><strong>Sound Source:</strong> Authentic 70M-View Danny Louis Tin Roof Rain & Growling Thunder</div>
                <div class="spec-item"><strong>Loop Math:</strong> 15s Fwd + 15s Rev x 2 (Zero Jump Cut Seams)</div>
                <div class="spec-item"><strong>Grading:</strong> Contrast 1.26 • Brightness -0.04 • Saturation 1.22</div>
            </div>
        </div>
    </div>
'''

# Hide all previous tab-contents initially
html = re.sub(r'class="tab-content"\s+style="display:block;"', 'class="tab-content" style="display:none;"', html)

# Insert tab content before </body>
html = html.replace("</body>", tab_content + "\n</body>")

with open(player_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated player.html with Real Nature 70M Channel Sound tab!")
