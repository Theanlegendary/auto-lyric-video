import os
import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path('C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video')

def to_seconds(t_str):
    parts = t_str.split(':')
    return int(parts[0]) * 60 + float(parts[1])

def parse_lrc(lrc_path):
    parsed = []
    with open(lrc_path, 'r', encoding='utf-8') as f:
        for line in f:
            m = re.match(r'\[(\d{2}:\d{2}\.\d{2})\](.*)', line.strip())
            if m:
                t = to_seconds(m.group(1))
                txt = m.group(2).strip()
                if txt:
                    parsed.append((t, txt))
    return parsed

def make_couplets(parsed, max_gap=10.0):
    couplets = []
    i = 0
    while i < len(parsed):
        l1 = parsed[i]
        if i + 1 < len(parsed):
            l2 = parsed[i+1]
            gap = l2[0] - l1[0]
            # If two lines are close enough in time (within max_gap), pair them!
            if gap <= max_gap:
                couplets.append({
                    'lines': [l1, l2],
                    'vocal_start': l1[0],
                    'vocal_end': l2[0] + 3.0,
                    'text': f"{l1[1].strip().upper()}\\N{l2[1].strip().upper()}"
                })
                i += 2
                continue
        # Single line if gap is too large or last line
        couplets.append({
            'lines': [l1],
            'vocal_start': l1[0],
            'vocal_end': l1[0] + 3.5,
            'text': l1[1].strip().upper()
        })
        i += 1
    return couplets

def schedule_couplets(couplets, song_duration):
    events = []
    n = len(couplets)
    for idx in range(n):
        c = couplets[idx]
        v_start = c['vocal_start']
        
        # Determine display start
        # If idx == 0: lead in by up to 0.4s
        if idx == 0:
            disp_start = max(0.0, v_start - 0.4)
        else:
            prev_end = events[-1]['end']
            ideal_start = max(0.0, v_start - 0.4)
            # Must strictly start AFTER prev_end
            disp_start = max(prev_end + 0.05, ideal_start)
            
        # Determine display end
        if idx + 1 < n:
            next_v_start = couplets[idx+1]['vocal_start']
            gap = next_v_start - v_start
            if gap > 6.0:
                # Long gap (instrumental): hold text for last vocal line + 3.0s, then clear screen
                last_line_t = c['lines'][-1][0]
                disp_end = min(last_line_t + 3.5, next_v_start - 0.4)
            else:
                # Continuous flow: end 0.15s before next vocal start
                disp_end = max(disp_start + 1.5, next_v_start - 0.20)
        else:
            last_line_t = c['lines'][-1][0]
            disp_end = min(song_duration - 0.5, last_line_t + 4.0)
            
        # Ensure minimum duration
        if disp_end <= disp_start:
            disp_end = disp_start + 1.5
            
        events.append({
            'start': disp_start,
            'end': disp_end,
            'text': c['text'],
            'lines': c['lines']
        })
        
    return events

songs = [
    ('APT', 173.5),
    ('Die_With_A_Smile', 251.8),
    ('Taylor_Swift_The_Fate_of_Ophelia', 229.7),
    ('HUNTR_X_Golden', 191.0),
    ('Billie_Eilish_BIRDS_OF_A_FEATHER', 211.1)
]

for s_name, dur in songs:
    lrc_path = base / 'songs' / s_name / 'lyrics.lrc'
    parsed = parse_lrc(lrc_path)
    couplets = make_couplets(parsed)
    events = schedule_couplets(couplets, dur)
    
    # Audit for overlaps
    overlaps = []
    for i in range(len(events) - 1):
        e1 = events[i]
        e2 = events[i+1]
        if e2['start'] < e1['end']:
            overlaps.append((i, e1['end'] - e2['start'], e1, e2))
            
    print(f"=== {s_name} ===")
    print(f"Total raw lines: {len(parsed)} -> Total 2-row couplets: {len(events)}")
    print(f"Overlaps detected: {len(overlaps)}")
    if overlaps:
        for o in overlaps[:3]:
            print(f"  CRITICAL OVERLAP of {o[1]:.2f}s: [{o[2]['text']}] vs [{o[3]['text']}]")
    else:
        print("  PERFECT AUDIT! 0 overlaps! All couplets transition cleanly with guaranteed gaps.")
