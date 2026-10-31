import os
import sys
import re
import time
import subprocess
from pathlib import Path
from PIL import Image, ImageFilter

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
sys.path.insert(0, str(base))

from auto_producer import parse_and_group_couplets, schedule_events, to_seconds, to_ass_time

song_dir = base / "songs" / "05_Billie_Eilish_BIRDS_OF_A_FEATHER_Pink_Edition"
audio_path = song_dir / "audio.mp3"
lrc_path = song_dir / "lyrics.lrc"
bg_sharp = base / "stock_anime_bgs" / "15_anime_birds_of_a_feather_pink_sunset_sky.png"
bg_blur = song_dir / "bg_blur.png"
out_video = base / "videos" / "05_Billie_Eilish_BIRDS_OF_A_FEATHER_Pink_Edition_Lyric_Video.mp4"
brain_dir = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

# 1. Create 8px blur
img = Image.open(str(bg_sharp))
img.filter(ImageFilter.GaussianBlur(radius=8)).save(str(bg_blur))
print("1. Created 8px Gaussian blur background.")

# 2. Get audio duration
p = subprocess.run(['ffmpeg', '-i', str(audio_path)], stderr=subprocess.PIPE, text=True, errors='ignore')
m_dur = re.search(r"Duration:\s*(\d{2}):(\d{2}):(\d{2}\.\d+)", p.stderr)
duration = 211.0
if m_dur:
    duration = int(m_dur.group(1)) * 3600 + int(m_dur.group(2)) * 60 + float(m_dur.group(3))

# 3. Parse LRC
lrc_text = lrc_path.read_text(encoding='utf-8')
couplets = parse_and_group_couplets(lrc_text)
first_vocal = couplets[0]['vocal_start'] if couplets else 5.0
print(f"2. Audio duration: {duration:.1f}s | First vocal: {first_vocal:.2f}s | Couplets: {len(couplets)}")

# 4. Intro timing
if first_vocal >= 5.0:
    t_blur = first_vocal
    t_sharp = max(1.5, first_vocal - 2.5)
    title_end = t_sharp
else:
    t_sharp = 2.5
    t_blur = 4.5
    title_end = 2.5

dt = round(t_blur - t_sharp, 2)

# 5. ASS Style - Cakes & Eclairs Espresso on Clear Pink Sky
styles = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,Patrick Hand,175,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,1,0,0,0,95,115,3,0,1,2,1,5,50,50,50,1
Style: Lyric,Patrick Hand,135,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,0,0,0,0,95,115,1,0,1,1.8,0.8,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events = schedule_events(couplets, duration, "BIRDS OF A FEATHER", "Billie Eilish", title_end)
ass_path = song_dir / "lyrics.ass"
with open(ass_path, "w", encoding="utf-8") as f:
    f.write(styles + "\n".join(events))
print(f"3. Generated ASS with {len(events)} events.")

# 6. Render
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
ass_escaped = ass_path.as_posix().replace(":", "\\\\:")
t_out = max(1.0, duration - 3.0)

fc = (
    f"[0:v]format=yuva420p,fade=t=out:st={t_sharp}:d={dt}:alpha=1[sharp];"
    f"[1:v][sharp]overlay=0:0:enable='lte(t,{t_blur})',"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=c0s=22:c0f=t+u[v];"
    f"[2:a]afade=t=in:ss=0:d=1.8,afade=t=out:st={t_out:.2f}:d=3.0[a]"
)

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-framerate", "30", "-t", str(duration), "-i", str(bg_sharp),
    "-loop", "1", "-framerate", "30", "-t", str(duration), "-i", str(bg_blur),
    "-i", str(audio_path),
    "-filter_complex", fc,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-preset", "faster", "-b:v", "6M", "-maxrate", "8M", "-bufsize", "12M", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest",
    str(out_video)
]

print("4. Starting 1080p render with 35mm grain and anti-block audio fade...")
t0 = time.time()
p_render = subprocess.run(cmd, check=True)
render_time = time.time() - t0
size_mb = os.path.getsize(out_video) / (1024 * 1024)
print(f"5. Render complete in {render_time:.1f}s | Size: {size_mb:.2f} MB")

# 7. Extract audit frame
sample_t = to_ass_time(first_vocal + 10.0)
audit_name = "audit_unique_bg_05_Billie_Eilish_BIRDS_OF_A_FEATHER_Pink_Edition.png"
subprocess.run([
    "ffmpeg", "-y", "-ss", sample_t, "-i", str(out_video),
    "-vframes", "1", str(brain_dir / audit_name)
], check=True)
print(f"6. Saved audit frame to {audit_name} at {sample_t}")
print("ALL_DONE!")
