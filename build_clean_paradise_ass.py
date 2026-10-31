import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/20_Coldplay_Paradise")
ass_path = song_dir / "lyrics_spotify.ass"

events = [
    # Title
    ("0:00:04.00", "0:00:15.00", "SpotifyTitle", r"{\pos(960,470)\fad(500,400)}Paradise\N{\fs66\fsp4\b0}Coldplay"),
    # Intro Chants & Verse 1
    ("0:00:54.00", "0:01:01.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Ooh-ooh-ooh, ooh-ooh-ooh\NOoh-ooh-ooh, ooh-ooh-ooh"),
    ("0:01:01.20", "0:01:07.80", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}When she was just a girl\NShe expected the world"),
    ("0:01:08.00", "0:01:14.60", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}But it flew away from her reach\NSo she ran away in her sleep"),
    # Chorus 1
    ("0:01:14.80", "0:01:21.80", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}And dreamed of para-, para-, paradise\NPara-, para-, paradise"),
    ("0:01:22.00", "0:01:31.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Para-, para-, paradise\NEvery time she closed her eyes"),
    # Re-intro Chants & Verse 2
    ("0:01:35.50", "0:01:42.20", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Ooh-ooh-ooh, ooh-ooh-ooh\NOoh-ooh-ooh, ooh-ooh-ooh"),
    ("0:01:42.40", "0:01:49.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}When she was just a girl\NShe expected the world"),
    ("0:01:49.20", "0:01:56.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}But it flew away from her reach\nAnd the bullets catch in her teeth".replace(r"\n", r"\N")),
    # Pre-Chorus 2
    ("0:01:56.20", "0:02:03.20", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Life goes on, it gets so heavy\nThe wheel breaks the butterfly".replace(r"\n", r"\N")),
    ("0:02:03.40", "0:02:12.80", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Every tear, a waterfall\nIn the night, the stormy night, she'd close her eyes".replace(r"\n", r"\N")),
    ("0:02:13.00", "0:02:19.80", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}In the night, the stormy night\nAway she'd fly".replace(r"\n", r"\N")),
    # Chorus 2
    ("0:02:20.00", "0:02:27.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}And dreamed of para-, para-, paradise\nPara-, para-, paradise".replace(r"\n", r"\N")),
    ("0:02:27.20", "0:02:33.20", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Para-, para-, paradise\nOh-oh-oh-oh, oh-oh-oh-oh".replace(r"\n", r"\N")),
    ("0:02:33.40", "0:02:40.80", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}She'd dream of para-para-paradise\nPara-para-paradise".replace(r"\n", r"\N")),
    ("0:02:41.00", "0:02:51.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Para-para-paradise\nOh-oh-oh-oh, oh-oh-oh-oh".replace(r"\n", r"\N")),
    # Bridge
    ("0:03:01.50", "0:03:07.80", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}La, la-la-la-la-la-la\nLa-la-la-la-la-la, yeah".replace(r"\n", r"\N")),
    ("0:03:08.00", "0:03:14.60", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}So lying underneath those stormy skies\NShe said, 'Oh, I know the sun must set to rise'"),
    # Chorus 3
    ("0:03:14.80", "0:03:21.50", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}This could be para-, para-, paradise\nPara-, para-, paradise".replace(r"\n", r"\N")),
    ("0:03:21.70", "0:03:28.40", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}This could be para-para-paradise\nOh-oh-oh-oh, oh-oh-oh-oh".replace(r"\n", r"\N")),
    ("0:03:28.60", "0:03:35.20", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}This could be para-, para-, paradise\nPara-, para-, paradise".replace(r"\n", r"\N")),
    ("0:03:35.40", "0:03:46.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}This could be para-, para-, paradise\nOh-oh-oh-oh, oh-oh-oh-oh".replace(r"\n", r"\N")),
    # Final Chorus & Outro
    ("0:04:02.50", "0:04:09.40", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}This could be para-, para-, paradise\nPara-, para-, paradise".replace(r"\n", r"\N")),
    ("0:04:09.60", "0:04:17.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}This could be para-, para-, paradise\nOh-oh-oh-oh, oh-oh-oh-oh".replace(r"\n", r"\N")),
    ("0:04:17.20", "0:04:28.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Ooh-ooh-ooh, ooh-ooh-ooh\nOoh-ooh-ooh, ooh-ooh-ooh".replace(r"\n", r"\N")),
]

header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyTitle,Poppins,130,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,2,0,1,1.5,3.0,5,50,50,50,1
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
