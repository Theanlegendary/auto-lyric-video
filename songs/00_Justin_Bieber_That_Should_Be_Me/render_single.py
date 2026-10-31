import os
import sys
import time
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

song_dir = base / "songs" / "00_Justin_Bieber_That_Should_Be_Me"
bg_path = song_dir / "that_should_be_me_7clouds_master.png"
audio_path = song_dir / "audio.mp3"
ass_path = song_dir / "lyrics_single.ass"
output_video = base / "videos" / "00_Justin_Bieber_That_Should_Be_Me_Lyric_Video.mp4"

ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

duration = 216.48
t_out = 213.98

print("=" * 60)
print("RENDERING 7CLOUDS SINGLE EDITION: Justin Bieber - That Should Be Me")
print(f"Background: {bg_path.name}")
print(f"ASS Subtitles: {ass_path.name}")
print(f"Output Video: {output_video.name}")
print("=" * 60)

fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=4:allf=t+u,"
    f"fade=t=out:st={t_out}:d=2.5[v]"
)
af = f"afade=t=in:ss=0:d=1.5,afade=t=out:st={t_out}:d=2.5"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", str(duration), "-i", str(bg_path),
    "-i", str(audio_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-map", "1:a",
    "-af", af,
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "18",
    "-g", "50",
    "-keyint_min", "25",
    "-c:a", "aac",
    "-b:a", "320k",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    str(output_video)
]

t0 = time.time()
res = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
elapsed = time.time() - t0

if res.returncode != 0:
    print(f"RENDER FAILED with code {res.returncode}")
    print("\n".join(res.stderr.splitlines()[-30:]))
    sys.exit(1)

mb = output_video.stat().st_size / (1024 * 1024)
print(f"\nSINGLE EDITION RENDER COMPLETE in {elapsed:.1f}s ({mb:.2f} MB)")

# Extract audit frames
audit_specs = [
    ("00:00:03.50", "audit_bieber_single_title.png", "Title Card: That Should Be Me / Justin Bieber"),
    ("00:00:20.00", "audit_bieber_single_verse.png", "Verse 1: Do you do what you did / when you did with me?"),
    ("00:00:41.00", "audit_bieber_single_chorus.png", "Chorus: That should be me, this is so sad / That should be me, that should be me"),
    ("00:02:08.00", "audit_bieber_single_bridge.png", "Bridge: I need to know / should I fight for love or disarm?"),
]

for ss, fname, label in audit_specs:
    out_img = brain / fname
    cmd_f = ["ffmpeg", "-y", "-ss", ss, "-i", str(output_video), "-vframes", "1", str(out_img)]
    subprocess.run(cmd_f, check=True)
    print(f"Extracted audit frame: {fname} at {ss} - {label}")

print("\nAudit frames ready for inspection.")
