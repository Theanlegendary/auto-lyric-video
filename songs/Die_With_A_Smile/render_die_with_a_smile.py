import subprocess
import time
import os
from PIL import Image, ImageFilter

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
song_dir = f"{base}/songs/Die_With_A_Smile"
bg_sharp = f"{base}/stock_anime_bgs/02_lofi_twilight_starry_night.png"
bg_blur = f"{song_dir}/twilight_blur.png"

# 1. Create soft 8px blur
img = Image.open(bg_sharp)
blurred = img.filter(ImageFilter.GaussianBlur(radius=8))
blurred.save(bg_blur)

audio = f"{song_dir}/audio.mp3"
ass_path = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/Die_With_A_Smile/lyrics.ass"
fonts_dir = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
out_video = f"{base}/output/Lady_Gaga_Bruno_Mars_Die_With_A_Smile_Lyric_Video.mp4"
duration = "251.8"

print("Starting render of Lady Gaga & Bruno Mars - Die With A Smile...")
t0 = time.time()

# Sharp on title 0-4.5s, smooth dissolve 4.5s to 7.2s, soft blur during vocals
filter_complex = (
    "[0:v][1:v]blend=all_expr='if(lte(T,4.5),A,if(between(T,4.5,7.2),A*(1-(T-4.5)/2.7)+B*(T-4.5)/2.7,B))',"
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
print(f"Die With A Smile render finished in {time.time()-t0:.1f}s! Exit code: {p.returncode}")
if p.returncode != 0:
    print("FFmpeg error:", p.stderr[-1000:])
else:
    file_size_mb = os.path.getsize(out_video) / (1024 * 1024)
    print(f"Success! Output size: {file_size_mb:.2f} MB")
