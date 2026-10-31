import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\29_Sia_Chandelier")

# Master Normal 1.0x Couplets
# Timing calibrated from Whisper + LRC for Sia - Chandelier
# Format: (start_sec, end_sec, text, is_title)
couplets_normal = [
    # Opening Title + First Line
    (0.30, 4.20, r"{\pos(960,340)\fad(300,200)\blur2.5}Chandelier\N{\fs80\fsp5\b0}Sia", True),
    (1.02, 4.20, r"{\pos(960,640)\fad(200,150)\blur2.0}Party girls don't get hurt\NCan't feel anything, when will I learn", False),
    
    # Verse 1
    (4.20, 8.62, r"{\pos(960,490)\fad(150,150)\blur2.0}I push it down, push it down", False),
    (11.96, 16.88, '{\\pos(960,490)\\fad(200,150)\\blur2.0}I\'m the one "for a good time call"\\NPhone\'s blowin\' up, ringin\' my doorbell', False),
    (17.14, 20.06, r"{\pos(960,490)\fad(150,150)\blur2.0}I feel the love, feel the love", False),
    
    # Pre-Chorus 1
    (22.60, 25.32, r"{\pos(960,490)\fad(150,150)\blur2.0}1, 2, 3, 1, 2, 3, drink\N1, 2, 3, 1, 2, 3, drink", False),
    (25.32, 28.12, r"{\pos(960,490)\fad(150,150)\blur2.0}1, 2, 3, 1, 2, 3, drink\N1, 2, 3, 1, 2, 3, drink", False),
    (28.12, 33.66, r"{\pos(960,490)\fad(150,150)\blur2.0}1, 2, 3, 1, 2, 3, drink\NThrow 'em back, 'til I lose count", False),
    
    # Chorus 1 (Soaring Hook)
    (35.48, 43.86, r"{\pos(960,490)\fad(250,200)\blur2.0}I'm gonna swing from the chandelier\NFrom the chandelier", False),
    (46.54, 55.00, r"{\pos(960,490)\fad(250,200)\blur2.0}I'm gonna live like tomorrow doesn't exist\NLike it doesn't exist", False),
    (55.86, 66.50, r"{\pos(960,490)\fad(250,200)\blur2.0}I'm gonna fly like a bird through the night\NFeel my tears as they dry", False),
    (67.88, 76.14, r"{\pos(960,490)\fad(250,200)\blur2.0}I'm gonna swing from the chandelier\NFrom the chandelier", False),
    
    # Post-Chorus 1
    (76.80, 81.74, r"{\pos(960,490)\fad(150,150)\blur2.0}And I'm holding on for dear life\NWon't look down, won't open my eyes", False),
    (81.74, 87.16, r"{\pos(960,490)\fad(150,150)\blur2.0}Keep my glass full until morning light\N'Cause I'm just holding on for tonight", False),
    (87.16, 92.92, r"{\pos(960,490)\fad(150,150)\blur2.0}Help me, I'm holding on for dear life\NWon't look down, won't open my eyes", False),
    (92.92, 99.60, r"{\pos(960,490)\fad(150,150)\blur2.0}Keep my glass full until morning light\N'Cause I'm just holding on for tonight", False),
    
    # Verse 2
    (100.14, 104.50, r"{\pos(960,490)\fad(150,150)\blur2.0}Sun is up, I'm a mess\NGotta get out now, gotta run from this", False),
    (104.50, 108.50, r"{\pos(960,490)\fad(150,150)\blur2.0}Here comes the shame, here comes the shame", False),
    
    # Pre-Chorus 2
    (109.52, 116.40, r"{\pos(960,490)\fad(150,150)\blur2.0}1, 2, 3, 1, 2, 3, drink\N1, 2, 3, 1, 2, 3, drink", False),
    (116.40, 122.50, r"{\pos(960,490)\fad(150,150)\blur2.0}1, 2, 3, 1, 2, 3, drink\NThrow 'em back, 'til I lose count", False),
    
    # Chorus 2
    (123.70, 131.28, r"{\pos(960,490)\fad(250,200)\blur2.0}I'm gonna swing from the chandelier\NFrom the chandelier", False),
    (134.38, 143.00, r"{\pos(960,490)\fad(250,200)\blur2.0}I'm gonna live like tomorrow doesn't exist\NLike it doesn't exist", False),
    (145.26, 154.66, r"{\pos(960,490)\fad(250,200)\blur2.0}I'm gonna fly like a bird through the night\NFeel my tears as they dry", False),
    (156.00, 165.30, r"{\pos(960,490)\fad(250,200)\blur2.0}I'm gonna swing from the chandelier\NFrom the chandelier", False),
    
    # Post-Chorus 2
    (165.30, 170.02, r"{\pos(960,490)\fad(150,150)\blur2.0}And I'm holding on for dear life\NWon't look down, won't open my eyes", False),
    (170.02, 175.46, r"{\pos(960,490)\fad(150,150)\blur2.0}Keep my glass full until morning light\N'Cause I'm just holding on for tonight", False),
    (176.02, 181.16, r"{\pos(960,490)\fad(150,150)\blur2.0}Help me, I'm holding on for dear life\NWon't look down, won't open my eyes", False),
    (181.16, 188.00, r"{\pos(960,490)\fad(150,150)\blur2.0}Keep my glass full until morning light\N'Cause I'm just holding on for tonight", False),
    
    # Outro Hook
    (188.00, 194.78, r"{\pos(960,490)\fad(150,150)\blur2.0}On for tonight\N'Cause I'm just holding on for tonight", False),
    (194.78, 207.22, r"{\pos(960,490)\fad(150,200)\blur2.0}On for tonight\N'Cause I'm just holding on for tonight", False),
    
    # Grand Outro Title Hook
    (207.50, 212.64, r"{\pos(960,460)\fad(400,500)\blur2.5}Chandelier\N{\fs88\fsp6\b0}Sia", True)
]

def format_ass_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:01d}:{m:02d}:{s:05.2f}"

def write_ass(couplets, out_path):
    header = """[Script Info]
Title: Sia - Chandelier (Official Fade Replay Lyric Edition)
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleGlow,Patrick Hand,170,&H00FFFFFF,&H000000FF,&H30FFFFFF,&H80000000,-1,0,0,0,100,100,6,0,1,3.5,0,5,180,180,110,1
Style: LyricGlow,Patrick Hand,98,&H00FFFFFF,&H000000FF,&H30FFFFFF,&H80000000,-1,0,0,0,100,100,2,0,1,3.0,0,5,180,180,110,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = []
    for st, et, text, is_title in couplets:
        st_str = format_ass_time(st)
        et_str = format_ass_time(et)
        style = "TitleGlow" if is_title else "LyricGlow"
        events.append(f"Dialogue: 0,{st_str},{et_str},{style},,0,0,0,,{text}")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(events) + "\n")
    print(f"Saved ASS: {out_path} ({len(events)} events)")

# Write Normal 1.0x ASS
normal_ass_path = song_dir / "lyrics_glowing_white.ass"
write_ass(couplets_normal, normal_ass_path)

# Generate Slowed + Reverb ASS (varispeed ratio 0.865)
ratio = 0.865
couplets_slowed = []
for st, et, text, is_title in couplets_normal:
    st_slowed = st / ratio
    et_slowed = et / ratio
    couplets_slowed.append((st_slowed, et_slowed, text, is_title))

slowed_ass_path = song_dir / "lyrics_slowed_reverb.ass"
write_ass(couplets_slowed, slowed_ass_path)
