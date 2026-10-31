---
name: fade-replay
description: >-
  Use this skill to produce aesthetic lyric videos in the 7clouds style, generate 20-minute 5-time replay study loops, apply slowed+reverb audio effects, or manage the Fade Replay 30-song music pipeline.
---

# Fade Replay — Automated Lyric Video Skill

Use this skill whenever creating, remastering, auditing, or managing aesthetic lyric videos.

## Core Rules

1. **7clouds Simplicity**: Pure scenic anime clouds at twilight/sunset. No character silhouettes, no ground clutter. Open negative space in the center.
2. **Couplets**: Strictly $\le 2$ rows per couplet. Never wrap to 3 lines.
3. **Typography**: Patrick Hand font, pure white text (`&H00FFFFFF`), dark charcoal border (`3.8`), soft drop shadow (`2.2`). Contrast $\ge 10:1$.
4. **20-Minute Replay Loops**: 6 total playthroughs (1 original + 5 replays) with `Replay [k/5]` chapter cards.
5. **Slowed + Reverb**: 0.865x tape varispeed, 3s cathedral reverb, 15.5kHz tape shelf warmth.

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
