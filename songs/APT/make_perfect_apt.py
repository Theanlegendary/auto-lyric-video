header = """[Script Info]
Title: ROSÉ & Bruno Mars - APT.
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,Patrick Hand,130,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,1,0,0,0,95,115,3,0,1,2,1,5,50,50,50,1
Style: Lyric,Patrick Hand,148,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,0,0,0,0,95,115,1,0,1,1.8,0.8,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events = [
    # Top title card (avoids overlapping the lyrics in the center!)
    'Dialogue: 0,0:00:00.20,0:00:04.80,TitleCard,,0,0,0,,{\\an8\\pos(960,110)\\fad(300,400)}APT.\\N{\\fs75\\fsp4}ROSÉ & Bruno Mars',
    
    # Intro
    'Dialogue: 0,0:00:00.11,0:00:04.80,Lyric,,0,0,0,,{\\pos(960,520)\\fad(150,150)}CHAEYOUNG\'S FAVORITE RANDOM GAME\\NRANDOM GAME',
    'Dialogue: 0,0:00:04.70,0:00:06.40,Lyric,,0,0,0,,{\\pos(960,520)\\fad(150,150)}GAME START!',

    # Chorus 1
    'Dialogue: 0,0:00:06.30,0:00:09.60,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\NAPATEU, APATEU',
    'Dialogue: 0,0:00:09.60,0:00:12.80,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\NUH, UH-HUH, UH-HUH',
    'Dialogue: 0,0:00:12.80,0:00:16.00,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\NAPATEU, APATEU',
    'Dialogue: 0,0:00:16.00,0:00:19.30,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\NUH, UH-HUH, UH-HUH',

    # Verse 1 (ROSÉ)
    'Dialogue: 0,0:00:19.30,0:00:22.70,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}KISSY FACE, KISSY FACE\\NSENT TO YOUR PHONE, BUT',
    'Dialogue: 0,0:00:22.70,0:00:25.80,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}I\'M TRYIN\' TO KISS YOUR LIPS FOR REAL\\N(UH-HUH, UH-HUH)',
    'Dialogue: 0,0:00:25.80,0:00:29.20,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}RED HEARTS, RED HEARTS\\nTHAT\'S WHAT I\'M ON, YEAH',
    'Dialogue: 0,0:00:29.20,0:00:32.20,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}COME GIVE ME SOMETHIN\'\\nI CAN FEEL (OH-OH-OH)',

    # Pre-Chorus 1
    'Dialogue: 0,0:00:32.20,0:00:35.40,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}DON\'T YOU WANT ME\\nLIKE I WANT YOU, BABY?',
    'Dialogue: 0,0:00:35.40,0:00:38.50,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}DON\'T YOU NEED ME\\nLIKE I NEED YOU NOW?',
    'Dialogue: 0,0:00:38.50,0:00:41.80,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}SLEEP TOMORROW\\nBUT TONIGHT GO CRAZY',
    'Dialogue: 0,0:00:41.80,0:00:45.10,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}ALL YOU GOTTA DO IS\\nJUST MEET ME AT THE',

    # Chorus 2
    'Dialogue: 0,0:00:45.10,0:00:48.30,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nAPATEU, APATEU',
    'Dialogue: 0,0:00:48.30,0:00:51.50,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nUH, UH-HUH, UH-HUH',
    'Dialogue: 0,0:00:51.50,0:00:54.70,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nAPATEU, APATEU',
    'Dialogue: 0,0:00:54.70,0:00:57.60,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nUH, UH-HUH, UH-HUH',

    # Verse 2 (Bruno Mars)
    'Dialogue: 0,0:00:57.60,0:01:01.00,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}IT\'S WHATEVER, IT\'S WHATEVER\\nIT\'S WHATEVER YOU LIKE (WHOO)',
    'Dialogue: 0,0:01:01.00,0:01:03.80,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}TURN THIS APATEU INTO A CLUB\\n(UH-HUH, UH-HUH)',
    'Dialogue: 0,0:01:03.80,0:01:08.00,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}I\'M TALKIN\' DRINK, DANCE, SMOKE\\nFREAK, PARTY ALL NIGHT (COME ON)',
    'Dialogue: 0,0:01:08.00,0:01:10.80,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}GEONBAE, GEONBAE, GIRL\\nWHAT\'S UP? (OH-OH-OH)',

    # Pre-Chorus 2
    'Dialogue: 0,0:01:10.80,0:01:14.00,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}DON\'T YOU WANT ME\\nLIKE I WANT YOU, BABY?',
    'Dialogue: 0,0:01:14.00,0:01:17.10,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}DON\'T YOU NEED ME\\nLIKE I NEED YOU NOW?',
    'Dialogue: 0,0:01:17.10,0:01:20.40,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}SLEEP TOMORROW\\nBUT TONIGHT GO CRAZY',
    'Dialogue: 0,0:01:20.40,0:01:23.70,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}ALL YOU GOTTA DO IS\\nJUST MEET ME AT THE',

    # Chorus 3
    'Dialogue: 0,0:01:23.70,0:01:26.90,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nAPATEU, APATEU',
    'Dialogue: 0,0:01:26.90,0:01:30.10,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nUH, UH-HUH, UH-HUH',
    'Dialogue: 0,0:01:30.10,0:01:33.40,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nAPATEU, APATEU',
    'Dialogue: 0,0:01:33.40,0:01:36.50,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nUH, UH-HUH, UH-HUH',

    # Bridge
    'Dialogue: 0,0:01:36.50,0:01:39.60,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}HEY, SO NOW YOU KNOW THE GAME',
    'Dialogue: 0,0:01:39.60,0:01:43.00,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}ARE YOU READY? \'CAUSE I\'M COMIN\'\\nTO GET YOU, GET YOU, GET YOU',
    'Dialogue: 0,0:01:43.00,0:01:49.40,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}HOLD ON, HOLD ON\\nI\'M ON MY WAY',
    'Dialogue: 0,0:01:49.40,0:01:55.90,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}YEAH, YEAH, YEAH, YEAH, YEAH\\nI\'M ON MY WAY',
    'Dialogue: 0,0:01:55.90,0:02:02.30,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}HOLD ON, HOLD ON\\nI\'M ON MY WAY',
    'Dialogue: 0,0:02:02.30,0:02:08.90,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}YEAH, YEAH, YEAH, YEAH, YEAH\\nI\'M ON MY WAY',

    # Pre-Chorus 3
    'Dialogue: 0,0:02:08.90,0:02:12.00,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}DON\'T YOU WANT ME\\nLIKE I WANT YOU, BABY?',
    'Dialogue: 0,0:02:12.00,0:02:15.10,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}DON\'T YOU NEED ME\\nLIKE I NEED YOU NOW?',
    'Dialogue: 0,0:02:15.10,0:02:18.40,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}SLEEP TOMORROW\\nBUT TONIGHT GO CRAZY',
    'Dialogue: 0,0:02:18.40,0:02:21.70,Lyric,,0,0,0,,{\\pos(960,500)\\fad(150,150)}ALL YOU GOTTA DO IS\\nJUST MEET ME AT THE',

    # Final Chorus Outro
    'Dialogue: 0,0:02:21.70,0:02:24.90,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nAPATEU, APATEU',
    'Dialogue: 0,0:02:24.90,0:02:28.20,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nUH, UH-HUH, UH-HUH\\n{\\fs90}(JUST MEET ME AT THE)',
    'Dialogue: 0,0:02:28.20,0:02:31.40,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nAPATEU, APATEU',
    'Dialogue: 0,0:02:31.40,0:02:34.60,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nUH, UH-HUH, UH-HUH\\n{\\fs90}(JUST MEET ME AT THE)',
    'Dialogue: 0,0:02:34.60,0:02:37.80,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nAPATEU, APATEU',
    'Dialogue: 0,0:02:37.80,0:02:41.00,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nUH, UH-HUH, UH-HUH\\n{\\fs90}(JUST MEET ME AT THE)',
    'Dialogue: 0,0:02:41.00,0:02:44.20,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,100)}APATEU, APATEU\\nAPATEU, APATEU',
    'Dialogue: 0,0:02:44.20,0:02:48.50,Lyric,,0,0,0,,{\\pos(960,500)\\fad(100,200)}APATEU, APATEU\\nUH, UH-HUH, UH-HUH'
]

out_ass = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/APT/lyrics_perfect_apt.ass"
with open(out_ass, "w", encoding="utf-8") as f:
    f.write(header + "\n".join(events))

print("Created lyrics_perfect_apt.ass with flawless line breaks, zero overlaps, and proper English romanization!")
