import os
import sys
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
song_dir = base / "songs" / "29_Sia_Chandelier"

bg_path = song_dir / "chandelier_blurred_master.png"
cloud_path = base / "seamless_color_clouds_3840.png"
lights_path = song_dir / "live_chandelier_lights.mp4"
ass_path = song_dir / "lyrics_glowing_white.ass"
audio_path = song_dir / "audio.mp3"

fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

out_test = song_dir / "test_layering.mp4"

# Render 6 seconds starting at 35.0s (Chorus: I'm gonna swing from the chandelier)
duration = 6.0
fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25[bg_pan];"
    f"[1:v]format=rgba[c_layer];"
    f"[bg_pan][c_layer]overlay=x='-mod(t*14, 1920)':y=15:format=auto[v_bg_cloud];"
    f"[2:v]format=yuv420p[lights];"
    f"[v_bg_cloud][lights]blend=all_mode=addition:all_opacity=0.35[v_live];"
    f"[v_live]subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=5:allf=t+u[v]"
)

cmd = [
    "ffmpeg", "-y",
    "-ss", "35.0", "-t", str(duration), "-loop", "1", "-i", str(bg_path),
    "-ss", "35.0", "-t", str(duration), "-loop", "1", "-i", str(cloud_path),
    "-stream_loop", "-1", "-t", str(duration), "-i", str(lights_path),
    "-ss", "35.0", "-t", str(duration), "-i", str(audio_path),
    "-filter_complex", fc,
    "-map", "[v]", "-map", "3:a",
    "-c:v", "libx264", "-preset", "ultrafast", "-crf", "18", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    "-t", str(duration),
    str(out_test)
]

print("Running test render command...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("FFmpeg error:", res.stderr)
else:
    print("Test render successful:", out_test)
    frame_audit = brain / "test_sia_layering_frame.png"
    subprocess.run([
        "ffmpeg", "-y", "-ss", "2.5", "-i", str(out_test),
        "-vframes", "1", str(frame_audit)
    ], capture_output=True)
    print("Saved audit frame to:", frame_audit)
