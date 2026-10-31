import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/18_Coldplay_Yellow")
ass_path = song_dir / "lyrics_spotify.ass"

events = [
    # Title Card
    ("0:00:04.00", "0:00:18.00", "SpotifyTitle", r"{\pos(960,470)\fad(500,400)}Yellow\N{\fs66\fsp4\b0}Coldplay"),
    # Verse 1
    ("0:00:32.20", "0:00:41.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Look at the stars\NLook how they shine for you"),
    ("0:00:41.20", "0:00:49.40", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}And everything you do\NYeah, they were all yellow"),
    ("0:00:49.60", "0:00:57.20", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}I came along\NI wrote a song for you"),
    ("0:00:57.40", "0:01:07.50", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}And all the things you do\NAnd it was called 'Yellow'"),
    ("0:01:08.00", "0:01:19.50", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}So then I took my turn\NOh, what a thing to have done"),
    ("0:01:19.80", "0:01:26.80", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}And it was all yellow"),
    # Chorus 1
    ("0:01:27.20", "0:01:39.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Your skin, oh yeah, your skin and bones\NTurn into something beautiful"),
    ("0:01:39.20", "0:01:52.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}And you know, you know I love you so\NYou know I love you so"),
    # Verse 2
    ("0:02:11.80", "0:02:20.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}I swam across\NI jumped across for you"),
    ("0:02:20.20", "0:02:29.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Oh, what a thing to do\N'Cause you were all yellow"),
    ("0:02:29.20", "0:02:35.50", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}I drew a line\NI drew a line for you"),
    ("0:02:35.70", "0:02:49.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Oh, what a thing to do\NAnd it was all yellow"),
    # Chorus 2
    ("0:02:50.00", "0:03:01.80", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}And your skin, oh yeah, your skin and bones\NTurn into something beautiful"),
    ("0:03:02.00", "0:03:18.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}And you know, for you, I'd bleed myself dry\NFor you, I'd bleed myself dry"),
    # Outro
    ("0:03:45.00", "0:03:55.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}It's true\NLook how they shine for you"),
    ("0:03:55.20", "0:04:07.50", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Look how they shine for you\NLook how they shine for you"),
    ("0:04:07.80", "0:04:16.80", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Look at the stars\NLook how they shine for you"),
    ("0:04:17.00", "0:04:26.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}And all the things that you do"),
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

print(f"Generated studio-aligned zero-lag ASS file with {len(events)} events: {ass_path}")
