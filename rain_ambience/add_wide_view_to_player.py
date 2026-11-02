import os
import re

player_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"

def update_player():
    with open(player_path, "r", encoding="utf-8") as f:
        html = f.read()

    if "real_nature_wide_forest_cabin_night" in html:
        print("Wide view tab already added")
        return

    top_btn = '        <button class="tab-btn active" onclick="openTab(event, \'tab-big-view-cabin-rain\')">🏡 🌧️ BIG VIEW: Wide Nature Cabin in Forest (Night Focus • 100% Monetizable)</button>\n'
    
    html = html.replace('class="tab-btn active"', 'class="tab-btn"')

    if '<div class="tabs-nav">' in html:
        html = html.replace('<div class="tabs-nav">', '<div class="tabs-nav">\n' + top_btn)

    tab_content = '''
    <div id="tab-big-view-cabin-rain" class="tab-content" style="display:block;">
        <div class="video-card">
            <h2>🏡 🌧️ BIG NATURE VIEW: Cozy Forest Cabin in Rain at Night</h2>
            <p class="desc">A wide-angle panoramic landscape view of a cozy cabin nestled in a lush, dense mountain rainforest with heavy rain falling over the canopy and roof. Graded into a soothing midnight blue palette for dark bedrooms, engineered with a 60-second seamless loop (zero seams), and paired with calming binaural rain & thunder audio.</p>
            <div class="video-wrapper">
                <video controls loop autoplay muted preload="auto" poster="thumbnail/wide_cabin_night_thumb_7clouds.jpg">
                    <source src="videos/real_nature_wide_forest_cabin_night_1min_sample.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            
            <h3 style="margin-top:25px; color:#00e5ff;">🎯 Big-View Viral Thumbnails (High CTR Formulas)</h3>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
                <div style="background:#161d27; padding:15px; border-radius:10px; border:1px solid #2a3749;">
                    <h4 style="color:#ffd700; margin-bottom:8px;">191M Formula (7clouds Edo SZ Brush Style)</h4>
                    <img src="thumbnail/wide_cabin_night_thumb_7clouds.jpg" style="width:100%; border-radius:6px;" alt="7clouds Wide Cabin">
                    <p style="font-size:13px; color:#aaa; margin-top:8px;">Font: <strong>Edo SZ</strong> | Fill: White | Shadow: Multi-layer Gaussian blur | Wide Nature Vista</p>
                </div>
                <div style="background:#161d27; padding:15px; border-radius:10px; border:1px solid #2a3749;">
                    <h4 style="color:#00e5ff; margin-bottom:8px;">164M Formula (LatinHype Bebas Neue Style)</h4>
                    <img src="thumbnail/wide_cabin_night_thumb_latinhype.jpg" style="width:100%; border-radius:6px;" alt="LatinHype Wide Cabin">
                    <p style="font-size:13px; color:#aaa; margin-top:8px;">Font: <strong>Bebas Neue</strong> | Fill: White | Shadow: Sharp 3D Solid Cut-Out | High Contrast</p>
                </div>
            </div>

            <div class="specs-grid" style="margin-top:20px;">
                <div class="spec-item"><strong>Camera Angle:</strong> Wide Panoramic Landscape Vista (Cabin & Forest Canopy)</div>
                <div class="spec-item"><strong>Night Grading:</strong> Deep Midnight Blue Tones (Gentle on Eyes for Sleep)</div>
                <div class="spec-item"><strong>Loop Math:</strong> 10s Fwd + 10s Rev x 3 = 60.0s (100% Zero-Seam Continuity)</div>
                <div class="spec-item"><strong>Audio Fidelity:</strong> 48kHz Stereo AAC (Binaural Tin Roof Clatter + Deep Thunder)</div>
            </div>
        </div>
    </div>
'''

    html = re.sub(r'class="tab-content"\s+style="display:block;"', 'class="tab-content" style="display:none;"', html)
    html = html.replace("</body>", tab_content + "\n</body>")

    with open(player_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Added Big View Cabin tab to player.html!")

if __name__ == "__main__":
    update_player()
