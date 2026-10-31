import os
import sys
import subprocess
import time
from pathlib import Path
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "15_Akon_Lonely"
raw_orange = base / "stock_anime_bgs" / "18_rdr_vegas_clear_orange_sky.png"
master_bg = song_dir / "vegas_rdr_orange_blurred_master.png"
audio_path = song_dir / "audio_7clouds.mp3"
out_video = base / "videos" / "15_Akon_Lonely_Lyric_Video.mp4"
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

# 1. Prepare master background
im = Image.open(raw_orange).convert("RGB").resize((1920, 1080), Image.Resampling.LANCZOS)
im_blur = im.filter(ImageFilter.GaussianBlur(radius=18))
scrim = Image.new("RGB", (1920, 1080), (28, 12, 8))
bg_spotify_orange = Image.blend(im_blur, scrim, 0.08)
bg_spotify_orange.save(master_orange, "PNG") if "master_orange" in locals() else bg_spotify_orange.save(master_bg, "PNG")

def fmt_ass(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

# 50/50 balanced couplets in Spotify Sentence Case
couplets = [
    (1.00, 9.50, "TITLE", "Lonely\\N{\\fs66\\fsp4\\b0}Akon"),
    (10.13, 20.20, "HOOK", "Lonely, I'm Mr. Lonely\\nI have nobody for my own"),
    (20.74, 23.80, "HOOK", "I am so lonely\\nI'm Mr. Lonely"),
    (24.38, 32.00, "SPOKEN", "Yo, this one here goes out\\nTo all my players out there, you know"),
    (32.49, 38.20, "SPOKEN", "That got that one good girl\\nWho's always been there, took all the bullshit"),
    (38.75, 42.50, "SPOKEN", "Then one day she can't take it no more\\nAnd decide to leave, yeah"),
    (42.99, 47.80, "VERSE", "I woke up in the middle of the night\\nAnd I noticed my girl wasn't by my side"),
    (48.21, 53.10, "VERSE", "Coulda sworn I was dreaming, for her I was feenin'\\nSo I had to get up and take a little ride"),
    (53.55, 58.50, "VERSE", "Backtracking over these few years\\nTryna figure out what I did to make it go bad"),
    (58.92, 63.80, "VERSE", "'Cause ever since my girl left me\\nMy whole life came crashing and I'm so"),
    (64.18, 68.50, "HOOK", "Lonely (So lonely)\\nI'm Mr. Lonely (Mr. Lonely)"),
    (68.88, 74.10, "HOOK", "I have nobody (I have nobody)\\nFor my own (To call my own, girl)"),
    (74.54, 79.20, "HOOK", "I'm so lonely (So lonely)\\nI'm Mr. Lonely (Mr. Lonely)"),
    (79.59, 85.20, "HOOK", "I have nobody (I have nobody)\\nFor my own (To call my own, girl)"),
    (85.64, 90.50, "VERSE", "Can't believe I had a girl like you\\nAnd I just let you walk right outta my life"),
    (90.93, 95.80, "VERSE", "After all I put you through\\nYou still stuck around and stayed by my side"),
    (96.25, 101.00, "VERSE", "What really hurt me is I broke your heart\\nBaby, you a good girl and I had no right"),
    (101.46, 106.40, "VERSE", "I really wanna make things right\\n'Cause without you in my life, girl, I'm so"),
    (106.89, 111.00, "HOOK", "Lonely (So lonely)\\nI'm Mr. Lonely (Mr. Lonely)"),
    (111.38, 116.80, "HOOK", "I have nobody (I have nobody)\\nFor my own (To call my own, girl)"),
    (117.22, 121.60, "HOOK", "I'm so lonely (So lonely)\\nI'm Mr. Lonely (Mr. Lonely)"),
    (122.07, 127.90, "HOOK", "I have nobody (I have nobody)\\nFor my own (To call my own, baby)"),
    (128.44, 133.10, "VERSE", "Been all about the world, ain't never met a girl\\nThat could take the things that you been through"),
    (133.51, 138.50, "VERSE", "Never thought the day would come where you would run\\nAnd I would be out chasing you"),
    (138.99, 143.70, "VERSE", "'Cause ain't nowhere in the globe I'd rather be\\nAin't no one in the globe I'd rather see"),
    (144.15, 149.10, "VERSE", "Than the girl of my dreams that made me be\\nSo happy, but now so lonely"),
    (149.54, 153.80, "HOOK", "Lonely (So lonely)\\nI'm Mr. Lonely (Mr. Lonely)"),
    (154.28, 159.50, "HOOK", "I have nobody (I have nobody)\\nFor my own (To call my own, no)"),
    (159.99, 164.20, "HOOK", "I'm so lonely (So lonely)\\nI'm Mr. Lonely (Mr. Lonely)"),
    (164.58, 169.80, "HOOK", "I have nobody (I have nobody)\\nFor my own (To call my own, girl)"),
    (170.36, 175.90, "VERSE", "Never thought that I'd be alone\\nNever thought that I'd be all on my own"),
    (176.42, 181.20, "VERSE", "I didn't think you'd be gone this long\\nI just want you to call my phone"),
    (181.63, 186.40, "VERSE", "Stop playing, girl, and come on home\\nBaby girl, I didn't mean to shout"),
    (186.84, 191.40, "VERSE", "I want me and you to work it out\\nI'd never wish to ever hurt my baby"),
    (191.90, 196.20, "HOOK", "And it's driving me crazy 'cause I'm so\\nLonely (So lonely)"),
    (196.72, 201.90, "HOOK", "I'm Mr. Lonely (Mr. Lonely)\\nI have nobody (I have nobody)"),
    (202.39, 206.90, "HOOK", "For my own (To call my own, no)\\nI'm so lonely (So lonely)"),
    (207.47, 212.30, "HOOK", "I'm Mr. Lonely (Mr. Lonely)\\nI have nobody (I have nobody)"),
    (212.80, 218.30, "HOOK", "For my own (To call my own, girl)\\nI am so lonely"),
    (218.76, 224.30, "OUTRO", "So lonely (Lonely)\\nSo lonely (So lonely)"),
    (224.78, 229.60, "OUTRO", "Mr. Lonely (Lonely)\\nSo lonely (So lonely)"),
    (230.09, 234.50, "OUTRO", "So lonely (Lonely)\\nSo lonely, Mr. Lonely"),
]

adjusted = []
for i in range(len(couplets)):
    st, en, ctype, txt = couplets[i]
    txt = txt.replace("\\n", "\\N")
    
    if i < len(couplets) - 1:
        next_st = couplets[i+1][0]
        max_allowed_en = round(next_st - 0.20, 2)
        if en < max_allowed_en:
            en = max_allowed_en
        elif en >= next_st:
            en = round(next_st - 0.05, 2)
    else:
        en = 234.80
    
    adjusted.append((st, en, ctype, txt))

# Verify 0 collisions
collisions = 0
for i in range(len(adjusted) - 1):
    curr_en = adjusted[i][1]
    next_st = adjusted[i+1][0]
    if curr_en > next_st:
        print(f"COLLISION at {i}: curr_en={curr_en} > next_st={next_st}")
        collisions += 1

print(f"Verified {len(adjusted)} events with {collisions} collisions.")

ass_header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SpotifyTitle,Poppins,135,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,2,0,1,1.5,3.0,5,50,50,50,1
Style: SpotifyHook,Poppins,82,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.2,2.5,5,50,50,50,1
Style: SpotifyVerse,Poppins,72,&H00FFFFFF,&H000000FF,&H00180B05,&H60100502,1,0,0,0,100,100,1,0,1,1.2,2.5,5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events_lines = []
for st, en, ctype, txt in adjusted:
    st_ass = fmt_ass(st)
    en_ass = fmt_ass(en)
    if ctype == "TITLE":
        line = f"Dialogue: 0,{st_ass},{en_ass},SpotifyTitle,,0,0,0,,{{\\pos(960,470)\\fad(500,300)}}{txt}"
    elif ctype in ["HOOK", "CHORUS", "OUTRO"]:
        line = f"Dialogue: 0,{st_ass},{en_ass},SpotifyHook,,0,0,0,,{{\\pos(960,490)\\fad(200,150)}}{txt}"
    else:
        line = f"Dialogue: 0,{st_ass},{en_ass},SpotifyVerse,,0,0,0,,{{\\pos(960,490)\\fad(200,150)}}{txt}"
    events_lines.append(line)

final_ass_content = ass_header + "\n".join(events_lines) + "\n"
out_ass_path = song_dir / "lyrics_spotify_rdr_orange.ass"

with open(out_ass_path, "w", encoding="utf-8") as f:
    f.write(final_ass_content)

print(f"Generated Spotify RDR ASS file: {out_ass_path}")

# FFmpeg Filtergraph
duration = 235.13
t_out = round(duration - 3.0, 2)
ass_escaped = out_ass_path.as_posix().replace(":", "\\\\:")

fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=5:allf=t+u,"
    f"fade=t=out:st={t_out}:d=3.0[v]"
)

af = f"afade=t=in:ss=0:d=1.8,afade=t=out:st={t_out}:d=3.0"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", str(duration), "-i", str(master_bg),
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

print("Starting full render for Akon - Lonely (Spotify Style + 50/50 Couplets + RDR/Vegas Clear Orange Sky)...")
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
