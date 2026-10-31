import subprocess
from pathlib import Path

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
song_dir = base / "songs" / "Taylor_Swift_The_Fate_of_Ophelia"
audio = song_dir / "audio.mp3"
bg_sharp = base / "stock_anime_bgs" / "03_anime_rooftop_sunset_skyline.png"
bg_blur = song_dir / "bg_blur.png"
ass_path = song_dir / "lyrics_remastered_indie.ass"
fonts_dir = base / "fonts"
out_video = base / "output" / "test_diag.mp4"

ass_esc = str(ass_path).replace("\\", "/").replace(":", "\\\\:")
fonts_esc = str(fonts_dir).replace("\\", "/").replace(":", "\\\\:")

filter_complex = (
    f"[0:v][1:v]blend=all_expr='if(lte(T,5.0),A,if(between(T,5.0,7.8),A*(1-(T-5.0)/2.8)+B*(T-5.0)/2.8,B))',"
    f"subtitles={ass_esc}:fontsdir={fonts_esc}[v]"
)

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-framerate", "30", "-t", "60", "-i", str(bg_sharp),
    "-loop", "1", "-framerate", "30", "-t", "60", "-i", str(bg_blur),
    "-ss", "0", "-t", "60", "-i", str(audio),
    "-filter_complex", filter_complex,
    "-map", "[v]", "-map", "2:a",
    "-c:v", "libx264", "-preset", "ultrafast", "-crf", "20", "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    str(out_video)
]

p = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", p.returncode)
if p.returncode != 0:
    print("Full stderr tail:\n", p.stderr[-1500:])
else:
    print("Success! Size:", out_video.stat().st_size)
