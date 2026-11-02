import os

def update_buttons():
    path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Add button to Option 1
    opt1_target = '• <strong>Sleep Rating</strong>: ⭐⭐⭐⭐⭐ (Most soothing for dark bedrooms).\n                    </p>'
    opt1_replace = '''• <strong>Sleep Rating</strong>: ⭐⭐⭐⭐⭐ (Most soothing for dark bedrooms).
                    </p>
                    <button class="tab-btn" style="width:100%; margin-top:12px; background:linear-gradient(135deg, #0284c7, #0369a1); border-color:#38bdf8; color:#fff; font-weight:700; text-align:center; padding:10px;" onclick="const p=document.getElementById('big-view-player'); p.src='videos/pure_nature_option1_alpine_lake_night_1min.mp4'; p.play(); p.scrollIntoView({behavior:'smooth', block:'center'});">
                        ▶ Watch Option 1 Video Preview (1-Min Loop)
                    </button>'''

    # Add button to Option 5
    opt5_target = '• <strong>Status</strong>: Ready now! (Full 3-Hour master already rendered above).\n                    </p>'
    opt5_replace = '''• <strong>Status</strong>: Ready now! (Full 3-Hour master already rendered above).
                    </p>
                    <button class="tab-btn" style="width:100%; margin-top:12px; background:linear-gradient(135deg, #db2777, #9d174d); border-color:#f472b6; color:#fff; font-weight:700; text-align:center; padding:10px;" onclick="const p=document.getElementById('big-view-player'); p.src='videos/real_nature_wide_forest_cabin_night_1min_sample.mp4'; p.play(); p.scrollIntoView({behavior:'smooth', block:'center'});">
                        ▶ Watch Option 5 Video Preview (1-Min Loop)
                    </button>'''

    norm_html = html.replace("\r\n", "\n")
    if opt1_target in norm_html and opt5_target in norm_html:
        norm_html = norm_html.replace(opt1_target, opt1_replace, 1)
        norm_html = norm_html.replace(opt5_target, opt5_replace, 1)
        final_html = norm_html.replace("\n", "\r\n")
        with open(path, "w", encoding="utf-8") as f:
            f.write(final_html)
        print("Updated buttons in player.html successfully!")
    else:
        print("Targets not found!")

if __name__ == "__main__":
    update_buttons()
