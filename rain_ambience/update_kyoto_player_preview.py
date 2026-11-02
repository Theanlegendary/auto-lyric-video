import os

path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace the image in Style 1 card with the newly darker version and add video preview button
old_img_tag = '<img src="thumbnail/nature_options/old_style_1_kyoto_edo_tea_house.jpg" style="width:100%; border-radius:8px; margin-bottom:12px;" alt="Edo Kyoto Tea House">'

new_img_tag = '''<img src="thumbnail/nature_options/kyoto_edo_darker_level_b.jpg" style="width:100%; border-radius:8px; margin-bottom:8px;" alt="Edo Kyoto Tea House (Cozy Dusk)">
                    <button class="tab-btn" style="width:100%; margin:4px 0 12px 0; background:linear-gradient(135deg, #0284c7, #0369a1); border-color:#38bdf8; color:#fff; font-weight:700; text-align:center; padding:10px; cursor:pointer;" onclick="const p=document.getElementById('big-view-player'); p.src='videos/kyoto_edo_tea_house_rain_living_loop_1min.mp4'; p.play(); p.scrollIntoView({behavior:'smooth', block:'center'});">
                        ▶ Watch Kyoto Tea House Living Rain Video Preview (1-Min Loop)
                    </button>'''

# Add darkness levels comparison grid into the card
darkness_comparison_html = """
            <!-- KYOTO DARKNESS LEVELS COMPARISON -->
            <div style="background:#111827; padding:18px; border-radius:12px; border:1px solid #374151; margin:20px 0;">
                <h3 style="color:#38bdf8; margin-top:0; margin-bottom:10px; font-size:16px;">🌙 Darkness Levels for Kyoto Tea House (Original vs Level A vs Level B vs Level C):</h3>
                <img src="thumbnail/nature_options/contact_sheet_kyoto_darkness_levels.jpg" style="width:100%; border-radius:8px; border:1px solid #4b5563;" alt="Kyoto Darkness Levels">
            </div>
"""

target_insert = '<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:20px;">'

if old_img_tag in text and target_insert in text:
    text = text.replace(old_img_tag, new_img_tag, 1)
    text = text.replace(target_insert, darkness_comparison_html + "\n            " + target_insert, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully updated Kyoto darkness levels and video preview button in player.html!")
else:
    print("Could not find targets in player.html")
