import os

path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

asian_section = """
    <!-- PREMIER SPOTLIGHT: JAPAN & KOREA FOREST/CITY RAIN HOUSES -->
    <div id="tab-japan-korea-houses" class="tab-content" style="display:block; margin-top:35px;">
        <div class="video-card" style="border: 2px solid #ec4899; box-shadow: 0 0 35px rgba(236, 72, 153, 0.30);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                <h2 style="margin:0; color:#f472b6;">🏯 🌸 🌧️ PREMIER: Japanese & Korean Forest House Overlooking City in Rain</h2>
                <span style="background:rgba(236,72,153,0.25); color:#fbcfe8; border:1px solid #ec4899; padding:4px 14px; border-radius:20px; font-size:12px; font-weight:800; text-transform:uppercase;">Viral East-Asian Zen Aesthetic</span>
            </div>
            <p class="desc" style="font-size:14px; color:#e2e8f0; line-height:1.6;">
                The ultimate viral rain formula: <strong>Forest + City Intersection</strong>. Traditional wooden architecture nestled in a lush green mountain forest with rain dripping from curved clay tile roof eaves, overlooking a misty quiet city below. Natural bright daylight, fresh vibrant greenery, zero dark gloom, and 100% YouTube monetizable.
            </p>

            <!-- Side-by-Side Comparison -->
            <div style="background:#111827; padding:18px; border-radius:12px; border:1px solid #374151; margin-bottom:25px;">
                <h3 style="color:#ffd700; margin-top:0; margin-bottom:12px; font-size:16px;">📊 Side-by-Side Comparison (Japan vs. Korea):</h3>
                <img src="thumbnail/nature_options/contact_sheet_japan_korea_forest_city.jpg" style="width:100%; border-radius:8px; border:1px solid #4b5563;" alt="Japan vs Korea Rain Houses">
            </div>

            <!-- Two Featured Cards -->
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:25px;">
                
                <!-- OPTION J: JAPAN -->
                <div style="background:#151c28; border:2px solid #38bdf8; border-radius:14px; padding:18px; box-shadow:0 0 20px rgba(56,189,248,0.25);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span style="font-weight:900; color:#38bdf8; font-size:18px;">🏯 OPTION J: Kyoto Forest Wooden House (Japan)</span>
                        <span style="background:rgba(56,189,248,0.25); color:#7dd3fc; font-size:11px; font-weight:800; padding:4px 10px; border-radius:8px;">HIGH CPM VIRAL</span>
                    </div>
                    <img src="thumbnail/nature_options/japan_forest_city_rain_house.jpg" style="width:100%; border-radius:8px; margin-bottom:12px;" alt="Kyoto Japanese House Rain">
                    <p style="font-size:14px; color:#cbd5e1; line-height:1.6; margin:0;">
                        • <strong>Architecture</strong>: Traditional dark cedar wood Machiya with authentic Kawara clay tile roof eaves and open sliding Shoji doors.<br>
                        • <strong>Nature</strong>: Vibrant green moss garden, stone path, bamboo water spout (tsukubai), and Japanese maple trees in gentle rain.<br>
                        • <strong>City View</strong>: Distant misty Kyoto skyline and pagoda rooftops nestled in the valley between the trees.<br>
                        • <strong>Lighting</strong>: Crisp, natural, bright daylight overcast rain (easy on the eyes, rich vibrant greens).
                    </p>
                </div>

                <!-- OPTION K: KOREA -->
                <div style="background:#151c28; border:2px solid #f43f5e; border-radius:14px; padding:18px; box-shadow:0 0 20px rgba(244,63,94,0.25);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span style="font-weight:900; color:#fb7185; font-size:18px;">⛰️ OPTION K: Mountain Hanok Overlooking Seoul (Korea)</span>
                        <span style="background:rgba(244,63,94,0.25); color:#fecdd3; font-size:11px; font-weight:800; padding:4px 10px; border-radius:8px;">HEALING AMBIENCE</span>
                    </div>
                    <img src="thumbnail/nature_options/korea_forest_city_rain_hanok.jpg" style="width:100%; border-radius:8px; margin-bottom:12px;" alt="Korean Hanok Rain">
                    <p style="font-size:14px; color:#cbd5e1; line-height:1.6; margin:0;">
                        • <strong>Architecture</strong>: Traditional Korean Hanok pavilion with sweeping curved Giwa tile roof and polished wooden veranda (maru).<br>
                        • <strong>Nature</strong>: Mountain forest hillside with Korean red pines, stone garden steps, and fresh green bushes under falling rain.<br>
                        • <strong>City View</strong>: Panoramic view through mountain clouds down to the misty Seoul skyline and Lotte Tower.<br>
                        • <strong>Lighting</strong>: Natural bright daylight, fresh mountain rain breeze, soothing and peaceful.
                    </p>
                </div>

            </div>
        </div>
    </div>
"""

# Insert right above <div id="tab-choose-pure-nature"
target = '<div id="tab-choose-pure-nature"'
if target in text:
    text = text.replace(target, asian_section + "\n" + target, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully added Japan & Korea showcase to player.html!")
else:
    print("Target not found")
