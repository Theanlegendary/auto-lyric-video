import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\30_Ed_Sheeran_Perfect")

# Semantic Word-Chunk Couplets with Rest-Cut Timing (Base 1.0x)
# Strict 7clouds logic:
# 1. Edo SZ brush font in Sentence case
# 2. <= 2 lines maximum
# 3. Main lyrics in lower third (78% down), center aligned
# 4. Zero-frame cuts, instantaneous snapping
# 5. Rest cuts (screen empty during pauses)
# 6. Intro Hero Title Hook: Placed in the MIDDLE, Big & Bold (Edo SZ 150pt + Poppins 42pt) like 31_gnash!
couplets_1x = [
    # Verse 1
    ("0:00:08.00", "0:00:13.50", "I found a love for me,", "Darling, just dive right in", "Lyric"),
    ("0:00:13.60", "0:00:16.50", "And follow my lead", "", "Lyric"),
    # [Rest cut from 16.50s to 17.00s]
    ("0:00:17.00", "0:00:24.00", "Well, I found a girl,", "Beautiful and sweet", "Lyric"),
    # [Rest cut from 24.00s to 24.80s]
    ("0:00:24.80", "0:00:30.80", "Oh, I never knew you were the someone", "Waiting for me", "Lyric"),
    # [Rest cut from 30.80s to 31.76s]

    # Pre-Chorus 1
    ("0:00:31.76", "0:00:36.40", "'Cause we were just kids", "When we fell in love", "Lyric"),
    ("0:00:36.70", "0:00:47.30", "Not knowing what it was,", "I will not give you up this time", "Lyric"),
    ("0:00:47.70", "0:00:55.20", "Darling, just kiss me slow,", "Your heart is all I own", "Lyric"),
    ("0:00:55.20", "0:01:00.80", "And in your eyes,", "You're holding mine", "Lyric"),
    # [Rest cut from 01:00.80 to 01:02.60]

    # Chorus 1
    ("0:01:02.60", "0:01:12.80", "Baby, I'm dancing in the dark", "With you between my arms", "Lyric"),
    ("0:01:12.80", "0:01:20.40", "Barefoot on the grass,", "Listening to our favorite song", "Lyric"),
    ("0:01:20.40", "0:01:27.50", "When you said you looked a mess,", "I whispered underneath my breath", "Lyric"),
    ("0:01:27.50", "0:01:35.50", "But you heard it, darling,", "You look perfect tonight", "Lyric"),
    # [Rest cut from 01:35.50 to 01:40.00 - 4.5s instrumental break!]

    # Verse 2
    ("0:01:40.20", "0:01:47.80", "Well, I found a woman,", "Stronger than anyone I know", "Lyric"),
    ("0:01:48.00", "0:01:55.00", "She shares my dreams,", "I hope that someday I'll share her home", "Lyric"),
    ("0:01:55.30", "0:01:59.80", "I found a lover,", "To carry more than just my secrets", "Lyric"),
    ("0:01:59.80", "0:02:04.20", "To carry love,", "To carry children of our own", "Lyric"),

    # Pre-Chorus 2
    ("0:02:04.20", "0:02:13.50", "We are still kids, but we're so in love", "Fighting against all odds", "Lyric"),
    ("0:02:13.80", "0:02:19.50", "I know we'll be alright this time", "", "Lyric"),
    # [Rest cut from 02:19.50 to 02:20.50]
    ("0:02:20.50", "0:02:27.50", "Darling, just hold my hand,", "Be my girl, I'll be your man", "Lyric"),
    ("0:02:27.60", "0:02:35.50", "I see my future in your eyes", "", "Lyric"),
    # [Rest cut from 02:35.50 to 02:39.80]

    # Chorus 2
    ("0:02:39.80", "0:02:51.00", "Baby, I'm dancing in the dark", "With you between my arms", "Lyric"),
    ("0:02:51.00", "0:02:58.50", "Barefoot on the grass,", "Listening to our favorite song", "Lyric"),
    ("0:02:58.50", "0:03:05.50", "When I saw you in that dress,", "Looking so beautiful", "Lyric"),
    ("0:03:05.50", "0:03:15.50", "I don't deserve this, darling,", "You look perfect tonight", "Lyric"),
    # [Rest cut from 03:15.50 to 03:19.50 - 4s instrumental break!]

    # Chorus 3 (Outro Climax)
    ("0:03:19.50", "0:03:36.50", "Baby, I'm dancing in the dark", "With you between my arms", "Lyric"),
    ("0:03:36.50", "0:03:44.20", "Barefoot on the grass,", "Listening to our favorite song", "Lyric"),
    ("0:03:44.20", "0:03:54.00", "I have faith in what I see,", "Now I know I have met an angel in person", "Lyric"),
    ("0:03:54.00", "0:03:59.50", "And she looks perfect,", "I don't deserve this", "Lyric"),
    ("0:03:59.50", "0:04:06.00", "You look perfect tonight", "", "Lyric"),
    # [Rest cut from 04:06.00 to 04:18.00 - 12s orchestral guitar solo / rest cut!]
    ("0:04:18.50", "0:04:24.00", "You look perfect tonight", "", "Lyric"),
]

def time_to_sec(t_str):
    parts = t_str.split(":")
    return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])

def sec_to_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def generate_ass(speed_ratio=1.0, title_tag="Official 7clouds Edo SZ Edition"):
    header = f"""[Script Info]
Title: Ed Sheeran - Perfect ({title_tag})
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
; 1. Hero Title: Middle screen (Alignment=5, pos 960,450), Big Edo SZ 150pt
Style: HeroTitle,Edo SZ,150,&H00FFFFFF,&H000000FF,&H35000000,&H60000000,0,0,0,0,100,100,2.0,0,1,4.5,3.0,5,160,160,100,1
; 2. Hero Subtitle: Middle screen (Alignment=5, pos 960,560), Poppins SemiBold 42pt
Style: HeroSub,Poppins SemiBold,42,&H00FFFFFF,&H000000FF,&H40000000,&H60000000,0,0,0,0,100,100,6.0,0,1,2.5,2.0,5,160,160,100,1
; 3. Main Lyrics: Lower-third (Alignment=2, MarginV=240, 78% down), Edo SZ 56pt
Style: SevenCloudsLyric,Edo SZ,56,&H00FFFFFF,&H000000FF,&H35000000,&H60000000,0,0,0,0,100,100,1.5,0,1,3.2,2.2,2,160,160,240,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = []
    
    # 1. Big Hero Title in the MIDDLE (0.6s to 7.8s)
    s_intro = sec_to_time(0.60 / speed_ratio)
    e_intro = sec_to_time(7.80 / speed_ratio)
    events.append(f"Dialogue: 0,{s_intro},{e_intro},HeroTitle,,0,0,0,,{{\\pos(960,450)\\blur2.2}}PERFECT\n")
    events.append(f"Dialogue: 0,{s_intro},{e_intro},HeroSub,,0,0,0,,{{\\pos(960,560)\\blur1.8}}ED SHEERAN\n")

    # 2. Main Lyrics
    for s_str, e_str, l1, l2, kind in couplets_1x:
        s_sec = time_to_sec(s_str) / speed_ratio
        e_sec = time_to_sec(e_str) / speed_ratio
        s_out = sec_to_time(s_sec)
        e_out = sec_to_time(e_sec)

        style_name = "SevenCloudsLyric"
        if l2:
            text = f"{{\\blur1.8}}{l1}\\N{l2}"
        else:
            text = f"{{\\blur1.8}}{l1}"
        
        events.append(f"Dialogue: 0,{s_out},{e_out},{style_name},,0,0,0,,{text}\n")

    return header + "".join(events)

# 1. Slowed + Reverb ASS (R = 0.865)
slowed_ass = generate_ass(speed_ratio=0.865, title_tag="Slowed + Reverb • Hero Title Middle")
(song_dir / "lyrics_edosz_slowed.ass").write_text(slowed_ass, encoding="utf-8")
print(f"Generated lyrics_edosz_slowed.ass (Slowed + Reverb with Hero Title in Middle)")

# 2. Original 1.0x ASS
normal_ass = generate_ass(speed_ratio=1.0, title_tag="Original 1.0x • Hero Title Middle")
(song_dir / "lyrics_edosz_normal.ass").write_text(normal_ass, encoding="utf-8")
print(f"Generated lyrics_edosz_normal.ass (Original 1.0x with Hero Title in Middle)")
