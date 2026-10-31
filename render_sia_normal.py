import os
import sys
import time
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

song_dir = base / "songs" / "29_Sia_Chandelier"
bg_path = song_dir / "chandelier_blurred_master.png"
cloud_path = base / "seamless_color_clouds_3840.png"
lights_path = song_dir / "live_chandelier_lights.mp4"
audio_path = song_dir / "audio.mp3"
ass_path = song_dir / "lyrics_glowing_white.ass"
output_video = base / "videos" / "29_Sia_Chandelier_Lyric_Video.mp4"

ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

duration = 212.64
t_out = 210.14

print(f"============================================================")
print(f"RENDERING FULL MASTER VIDEO: 29. Sia - Chandelier (Normal 1.0x Mix)")
print(f"Audio Duration: {duration}s | Fade out: {t_out}s")
print(f"Background: {bg_path.name}")
print(f"Live Lights: {lights_path.name} (LAYERED BEHIND LYRICS)")
print(f"Live Clouds: {cloud_path.name} (LAYERED BEHIND LYRICS)")
print(f"ASS file: {ass_path.name}")
print(f"Output: {output_video.name}")
print(f"============================================================")

fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25[bg_pan];"
    f"[1:v]format=rgba[c_layer];"
    f"[bg_pan][c_layer]overlay=x='-mod(t*14, 1920)':y=15:format=auto[v_bg_cloud];"
    f"[2:v]format=yuv420p[lights];"
    f"[v_bg_cloud][lights]blend=all_mode=addition:all_opacity=0.35,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=5:allf=t+u,"
    f"fade=t=out:st={t_out}:d=2.5[v]"
)
af = f"afade=t=in:ss=0:d=1.5,afade=t=out:st={t_out}:d=2.5"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", str(duration), "-i", str(bg_path),
    "-loop", "1", "-t", str(duration), "-i", str(cloud_path),
    "-stream_loop", "-1", "-t", str(duration), "-i", str(lights_path),
    "-i", str(audio_path),
    "-filter_complex", fc,
    "-af", af,
    "-map", "[v]", "-map", "3:a",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "320k",
    "-t", str(duration),
    str(output_video)
]

t0 = time.time()
print("Starting FFmpeg render...")
proc = subprocess.run(cmd, capture_output=True, text=True)
t1 = time.time()

if proc.returncode != 0:
    print("Error during rendering:")
    print(proc.stderr[-2000:])
    sys.exit(1)

file_size_mb = os.path.getsize(output_video) / (1024 * 1024)
print(f"SUCCESS! Rendered in {t1 - t0:.1f}s")
print(f"Output File: {output_video}")
print(f"File Size: {file_size_mb:.2f} MB")
