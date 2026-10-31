import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Run a 1-second subtitle burn with -v verbose or debug to see libass font matching!
ass_content = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Patrick Hand,130,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,5,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:01.00,Default,,0,0,0,,CLOUD NINE
"""

with open("test_font_match.ass", "w", encoding="utf-8") as f:
    f.write(ass_content)

fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
cmd = [
    "ffmpeg", "-y", "-v", "verbose",
    "-f", "lavfi", "-i", "color=c=black:s=1920x1080:d=1",
    "-vf", f"subtitles=test_font_match.ass:fontsdir={fonts_escaped}",
    "-frames:v", "1", "test_font_out.png"
]

res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')
for line in res.stderr.splitlines():
    if "font" in line.lower() or "glyph" in line.lower() or "match" in line.lower():
        print(line)
