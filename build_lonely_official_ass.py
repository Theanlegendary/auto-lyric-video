import sys
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
sys.path.insert(0, str(base))
import auto_producer

# Define the exact section-aware couplets for Lonely with official studio timestamps:
groups = [
    # Verse 1
    ([(13.18, "EVERYBODY KNOWS MY NAME NOW"), (15.85, "BUT SOMETHING 'BOUT IT STILL FEELS STRANGE")], 13.18, 19.02, "EVERYBODY KNOWS MY NAME NOW\\NBUT SOMETHING 'BOUT IT STILL FEELS STRANGE"),
    ([(19.02, "LIKE LOOKING IN A MIRROR, TRYING TO STEADY YOURSELF"), (21.52, "AND SEEING SOMEBODY ELSE")], 19.02, 23.52, "LIKE LOOKING IN A MIRROR, TRYING TO STEADY YOURSELF\\NAND SEEING SOMEBODY ELSE"),
    ([(24.86, "AND EVERYTHING IS NOT THE SAME NOW"), (27.82, "IT FEELS LIKE ALL OUR LIVES HAVE CHANGED")], 24.86, 30.95, "AND EVERYTHING IS NOT THE SAME NOW\\NIT FEELS LIKE ALL OUR LIVES HAVE CHANGED"),
    ([(30.95, "MAYBE WHEN I'M OLDER IT WILL ALL CALM DOWN"), (33.66, "BUT IT'S KILLING ME NOW")], 30.95, 36.50, "MAYBE WHEN I'M OLDER IT WILL ALL CALM DOWN\\NBUT IT'S KILLING ME NOW"),
    
    # Chorus 1
    ([(37.45, "WHAT IF YOU HAD IT ALL"), (40.50, "BUT NOBODY TO CALL?")], 37.45, 43.67, "WHAT IF YOU HAD IT ALL\\NBUT NOBODY TO CALL?"),
    ([(43.67, "MAYBE THEN YOU'D KNOW ME"), (49.51, "'CAUSE I'VE HAD EVERYTHING")], 43.67, 52.39, "MAYBE THEN YOU'D KNOW ME\\N'CAUSE I'VE HAD EVERYTHING"),
    ([(52.39, "BUT NO ONE'S LISTENING"), (55.60, "AND THAT'S JUST FUCKIN' LONELY")], 52.39, 58.52, "BUT NO ONE'S LISTENING\\NAND THAT'S JUST FUCKIN' LONELY"),
    
    # Post-Chorus 1
    ([(59.39, "I'M SO LONELY..."), (66.07, "LONELY...")], 59.39, 72.00, "I'M SO LONELY...\\NLONELY..."),
    
    # Verse 2
    ([(72.95, "EVERYBODY KNOWS MY PAST NOW"), (75.74, "LIKE MY HOUSE WAS ALWAYS MADE OF GLASS")], 72.95, 78.79, "EVERYBODY KNOWS MY PAST NOW\\NLIKE MY HOUSE WAS ALWAYS MADE OF GLASS"),
    ([(78.79, "AND MAYBE THAT'S THE PRICE YOU PAY"), (80.91, "FOR THE MONEY AND FAME AT AN EARLY AGE")], 78.79, 84.75, "AND MAYBE THAT'S THE PRICE YOU PAY\\NFOR THE MONEY AND FAME AT AN EARLY AGE"),
    ([(84.75, "AND EVERYBODY SAW ME SICK"), (87.75, "AND IT FELT LIKE NO ONE GAVE A SHIT")], 84.75, 90.47, "AND EVERYBODY SAW ME SICK\\NAND IT FELT LIKE NO ONE GAVE A SHIT"),
    ([(90.47, "THEY CRITICIZED THE THINGS I DID"), (92.93, "AS AN IDIOT KID")], 90.47, 96.00, "THEY CRITICIZED THE THINGS I DID\\NAS AN IDIOT KID"),
    
    # Chorus 2
    ([(97.51, "WHAT IF YOU HAD IT ALL"), (100.27, "BUT NOBODY TO CALL?")], 97.51, 103.65, "WHAT IF YOU HAD IT ALL\\NBUT NOBODY TO CALL?"),
    ([(103.65, "MAYBE THEN YOU'D KNOW ME"), (109.40, "'CAUSE I'VE HAD EVERYTHING")], 103.65, 112.36, "MAYBE THEN YOU'D KNOW ME\\N'CAUSE I'VE HAD EVERYTHING"),
    ([(112.36, "BUT NO ONE'S LISTENING"), (115.53, "AND THAT'S JUST FUCKIN' LONELY")], 112.36, 118.49, "BUT NO ONE'S LISTENING\\NAND THAT'S JUST FUCKIN' LONELY"),
    
    # Outro
    ([(119.41, "I'M SO LONELY..."), (126.04, "LONELY...")], 119.41, 131.00, "I'M SO LONELY...\\NLONELY..."),
    ([(131.30, "I'M SO LONELY..."), (138.22, "LONELY...")], 131.30, 145.00, "I'M SO LONELY...\\NLONELY...")
]

title_end = 12.20
song_duration = 149.42

scheduled = []
n = len(groups)
for idx in range(n):
    grp = groups[idx]
    v_start = grp[1]
    v_end = grp[2]
    txt = grp[3]
    
    ideal_start = max(0.0, v_start - 0.30)
    if idx == 0:
        disp_start = max(title_end + 0.10, ideal_start)
    else:
        prev_end = scheduled[-1]['end']
        disp_start = max(prev_end + 0.05, ideal_start)
        
    if idx + 1 < n:
        next_v_start = groups[idx+1][1]
        ideal_end = max(v_end + 0.60, next_v_start - 0.20)
        disp_end = min(ideal_end, next_v_start - 0.20)
    else:
        disp_end = min(song_duration - 1.0, v_end + 2.5)
        
    if disp_end <= disp_start:
        disp_end = disp_start + 2.0
        
    scheduled.append({'start': disp_start, 'end': disp_end, 'text': txt})

events = []
# Official Cinematic TitleCard
events.append(
    f"Dialogue: 0,0:00:01.50,{auto_producer.to_ass_time(title_end)},TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(600,400)}}LONELY\\N{{\\fs75\\fsp4}}Justin Bieber & benny blanco"
)

for item in scheduled:
    s_str = auto_producer.to_ass_time(item['start'])
    e_str = auto_producer.to_ass_time(item['end'])
    events.append(
        f"Dialogue: 0,{s_str},{e_str},Lyric,,0,0,0,,{{\\pos(960,490)\\fad(220,150)}}{item['text']}"
    )

song_dir = base / "songs" / "14_Justin_Bieber_Lonely"
ass_path = song_dir / "lyrics_couplets_final.ass"
header = auto_producer.styles_white
ass_path.write_text(header + "\n".join(events), encoding="utf-8")
print(f"SUCCESS: Generated {len(events)} ASS events for Lonely!")
for e in events[:4]:
    print(" ", e)
