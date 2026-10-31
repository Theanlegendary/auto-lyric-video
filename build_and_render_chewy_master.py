import os
import sys
import subprocess
import time
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "15_Akon_Lonely"
audio_path = song_dir / "audio_7clouds.mp3"
bg_blur = song_dir / "vibe_sky_blurred_master.png"
out_video = base / "videos" / "15_Akon_Lonely_Lyric_Video.mp4"

fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

def fmt_ass(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

raw_couplets = [
    # (start, end, style_type, text)
    (1.00, 9.50, "TITLE", "LONELY\\N{\\fs95\\fsp4}Akon"),
    (10.13, 20.20, "HOOK", "I'M SO LONELY, I'M MR. LONELY\\NI HAVE NOBODY FOR MY OWN"),
    (20.74, 23.80, "HOOK", "I'M SO LONELY"),
    (24.38, 32.00, "VERSE", "YO! THIS ONE HERE\\NGOES OUT TO ALL MY PLAYERS OUT THERE MAN, YA KNOW"),
    (32.49, 38.20, "VERSE", "THAT GOT THAT ONE GOOD GIRL WHO'S ALWAYS BEEN THERE MAN, LIKE\\NTOOK ALL THE BULLSHIT"),
    (38.75, 42.50, "VERSE", "BUT THEN ONE DAY SHE CAN'T TAKE IT NO MORE AND DECIDE TO LEAVE\\NYEAH"),
    (42.99, 47.80, "VERSE", "I WOKE UP IN THE MIDDLE OF THE NIGHT\\NAND I NOTICED MY GIRL WASN'T BY MY SIDE"),
    (48.21, 53.10, "VERSE", "COULDA SWORN I WAS DREAMING, FOR HER I WAS FEENIN'\\NSO I HAD TO TAKE A LITTLE RIDE"),
    (53.55, 58.50, "VERSE", "BACK TRACKING OVER THESE FEW YEARS\\NTRYNA FIGURE OUT WHAT I DO TO MAKE IT GO BAD"),
    (58.92, 63.80, "VERSE", "'CAUSE EVER SINCE MY GIRL LEFT ME\\nMY WHOLE LIFE CAME CRASHING AND I'M SO"),
    (64.18, 68.50, "HOOK", "LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (68.88, 74.10, "HOOK", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN GIRL)"),
    (74.54, 79.20, "HOOK", "I'M SO LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (79.59, 85.20, "HOOK", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN GIRL)"),
    (85.64, 90.50, "VERSE", "CAN'T BELIEVE I HAD A GIRL LIKE YOU\\nAND I JUST LET YOU WALK RIGHT OUTTA MY LIFE"),
    (90.93, 95.80, "VERSE", "AFTER ALL I PUT YOU THROUGH\\nYOU STILL STUCK AROUND AND STAYED BY MY SIDE"),
    (96.25, 101.00, "VERSE", "WHAT REALLY HURT ME IS I BROKE YOUR HEART\\nBABY YOU A GOOD GIRL AND I HAD NO RIGHT"),
    (101.46, 106.40, "VERSE", "I REALLY WANNA MAKE THINGS RIGHT\\n'CAUSE WITHOUT YOU IN MY LIFE GIRL I'M SO"),
    (106.89, 111.00, "HOOK", "LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (111.38, 116.80, "HOOK", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN GIRL)"),
    (117.22, 121.60, "HOOK", "I'M SO LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (122.07, 127.90, "HOOK", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN BABY)"),
    (128.44, 133.10, "VERSE", "BEEN ALL ABOUT THE WORLD AIN'T NEVER MET A GIRL\\nTHAT COULD TAKE THE THINGS THAT YOU BEEN THROUGH"),
    (133.51, 138.50, "VERSE", "NEVER THOUGHT THE DAY WOULD COME WHERE YOU WOULD GET UP AND RUN\\nAND I WOULD BE OUT CHASING YOU"),
    (138.99, 143.70, "VERSE", "'CAUSE AIN'T NOWHERE IN THE GLOBE I'D RATHER BE\\nAIN'T NO ONE IN THE GLOBE I'D RATHER SEE"),
    (144.15, 149.10, "VERSE", "THAN THE GIRL OF MY DREAMS THAT MADE ME BE\\nSO HAPPY BUT NOW SO LONELY"),
    (149.54, 153.80, "HOOK", "LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (154.28, 159.50, "HOOK", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN NO)"),
    (159.99, 164.20, "HOOK", "I'M SO LONELY (SO LONELY)\\nI'M MR. LONELY (MR. LONELY)"),
    (164.58, 169.80, "HOOK", "I HAVE NOBODY (I HAVE NOBODY)\\nFOR MY OWN (TO CALL MY OWN GIRL)"),
    (170.36, 175.90, "VERSE", "LONELY\\nNEVER THOUGHT THAT I'D BE ALONE (BE ALONE)"),
    (176.42, 181.20, "VERSE", "I DIDN'T THINK YOU'D BE GONE THIS LONG (GONE SO LONG)\\nI JUST WANT YOU TO CALL MY PHONE"),
    (181.63, 186.40, "VERSE", "STOP PLAYING GIRL AND COME ON HOME (COME ON HOME)\\nBABY GIRL, I DIDN'T MEAN TO SHOUT"),
    (186.84, 191.40, "VERSE", "I WANT ME AND YOU TO WORK IT OUT (WORK IT OUT BABY)\\nI'D NEVER WISH TO EVER HURT MY BABY"),
    (191.90, 196.20, "HOOK", "AND IT'S DRIVING ME CRAZY 'CAUSE I'M SO\\nLONELY (SO LONELY)"),
    (196.72, 201.90, "HOOK", "I'M MR. LONELY (MR. LONELY)\\nI HAVE NOBODY (I HAVE NOBODY)"),
    (202.39, 206.90, "HOOK", "FOR MY OWN (TO CALL MY OWN NO)\\nI'M SO LONELY (SO LONELY)"),
    (207.47, 212.30, "HOOK", "I'M MR. LONELY (MR. LONELY)\\nI HAVE NOBODY (I HAVE NOBODY)"),
    (212.80, 218.30, "HOOK", "FOR MY OWN (TO CALL MY OWN GIRL)\\nI AM SO LONELY"),
    (218.76, 224.30, "HOOK", "SO LONELY (LONELY)\\nSO LONELY (SO LONELY)"),
    (224.78, 229.60, "HOOK", "MR. LONELY (LONELY)\\nSO LONELY (SO LONELY)"),
    (230.09, 234.50, "HOOK", "SO LONELY (LONELY)\\nSO LONELY, MR. LONELY"),
]

# Sing-along holding time & collision prevention
adjusted = []
for i in range(len(raw_couplets)):
    st, en, stype, txt = raw_couplets[i]
    txt = txt.replace("\\n", "\\N")
    
    if i < len(raw_couplets) - 1:
        next_st = raw_couplets[i+1][0]
        max_allowed_en = round(next_st - 0.20, 2)
        if en < max_allowed_en:
            en = max_allowed_en
        elif en >= next_st:
            en = round(next_st - 0.05, 2)
    else:
        en = 234.80
    
    adjusted.append((st, en, stype, txt))

# Verify collisions
collisions = 0
for i in range(len(adjusted) - 1):
    curr_en = adjusted[i][1]
    next_st = adjusted[i+1][0]
    if curr_en > next_st:
        print(f"COLLISION at {i}: curr_en={curr_en} > next_st={next_st}")
        collisions += 1

print(f"Verified {len(adjusted)} events with {collisions} collisions.")

# Build ASS header with Chewy "Cloud Nine" style
# Font: Chewy (chunky handwritten, pure luminous white, soft ambient shadow, micro-halo anti-aliasing)
ass_header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,Chewy,195,&H00FFFFFF,&H000000FF,&H00100818,&H50000000,1,0,0,0,100,100,3,0,1,0.8,2.8,5,50,50,50,1
Style: HookBig,Chewy,165,&H00FFFFFF,&H000000FF,&H00100818,&H50000000,1,0,0,0,100,100,1,0,1,0.8,2.5,5,50,50,50,1
Style: VerseBig,Chewy,125,&H00FFFFFF,&H000000FF,&H00100818,&H50000000,1,0,0,0,100,100,1,0,1,0.8,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events_lines = []
for st, en, stype, txt in adjusted:
    st_ass = fmt_ass(st)
    en_ass = fmt_ass(en)
    if stype == "TITLE":
        line = f"Dialogue: 0,{st_ass},{en_ass},TitleCard,,0,0,0,,{{\\pos(960,470)\\fad(600,400)}}{txt}"
    elif stype == "HOOK":
        line = f"Dialogue: 0,{st_ass},{en_ass},HookBig,,0,0,0,,{{\\pos(960,490)\\fad(220,150)}}{txt}"
    else:
        line = f"Dialogue: 0,{st_ass},{en_ass},VerseBig,,0,0,0,,{{\\pos(960,490)\\fad(220,150)}}{txt}"
    events_lines.append(line)

final_ass_content = ass_header + "\n".join(events_lines) + "\n"
out_ass_path = song_dir / "lyrics_chewy_cloudnine.ass"

with open(out_ass_path, "w", encoding="utf-8") as f:
    f.write(final_ass_content)

print(f"Generated ASS: {out_ass_path}")

# Now build the full FFmpeg render command
duration = 235.13
t_out = round(duration - 3.0, 2)
ass_escaped = out_ass_path.as_posix().replace(":", "\\\\:")

fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=6:allf=t+u,"
    f"fade=t=out:st={t_out}:d=3.0[v]"
)

af = f"afade=t=in:ss=0:d=1.8,afade=t=out:st={t_out}:d=3.0"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", str(duration), "-i", str(bg_blur),
    "-i", str(audio_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-map", "1:a",
    "-af", af,
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "18",
    "-c:a", "aac",
    "-b:a", "320k",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    str(out_video)
]

print("Rendering full master video with Chewy Cloud Nine style...")
start_time = time.time()
res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')
elapsed = time.time() - start_time

if res.returncode == 0:
    size_mb = out_video.stat().st_size / (1024 * 1024)
    print(f"SUCCESS! Rendered master video {out_video.name} in {elapsed:.1f}s ({size_mb:.2f} MB)")
else:
    print(f"FAILED with code {res.returncode}")
    print("Stderr tail:")
    print("\n".join(res.stderr.splitlines()[-30:]))
