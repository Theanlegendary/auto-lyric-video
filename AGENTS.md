# Antigravity Brain Context — Fade Replay Lyric Video Engine

> **Brand**: **Fade Replay**  
> **Repository**: `https://github.com/Theanlegendary/auto-lyric-video`  
> **Workspace Path**: `C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video`  
> **Catalog**: 30 Songs (00 to 29) + 20-Minute 5-Time Replay Loop Engine

Whenever Antigravity or any AI assistant runs in this project or on this topic, strictly adhere to the following brain rules:

---

## 1. Visual & Typography Standard (7clouds Formula)
- **Backgrounds**: Scenic anime cumulus clouds at twilight, dawn, or sunset (Makoto Shinkai aesthetic).
- **Negative Reading Space**: The central 60% of the screen must be clean sky gradients free of human silhouettes, buildings, ground clutter, or text.
- **Font**: **Patrick Hand** (`fonts/PatrickHand.ttf`) for lyrics and hook titles.
  - Title Hook Card: 170–200pt, centered (`\pos(960,460)`), fade in/out (`\fad(500,400)`).
  - Couplet Subtitles: 96–102pt, centered (`\pos(960,490)`), fade in/out (`\fad(200,150)`).
- **Colors**:
  - Primary text: Pure White `&H00FFFFFF`
  - Outline: Deep Charcoal/Navy `&H00101828` with `Outline: 3.8`
  - Shadow: Soft drop shadow `&H80000000` with `Shadow: 2.2`
  - Contrast Ratio: Must maintain $\ge 10:1$ contrast against the sky.
- **Line Limit Rule**: Strictly $\le 2$ rows per couplet. Never wrap to 3 lines. Horizontal margins $> 180$px.

---

## 2. Audio & Loop Formats
1. **Normal 1.0x Full Mix**: Standard high-definition studio mix (`audio.mp3`).
2. **Slowed + Reverb Brand Edition**:
   - 0.865x Tape Varispeed ($tempo \times 0.865$, pitch drops $-2.5$ semitones).
   - 3.0s Cathedral Reverb hall.
   - 15.5kHz Warm Tape Shelf EQ.
   - Subtitle timestamps scaled by $1 / 0.865$.
3. **20+ Minute 5-Time Replay Loop Edition**:
   - 6 total plays (1 original + 5 continuous replays).
   - Chapter title cards on loops 2–6 (`Artist • Replay [k/5]`).
   - Looped audio via `ffmpeg -stream_loop 5 -i audio.mp3`.
   - Maximize YouTube Average View Duration (AVD 12–16 min) and mid-roll ad monetization.

---

## 3. Standard Pipeline for Adding a Song
1. Download audio & synced lyrics: `syncedlyrics.search("<Artist> - <Title>")`.
2. Align word timestamps using `faster-whisper base.en` (`whisper_words.txt`).
3. Break lyrics into balanced 2-row couplets ($\le 38$ chars per line). Generate `.ass` file.
4. Generate 16:9 7clouds cloudscape wallpaper (negative space in center, twilight/sunset mood).
5. Render MP4 with FFmpeg using zoompan drift + ASS subtitle filter.
6. Verification Audit: Extract test frames, verify contrast ratio $> 10:1$, confirm zero text clipping.
7. Append to `Fade_Replay_YouTube_Upload_Guide.txt` and `player.html`.
