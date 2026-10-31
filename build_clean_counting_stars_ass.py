import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/23_OneRepublic_Counting_Stars")
ass_path = song_dir / "lyrics_spotify.ass"

events = [
    # Acoustic Intro Chorus
    ("0:00:00.50", "0:00:08.80", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Lately, I've been, I've been losing sleep\NDreaming about the things that we could be"),
    ("0:00:09.00", "0:00:16.80", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}But baby, I've been, I've been praying hard\NSaid, no more counting dollars, we'll be counting stars"),
    ("0:00:17.00", "0:00:22.50", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Yeah, we'll be counting stars"),
    
    # HUGE HOOK TITLE INTRO (During the 14s Guitar & Drum Build Up)
    ("0:00:23.00", "0:00:36.50", "SpotifyTitle", r"{\pos(960,470)\fad(600,450)}Counting Stars\N{\fs84\fsp6\b0}OneRepublic"),
    
    # Verse 1
    ("0:00:37.00", "0:00:46.80", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}I see this life like a swinging vine\NSwing my heart across the line"),
    ("0:00:47.00", "0:00:54.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}In my face is flashing signs\NSeek it out and ye shall find"),
    ("0:00:54.20", "0:01:02.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Old, but I'm not that old\NYoung, but I'm not that bold"),
    ("0:01:02.20", "0:01:10.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}I feel something so right doing the wrong thing\nAnd I feel something so wrong doing the right thing".replace(r"\n", r"\N")),
    ("0:01:10.20", "0:01:17.50", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}I couldn't lie, couldn't lie, couldn't lie\nEverything that kills me makes me feel alive".replace(r"\n", r"\N")),
    
    # Chorus 1
    ("0:01:17.70", "0:01:25.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Lately, I've been, I've been losing sleep\nDreaming about the things that we could be".replace(r"\n", r"\N")),
    ("0:01:25.20", "0:01:33.20", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}But baby, I've been, I've been praying hard\nSaid, no more counting dollars, we'll be counting stars".replace(r"\n", r"\N")),
    ("0:01:33.40", "0:01:41.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Lately, I've been, I've been losing sleep\nDreaming about the things that we could be".replace(r"\n", r"\N")),
    ("0:01:41.20", "0:01:53.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}But baby, I've been, I've been praying hard\nSaid, no more counting dollars, we'll be counting stars".replace(r"\n", r"\N")),
    
    # Verse 2
    ("0:01:56.00", "0:02:04.50", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}I feel your love and I feel it burn\nDown this river, every turn".replace(r"\n", r"\N")),
    ("0:02:04.70", "0:02:12.80", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}\"Hope\" is our four-letter word\nMake that money, watch it burn".replace(r"\n", r"\N")),
    ("0:02:13.00", "0:02:20.50", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}And I feel something so wrong doing the right thing\nI couldn't lie, couldn't lie, couldn't lie".replace(r"\n", r"\N")),
    ("0:02:20.70", "0:02:28.50", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Everything that drowns me makes me wanna fly"),
    
    # Chorus 2
    ("0:02:28.70", "0:02:36.20", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Lately, I've been, I've been losing sleep\nDreaming about the things that we could be".replace(r"\n", r"\N")),
    ("0:02:36.40", "0:02:44.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}But baby, I've been, I've been praying hard\nSaid, no more counting dollars, we'll be counting stars".replace(r"\n", r"\N")),
    ("0:02:44.20", "0:02:51.80", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Lately, I've been, I've been losing sleep\nDreaming about the things that we could be".replace(r"\n", r"\N")),
    ("0:02:52.00", "0:03:02.50", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}But baby, I've been, I've been praying hard\nSaid, no more counting dollars, we'll be counting stars".replace(r"\n", r"\N")),
    
    # Bridge
    ("0:03:02.70", "0:03:11.50", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Oh, take that money, watch it burn\nSink in the river the lessons I learned".replace(r"\n", r"\N")),
    ("0:03:11.70", "0:03:19.50", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Take that money, watch it burn\nSink in the river the lessons I learned".replace(r"\n", r"\N")),
    ("0:03:19.70", "0:03:26.50", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Everything that kills me makes me feel alive"),
    
    # Final Climax & Outro
    ("0:03:26.70", "0:03:34.50", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Lately, I've been, I've been losing sleep\nDreaming about the things that we could be".replace(r"\n", r"\N")),
    ("0:03:34.70", "0:03:42.20", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Baby, I've been, I've been praying hard\nSaid, no more counting dollars, we'll be counting stars".replace(r"\n", r"\N")),
    ("0:03:42.40", "0:03:50.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Lately, I've been, I've been losing sleep\nDreaming about the things that we could be".replace(r"\n", r"\N")),
    ("0:03:50.20", "0:03:58.00", "SpotifyHook",  r"{\pos(960,490)\fad(200,150)}Baby, I've been, I've been praying hard\nSaid, no more counting dollars, we'll be counting stars".replace(r"\n", r"\N")),
    ("0:03:58.20", "0:04:14.00", "SpotifyVerse", r"{\pos(960,490)\fad(200,150)}Take that money, watch it burn\nSink in the river the lessons I learned".replace(r"\n", r"\N")),
]

header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyTitle,Poppins,170,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,2,0,1,1.8,3.5,5,50,50,50,1
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
