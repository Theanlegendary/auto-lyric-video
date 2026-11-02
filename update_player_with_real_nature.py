import re

player_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"

with open(player_path, "r", encoding="utf-8") as f:
    content = f.read()

# Check if tab already exists
if "real_nature_tin_roof_rain" in content:
    print("Already in player.html")
else:
    # Add tab button and tab content
    # Look for last tab button
    button_html = '''        <button class="tab-btn" onclick="openTab(event, 'tab-real-nature-rain')">🌧️ 🌿 Real Nature: Tin Roof Rain (Ping-Pong Loop • High Contrast)</button>\n'''
    
    # We find where tab-buttons end (before </header> or <div class="tab-content" or similar)
    match_btn = re.search(r'(<button class="tab-btn"[^>]*>.*?</button>\s*)+', content)
    if match_btn:
        pos = match_btn.end()
        content = content[:pos] + button_html + content[pos:]
    
    # Tab content
    tab_pane_html = '''
    <div id="tab-real-nature-rain" class="tab-content">
        <div class="video-card">
            <h2>🌧️ Real Live-Action Tin Roof Rain with Distant Thunder (Danny Louis 70M Formula)</h2>
            <p class="desc">1080p Real live-action camera footage with forward + reverse ping-pong loop (100% zero jump-cut seam), cinematic contrast boost (eq=contrast=1.22), deep rainforest blacks, and 60-second seamless binaural tin roof rain & rolling thunder loop.</p>
            <div class="video-wrapper">
                <video controls loop preload="metadata">
                    <source src="videos/real_nature_tin_roof_rain_seamless_loop.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            <div class="specs-grid">
                <div class="spec-item"><strong>Footage:</strong> Real Nature (Pexels 1080p live-action)</div>
                <div class="spec-item"><strong>Loop Technique:</strong> 30s Forward + 30s Reverse Ping-Pong (Zero Seam)</div>
                <div class="spec-item"><strong>Grading:</strong> Contrast 1.22, Brightness -0.04, Saturation 1.18</div>
                <div class="spec-item"><strong>Audio:</strong> Binaural Tin Roof Clatter + Sub-80Hz Thunder</div>
            </div>
        </div>
    </div>
'''
    # Append before </body> or inside container
    if "</body>" in content:
        content = content.replace("</body>", tab_pane_html + "\n</body>")
    
    with open(player_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated player.html with real nature rain video tab!")
