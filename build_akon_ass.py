import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

song_dir = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/15_Akon_Lonely"

# Format time to ASS format: H:MM:SS.cc
def fmt_ass(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

# Raw parsed events from lrclib_synced.lrc:
# We will create couplets with strict timing:
# Title card: 00:01.00 -> 00:09.50
# Intro sample:
# 1. 00:10.13 -> 00:20.20: I'M SO LONELY, I'M MR. LONELY \N I HAVE NOBODY FOR MY OWN
# 2. 00:20.74 -> 00:23.80: I'M SO LONELY
# Spoken Intro:
# 3. 00:24.38 -> 00:32.00: YO! THIS ONE HERE \N GOES OUT TO ALL MY PLAYERS OUT THERE MAN, YA KNOW
# 4. 00:32.49 -> 00:38.20: THAT GOT THAT ONE GOOD GIRL WHO'S ALWAYS BEEN THERE MAN, LIKE \N TOOK ALL THE BULLSHIT
# 5. 00:38.75 -> 00:42.50: BUT THEN ONE DAY SHE CAN'T TAKE IT NO MORE AND DECIDE TO LEAVE \N YEAH
# Verse 1:
# 6. 00:42.99 -> 00:47.80: I WOKE UP IN THE MIDDLE OF THE NIGHT \N AND I NOTICED MY GIRL WASN'T BY MY SIDE
# 7. 00:48.21 -> 00:53.10: COULDA SWORN I WAS DREAMING, FOR HER I WAS FEENIN' \N SO I HAD TO TAKE A LITTLE RIDE
# 8. 00:53.55 -> 00:58.50: BACK TRACKING OVER THESE FEW YEARS \N TRYNA FIGURE OUT WHAT I DO TO MAKE IT GO BAD
# 9. 00:58.92 -> 01:03.80: 'CAUSE EVER SINCE MY GIRL LEFT ME \N MY WHOLE LIFE CAME CRASHING AND I'M SO
# Chorus 1:
# 10. 01:04.18 -> 01:08.50: LONELY (SO LONELY) \N I'M MR. LONELY (MR. LONELY)
# 11. 01:08.88 -> 01:14.10: I HAVE NOBODY (I HAVE NOBODY) \N FOR MY OWN (TO CALL MY OWN GIRL)
# 12. 01:14.54 -> 01:19.20: I'M SO LONELY (SO LONELY) \N I'M MR. LONELY (MR. LONELY)
# 13. 01:19.59 -> 01:25.20: I HAVE NOBODY (I HAVE NOBODY) \N FOR MY OWN (TO CALL MY OWN GIRL)
# Verse 2:
# 14. 01:25.64 -> 01:30.50: CAN'T BELIEVE I HAD A GIRL LIKE YOU \N AND I JUST LET YOU WALK RIGHT OUTTA MY LIFE
# 15. 01:30.93 -> 01:35.80: AFTER ALL I PUT YOU THROUGH \N YOU STILL STUCK AROUND AND STAYED BY MY SIDE
# 16. 01:36.25 -> 01:41.00: WHAT REALLY HURT ME IS I BROKE YOUR HEART \N BABY YOU A GOOD GIRL AND I HAD NO RIGHT
# 17. 01:41.46 -> 01:46.40: I REALLY WANNA MAKE THINGS RIGHT \N 'CAUSE WITHOUT YOU IN MY LIFE GIRL I'M SO
# Chorus 2:
# 18. 01:46.89 -> 01:51.00: LONELY (SO LONELY) \N I'M MR. LONELY (MR. LONELY)
# 19. 01:51.38 -> 01:56.80: I HAVE NOBODY (I HAVE NOBODY) \N FOR MY OWN (TO CALL MY OWN GIRL)
# 20. 01:57.22 -> 02:01.60: I'M SO LONELY (SO LONELY) \N I'M MR. LONELY (MR. LONELY)
# 21. 02:02.07 -> 02:07.90: I HAVE NOBODY (I HAVE NOBODY) \N FOR MY OWN (TO CALL MY OWN BABY)
# Verse 3:
# 22. 02:08.44 -> 02:13.10: BEEN ALL ABOUT THE WORLD AIN'T NEVER MET A GIRL \N THAT COULD TAKE THE THINGS THAT YOU BEEN THROUGH
# 23. 02:13.51 -> 02:18.50: NEVER THOUGHT THE DAY WOULD COME WHERE YOU WOULD GET UP AND RUN \N AND I WOULD BE OUT CHASING YOU
# 24. 02:18.99 -> 02:23.70: 'CAUSE AIN'T NOWHERE IN THE GLOBE I'D RATHER BE \N AIN'T NO ONE IN THE GLOBE I'D RATHER SEE
# 25. 02:24.15 -> 02:29.10: THAN THE GIRL OF MY DREAMS THAT MADE ME BE \N SO HAPPY BUT NOW SO LONELY
# Chorus 3:
# 26. 02:29.54 -> 02:33.80: LONELY (SO LONELY) \N I'M MR. LONELY (MR. LONELY)
# 27. 02:34.28 -> 02:39.50: I HAVE NOBODY (I HAVE NOBODY) \N FOR MY OWN (TO CALL MY OWN NO)
# 28. 02:39.99 -> 02:44.20: I'M SO LONELY (SO LONELY) \N I'M MR. LONELY (MR. LONELY)
# 29. 02:44.58 -> 02:49.80: I HAVE NOBODY (I HAVE NOBODY) \N FOR MY OWN (TO CALL MY OWN GIRL)
# Bridge:
# 30. 02:50.36 -> 02:55.90: LONELY \N NEVER THOUGHT THAT I'D BE ALONE (BE ALONE)
# 31. 02:56.42 -> 03:01.20: I DIDN'T THINK YOU'D BE GONE THIS LONG (GONE SO LONG) \N I JUST WANT YOU TO CALL MY PHONE
# 32. 03:01.63 -> 03:06.40: STOP PLAYING GIRL AND COME ON HOME (COME ON HOME) \N BABY GIRL, I DIDN'T MEAN TO SHOUT
# 33. 03:06.84 -> 03:11.40: I WANT ME AND YOU TO WORK IT OUT (WORK IT OUT BABY) \N I'D NEVER WISH TO EVER HURT MY BABY
# 34. 03:11.90 -> 03:16.20: AND IT'S DRIVING ME CRAZY 'CAUSE I'M SO \N LONELY (SO LONELY)
# Chorus 4:
# 35. 03:16.72 -> 03:21.90: I'M MR. LONELY (MR. LONELY) \N I HAVE NOBODY (I HAVE NOBODY)
# 36. 03:22.39 -> 03:26.90: FOR MY OWN (TO CALL MY OWN NO) \N I'M SO LONELY (SO LONELY)
# 37. 03:27.47 -> 03:32.30: I'M MR. LONELY (MR. LONELY) \N I HAVE NOBODY (I HAVE NOBODY)
# Outro:
# 38. 03:32.80 -> 03:38.30: FOR MY OWN (TO CALL MY OWN GIRL) \N I AM SO LONELY
# 39. 03:38.76 -> 03:44.30: SO LONELY (LONELY) \N SO LONELY (SO LONELY)
# 40. 03:44.78 -> 03:49.60: MR. LONELY (LONELY) \N SO LONELY (SO LONELY)
# 41. 03:50.09 -> 03:54.50: SO LONELY (LONELY) \N SO LONELY, MR. LONELY

raw_couplets = [
    (1.00, 9.50, "TITLE", "LONELY\\N{\\fs75\\fsp4}Akon"),
    (10.13, 20.20, "LYRIC", "I'M SO LONELY, I'M MR. LONELY\\NI HAVE NOBODY FOR MY OWN"),
    (20.74, 23.80, "LYRIC", "I'M SO LONELY"),
    (24.38, 32.00, "LYRIC", "YO! THIS ONE HERE\\NGOES OUT TO ALL MY PLAYERS OUT THERE MAN, YA KNOW"),
    (32.49, 38.20, "LYRIC", "THAT GOT THAT ONE GOOD GIRL WHO'S ALWAYS BEEN THERE MAN, LIKE\\NTOOK ALL THE BULLSHIT"),
    (38.75, 42.50, "LYRIC", "BUT THEN ONE DAY SHE CAN'T TAKE IT NO MORE AND DECIDE TO LEAVE\\NYEAH"),
    (42.99, 47.80, "LYRIC", "I WOKE UP IN THE MIDDLE OF THE NIGHT\\NAND I NOTICED MY GIRL WASN'T BY MY SIDE"),
    (48.21, 53.10, "LYRIC", "COULDA SWORN I WAS DREAMING, FOR HER I WAS FEENIN'\\NSO I HAD TO TAKE A LITTLE RIDE"),
    (53.55, 58.50, "LYRIC", "BACK TRACKING OVER THESE FEW YEARS\\NTRYNA FIGURE OUT WHAT I DO TO MAKE IT GO BAD"),
    (58.92, 63.80, "LYRIC", "'CAUSE EVER SINCE MY GIRL LEFT ME\\nMY WHOLE LIFE CAME CRASHING AND I'M SO"),
    (64.18, 68.50, "LYRIC", "LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (68.88, 74.10, "LYRIC", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN GIRL)"),
    (74.54, 79.20, "LYRIC", "I'M SO LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (79.59, 85.20, "LYRIC", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN GIRL)"),
    (85.64, 90.50, "LYRIC", "CAN'T BELIEVE I HAD A GIRL LIKE YOU\\nAND I JUST LET YOU WALK RIGHT OUTTA MY LIFE"),
    (90.93, 95.80, "LYRIC", "AFTER ALL I PUT YOU THROUGH\\nYOU STILL STUCK AROUND AND STAYED BY MY SIDE"),
    (96.25, 101.00, "LYRIC", "WHAT REALLY HURT ME IS I BROKE YOUR HEART\\nBABY YOU A GOOD GIRL AND I HAD NO RIGHT"),
    (101.46, 106.40, "LYRIC", "I REALLY WANNA MAKE THINGS RIGHT\\n'CAUSE WITHOUT YOU IN MY LIFE GIRL I'M SO"),
    (106.89, 111.00, "LYRIC", "LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (111.38, 116.80, "LYRIC", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN GIRL)"),
    (117.22, 121.60, "LYRIC", "I'M SO LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (122.07, 127.90, "LYRIC", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN BABY)"),
    (128.44, 133.10, "LYRIC", "BEEN ALL ABOUT THE WORLD AIN'T NEVER MET A GIRL\\nTHAT COULD TAKE THE THINGS THAT YOU BEEN THROUGH"),
    (133.51, 138.50, "LYRIC", "NEVER THOUGHT THE DAY WOULD COME WHERE YOU WOULD GET UP AND RUN\\nAND I WOULD BE OUT CHASING YOU"),
    (138.99, 143.70, "LYRIC", "'CAUSE AIN'T NOWHERE IN THE GLOBE I'D RATHER BE\\nAIN'T NO ONE IN THE GLOBE I'D RATHER SEE"),
    (144.15, 149.10, "LYRIC", "THAN THE GIRL OF MY DREAMS THAT MADE ME BE\\nSO HAPPY BUT NOW SO LONELY"),
    (149.54, 153.80, "LYRIC", "LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (154.28, 159.50, "LYRIC", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN NO)"),
    (159.99, 164.20, "LYRIC", "I'M SO LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (164.58, 169.80, "LYRIC", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN GIRL)"),
    (170.36, 175.90, "LYRIC", "LONELY\\nNEVER THOUGHT THAT I'D BE ALONE (BE ALONE)"),
    (176.42, 181.20, "LYRIC", "I DIDN'T THINK YOU'D BE GONE THIS LONG (GONE SO LONG)\\nI JUST WANT YOU TO CALL MY PHONE"),
    (181.63, 186.40, "LYRIC", "STOP PLAYING GIRL AND COME ON HOME (COME ON HOME)\\nBABY GIRL, I DIDN'T MEAN TO SHOUT"),
    (186.84, 191.40, "LYRIC", "I WANT ME AND YOU TO WORK IT OUT (WORK IT OUT BABY)\\nI'D NEVER WISH TO EVER HURT MY BABY"),
    (191.90, 196.20, "LYRIC", "AND IT'S DRIVING ME CRAZY 'CAUSE I'M SO\\nLONELY (SO LONELY)"),
    (196.72, 201.90, "LYRIC", "I'M MR. LONELY (MR. LONELY)\\nI HAVE NOBODY (I HAVE NOBODY)"),
    (202.39, 206.90, "LYRIC", "FOR MY OWN (TO CALL MY OWN NO)\\nI'M SO LONELY (SO LONELY)"),
    (207.47, 212.30, "LYRIC", "I'M MR. LONELY (MR. LONELY)\\nI HAVE NOBODY (I HAVE NOBODY)"),
    (212.80, 218.30, "LYRIC", "FOR MY OWN (TO CALL MY OWN GIRL)\\nI AM SO LONELY"),
    (218.76, 224.30, "LYRIC", "SO LONELY (LONELY)\\nSO LONELY (SO LONELY)"),
    (224.78, 229.60, "LYRIC", "MR. LONELY (LONELY)\\nSO LONELY (SO LONELY)"),
    (230.09, 234.50, "LYRIC", "SO LONELY (LONELY)\\nSO LONELY, MR. LONELY"),
]

# Adjust formatting: replace literal \n with \N
clean_couplets = []
for st, en, stype, txt in raw_couplets:
    txt = txt.replace("\\n", "\\N")
    clean_couplets.append((st, en, stype, txt))

# Enforce Sing-Along Holding and Zero Collision:
# For every couplet k, End_k = min(Original_End_k, Start_{k+1} - 0.20)
# But if Original_End_k < Start_{k+1} - 0.20, we can EXTEND it to Start_{k+1} - 0.20 (Sing-Along Hold)!
adjusted = []
for i in range(len(clean_couplets)):
    st, en, stype, txt = clean_couplets[i]
    if i < len(clean_couplets) - 1:
        next_st = clean_couplets[i+1][0]
        # Extend to hold until next line minus 0.20s
        hold_end = round(next_st - 0.20, 2)
        final_en = max(en, hold_end)
        # Ensure strict no-collision
        if final_en >= next_st:
            final_en = round(next_st - 0.15, 2)
    else:
        final_en = en
    adjusted.append((st, final_en, stype, txt))

# Verify zero collisions
collisions = 0
for i in range(len(adjusted) - 1):
    cur_end = adjusted[i][1]
    nxt_start = adjusted[i+1][0]
    if cur_end > nxt_start:
        print(f"COLLISION at {i}: {cur_end} > {nxt_start}")
        collisions += 1

print(f"Verification complete: {collisions} collisions across {len(adjusted)} events.")

# Generate ASS File
ass_header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,Patrick Hand,170,&H00FFFFFF,&H000000FF,&H00181020,&H70000000,1,0,0,0,95,115,3,0,1,2.8,2.2,5,50,50,50,1
Style: Lyric,Patrick Hand,138,&H00FFFFFF,&H000000FF,&H00181020,&H70000000,1,0,0,0,95,115,2,0,1,2.5,1.8,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events_lines = []
for st, en, stype, txt in adjusted:
    st_ass = fmt_ass(st)
    en_ass = fmt_ass(en)
    if stype == "TITLE":
        line = f"Dialogue: 0,{st_ass},{en_ass},TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(600,400)}}{txt}"
    else:
        line = f"Dialogue: 0,{st_ass},{en_ass},Lyric,,0,0,0,,{{\\pos(960,490)\\fad(220,150)}}{txt}"
    events_lines.append(line)

final_ass_content = ass_header + "\n".join(events_lines) + "\n"
out_ass_path = os.path.join(song_dir, "lyrics_couplets_final.ass")

with open(out_ass_path, "w", encoding="utf-8") as f:
    f.write(final_ass_content)

print(f"Successfully generated: {out_ass_path}")
print(f"First 5 dialogue lines:")
for l in events_lines[:5]:
    print(l)
