#!/usr/bin/env python3
"""
Spotify Modern Glass Edition Renderer
Applies the exact winning formula from Justin_Bieber_That_Should_Be_Me_Spotify_Glass:
1. Sharp intro title card (0.0s -> 2.8s - 4.5s)
2. Smooth crossfade dissolve over 2.7s into pre-computed Spotify Glass frosted blur
   (GaussianBlur radius=32, Brightness 0.82, Contrast 1.15)
3. Full duration glassmorphic background for maximum lyric legibility
4. Centered 2-row couplets with sing-along timing
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
glass_dir = BASE_DIR / "spotify_glass_bgs"

SONGS = [
    {
        "id": "dwas",
        "title": "Die With A Smile",
        "artist": "Lady Gaga & Bruno Mars",
        "folder": "Die_With_A_Smile",
        "bg_sharp": BASE_DIR / "stock_anime_bgs" / "02_lofi_twilight_starry_night.png",
        "bg_glass": glass_dir / "bg_spotify_glass_dwas.png",
        "preset": "cinematic",
        "dissolve_start": 4.5,
        "dissolve_end": 7.2,
        "out_file": output_dir / "Lady_Gaga_Bruno_Mars_Die_With_A_Smile_Spotify_Glass.mp4"
    },
    {
        "id": "ophelia",
        "title": "The Fate of Ophelia",
        "artist": "Taylor Swift",
        "folder": "Taylor_Swift_The_Fate_of_Ophelia",
        "bg_sharp": BASE_DIR / "stock_anime_bgs" / "03_anime_rooftop_sunset_skyline.png",
        "bg_glass": glass_dir / "bg_spotify_glass_ophelia.png",
        "preset": "cinematic",
        "dissolve_start": 5.0,
        "dissolve_end": 7.8,
        "out_file": output_dir / "Taylor_Swift_The_Fate_of_Ophelia_Spotify_Glass.mp4"
    },
    {
        "id": "apt",
        "title": "APT.",
        "artist": "ROSÉ & Bruno Mars",
        "folder": "APT",
        "bg_sharp": BASE_DIR / "light_clouds_sharp_1080.png",
        "bg_glass": glass_dir / "bg_spotify_glass_apt.png",
        "preset": "indie",
        "dissolve_start": 2.8,
        "dissolve_end": 5.5,
        "out_file": output_dir / "ROSE_Bruno_Mars_APT_Spotify_Glass.mp4"
    }
]


def render_spotify_glass(song_cfg: dict):
    print("\n" + "=" * 55)
    print(f"Rendering Spotify Modern Glass: {song_cfg['title']} by {song_cfg['artist']}")
    print("=" * 55)

    fdir = BASE_DIR / "songs" / song_cfg["folder"]
    lrc_path = fdir / "lyrics.lrc"
    audio_path = fdir / "audio.mp3"
    ass_path = fdir / f"lyrics_spotify_glass_{song_cfg['preset']}.ass"

    # 1. Generate Subtitle using Spotify Glass Styling (Cormorant Garamond or DM Sans)
    engine.generate_ass_file(
        lrc_path=lrc_path,
        out_ass_path=ass_path,
        bg_image_path=song_cfg["bg_glass"],
        title=song_cfg["title"],
        artist=song_cfg["artist"],
        preset_key=song_cfg["preset"],
        vertical_ratio=0.60
    )
    print(f"[OK] Subtitle generated: {ass_path.name}")

    # 2. Get Audio Duration
    p_probe = subprocess.run([
        "ffmpeg", "-i", str(audio_path)
    ], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors="ignore")
    m_dur = re.search(r"Duration:\s*(\d{2}):(\d{2}):(\d{2}\.\d+)", p_probe.stderr)
    duration = 216.0
    if m_dur:
        duration = int(m_dur.group(1)) * 3600 + int(m_dur.group(2)) * 60 + float(m_dur.group(3))

    render_dur = f"{duration:.2f}"
    out_video = song_cfg["out_file"]
    ds = song_cfg["dissolve_start"]
    de = song_cfg["dissolve_end"]
    dur_trans = de - ds

    print(f"[*] Rendering {render_dur}s video with Spotify Glass dissolve to: {out_video.name}")
    t0 = time.time()

    ass_esc = str(ass_path).replace("\\", "/").replace(":", "\\\\:")
    fonts_esc = str(fonts_dir).replace("\\", "/").replace(":", "\\\\:")

    # High-performance hardware-accelerated xfade from sharp to glass blur + subtitles
    filter_complex = (
        f"[0:v][1:v]xfade=transition=fade:duration={dur_trans:.2f}:offset={ds:.2f}[bg];"
        f"[bg]subtitles={ass_esc}:fontsdir={fonts_esc}[v]"
    )

    cmd = [
        "ffmpeg", "-nostdin", "-y",
        "-loop", "1", "-framerate", "30", "-t", f"{de:.2f}", "-i", str(song_cfg["bg_sharp"]),
        "-loop", "1", "-framerate", "30", "-t", render_dur, "-i", str(song_cfg["bg_glass"]),
        "-i", str(audio_path),
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "2:a",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "19", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(out_video)
    ]

    p = subprocess.run(cmd, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    if p.returncode == 0:
        size_mb = out_video.stat().st_size / (1024 * 1024)
        print(f"[OK] Full video finished in {time.time()-t0:.1f}s | Size: {size_mb:.2f} MB")
        # Also copy to root project folder for instant playback
        root_copy = BASE_DIR / out_video.name
        import shutil
        shutil.copy2(out_video, root_copy)
        print(f"[OK] Copied to root: {root_copy.name}")
        return True
    else:
        print("[!] FFmpeg error:", p.stderr[-800:])
        return False


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--song", type=str, default="dwas")
    args = parser.parse_args()

    target = next((s for s in SONGS if s["id"] == args.song), SONGS[0])
    render_spotify_glass(target)
