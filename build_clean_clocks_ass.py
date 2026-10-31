import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/21_Coldplay_Clocks")
ass_path = song_dir / "lyrics_spotify.ass"

events = [
    # Title
    ("0:00:04.00", "0:00:18.00", "SpotifyTitle", r"{\pos(960,470)\fad(500,400)}Clocks\N{\fs66\fsp4\b0}Coldplay"),
    # Verse 1
    ("0:00:29.00", "0:00:36.60", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}The lights go out and I can't be saved\NTides that I tried to swim against"),
    ("0:00:36.80", "0:00:44.20", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Brought me down upon my knees\NOh, I beg, I beg and plead"),
    ("0:00:44.40", "0:00:51.20", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Come out of things unsaid\NShoot an apple off my head"),
    ("0:00:51.40", "0:00:58.20", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}And a trouble that can't be named\NA tiger's waiting to be tamed"),
    # Chorus 1
    ("0:00:58.40", "0:01:14.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Singing, you are\NYou are"),
    # Verse 2
    ("0:01:27.60", "0:01:35.20", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Confusion never stops\NClosing walls and ticking clocks"),
    ("0:01:35.40", "0:01:43.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Gonna come back and take you home\nI could not stop that you now know".replace(r"\n", r"\N")),
    ("0:01:43.20", "0:01:49.20", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Singing, come out upon my seas\nCursed missed opportunities".replace(r"\n", r"\N")),
    ("0:01:49.40", "0:01:58.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Am I a part of the cure\nOr am I part of the disease?".replace(r"\n", r"\N")),
    # Chorus 2
    ("0:01:58.20", "0:02:14.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Singing, you are\nYou are".replace(r"\n", r"\N")),
    ("0:02:14.20", "0:02:30.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}You are\nYou are".replace(r"\n", r"\N")),
    # Bridge
    ("0:02:56.20", "0:03:08.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}And nothing else compares\nOh, nothing else compares".replace(r"\n", r"\N")),
    ("0:03:10.80", "0:03:24.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}And nothing else compares\nOh, nothing else compares".replace(r"\n", r"\N")),
    # Climactic Chorus
    ("0:03:55.50", "0:04:08.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}You are\nYou are".replace(r"\n", r"\N")),
    # Outro
    ("0:04:08.20", "0:04:16.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Home, home, where I wanted to go\nHome, home, where I wanted to go".replace(r"\n", r"\N")),
    ("0:04:16.20", "0:04:29.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Home, home, where I wanted to go\nHome, home, where I wanted to go".replace(r"\n", r"\N")),
    ("0:04:29.20", "0:04:45.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Home, home, where I wanted to go\nHome, home, where I wanted to go".replace(r"\n", r"\N")),
]

header = """[Script Info]
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
"""

lines = [header]
for start, end, style, text in events:
    lines.append(f"Dialogue: 0,{start},{end},{style},,0,0,0,,{text}\n")

with open(ass_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"Generated clean ASS file with {len(events)} events: {ass_path}")
