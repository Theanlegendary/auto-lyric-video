from pathlib import Path

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/19_Coldplay_A_Sky_Full_of_Stars")
ass_file = song_dir / "lyrics_spotify.ass"

content = """[Script Info]
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
Dialogue: 0,0:00:04.00,0:00:14.00,SpotifyTitle,,0,0,0,,{\\pos(960,470)\\fad(500,400)}A Sky Full of Stars\\N{\\fs66\\fsp4\\b0}Coldplay
Dialogue: 0,0:00:17.00,0:00:32.20,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}'Cause you're a sky, 'cause you're a sky full of stars\\NI'm gonna give you my heart
Dialogue: 0,0:00:32.40,0:00:47.70,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}'Cause you're a sky, 'cause you're a sky full of stars\\N'Cause you light up the path
Dialogue: 0,0:00:47.90,0:01:03.10,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}I don't care, go on and tear me apart\\NI don't care if you do, ooh-ooh
Dialogue: 0,0:01:03.30,0:01:14.50,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}'Cause in a sky, 'cause in a sky full of stars\\NI think I saw you
Dialogue: 0,0:01:41.80,0:01:57.00,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}'Cause you're a sky, 'cause you're a sky full of stars\\NI wanna die in your arms
Dialogue: 0,0:01:57.20,0:02:12.30,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}'Cause you get lighter the more it gets dark\\NI'm gonna give you my heart
Dialogue: 0,0:02:12.50,0:02:27.60,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}I don't care, go on and tear me apart\\NI don't care if you do, ooh-ooh
Dialogue: 0,0:02:27.80,0:02:40.80,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}'Cause in a sky, 'cause in a sky full of stars\\NI think I see you
Dialogue: 0,0:02:41.00,0:02:50.00,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}I think I see you
Dialogue: 0,0:03:36.60,0:03:49.40,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}'Cause you're a sky, you're a sky full of stars\\NSuch a heavenly view
Dialogue: 0,0:03:49.60,0:04:02.00,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}You're such a heavenly view
"""

with open(ass_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated clean {ass_file}!")
