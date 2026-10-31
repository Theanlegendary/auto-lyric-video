import re

lrc_file = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/APT/lyrics.lrc"

# Let's read all parsed lines
parsed = []
with open(lrc_file, "r", encoding="utf-8") as f:
    for line in f:
        m = re.match(r"\[(\d{2}:\d{2}\.\d{2})\](.*)", line.strip())
        if m:
            parts = m.group(1).split(":")
            sec = int(parts[0]) * 60 + float(parts[1])
            txt = m.group(2).strip()
            if txt:
                parsed.append((sec, txt))

for i, (t, txt) in enumerate(parsed):
    print(f"[{t:05.2f}] {txt}")
