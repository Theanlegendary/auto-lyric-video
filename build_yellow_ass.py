from pathlib import Path

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/18_Coldplay_Yellow")
ass_file = song_dir / "lyrics_spotify.ass"

content = """[Script Info]
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
Dialogue: 0,0:00:06.00,0:00:18.00,SpotifyTitle,,0,0,0,,{\\pos(960,470)\\fad(500,400)}Yellow\\N{\\fs66\\fsp4\\b0}Coldplay
Dialogue: 0,0:00:34.80,0:00:42.90,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Look at the stars\\NLook how they shine for you
Dialogue: 0,0:00:43.10,0:00:51.20,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}And everything you do\\NYeah, they were all yellow
Dialogue: 0,0:00:51.40,0:00:59.50,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}I came along\\NI wrote a song for you
Dialogue: 0,0:00:59.70,0:01:10.40,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}And all the things you do\\NAnd it was called "Yellow"
Dialogue: 0,0:01:10.60,0:01:21.80,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}So then I took my turn\\NOh, what a thing to have done
Dialogue: 0,0:01:22.00,0:01:29.90,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}And it was all yellow
Dialogue: 0,0:01:30.40,0:01:41.10,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Your skin, oh yeah, your skin and bones\\NTurn into something beautiful
Dialogue: 0,0:01:41.30,0:01:57.00,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}And you know, you know I love you so\\NYou know I love you so
Dialogue: 0,0:02:14.00,0:02:22.20,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}I swam across\\NI jumped across for you
Dialogue: 0,0:02:22.40,0:02:30.50,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Oh, what a thing to do\\N'Cause you were all yellow
Dialogue: 0,0:02:30.70,0:02:38.70,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}I drew a line\\NI drew a line for you
Dialogue: 0,0:02:38.90,0:02:52.80,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Oh, what a thing to do\\NAnd it was all yellow
Dialogue: 0,0:02:53.00,0:03:03.80,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}And your skin, oh yeah, your skin and bones\\NTurn into something beautiful
Dialogue: 0,0:03:04.00,0:03:20.00,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}And you know, for you, I'd bleed myself dry\\NFor you, I'd bleed myself dry
Dialogue: 0,0:03:35.80,0:03:44.80,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}It's true\\NLook how they shine for you
Dialogue: 0,0:03:45.00,0:03:55.80,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Look how they shine for you\\NLook how they shine for you
Dialogue: 0,0:03:56.00,0:04:09.80,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Look how they shine for you\\NLook how they shine
Dialogue: 0,0:04:10.00,0:04:18.00,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Look at the stars\\NLook how they shine for you
Dialogue: 0,0:04:18.20,0:04:26.50,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}And all the things that you do
"""

with open(ass_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated clean {ass_file}!")
