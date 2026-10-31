# Antigravity Brain Context — Fade Replay Lyric Video Engine

> **Brand**: **Fade Replay**  
> **Repository**: `https://github.com/Theanlegendary/auto-lyric-video`  
> **Workspace Path**: `C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video`  
> **Catalog**: 30 Songs (00 to 29) + 20-Minute 5-Time Replay Loop Engine

Whenever Antigravity or any AI assistant runs in this project or on this topic, strictly adhere to the following brain rules:

---

## 1. Visual & Typography Standard (Authentic 7clouds Formula)
- **Backgrounds**: High-contrast, high-quality landscape image (Unsplash aesthetic or Makoto Shinkai scenic anime sky/ocean).
- **Core Font**: **Edo SZ** (`fonts/edosz.ttf` by Vic Fieger). Signature bold, brush-stroke style script font that gives the lyrics an impactful, organic look.
  - *Alternative/Handwritten option*: **Patrick Hand** (`fonts/PatrickHand.ttf`).
- **Text Shadow & Glow**: Soft black outer glow / shadow behind pure white text (`&H00FFFFFF`) with `\blur1.8`, `Outline: 3.2`, `Shadow: 2.2` to prevent lyrics from getting lost on changing backgrounds.
- **Case Logic**: Standard **Sentence case** rather than ALL CAPS, making long lines effortless to read sequentially.
- **Sizing & Screen Space**:
  - Main lyric text occupies roughly **35% to 45% of screen width** (scaled 60pt–68pt in 1080p).
  - Strictly **1 or 2 lines maximum** at any given time. Phrases longer than 4–5 words split into 2 stacked lines.
  - Positioned vertically in the **lower third** of the viewport (roughly **75% to 80% down from top**, `Alignment: 2`, `MarginV: 180–220px`), clearing timeline seeker and video UI overlays.
- **Structural Transition Logic**:
  - **Pacing ("Word-Chunk" Logic)**: Lyrics appear in complete semantic phrases right as the artist begins speaking the first word.
  - **The "Rest" Cut**: The moment a phrase ends, text **instantly disappears**. Empty screen during pauses and instrumental breaks creates visual breathing room.
  - **Transitions**: **Zero-frame cuts** (no fade-ins or animations `\fad(0,0)`), snapping precisely onto the audio grid.
- **Secondary Font**: Clean, highly legible Sans-Serif font (like Montserrat, Arial, or Poppins SemiBold at 28pt–32pt) for intro track metadata: `Artist - Title (Lyrics)`.

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
