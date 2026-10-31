from pathlib import Path

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/17_Katy_Perry_The_One_That_Got_Away")
ass_file = song_dir / "lyrics_spotify.ass"

content = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyTitle,Poppins,125,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,2,0,1,1.5,3.0,5,50,50,50,1
Style: SpotifyHook,Poppins,82,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.2,2.5,5,50,50,50,1
Style: SpotifyVerse,Poppins,72,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.2,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.60,0:00:03.20,SpotifyTitle,,0,0,0,,{\\pos(960,470)\\fad(300,200)}The One That Got Away\\N{\\fs60\\fsp4\\b0}Katy Perry
Dialogue: 0,0:00:03.40,0:00:10.30,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Summer after high school when we first met\\NWe'd make out in your Mustang to Radiohead
Dialogue: 0,0:00:10.50,0:00:17.40,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}And on my 18th birthday\\NWe got matching tattoos
Dialogue: 0,0:00:17.60,0:00:24.90,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Used to steal your parents' liquor and climb to the roof\\NTalk about our future like we had a clue
Dialogue: 0,0:00:25.10,0:00:30.40,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Never planned that one day\\NI'd be losing you
Dialogue: 0,0:00:30.60,0:00:37.40,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}In another life\\NI would be your girl
Dialogue: 0,0:00:37.60,0:00:44.50,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}We'd keep all our promises\\NBe us against the world
Dialogue: 0,0:00:44.70,0:00:51.40,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}In another life\\NI would make you stay
Dialogue: 0,0:00:51.60,0:00:58.80,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}So I don't have to say you were\\NThe one that got away
Dialogue: 0,0:00:59.00,0:01:02.70,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}The one that got away
Dialogue: 0,0:01:02.90,0:01:09.50,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}I was June and you were my Johnny Cash\\NNever one without the other, we made a pact
Dialogue: 0,0:01:09.70,0:01:16.80,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Sometimes when I miss you\\NI put those records on
Dialogue: 0,0:01:17.00,0:01:23.90,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Someone said you had your tattoo removed\\NSaw you downtown singing the blues
Dialogue: 0,0:01:24.10,0:01:29.10,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}It's time to face the music\\NI'm no longer your muse
Dialogue: 0,0:01:29.30,0:01:36.60,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}But in another life\\NI would be your girl
Dialogue: 0,0:01:36.80,0:01:43.60,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}We'd keep all our promises\\NBe us against the world
Dialogue: 0,0:01:43.80,0:01:50.50,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}In another life\\NI would make you stay
Dialogue: 0,0:01:50.70,0:01:57.90,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}So I don't have to say you were\\NThe one that got away
Dialogue: 0,0:01:58.10,0:02:01.40,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}The one that got away
Dialogue: 0,0:02:01.60,0:02:08.80,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}The one\\NThe one
Dialogue: 0,0:02:09.00,0:02:15.60,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}The one\\NThe one that got away
Dialogue: 0,0:02:15.80,0:02:23.10,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}All this money can't buy me a time machine, no\\NCan't replace you with a million rings, no
Dialogue: 0,0:02:23.30,0:02:30.40,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}I should've told you what you meant to me\\N'Cause now I pay the price
Dialogue: 0,0:02:30.60,0:02:37.90,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}In another life\\NI would be your girl
Dialogue: 0,0:02:38.10,0:02:44.90,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}We'd keep all our promises\\NBe us against the world
Dialogue: 0,0:02:45.10,0:02:51.80,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}In another life\\NI would make you stay
Dialogue: 0,0:02:52.00,0:02:59.20,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}So I don't have to say you were\\NThe one that got away
Dialogue: 0,0:02:59.40,0:03:07.40,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}The one that got away\\NThe one that got away
Dialogue: 0,0:03:07.60,0:03:14.80,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}In another life\\NI would make you stay
Dialogue: 0,0:03:15.00,0:03:26.50,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}So I don't have to say you were\\NThe one that got away
"""

with open(ass_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Regenerated clean Katy Perry lyrics_spotify.ass!")
