import os

section_html = '''
        <!-- PREMIER: 100% REAL LIVE-ACTION CAMERA RAIN FOOTAGE -->
        <div id="tab-real-camera-rain" class="tab-content" style="display:block; margin-top:35px;">
            <div class="video-card" style="border: 2px solid #38bdf8; box-shadow: 0 0 40px rgba(56, 189, 248, 0.35); background:#0c121e;">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                    <div>
                        <span style="background:linear-gradient(135deg, #0284c7, #0369a1); color:#fff; font-size:11px; font-weight:900; padding:4px 10px; border-radius:6px; letter-spacing:1px;">100% REAL CAMERA FOOTAGE</span>
                        <h2 style="margin:8px 0 4px 0; color:#38bdf8; font-size:24px;">📹 Real Live-Action Rain: Cozy Shelter, Roof Eaves & Japanese Temple</h2>
                        <p style="color:#94a3b8; margin:0; font-size:14px;">Genuine live filmed video (real water droplets, swaying trees, dripping eaves) with high-fidelity 48kHz binaural rain sound.</p>
                    </div>
                    <span style="background:rgba(56, 189, 248, 0.15); border:1px solid #38bdf8; color:#7dd3fc; padding:6px 12px; border-radius:8px; font-size:12px; font-weight:800;">GENUINE FILMED FOOTAGE</span>
                </div>

                <!-- Contact Sheet -->
                <div style="background:#111827; padding:18px; border-radius:12px; border:1px solid #374151; margin:20px 0;">
                    <h3 style="color:#38bdf8; margin-top:0; margin-bottom:10px; font-size:16px;">📸 8 Real Camera Rain Candidates Contact Sheet:</h3>
                    <img src="thumbnail/nature_options/contact_sheet_real_camera_rain_vibe.jpg" style="width:100%; border-radius:8px; border:1px solid #4b5563;" alt="Real Camera Rain Candidates">
                </div>

                <!-- 3 Top Real Video Cards -->
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:20px;">
                    
                    <!-- REAL OPTION 1: JAPAN TEMPLE -->
                    <div style="background:#151c28; border:2px solid #38bdf8; border-radius:14px; padding:18px; box-shadow:0 0 20px rgba(56,189,248,0.2);">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                            <span style="font-weight:900; color:#38bdf8; font-size:16px;">⛩️ 1. Authentic Japanese Temple Rain Chain</span>
                            <span style="background:rgba(56,189,248,0.2); color:#7dd3fc; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">AUTHENTIC JAPAN</span>
                        </div>
                        <img src="thumbnail/nature_options/real_rain_option1_japanese_temple.jpg" style="width:100%; border-radius:8px; margin-bottom:8px;" alt="Real Japanese Temple Rain">
                        <button class="tab-btn" style="width:100%; margin:4px 0 12px 0; background:linear-gradient(135deg, #0284c7, #0369a1); border-color:#38bdf8; color:#fff; font-weight:700; text-align:center; padding:10px; cursor:pointer;" onclick="const p=document.getElementById('big-view-player'); p.src='videos/real_rain_option1_japanese_temple_rain_chain_1min.mp4'; p.play(); p.scrollIntoView({behavior:'smooth', block:'center'});">
                            ▶ Watch Real Option 1: Japan Temple Rain Chain (1-Min Loop)
                        </button>
                        <p style="font-size:13px; color:#cbd5e1; line-height:1.6; margin:0;">
                            <strong>Location</strong>: Historic Japanese Temple (Kyoto / Kamakura).<br>
                            <strong>Visual</strong>: Genuine 4K footage of a copper rain chain (<em>kusaridoi</em>) channeling water from dark temple roof eaves into the temple courtyard, with lush green Japanese trees.<br>
                            <strong>Sound</strong>: Crystal-clear gentle rainfall with water trickling down the rain chain.
                        </p>
                    </div>

                    <!-- REAL OPTION 2: WOODEN ROOF EAVES -->
                    <div style="background:#151c28; border:2px solid #10b981; border-radius:14px; padding:18px; box-shadow:0 0 20px rgba(16,185,129,0.2);">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                            <span style="font-weight:900; color:#34d399; font-size:16px;">🏡 2. Wooden House Roof Eaves & Forest Rain</span>
                            <span style="background:rgba(16,185,129,0.2); color:#6ee7b7; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">COZY SHELTER</span>
                        </div>
                        <img src="thumbnail/nature_options/real_rain_option2_roof_eaves.jpg" style="width:100%; border-radius:8px; margin-bottom:8px;" alt="Real Roof Eaves Rain">
                        <button class="tab-btn" style="width:100%; margin:4px 0 12px 0; background:linear-gradient(135deg, #059669, #047857); border-color:#34d399; color:#fff; font-weight:700; text-align:center; padding:10px; cursor:pointer;" onclick="const p=document.getElementById('big-view-player'); p.src='videos/real_rain_option2_roof_eaves_forest_rain_1min.mp4'; p.play(); p.scrollIntoView({behavior:'smooth', block:'center'});">
                            ▶ Watch Real Option 2: Wooden House Eaves Rain (1-Min Loop)
                        </button>
                        <p style="font-size:13px; color:#cbd5e1; line-height:1.6; margin:0;">
                            <strong>View</strong>: Porch perspective from under dark wooden roof eaves.<br>
                            <strong>Visual</strong>: Heavy natural rain pouring in beautiful vertical streams off the roof edge, lush green trees swaying in the background.<br>
                            <strong>Sound</strong>: Deep, steady rain patter and distant rolling thunder.
                        </p>
                    </div>

                    <!-- REAL OPTION 3: MOODY DARK SHELTER -->
                    <div style="background:#151c28; border:2px solid #a855f7; border-radius:14px; padding:18px; box-shadow:0 0 20px rgba(168,85,247,0.2);">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                            <span style="font-weight:900; color:#c084fc; font-size:16px;">🌧️ 3. Moody Dark Shelter & Green Canopy</span>
                            <span style="background:rgba(168,85,247,0.2); color:#d8b4fe; font-size:10px; font-weight:800; padding:3px 8px; border-radius:6px;">DARK & MOODY</span>
                        </div>
                        <img src="thumbnail/nature_options/real_rain_option3_dark_shelter.jpg" style="width:100%; border-radius:8px; margin-bottom:8px;" alt="Dark Shelter Rain">
                        <button class="tab-btn" style="width:100%; margin:4px 0 12px 0; background:linear-gradient(135deg, #7e22ce, #6b21a8); border-color:#c084fc; color:#fff; font-weight:700; text-align:center; padding:10px; cursor:pointer;" onclick="const p=document.getElementById('big-view-player'); p.src='videos/real_rain_option3_dark_shelter_forest_rain_1min.mp4'; p.play(); p.scrollIntoView({behavior:'smooth', block:'center'});">
                            ▶ Watch Real Option 3: Dark Shelter Rain (1-Min Loop)
                        </button>
                        <p style="font-size:13px; color:#cbd5e1; line-height:1.6; margin:0;">
                            <strong>Lighting</strong>: Darker moody overcast dusk atmosphere.<br>
                            <strong>Visual</strong>: Rain dripping from shelter overhang into dark, rich emerald rainforest leaves. Cozy and contemplative.<br>
                            <strong>Sound</strong>: Soft binaural rainfall with peaceful ambient woodland resonance.
                        </p>
                    </div>

                </div>
            </div>
        </div>
'''

target_marker = '<!-- PREMIER: 3 AUTHENTIC HISTORIC OLD-STYLE HOUSES IN RAIN -->'
player_path = r'C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html'

with open(player_path, 'r', encoding='utf-8') as f:
    content = f.read()

if target_marker in content:
    content = content.replace(target_marker, section_html + '\n\n        ' + target_marker)
    with open(player_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Successfully injected Real Camera Rain section into player.html!')
else:
    print('Target marker not found!')
