import sys
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\30_Ed_Sheeran_Perfect")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

# Let's check how the new Hero Title looks when rendered on the 80/20 Sea background
hero_ass_content = """[Script Info]
Title: Ed Sheeran - Perfect (Hero Title Test)
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
; Big Hero Title: Edo SZ 150pt centered in the middle of the screen
Style: HeroTitle,Edo SZ,150,&H00FFFFFF,&H000000FF,&H35000000,&H60000000,0,0,0,0,100,100,2.0,0,1,4.5,3.0,5,160,160,100,1
; Subtitle Artist: Poppins SemiBold 42pt centered below
Style: HeroSub,Poppins SemiBold,42,&H00FFFFFF,&H000000FF,&H40000000,&H60000000,0,0,0,0,100,100,6.0,0,1,2.5,2.0,5,160,160,100,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.60,0:00:08.00,HeroTitle,,0,0,0,,{\\pos(960,450)\\blur2.2}PERFECT
Dialogue: 0,0:00:00.60,0:00:08.00,HeroSub,,0,0,0,,{\\pos(960,560)\\blur1.8}ED SHEERAN
"""

(song_dir / "test_hero_title.ass").write_text(hero_ass_content, encoding='utf-8')
print("Generated test_hero_title.ass")
