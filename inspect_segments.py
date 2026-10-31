import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/27_Joji_Glimpse_of_Us")

# Let's inspect the whisper words file to build couplets
words_file = song_dir / "whisper_words.txt"
content = words_file.read_text(encoding="utf-8")

# Let's print out the segments
segments = []
for line in content.splitlines():
    if line.startswith("[") and "->" in line:
        parts = line.split("]")
        time_part = parts[0].strip("[")
        text_part = parts[1].strip()
        t_start, t_end = [float(x.strip()) for x in time_part.split("->")]
        segments.append((t_start, t_end, text_part))

for i, (ts, te, txt) in enumerate(segments):
    print(f"{i+1:02d}: [{ts:6.2f} -> {te:6.2f}] {txt}")
