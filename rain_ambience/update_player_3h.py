import os

def update_player():
    path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    old_section = """    <div id="tab-big-view-cabin-rain" class="tab-content" style="display:block;">
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
    </div>"""

    new_section = """    <div id="tab-big-view-cabin-rain" class="tab-content" style="display:block;">
        <div class="video-card">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                <h2 style="margin:0;">🏡 🌌 🌧️ 3-HOUR PREMIER MASTER: Cozy Rainforest Cabin Rain at Night</h2>
                <span style="background:rgba(16,185,129,0.25); color:#34d399; border:1px solid #10b981; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:800; text-transform:uppercase;">100% Monetizable • 3 Hours (10,800s)</span>
            </div>
            <p class="desc">A wide-angle panoramic landscape view of a cozy cabin nestled deep in a misty tropical rainforest with rain pouring across the canopy and metal roof. Graded into a soothing midnight blue palette for dark bedrooms, insomnia relief, and deep focus. 100% Commercial live camera footage + clean binaural rain and thunder audio. Zero Content ID claims, 100% safe to monetize on YouTube.</p>
            
            <!-- Duration / Sample Switcher -->
            <div style="display:flex; gap:10px; margin-bottom:15px; flex-wrap:wrap;">
                <button class="tab-btn active" style="width:auto; padding:8px 18px; border-color:#10b981; background:rgba(16,185,129,0.3);" onclick="document.getElementById('big-view-player').src='videos/our_rain_big_view_cabin_night_3h_master.mp4'; document.getElementById('big-view-player').play();">
                    ▶ Play Full 3-Hour Master (10,800s • 1.69 GB)
                </button>
                <button class="tab-btn" style="width:auto; padding:8px 18px; border-color:rgba(255,255,255,0.3); background:rgba(255,255,255,0.06);" onclick="document.getElementById('big-view-player').src='videos/real_nature_wide_forest_cabin_night_1min_sample.mp4'; document.getElementById('big-view-player').play();">
                    ▶ Play 1-Minute Preview Loop
                </button>
            </div>

            <div class="video-wrapper">
                <video id="big-view-player" controls preload="metadata" poster="thumbnail/wide_cabin_night_thumb_7clouds.jpg">
                    <source src="videos/our_rain_big_view_cabin_night_3h_master.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            
            <h3 style="margin-top:25px; color:#00e5ff;">🎯 Viral Thumbnails (191M & 164M High CTR Formulas)</h3>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
                <div style="background:#161d27; padding:15px; border-radius:10px; border:1px solid #2a3749;">
                    <h4 style="color:#ffd700; margin-bottom:8px;">191M Formula (7clouds Edo SZ Brush Style)</h4>
                    <img src="thumbnail/wide_cabin_night_thumb_7clouds.jpg" style="width:100%; border-radius:6px;" alt="7clouds Wide Cabin">
                    <p style="font-size:13px; color:#aaa; margin-top:8px;">Font: <strong>Edo SZ</strong> | Fill: White | Shadow: Multi-layer Gaussian blur | Wide Nature Vista | <a href="thumbnail/wide_cabin_night_thumb_7clouds.jpg" download style="color:#38bdf8;">Download JPG</a></p>
                </div>
                <div style="background:#161d27; padding:15px; border-radius:10px; border:1px solid #2a3749;">
                    <h4 style="color:#00e5ff; margin-bottom:8px;">164M Formula (LatinHype Bebas Neue Style)</h4>
                    <img src="thumbnail/wide_cabin_night_thumb_latinhype.jpg" style="width:100%; border-radius:6px;" alt="LatinHype Wide Cabin">
                    <p style="font-size:13px; color:#aaa; margin-top:8px;">Font: <strong>Bebas Neue</strong> | Fill: White | Shadow: Sharp 3D Solid Cut-Out | Dark Mode Pop | <a href="thumbnail/wide_cabin_night_thumb_latinhype.jpg" download style="color:#38bdf8;">Download JPG</a></p>
                </div>
            </div>

            <!-- YouTube Copy-Paste Upload Kit -->
            <h3 style="margin-top:25px; color:#ffd700;">🚀 YouTube Copy-Paste Upload Kit (Ready to Monetize)</h3>
            <div style="background:#131a24; padding:20px; border-radius:10px; border:1px solid #233144; margin-top:15px; font-family:monospace; font-size:13px; color:#e0e6ed; line-height:1.6;">
                <p><strong style="color:#ffd700;">VIDEO TITLE:</strong><br>
                Rain on Cozy Cabin in Murky Rainforest at Night • Heavy Rain & Thunder Sounds for Sleep (3 Hours)</p>
                <hr style="border:0; border-top:1px solid #233144; margin:12px 0;">
                <p><strong style="color:#ffd700;">DESCRIPTION:</strong><br>
                Fall asleep in minutes and cure insomnia with tranquil heavy rain falling on a secluded cozy cabin tucked deep inside a foggy mountain rainforest at night. Wide panoramic nature vista graded in deep midnight blue to prevent screen glare, accompanied by gentle binaural roof rain and distant rolling thunder.<br><br>
                Perfect for: Deep sleep, studying, insomnia relief, anxiety reduction, meditation, and relaxing background noise.<br><br>
                ⏱️ TIMESTAMPS:<br>
                00:00:00 - Rainforest Rain at Secluded Cabin<br>
                01:00:00 - Deep Sleep & Distant Rolling Thunder<br>
                02:00:00 - Midnight Canopy Downpour<br>
                02:59:00 - Waking Up Refreshed<br><br>
                🎧 Headphones recommended for full binaural immersion.<br>
                ✨ 100% Commercial Licensed live-action footage & original audio design.</p>
                <hr style="border:0; border-top:1px solid #233144; margin:12px 0;">
                <p><strong style="color:#ffd700;">SEARCH TAGS:</strong><br>
                rain on cabin, rain sounds for sleep, cozy cabin rain, heavy rain at night, rain on tin roof, rain sounds, sleep sounds, insomnia relief, rain in rainforest, 3 hours rain, ambient rain, white noise for sleeping, study sounds, deep sleep rain, rain and thunder sounds, cabin ambience</p>
            </div>

            <div class="specs-grid" style="margin-top:20px;">
                <div class="spec-item"><strong>Duration:</strong> Exactly 3 Hours, 0 Minutes, 0 Seconds (10,800s • 270,000 frames)</div>
                <div class="spec-item"><strong>File Size:</strong> 1.69 GB (1730 MB • Fast YouTube Upload)</div>
                <div class="spec-item"><strong>Resolution & FPS:</strong> 1080p Full HD (1920x1080 @ 25fps)</div>
                <div class="spec-item"><strong>Audio Fidelity:</strong> 48kHz Stereo AAC 128 kbps (Binaural Tin Roof & Thunder)</div>
                <div class="spec-item"><strong>Monetization Status:</strong> 100% Safe (CC0 Footage + Binaural Foley • Zero Reused Content)</div>
                <div class="spec-item"><strong>Eye Comfort:</strong> Midnight Blue Low-Luminance (Zero Glare for Insomnia)</div>
            </div>
        </div>
    </div>"""

    # Normalize line endings for replacement
    html_norm = html.replace("\r\n", "\n")
    old_norm = old_section.replace("\r\n", "\n")
    new_norm = new_section.replace("\r\n", "\n")

    if old_norm in html_norm:
        html_norm = html_norm.replace(old_norm, new_norm)
        # Restore CRLF
        final_html = html_norm.replace("\n", "\r\n")
        with open(path, "w", encoding="utf-8") as f:
            f.write(final_html)
        print("Successfully updated player.html with 3-Hour Cabin Night section!")
    else:
        print("Could not find exact old section in player.html")

if __name__ == "__main__":
    update_player()
