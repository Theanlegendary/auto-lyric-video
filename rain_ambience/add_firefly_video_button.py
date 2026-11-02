import os

path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

target = '<h4 style="color:#38bdf8; margin:0 0 8px 0;">Firefly Look A: Flooded Ancient Forest (Most Magical)</h4>'
replacement = '''<h4 style="color:#38bdf8; margin:0 0 8px 0;">Firefly Look A: Flooded Ancient Forest (Most Magical)</h4>
                        <button class="tab-btn" style="width:100%; margin:0 0 10px 0; background:linear-gradient(135deg, #0284c7, #0369a1); border-color:#38bdf8; color:#fff; font-weight:700; text-align:center; padding:8px; cursor:pointer;" onclick="const p=document.getElementById('big-view-player'); p.src='videos/magical_fireflies_rain_forest_night_sample.mp4'; p.play(); p.scrollIntoView({behavior:'smooth', block:'center'});">
                            ▶ Play Live Fireflies Animated Video (30s)
                        </button>'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Added play button for fireflies video!")
else:
    print("Target not found")
