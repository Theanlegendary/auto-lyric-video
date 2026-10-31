import os
import sys
import subprocess
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
raw_orange = os.path.join(base, "stock_anime_bgs", "18_rdr_vegas_clear_orange_sky.png")
song_dir = os.path.join(base, "songs", "15_Akon_Lonely")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

# 1. Create Spotify Glass blurred orange master
im = Image.open(raw_orange).convert("RGB").resize((1920, 1080), Image.Resampling.LANCZOS)
im_blur = im.filter(ImageFilter.GaussianBlur(radius=18))
scrim = Image.new("RGB", (1920, 1080), (28, 12, 8)) # subtle warm desert scrim
bg_spotify_orange = Image.blend(im_blur, scrim, 0.08)

master_orange_path = os.path.join(song_dir, "vegas_rdr_orange_blurred_master.png")
bg_spotify_orange.save(master_orange_path, "PNG")
print(f"Saved master blurred orange background: {master_orange_path}")

# 2. ASS test with Spotify style: Poppins Bold, Sentence Case, 50/50 balance
test_ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyTitle,Poppins,135,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,2,0,1,1.5,3.0,5,50,50,50,1
Style: SpotifyHook,Poppins,82,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.2,2.5,5,50,50,50,1
Style: SpotifyVerse,Poppins,72,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.2,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:01.00,0:00:05.00,SpotifyTitle,,0,0,0,,{{\\pos(960,470)\\fad(500,300)}}Lonely\\N{{\\fs64\\fsp4\\b0}}Akon
Dialogue: 0,0:00:05.00,0:00:10.00,SpotifyHook,,0,0,0,,{{\\pos(960,490)\\fad(200,150)}}Lonely, I'm Mr. Lonely\\nI have nobody for my own
Dialogue: 0,0:00:10.00,0:00:15.00,SpotifyVerse,,0,0,0,,{{\\pos(960,490)\\fad(200,150)}}I woke up in the middle of the night\\nAnd I noticed my girl wasn't by my side
"""

test_ass = test_ass.replace("\\n", "\\N")
ass_path = os.path.join(base, "test_spotify_orange.ass")
with open(ass_path, "w", encoding="utf-8") as f:
    f.write(test_ass)

ass_escaped = ass_path.replace("\\", "/").replace(":", "\\\\:")

# 3. Render Title (00:03), Hook (00:07), Verse (00:12)
frames = [
    ("00:00:03", "preview_spotify_orange_title.png"),
    ("00:00:07", "preview_spotify_orange_hook.png"),
    ("00:00:12", "preview_spotify_orange_verse.png"),
]

for ss, fname in frames:
    out_p = os.path.join(brain, fname)
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "15", "-i", master_orange_path,
        "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
        "-ss", ss, "-vframes", "1",
        out_p
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered: {fname}")

print("Spotify orange preview frames rendered!")
