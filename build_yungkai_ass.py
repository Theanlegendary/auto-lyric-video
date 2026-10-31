import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/28_yung_kai_blue")

def sec_to_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def time_to_sec(t_str):
    parts = t_str.split(":")
    h = int(parts[0])
    m = int(parts[1])
    s = float(parts[2])
    return h * 3600 + m * 60 + s

couplets = [
    # Intro Title Hook
    ("0:00:00.60", "0:00:08.50", "blue", "yung kai", "TitleGlow"),
    
    # Verse 1
    ("0:00:18.50", "0:00:25.50", "Your morning eyes", "I could stare like watching stars", "LyricGlow"),
    ("0:00:25.80", "0:00:33.00", "I could walk you by", "And I'll tell without a thought you'd be mine", "LyricGlow"),
    
    # Pre-Chorus
    ("0:00:33.50", "0:00:39.50", "Would you mind if I took your hand tonight?", "Know you're all that I want this life", "LyricGlow"),
    ("0:00:40.00", "0:00:47.00", "I'll imagine we fell in love", "I'll nap under moonlight skies with you", "LyricGlow"),
    
    # Chorus 1
    ("0:00:47.20", "0:00:54.20", "I think I'll picture us, you with the waves", "The ocean's colors on your face", "LyricGlow"),
    ("0:00:54.50", "0:01:01.50", "I'll leave my heart with your air", "So let me fly with you", "LyricGlow"),
    ("0:01:01.80", "0:01:14.50", "Will you be forever with me?", "Cause you're so blue", "LyricGlow"),
    
    # Mid-Song Atmospheric Hook
    ("0:01:15.00", "0:01:45.00", "blue", "yung kai", "TitleGlow"),
    
    # Verse 2
    ("0:01:46.00", "0:01:52.50", "My love will always stay by you", "I'll keep it safe, so don't you worry a thing", "LyricGlow"),
    ("0:01:52.80", "0:02:00.50", "I'll tell you I love you more", "It's stuck with you forever", "LyricGlow"),
    ("0:02:00.80", "0:02:07.80", "So promise you won't let it go", "I'll trust the universe will always bring me to you", "LyricGlow"),
    
    # Chorus 2
    ("0:02:08.00", "0:02:15.80", "I'll imagine we fell in love", "I'll nap under moonlight skies with you", "LyricGlow"),
    ("0:02:16.00", "0:02:23.00", "I think I'll picture us, you with the waves", "The ocean's colors on your face", "LyricGlow"),
    ("0:02:23.20", "0:02:30.00", "I'll leave my heart with your air", "So let me fly with you", "LyricGlow"),
    ("0:02:30.20", "0:02:44.00", "Will you be forever with me?", "Cause you're so blue", "LyricGlow"),
    
    # Outro Hook
    ("0:02:45.00", "0:03:25.00", "blue", "yung kai", "TitleGlow"),
]

header = """[Script Info]
Title: yung kai - blue (Glowing Pure White Handwritten Edition)
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleGlow,Patrick Hand,200,&H00FFFFFF,&H000000FF,&H30FFFFFF,&H50FFFFFF,1,0,0,0,95,112,2,0,1,3.5,0,5,50,50,50,1
Style: LyricGlow,Patrick Hand,98,&H00FFFFFF,&H000000FF,&H30FFFFFF,&H50FFFFFF,1,0,0,0,94,112,1,0,1,3.0,0,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events = []
for start, end, l1, l2, style in couplets:
    if style == "TitleGlow":
        text = f"{{\\pos(960,460)\\fad(500,400)\\blur2.5}}{l1}\\N{{\\fs88\\fsp6\\b0}}{l2}"
    else:
        text = f"{{\\pos(960,490)\\fad(200,150)\\blur2.0}}{l1}\\N{l2}"
    events.append(f"Dialogue: 0,{start},{end},{style},,0,0,0,,{text}\n")

ass_path = song_dir / "lyrics_glowing_white.ass"
ass_path.write_text(header + "".join(events), encoding="utf-8")
print(f"Generated {ass_path.name} with {len(couplets)} dialogue events.")

# Slowed Reverb ASS
R = 0.865
slowed_events = []
for start, end, l1, l2, style in couplets:
    s_sec = time_to_sec(start) / R
    e_sec = time_to_sec(end) / R
    s_str = sec_to_time(s_sec)
    e_str = sec_to_time(e_sec)
    
    if style == "TitleGlow":
        text = f"{{\\pos(960,460)\\fad(500,400)\\blur2.5}}{l1}\\N{{\\fs88\\fsp6\\b0}}{l2} (Slowed + Reverb)"
    else:
        text = f"{{\\pos(960,490)\\fad(200,150)\\blur2.0}}{l1}\\N{l2}"
    slowed_events.append(f"Dialogue: 0,{s_str},{e_str},{style},,0,0,0,,{text}\n")

slowed_ass_path = song_dir / "lyrics_slowed_reverb.ass"
slowed_header = header.replace("Handwritten Edition", "Slowed + Reverb Glowing White Edition")
slowed_ass_path.write_text(slowed_header + "".join(slowed_events), encoding="utf-8")
print(f"Generated {slowed_ass_path.name} with {len(couplets)} dialogue events.")
