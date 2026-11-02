import os

def add_nature_chooser():
    path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    new_section = """
    <!-- CHOOSE YOUR PURE NATURE LOOK SHOWCASE -->
    <div id="tab-choose-pure-nature" class="tab-content" style="display:block; margin-top:35px;">
        <div class="video-card" style="border: 2px solid #00e5ff; box-shadow: 0 0 30px rgba(0, 229, 255, 0.25);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                <h2 style="margin:0; color:#00e5ff;">🌲 🏔️ 🌧️ CHOOSE YOUR PURE NATURE LOOK (100% Wild Nature • Zero Buildings)</h2>
                <span style="background:rgba(0,229,255,0.2); color:#00e5ff; border:1px solid #00e5ff; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:800; text-transform:uppercase;">Visual Selector Catalog</span>
            </div>
            <p class="desc">Which pure wild nature look do you want for our next long sleep video? All options are 100% real live-action camera footage, color-graded into our signature <strong>Midnight Indigo Dark Mode</strong> for insomnia relief, zero screen glare, and 100% monetization safety.</p>

            <!-- Full Contact Sheet -->
            <div style="background:#111722; padding:15px; border-radius:12px; border:1px solid #233144; margin-bottom:25px;">
                <h4 style="color:#ffd700; margin-top:0; margin-bottom:10px;">📊 Side-by-Side Comparison Grid (All Options Graded for Night):</h4>
                <img src="thumbnail/nature_options/contact_sheet_pure_nature_night_graded.jpg" style="width:100%; border-radius:8px; border:1px solid #334460;" alt="Pure Nature Comparison Grid">
            </div>

            <!-- Option Cards Grid -->
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:20px;">
                <!-- OPTION 1 -->
                <div style="background:#141c28; border:2px solid #38bdf8; border-radius:12px; overflow:hidden; padding:15px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                        <span style="font-weight:800; color:#38bdf8; font-size:15px;">🌟 OPTION 1: Alpine Mountain Lake</span>
                        <span style="background:rgba(56,189,248,0.25); color:#7dd3fc; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">RECOMMENDED</span>
                    </div>
                    <img src="thumbnail/nature_options/pure_nature_night_5174040.jpg" style="width:100%; border-radius:8px; margin-bottom:10px;" alt="Alpine Lake Rain">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>Scene</strong>: Epic granite mountain peaks flanking a vast pine valley with heavy rain creating thousands of soothing ripples across crystal lake water.<br>
                        • <strong>Vibe</strong>: 100% Pure wilderness vista, ultra-peaceful, zero buildings.<br>
                        • <strong>Sleep Rating</strong>: ⭐⭐⭐⭐⭐ (Most soothing for dark bedrooms).
                    </p>
                </div>

                <!-- OPTION 2 -->
                <div style="background:#141c28; border:1px solid #2a3749; border-radius:12px; overflow:hidden; padding:15px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                        <span style="font-weight:800; color:#a78bfa; font-size:15px;">OPTION 2: Flooded Ancient Forest</span>
                        <span style="background:rgba(167,139,250,0.25); color:#c4b5fd; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">DEEP MYSTERY</span>
                    </div>
                    <img src="thumbnail/nature_options/pure_nature_night_9934612.jpg" style="width:100%; border-radius:8px; margin-bottom:10px;" alt="Flooded Forest Rain">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>Scene</strong>: Ancient mossy trees standing in calm, mist-shrouded forest water with heavy rain pattering onto the water surface.<br>
                        • <strong>Vibe</strong>: Secluded deep woodland sanctuary, rich reflections, mysterious tranquility.<br>
                        • <strong>Sleep Rating</strong>: ⭐⭐⭐⭐⭐ (Hypnotic water ripples).
                    </p>
                </div>

                <!-- OPTION 3 -->
                <div style="background:#141c28; border:1px solid #2a3749; border-radius:12px; overflow:hidden; padding:15px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                        <span style="font-weight:800; color:#34d399; font-size:15px;">OPTION 3: Misty Evergreen Pine Ridge</span>
                        <span style="background:rgba(52,211,153,0.25); color:#6ee7b7; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">PACIFIC RAIN</span>
                    </div>
                    <img src="thumbnail/nature_options/pure_nature_night_10766175.jpg" style="width:100%; border-radius:8px; margin-bottom:10px;" alt="Misty Pine Ridge">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>Scene</strong>: Endless mountain pines shrouded in drifting fog with torrential rain streaming down through giant pine needles.<br>
                        • <strong>Vibe</strong>: Mountain storm, dense wilderness, organic pine forest downpour.<br>
                        • <strong>Sleep Rating</strong>: ⭐⭐⭐⭐ (Intense cozy mountain atmosphere).
                    </p>
                </div>

                <!-- OPTION 4 -->
                <div style="background:#141c28; border:1px solid #2a3749; border-radius:12px; overflow:hidden; padding:15px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                        <span style="font-weight:800; color:#fbbf24; font-size:15px;">OPTION 4: Tropical Rainforest Ridge</span>
                        <span style="background:rgba(251,191,36,0.25); color:#fde68a; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">MONSOON</span>
                    </div>
                    <img src="thumbnail/nature_options/pure_nature_night_9353501.jpg" style="width:100%; border-radius:8px; margin-bottom:10px;" alt="Rainforest Canopy">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>Scene</strong>: High mountain ridge overlooking an endless rolling sea of tropical jungle trees in heavy monsoon rain.<br>
                        • <strong>Vibe</strong>: Expansive rainforest horizon, wild jungle canopy.<br>
                        • <strong>Sleep Rating</strong>: ⭐⭐⭐⭐ (Vast open landscape).
                    </p>
                </div>

                <!-- OPTION 5 -->
                <div style="background:#141c28; border:1px solid #2a3749; border-radius:12px; overflow:hidden; padding:15px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                        <span style="font-weight:800; color:#f472b6; font-size:15px;">OPTION 5: Secluded Cabin in Rainforest</span>
                        <span style="background:rgba(244,114,182,0.25); color:#fbcfe8; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">CURRENT 3H MASTER</span>
                    </div>
                    <img src="thumbnail/nature_options/pure_nature_night_12717007.jpg" style="width:100%; border-radius:8px; margin-bottom:10px;" alt="Secluded Cabin">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>Scene</strong>: Secluded mountain cabin with metal roof nestled in lush banana trees and tropical foliage in midnight rain.<br>
                        • <strong>Vibe</strong>: Cozy shelter, tin roof acoustic clatter + rolling thunder.<br>
                        • <strong>Status</strong>: Ready now! (Full 3-Hour master already rendered above).
                    </p>
                </div>
            </div>
        </div>
    </div>
"""

    norm_html = html.replace("\r\n", "\n")
    target = "</body>"
    replacement = new_section + "\n</body>"

    if target in norm_html:
        norm_html = norm_html.replace(target, replacement, 1)
        final_html = norm_html.replace("\n", "\r\n")
        with open(path, "w", encoding="utf-8") as f:
            f.write(final_html)
        print("Successfully added Pure Nature Look Selector to player.html!")
    else:
        print("Target not found in player.html")

if __name__ == "__main__":
    add_nature_chooser()
