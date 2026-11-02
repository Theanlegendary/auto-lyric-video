import os

path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace Option 1 block
old_opt1 = 'alt="Alpine Lake Rain">'
btn_opt1 = '''alt="Alpine Lake Rain">
                    <button class="tab-btn" style="width:100%; margin:8px 0 12px 0; background:linear-gradient(135deg, #0284c7, #0369a1); border-color:#38bdf8; color:#fff; font-weight:700; text-align:center; padding:10px; cursor:pointer;" onclick="const p=document.getElementById('big-view-player'); p.src='videos/pure_nature_option1_alpine_lake_night_1min.mp4'; p.play(); p.scrollIntoView({behavior:'smooth', block:'center'});">
                        ▶ Watch Option 1 Video Preview (1-Min Loop)
                    </button>'''

# Replace Option 5 block
old_opt5 = 'alt="Secluded Cabin">'
btn_opt5 = '''alt="Secluded Cabin">
                    <button class="tab-btn" style="width:100%; margin:8px 0 12px 0; background:linear-gradient(135deg, #db2777, #9d174d); border-color:#f472b6; color:#fff; font-weight:700; text-align:center; padding:10px; cursor:pointer;" onclick="const p=document.getElementById('big-view-player'); p.src='videos/real_nature_wide_forest_cabin_night_1min_sample.mp4'; p.play(); p.scrollIntoView({behavior:'smooth', block:'center'});">
                        ▶ Watch Option 5 Video Preview (1-Min Loop)
                    </button>'''

if old_opt1 in text and old_opt5 in text:
    text = text.replace(old_opt1, btn_opt1, 1)
    text = text.replace(old_opt5, btn_opt5, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Success replacing buttons!")
else:
    print("Could not find alt tags")
