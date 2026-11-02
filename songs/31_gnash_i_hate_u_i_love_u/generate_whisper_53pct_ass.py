import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# Position at 53% from top: 1080 * 0.53 = 572px
# Style: Alignment 2 (bottom center) with MarginV = 475px places the text base at Y = 1080 - 475 = 605px,
# and text center at ~572px (exactly 53% of the screen height!).
# Or explicit \pos(960, 572) with Alignment 5 (middle center).
# Using Alignment 5 with \pos(960, 572) guarantees exact 53% vertical centering!

header = """[Script Info]
Title: gnash - i hate u, i love u (Official 7clouds Edo SZ - Whisper Synced 53% Edition)
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
; 1. Core Font: Edo SZ, Sentence case, 53% screen position (Alignment=5, pos 960,572), soft black outer glow & shadow
Style: SevenCloudsLyric,Edo SZ,60,&H00FFFFFF,&H000000FF,&H35000000,&H60000000,0,0,0,0,100,100,1.5,0,1,3.2,2.2,5,160,160,100,1
; 4. Secondary Font: Poppins SemiBold for Intro Metadata (30pt, centered at 53%)
Style: SevenCloudsIntro,Poppins SemiBold,30,&H00FFFFFF,&H000000FF,&H40000000,&H60000000,0,0,0,0,100,100,3.0,0,1,2.0,1.5,5,160,160,100,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

# Synced exactly with Whisper studio word timestamps
events = [
    # Intro Card (0.60 to 4.20)
    ("0:00:00.60", "0:00:04.20", "SevenCloudsIntro", "{\\pos(960,572)\\blur1.5}gnash - i hate u, i love u (Lyrics)\\Nft. olivia o'brien"),

    # Verse 1 (Olivia O'Brien)
    ("0:00:04.40", "0:00:08.50", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Feeling used, but I'm\\nStill missing you"),
    ("0:00:08.60", "0:00:12.50", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}And I can't see the end of this\\nJust wanna feel your kiss against my lips"),
    ("0:00:12.54", "0:00:18.10", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}And now all this time is passing by\\nBut I still can't seem to tell you why"),
    ("0:00:18.18", "0:00:21.80", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}It hurts me every time I see you\\nRealize how much I need you"),

    # Chorus 1 (rest cut from 21.80 to 22.58)
    ("0:00:22.58", "0:00:25.50", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate you, I love you"),
    ("0:00:25.50", "0:00:29.30", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate that I love you\\nDon't want to"),
    ("0:00:29.34", "0:00:33.30", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}But I can't put\\nNobody else above you"),
    ("0:00:33.34", "0:00:35.90", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate you, I love you"),
    ("0:00:35.92", "0:00:41.10", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate that I want you\\nYou want her, you need her"),
    ("0:00:41.10", "0:00:44.20", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}And I'll never be her"),

    # Verse 2 (gnash) - Rest cut 44.20 to 46.16
    ("0:00:46.16", "0:00:51.90", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I miss you when I can't sleep\\nOr right after coffee, or right when I can't eat"),
    ("0:00:51.96", "0:00:57.00", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I miss you in my front seat\\nStill got sand in my sweaters from nights we don't remember"),
    ("0:00:57.44", "0:01:02.50", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Do you miss me like I miss you?\\nFucked around and got attached to you"),
    ("0:01:03.00", "0:01:07.40", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Friends can break your heart too, and\\nI'm always tired but never of you"),

    ("0:01:07.46", "0:01:13.00", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}If I pulled a you on you, you wouldn't like that shit\\nI put this reel out, but you wouldn't bite that shit"),
    ("0:01:13.02", "0:01:18.20", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I type a text but then I never mind that shit\\nI got these feelings but you never mind that shit"),

    ("0:01:18.24", "0:01:23.08", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Oh oh, keep it on the low\\nYou're still in love with me but your friends don't know"),
    ("0:01:23.08", "0:01:28.28", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}If you wanted me you would just say so\\nAnd if I were you, I would never let me go"),

    ("0:01:28.28", "0:01:33.30", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I don't mean no harm\\nI just miss you on my arm"),
    ("0:01:33.40", "0:01:38.40", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Wedding bells were just alarms\\nCaution tape around my heart"),

    ("0:01:39.00", "0:01:43.66", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}You ever wonder what we could've been?\\nYou said you wouldn't and you fucking did"),
    ("0:01:44.30", "0:01:49.48", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Lie to me, lie with me, get your fucking fix\\nNow all my drinks and all my feelings are all fucking mixed"),

    ("0:01:49.48", "0:01:54.16", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Always missing people that I shouldn't be missing\\nSometimes you gotta burn some bridges just to create some distance"),
    ("0:01:54.16", "0:01:59.60", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I know that I control my thoughts, and I should stop reminiscing\\nBut I learned from my dad that it's good to have feelings"),

    ("0:01:59.60", "0:02:04.20", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}When love and trust are gone\\nI guess this is moving on"),
    ("0:02:04.88", "0:02:09.90", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Everyone I do right does me wrong\\nSo every lonely night, I sing this song"),

    # Chorus 2
    ("0:02:09.90", "0:02:12.44", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate you, I love you"),
    ("0:02:12.44", "0:02:15.10", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate that I love you"),
    ("0:02:15.14", "0:02:20.30", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Don't want to, but I can't put\\nNobody else above you"),
    ("0:02:20.30", "0:02:22.86", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate you, I love you"),
    ("0:02:22.86", "0:02:25.50", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate that I want you"),
    ("0:02:25.50", "0:02:28.04", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}You want her, you need her"),
    ("0:02:28.04", "0:02:31.50", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}And I'll never be her"),

    # Bridge (Olivia O'Brien) - Rest cut 2:31.50 to 2:33.24
    ("0:02:33.24", "0:02:42.50", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}All alone I watch you watch her\\nLike she's the only girl you've ever seen"),
    ("0:02:43.36", "0:02:53.00", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}You don't care, you never did\\nYou don't give a damn about me"),
    ("0:02:53.64", "0:03:03.00", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Yeah, all alone I watch you watch her\\nShe's the only thing you've ever seen"),
    ("0:03:04.42", "0:03:14.50", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}How is it you never notice\\nThat you are slowly killing me"),

    # Outro Chorus - Rest cut 3:14.50 to 3:17.30
    ("0:03:17.30", "0:03:20.26", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate you, I love you"),
    ("0:03:20.26", "0:03:22.88", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate that I love you"),
    ("0:03:22.88", "0:03:28.12", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}Don't want to, but I can't put\\nNobody else above you"),
    ("0:03:28.12", "0:03:30.72", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate you, I love you"),
    ("0:03:30.72", "0:03:33.34", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}I hate that I want you"),
    ("0:03:33.34", "0:03:35.86", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}You want her, you need her"),
    ("0:03:35.86", "0:03:42.50", "SevenCloudsLyric", "{\\pos(960,572)\\blur1.8}And I'll never be her"),
]

event_lines = []
for start, end, style, text in events:
    event_lines.append(f"Dialogue: 0,{start},{end},{style},,0,0,0,,{text}")

ass_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\31_gnash_i_hate_u_i_love_u\lyrics_7clouds_whisper_53pct.ass")
ass_path.write_text(header + "\n".join(event_lines) + "\n", encoding="utf-8")
print(f"Generated {len(events)} whisper-accurate events positioned at 53% in {ass_path.name}")
