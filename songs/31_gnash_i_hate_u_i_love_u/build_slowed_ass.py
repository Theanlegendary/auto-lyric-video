import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# 0.865 varispeed factor
SPEED = 0.865

def time_to_seconds(t_str):
    parts = t_str.split(':')
    h = int(parts[0])
    m = int(parts[1])
    s = float(parts[2])
    return h * 3600 + m * 60 + s

def seconds_to_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

src_ass = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\31_gnash_i_hate_u_i_love_u\lyrics_7clouds_clean.ass")
out_ass = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\31_gnash_i_hate_u_i_love_u\lyrics_7clouds_clean_slowed.ass")

lines = src_ass.read_text(encoding='utf-8').splitlines()
out_lines = []

for line in lines:
    if line.startswith("Dialogue:"):
        # Format: Dialogue: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
        parts = line.split(',', 9)
        start_sec = time_to_seconds(parts[1]) / SPEED
        end_sec = time_to_seconds(parts[2]) / SPEED
        parts[1] = seconds_to_time(start_sec)
        parts[2] = seconds_to_time(end_sec)
        out_lines.append(','.join(parts))
    else:
        out_lines.append(line)

out_ass.write_text('\n'.join(out_lines) + '\n', encoding='utf-8')
print("Successfully created slowed ASS subtitles:", out_ass.name)
