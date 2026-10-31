import sys
from pathlib import Path
from PIL import ImageFont

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\30_Ed_Sheeran_Perfect")
font_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts\PatrickHand.ttf")
font = ImageFont.truetype(str(font_path), 96)

def time_to_sec(t_str):
    parts = t_str.split(":")
    h = int(parts[0])
    m = int(parts[1])
    s = float(parts[2])
    return h * 3600 + m * 60 + s

def sec_to_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

# Base 1.0x couplets for Ed Sheeran - Perfect
# Whisper-verified and couplet balanced (<= 2 rows)
couplets_1x = [
    # Intro Title Hook
    ("0:00:00.60", "0:00:07.50", "Perfect", "Ed Sheeran", "Title7Clouds"),

    # Verse 1
    ("0:00:07.80", "0:00:12.20", "I found a love for me,", "darling, just dive right in", "Lyric7Clouds"),
    ("0:00:12.40", "0:00:16.50", "and follow my lead", "", "Lyric7Clouds"),
    ("0:00:16.80", "0:00:24.50", "Well, I found a girl,", "beautiful and sweet", "Lyric7Clouds"),
    ("0:00:24.80", "0:00:31.50", "Oh, I never knew you were the someone", "waiting for me", "Lyric7Clouds"),

    # Pre-Chorus 1
    ("0:00:31.80", "0:00:40.20", "'Cause we were just kids", "when we fell in love", "Lyric7Clouds"),
    ("0:00:40.50", "0:00:47.50", "Not knowing what it was,", "I will not give you up this time", "Lyric7Clouds"),
    ("0:00:47.80", "0:00:55.00", "Darling, just kiss me slow,", "your heart is all I own", "Lyric7Clouds"),
    ("0:00:55.20", "0:01:02.20", "And in your eyes,", "you're holding mine", "Lyric7Clouds"),

    # Chorus 1
    ("0:01:02.50", "0:01:09.00", "Baby, I'm dancing in the dark", "with you between my arms", "Lyric7Clouds"),
    ("0:01:09.20", "0:01:17.00", "Barefoot on the grass,", "listening to our favorite song", "Lyric7Clouds"),
    ("0:01:17.20", "0:01:23.50", "When you said you looked a mess,", "I whispered underneath my breath", "Lyric7Clouds"),
    ("0:01:23.80", "0:01:35.00", "But you heard it, darling,", "you look perfect tonight", "Lyric7Clouds"),

    # Instrumental Hook
    ("0:01:35.50", "0:01:40.00", "Perfect", "Ed Sheeran", "Title7Clouds"),

    # Verse 2
    ("0:01:40.20", "0:01:47.50", "Well, I found a woman,", "stronger than anyone I know", "Lyric7Clouds"),
    ("0:01:47.80", "0:01:54.80", "She shares my dreams,", "I hope that someday I'll share her home", "Lyric7Clouds"),
    ("0:01:55.00", "0:01:59.50", "I found a lover,", "to carry more than just my secrets", "Lyric7Clouds"),
    ("0:01:59.80", "0:02:04.00", "To carry love,", "to carry children of our own", "Lyric7Clouds"),

    # Pre-Chorus 2
    ("0:02:04.20", "0:02:13.50", "We are still kids, but we're so in love", "Fighting against all odds", "Lyric7Clouds"),
    ("0:02:13.80", "0:02:20.50", "I know we'll be alright this time", "", "Lyric7Clouds"),
    ("0:02:20.80", "0:02:27.50", "Darling, just hold my hand,", "be my girl, I'll be your man", "Lyric7Clouds"),
    ("0:02:27.80", "0:02:35.50", "I see my future in your eyes", "", "Lyric7Clouds"),

    # Chorus 2
    ("0:02:35.80", "0:02:43.00", "Baby, I'm dancing in the dark", "with you between my arms", "Lyric7Clouds"),
    ("0:02:43.20", "0:02:51.00", "Barefoot on the grass,", "listening to our favorite song", "Lyric7Clouds"),
    ("0:02:51.20", "0:02:57.50", "When I saw you in that dress,", "looking so beautiful", "Lyric7Clouds"),
    ("0:02:57.80", "0:03:07.50", "I don't deserve this, darling,", "you look perfect tonight", "Lyric7Clouds"),

    # Chorus 3 (Outro Climax)
    ("0:03:07.80", "0:03:19.50", "Baby, I'm dancing in the dark", "with you between my arms", "Lyric7Clouds"),
    ("0:03:19.80", "0:03:26.50", "Barefoot on the grass,", "listening to our favorite song", "Lyric7Clouds"),
    ("0:03:26.80", "0:03:34.50", "I have faith in what I see,", "now I know I have met an angel in person", "Lyric7Clouds"),
    ("0:03:34.80", "0:03:44.50", "And she looks perfect,", "I don't deserve this", "Lyric7Clouds"),
    ("0:03:44.80", "0:03:58.00", "You look perfect tonight", "", "Lyric7Clouds"),
    ("0:03:58.50", "0:04:22.00", "Perfect", "Ed Sheeran", "Title7Clouds"),
]

# Verify line widths
max_w = 0
longest_str = ""
for s, e, l1, l2, st in couplets_1x:
    for text_line in [l1, l2]:
        text_line = text_line.strip()
        if text_line:
            bbox = font.getbbox(text_line)
            w = bbox[2] - bbox[0]
            if w > max_w:
                max_w = w
                longest_str = text_line

print(f"Max Line Width at 96pt: {max_w}px (Safe screen margin limit: 1560px)")
print(f"Longest line: '{longest_str}'")
if max_w < 1560:
    print("VERIFICATION PASS: All lines fit comfortably without clipping!")

header_template = """[Script Info]
Title: Ed Sheeran - Perfect ({sub_title})
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Title7Clouds,Patrick Hand,170,&H00FFFFFF,&H000000FF,&H00101828,&H80000000,-1,0,0,0,100,100,5,0,1,4.0,2.5,5,180,180,110,1
Style: Lyric7Clouds,Patrick Hand,96,&H00FFFFFF,&H000000FF,&H00101828,&H80000000,-1,0,0,0,100,100,2,0,1,3.8,2.2,5,180,180,110,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

# Build Slowed + Reverb ASS (R = 0.865)
R = 0.865

def build_ass(edition_name, tag):
    events = []
    for s_str, e_str, l1, l2, style in couplets_1x:
        s_sec = time_to_sec(s_str) / R
        e_sec = time_to_sec(e_str) / R
        s_out = sec_to_time(s_sec)
        e_out = sec_to_time(e_sec)
        
        if style == "Title7Clouds":
            sub = f"{l2} • {tag}"
            text = f"{{\\pos(960,460)\\fad(500,400)}}{l1}\\N{{\\fs84\\fsp6\\b0}}{sub}"
        else:
            if l2:
                text = f"{{\\pos(960,490)\\fad(200,150)}}{l1}\\N{l2}"
            else:
                text = f"{{\\pos(960,510)\\fad(200,150)}}{l1}"
        events.append(f"Dialogue: 0,{s_out},{e_out},{style},,0,0,0,,{text}\n")
    
    content = header_template.format(sub_title=edition_name) + "".join(events)
    return content

# 1. Pink Mode ASS
pink_ass = build_ass("Pink Mode • Slowed + Reverb", "Pink Edition (Slowed + Reverb)")
(song_dir / "lyrics_pink_slowed.ass").write_text(pink_ass, encoding="utf-8")
print(f"Generated lyrics_pink_slowed.ass ({len(couplets_1x)} events)")

# 2. Sunset Mode ASS
sunset_ass = build_ass("Sunset Mode • Slowed + Reverb", "Sunset Edition (Slowed + Reverb)")
(song_dir / "lyrics_sunset_slowed.ass").write_text(sunset_ass, encoding="utf-8")
print(f"Generated lyrics_sunset_slowed.ass ({len(couplets_1x)} events)")
