# Fade Replay — AI Assistant Rules & Workflow Standards

> **Context**: This repository powers **Fade Replay**, an aesthetic music and lyric video brand inspired by top YouTube channels (7clouds, Cakes & Eclairs, Vibe Music). Whenever an AI assistant is chatting with a developer in this workspace, follow these mandatory rules and specifications.

---

## 1. Visual & Typography Formula (7clouds Standard)

- **Aesthetic**: Scenic anime cumulus clouds at twilight, dawn, or sunset (Makoto Shinkai inspired).
- **Negative Reading Space**: The central 60% of the frame MUST have clean, smooth sky gradients free of human silhouettes, buildings, ground clutter, or watermarks so pure white text remains 100% legible.
- **Font**: Primary font is **Patrick Hand** (`fonts/PatrickHand.ttf`).
  - Title Hook Card: 170–200pt, centered (`\pos(960,460)`), with subtle fade in/out (`\fad(500,400)`).
  - Couplet Subtitles: 96–102pt, centered (`\pos(960,490)`), with fast fade (`\fad(200,150)`).
- **Colors & Outline**:
  - Primary text: Pure White `&H00FFFFFF`
  - Outline: Deep Charcoal/Navy `&H00101828` with `Outline: 3.8`
  - Shadow: Soft drop shadow `&H80000000` with `Shadow: 2.2`
  - Contrast Ratio: Must maintain $\ge 10:1$ contrast against the sky.
- **Line Limit Rule**: Strictly $\le 2$ rows per couplet. Never wrap to 3 lines. Margins must exceed 180px on both sides.

---

## 2. Audio & Video Formats

1. **Normal 1.0x Full Mix**: Standard high-fidelity studio mix (`audio.mp3`).
2. **Slowed + Reverb Brand Edition**:
   - 0.865x Tape Varispeed ($tempo \times 0.865$, pitch drops $-2.5$ semitones).
   - 3.0s Cathedral Reverb Hall.
   - 15.5kHz Warm Tape Shelf EQ.
   - Subtitle timestamps scaled by $1 / 0.865$.
3. **20+ Minute 5-Time Replay Loop Edition**:
   - 6 total plays (1 original + 5 continuous replays).
   - Chapter title cards on loops 2–6 (`Artist • Replay [k/5]`).
   - Looped audio via `ffmpeg -stream_loop 5 -i audio.mp3`.
   - Optimized for YouTube watch time (AVD 12–16 min) and mid-roll ad monetization.

---

## 3. Directory Layout & Conventions

```
auto_lyric_video/
├── .gemini/rules.md              # These assistant guidelines
├── AI_CONTEXT.md                 # Full conversation & knowledge base memory
├── README.md                     # Project documentation & quick start
├── FADE_REPLAY_SPEC.md           # Engineering specifications & FFmpeg commands
├── SONG_CATALOG.md               # Tracking sheet for songs 00 to 29
├── Fade_Replay_YouTube_Upload_Guide.txt # SEO titles, chapters, timestamps, tags
├── player.html                   # Interactive multi-track player
├── fonts/                        # Font TTFs (PatrickHand, Poppins, etc.)
├── sounds/                       # Master audio MP3s
├── thumbnail/                    # 1920x1080 YouTube video thumbnails
├── stock_anime_bgs/              # Curated scenic wallpaper library
├── videos/                       # Rendered MP4 output destination
└── songs/
    └── <id>_<Artist>_<SongTitle>/
        ├── audio.mp3             # Song audio
        ├── lyrics.lrc            # Synced LRC
        ├── whisper_words.txt     # Word-level Whisper timestamps
        ├── lyrics_*.ass          # ASS subtitles (single, loop, slowed)
        ├── *_master.png          # 1920x1080 wallpaper
        ├── render_*.py           # Dedicated render script
        └── build_ass.py          # Couplet generator script
```

---

## 4. Standard Pipeline for Adding a New Song

1. **Setup Directory**: Create `songs/<id>_<Artist>_<Title>/` and place `audio.mp3`.
2. **Fetch LRC**: Use `syncedlyrics.search("<Artist> - <Title>")` to retrieve base timings.
3. **Whisper Word Alignment**: Run `faster-whisper base.en` to get precise acoustic word timestamps.
4. **Build ASS Subtitles**: Break text into 2-row couplets ($\le 38$ chars per line). Generate `.ass` file.
5. **Background Artwork**: Create or select a 1920x1080 scenic 7clouds sky wallpaper with clean center space.
6. **Render with FFmpeg**: Apply organic zoompan drift, ASS subtitle filter, and subtle grain.
7. **Verification Audit**: Extract test frames, verify contrast ratio $> 10:1$, confirm zero text clipping.
8. **Update Guides**: Append SEO metadata to `Fade_Replay_YouTube_Upload_Guide.txt` and add to `player.html`.

---

## 5. Coding & Execution Safety Rules on Windows

- **No Complex PowerShell Inline Python**: Never execute multiline python through `powershell -Command "python -c \"...\""` because quotation marks corrupt. Always write a `.py` file and execute `python script.py`.
- **UTF-8 Output**: Always include `sys.stdout.reconfigure(encoding='utf-8')` at the top of scripts.
- **FFmpeg Subtitle Path Escaping**: In ASS filter, escape colons: `ass_path.as_posix().replace(":", "\\\\:")`.
- **FFmpeg Frame Extraction**: Put `-ss` after `-i` when extracting audit frames from rendered `.mp4`.
- **Video Storage**: Do not commit large `.mp4` video files to git (ignored in `.gitignore`). Re-render on demand using the python render scripts.
