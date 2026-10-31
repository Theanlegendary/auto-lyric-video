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
ass_path = song_dir / "lyrics_20min_loop.ass"
output_video = base / "videos" / "00_Justin_Bieber_That_Should_Be_Me_20Min_5x_Replay_Lyric_Video.mp4"

ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

NUM_LOOPS = 6 # 1 original + 5 replays
TRACK_DURATION = 216.48
TOTAL_DURATION = NUM_LOOPS * TRACK_DURATION # 1298.88s = 21m 38.88s
t_out = TOTAL_DURATION - 3.5

print("=" * 70)
print("RENDERING 20+ MINUTE 5-TIME REPLAY MASTERPIECE:")
print("Justin Bieber - That Should Be Me (5 Times Replay / 20+ Minutes Loop)")
print(f"Total Duration: {TOTAL_DURATION:.2f}s ({TOTAL_DURATION/60:.2f} minutes)")
print(f"Background: {bg_path.name}")
print(f"ASS Subtitles: {ass_path.name}")
print(f"Output Video: {output_video.name}")
print("=" * 70)

fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00008,1.04)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=4:allf=t+u,"
    f"fade=t=out:st={t_out:.2f}:d=3.5[v]"
)
af = f"afade=t=in:ss=0:d=1.5,afade=t=out:st={t_out:.2f}:d=3.5"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", str(TOTAL_DURATION), "-i", str(bg_path),
    "-stream_loop", "5", "-i", str(audio_path),
    "-t", str(TOTAL_DURATION),
    "-filter_complex", fc,
    "-map", "[v]",
    "-map", "1:a",
    "-af", af,
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "21",
    "-g", "50",
    "-keyint_min", "25",
    "-c:a", "aac",
    "-b:a", "256k",
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
print(f"\n20-MIN 5X REPLAY RENDER COMPLETE in {elapsed:.1f}s ({mb:.2f} MB)")

# Extract audit frames from across multiple loops
audit_specs = [
    ("00:00:04.00", "audit_bieber_20min_loop1_title.png", "Loop 1 (Original) Title Card"),
    ("00:00:41.00", "audit_bieber_20min_loop1_chorus.png", "Loop 1 Chorus: That should be me, this is so sad"),
    ("00:03:40.00", "audit_bieber_20min_loop2_replay1_title.png", "Loop 2 Title: Justin Bieber • Replay [1/5]"),
    ("00:07:54.00", "audit_bieber_20min_loop3_replay2_chorus.png", "Loop 3 (Replay 2) Chorus"),
    ("00:15:30.00", "audit_bieber_20min_loop5_replay4_verse.png", "Loop 5 (Replay 4) Verse"),
    ("00:21:20.00", "audit_bieber_20min_loop6_replay5_outro.png", "Loop 6 (Replay 5) Outro"),
]

for ss, fname, label in audit_specs:
    out_img = brain / fname
    cmd_f = ["ffmpeg", "-y", "-ss", ss, "-i", str(output_video), "-vframes", "1", str(out_img)]
    subprocess.run(cmd_f, check=True)
    print(f"Extracted audit frame: {fname} at {ss} - {label}")

print("\nAll 20-min loop audit frames ready for inspection.")
