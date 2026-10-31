import subprocess
import time

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
bg_sharp = f"{base}/new_bgs/bg_pink_sunset_island.jpg"
bg_blur = f"{base}/new_bgs/subtle_blur_bg_pink_sunset_island.jpg"
audio = f"{base}/audio.mp3"
ass_path = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/lyrics_bigger.ass"
fonts_dir = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
out_clip = f"{base}/preview_fresh_bg_bigger_text.mp4"

# Blend from sharp (A) to subtle blur (B) between 2.8s and 5.5s
filter_complex = (
    "[0:v][1:v]blend=all_expr='if(lte(T,2.8),A,if(between(T,2.8,5.5),A*(1-(T-2.8)/2.7)+B*(T-2.8)/2.7,B))',"
    f"subtitles={ass_path}:fontsdir={fonts_dir}[v]"
)

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-framerate", "30", "-t", "18", "-i", bg_sharp,
    "-loop", "1", "-framerate", "30", "-t", "18", "-i", bg_blur,
    "-ss", "0", "-t", "18", "-i", audio,
    "-filter_complex", filter_complex,
    "-map", "[v]", "-map", "2:a",
    "-c:v", "libx264", "-preset", "faster", "-crf", "18", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    out_clip
]

subprocess.run(cmd, check=True)
print("Rendered preview_fresh_bg_bigger_text.mp4 successfully!")
