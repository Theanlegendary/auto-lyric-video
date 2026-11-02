import cv2
import os
import re

video_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos\our_tin_roof_rain_seamless_loop.mp4"
brain_dir = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
player_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"

# 1. Audit Video Frames
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
dur = total_frames / fps
print(f"Our Rain Video Stats: {dur:.2f}s, {total_frames} frames, {fps} fps")

checkpoints = [
    (15.0, "audit_our_rain_forward_15s.png"),
    (30.0, "audit_our_rain_pivot_30s.png"),
    (45.0, "audit_our_rain_reverse_45s.png"),
    (59.8, "audit_our_rain_end_seam_59s.png")
]

for sec, fname in checkpoints:
    frame_idx = min(int(sec * fps), int(total_frames - 1))
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ret, frame = cap.read()
    if ret:
        out_p = os.path.join(brain_dir, fname)
        # 960x540 for web view
        small = cv2.resize(frame, (960, 540))
        cv2.imwrite(out_p, small)
        print(f"Extracted {fname} at frame {frame_idx}")

cap.release()

# 2. Update player.html with dedicated premier tab
with open(player_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add button
new_btn = '        <button class="tab-btn active" onclick="openTab(event, \'tab-our-rain-tin-roof\')">🌧️ 🏠 OUR RAIN: Tin Roof in Murky Forest (Danny Louis Formula • Seamless Ping-Pong)</button>\n'

# Make sure other tabs are not active by default if we want this as premier, or add as a top tab
# Remove active from other buttons if present
html = html.replace('class="tab-btn active"', 'class="tab-btn"')

# Insert new button at top of tab buttons
btn_marker = '<div class="tabs-nav">'
if btn_marker in html:
    html = html.replace(btn_marker, btn_marker + "\n" + new_btn)

# Add Tab Content
tab_content = '''
    <div id="tab-our-rain-tin-roof" class="tab-content" style="display:block;">
        <div class="video-card">
            <h2>🌧️ OUR RAIN: Heavy Rain on Stale Tin Roof in Murky Forest (Danny Louis 70M Formula)</h2>
            <p class="desc">1080p Real live-action footage of rain pouring and spraying on corrugated tin roof in a foggy forest. Engineered with a 30s forward + 30s reverse ping-pong loop (100% zero jump cut seam), boosted contrast (1.28x) with rich murky forest blacks, and paired with seamless 60-second binaural tin roof rain & rolling thunder loop.</p>
            <div class="video-wrapper">
                <video controls loop autoplay muted preload="auto" poster="thumbnail/our_rain_thumbnail_7clouds_style.png">
                    <source src="videos/our_tin_roof_rain_seamless_loop.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            
            <h3 style="margin-top:25px; color:#00e5ff;">🎯 Viral Thumbnails for Our Rain Video (191M & 164M CTR Formulas)</h3>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
                <div style="background:#161d27; padding:15px; border-radius:10px; border:1px solid #2a3749;">
                    <h4 style="color:#ffd700; margin-bottom:8px;">191M Formula (7clouds Brush Stencil Style)</h4>
                    <img src="thumbnail/our_rain_thumbnail_7clouds_style.png" style="width:100%; border-radius:6px;" alt="7clouds style">
                    <p style="font-size:13px; color:#aaa; margin-top:8px;">Font: <strong>Edo SZ</strong> | Fill: White | Shadow: Multi-layer Gaussian blur | Center aligned</p>
                </div>
                <div style="background:#161d27; padding:15px; border-radius:10px; border:1px solid #2a3749;">
                    <h4 style="color:#00e5ff; margin-bottom:8px;">164M Formula (LatinHype Tall Bold Sans Style)</h4>
                    <img src="thumbnail/our_rain_thumbnail_latinhype_style.png" style="width:100%; border-radius:6px;" alt="LatinHype style">
                    <p style="font-size:13px; color:#aaa; margin-top:8px;">Font: <strong>Bebas Neue</strong> | Fill: White | Shadow: Sharp 3D solid cut-out | Upper-center aligned</p>
                </div>
            </div>

            <div class="specs-grid" style="margin-top:20px;">
                <div class="spec-item"><strong>Visual Source:</strong> Real Corrugated Tin Roof Overhang in Murky Rainforest</div>
                <div class="spec-item"><strong>Loop Precision:</strong> 30.0s Fwd + 30.0s Rev (Zero Seam Artifacts)</div>
                <div class="spec-item"><strong>Grading:</strong> Contrast 1.28 • Brightness -0.03 • Saturation 1.22</div>
                <div class="spec-item"><strong>Audio Mastering:</strong> Binaural Tin Roof Clatter + Sub-80Hz Rolling Thunder</div>
            </div>
        </div>
    </div>
'''

# Hide all other tab-contents initially so this one shows
html = re.sub(r'class="tab-content"\s+style="display:block;"', 'class="tab-content" style="display:none;"', html)

# Insert tab content before </body>
html = html.replace("</body>", tab_content + "\n</body>")

with open(player_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated player.html with Our Rain feature tab!")
