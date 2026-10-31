import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/27_Joji_Glimpse_of_Us")

# Define the exact couplets for Joji - Glimpse of Us
# Format: (start_str, end_str, line1, line2, style)
couplets = [
    # Intro Title Hook
    ("0:00:00.60", "0:00:08.50", "Glimpse of Us", "Joji", "TitleGlow"),
    
    # Verse 1
    ("0:00:16.80", "0:00:24.80", "She'd take the world off my shoulders", "If it was ever hard to move", "LyricGlow"),
    ("0:00:25.20", "0:00:33.20", "She'd turn the rain to a rainbow", "When I was living in the blue", "LyricGlow"),
    
    # Pre-Chorus
    ("0:00:33.80", "0:00:41.80", "Why then, if she's so perfect", "Do I still wish that it was you?", "LyricGlow"),
    ("0:00:42.20", "0:00:49.80", "Perfect don't mean that it's working", "So what can I do? (Ooh)", "LyricGlow"),
    ("0:00:50.10", "0:00:57.80", "When you're out of sight", "In my mind", "LyricGlow"),
    
    # Chorus 1
    ("0:00:58.40", "0:01:06.80", "'Cause sometimes I look in her eyes", "And that's where I find a glimpse of us", "LyricGlow"),
    ("0:01:07.10", "0:01:15.20", "And I try to fall for her touch", "But I'm thinking of the way it was", "LyricGlow"),
    ("0:01:15.50", "0:01:23.20", "Said, \"I'm fine\" and said, \"I moved on\"", "I'm only here passing time in her arms", "LyricGlow"),
    ("0:01:23.60", "0:01:32.50", "Hoping I'll find", "A glimpse of us", "LyricGlow"),
    
    # Verse 2
    ("0:01:33.20", "0:01:41.20", "Tell me he savors your glory", "Does he laugh the way I did?", "LyricGlow"),
    ("0:01:41.60", "0:01:49.80", "Is this a part of your story?", "One that I had never lived", "LyricGlow"),
    
    # Bridge
    ("0:01:50.20", "0:01:58.20", "Maybe one day, you'll feel lonely", "And in his eyes, you'll get a glimpse", "LyricGlow"),
    ("0:01:58.50", "0:02:06.00", "Maybe you'll start slipping slowly", "And find me again", "LyricGlow"),
    ("0:02:06.30", "0:02:14.50", "When you're out of sight", "In my mind", "LyricGlow"),
    
    # Chorus 2
    ("0:02:14.80", "0:02:23.20", "'Cause sometimes I look in her eyes", "And that's where I find a glimpse of us", "LyricGlow"),
    ("0:02:23.50", "0:02:31.50", "And I try to fall for her touch", "But I'm thinking of the way it was", "LyricGlow"),
    ("0:02:31.80", "0:02:39.50", "Said, \"I'm fine\" and said, \"I moved on\"", "I'm only here passing time in her arms", "LyricGlow"),
    ("0:02:39.80", "0:02:50.00", "Hoping I'll find", "A glimpse of us", "LyricGlow"),
    
    # Instrumental / Piano emotional swell
    ("0:02:50.50", "0:03:00.50", "Glimpse of Us", "Joji", "TitleGlow"),
    
    # Final Chorus
    ("0:03:01.20", "0:03:09.80", "'Cause sometimes I look in her eyes", "And that's where I find a glimpse of us", "LyricGlow"),
    ("0:03:10.10", "0:03:18.20", "And I try to fall for her touch", "But I'm thinking of the way it was", "LyricGlow"),
    ("0:03:18.50", "0:03:26.20", "Said, \"I'm fine\" and said, \"I moved on\"", "I'm only here passing time in her arms", "LyricGlow"),
    ("0:03:26.50", "0:03:42.00", "Hoping I'll find", "A glimpse of us", "LyricGlow"),
]

# Generate Normal ASS file
header = """[Script Info]
Title: Joji - Glimpse of Us (Glowing Pure White Handwritten Edition)
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
