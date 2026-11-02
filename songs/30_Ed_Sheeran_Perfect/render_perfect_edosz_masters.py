import os
import sys
import time
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
song_dir = base / "songs" / "30_Ed_Sheeran_Perfect"
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

audio_path = song_dir / "audio_perfect_slowed_reverb.mp3"
ass_path = song_dir / "lyrics_edosz_slowed.ass"
ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

duration = 305.40
t_out = 302.40

editions = [
    {
        "name": "80% Sky / 20% Sea (Blue Filter)",
        "bg": song_dir / "perfect_80sky_20sea_bluefilter.png",
        "video": base / "videos" / "30_Ed_Sheeran_Perfect_80Sky_20Sea_BlueFilter_Lyric_Video.mp4",
        "desc": "80% Vast Azure Sky + 20% Soft Turquoise Sea with Ethereal Glow"
    },
    {
        "name": "Pink Mode (Cotton-Candy)",
        "bg": song_dir / "perfect_pink_master.png",
        "video": base / "videos" / "30_Ed_Sheeran_Perfect_Slowed_Reverb_Pink_Edition_Lyric_Video.mp4",
        "desc": "Pastel Pink Cotton-Candy Clouds with Edo SZ 7clouds Typography"
    },
    {
        "name": "Sunset Mode (Amber Dusk)",
        "bg": song_dir / "perfect_sunset_master.png",
        "video": base / "videos" / "30_Ed_Sheeran_Perfect_Slowed_Reverb_Sunset_Edition_Lyric_Video.mp4",
        "desc": "Warm Golden-Amber Dusk Clouds with Edo SZ 7clouds Typography"
    }
]

for ed in editions:
    print("=" * 70)
    print(f"RENDERING MASTER: Ed Sheeran - Perfect ({ed['name']} • Slowed + Reverb)")
    print(f"Theme: {ed['desc']}")
    print(f"Output: {ed['video'].name}")
    print("=" * 70)
    t0 = time.time()

    fc = (
        f"[0:v]format=yuv420p,"
        f"zoompan=z='min(zoom+0.00008,1.04)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
        f"fade=t=in:st=0:d=1.5,"
        f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
        f"noise=alls=3:allf=t+u,"
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
        "-crf", "18",
        "-g", "50",
        "-keyint_min", "25",
        "-c:a", "aac",
        "-b:a", "320k",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        str(ed["video"])
    ]

    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    dt = time.time() - t0
    if res.returncode == 0 and ed["video"].exists():
        sz = ed["video"].stat().st_size / (1024 * 1024)
        print(f"  [SUCCESS] Rendered {ed['video'].name} in {dt:.1f}s | Size: {sz:.2f} MB\n")
    else:
        print(f"  [ERROR] Render failed in {dt:.1f}s:\n{res.stderr[-500:]}\n")
