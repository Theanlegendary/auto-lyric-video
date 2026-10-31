#!/usr/bin/env python3
"""
Batch Remastering Script using the New Typography & Layout Engine.
Generates pristine 1080p aesthetic lyric videos for all 5 songs:
- Style C: DM Sans Medium (Indie Aesthetic, soft white #F7F5F2, wider tracking, subtle shadow)
- Vertical position: 60% height (Y = 648px)
- Display max 2 lines at once (Couplets)
- Zero overlaps
- Gentle upward settle animation (+12px -> 0px over 300ms) with smooth opacity fade
"""

import sys
import os
import re
import time
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))
from lyric_engine import LyricLayoutEngine

engine = LyricLayoutEngine(1920, 1080)
fonts_dir = BASE_DIR / "fonts"
output_dir = BASE_DIR / "output"
output_dir.mkdir(parents=True, exist_ok=True)

SONGS_CONFIG = [
    {
        "id": "ophelia",
        "folder": "Taylor_Swift_The_Fate_of_Ophelia",
        "title": "The Fate of Ophelia",
        "artist": "Taylor Swift",
        "preset": "indie",
        "bg_sharp": BASE_DIR / "stock_anime_bgs" / "03_anime_rooftop_sunset_skyline.png",
        "bg_blur": BASE_DIR / "songs" / "Taylor_Swift_The_Fate_of_Ophelia" / "bg_blur.png",
        "out_name": "Taylor_Swift_The_Fate_of_Ophelia_Remastered_Indie.mp4",
        "vocal_start": 11.0,
        "dissolve_start": 5.0,
        "dissolve_end": 7.8
    },
    {
        "id": "apt",
        "folder": "APT",
        "title": "APT.",
        "artist": "ROSA% & Bruno Mars",
        "preset": "indie",
        "bg_sharp": BASE_DIR / "light_clouds_sharp_1080.png",
        "bg_blur": BASE_DIR / "light_clouds_blur_1080.png",
        "out_name": "ROSE_Bruno_Mars_APT_Remastered_Indie.mp4",
        "vocal_start": 0.1,
        "dissolve_start": 2.8,
        "dissolve_end": 5.5
    },
    {
        "id": "die_with_a_smile",
        "folder": "Die_With_A_Smile",
        "title": "Die With A Smile",
        "artist": "Lady Gaga & Bruno Mars",
        "preset": "cinematic",  # Cormorant Garamond for sad ballad
        "bg_sharp": BASE_DIR / "stock_anime_bgs" / "02_lofi_twilight_starry_night.png",
        "bg_blur": BASE_DIR / "songs" / "Die_With_A_Smile" / "twilight_blur.png",
        "out_name": "Lady_Gaga_Bruno_Mars_Die_With_A_Smile_Remastered.mp4",
        "vocal_start": 7.8,
        "dissolve_start": 4.5,
        "dissolve_end": 7.2
    },
    {
        "id": "golden",
        "folder": "HUNTR_X_Golden",
        "title": "Golden",
        "artist": "HUNTR/X (KPop Demon Hunters)",
        "preset": "modern",  # Inter Medium
        "bg_sharp": BASE_DIR / "stock_anime_bgs" / "01_makoto_shinkai_clouds.png",
        "bg_blur": BASE_DIR / "stock_anime_bgs" / "01_makoto_shinkai_clouds_blur.png",
        "out_name": "HUNTR_X_Golden_Remastered.mp4",
        "vocal_start": 12.0,
        "dissolve_start": 5.0,
        "dissolve_end": 7.8
    },
    {
        "id": "birds_of_a_feather",
        "folder": "Billie_Eilish_BIRDS_OF_A_FEATHER",
        "title": "BIRDS OF A FEATHER",
        "artist": "Billie Eilish",
        "preset": "indie",
        "bg_sharp": BASE_DIR / "stock_anime_bgs" / "01_makoto_shinkai_clouds.png",
        "bg_blur": BASE_DIR / "stock_anime_bgs" / "01_makoto_shinkai_clouds_blur.png",
        "out_name": "Billie_Eilish_BIRDS_OF_A_FEATHER_Remastered.mp4",
        "vocal_start": 4.0,
        "dissolve_start": 3.0,
        "dissolve_end": 5.5
    }
]


def render_song(song_cfg: dict, preview_only: bool = False, preview_seconds: float = 30.0):
    folder_dir = BASE_DIR / "songs" / song_cfg["folder"]
    lrc_path = folder_dir / "lyrics.lrc"
    audio_path = folder_dir / "audio.mp3"
    ass_path = folder_dir / f"lyrics_remastered_{song_cfg['preset']}.ass"

    print(f"\n==================================================")
    print(f"Processing: {song_cfg['title']} by {song_cfg['artist']}")
    print(f"Preset: {song_cfg['preset']} | Vertical: 60%")

    # 1. Generate ASS subtitle file with Adaptive Contrast & Pro Title
    engine.generate_ass_file(
        lrc_path=lrc_path,
        out_ass_path=ass_path,
        bg_image_path=song_cfg["bg_sharp"],
        title=song_cfg["title"],
        artist=song_cfg["artist"],
        preset_key=song_cfg["preset"],
        vertical_ratio=0.60,
        color_mode=song_cfg.get("color_mode", "auto")
    )
    print(f"[+] Generated subtitle: {ass_path.name}")

    # 2. Get Audio Duration via ffmpeg
    p_probe = subprocess.run([
        "ffmpeg", "-i", str(audio_path)
    ], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors="ignore")
    m_dur = re.search(r"Duration:\s*(\d{2}):(\d{2}):(\d{2}\.\d+)", p_probe.stderr)
    duration = 180.0
    if m_dur:
        duration = int(m_dur.group(1)) * 3600 + int(m_dur.group(2)) * 60 + float(m_dur.group(3))

    if preview_only:
        render_duration = str(preview_seconds)
        out_video = output_dir / f"PREVIEW_{song_cfg['out_name']}"
    else:
        render_duration = f"{duration:.2f}"
        out_video = output_dir / song_cfg["out_name"]

    print(f"[*] Rendering to {out_video.name} (Duration: {render_duration}s)...")
    t0 = time.time()

    # Escape paths for FFmpeg filter_complex on Windows
    ass_esc = str(ass_path).replace("\\", "/").replace(":", "\\\\:")
    fonts_esc = str(fonts_dir).replace("\\", "/").replace(":", "\\\\:")

    ds = song_cfg["dissolve_start"]
    de = song_cfg["dissolve_end"]
    dur_trans = de - ds

    # High-performance hardware-optimized xfade dissolve + subtitle overlay
    filter_complex = (
        f"[0:v][1:v]xfade=transition=fade:duration={dur_trans:.2f}:offset={ds:.2f}[bg];"
        f"[bg]subtitles={ass_esc}:fontsdir={fonts_esc}[v]"
    )

    cmd = [
        "ffmpeg", "-nostdin", "-y",
        "-loop", "1", "-framerate", "30", "-t", f"{de:.2f}", "-i", str(song_cfg["bg_sharp"]),
        "-loop", "1", "-framerate", "30", "-t", render_duration, "-i", str(song_cfg["bg_blur"]),
        "-i", str(audio_path),
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "2:a",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "19", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(out_video)
    ]

    p = subprocess.run(cmd, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    if p.returncode != 0:
        print(f"[!] FFmpeg error: {p.stderr[-800:]}")
        return False
    else:
        size_mb = out_video.stat().st_size / (1024 * 1024)
        print(f"[✓] Render finished in {time.time()-t0:.1f}s | Output: {size_mb:.2f} MB")
        return True


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Render all 5 songs")
    parser.add_argument("--song", type=str, default="ophelia", help="Single song id")
    parser.add_argument("--preview", action="store_true", help="Render 30s preview only")
    args = parser.parse_args()

    if args.all:
        for s in SONGS_CONFIG:
            render_song(s, preview_only=args.preview)
    else:
        target = next((s for s in SONGS_CONFIG if s["id"] == args.song), SONGS_CONFIG[0])
        render_song(target, preview_only=args.preview)
