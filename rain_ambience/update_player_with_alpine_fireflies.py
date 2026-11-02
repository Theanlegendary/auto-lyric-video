import os

winner_html = '''
        <!-- SELECTED WINNER: ALPINE MOUNTAIN LAKE AT NIGHT + TINY DELICATE FIREFLIES -->
        <div id="tab-alpine-lake-winner" class="tab-content" style="display:block; margin-top:35px;">
            <div class="video-card" style="border: 3px solid #38bdf8; box-shadow: 0 0 50px rgba(56, 189, 248, 0.45); background: linear-gradient(180deg, #091322 0%, #050b14 100%);">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:14px;">
                    <div>
                        <span style="background:linear-gradient(135deg, #0284c7, #38bdf8); color:#000; font-size:11px; font-weight:900; padding:4px 10px; border-radius:6px; letter-spacing:1px;">⭐ SELECTED MASTER PREVIEW</span>
                        <h2 style="margin:8px 0 4px 0; color:#38bdf8; font-size:24px;">✨ Alpine Mountain Lake in Night Rain + 4 Tiny Delicate Fireflies</h2>
                        <p style="color:#94a3b8; margin:0; font-size:14px;">Real 1080p alpine lake rain footage with deep night blue grading, 4 tiny organic bioluminescent fireflies gently drifting and twinkling over the water, and 48kHz binaural rain sound.</p>
                    </div>
                    <span style="background:rgba(56, 189, 248, 0.15); border:1px solid #38bdf8; color:#7dd3fc; padding:6px 14px; border-radius:8px; font-size:12px; font-weight:800;">YOUR SELECTION</span>
                </div>

                <div style="display:grid; grid-template-columns: 1fr; gap:15px;">
                    <div style="background:#0f172a; border:2px solid #38bdf8; border-radius:14px; padding:18px;">
                        <img src="thumbnail/nature_options/alpine_lake_tiny_fireflies_preview.jpg" style="width:100%; border-radius:10px; margin-bottom:12px; border:1px solid #334155;" alt="Alpine Lake with Tiny Fireflies">
                        
                        <button class="tab-btn" style="width:100%; margin:4px 0 14px 0; background:linear-gradient(135deg, #0284c7, #0369a1); border-color:#38bdf8; color:#fff; font-weight:800; font-size:15px; text-align:center; padding:14px; cursor:pointer; box-shadow:0 0 25px rgba(56,189,248,0.35);" onclick="const p=document.getElementById('big-view-player'); p.src='videos/alpine_lake_night_tiny_fireflies_1min.mp4'; p.play(); p.scrollIntoView({behavior:'smooth', block:'center'});">
                            ▶ Click to Watch: Alpine Lake + Tiny Fireflies (1-Min Preview Loop)
                        </button>
                        
                        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:12px; font-size:13px; color:#cbd5e1; line-height:1.6; margin-top:8px;">
                            <div style="background:#1e293b; padding:12px; border-radius:8px;">
                                <strong style="color:#38bdf8;">🌲 Visual & Scene</strong>: Real alpine lake surrounded by pine mountain valley, gentle raindrops pattering on water surface with deep moody night grading.
                            </div>
                            <div style="background:#1e293b; padding:12px; border-radius:8px;">
                                <strong style="color:#fbbf24;">✨ 4 Tiny Fireflies</strong>: Smallest pinpoint micro-cores (1.5px) with soft organic halo (6px), gently drifting with sinusoidal physics and periodic soft breathing twinkle.
                            </div>
                            <div style="background:#1e293b; padding:12px; border-radius:8px;">
                                <strong style="color:#34d399;">🎧 Binaural Audio</strong>: 48kHz stereo natural rain patter + soft mountain wind and distant rolling thunder.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
'''

target_marker = '<!-- PREMIER: 100% REAL LIVE-ACTION CAMERA RAIN FOOTAGE -->'
player_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"

with open(player_path, "r", encoding="utf-8") as f:
    content = f.read()

if target_marker in content:
    content = content.replace(target_marker, winner_html + "\n\n        " + target_marker)
    with open(player_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully injected Alpine Lake Winner Card into player.html!")
else:
    print("Target marker not found!")
