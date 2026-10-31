import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

def to_seconds(t_str):
    parts = t_str.split(":")
    return int(parts[0]) * 60 + float(parts[1])

def test_couplets(lrc_path):
    parsed = []
    with open(lrc_path, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\[(\d{2}:\d{2}\.\d{2})\](.*)", line.strip())
            if m:
                t = to_seconds(m.group(1))
                txt = m.group(2).strip()
                if txt:
                    parsed.append((t, txt))
                    
    couplets = []
    i = 0
    while i < len(parsed):
        l1 = parsed[i]
        if i + 1 < len(parsed):
            l2 = parsed[i+1]
            gap = l2[0] - l1[0]
            if gap <= 10.0:
                t_end = parsed[i+2][0] if i + 2 < len(parsed) else l2[0] + 4.5
                couplets.append({
                    "start": l1[0],
                    "end": t_end,
                    "text": f"{l1[1].strip().upper()}\\N{l2[1].strip().upper()}"
                })
                i += 2
                continue
        t_end = parsed[i+1][0] if i + 1 < len(parsed) else l1[0] + 4.5
        couplets.append({
            "start": l1[0],
            "end": t_end,
            "text": l1[1].strip().upper()
        })
        i += 1
    return couplets

lrc_p = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/Taylor_Swift_The_Fate_of_Ophelia/lyrics.lrc"
couplets = test_couplets(lrc_p)
print(f"Total couplets generated: {len(couplets)}")
for c in couplets[:8]:
    print(f"[{c['start']:05.2f}s -> {c['end']:05.2f}s]:")
    print(f"  {repr(c['text'])}")
    print("-" * 40)
