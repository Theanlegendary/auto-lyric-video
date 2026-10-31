import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "25_The_Neighbourhood_Sweater_Weather"
in_ass = song_dir / "lyrics_glowing_white.ass"
out_ass = song_dir / "lyrics_slowed_reverb.ass"

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

R = 0.865

with open(in_ass, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith("Title:"):
        new_lines.append("Title: Sweater Weather - The Neighbourhood (Slowed + Reverb Glowing White Edition)\n")
    elif line.startswith("Dialogue:"):
        # Format: Dialogue: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
        parts = line.split(",", 9)
        start_sec = time_to_sec(parts[1]) / R
        end_sec = time_to_sec(parts[2]) / R
        
        parts[1] = sec_to_time(start_sec)
        parts[2] = sec_to_time(end_sec)
        
        text = parts[9]
        # For the opening title card, add Slowed + Reverb tag
        if "Sweater Weather" in text and "The Neighbourhood" in text and start_sec < 10:
            text = text.replace("The Neighbourhood", "The Neighbourhood (Slowed + Reverb)")
        elif "Sweater Weather" in text and "The Neighbourhood" in text and start_sec > 100:
            text = text.replace("The Neighbourhood", "The Neighbourhood (Slowed + Reverb)")
            
        parts[9] = text
        new_lines.append(",".join(parts))
    else:
        new_lines.append(line)

with open(out_ass, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"Generated {out_ass.name} successfully.")

# Inspect dialogue lines
print("\nVerifying dialogue lines:")
with open(out_ass, "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("Dialogue:"):
            parts = line.split(",", 9)
            print(f"[{parts[1]} --> {parts[2]}] {parts[3]}: {parts[9].strip()[:70]}")
