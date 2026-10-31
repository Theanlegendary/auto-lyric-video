# Generate two perfect subtitle style files: Black text for light BG, White text for dark BG

header_template = """[Script Info]
Title: That Should Be Me - Perfect Contrast
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
{styles}

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.50,0:00:04.50,TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(500,400)}}THAT SHOULD BE ME\\N{{\\fs85\\fsp4}}Justin Bieber
Dialogue: 0,0:00:05.88,0:00:10.83,Lyric,,0,0,0,,{{\\pos(960,470)\\fad(200,200)}}EVERYBODY'S LAUGHIN'\\NIN MY MIND
Dialogue: 0,0:00:12.33,0:00:17.73,Lyric,,0,0,0,,{{\\pos(960,470)\\fad(200,200)}}RUMOURS SPREADIN' 'BOUT\\NTHIS OTHER GUY
Dialogue: 0,0:00:32.41,0:00:35.24,Lyric,,0,0,0,,{{\\pos(960,470)\\fad(200,200)}}THAT SHOULD BE ME\\NHOLDIN' YOUR HAND
"""

# 1. Black Text for Light Backgrounds (Clouds, Pastel Sky)
# Primary: &H00151515 (Crisp Dark Charcoal), Outline: &H00FFFFFF (Clean soft white halo for maximum contrast)
styles_black = """Style: TitleCard,Patrick Hand,185,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,1,0,0,0,95,115,3,0,1,2,1,5,50,50,50,1
Style: Lyric,Patrick Hand,148,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,0,0,0,0,95,115,1,0,1,1.8,0.8,5,50,50,50,1"""

# 2. White Text for Dark Backgrounds (Night Sky, Twilight, Dark City)
# Primary: &H00FFFFFF (Pure White), Outline: &H00101010 (Deep Black outline), Shadow: &H80000000
styles_white = """Style: TitleCard,Patrick Hand,185,&H00FFFFFF,&H000000FF,&H00121018,&H80000000,1,0,0,0,95,115,3,0,1,2.5,2,5,50,50,50,1
Style: Lyric,Patrick Hand,148,&H00FFFFFF,&H000000FF,&H00121018,&H80000000,0,0,0,0,95,115,1,0,1,2.2,1.5,5,50,50,50,1"""

with open("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/lyrics_black_text.ass", "w", encoding="utf-8") as f:
    f.write(header_template.format(styles=styles_black))

with open("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/lyrics_white_text.ass", "w", encoding="utf-8") as f:
    f.write(header_template.format(styles=styles_white))

print("Created lyrics_black_text.ass and lyrics_white_text.ass successfully!")
