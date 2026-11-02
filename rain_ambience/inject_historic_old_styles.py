import os

path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

historic_section = """
    <!-- PREMIER: 3 AUTHENTIC HISTORIC OLD-STYLE HOUSES IN RAIN -->
    <div id="tab-historic-old-styles" class="tab-content" style="display:block; margin-top:35px;">
        <div class="video-card" style="border: 2px solid #ffd700; box-shadow: 0 0 40px rgba(255, 215, 0, 0.35);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                <h2 style="margin:0; color:#ffd700;">🏯 🌾 🌧️ 3 AUTHENTIC HISTORIC OLD-STYLE HOUSES IN RAIN (Japan & Korea)</h2>
                <span style="background:rgba(255,215,0,0.25); color:#ffd700; border:1px solid #ffd700; padding:4px 14px; border-radius:20px; font-size:12px; font-weight:800; text-transform:uppercase;">100% Ancient Heritage Vibe</span>
            </div>
            <p class="desc" style="font-size:14px; color:#e2e8f0; line-height:1.6;">
                True authentic <strong>Old-Style Architecture</strong>: Aged rustic dark timber, moss-covered antique roof tiles and historic thatched straw, stone lanterns, hand-hewn wood, and traditional historic village rooftops in the misty mountain rain. Natural bright overcast daylight, fresh vibrant greenery, zero modern skyscrapers.
            </p>

            <!-- 3-Way Comparison Grid -->
            <div style="background:#111827; padding:18px; border-radius:12px; border:1px solid #374151; margin-bottom:25px;">
                <h3 style="color:#ffd700; margin-top:0; margin-bottom:12px; font-size:16px;">📊 3-Way Comparison: All 3 Historic Old Styles</h3>
                <img src="thumbnail/nature_options/contact_sheet_3_historic_old_styles.jpg" style="width:100%; border-radius:8px; border:1px solid #4b5563;" alt="3 Historic Old Styles">
            </div>

            <!-- 3 Individual Cards -->
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:20px;">
                
                <!-- STYLE 1: EDO KYOTO -->
                <div style="background:#151c28; border:2px solid #38bdf8; border-radius:14px; padding:18px; box-shadow:0 0 20px rgba(56,189,248,0.2);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span style="font-weight:900; color:#38bdf8; font-size:16px;">🏯 1. Edo Kyoto Mountain Tea House</span>
                        <span style="background:rgba(56,189,248,0.2); color:#7dd3fc; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">ZEN RETREAT</span>
                    </div>
                    <img src="thumbnail/nature_options/old_style_1_kyoto_edo_tea_house.jpg" style="width:100%; border-radius:8px; margin-bottom:12px;" alt="Edo Kyoto Tea House">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.6; margin:0;">
                        • <strong>Architecture</strong>: Weathered dark cedar timber, antique curved clay roof tiles with genuine green moss, open Shoji screens, and a soft warm paper floor lantern (*Andon*) inside.<br>
                        • <strong>Garden & Forest</strong>: Ancient stone lantern (*Ishidoro*), wet flagstone pathway, weeping red maple, and bamboo grove.<br>
                        • <strong>View</strong>: Distant misty terraced valley with traditional wooden roofs.<br>
                        • <strong>Lighting</strong>: Natural bright daylight rain.
                    </p>
                </div>

                <!-- STYLE 2: SHIRAKAWA-GO -->
                <div style="background:#151c28; border:2px solid #10b981; border-radius:14px; padding:18px; box-shadow:0 0 20px rgba(16,185,129,0.2);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span style="font-weight:900; color:#34d399; font-size:16px;">🌾 2. Shirakawa-go Thatched Farmhouse</span>
                        <span style="background:rgba(16,185,129,0.2); color:#6ee7b7; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">RUSTIC HERITAGE</span>
                    </div>
                    <img src="thumbnail/nature_options/old_style_2_shirakawago_thatched_house.jpg" style="width:100%; border-radius:8px; margin-bottom:12px;" alt="Shirakawa-go Farmhouse">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.6; margin:0;">
                        • <strong>Architecture</strong>: Authentic historic *Gassho-zukuri* steep thatched straw roof with moss and heavy rain streaming off the eaves, hand-hewn weathered timber walls.<br>
                        • <strong>Environment</strong>: Stone water basin with bamboo fountain, cedar trees, and misty mountain slopes.<br>
                        • <strong>View</strong>: Historic rural mountain village and rice terraces.<br>
                        • <strong>Lighting</strong>: Atmospheric overcast daylight rain.
                    </p>
                </div>

                <!-- STYLE 3: JOSEON HANOK -->
                <div style="background:#151c28; border:2px solid #f43f5e; border-radius:14px; padding:18px; box-shadow:0 0 20px rgba(244,63,94,0.2);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span style="font-weight:900; color:#fb7185; font-size:16px;">⛰️ 3. Joseon Historic Mountain Hanok</span>
                        <span style="background:rgba(244,63,94,0.2); color:#fecdd3; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">PALACE & MOUNTAIN</span>
                    </div>
                    <img src="thumbnail/nature_options/old_style_3_joseon_historic_hanok.jpg" style="width:100%; border-radius:8px; margin-bottom:12px;" alt="Joseon Hanok Rain">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.6; margin:0;">
                        • <strong>Architecture</strong>: Historic Joseon Hanok residence with elegant curved clay *Giwa* tile roofs, wooden veranda (*Maru*), and earthen stone foundation.<br>
                        • <strong>Garden</strong>: Rain dripping from the roof into a serene lotus pond with rain ripples, glazed *Jangdokdae* earthenware pots, and ancient twisted pines.<br>
                        • <strong>View</strong>: Misty mountain valley with traditional roofs.<br>
                        • <strong>Lighting</strong>: Fresh, bright, peaceful daylight rain.
                    </p>
                </div>

            </div>
        </div>
    </div>
"""

# Insert right above <div id="tab-japan-korea-houses"
target = '<div id="tab-japan-korea-houses"'
if target in text:
    text = text.replace(target, historic_section + "\n" + target, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully added Historic Old Styles to player.html!")
else:
    print("Target not found")
