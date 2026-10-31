import os
import sys
import subprocess
import time
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
song_dir = base / "songs" / "16_Justin_Bieber_Love_Yourself"
out_video = base / "videos" / "16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4"
audio_path = song_dir / "audio.mp3"
master_bg = song_dir / "acoustic_sunset_blurred_master.png"
ass_path = song_dir / "lyrics_spotify.ass"

ass_escaped = ass_path.as_posix().replace(":", "\\\\:")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

print("Rendering master video for Song #16: Justin Bieber - Love Yourself...")
duration = 234.53
t_out = round(duration - 3.0, 2)

fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=5:allf=t+u,"
    f"fade=t=out:st={t_out}:d=3.0[v]"
)

af = f"afade=t=in:ss=0:d=1.8,afade=t=out:st={t_out}:d=3.0"

cmd_full = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", str(duration), "-i", str(master_bg),
    "-i", str(audio_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-map", "1:a",
    "-af", af,
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "18",
    "-c:a", "aac",
    "-b:a", "320k",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    str(out_video)
]

start_t = time.time()
res = subprocess.run(cmd_full, capture_output=True, text=True, errors='ignore')
elapsed = time.time() - start_t

if res.returncode == 0:
    size_mb = out_video.stat().st_size / (1024 * 1024)
    print(f"SUCCESS! Rendered master video {out_video.name} in {elapsed:.1f}s ({size_mb:.2f} MB)")
    
    # Extract audit frames from final video
    preview_frames = [
        ("00:00:04", "audit_16_love_yourself_title.png"),
        ("00:00:15", "audit_16_love_yourself_verse1.png"),
        ("00:00:43", "audit_16_love_yourself_prechorus.png"),
        ("00:01:03", "audit_16_love_yourself_chorus.png"),
        ("00:02:56", "audit_16_love_yourself_bridge.png"),
        ("00:03:45", "audit_16_love_yourself_outro.png"),
    ]
    
    for ss, fname in preview_frames:
        out_p = brain / fname
        cmd_f = [
            "ffmpeg", "-y",
            "-ss", ss,
            "-i", str(out_video),
            "-vframes", "1",
            str(out_p)
        ]
        subprocess.run(cmd_f, check=True)
        print(f"Rendered audit frame from video: {fname}")
else:
    print(f"FAILED with returncode {res.returncode}")
    print("\n".join(res.stderr.splitlines()[-30:]))
