import re
import sys
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
sys.path.insert(0, str(base))
import auto_producer

srt_path = base / "official_birds.en-nP7-2PuUl7o.srt"
srt_content = srt_path.read_text(encoding="utf-8")

def parse_srt(content):
    # Split into subtitle blocks
    blocks = re.split(r'\n\s*\n', content.strip())
    entries = []
    for b in blocks:
        lines = [l.strip() for l in b.splitlines() if l.strip()]
        if len(lines) >= 3:
            # Time line: 00:00:03,833 --> 00:00:05,792
            m_time = re.match(r'(\d{2}:\d{2}:\d{2}[,\.]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[,\.]\d{3})', lines[1])
            if m_time:
                s_str, e_str = m_time.groups()
                def to_sec(ts):
                    ts = ts.replace(',', '.')
                    h, m, s = ts.split(':')
                    return int(h)*3600 + int(m)*60 + float(s)
                start_sec = to_sec(s_str)
                end_sec = to_sec(e_str)
                # Text lines
                text = " ".join(lines[2:])
                # Clean music notes and brackets
                text = re.sub(r'^[♪\s]+|[♪\s]+$', '', text)
                text = re.sub(r'\s*\([^)]*\)', '', text) # remove background ad-lib parentheticals for main line
                text = re.sub(r'\s+', ' ', text).strip().upper()
                if text and text != "":
                    entries.append({'start': start_sec, 'end': end_sec, 'text': text})
    return entries

entries = parse_srt(srt_content)
print(f"Parsed {len(entries)} official entries from SRT.")
for i, e in enumerate(entries[:8]):
    print(f"  {i}: [{e['start']:.2f} -> {e['end']:.2f}] {e['text']}")
