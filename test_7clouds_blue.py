import os
import sys
import subprocess
from PIL import Image, ImageFilter
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
raw_img_path = brain / "blue_yung_kai_7clouds_sky_1793329406801.jpg"
song_dir = base / "songs" / "28_yung_kai_blue"

# 1. Resize to 1920x1080
img = Image.open(raw_img_path).convert('RGB')
img_1080 = img.resize((1920, 1080), Image.Resampling.LANCZOS)
clean_bg_path = song_dir / "blue_7clouds_master.png"
img_1080.save(clean_bg_path)
print(f"Saved 7clouds master background: {clean_bg_path}")

# 2. Build 7clouds style ASS file
# 7clouds characteristics:
# - Pure white text
# - Clean solid black outline (border 3.8) and soft drop shadow (shadow 2.5) for instant readability over pastel/light clouds
# - Patrick Hand 102pt for couplets, 175pt for title
ass_7clouds_path = song_dir / "lyrics_7clouds_clean.ass"

header = """[Script Info]
Title: yung kai - blue (7clouds Clean Aesthetic Edition)
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Title7Clouds,Patrick Hand,175,&H00FFFFFF,&H000000FF,&H00101828,&H80000000,-1,0,0,0,100,100,5,0,1,4.0,2.5,5,180,180,110,1
Style: Lyric7Clouds,Patrick Hand,102,&H00FFFFFF,&H000000FF,&H00101828,&H80000000,-1,0,0,0,100,100,2,0,1,3.8,2.2,5,180,180,110,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

# Read couplets from existing lyrics_glowing_white.ass
existing_ass = (song_dir / "lyrics_glowing_white.ass").read_text(encoding='utf-8')
events = []
for line in existing_ass.splitlines():
    if line.startswith("Dialogue:"):
        parts = line.split(",", 9)
        # parts: [0:Layer, 1:Start, 2:End, 3:Style, 4:Name, 5:MarginL, 6:MarginR, 7:MarginV, 8:Effect, 9:Text]
        style = "Title7Clouds" if "Title" in parts[3] else "Lyric7Clouds"
        # strip old blur and font overrides if any
        text = parts[9]
        # remove \blur...
        import re
        text_clean = re.sub(r'\\blur[0-9\.]+', '', text)
        events.append(f"Dialogue: 0,{parts[1]},{parts[2]},{style},,0,0,0,,{text_clean}")

ass_7clouds_path.write_text(header + "\n".join(events) + "\n", encoding='utf-8')
print(f"Saved 7clouds ASS: {ass_7clouds_path}")

# 3. Test render a sample chorus frame (at 45.0s: "I think I'll picture us, you with the waves")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
ass_escaped = ass_7clouds_path.as_posix().replace(":", "\\\\:")

out_chorus_frame = brain / "audit_yungkai_7clouds_chorus.png"
out_title_frame = brain / "audit_yungkai_7clouds_title.png"

# Notice 7clouds simple motion:
# Just smooth, elegant, slow zoompan of the sky itself! NO clunky overlay sprites!
fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00012,1.06)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=4:allf=t+u[v]"
)

# Extract Title at 3.5s
subprocess.run([
    "ffmpeg", "-y",
    "-ss", "3.5", "-t", "0.5",
    "-loop", "1", "-i", str(clean_bg_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-vframes", "1", str(out_title_frame)
], capture_output=True)
print(f"Saved Title audit: {out_title_frame}")

# Extract Chorus at 48.0s
subprocess.run([
    "ffmpeg", "-y",
    "-ss", "48.0", "-t", "0.5",
    "-loop", "1", "-i", str(clean_bg_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-vframes", "1", str(out_chorus_frame)
], capture_output=True)
print(f"Saved Chorus audit: {out_chorus_frame}")
