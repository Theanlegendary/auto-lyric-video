#!/usr/bin/env python3
"""
Auto Lyric Video Generator
Creates aesthetic, synchronized lyric videos (in the style of Cakes & Eclairs, 7clouds, etc.)
from a YouTube URL, audio file, or song name.
"""

import os
import sys
import re
import json
import argparse
import subprocess
import urllib.request
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FONTS_DIR = BASE_DIR / "fonts"
OUTPUT_DIR = BASE_DIR / "output"

FONTS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_FONT_NAME = "Patrick Hand"
DEFAULT_FONT_URL = "https://github.com/google/fonts/raw/main/ofl/patrickhand/PatrickHand-Regular.ttf"
DEFAULT_FONT_FILE = FONTS_DIR / "PatrickHand.ttf"


def ensure_font():
    """Ensure the Patrick Hand font is present."""
    if not DEFAULT_FONT_FILE.exists():
        print(f"[*] Downloading aesthetic font ({DEFAULT_FONT_NAME})...")
        try:
            urllib.request.urlretrieve(DEFAULT_FONT_URL, str(DEFAULT_FONT_FILE))
            print("[+] Font downloaded.")
        except Exception as e:
            print(f"[!] Warning downloading font: {e}")


def to_ass_time(seconds: float) -> str:
    """Format seconds into ASS timestamp H:MM:SS.CC"""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def format_lyric_text(text: str) -> str:
    """
    Format lyric line to match the aesthetic two-line centered layout.
    Splits long lines naturally at commas or midpoints and converts to uppercase.
    """
    text = text.strip()
    if not text:
        return ""

    # Check for natural comma split
    if "," in text:
        idx = text.find(",")
        part1 = text[:idx].strip()
        part2 = text[idx + 1:].strip()
        if len(part1) >= 6 and len(part2) >= 6:
            return f"{part1.upper()}\\N{part2.upper()}"

    # Split long lines at midpoint
    words = text.split()
    if len(words) >= 5 or len(text) > 28:
        mid = len(words) // 2
        line1 = " ".join(words[:mid]).upper()
        line2 = " ".join(words[mid:]).upper()
        return f"{line1}\\N{line2}"

    return text.upper()


def fetch_youtube_audio_and_meta(url: str, work_dir: Path):
    """Download audio and metadata from a YouTube video using yt-dlp."""
    print(f"[*] Fetching metadata & audio from YouTube: {url}")
    out_tmpl = str(work_dir / "audio.%(ext)s")

    cmd = [
        "yt-dlp",
        "--dump-json",
        "-x",
        "--audio-format", "mp3",
        "-o", out_tmpl,
        url
    ]
    p = subprocess.run(cmd, capture_output=True, text=True, check=True)
    meta = json.loads(p.stdout.strip().splitlines()[0])
    
    title = meta.get("track") or meta.get("title", "Unknown Title")
    artist = meta.get("artist") or meta.get("uploader", "Unknown Artist")

    # Clean typical YouTube title noise like "Justin Bieber - That Should Be Me - Cakes & Eclairs"
    raw_title = meta.get("title", "")
    if " - " in raw_title:
        parts = [p.strip() for p in raw_title.split(" - ")]
        if len(parts) >= 2:
            artist = parts[0]
            title = parts[1]
            # Strip extra tags like "(Lyrics)" or channel names
            title = re.sub(r"[\(\[].*?[\)\]]", "", title).strip()

    audio_file = work_dir / "audio.mp3"
    return audio_file, artist, title, meta


def fetch_synced_lyrics(artist: str, title: str):
    """Fetch synced LRC lyrics from LRCLIB."""
    print(f"[*] Querying synced lyrics for '{title}' by '{artist}'...")
    try:
        url = "https://lrclib.net/api/get"
        params = {"artist_name": artist, "track_name": title}
        headers = {"User-Agent": "AutoLyricMaker/1.0"}
        r = requests.get(url, params=params, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if data.get("syncedLyrics"):
                print("[+] Found synced lyrics on LRCLIB!")
                return parse_lrc(data["syncedLyrics"])
        
        # Try search endpoint if exact match fails
        search_url = "https://lrclib.net/api/search"
        r = requests.get(search_url, params={"q": f"{artist} {title}"}, headers=headers, timeout=10)
        if r.status_code == 200:
            results = r.json()
            for res in results:
                if res.get("syncedLyrics"):
                    print(f"[+] Found synced lyrics via search: {res.get('trackName')}")
                    return parse_lrc(res["syncedLyrics"])
    except Exception as e:
        print(f"[!] Warning querying LRCLIB: {e}")
    return None


def parse_lrc(lrc_text: str):
    """Parse LRC format string into a list of (timestamp_seconds, text)."""
    lines = []
    time_regex = re.compile(r"\[(\d+):(\d+\.\d+)\]\s*(.*)")
    for line in lrc_text.splitlines():
        m = time_regex.match(line)
        if m:
            mins, secs, text = int(m.group(1)), float(m.group(2)), m.group(3).strip()
            timestamp = mins * 60 + secs
            if text:
                lines.append((timestamp, text))
    return lines


def transcribe_with_whisper(audio_path: Path):
    """Fallback speech-to-text with faster-whisper if no synced LRC lyrics exist."""
    print("[*] Running faster-whisper AI transcription for timestamps...")
    from faster_whisper import WhisperModel
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(audio_path), word_timestamps=True)
    lines = []
    for seg in segments:
        text = seg.text.strip()
        if text:
            lines.append((seg.start, text))
    return lines


def generate_ass(lines, title: str, artist: str, output_ass: Path, lead_in: float = 1.0):
    """
    Generate an ASS subtitle file with aesthetic fonts, positions, and fades.
    Includes a configurable lead-in (default 1.0s) so subtitles appear before the vocals start,
    making it easy for viewers to read and sing along on cue.
    """
    ass_header = f"""[Script Info]
Title: {title} - Lyric Video (Sing-Along Ready)
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,{DEFAULT_FONT_NAME},175,&H002A202A,&H000000FF,&H002A202A,&H80000000,1,0,0,0,95,115,3,0,1,1,1,5,50,50,50,1
Style: Lyric,{DEFAULT_FONT_NAME},120,&H002A202A,&H000000FF,&H002A202A,&H80000000,0,0,0,0,95,115,1,0,1,0.5,0.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = []
    
    # Pre-calculate sing-along timings with lead-in
    scheduled = []
    for i in range(len(lines)):
        t_vocal, text = lines[i]
        # Subtitle appears lead_in seconds before the vocals start
        t_sub_start = max(0.5, t_vocal - lead_in)
        if scheduled and t_sub_start < scheduled[-1]["end"]:
            prev_end = t_sub_start - 0.15
            if prev_end > scheduled[-1]["start"] + 1.2:
                scheduled[-1]["end"] = prev_end
            else:
                t_sub_start = scheduled[-1]["end"] + 0.10

        if i + 1 < len(lines):
            next_vocal = lines[i + 1][0]
            next_sub_start = next_vocal - lead_in
            diff = next_vocal - t_vocal
            if diff < 5.0:
                t_sub_end = max(t_sub_start + 1.5, next_sub_start - 0.15)
            else:
                words = len(text.split())
                t_sub_end = t_vocal + min(words * 0.45 + 1.5, 4.5)
        else:
            t_sub_end = t_vocal + 4.5

        scheduled.append({
            "start": t_sub_start,
            "end": t_sub_end,
            "text": text
        })

    # Opening title card (runs from 1s to ~1.5s before the first subtitle appears)
    first_sub = scheduled[0]["start"] if scheduled else 10.0
    title_end = max(3.0, min(first_sub - 1.5, 11.5))
    events.append(
        f"Dialogue: 0,0:00:01.00,{to_ass_time(title_end)},TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(600,600)}}{title.upper()}\\N{{\\fs75\\fsp4}}{artist.upper()}"
    )

    for item in scheduled:
        formatted = format_lyric_text(item["text"])
        start_str = to_ass_time(item["start"])
        end_str = to_ass_time(item["end"])
        events.append(
            f"Dialogue: 0,{start_str},{end_str},Lyric,,0,0,0,,{{\\pos(960,470)\\fad(200,200)}}{formatted}"
        )

    full_content = ass_header + "\n".join(events) + "\n"
    with open(output_ass, "w", encoding="utf-8") as f:
        f.write(full_content)
    print(f"[+] Generated subtitle file with {lead_in}s sing-along lead-in: {output_ass}")


def create_blurred_background(bg_path: Path, style: str = "spotify") -> Path:
    """Generate pre-computed blurred background based on selected style."""
    from PIL import Image, ImageFilter, ImageEnhance
    
    img = Image.open(str(bg_path))
    blur_path = bg_path.parent / f"bg_blur_{style}.png"

    if style == "dream":
        blur = img.filter(ImageFilter.GaussianBlur(radius=28))
    elif style == "lofi":
        blur = img.filter(ImageFilter.GaussianBlur(radius=22))
        enhancer = ImageEnhance.Color(blur)
        blur = enhancer.enhance(1.30)
    else:  # default 'spotify'
        blur = img.filter(ImageFilter.GaussianBlur(radius=32))
        blur = ImageEnhance.Brightness(blur).enhance(0.82)
        blur = ImageEnhance.Contrast(blur).enhance(1.15)

    blur.save(str(blur_path))
    return blur_path


def render_video(bg_image: Path, audio_file: Path, ass_file: Path, output_mp4: Path, soft_intro: float = 1.8, blur_style: str = "spotify"):
    """Render the final high-definition MP4 using FFmpeg with soft audio intro and background blur transition."""
    print(f"[*] Rendering final 1080p video with FFmpeg (Blur style: {blur_style})...")
    ass_escaped = str(ass_file).replace("\\", "/").replace(":", "\\:")
    fonts_escaped = str(FONTS_DIR).replace("\\", "/").replace(":", "\\:")

    audio_filters = []
    if soft_intro > 0:
        audio_filters.append(f"afade=t=in:ss=0:d={soft_intro}")
    audio_filter_arg = ",".join(audio_filters) if audio_filters else "anull"

    if blur_style and blur_style.lower() != "none":
        blur_bg = create_blurred_background(bg_image, blur_style.lower())
        # Smooth dissolve transition from sharp to blurred between 2.8s and 5.5s (2.7s duration)
        filter_complex = (
            "[0:v][1:v]blend=all_expr='if(lte(T,2.8),A,if(between(T,2.8,5.5),A*(1-(T-2.8)/2.7)+B*(T-2.8)/2.7,B))',"
            f"subtitles={ass_escaped}:fontsdir={fonts_escaped}[v]"
        )
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-framerate", "30", "-i", str(bg_image),
            "-loop", "1", "-framerate", "30", "-i", str(blur_bg),
            "-i", str(audio_file),
            "-filter_complex", filter_complex,
            "-map", "[v]", "-map", "2:a",
            "-af", audio_filter_arg,
            "-c:v", "libx264", "-preset", "faster", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            str(output_mp4)
        ]
    else:
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-framerate", "30", "-i", str(bg_image),
            "-i", str(audio_file),
            "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
            "-af", audio_filter_arg,
            "-c:v", "libx264", "-preset", "faster", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            str(output_mp4)
        ]

    subprocess.run(cmd, check=True)
    print(f"[+] Successfully exported lyric video to: {output_mp4}")


def main():
    parser = argparse.ArgumentParser(description="Create aesthetic lyric video automatically.")
    parser.add_argument("--url", help="YouTube video URL")
    parser.add_argument("--artist", help="Artist name", default="")
    parser.add_argument("--title", help="Song title", default="")
    parser.add_argument("--audio", help="Local audio file path (mp3/wav)")
    parser.add_argument("--bg", help="Background image path (1920x1080)")
    parser.add_argument("--output", help="Output MP4 file path")
    parser.add_argument("--lead-in", type=float, default=1.0, help="Seconds before vocals start to display lyrics (default: 1.0s for singing along)")
    parser.add_argument("--soft-intro", type=float, default=1.8, help="Seconds for soft audio intro fade-in (default: 1.8s)")
    parser.add_argument("--blur-style", choices=["spotify", "dream", "lofi", "none"], default="spotify", help="Background blur style (default: spotify)")
    args = parser.parse_args()

    ensure_font()

    work_dir = BASE_DIR / "temp"
    work_dir.mkdir(parents=True, exist_ok=True)

    if args.url:
        audio_path, artist, title, _ = fetch_youtube_audio_and_meta(args.url, work_dir)
        if args.artist:
            artist = args.artist
        if args.title:
            title = args.title
    elif args.audio:
        audio_path = Path(args.audio)
        artist = args.artist or "Unknown Artist"
        title = args.title or audio_path.stem
    else:
        print("[!] Error: Either --url or --audio must be provided.")
        sys.exit(1)

    print(f"[+] Target: '{title}' by '{artist}'")

    # Synced lyrics
    lyrics = fetch_synced_lyrics(artist, title)
    if not lyrics:
        print("[*] No LRC found online. Falling back to Whisper speech-to-text...")
        lyrics = transcribe_with_whisper(audio_path)

    # Subtitle ASS file
    ass_path = work_dir / "lyrics.ass"
    generate_ass(lyrics, title, artist, ass_path, lead_in=args.lead_in)

    # Background image
    if args.bg and Path(args.bg).exists():
        bg_path = Path(args.bg)
    else:
        bg_path = BASE_DIR / "clean_bg_1080.png"
        if not bg_path.exists():
            print("[*] Clean background image not found, using default pastel background.")
            # Create a fallback pastel sunset image if missing
            from PIL import Image
            img = Image.new("RGB", (1920, 1080), (255, 182, 193))
            img.save(str(bg_path))

    # Output file
    safe_name = re.sub(r"[^\w\-_\. ]", "_", f"{artist}_{title}_Lyric_Video.mp4")
    out_path = Path(args.output) if args.output else OUTPUT_DIR / safe_name

    render_video(bg_path, audio_path, ass_path, out_path, soft_intro=args.soft_intro, blur_style=args.blur_style)
    print("\n" + "=" * 50)
    print(f"🎉 LYRIC VIDEO READY: {out_path}")
    print("=" * 50)


if __name__ == "__main__":
    main()
