import sys
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
sys.path.insert(0, str(base))
import auto_producer
from parse_official_srt import entries

# Remove electrical buzzing entry (index 38)
clean_entries = entries[:38]

# Group entries into official couplets:
# Pairs: (0,1), (2,3), (4,5), (6,7), (8,9), (10,11), (12,13), (14,15), (16,17), 
# Single: 18,
# Pairs: (19,20), (21,22), (23,24), (25,26), (27,28), (29,30), (31,32), (33,34), (35,36),
# Single: 37
couplet_groups = [
    [0, 1],
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
    [10, 11],
    [12, 13],
    [14, 15],
    [16, 17],
    [18],
    [19, 20],
    [21, 22],
    [23, 24],
    [25, 26],
    [27, 28],
    [29, 30],
    [31, 32],
    [33, 34],
    [35, 36],
    [37]
]

couplets = []
for grp in couplet_groups:
    lines = [clean_entries[idx] for idx in grp]
    v_start = lines[0]['start']
    v_end = lines[-1]['end']
    text = "\\N".join(l['text'] for l in lines)
    couplets.append({
        'v_start': v_start,
        'v_end': v_end,
        'text': text
    })

# Title card ends at 00:03.40 (before vocal at 03.83)
title_end = 3.40

# Build scheduled items
scheduled = []
n = len(couplets)
for idx in range(n):
    c = couplets[idx]
    v_start = c['v_start']
    v_end = c['v_end']
    
    # Start: 0.30s lead-in
    ideal_start = max(0.0, v_start - 0.30)
    if idx == 0:
        disp_start = max(title_end + 0.10, ideal_start)
    else:
        prev_end = scheduled[-1]['end']
        disp_start = max(prev_end + 0.05, ideal_start)
        
    # End: Hold until official vocal end, or right before next lyric starts
    if idx + 1 < n:
        next_v_start = couplets[idx+1]['v_start']
        # End at either official vocal end + 0.8s hold, or next_v_start - 0.20s
        ideal_end = max(v_end + 0.80, next_v_start - 0.20)
        disp_end = min(ideal_end, next_v_start - 0.20)
    else:
        disp_end = min(210.0, v_end + 3.0)
        
    if disp_end <= disp_start:
        disp_end = disp_start + 2.0
        
    scheduled.append({
        'start': disp_start,
        'end': disp_end,
        'text': c['text']
    })

events = []
# TitleCard
events.append(
    f"Dialogue: 0,0:00:00.60,{auto_producer.to_ass_time(title_end)},TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(500,400)}}BIRDS OF A FEATHER\\N{{\\fs80\\fsp4}}Billie Eilish"
)

for item in scheduled:
    s_str = auto_producer.to_ass_time(item['start'])
    e_str = auto_producer.to_ass_time(item['end'])
    events.append(
        f"Dialogue: 0,{s_str},{e_str},Lyric,,0,0,0,,{{\\pos(960,490)\\fad(180,120)}}{item['text']}"
    )

ass_path = base / "songs" / "05_Billie_Eilish_BIRDS_OF_A_FEATHER_Pink_Edition" / "lyrics_couplets_final.ass"
header = auto_producer.styles_black
ass_path.write_text(header + "\n".join(events), encoding="utf-8")
print(f"SUCCESS: Generated {len(events)} ASS events from Official SRT!")
for i, ev in enumerate(events[:8]):
    print(f"  {i}: {ev}")
