import os
import sys
import time
import subprocess
from pathlib import Path
from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
song_dir = base / "songs" / "30_Ed_Sheeran_Perfect"
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

audio_path = song_dir / "audio_perfect_slowed_reverb.mp3"
duration = 305.40
t_out = 302.40

editions = [
    {
        "name": "Pink Mode",
        "bg": song_dir / "perfect_pink_master.png",
        "ass": song_dir / "lyrics_pink_slowed.ass",
        "video": base / "videos" / "30_Ed_Sheeran_Perfect_Slowed_Reverb_Pink_Edition_Lyric_Video.mp4",
        "prefix": "audit_perfect_pink",
        "desc": "Pastel Pink Cotton-Candy Twilight Clouds"
    },
    {
        "name": "Sunset Mode",
        "bg": song_dir / "perfect_sunset_master.png",
        "ass": song_dir / "lyrics_sunset_slowed.ass",
        "video": base / "videos" / "30_Ed_Sheeran_Perfect_Slowed_Reverb_Sunset_Edition_Lyric_Video.mp4",
        "prefix": "audit_perfect_sunset",
        "desc": "Warm Golden-Amber & Coral Dusk Clouds"
    }
]

for ed in editions:
    print("=" * 70)
    print(f"RENDERING: 30. Ed Sheeran - Perfect ({ed['name']} • Slowed + Reverb)")
    print(f"Theme: {ed['desc']}")
    print(f"Background: {ed['bg'].name}")
    print(f"Subtitles: {ed['ass'].name}")
    print(f"Output: {ed['video'].name}")
    print("=" * 70)

    ass_escaped = ed["ass"].as_posix().replace(":", "\\\\:")

    fc = (
        f"[0:v]format=yuv420p,"
        f"zoompan=z='min(zoom+0.00008,1.04)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
        f"fade=t=in:st=0:d=1.5,"
        f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
        f"noise=alls=4:allf=t+u,"
        f"fade=t=out:st={t_out}:d=3.0[v]"
    )
    af = f"afade=t=in:ss=0:d=1.5,afade=t=out:st={t_out}:d=3.0"

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", str(duration), "-i", str(ed["bg"]),
        "-i", str(audio_path),
        "-filter_complex", fc,
        "-map", "[v]",
        "-map", "1:a",
        "-af", af,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "19",
        "-g", "50",
        "-keyint_min", "25",
        "-c:a", "aac",
        "-b:a", "256k",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        str(ed["video"])
    ]

    t0 = time.time()
    res = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
    elapsed = time.time() - t0

    if res.returncode != 0:
        print(f"RENDER FAILED with code {res.returncode}")
        print("\n".join(res.stderr.splitlines()[-30:]))
        sys.exit(1)

    mb = ed["video"].stat().st_size / (1024 * 1024)
    print(f"RENDER COMPLETE: {ed['video'].name} ({mb:.2f} MB, {elapsed:.1f}s)")

    # Extract audit frames
    audit_specs = [
        ("00:00:04.00", f"{ed['prefix']}_title.png", "Title Card: Perfect / Ed Sheeran"),
        ("00:00:25.00", f"{ed['prefix']}_verse.png", "Verse 1: Well, I found a girl / beautiful and sweet"),
        ("00:01:25.00", f"{ed['prefix']}_chorus.png", "Chorus: Barefoot on the grass / listening to our favorite song")
    ]

    for ss, fname, label in audit_specs:
        out_img = brain / fname
        cmd_f = ["ffmpeg", "-y", "-ss", ss, "-i", str(ed["video"]), "-vframes", "1", str(out_img)]
        subprocess.run(cmd_f, check=True)
        print(f"  Extracted: {fname} at {ss} - {label}")

        # Crop and analyze contrast
        im = Image.open(out_img)
        arr = np.array(im)
        crop = arr[350:750, 300:1620]
        crop_im = Image.fromarray(crop)
        crop_im.save(brain / f"crop_{fname}")

        r, g, b = crop[:, :, 0], crop[:, :, 1], crop[:, :, 2]
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        peak = np.percentile(lum, 99.5)
        outline = np.percentile(lum, 1.0)
        contrast = (peak + 0.05) / (outline + 0.05)
        print(f"    Contrast: {contrast:.1f}:1 (Peak: {peak:.1f}, Outline: {outline:.1f})")

print("\nALL RENDERS AND AUDITS COMPLETED SUCCESSFULLY!")
