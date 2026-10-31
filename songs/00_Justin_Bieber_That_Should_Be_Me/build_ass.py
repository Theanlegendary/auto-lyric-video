import sys
from pathlib import Path
from PIL import ImageFont

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\00_Justin_Bieber_That_Should_Be_Me")
font_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts\PatrickHand.ttf"
font = ImageFont.truetype(font_path, 96)

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

TRACK_DURATION = 216.48

# Balanced 2-row couplets (whisper-synced)
couplets = [
    # Intro Title Hook
    ("0:00:00.60", "0:00:06.50", "That Should Be Me", "Justin Bieber", "Title7Clouds"),

    # Verse 1
    ("0:00:06.80", "0:00:12.80", "Everybody's laughing in my mind", "", "Lyric7Clouds"),
    ("0:00:12.90", "0:00:18.40", "Rumors spreading", "'bout this other guy", "Lyric7Clouds"),
    ("0:00:18.60", "0:00:22.40", "Do you do what you did", "when you did with me?", "Lyric7Clouds"),
    ("0:00:22.50", "0:00:25.40", "Does he love you", "the way I can?", "Lyric7Clouds"),
    ("0:00:25.50", "0:00:29.00", "Did you forget all the plans", "that you made with me?", "Lyric7Clouds"),
    ("0:00:29.10", "0:00:32.20", "'Cause, baby, I didn't", "", "Lyric7Clouds"),

    # Chorus 1
    ("0:00:32.40", "0:00:39.10", "That should be me holding your hand", "That should be me making you laugh", "Lyric7Clouds"),
    ("0:00:39.20", "0:00:45.70", "That should be me, this is so sad", "That should be me, that should be me", "Lyric7Clouds"),
    ("0:00:45.80", "0:00:52.80", "That should be me feeling your kiss", "That should be me buying you gifts", "Lyric7Clouds"),
    ("0:00:52.90", "0:01:02.00", "This is so wrong, I can't go on", "'Til you believe that that should be me", "Lyric7Clouds"),
    ("0:01:02.20", "0:01:06.50", "That Should Be Me", "Justin Bieber", "Title7Clouds"),

    # Verse 2
    ("0:01:06.80", "0:01:14.20", "You said you needed a little time", "for my mistakes", "Lyric7Clouds"),
    ("0:01:14.40", "0:01:21.80", "It's funny how you used that time", "to have me replaced", "Lyric7Clouds"),
    ("0:01:22.00", "0:01:28.20", "Did you think that I wouldn't see you", "out at the movies?", "Lyric7Clouds"),
    ("0:01:28.40", "0:01:34.00", "What you doing to me?", "You're taking him where we used to go", "Lyric7Clouds"),
    ("0:01:34.20", "0:01:38.00", "Now if you're tryna break my heart", "It's working 'cause you know that...", "Lyric7Clouds"),

    # Chorus 2
    ("0:01:38.20", "0:01:44.20", "That should be me holding your hand", "That should be me making you laugh", "Lyric7Clouds"),
    ("0:01:44.40", "0:01:50.00", "That should be me, this is so sad", "That should be me, that should be me", "Lyric7Clouds"),
    ("0:01:50.20", "0:01:56.50", "That should be me feeling your kiss", "That should be me buying you gifts", "Lyric7Clouds"),
    ("0:01:56.70", "0:02:04.50", "This is so wrong, I can't go on", "'Til you believe that that should be me", "Lyric7Clouds"),

    # Bridge
    ("0:02:05.00", "0:02:11.80", "I need to know,", "should I fight for love or disarm?", "Lyric7Clouds"),
    ("0:02:12.00", "0:02:18.20", "It's getting harder to shield", "this pain in my heart", "Lyric7Clouds"),
    ("0:02:18.50", "0:02:24.50", "That Should Be Me", "Justin Bieber", "Title7Clouds"),

    # Chorus 3
    ("0:02:24.80", "0:02:32.00", "That should be me holding your hand", "That should be me making you laugh", "Lyric7Clouds"),
    ("0:02:32.20", "0:02:39.00", "That should be me, this is so sad", "That should be me, that should be me", "Lyric7Clouds"),
    ("0:02:39.20", "0:02:46.00", "That should be me feeling your kiss", "That should be me buying you gifts", "Lyric7Clouds"),
    ("0:02:46.20", "0:02:53.80", "This is so wrong, I can't go on", "'Til you believe that that should be me", "Lyric7Clouds"),

    # Outro
    ("0:02:54.00", "0:03:03.00", "Holding your hand, that should be me", "The one making you laugh, oh baby", "Lyric7Clouds"),
    ("0:03:03.50", "0:03:13.00", "That should be me giving you flowers", "That should be me talking for hours", "Lyric7Clouds"),
    ("0:03:13.20", "0:03:22.00", "That should be me, that should be me", "Oh baby, that should be me", "Lyric7Clouds"),
    ("0:03:23.00", "0:03:34.00", "That Should Be Me", "Justin Bieber", "Title7Clouds"),
]

# Check widths
max_w = 0
longest_str = ""
for s, e, l1, l2, st in couplets:
    for text_line in [l1, l2]:
        text_line = text_line.strip()
        if text_line:
            bbox = font.getbbox(text_line)
            w = bbox[2] - bbox[0]
            if w > max_w:
                max_w = w
                longest_str = text_line

print(f"Verified Max Line Width at size 96: {max_w}px (Safe limit: 1550px)")
print(f"Longest line: '{longest_str}'")

header_template = """[Script Info]
Title: Justin Bieber - That Should Be Me ({sub_title})
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

def format_event(start_sec, end_sec, l1, l2, style, loop_idx=0, is_title_start=False):
    s_str = sec_to_time(start_sec)
    e_str = sec_to_time(end_sec)
    if style == "Title7Clouds":
        if is_title_start and loop_idx > 0:
            sub = f"{l2} • Replay [{loop_idx}/5]"
        else:
            sub = l2
        text = f"{{\\pos(960,460)\\fad(500,400)}}{l1}\\N{{\\fs84\\fsp6\\b0}}{sub}"
    else:
        if l2:
            text = f"{{\\pos(960,490)\\fad(200,150)}}{l1}\\N{l2}"
        else:
            text = f"{{\\pos(960,510)\\fad(200,150)}}{l1}"
    return f"Dialogue: 0,{s_str},{e_str},{style},,0,0,0,,{text}\n"

# 1. Single Edition ASS
single_events = []
for start, end, l1, l2, style in couplets:
    s_sec = time_to_sec(start)
    e_sec = time_to_sec(end)
    single_events.append(format_event(s_sec, e_sec, l1, l2, style, loop_idx=0, is_title_start=(s_sec < 5)))

single_ass = header_template.format(sub_title="7clouds Clean Aesthetic Edition") + "".join(single_events)
single_file = song_dir / "lyrics_single.ass"
single_file.write_text(single_ass, encoding="utf-8")
print(f"Generated {single_file.name} ({len(single_events)} events)")

# 2. 20-Min 5x Replay (6 Total Loops) Edition ASS
NUM_LOOPS = 6
loop_events = []
for loop_idx in range(NUM_LOOPS):
    offset = loop_idx * TRACK_DURATION
    for start, end, l1, l2, style in couplets:
        s_sec = time_to_sec(start) + offset
        e_sec = time_to_sec(end) + offset
        is_title_start = (time_to_sec(start) < 5)
        loop_events.append(format_event(s_sec, e_sec, l1, l2, style, loop_idx=loop_idx, is_title_start=is_title_start))

total_dur_sec = NUM_LOOPS * TRACK_DURATION
print(f"Total duration: {total_dur_sec:.2f}s = {total_dur_sec/60:.2f} minutes")

loop_ass = header_template.format(sub_title="20-Min 5-Time Replay Edition") + "".join(loop_events)
loop_file = song_dir / "lyrics_20min_loop.ass"
loop_file.write_text(loop_ass, encoding="utf-8")
print(f"Generated {loop_file.name} ({len(loop_events)} events, 6 iterations / 5 replays)")
