import os
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
brain = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
bg_path = os.path.join(base, "songs", "15_Akon_Lonely", "vibe_sky_blurred_master.png")
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

fonts = [
    ("Chewy", "Chewy", 185, 130),
    ("Sniglet", "Sniglet", 180, 125),
    ("BalsamiqSans", "Balsamiq Sans", 175, 120),
]

for label, fname, hook_sz, verse_sz in fonts:
    # ASS script with clean big style
    ass_content = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,{fname},195,&H00FFFFFF,&H000000FF,&H00100818,&H55000000,1,0,0,0,100,100,2,0,1,0.8,2.8,5,50,50,50,1
Style: HookBig,{fname},{hook_sz},&H00FFFFFF,&H000000FF,&H00100818,&H55000000,1,0,0,0,100,100,1,0,1,0.8,2.5,5,50,50,50,1
Style: VerseClean,{fname},{verse_sz},&H00FFFFFF,&H000000FF,&H00100818,&H55000000,1,0,0,0,100,100,1,0,1,0.8,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:01.00,0:00:05.00,TitleCard,,0,0,0,,{{\\pos(960,470)}}LONELY\\N{{\\fs95\\fsp3}}Akon
Dialogue: 0,0:00:05.00,0:00:10.00,HookBig,,0,0,0,,{{\\pos(960,490)}}LONELY\\NI'M MR. LONELY
Dialogue: 0,0:00:10.00,0:00:15.00,HookBig,,0,0,0,,{{\\pos(960,490)}}I HAVE NOBODY\\NFOR MY OWN
Dialogue: 0,0:00:15.00,0:00:20.00,VerseClean,,0,0,0,,{{\\pos(960,490)}}CAN'T BELIEVE I HAD A GIRL LIKE YOU\\NAND I JUST LET YOU WALK OUT OF MY LIFE
"""
    ass_path = os.path.join(base, f"test_bigclean_{label}.ass")
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_content)
    
    ass_escaped = ass_path.replace("\\", "/").replace(":", "\\\\:")
    
    # Render Hook frame at 00:07 and Title at 00:03
    for ss, desc in [("00:00:03", "title"), ("00:00:07", "hook"), ("00:00:12", "hook2"), ("00:00:17", "verse")]:
        out_f = os.path.join(brain, f"akon_bigclean_{label}_{desc}.png")
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-t", "25", "-i", bg_path,
            "-vf", f"subtitles={ass_escaped}:fontsdir={fonts_escaped}",
            "-ss", ss, "-vframes", "1",
            out_f
        ]
        subprocess.run(cmd, check=True)
        print(f"Rendered {label} - {desc}")

print("All big clean previews rendered!")
