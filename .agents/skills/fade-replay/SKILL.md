---
name: fade-replay
description: >-
  Use this skill to produce aesthetic lyric videos in the 7clouds style, generate 20-minute 5-time replay study loops, apply slowed+reverb audio effects, or manage the Fade Replay 30-song music pipeline.
---

# Fade Replay — Automated Lyric Video Skill

Use this skill whenever creating, remastering, auditing, or managing aesthetic lyric videos.

## Core Rules

1. **7clouds Aesthetics**: High-contrast, scenic landscape or anime sky/ocean (Unsplash style).
2. **Couplets & Screen Space**: Strictly $\le 2$ rows per couplet. Occupies 35% to 45% screen width. Positioned in lower third (75%–80% down from top, `Alignment: 2`, `MarginV: 180–220px`).
3. **Typography**: **Edo SZ** (`edosz.ttf` by Vic Fieger) signature brush font in **Sentence case** (or **Patrick Hand** handwritten alternative). Pure white text (`&H00FFFFFF`), soft black outer glow/shadow (`&H35000000` / `&H60000000`, `\blur1.8`).
4. **Transition Logic**: Complete semantic phrases (word-chunk logic), zero-frame cuts (no fade-ins), and rest cuts (screen empty during pauses). Secondary font: clean sans-serif (Poppins/Montserrat 28–32pt) for intro `Artist - Title (Lyrics)`.
5. **20-Minute Replay Loops**: 6 total playthroughs (1 original + 5 replays) with `Replay [k/5]` chapter cards.
6. **Slowed + Reverb**: 0.865x tape varispeed, 3s cathedral reverb, 15.5kHz tape shelf warmth.

## Step-by-Step Procedure to Add a New Song

1. **Setup Song Directory**:
   Create `songs/<id>_<Artist>_<Title>/` and place `audio.mp3`.
2. **Fetch Synced Lyrics**:
   Use `syncedlyrics.search("<Artist> - <Title>")` to save `lyrics.lrc`.
3. **Whisper Word Alignment**:
   Run `faster-whisper base.en` to save word-level timestamps to `whisper_words.txt`.
4. **Build ASS Subtitles**:
   Generate `lyrics_single.ass` and `lyrics_20min_loop.ass` with balanced 2-row couplets.
5. **Scenic Wallpaper**:
   Select or generate a 1920x1080 7clouds wallpaper with clean center reading space.
6. **FFmpeg Render**:
   Run render script with subtle `zoompan` and ASS filter.
7. **Quality Audit**:
   Extract test frames, verify contrast $> 10:1$, confirm margins $> 180$px.
8. **Update Guides**:
   Add track to `player.html` and append SEO metadata to `Fade_Replay_YouTube_Upload_Guide.txt`.
