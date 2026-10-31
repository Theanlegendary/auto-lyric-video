import os
import sys
import subprocess
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
bg_p = os.path.join(base, "songs", "15_Akon_Lonely", "vegas_rdr_orange_blurred_master.png")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

ass_text = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyUpright,Poppins,84,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.2,2.5,5,50,50,50,1
Style: SpotifyItalic,Poppins Black,84,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,1,0,0,100,100,1,0,1,1.2,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:05.00,SpotifyUpright,,0,0,0,,{{\\pos(960,490)}}Lonely, I'm Mr. Lonely\\NI have nobody for my own
Dialogue: 0,0:00:05.00,0:00:10.00,SpotifyItalic,,0,0,0,,{{\\pos(960,490)}}Lonely, I'm Mr. Lonely\\NI have nobody for my own
"""

ass_file = os.path.join(base, "compare_spotify_upright_vs_italic.ass")
with open(ass_file, "w", encoding="utf-8") as f:
    f.write(ass_text)

ass_escaped = ass_file.replace("\\", "/").replace(":", "\\\\:")

for ss, fname in [("00:00:02", "compare_spotify_upright.png"), ("00:00:07", "compare_spotify_italic.png")]:
    out_p = os.path.join(brain, fname)
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "10", "-i", bg_p,
        "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
        "-ss", ss, "-vframes", "1",
        out_p
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered: {fname}")
