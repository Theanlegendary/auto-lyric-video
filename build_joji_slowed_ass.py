import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/27_Joji_Glimpse_of_Us")
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

lines = in_ass.read_text(encoding="utf-8").splitlines()
new_lines = []

for line in lines:
    if line.startswith("Title:"):
        new_lines.append("Title: Joji - Glimpse of Us (Slowed + Reverb Glowing White Edition)")
    elif line.startswith("Dialogue:"):
        parts = line.split(",", 9)
        start_sec = time_to_sec(parts[1]) / R
        end_sec = time_to_sec(parts[2]) / R
        
        parts[1] = sec_to_time(start_sec)
        parts[2] = sec_to_time(end_sec)
        
        text = parts[9]
        if "Glimpse of Us" in text and "Joji" in text and "\\N" in text:
            text = text.replace("Joji", "Joji (Slowed + Reverb)")
        parts[9] = text
        new_lines.append(",".join(parts))
    else:
        new_lines.append(line)

out_ass.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
print(f"Generated {out_ass.name} successfully.")

# Verify lines
for l in new_lines:
    if l.startswith("Dialogue:"):
        p = l.split(",", 9)
        print(f"[{p[1]} -> {p[2]}] {p[9][:60]}")
