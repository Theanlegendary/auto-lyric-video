import subprocess

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
audio = f"{base}/audio.mp3"
fonts = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

# Clip 1: Light Pastel Clouds + Black Lyrics
light_sharp = f"{base}/light_clouds_sharp_1080.png"
light_blur = f"{base}/light_clouds_blur_1080.png"
ass_black = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/lyrics_black_text.ass"
out_light = f"{base}/preview_light_clouds_black_text.mp4"

fc_light = (
    "[0:v][1:v]blend=all_expr='if(lte(T,2.8),A,if(between(T,2.8,5.5),A*(1-(T-2.8)/2.7)+B*(T-2.8)/2.7,B))',"
    f"subtitles={ass_black}:fontsdir={fonts}[v]"
)

cmd_light = [
    "ffmpeg", "-y",
    "-loop", "1", "-framerate", "30", "-t", "18", "-i", light_sharp,
    "-loop", "1", "-framerate", "30", "-t", "18", "-i", light_blur,
    "-ss", "0", "-t", "18", "-i", audio,
    "-filter_complex", fc_light,
    "-map", "[v]", "-map", "2:a",
    "-c:v", "libx264", "-preset", "faster", "-crf", "18", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    out_light
]
subprocess.run(cmd_light, check=True)
print("Rendered preview_light_clouds_black_text.mp4!")

# Clip 2: Dark Twilight Night + White Lyrics
dark_sharp = f"{base}/dark_twilight_sharp_1080.png"
dark_blur = f"{base}/dark_twilight_blur_1080.png"
ass_white = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/lyrics_white_text.ass"
out_dark = f"{base}/preview_dark_twilight_white_text.mp4"

fc_dark = (
    "[0:v][1:v]blend=all_expr='if(lte(T,2.8),A,if(between(T,2.8,5.5),A*(1-(T-2.8)/2.7)+B*(T-2.8)/2.7,B))',"
    f"subtitles={ass_white}:fontsdir={fonts}[v]"
)

cmd_dark = [
    "ffmpeg", "-y",
    "-loop", "1", "-framerate", "30", "-t", "18", "-i", dark_sharp,
    "-loop", "1", "-framerate", "30", "-t", "18", "-i", dark_blur,
    "-ss", "0", "-t", "18", "-i", audio,
    "-filter_complex", fc_dark,
    "-map", "[v]", "-map", "2:a",
    "-c:v", "libx264", "-preset", "faster", "-crf", "18", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    out_dark
]
subprocess.run(cmd_dark, check=True)
print("Rendered preview_dark_twilight_white_text.mp4!")
