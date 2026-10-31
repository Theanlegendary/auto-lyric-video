import os
import sys
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "15_Akon_Lonely"
audio_path = song_dir / "audio_7clouds.mp3"
bg_blur = song_dir / "vibe_sky_blurred_master.png"
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

for opt, fname, sz_hook, sz_verse in [("Chewy", "Chewy", 185, 130), ("Sniglet", "Sniglet", 180, 125)]:
    ass_path = base / f"sample_{opt}.ass"
    ass_content = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,{fname},195,&H00FFFFFF,&H000000FF,&H00100818,&H50000000,1,0,0,0,100,100,3,0,1,0.8,2.8,5,50,50,50,1
Style: HookBig,{fname},{sz_hook},&H00FFFFFF,&H000000FF,&H00100818,&H50000000,1,0,0,0,100,100,1,0,1,0.8,2.5,5,50,50,50,1
Style: VerseBig,{fname},{sz_verse},&H00FFFFFF,&H000000FF,&H00100818,&H50000000,1,0,0,0,100,100,1,0,1,0.8,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:01.00,0:00:09.93,TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(600,400)}}LONELY\\N{{\\fs95\\fsp4}}Akon
Dialogue: 0,0:00:10.13,0:00:15.20,HookBig,,0,0,0,,{{\\pos(960,490)\\fad(220,150)}}LONELY\\NI'M MR. LONELY
Dialogue: 0,0:00:15.30,0:00:20.54,HookBig,,0,0,0,,{{\\pos(960,490)\\fad(220,150)}}I HAVE NOBODY\\NFOR MY OWN
Dialogue: 0,0:00:20.74,0:00:24.18,HookBig,,0,0,0,,{{\\pos(960,490)\\fad(220,150)}}I'M SO LONELY
"""
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_content)
    
    ass_escaped = ass_path.as_posix().replace(":", "\\\\:")
    out_video = base / "videos" / f"15_Akon_Lonely_Sample_{opt}.mp4"
    
    fc = (
        f"[0:v]format=yuv420p,"
        f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
        f"fade=t=in:st=0:d=1.5,"
        f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
        f"noise=alls=6:allf=t+u[v]"
    )
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "25", "-i", str(bg_blur),
        "-i", str(audio_path),
        "-t", "25",
        "-filter_complex", fc,
        "-map", "[v]",
        "-map", "1:a",
        "-af", "afade=t=in:ss=0:d=1.8",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "18",
        "-c:a", "aac", "-b:a", "320k",
        str(out_video)
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered sample: {out_video.name}")
