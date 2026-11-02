import os
import re

path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"
with open(path, "r", encoding="utf-8") as f:
    raw = f.read()

# 1. Normalize excessive newlines
lines = [l.strip() for l in raw.replace("\r\n", "\n").split("\n")]
clean_lines = []
empty_count = 0
for l in lines:
    if not l:
        empty_count += 1
        if empty_count <= 1:
            clean_lines.append("")
    else:
        empty_count = 0
        clean_lines.append(l)

clean_html = "\n".join(clean_lines)

# 2. Build the 12 Natural Nature ID Showcase
nature_12_section = """
    <!-- 12 REAL NATURE ID SAMPLE VIEWS (NATURAL LIGHTING • NO DARKNESS • NO FIREFLIES) -->
    <div id="tab-choose-pure-nature" class="tab-content" style="display:block; margin-top:35px;">
        <div class="video-card" style="border: 2px solid #10b981; box-shadow: 0 0 35px rgba(16, 185, 129, 0.25);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                <h2 style="margin:0; color:#34d399;">🌲 🌧️ 12 REAL NATURE ID SAMPLE VIEWS (Clear Natural Lighting • Zero Darkness)</h2>
                <span style="background:rgba(16,185,129,0.25); color:#34d399; border:1px solid #10b981; padding:4px 14px; border-radius:20px; font-size:12px; font-weight:800; text-transform:uppercase;">100% Real Live-Action Camera</span>
            </div>
            <p class="desc" style="font-size:14px; color:#e2e8f0; line-height:1.6;">
                Here are <strong>12 Real Nature Rain Views</strong> in their natural daylight and misty overcast lighting (no heavy dark night grade, no fireflies). You can see the vibrant green pine trees, alpine lakes with rain ripples, ancient mossy woods, rainforest canopies, and jungle foliage. Choose the ID you want for our next video!
            </p>

            <!-- Complete 12-ID Contact Sheet Grid -->
            <div style="background:#111827; padding:18px; border-radius:12px; border:1px solid #374151; margin-bottom:25px;">
                <h3 style="color:#ffd700; margin-top:0; margin-bottom:12px; font-size:16px;">📊 Master Contact Sheet: All 12 Nature Rain Views</h3>
                <img src="thumbnail/nature_options/contact_sheet_12_bright_nature_ids.jpg" style="width:100%; border-radius:8px; border:1px solid #4b5563;" alt="12 Nature ID Contact Sheet">
            </div>

            <!-- 12 Individual Nature Cards -->
            <h3 style="color:#38bdf8; margin:25px 0 15px 0; font-size:18px;">🔍 Browse All 12 Nature IDs Individually:</h3>
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:20px;">
                
                <!-- ID 5174040 -->
                <div style="background:#131d2e; border:2px solid #38bdf8; border-radius:12px; padding:15px; box-shadow:0 0 15px rgba(56,189,248,0.2);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                        <span style="font-weight:900; color:#38bdf8; font-size:15px;">ID: 5174040 — Alpine Lake & Pines</span>
                        <span style="background:rgba(56,189,248,0.2); color:#7dd3fc; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">RECOMMENDED</span>
                    </div>
                    <img src="thumbnail/nature_options/bright_nature_5174040.jpg" style="width:100%; border-radius:8px; margin-bottom:10px;" alt="ID 5174040">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: Vast turquoise mountain lake with thousands of gentle rain ripples, towering rocky alpine peaks, and lush pine valley.<br>
                        • <strong>Lighting</strong>: Natural daytime mountain air, bright and crystal clear.
                    </p>
                </div>

                <!-- ID 9934612 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#a78bfa; font-size:15px;">ID: 9934612 — Flooded Mossy Forest</span>
                    <img src="thumbnail/nature_options/bright_nature_9934612.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 9934612">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: Ancient mossy tree trunks reflected in a calm flooded woodland pool with gentle raindrops pattering onto the water surface.<br>
                        • <strong>Lighting</strong>: Atmospheric overcast daylight woods.
                    </p>
                </div>

                <!-- ID 9353501 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#34d399; font-size:15px;">ID: 9353501 — Rainforest Canopy Vista</span>
                    <img src="thumbnail/nature_options/bright_nature_9353501.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 9353501">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: High mountain ridge overlooking an endless ocean of rolling lush green tropical rainforest trees with drifting mist.<br>
                        • <strong>Lighting</strong>: Bright tropical rainforest mountain daylight.
                    </p>
                </div>

                <!-- ID 8110359 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#fbbf24; font-size:15px;">ID: 8110359 — Deep Tropical Ferns</span>
                    <img src="thumbnail/nature_options/bright_nature_8110359.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 8110359">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: Vibrant emerald green jungle foliage, drooping tropical ferns, and wild blossoms in steady rain.<br>
                        • <strong>Lighting</strong>: Rich natural green daylight rainforest.
                    </p>
                </div>

                <!-- ID 11643791 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#f472b6; font-size:15px;">ID: 11643791 — Elephant-Ear Leaves</span>
                    <img src="thumbnail/nature_options/bright_nature_11643791.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 11643791">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: Glistening giant elephant-ear leaves with clean rainwater streams trickling off glossy green surfaces.<br>
                        • <strong>Lighting</strong>: Fresh morning rain daylight.
                    </p>
                </div>

                <!-- ID 13180836 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#60a5fa; font-size:15px;">ID: 13180836 — Misty Old-Growth Woods</span>
                    <img src="thumbnail/nature_options/bright_nature_13180836.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 13180836">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: Ancient thick tree trunk and fresh green forest canopy with gentle misty rain falling through the branches.<br>
                        • <strong>Lighting</strong>: Natural overcast misty forest.
                    </p>
                </div>

                <!-- ID 10766175 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#4ade80; font-size:15px;">ID: 10766175 — Evergreen Pine Ridge</span>
                    <img src="thumbnail/nature_options/bright_nature_10766175.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 10766175">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: Towering evergreen mountain pine trees shrouded in drifting white fog with heavy rain streaming through needles.<br>
                        • <strong>Lighting</strong>: Mountain fog & natural daylight.
                    </p>
                </div>

                <!-- ID 5918481 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#facc15; font-size:15px;">ID: 5918481 — Open Meadow & Valley</span>
                    <img src="thumbnail/nature_options/bright_nature_5918481.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 5918481">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: Expansive open green valley and rural field in heavy summer rainfall with distant tree horizon.<br>
                        • <strong>Lighting</strong>: Bright open daylight rain.
                    </p>
                </div>

                <!-- ID 9328701 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#2dd4bf; font-size:15px;">ID: 9328701 — Jungle Palm Fronds</span>
                    <img src="thumbnail/nature_options/bright_nature_9328701.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 9328701">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: Tropical wild palm fronds and lush rainforest trees swaying gently under monsoon rain.<br>
                        • <strong>Lighting</strong>: Vibrant green jungle daylight.
                    </p>
                </div>

                <!-- ID 4828773 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#a3e635; font-size:15px;">ID: 4828773 — Fresh Garden Greenery</span>
                    <img src="thumbnail/nature_options/bright_nature_4828773.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 4828773">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: Dense hanging grape vine leaves and lush garden foliage with heavy raindrops falling directly onto leaves.<br>
                        • <strong>Lighting</strong>: Bright fresh garden daylight.
                    </p>
                </div>

                <!-- ID 13446069 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#38bdf8; font-size:15px;">ID: 13446069 — Misty Pine Forest</span>
                    <img src="thumbnail/nature_options/bright_nature_13446069.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 13446069">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: Mountain fog and drifting mist rolling through a dense evergreen pine forest in gentle rain.<br>
                        • <strong>Lighting</strong>: Atmospheric cool misty overcast.
                    </p>
                </div>

                <!-- ID 12717007 -->
                <div style="background:#131d2e; border:1px solid #374151; border-radius:12px; padding:15px;">
                    <span style="font-weight:900; color:#f43f5e; font-size:15px;">ID: 12717007 — Cabin in Rainforest (Day)</span>
                    <img src="thumbnail/nature_options/bright_nature_12717007.jpg" style="width:100%; border-radius:8px; margin:8px 0 10px 0;" alt="ID 12717007">
                    <p style="font-size:13px; color:#cbd5e1; line-height:1.5; margin:0;">
                        • <strong>View</strong>: The mountain cabin nestled among banana trees, seen in natural daylight (bright green foliage, no dark blue night filter).<br>
                        • <strong>Lighting</strong>: Natural daytime rainforest.
                    </p>
                </div>

            </div>
        </div>
    </div>
"""

# Replace from <div id="tab-choose-pure-nature" to </body>
start_marker = '<div id="tab-choose-pure-nature"'
end_marker = '</body>'

idx_start = clean_html.find(start_marker)
if idx_start != -1:
    idx_end = clean_html.find(end_marker, idx_start)
    if idx_end != -1:
        updated_html = clean_html[:idx_start] + nature_12_section + "\n" + clean_html[idx_end:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated_html.replace("\n", "\r\n"))
        print("Successfully replaced with 12 Bright Nature IDs in player.html!")
    else:
        print("End marker not found")
else:
    print("Start marker not found")
