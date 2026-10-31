import os
from pathlib import Path

out_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\spotify_style_choices")
out_dir.mkdir(parents=True, exist_ok=True)

events = """[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.60,0:00:05.60,SpotifyTitle,,0,0,0,,{\\pos(960,470)\\fad(400,300)}Sweater Weather\\N{\\fs84\\fsp6\\b0}The Neighbourhood
Dialogue: 0,0:00:05.90,0:00:14.00,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}And all I am is a man\\NI want the world in my hands
Dialogue: 0,0:00:14.20,0:00:21.80,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}I hate the beach, but I stand\\NIn California, with my toes in the sand
Dialogue: 0,0:00:22.00,0:00:29.60,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Use the sleeves of my sweater, let's have an adventure\\NHead in the clouds, but my gravity's centered
Dialogue: 0,0:00:29.80,0:00:37.40,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}Touch my neck, and I'll touch yours\\nYou in those little high-waisted shorts, oh
Dialogue: 0,0:00:37.70,0:00:42.60,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}She knows what I think about\\NAnd what I think about
Dialogue: 0,0:00:42.80,0:00:46.70,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}One love, two mouths\\NOne love, one house
Dialogue: 0,0:00:46.90,0:00:50.50,SpotifyVerse,,0,0,0,,{\\pos(960,490)\\fad(200,150)}No shirt, no blouse\\NJust us, you find out
Dialogue: 0,0:00:50.70,0:00:59.80,SpotifyHook,,0,0,0,,{\\pos(960,490)\\fad(200,150)}'Cause it's too cold for you here and now\\NSo let me hold both your hands in the holes of my sweater
"""

styles_def = {
    # Option 1: Spotify Max Pro (Poppins Bold 98pt clean white)
    "style1_spotify_max_pro.ass": """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyTitle,Poppins,175,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,2,0,1,2.0,3.5,5,50,50,50,1
Style: SpotifyHook,Poppins,106,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.8,2.8,5,50,50,50,1
Style: SpotifyVerse,Poppins,96,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.6,2.5,5,50,50,50,1
""",

    # Option 2: Spotify Amber Glow (Poppins Bold 96pt with warm amber halo)
    "style2_spotify_amber_glow.ass": """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyTitle,Poppins,175,&H00FFFFFF,&H000000FF,&H00103570,&H60051530,1,0,0,0,100,100,2,0,1,2.2,3.8,5,50,50,50,1
Style: SpotifyHook,Poppins,106,&H00FFFFFF,&H000000FF,&H00154080,&H60051530,1,0,0,0,100,100,1,0,1,2.0,3.0,5,50,50,50,1
Style: SpotifyVerse,Poppins,96,&H00FFFFFF,&H000000FF,&H00154080,&H60051530,1,0,0,0,100,100,1,0,1,1.8,2.6,5,50,50,50,1
""",

    # Option 3: Spotify Modern Floating (Inter Bold with wider letter tracking \fsp2)
    "style3_spotify_modern_floating.ass": """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyTitle,Inter,170,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,4,0,1,1.8,3.2,5,50,50,50,1
Style: SpotifyHook,Inter,104,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,2,0,1,1.6,2.4,5,50,50,50,1
Style: SpotifyVerse,Inter,94,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,2,0,1,1.4,2.2,5,50,50,50,1
""",

    # Option 4: Spotify Handwritten Hybrid (Patrick Hand Large 112pt)
    "style4_spotify_handwritten_hybrid.ass": """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyTitle,Patrick Hand,180,&H00FFFFFF,&H000000FF,&H00100804,&H60000000,1,0,0,0,95,115,3,0,1,2.0,3.5,5,50,50,50,1
Style: SpotifyHook,Patrick Hand,116,&H00FFFFFF,&H000000FF,&H00100804,&H60000000,1,0,0,0,95,115,1,0,1,1.8,2.6,5,50,50,50,1
Style: SpotifyVerse,Patrick Hand,104,&H00FFFFFF,&H000000FF,&H00100804,&H60000000,1,0,0,0,95,115,1,0,1,1.6,2.2,5,50,50,50,1
""",

    # Option 5: Spotify Cinematic Rounded (Fredoka Rounded Bold 104pt)
    "style5_spotify_cinematic_rounded.ass": """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyTitle,Fredoka,175,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,2,0,1,2.0,3.6,5,50,50,50,1
Style: SpotifyHook,Fredoka,106,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.8,3.0,5,50,50,50,1
Style: SpotifyVerse,Fredoka,95,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.6,2.6,5,50,50,50,1
"""
}

for fname, header in styles_def.items():
    p = out_dir / fname
    with open(p, "w", encoding="utf-8") as f:
        f.write(header + "\n" + events)
    print(f"Created ASS: {fname}")
