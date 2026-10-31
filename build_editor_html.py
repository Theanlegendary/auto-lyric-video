#!/usr/bin/env python3
"""
Build the full-featured Aesthetic Lyric Studio & Cinematic Background Engine (editor.html).
Includes:
- 8 Curated Cinematic Background Presets (Rainy City, Twilight, Sunset, Moonlit Ocean, Lonely Bedroom, Misty Road, Travel, Forest)
- User custom image/video file uploader with live canvas analysis
- Ken Burns slow zoom (1.00x -> 1.06x) & gentle pan motion engine
- Real-time lyric area luminance analysis & adaptive contrast HUD
- Subtle film grain, scrim gradient, and dimming controls
- Professional Opening Title Sequence designer (Title, Artist, Feat, Album, Year, Watermark)
- Non-overlapping 2-line couplet lyrics engine with upward settle
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
manifest_path = BASE_DIR / "songs_manifest.json"

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest_data = json.load(f)

# Import background library
from background_engine import get_background_library
bg_library = get_background_library()

manifest_json_str = json.dumps(manifest_data, ensure_ascii=False)
bg_library_json_str = json.dumps(bg_library, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aesthetic Lyric Video Studio & Background Engine</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-dark: #100d14;
      --panel-bg: #1a1420;
      --panel-border: #31253a;
      --accent: #ca669d;
      --accent-hover: #e079b1;
      --accent-glow: rgba(202, 102, 157, 0.35);
      --text-main: #f5f0f6;
      --text-muted: #a79bae;
      --soft-white: #F7F5F2;
      --charcoal: #222222;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: var(--bg-dark);
      color: var(--text-main);
      font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 18px 16px 48px;
    }}

    .studio-container {{
      max-width: 1480px;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .studio-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 24px;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 16px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }}

    .studio-title h1 {{
      font-size: 21px;
      font-weight: 600;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .studio-title p {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .badge {{
      display: inline-block;
      font-size: 11px;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 20px;
      background: rgba(202, 102, 157, 0.18);
      color: #ff9ecc;
      border: 1px solid rgba(202, 102, 157, 0.4);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .badge.cinematic {{
      background: rgba(142, 221, 184, 0.18);
      color: #8eddb8;
      border-color: rgba(142, 221, 184, 0.4);
    }}

    /* Main Grid */
    .studio-grid {{
      display: grid;
      grid-template-columns: 1fr 440px;
      gap: 20px;
    }}

    @media (max-width: 1100px) {{
      .studio-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Canvas Card */
    .preview-card {{
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 16px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      box-shadow: 0 12px 40px rgba(0,0,0,0.5);
    }}

    .canvas-wrapper {{
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      background: #000;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    }}

    canvas#lyricCanvas {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    /* Playback Controls */
    .playback-bar {{
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 14px;
      background: #140f18;
      border-radius: 10px;
      border: 1px solid #2a2130;
    }}

    .btn-play {{
      background: var(--accent);
      color: #fff;
      border: none;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 16px;
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px var(--accent-glow);
    }}

    .btn-play:hover {{
      background: var(--accent-hover);
      transform: scale(1.05);
    }}

    .time-display {{
      font-size: 13px;
      font-family: monospace;
      color: #ddd;
      min-width: 90px;
    }}

    .scrubber-slider {{
      flex: 1;
      accent-color: var(--accent);
      cursor: pointer;
      height: 6px;
    }}

    /* Contrast HUD */
    .contrast-hud {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #130e18;
      border: 1px solid #281e2e;
      border-radius: 10px;
      padding: 8px 14px;
      font-size: 12px;
    }}

    .hud-chip {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .hud-indicator {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #8eddb8;
      box-shadow: 0 0 8px #8eddb8;
    }}

    /* Controls Sidebar */
    .control-card {{
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 16px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      box-shadow: 0 12px 40px rgba(0,0,0,0.5);
      max-height: 87vh;
      overflow-y: auto;
    }}

    .section-title {{
      font-size: 13px;
      font-weight: 700;
      color: #e5d8ea;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      border-bottom: 1px solid #2e2436;
      padding-bottom: 6px;
      margin-top: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    /* Background Library Carousel Grid */
    .bg-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}

    .bg-card {{
      background: #241c2a;
      border: 1px solid #362940;
      border-radius: 10px;
      overflow: hidden;
      cursor: pointer;
      transition: all 0.15s ease;
      display: flex;
      flex-direction: column;
      text-align: left;
    }}

    .bg-card:hover {{
      border-color: #5d456f;
      transform: translateY(-1px);
    }}

    .bg-card.active {{
      border-color: var(--accent);
      box-shadow: 0 0 12px rgba(202, 102, 157, 0.35);
    }}

    .bg-thumb {{
      width: 100%;
      height: 60px;
      object-fit: cover;
      background: #100a14;
    }}

    .bg-info {{
      padding: 6px 8px;
      font-size: 11px;
    }}

    .bg-info strong {{
      display: block;
      color: #f0e6f2;
      font-size: 11px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .bg-info span {{
      color: #9f91a5;
      font-size: 10px;
    }}

    /* Upload Box */
    .upload-box {{
      border: 2px dashed #42324f;
      border-radius: 10px;
      padding: 12px;
      text-align: center;
      cursor: pointer;
      background: rgba(30, 22, 36, 0.4);
      transition: all 0.2s ease;
      font-size: 12px;
      color: #c9bacc;
    }}

    .upload-box:hover {{
      border-color: var(--accent);
      background: rgba(202, 102, 157, 0.08);
      color: #fff;
    }}

    /* Preset & Controls */
    .presets-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 8px;
    }}

    .preset-btn {{
      background: #241c2a;
      border: 1px solid #382c42;
      border-radius: 8px;
      padding: 8px 6px;
      color: #d1bfd6;
      font-size: 11px;
      text-align: center;
      cursor: pointer;
      transition: all 0.15s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
    }}

    .preset-btn.active {{
      background: #472144;
      border-color: var(--accent);
      color: #fff;
      font-weight: 600;
    }}

    .field-group {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .field-group label {{
      font-size: 11px;
      color: #b7a6bd;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }}

    .input-text {{
      background: #141018;
      border: 1px solid #362940;
      border-radius: 6px;
      padding: 7px 10px;
      color: #fff;
      font-size: 13px;
      font-family: inherit;
    }}

    .input-text:focus {{
      outline: none;
      border-color: var(--accent);
    }}

    .param-group {{
      display: flex;
      flex-direction: column;
      gap: 5px;
    }}

    .param-header {{
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      color: #b7a6bd;
    }}

    .param-header span.val {{
      color: var(--accent);
      font-family: monospace;
      font-weight: 600;
    }}

    input[type="range"] {{
      width: 100%;
      accent-color: var(--accent);
      cursor: pointer;
      height: 5px;
      background: #2a2030;
      border-radius: 4px;
    }}

    .toggle-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
      color: #d5c7db;
    }}

    .btn-export {{
      background: linear-gradient(135deg, #a43a7a, #ca669d);
      color: #fff;
      border: none;
      padding: 12px 18px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 6px 20px var(--accent-glow);
      margin-top: 6px;
    }}

    .btn-export:hover {{
      background: linear-gradient(135deg, #b8438a, #db72ae);
      transform: translateY(-1px);
    }}
  </style>
</head>
<body>

  <div class="studio-container">
    <div class="studio-header">
      <div class="studio-title">
        <h1>
          <span>Aesthetic Lyric Video Studio</span>
          <span class="badge cinematic">Cinematic Background Engine</span>
        </h1>
        <p>Curated sad-song backgrounds, Ken Burns motion, adaptive contrast, and pro opening sequence.</p>
      </div>
      <div>
        <span style="font-size: 12px; color: #a99bb0;">Rainy City &middot; Moonlit Ocean &middot; Twilight Starry Night &middot; Misty Road</span>
      </div>
    </div>

    <div class="studio-grid">
      <!-- Preview Canvas -->
      <div class="preview-card">
        <div class="canvas-wrapper" id="canvasWrapper">
          <canvas id="lyricCanvas" width="1920" height="1080"></canvas>
        </div>

        <div class="playback-bar">
          <button class="btn-play" id="btnPlay" onclick="togglePlay()">&#9658;</button>
          <span class="time-display" id="timeDisplay">00:00 / 00:00</span>
          <input type="range" class="scrubber-slider" id="scrubber" min="0" max="100" value="0" step="0.1" oninput="onScrub(this.value)">
        </div>

        <!-- Real-time HUD -->
        <div class="contrast-hud">
          <div class="hud-chip">
            <span class="hud-indicator" id="hudIndicator"></span>
            <span id="hudLuminance">Lyric Zone: 57.6 / 255</span>
          </div>
          <div class="hud-chip">
            <span style="color: #bbb;">Active Style:</span>
            <strong id="hudActiveStyle" style="color: #F7F5F2;">Soft White (#F7F5F2)</strong>
          </div>
          <div class="hud-chip">
            <span style="color: #bbb;">Motion:</span>
            <span id="hudMotionStatus" style="color: #8eddb8; font-family: monospace;">Ken Burns Zoom (1.00x &rarr; 1.06x)</span>
          </div>
        </div>
      </div>

      <!-- Controls Sidebar -->
      <div class="control-card">
        <!-- 1. Song Selection -->
        <div class="section-title">Select Song</div>
        <select id="selectSong" class="input-text" style="width: 100%; cursor: pointer;" onchange="loadSong(parseInt(this.value))">
          <!-- Populated dynamically -->
        </select>

        <!-- 2. Cinematic Background Presets -->
        <div class="section-title">Cinematic Background Library</div>
        <div class="bg-grid" id="bgGrid"></div>

        <!-- Custom Upload -->
        <div class="upload-box" onclick="document.getElementById('fileUpload').click()">
          <span>&#128247; <strong>Upload Custom Image or Video</strong></span>
          <div style="font-size: 11px; opacity: 0.7; margin-top: 2px;">Drop photo, GIF, or MP4 here</div>
          <input type="file" id="fileUpload" style="display: none;" accept="image/*,video/*" onchange="handleCustomUpload(this)">
        </div>

        <!-- 3. Motion & Visual Treatment -->
        <div class="section-title">Visual Treatment & Motion</div>
        <div class="param-group">
          <div class="param-header">
            <span>Ken Burns Motion Intensity</span>
            <span class="val" id="valMotion">Cinematic (6%)</span>
          </div>
          <input type="range" id="sliderMotion" min="0" max="12" value="6" step="1" oninput="updateParam('motionIntensity', this.value)">
        </div>

        <div class="param-group">
          <div class="param-header">
            <span>Soft Scrim Gradient</span>
            <span class="val" id="valScrim">24%</span>
          </div>
          <input type="range" id="sliderScrim" min="0" max="60" value="24" step="2" oninput="updateParam('scrimIntensity', this.value)">
        </div>

        <div class="param-group">
          <div class="param-header">
            <span>Background Dim / Vignette</span>
            <span class="val" id="valDim">18%</span>
          </div>
          <input type="range" id="sliderDim" min="0" max="60" value="18" step="2" oninput="updateParam('dimIntensity', this.value)">
        </div>

        <div class="param-group">
          <div class="param-header">
            <span>Soft Gaussian Blur</span>
            <span class="val" id="valBlur">0px</span>
          </div>
          <input type="range" id="sliderBlur" min="0" max="16" value="0" step="1" oninput="updateParam('blurRadius', this.value)">
        </div>

        <div class="toggle-row">
          <span>35mm Organic Film Grain</span>
          <input type="checkbox" id="checkFilmGrain" checked onchange="updateParam('filmGrain', this.checked)">
        </div>

        <!-- 4. Typography Presets -->
        <div class="section-title">Typography Preset</div>
        <div class="presets-grid">
          <div class="preset-btn active" id="btnPresetCinematic" onclick="setPreset('cinematic')">
            <span style="font-family: 'Cormorant Garamond'; font-size: 17px;">Aa</span>
            <strong>Style A</strong>
            <span style="font-size: 9px; opacity: 0.75;">Cormorant Garamond</span>
          </div>

          <div class="preset-btn" id="btnPresetIndie" onclick="setPreset('indie')">
            <span style="font-family: 'DM Sans'; font-size: 15px;">Aa</span>
            <strong>Style C</strong>
            <span style="font-size: 9px; opacity: 0.75;">DM Sans Medium</span>
          </div>

          <div class="preset-btn" id="btnPresetModern" onclick="setPreset('modern')">
            <span style="font-family: 'Inter'; font-size: 15px;">Aa</span>
            <strong>Style B</strong>
            <span style="font-size: 9px; opacity: 0.75;">Inter Medium</span>
          </div>
        </div>

        <!-- 5. Opening Sequence -->
        <div class="section-title">
          <span>Opening Title Sequence</span>
          <input type="checkbox" id="checkOpening" checked onchange="updateParam('openingEnabled', this.checked)">
        </div>

        <div class="field-group">
          <label>Song Title</label>
          <input type="text" class="input-text" id="inputTitle" oninput="updateOpeningMeta('title', this.value)">
        </div>

        <div class="field-group">
          <label>Artist Name</label>
          <input type="text" class="input-text" id="inputArtist" oninput="updateOpeningMeta('artist', this.value)">
        </div>

        <div class="field-group">
          <label>Featured Artist (Optional)</label>
          <input type="text" class="input-text" id="inputFeat" placeholder="e.g. feat. Bruno Mars" oninput="updateOpeningMeta('featured_artist', this.value)">
        </div>

        <div class="param-group">
          <div class="param-header">
            <span>Opening Duration</span>
            <span class="val" id="valOpeningDur">4.5s</span>
          </div>
          <input type="range" id="sliderOpeningDur" min="1.5" max="7.0" value="4.5" step="0.5" oninput="updateOpeningMeta('duration', this.value)">
        </div>

        <button class="btn-export" onclick="exportAss()">
          <span>&#8681;</span> Export Remastered ASS Subtitles
        </button>
      </div>
    </div>
  </div>

  <audio id="audioPlayer" preload="auto"></audio>

  <script>
    const SONGS = {manifest_json_str};
    const BG_LIBRARY = {bg_library_json_str};

    let activeSongIndex = 2; // Default to Die With A Smile (the user's favorite!)
    let activePreset = 'cinematic'; // Default to Cormorant Garamond
    let activeBgId = 'twilight_night';

    let customUploadedImg = null;
    let customUploadedVideo = null;

    const settings = {{
      fontFamily: "'Cormorant Garamond', serif",
      fontWeight: '600',
      fontSize: 60,
      verticalRatio: 0.60,
      lineHeightMult: 1.25,
      letterSpacing: 0.8,
      casing: 'sentence',
      motionIntensity: 0.06, // 6% slow zoom
      scrimIntensity: 0.24,
      dimIntensity: 0.18,
      blurRadius: 0,
      filmGrain: true
    }};

    const canvas = document.getElementById('lyricCanvas');
    const ctx = canvas.getContext('2d');
    const audio = document.getElementById('audioPlayer');
    const scrubber = document.getElementById('scrubber');
    const timeDisplay = document.getElementById('timeDisplay');
    const btnPlay = document.getElementById('btnPlay');

    const hudIndicator = document.getElementById('hudIndicator');
    const hudLuminance = document.getElementById('hudLuminance');
    const hudActiveStyle = document.getElementById('hudActiveStyle');

    const loadedBgImages = {{}};

    function initStudio() {{
      preloadBackgrounds();
      renderSongDropdown();
      renderBgGrid();
      loadSong(activeSongIndex);
      setupCanvasLoop();
    }}

    function preloadBackgrounds() {{
      BG_LIBRARY.forEach(bg => {{
        const img = new Image();
        img.src = bg.relative_url;
        loadedBgImages[bg.id] = img;
      }});
    }}

    function renderSongDropdown() {{
      const sel = document.getElementById('selectSong');
      sel.innerHTML = '';
      SONGS.forEach((s, i) => {{
        const opt = document.createElement('option');
        opt.value = i;
        opt.textContent = `${{s.title}} — ${{s.artist}}`;
        if (i === activeSongIndex) opt.selected = true;
        sel.appendChild(opt);
      }});
    }}

    function renderBgGrid() {{
      const grid = document.getElementById('bgGrid');
      grid.innerHTML = '';
      BG_LIBRARY.forEach(bg => {{
        const card = document.createElement('div');
        card.className = 'bg-card' + (bg.id === activeBgId ? ' active' : '');
        card.innerHTML = `
          <img class="bg-thumb" src="${{bg.relative_url}}" alt="${{bg.name}}">
          <div class="bg-info">
            <strong>${{bg.name}}</strong>
            <span>${{bg.category.replace('_', ' ')}} &middot; Lum ${{bg.mean_lum}}</span>
          </div>
        `;
        card.onclick = () => selectBackground(bg.id);
        grid.appendChild(card);
      }});
    }}

    function selectBackground(bgId) {{
      activeBgId = bgId;
      customUploadedImg = null;
      customUploadedVideo = null;
      document.querySelectorAll('.bg-card').forEach(c => c.classList.remove('active'));
      const activeCard = Array.from(document.querySelectorAll('.bg-card')).find(c => c.innerHTML.includes(bgId));
      if (activeCard) activeCard.classList.add('active');

      const bg = BG_LIBRARY.find(b => b.id === bgId);
      if (bg) {{
        updateHudForBg(bg.mean_lum, bg.contrast_mode);
      }}
    }}

    function handleCustomUpload(input) {{
      if (!input.files || !input.files[0]) return;
      const file = input.files[0];
      const url = URL.createObjectURL(file);

      if (file.type.startsWith('video/')) {{
        const vid = document.createElement('video');
        vid.src = url;
        vid.loop = true;
        vid.muted = true;
        vid.autoplay = true;
        vid.play();
        customUploadedVideo = vid;
        customUploadedImg = null;
      }} else {{
        const img = new Image();
        img.src = url;
        customUploadedImg = img;
        customUploadedVideo = null;
      }}

      activeBgId = 'custom';
      document.querySelectorAll('.bg-card').forEach(c => c.classList.remove('active'));
      hudLuminance.textContent = 'Custom Uploaded Background';
      hudActiveStyle.textContent = 'Soft White (#F7F5F2)';
      hudActiveStyle.style.color = '#F7F5F2';
      hudIndicator.style.background = '#F7F5F2';
    }}

    function loadSong(idx) {{
      activeSongIndex = idx;
      const song = SONGS[idx];
      audio.src = song.audio_url;
      audio.load();

      document.getElementById('inputTitle').value = song.title;
      document.getElementById('inputArtist').value = song.artist;
      document.getElementById('inputFeat').value = song.featured_artist || '';
      document.getElementById('checkOpening').checked = song.opening.enabled;
      document.getElementById('sliderOpeningDur').value = song.opening.duration;
      document.getElementById('valOpeningDur').textContent = song.opening.duration + 's';

      if (song.recommended_preset) {{
        setPreset(song.recommended_preset);
      }}

      // Match background to song style
      if (song.id === 'die_with_a_smile') selectBackground('twilight_night');
      else if (song.id === 'ophelia') selectBackground('dreamy_sunset');
      else if (song.id === 'apt') selectBackground('rainy_city_night');
      else if (song.id === 'golden') selectBackground('moonlit_ocean');
      else if (song.id === 'birds_of_a_feather') selectBackground('soft_nature');
    }}

    function updateHudForBg(lum, mode) {{
      hudLuminance.textContent = `Lyric Zone: ${{lum}} / 255`;
      if (mode === 'bright_bg') {{
        hudActiveStyle.textContent = 'Dark Charcoal (#222222)';
        hudActiveStyle.style.color = '#ff9ecc';
        hudIndicator.style.background = '#222222';
      }} else {{
        hudActiveStyle.textContent = 'Soft White (#F7F5F2)';
        hudActiveStyle.style.color = '#F7F5F2';
        hudIndicator.style.background = '#F7F5F2';
      }}
    }}

    function setPreset(key) {{
      activePreset = key;
      document.querySelectorAll('.preset-btn').forEach(btn => btn.classList.remove('active'));

      if (key === 'cinematic') {{
        document.getElementById('btnPresetCinematic').classList.add('active');
        settings.fontFamily = "'Cormorant Garamond', serif";
        settings.fontWeight = '600';
        settings.fontSize = 60;
        settings.lineHeightMult = 1.25;
        settings.letterSpacing = 0.8;
        settings.casing = 'sentence';
      }} else if (key === 'indie') {{
        document.getElementById('btnPresetIndie').classList.add('active');
        settings.fontFamily = "'DM Sans', sans-serif";
        settings.fontWeight = '500';
        settings.fontSize = 52;
        settings.lineHeightMult = 1.24;
        settings.letterSpacing = 2.0;
        settings.casing = 'lowercase';
      }} else if (key === 'modern') {{
        document.getElementById('btnPresetModern').classList.add('active');
        settings.fontFamily = "'Inter', sans-serif";
        settings.fontWeight = '500';
        settings.fontSize = 54;
        settings.lineHeightMult = 1.22;
        settings.letterSpacing = 0.2;
        settings.casing = 'sentence';
      }}
    }}

    function updateParam(param, val) {{
      if (param === 'motionIntensity') {{
        settings.motionIntensity = parseFloat(val) / 100.0;
        document.getElementById('valMotion').textContent = val === '0' ? 'Static (0%)' : `Cinematic (${{val}}%)`;
      }} else if (param === 'scrimIntensity') {{
        settings.scrimIntensity = parseFloat(val) / 100.0;
        document.getElementById('valScrim').textContent = val + '%';
      }} else if (param === 'dimIntensity') {{
        settings.dimIntensity = parseFloat(val) / 100.0;
        document.getElementById('valDim').textContent = val + '%';
      }} else if (param === 'blurRadius') {{
        settings.blurRadius = parseInt(val);
        document.getElementById('valBlur').textContent = val + 'px';
      }} else if (param === 'filmGrain') {{
        settings.filmGrain = Boolean(val);
      }} else if (param === 'openingEnabled') {{
        SONGS[activeSongIndex].opening.enabled = Boolean(val);
      }}
    }}

    function updateOpeningMeta(field, val) {{
      const song = SONGS[activeSongIndex];
      if (field === 'duration') {{
        song.opening.duration = parseFloat(val);
        document.getElementById('valOpeningDur').textContent = val + 's';
      }} else {{
        song[field] = val;
      }}
    }}

    function togglePlay() {{
      if (audio.paused) {{
        audio.play();
        btnPlay.innerHTML = '&#10074;&#10074;';
      }} else {{
        audio.pause();
        btnPlay.innerHTML = '&#9658;';
      }}
    }}

    function onScrub(val) {{
      if (audio.duration) {{
        audio.currentTime = (parseFloat(val) / 100.0) * audio.duration;
      }}
    }}

    function formatTime(s) {{
      const m = Math.floor(s / 60);
      const sec = Math.floor(s % 60);
      return `${{m.toString().padStart(2, '0')}}:${{sec.toString().padStart(2, '0')}}`;
    }}

    function formatLyricCasing(text, mode) {{
      if (!text) return '';
      if (mode === 'lowercase') return text.toLowerCase();
      let s = text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
      s = s.replace(/\\bi\\b/g, 'I')
           .replace(/\\bi'm\\b/g, "I'm")
           .replace(/\\bi'd\\b/g, "I'd")
           .replace(/\\bi'll\\b/g, "I'll")
           .replace(/\\bi've\\b/g, "I've")
           .replace(/\\bbruno mars\\b/gi, 'Bruno Mars')
           .replace(/\\blady gaga\\b/gi, 'Lady Gaga')
           .replace(/\\btaylor swift\\b/gi, 'Taylor Swift')
           .replace(/\\bbillie eilish\\b/gi, 'Billie Eilish')
           .replace(/\\bapt\\b/gi, 'APT')
           .replace(/\\bophelia\\b/gi, 'Ophelia');
      return s;
    }}

    // Real-Time Canvas Rendering Loop with Ken Burns Engine
    function setupCanvasLoop() {{
      function render() {{
        const curTime = audio.currentTime || 0;
        const dur = audio.duration || 1;

        if (!audio.paused) {{
          scrubber.value = (curTime / dur) * 100;
          timeDisplay.textContent = `${{formatTime(curTime)}} / ${{formatTime(dur)}}`;
        }}

        // 1. Calculate Ken Burns Zoom & Pan from playback timestamp
        // Slow zoom from 1.00 to (1.00 + motionIntensity) over 30s cycle
        const cycleProgress = (curTime % 30.0) / 30.0;
        const zoom = 1.00 + (settings.motionIntensity * cycleProgress);
        const panX = (cycleProgress - 0.5) * 20.0;

        ctx.save();
        ctx.clearRect(0, 0, 1920, 1080);

        // Apply Ken Burns transformation centered
        ctx.translate(960 + panX, 540);
        ctx.scale(zoom, zoom);
        ctx.translate(-960, -540);

        // Draw Background (Image or Video)
        if (customUploadedVideo && customUploadedVideo.readyState >= 2) {{
          ctx.drawImage(customUploadedVideo, 0, 0, 1920, 1080);
        }} else if (customUploadedImg && customUploadedImg.complete) {{
          ctx.drawImage(customUploadedImg, 0, 0, 1920, 1080);
        }} else {{
          const bgImg = loadedBgImages[activeBgId];
          if (bgImg && bgImg.complete && bgImg.naturalWidth > 0) {{
            ctx.drawImage(bgImg, 0, 0, 1920, 1080);
          }} else {{
            ctx.fillStyle = '#140f18';
            ctx.fillRect(0, 0, 1920, 1080);
          }}
        }}

        ctx.restore(); // Restore unscaled coordinate system for UI & lyrics

        // 2. Visual Treatment: Soft Dimming & Restrained Vignette
        if (settings.dimIntensity > 0) {{
          ctx.fillStyle = `rgba(10, 8, 14, ${{settings.dimIntensity}})`;
          ctx.fillRect(0, 0, 1920, 1080);
        }}

        // 3. Soft Translucent Scrim Gradient behind Lyric Region
        if (settings.scrimIntensity > 0) {{
          drawTranslucentScrim(settings.verticalRatio, settings.scrimIntensity);
        }}

        // 4. Subtle 35mm Moving Film Grain
        if (settings.filmGrain) {{
          drawSubtleFilmGrain();
        }}

        // 5. Active Text Contrast Determination
        const bgPreset = BG_LIBRARY.find(b => b.id === activeBgId);
        const isDarkText = bgPreset && bgPreset.contrast_mode === 'bright_bg';
        const textColor = isDarkText ? '#222222' : '#F7F5F2';
        const outlineColor = isDarkText ? 'rgba(255, 255, 255, 0.45)' : 'rgba(18, 16, 22, 0.45)';
        const shadowColor = isDarkText ? 'rgba(255, 255, 255, 0.35)' : 'rgba(0, 0, 0, 0.45)';

        // 6. Professional Opening Sequence
        const song = SONGS[activeSongIndex];
        const openCfg = song.opening;
        if (openCfg && openCfg.enabled && curTime >= openCfg.start_time && curTime <= (openCfg.start_time + openCfg.duration)) {{
          renderOpeningSequence(curTime, song, openCfg, textColor, outlineColor, shadowColor);
        }}

        // 7. Active Lyric Couplet
        const activeCue = song.couplets.find(c => curTime >= c.start && curTime <= c.end);
        if (activeCue) {{
          renderLyricCue(curTime, activeCue, textColor, outlineColor, shadowColor);
        }}

        requestAnimationFrame(render);
      }}

      requestAnimationFrame(render);
    }}

    function drawTranslucentScrim(vRatio, intensity) {{
      const centerY = 1080 * vRatio;
      const hHalf = 190;
      const grad = ctx.createLinearGradient(0, centerY - hHalf, 0, centerY + hHalf);
      grad.addColorStop(0, 'rgba(0, 0, 0, 0)');
      grad.addColorStop(0.5, `rgba(0, 0, 0, ${{intensity}})`);
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');

      ctx.save();
      ctx.fillStyle = grad;
      ctx.fillRect(0, centerY - hHalf, 1920, hHalf * 2);
      ctx.restore();
    }}

    function drawSubtleFilmGrain() {{
      ctx.save();
      ctx.fillStyle = 'rgba(255, 255, 255, 0.022)';
      for (let i = 0; i < 350; i++) {{
        const gx = Math.random() * 1920;
        const gy = Math.random() * 1080;
        ctx.fillRect(gx, gy, 1.5, 1.5);
      }}
      ctx.restore();
    }}

    function renderOpeningSequence(t, song, cfg, textColor, outlineColor, shadowColor) {{
      const elapsed = t - cfg.start_time;
      const remaining = (cfg.start_time + cfg.duration) - t;

      let opacity = 1.0;
      if (elapsed < 0.6) opacity = elapsed / 0.6;
      else if (remaining < 0.6) opacity = Math.max(0, remaining / 0.6);

      let yOffset = 0;
      if (elapsed < 0.5) {{
        const p = elapsed / 0.5;
        const easeOut = 1 - (1 - p) * (1 - p);
        yOffset = (1 - easeOut) * 16;
      }}

      ctx.save();
      ctx.globalAlpha = opacity;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';

      const baseY = (1080 * 0.48) + yOffset;

      // Title
      ctx.font = `${{settings.fontWeight}} ${{Math.round(settings.fontSize * 1.35)}}px ${{settings.fontFamily}}`;
      ctx.fillStyle = textColor;
      ctx.shadowColor = shadowColor;
      ctx.shadowBlur = 4;
      ctx.shadowOffsetX = 1.5;
      ctx.shadowOffsetY = 1.5;
      ctx.fillText(formatLyricCasing(song.title, 'sentence'), 960, baseY);

      // Artist
      let artistLine = song.artist;
      if (song.featured_artist) artistLine += ` (feat. ${{song.featured_artist}})`;
      ctx.font = `500 ${{Math.round(settings.fontSize * 0.65)}}px ${{settings.fontFamily}}`;
      ctx.fillText(artistLine, 960, baseY + settings.fontSize * 0.95);

      ctx.restore();
    }}

    function renderLyricCue(t, cue, textColor, outlineColor, shadowColor) {{
      const elapsed = t - cue.start;
      const remaining = cue.end - t;

      let opacity = 1.0;
      if (elapsed < 0.28) opacity = elapsed / 0.28;
      else if (remaining < 0.22) opacity = Math.max(0, remaining / 0.22);

      let yOffset = 0;
      if (elapsed < 0.28) {{
        const progress = elapsed / 0.28;
        const easeOut = 1 - (1 - progress) * (1 - progress);
        yOffset = (1 - easeOut) * 14;
      }}

      const lines = cue.lines.map(l => formatLyricCasing(l, settings.casing));
      const baseY = (1080 * settings.verticalRatio) + yOffset;
      const lineSpacing = settings.fontSize * settings.lineHeightMult;

      ctx.save();
      ctx.globalAlpha = opacity;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.font = `${{settings.fontWeight}} ${{settings.fontSize}}px ${{settings.fontFamily}}`;

      ctx.shadowColor = shadowColor;
      ctx.shadowBlur = 4;
      ctx.shadowOffsetX = 1.5;
      ctx.shadowOffsetY = 1.5;

      if (lines.length === 1) {{
        ctx.fillStyle = textColor;
        ctx.fillText(lines[0], 960, baseY);
      }} else {{
        const y1 = baseY - (lineSpacing / 2);
        const y2 = baseY + (lineSpacing / 2);
        ctx.fillStyle = textColor;
        ctx.fillText(lines[0], 960, y1);
        ctx.fillText(lines[1], 960, y2);
      }}

      ctx.restore();
    }}

    function exportAss() {{
      const song = SONGS[activeSongIndex];
      const fontName = activePreset === 'cinematic' ? 'Cormorant Garamond' :
                       activePreset === 'modern' ? 'Inter' : 'DM Sans';
      const bold = activePreset === 'cinematic' ? 1 : 0;
      const vRatio = settings.verticalRatio;
      const fontSize = settings.fontSize;

      const bg = BG_LIBRARY.find(b => b.id === activeBgId);
      const isDark = bg && bg.contrast_mode === 'bright_bg';
      const priColor = isDark ? '&H00222222' : '&H00F2F5F7';
      const outColor = isDark ? '&H5AFFFFFF' : '&H50161214';
      const shadowColor = isDark ? '&H4DFFFFFF' : '&H66000000';

      let assContent = `[Script Info]\\nTitle: ${{song.title}} - ${{song.artist}}\\nScriptType: v4.00+\\nPlayResX: 1920\\nPlayResY: 1080\\nWrapStyle: 0\\nScaledBorderAndShadow: yes\\n\\n`;
      assContent += `[V4+ Styles]\\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\\n`;
      assContent += `Style: TitleCard,${{fontName}},${{Math.round(fontSize * 1.35)}},${{priColor}},&H000000FF,${{outColor}},${{shadowColor}},${{bold}},0,0,0,100,100,1.5,0,1,1.0,2.0,5,50,50,50,1\\n`;
      assContent += `Style: Lyric,${{fontName}},${{fontSize}},${{priColor}},&H000000FF,${{outColor}},${{shadowColor}},${{bold}},0,0,0,100,100,${{settings.letterSpacing}},0,1,1.0,2.0,5,50,50,50,1\\n\\n`;
      assContent += `[Events]\\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\\n`;

      if (song.opening && song.opening.enabled && song.first_vocal_start >= 2.0) {{
        const titleY = Math.round(1080 * 0.48);
        const st = song.opening.start_time;
        const et = st + song.opening.duration;
        const toAss = (s) => {{
          const h = Math.floor(s / 3600);
          const m = Math.floor((s % 3600) / 60);
          const sec = (s % 60).toFixed(2).padStart(5, '0');
          return `${{h}}:${{m.toString().padStart(2, '0')}}:${{sec}}`;
        }};
        assContent += `Dialogue: 0,${{toAss(st)}},${{toAss(et)}},TitleCard,,0,0,0,,{{\\\\pos(960,${{titleY}})\\\\fad(500,450)\\\\fsp1.5}}${{formatLyricCasing(song.title, 'sentence')}}\\\\N{{\\\\fs42\\\\fsp2.5\\\\c${{priColor}}}}${{song.artist}}\\n`;
      }}

      const baseY = Math.round(1080 * vRatio);
      song.couplets.forEach(cue => {{
        const toAss = (s) => {{
          const h = Math.floor(s / 3600);
          const m = Math.floor((s % 3600) / 60);
          const sec = (s % 60).toFixed(2).padStart(5, '0');
          return `${{h}}:${{m.toString().padStart(2, '0')}}:${{sec}}`;
        }};

        const lines = cue.lines.map(l => formatLyricCasing(l, settings.casing));
        const anim = `\\\\move(960,${{baseY + 12}},960,${{baseY}},0,300)\\\\fad(280,200)\\\\fsp${{settings.letterSpacing}}`;
        const text = lines.join('\\\\N');
        assContent += `Dialogue: 0,${{toAss(cue.start)}},${{toAss(cue.end)}},Lyric,,0,0,0,,{{${{anim}}}}${{text}}\\n`;
      }});

      const blob = new Blob([assContent], {{ type: 'text/plain;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${{song.title.replace(/[^a-zA-Z0-9]/g, '_')}}_${{activeBgId}}.ass`;
      a.click();
      URL.revokeObjectURL(url);
    }}

    window.onload = initStudio;
  </script>
</body>
</html>
"""

out_html = BASE_DIR / "editor.html"
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated {out_html} ({out_html.stat().st_size} bytes)")
