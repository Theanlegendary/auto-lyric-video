# Fade Replay — Automated 7clouds Aesthetic Lyric Video Pipeline

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-7.1-green.svg)](https://ffmpeg.org/)
[![faster-whisper](https://img.shields.io/badge/Whisper-AI%20Alignment-orange.svg)](https://github.com/SYSTRAN/faster-whisper)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

**Fade Replay** is a complete, automated aesthetic music and lyric video creation pipeline engineered to match the viral quality of top YouTube channels like **7clouds**, **Cakes & Eclairs**, and **Vibe Music**.

It generates 1080p 60fps/25fps videos with synchronized handwritten typography, breathtaking anime cloudscapes, frame-accurate Whisper word-level alignment, and extended 20+ minute 5-time replay study loops.

---

## ✨ Features

- **☁️ Signature 7clouds Cloudscape Aesthetic**: Pure scenic Makoto Shinkai anime cloudscapes at twilight, dawn, and sunset with zero distracting foreground clutter and guaranteed negative space for reading.
- **✍️ High-Contrast Handwritten Typography**: Built with `Patrick Hand` and `Poppins` fonts, pure white fill (`&H00FFFFFF`), deep charcoal outline (`&H00101828`), and soft drop shadows ($> 10:1$ contrast ratio).
- **📏 Strictly $\le 2$ Rows per Couplet**: Whisper word timestamps guarantee natural phrasing, syllable balance, and zero text truncation across all screen resolutions.
- **🔁 20+ Minute 5-Time Replay Loop Engine**: Mathematically loops audio and subtitles 6 times (1 original + 5 replays) with dynamic progress hook cards (`Replay [1/5]` to `[5/5]`) to maximize YouTube Average View Duration (AVD) and unlock mid-roll monetization.
- **🎧 Slowed + Reverb Varispeed Engine**: Full 0.865x tape varispeed pitch shift, 3-second cathedral reverb hall, and 15.5 kHz analog tape shelf EQ.
- **🎬 Interactive Showcase Player**: Launch [`player.html`](player.html) in any browser to preview and audition all 30 songs and variations instantly.
- **📑 YouTube SEO Automation**: Auto-generates upload-ready titles, timestamps, chapters, and tags in [`Fade_Replay_YouTube_Upload_Guide.txt`](Fade_Replay_YouTube_Upload_Guide.txt).

---

## 🚀 Quick Start

### 1. Requirements

Ensure you have **Python 3.10+** and **FFmpeg** installed and accessible in your system `PATH`:

```bash
# Verify FFmpeg
ffmpeg -version

# Install Python packages
pip install faster-whisper syncedlyrics pillow numpy
```

### 2. Audition the Songs

Open [`player.html`](player.html) in your browser:
```bash
# Windows
start player.html

# macOS
open player.html

# Linux
xdg-open player.html
```

### 3. Render a Song

To render any song in the catalog, navigate to its folder and run its render script:

```bash
# Render Single 1x Edition of That Should Be Me
python songs/00_Justin_Bieber_That_Should_Be_Me/render_single.py

# Render 20+ Minute 5x Replay Loop Edition
python songs/00_Justin_Bieber_That_Should_Be_Me/render_20min_loop.py

# Render yung kai - blue (7clouds Perfect Twilight Remaster)
python render_yungkai_7clouds.py
```

The rendered video will be saved in `videos/`.

---

## 📁 Repository Structure

```
.
├── .gemini/
│   └── rules.md                  # Automatic AI Assistant rules for Antigravity
├── AI_CONTEXT.md                 # Complete historical memory & prompt guidelines
├── FADE_REPLAY_SPEC.md           # Technical equations, ASS styles, and FFmpeg filters
├── SONG_CATALOG.md               # Master tracker for Songs 00 to 29
├── Fade_Replay_YouTube_Upload_Guide.txt # SEO titles, descriptions, chapters, tags
├── player.html                   # Multi-track HTML5 video player
├── fonts/                        # TrueType fonts (Patrick Hand, Poppins, etc.)
├── sounds/                       # Master audio files
├── thumbnail/                    # YouTube 1080p video thumbnails
├── stock_anime_bgs/              # Curated cloudscape wallpapers
├── videos/                       # Rendered output destination (git-ignored)
└── songs/                        # Individual song workspaces
    ├── 00_Justin_Bieber_That_Should_Be_Me/
    ├── 28_yung_kai_blue/
    ├── 29_Sia_Chandelier/
    └── ... (30 songs total)
```

---

## 🤖 For AI Assistants & Collaborators

If you are an AI assistant (Google Antigravity, Claude, ChatGPT, Cursor) loaded into this repository on another device:
- **Read [`AI_CONTEXT.md`](AI_CONTEXT.md)** for complete project history, design decisions, and chat context.
- **Read [`.gemini/rules.md`](.gemini/rules.md)** for formatting rules, ASS subtitle parameters, and coding constraints.
- **Read [`FADE_REPLAY_SPEC.md`](FADE_REPLAY_SPEC.md)** for FFmpeg filter pipelines and acoustic Whisper alignment scripts.

---

## 📄 License

MIT License — see LICENSE for details.
