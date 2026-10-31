import subprocess
import time
import os

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
bg_sharp = f"{base}/light_clouds_sharp_1080.png"
bg_blur = f"{base}/light_clouds_blur_1080.png"
audio = f"{base}/songs/APT/audio.mp3"
ass_path = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/APT/lyrics_perfect_apt.ass"
fonts_dir = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
out_video = f"{base}/output/ROSE_Bruno_Mars_APT_Lyric_Video.mp4"
duration = "173.5"

print("Starting render of ROSÉ & Bruno Mars - APT. Lyric Video...")
t0 = time.time()

# Sharp on title 0-3s, smooth dissolve 3-5.5s, blurred remainder
filter_complex = (
    "[0:v][1:v]blend=all_expr='if(lte(T,2.8),A,if(between(T,2.8,5.5),A*(1-(T-2.8)/2.7)+B*(T-2.8)/2.7,B))',"
    f"subtitles={ass_path}:fontsdir={fonts_dir}[v]"
)

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-framerate", "30", "-t", duration, "-i", bg_sharp,
    "-loop", "1", "-framerate", "30", "-t", duration, "-i", bg_blur,
    "-i", audio,
    "-filter_complex", filter_complex,
    "-map", "[v]", "-map", "2:a",
    "-c:v", "libx264", "-preset", "faster", "-crf", "18", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest",
    out_video
]

p = subprocess.run(cmd, capture_output=True, text=True)
print(f"APT render finished in {time.time()-t0:.1f}s! Exit code: {p.returncode}")
if p.returncode != 0:
    print("FFmpeg error:", p.stderr[-1000:])
else:
    file_size_mb = os.path.getsize(out_video) / (1024 * 1024)
    print(f"Success! Output size: {file_size_mb:.2f} MB")
