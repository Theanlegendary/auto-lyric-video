header = """[Script Info]
Title: Lady Gaga & Bruno Mars - Die With A Smile
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,Patrick Hand,185,&H00FFFFFF,&H000000FF,&H00121018,&H80000000,1,0,0,0,95,115,3,0,1,2.5,2,5,50,50,50,1
Style: Lyric,Patrick Hand,148,&H00FFFFFF,&H000000FF,&H00121018,&H80000000,0,0,0,0,95,115,1,0,1,2.2,1.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events = [
    # Title card during acoustic intro
    "Dialogue: 0,0:00:00.60,0:00:06.00,TitleCard,,0,0,0,,{\\pos(960,470)\\fad(500,400)}DIE WITH A SMILE\\N{\\fs85\\fsp4}Lady Gaga & Bruno Mars",
    
    # Verse 1 (Bruno Mars)
    "Dialogue: 0,0:00:07.80,0:00:14.50,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}I, I JUST WOKE UP\\NFROM A DREAM",
    "Dialogue: 0,0:00:14.50,0:00:19.30,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}WHERE YOU AND I\\nHAD TO SAY GOODBYE",
    "Dialogue: 0,0:00:19.30,0:00:23.80,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}AND I DON'T KNOW\\nWHAT IT ALL MEANS",
    "Dialogue: 0,0:00:23.80,0:00:28.40,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}BUT SINCE I SURVIVED\\nI REALIZED",
    "Dialogue: 0,0:00:28.40,0:00:32.90,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}WHEREVER YOU GO\\nTHAT'S WHERE I'LL FOLLOW",
    "Dialogue: 0,0:00:32.90,0:00:37.30,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}NOBODY'S PROMISED\\nTOMORROW",
    "Dialogue: 0,0:00:37.30,0:00:41.50,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}SO I'MA LOVE YOU EVERY NIGHT\\nLIKE IT'S THE LAST NIGHT",
    "Dialogue: 0,0:00:41.50,0:00:43.80,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}LIKE IT'S THE LAST NIGHT",

    # Chorus 1
    "Dialogue: 0,0:00:43.80,0:00:52.80,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}IF THE WORLD WAS ENDING\\nI'D WANNA BE NEXT TO YOU",
    "Dialogue: 0,0:00:52.80,0:01:01.90,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}IF THE PARTY WAS OVER AND\\nOUR TIME ON EARTH WAS THROUGH",
    "Dialogue: 0,0:01:01.90,0:01:11.20,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}I'D WANNA HOLD YOU JUST FOR A WHILE\\nAND DIE WITH A SMILE",
    "Dialogue: 0,0:01:11.20,0:01:21.00,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}IF THE WORLD WAS ENDING\\nI'D WANNA BE NEXT TO YOU",

    # Verse 2 (Lady Gaga)
    "Dialogue: 0,0:01:23.80,0:01:32.20,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}OH, LOST, LOST IN THE WORDS\\nTHAT WE SCREAM",
    "Dialogue: 0,0:01:32.20,0:01:36.60,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}I DON'T EVEN WANNA\\nDO THIS ANYMORE",
    "Dialogue: 0,0:01:36.60,0:01:40.20,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}'CAUSE YOU ALREADY KNOW\\nWHAT YOU MEAN TO ME",
    "Dialogue: 0,0:01:40.20,0:01:45.80,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}AND OUR LOVE'S THE ONLY WAR\\nWORTH FIGHTING FOR",

    # Pre-Chorus 2
    "Dialogue: 0,0:01:45.80,0:01:50.50,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}WHEREVER YOU GO\\nTHAT'S WHERE I'LL FOLLOW",
    "Dialogue: 0,0:01:50.50,0:01:54.80,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}NOBODY'S PROMISED\\nTOMORROW",
    "Dialogue: 0,0:01:54.80,0:01:58.90,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}SO I'MA LOVE YOU EVERY NIGHT\\nLIKE IT'S THE LAST NIGHT",
    "Dialogue: 0,0:01:58.90,0:02:01.30,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}LIKE IT'S THE LAST NIGHT",

    # Chorus 2 (Duet)
    "Dialogue: 0,0:02:01.30,0:02:10.30,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}IF THE WORLD WAS ENDING\\nI'D WANNA BE NEXT TO YOU",
    "Dialogue: 0,0:02:10.30,0:02:19.50,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}IF THE PARTY WAS OVER AND\\nOUR TIME ON EARTH WAS THROUGH",
    "Dialogue: 0,0:02:19.50,0:02:28.60,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}I'D WANNA HOLD YOU JUST FOR A WHILE\\nAND DIE WITH A SMILE",
    "Dialogue: 0,0:02:28.60,0:02:37.30,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}IF THE WORLD WAS ENDING\\nI'D WANNA BE NEXT TO YOU",

    # Bridge (Duet & Guitar Solo)
    "Dialogue: 0,0:02:37.30,0:02:41.80,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}RIGHT NEXT TO YOU",
    "Dialogue: 0,0:02:41.80,0:02:46.30,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}NEXT TO YOU",
    "Dialogue: 0,0:02:46.30,0:02:50.20,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}RIGHT NEXT TO YOU",
    "Dialogue: 0,0:02:50.20,0:02:55.00,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}OH-OH, OH",

    # Final Explosion Chorus
    "Dialogue: 0,0:03:09.50,0:03:18.80,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}IF THE WORLD WAS ENDING\\nI'D WANNA BE NEXT TO YOU",
    "Dialogue: 0,0:03:18.80,0:03:27.90,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}IF THE PARTY WAS OVER AND\\nOUR TIME ON EARTH WAS THROUGH",
    "Dialogue: 0,0:03:27.90,0:03:37.00,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}I'D WANNA HOLD YOU JUST FOR A WHILE\\nAND DIE WITH A SMILE",
    "Dialogue: 0,0:03:37.00,0:03:46.10,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}IF THE WORLD WAS ENDING\\nI'D WANNA BE NEXT TO YOU",
    "Dialogue: 0,0:03:46.10,0:03:55.00,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,200)}IF THE WORLD WAS ENDING\\nI'D WANNA BE NEXT TO YOU",
    "Dialogue: 0,0:03:57.80,0:04:04.00,Lyric,,0,0,0,,{\\pos(960,470)\\fad(200,300)}I'D WANNA BE NEXT TO YOU"
]

out_ass = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/Die_With_A_Smile/lyrics.ass"
with open(out_ass, "w", encoding="utf-8") as f:
    f.write(header + "\n".join(events))

print("Created Die With A Smile lyrics.ass successfully!")
