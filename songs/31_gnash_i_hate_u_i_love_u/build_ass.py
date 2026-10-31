import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

lines = [
    # (start, end, text, is_intro)
    ("0:00:00.60", "0:00:04.20", "gnash - i hate u, i love u (Lyrics)\\Nft. olivia o'brien", True),
    
    # Verse 1 (Olivia O'Brien)
    ("0:00:04.80", "0:00:08.50", "Feeling used, but I'm\\nStill missing you", False),
    ("0:00:08.80", "0:00:13.20", "And I can't see the end of this\\nJust wanna feel your kiss against my lips", False),
    ("0:00:13.50", "0:00:18.50", "And now all this time is passing by\\nBut I still can't seem to tell you why", False),
    ("0:00:18.80", "0:00:23.50", "It hurts me every time I see you\\nRealize how much I need you", False),
    
    # Chorus 1
    ("0:00:24.00", "0:00:28.80", "I hate you, I love you\\nI hate that I love you", False),
    ("0:00:29.00", "0:00:34.00", "Don't want to, but I can't put\\nNobody else above you", False),
    ("0:00:34.30", "0:00:39.00", "I hate you, I love you\\nI hate that I want you", False),
    ("0:00:39.30", "0:00:44.20", "You want her, you need her\\nAnd I'll never be her", False),
    
    # Verse 2 (gnash) - Rest cut between 0:44.20 and 0:47.80
    ("0:00:47.80", "0:00:52.80", "I miss you when I can't sleep\\nOr right after coffee, or right when I can't eat", False),
    ("0:00:53.00", "0:00:58.20", "I miss you in my front seat\\nStill got sand in my sweaters from nights we don't remember", False),
    ("0:00:58.50", "0:01:03.50", "Do you miss me like I miss you?\\nFucked around and got attached to you", False),
    ("0:01:03.80", "0:01:08.50", "Friends can break your heart too, and\\nI'm always tired but never of you", False),
    
    ("0:01:08.70", "0:01:13.60", "If I pulled a you on you, you wouldn't like that shit\\nI put this reel out, but you wouldn't bite that shit", False),
    ("0:01:13.70", "0:01:18.80", "I type a text but then I never mind that shit\\nI got these feelings but you never mind that shit", False),
    ("0:01:19.00", "0:01:24.00", "Oh oh, keep it on the low\\nYou're still in love with me but your friends don't know", False),
    ("0:01:24.20", "0:01:29.20", "If you wanted me you would just say so\\nAnd if I were you, I would never let me go", False),
    
    ("0:01:29.40", "0:01:34.20", "I don't mean no harm\\nI just miss you on my arm", False),
    ("0:01:34.40", "0:01:39.80", "Wedding bells were just alarms\\nCaution tape around my heart", False),
    
    ("0:01:40.10", "0:01:45.00", "You ever wonder what we could've been?\\nYou said you wouldn't and you fucking did", False),
    ("0:01:45.20", "0:01:50.20", "Lie to me, lie with me, get your fucking fix\\nNow all my drinks and all my feelings are all fucking mixed", False),
    
    ("0:01:50.40", "0:01:55.00", "Always missing people that I shouldn't be missing\\nSometimes you gotta burn some bridges just to create some distance", False),
    ("0:01:55.10", "0:02:00.60", "I know that I control my thoughts, and I should stop reminiscing\\nBut I learned from my dad that it's good to have feelings", False),
    
    ("0:02:00.90", "0:02:05.50", "When love and trust are gone\\nI guess this is moving on", False),
    ("0:02:05.70", "0:02:10.50", "Everyone I do right does me wrong\\nSo every lonely night, I sing this song", False),
    
    # Chorus 2
    ("0:02:10.80", "0:02:16.00", "I hate you, I love you\\nI hate that I love you", False),
    ("0:02:16.10", "0:02:21.00", "Don't want to, but I can't put\\nNobody else above you", False),
    ("0:02:21.20", "0:02:26.20", "I hate you, I love you\\nI hate that I want you", False),
    ("0:02:26.40", "0:02:31.50", "You want her, you need her\\nAnd I'll never be her", False),
    
    # Bridge (Olivia O'Brien) - Rest cut 02:31.50 to 02:34.50
    ("0:02:34.50", "0:02:44.80", "All alone I watch you watch her\\nLike she's the only girl you've ever seen", False),
    ("0:02:45.00", "0:02:54.80", "You don't care, you never did\\nYou don't give a damn about me", False),
    ("0:02:55.20", "0:03:05.50", "Yeah, all alone I watch you watch her\\nShe's the only thing you've ever seen", False),
    ("0:03:05.80", "0:03:16.50", "How is it you never notice\\nThat you are slowly killing me", False),
    
    # Outro Chorus - Rest cut 03:16.50 to 03:18.50
    ("0:03:18.60", "0:03:23.80", "I hate you, I love you\\nI hate that I love you", False),
    ("0:03:24.00", "0:03:28.80", "Don't want to, but I can't put\\nNobody else above you", False),
    ("0:03:29.00", "0:03:34.00", "I hate you, I love you\\nI hate that I want you", False),
    ("0:03:34.20", "0:03:42.50", "You want her, you need her\\nAnd I'll never be her", False),
]

header = """[Script Info]
Title: gnash - i hate u, i love u (Official 7clouds Edo SZ Edition)
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
; 1. Core Font: Edo SZ, Sentence case, lower third (78% down = MarginV 200), soft black outer glow & shadow
Style: SevenCloudsLyric,Edo SZ,62,&H00FFFFFF,&H000000FF,&H35000000,&H60000000,0,0,0,0,100,100,1.5,0,1,3.2,2.2,2,160,160,200,1
; 4. Secondary Font: Poppins SemiBold for Intro Metadata (30pt, lower third MarginV 220)
Style: SevenCloudsIntro,Poppins SemiBold,30,&H00FFFFFF,&H000000FF,&H40000000,&H60000000,0,0,0,0,100,100,3.0,0,1,2.0,1.5,2,160,160,220,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

event_lines = []
for start, end, text, is_intro in lines:
    style = 'SevenCloudsIntro' if is_intro else 'SevenCloudsLyric'
    blur = '{\\blur1.5}' if is_intro else '{\\blur1.8}'
    event_lines.append(f'Dialogue: 0,{start},{end},{style},,0,0,0,,{blur}{text}')

ass_text = header + '\n'.join(event_lines) + '\n'

out_ass = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\31_gnash_i_hate_u_i_love_u\lyrics_7clouds_clean.ass")
with open(out_ass, "w", encoding="utf-8") as f:
    f.write(ass_text)

print(f"Wrote {len(lines)} dialogue events to {out_ass.name}")
