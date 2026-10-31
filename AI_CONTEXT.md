# Fade Replay — Complete AI System Context & Project Memory

> **Purpose**: This document preserves the entire operational memory, creative decisions, technical standards, and chat history of the **Fade Replay** project. Any AI assistant or developer loading this repository on another device can read this document to understand exactly how the project works, what tools are used, and how to continue generating songs without losing context.

---

## 1. Project Background & Vision

**Fade Replay** is an automated aesthetic lyric video production pipeline developed to match and exceed the visual and algorithmic performance of top YouTube lyric channels:
- **7clouds** (clean anime cloudscapes, pure white handwritten typography, gentle zoompan).
- **Cakes & Eclairs** (subtle color grading, aesthetic pacing, romantic nostalgic themes).
- **Vibe Music** (modern pop hits, sing-along typography, high contrast).

The pipeline automates:
1. Audio acquisition and acoustic analysis.
2. Word-level timestamp alignment using local Whisper AI (`faster-whisper base.en`).
3. Couplet restructuring (strictly $\le 2$ rows, syllable-balanced, line-length capped).
4. Substation Alpha (`.ass`) rendering with custom styling.
5. Background art synthesis (scenic anime cloudscapes with negative central reading space).
6. FFmpeg video composition (subtle zoompan camera drift, film grain, audio fades).
7. Frame-accurate quality audits (text contrast ratio $> 10:1$, zero line clipping).
8. Interactive multi-track web showcase ([`player.html`](player.html)).
9. SEO metadata generation ([`Fade_Replay_YouTube_Upload_Guide.txt`](Fade_Replay_YouTube_Upload_Guide.txt)).

---

## 2. Key Aesthetic Formulas & Decisions Made in Chat

### Formula 1: Signature 7clouds Aesthetic Remaster
- **Problem solved in chat**: Previous iterations had clunky sliding artificial sprite clouds, heavy foreground blurs, or washed-out backgrounds where lyrics lost contrast.
- **The Solution**: 
  - Pure scenic open-sky anime wallpaper (Makoto Shinkai aesthetic) featuring rich twilight, indigo, and sunset afterglow clouds.
  - Zero foreground clutter: NO human figures, NO silhouettes, NO buildings, NO text on wallpaper.
  - Camera Motion: Smooth organic `zoompan` directly on the background image (`min(zoom+0.00010, 1.05)`), simulating a slow drone shot through the atmosphere.
  - Text: Handwritten `Patrick Hand` font, pure white (`&H00FFFFFF`), dark navy outline (`&H00101828`, border 3.8), and soft drop shadow (`&H80000000`, shadow 2.2).
  - Couplet Layout: Strictly $\le 2$ rows per couplet. Never wrap to 3 rows.

### Formula 2: Slowed + Reverb Brand Edition
- **Audio Engineering**:
  - Speed & Pitch: $0.865\times$ tape varispeed (both tempo and pitch scale down naturally, dropping pitch by $\approx 2.5$ semitones).
  - Reverb: 3.0-second decay Cathedral Reverb hall with soft pre-delay.
  - Warmth: 15.5 kHz high-shelf tape saturation to simulate analog tape nostalgia.
- **Subtitle Sync**:
  - All Whisper timestamps are scaled by $t' = t / 0.865$.
  - Hook card displays `Song Title (Slowed + Reverb)`.

### Formula 3: 20+ Minute 5-Time Replay Loop Edition
- **Why Top Channels Loop Songs 5 Times**:
  1. **YouTube Algorithm / Average View Duration (AVD)**: Study, homework, and sleep listeners keep extended loops playing in the background. While a 3-minute video averages 1.5–2.5 minutes of watch time, a 20-minute video routinely clocks **12–16 minutes AVD** (over $600\%$ increase), heavily triggering YouTube's recommendation engine.
  2. **Monetization (The 8-Minute Rule)**: YouTube allows mid-roll ads only on videos 8 minutes or longer. A 21-minute video comfortably supports 3 to 4 mid-roll ad slots, multiplying channel RPM by $3\times$ to $5\times$.
  3. **High Search Intent**: High organic search volume for terms like `"on repeat"`, `"5 times replay"`, `"20 minutes loop"`, and `"study loop"`.
- **Implementation in Fade Replay**:
  - Repeats the track 6 times total (1 original + 5 replays) for an optimal 20–22 minute runtime.
  - Subtitle events are mathematically looped: $t_{start}' = t_{start} + k \times T_{duration}$, $t_{end}' = t_{end} + k \times T_{duration}$ for $k \in \{0, 1, 2, 3, 4, 5\}$.
  - Dynamic Replay Progress Cards: Loops 2 through 6 introduce the track with `Artist • Replay [k/5]`.
  - Audio: Seamless looping via `ffmpeg -stream_loop 5 -i audio.mp3`.

---

## 3. Catalog of Engineered Songs (00 to 29)

| # | Artist & Title | Formats Available | Visual Theme |
| :--- | :--- | :--- | :--- |
| **00** | **Justin Bieber — That Should Be Me** | Single (3:36) + **20-Min 5x Replay (21:38)** | Twilight Heartbreak Clouds (Sapphire/Rose Glow) |
| **01** | ROSÉ & Bruno Mars — APT. | Single (2:49) + Spotify Glass | Fluffy Pastel Cotton-Candy Clouds |
| **02** | Lady Gaga & Bruno Mars — Die With A Smile | Single (4:11) + Spotify Glass | Celestial Twilight Skyline |
| **03** | Taylor Swift — The Fate of Ophelia | Single (4:12) + Spotify Glass | Dramatic Alpine Mountain Dawn |
| **04** | HUNTR/X — Golden | Single (3:45) | Golden Hour Celestial Overlook |
| **05** | Billie Eilish — BIRDS OF A FEATHER | Single (3:15) Pink Edition | Anime Pink Sunset Sky |
| **06** | Sabrina Carpenter — Espresso | Single (2:55) | Coastal Ocean & Soaring Birds |
| **07** | Benson Boone — Beautiful Things | Single (3:00) | Cherry Blossom Spring Pathway |
| **08** | Chappell Roan — Good Luck, Babe! | Single (3:38) | Summer Coastal Terrace |
| **09** | Teddy Swims — Lose Control | Single (3:30) | Retro 80s Neon Twilight Skyline |
| **10** | Ruth B. — Dandelions | Single (3:53) | Dandelion Wildflower Sunset Field |
| **11** | Justin Bieber — Favorite Girl | Single (4:16) | Sunset Street Flower Shop |
| **12** | Melanie Martinez — Play Date | Single (2:59) | Clean Celestial Night Sky |
| **13** | Stephen Sanchez — Until I Found You | Single (2:57) | Aesthetic Pink Twilight Sky |
| **14** | Justin Bieber — Lonely | Single (2:29) | Solitary Desert Twilight Horizon |
| **15** | Akon — Lonely | Single (3:55) | Starry Night Sunset Vista |
| **16** | Justin Bieber — Love Yourself | Single (3:53) Dark Edition | Acoustic Sunset Window Breeze |
| **17** | Katy Perry — The One That Got Away | Single (3:47) | Nostalgic Mustang Cliff Sunset |
| **18** | Coldplay — Yellow | Single (4:29) | Starry Night Coastal Beach |
| **19** | Coldplay — A Sky Full of Stars | Single (4:27) | Deep Cosmic Starlight Sky |
| **20** | Coldplay — Paradise | Single (4:38) | Twilight Dreamscape Clouds |
| **21** | Coldplay — Clocks | Single (5:07) | Celestial Cosmic Starlight |
| **22** | Billie Eilish & Khalid — lovely | Single (3:20) | Aurora Lake Twilight |
| **23** | OneRepublic — Counting Stars | Single (4:17) | Celestial Starfield Sky |
| **24** | Lord Huron — The Night We Met | Single (3:28) | Indigo Starry Forest Clearing |
| **25** | The Neighbourhood — Sweater Weather | Single (4:00) + Slowed Reverb (4:37) | Autumn Twilight Mist & Stars |
| **26** | Tom Odell — Another Love | Single (4:04) | Pastel Melancholic Sunset |
| **27** | Adele — Skyfall | Single (4:46) | Golden Hour Moody Ledge |
| **27b**| Joji — Glimpse of Us | Single (3:53) + Slowed Reverb (4:30) | Moody Indigo Twilight & Rain Ledge |
| **28** | yung kai — blue | Single (3:34) **7clouds Remaster** + Slowed (4:08) | Deep Sapphire Twilight Moonlight Clouds |
| **29** | Sia — Chandelier | Single (3:32) + Slowed Reverb (4:06) | Celestial Prism Bokeh & Penthouse Sky |

---

## 4. Dependencies & Environment Setup

On any new device or environment, ensure the following are installed:
```bash
# Python dependencies
pip install faster-whisper syncedlyrics pillow numpy

# FFmpeg must be available in PATH:
# Verify with: ffmpeg -version
```

---

## 5. Standard Song Generation Script Reference

To create a new song, follow the pattern established in `songs/00_Justin_Bieber_That_Should_Be_Me/build_ass.py` and `render_single.py`:

```python
# FFmpeg Render Filter Complex Pattern:
fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=4:allf=t+u,"
    f"fade=t=out:st={t_out}:d=2.5[v]"
)
```

To extract audit verification frames:
```bash
ffmpeg -y -ss 00:00:41.00 -i output.mp4 -vframes 1 audit_frame.png
```
Calculate contrast: Text peak luminance $> 250$, outline luminance $< 30$ (Contrast $> 10:1$).
