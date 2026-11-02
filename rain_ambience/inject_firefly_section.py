import os

path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

firefly_block = """
            <!-- MAGICAL FIREFLIES SPECIAL SHOWCASE -->
            <div style="margin-top:30px; background:linear-gradient(135deg, rgba(20, 25, 45, 0.95), rgba(15, 20, 35, 0.95)); border:2px solid #fbbf24; border-radius:14px; padding:20px; box-shadow:0 0 25px rgba(251, 191, 36, 0.25);">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                    <h3 style="margin:0; color:#ffd700; font-size:18px;">✨ 🪲 🌧️ SPECIAL EDITION: Rain in Nature with Glowing Bioluminescent Fireflies</h3>
                    <span style="background:rgba(251,191,36,0.25); color:#fde68a; border:1px solid #fbbf24; padding:4px 12px; border-radius:20px; font-size:11px; font-weight:800; text-transform:uppercase;">Viral YouTube Concept</span>
                </div>
                <p style="font-size:14px; color:#e2e8f0; line-height:1.6; margin-bottom:15px;">
                    Combining peaceful heavy rain with hundreds of warm, hypnotic golden & emerald glowing fireflies floating through the dark trees and reflecting on calm water ripples.
                </p>
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:15px;">
                    <div style="background:#0f1520; padding:12px; border-radius:10px; border:1px solid #28374d;">
                        <h4 style="color:#38bdf8; margin:0 0 8px 0;">Firefly Look A: Flooded Ancient Forest (Most Magical)</h4>
                        <img src="thumbnail/nature_options/fireflies_flooded_forest.jpg" style="width:100%; border-radius:6px;" alt="Fireflies Flooded Forest">
                        <p style="font-size:12px; color:#cbd5e1; margin:8px 0 0 0;">Glowing fireflies hovering above water ripples with reflections between ancient mossy trees.</p>
                    </div>
                    <div style="background:#0f1520; padding:12px; border-radius:10px; border:1px solid #28374d;">
                        <h4 style="color:#a78bfa; margin:0 0 8px 0;">Firefly Look B: Alpine Mountain Lake</h4>
                        <img src="thumbnail/nature_options/fireflies_alpine_lake.jpg" style="width:100%; border-radius:6px;" alt="Fireflies Alpine Lake">
                        <p style="font-size:12px; color:#cbd5e1; margin:8px 0 0 0;">Luminous fireflies dancing across the wide mountain lake surface with dark pine valley.</p>
                    </div>
                    <div style="background:#0f1520; padding:12px; border-radius:10px; border:1px solid #28374d;">
                        <h4 style="color:#f472b6; margin:0 0 8px 0;">Firefly Look C: Rainforest Cabin Sanctuary</h4>
                        <img src="thumbnail/nature_options/fireflies_rainforest_cabin.jpg" style="width:100%; border-radius:6px;" alt="Fireflies Rainforest Cabin">
                        <p style="font-size:12px; color:#cbd5e1; margin:8px 0 0 0;">Hypnotic golden glowing orbs drifting through the banana leaves and canopy around the cabin.</p>
                    </div>
                </div>
            </div>
"""

# Insert right after closing of option cards grid
target = '</div>\n\n        </div>\n\n    </div>\n\n\n\n</body>'
norm_text = text.replace("\r\n", "\n")

# Find the end of option cards grid
marker = '• <strong>Status</strong>: Ready now! (Full 3-Hour master already rendered above).'
if marker in norm_text:
    idx = norm_text.find(marker)
    # find the closing </div> of the card, then </div> of grid
    idx2 = norm_text.find('</div>', idx)
    idx3 = norm_text.find('</div>', idx2 + 6)
    insertion_pt = idx3 + 6
    updated = norm_text[:insertion_pt] + firefly_block + norm_text[insertion_pt:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(updated.replace("\n", "\r\n"))
    print("Successfully added Fireflies showcase to player.html!")
else:
    print("Could not find marker")
