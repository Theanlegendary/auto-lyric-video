import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
songs_dir = base / "songs"

def smart_format_lyric(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)
    
    # Check parenthetical at end
    m_paren = re.search(r"^(.*?)\s*(\([^\)]+\))$", text)
    if m_paren:
        main_part = m_paren.group(1).strip()
        paren_part = m_paren.group(2).strip()
        if len(main_part) >= 12:
            return f"{main_part.upper()}\\N{paren_part.upper()}"
            
    # Short line threshold: keep as 1 clean line!
    words = text.split()
    if len(text) < 34 and len(words) < 8:
        return text.upper()
        
    # Natural comma split
    if "," in text:
        comma_indices = [m.start() for m in re.finditer(r",", text)]
        midpoint = len(text) / 2
        best_comma = min(comma_indices, key=lambda idx: abs(idx - midpoint))
        p1 = text[:best_comma].strip()
        p2 = text[best_comma + 1:].strip()
        if len(p1) >= 8 and len(p2) >= 8:
            return f"{p1.upper()}\\N{p2.upper()}"
            
    # Midpoint split
    mid = len(words) // 2
    p1 = " ".join(words[:mid]).strip()
    p2 = " ".join(words[mid:]).strip()
    return f"{p1.upper()}\\N{p2.upper()}"

def to_seconds(t_str):
    parts = t_str.split(":")
    return int(parts[0]) * 60 + float(parts[1])

songs = [
    ("APT.", "songs/APT/lyrics.lrc"),
    ("Die With A Smile", "songs/Die_With_A_Smile/lyrics.lrc"),
    ("The Fate of Ophelia", "songs/Taylor_Swift_The_Fate_of_Ophelia/lyrics.lrc"),
    ("Golden", "songs/HUNTR_X_Golden/lyrics.lrc"),
    ("BIRDS OF A FEATHER", "songs/Billie_Eilish_BIRDS_OF_A_FEATHER/lyrics.lrc")
]

print("==================== INTRO TIMING AUDIT ====================")
for title, lrc_rel in songs:
    lrc_path = base / lrc_rel
    parsed = []
    with open(lrc_path, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\[(\d{2}:\d{2}\.\d{2})\](.*)", line.strip())
            if m:
                t = to_seconds(m.group(1))
                txt = m.group(2).strip()
                if txt:
                    parsed.append((t, txt))
    first_t = parsed[0][0] if parsed else 0.0
    
    # Calculate dynamic blur timing
    if first_t <= 3.5:
        t_blur_start = 0.5
        t_blur_end = 3.0
    else:
        t_blur_start = max(1.0, first_t - 2.5)
        t_blur_end = first_t
        
    print(f"SONG: {title}")
    print(f"  First Vocal Starts at : {first_t:.2f}s")
    print(f"  Background Sharp Until: {t_blur_start:.2f}s (No premature fade!)")
    print(f"  Blur Dissolve Window  : {t_blur_start:.2f}s -> {t_blur_end:.2f}s (2.5s smooth transition)")
    print(f"  First 3 Formatted Lines:")
    for t, txt in parsed[:3]:
        print(f"    [{t:05.2f}] -> {repr(smart_format_lyric(txt))}")
    print("-" * 55)
