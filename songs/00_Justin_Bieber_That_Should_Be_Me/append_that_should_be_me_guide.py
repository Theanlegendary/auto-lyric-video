import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

guide_file = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\Fade_Replay_YouTube_Upload_Guide.txt")

entry = """
================================================================================
SONG #00: Justin Bieber - That Should Be Me (20 Minutes Loop / 5 Times Replay)
Aesthetic Style: 7clouds Twilight Heartbreak Cloudscape (Sapphire / Indigo / Rose Rim Glow)
Video Files:
- Single Track (3:36): videos/00_Justin_Bieber_That_Should_Be_Me_Lyric_Video.mp4
- 20-Min 5x Replay (21:38): videos/00_Justin_Bieber_That_Should_Be_Me_20Min_5x_Replay_Lyric_Video.mp4
================================================================================

TITLE:
Justin Bieber - That Should Be Me (20 Minutes Loop / 5 Times Replay) [Lyrics]

ALTERNATIVE TITLES:
Justin Bieber - That Should Be Me (5 Times Replay - 20+ Minutes) [Lyrics]
Justin Bieber - That Should Be Me (Lyrics) [20 Minutes Loop / Study & Sleep]

DESCRIPTION:
Justin Bieber - That Should Be Me (20 Minutes Loop / 5 Times Replay) [Lyrics]

Stream "That Should Be Me":
https://JustinBieber.lnk.to/MyWorld2

Fade Replay:
Clean, peaceful aesthetic lyric videos inspired by 7clouds. High-definition twilight skies, synchronized 2-row couplets, and seamless extended loops for studying, sleeping, and comfort listening.

TIMESTAMPS / CHAPTERS:
0:00 Loop 1 (Original)
3:36 Loop 2 (Replay [1/5])
7:13 Loop 3 (Replay [2/5])
10:49 Loop 4 (Replay [3/5])
14:26 Loop 5 (Replay [4/5])
18:02 Loop 6 (Replay [5/5])

(Lyrics):
[Verse 1]
Everybody's laughing in my mind
Rumors spreading 'bout this other guy
Do you do what you did when you did with me?
Does he love you the way I can?
Did you forget all the plans that you made with me?
'Cause, baby, I didn't

[Chorus]
That should be me holding your hand
That should be me making you laugh
That should be me, this is so sad
That should be me, that should be me
That should be me feeling your kiss
That should be me buying you gifts
This is so wrong, I can't go on
'Til you believe that that should be me

[Verse 2]
You said you needed a little time for my mistakes
It's funny how you used that time to have me replaced
Did you think that I wouldn't see you out at the movies?
What you doing to me? You're taking him where we used to go
Now if you're tryna break my heart
It's working 'cause you know that

[Chorus]
That should be me holding your hand
That should be me making you laugh
That should be me, this is so sad
That should be me, that should be me
That should be me feeling your kiss
That should be me buying you gifts
This is so wrong, I can't go on
'Til you believe that that should be me

[Bridge]
I need to know, should I fight for love or disarm?
It's getting harder to shield this pain in my heart
Oh, whoa...

[Chorus]
That should be me holding your hand
That should be me making you laugh
That should be me, this is so sad
That should be me, that should be me
That should be me feeling your kiss
That should be me buying you gifts
This is so wrong, I can't go on
'Til you believe that that should be me

[Outro]
Holding your hand, that should be me
The one making you laugh, oh baby
That should be me giving you flowers
That should be me talking for hours
That should be me, that should be me
Oh baby, that should be me

TAGS:
justin bieber that should be me, that should be me lyrics, that should be me 20 minutes, that should be me 5 times replay, that should be me 5 times, that should be me loop, that should be me on repeat, justin bieber lyrics, that should be me holding your hand, that should be me making you laugh, fade replay, 7clouds style lyric video, study loop, sleep loop, chill lyrics, pop classics 2010s
"""

with open(guide_file, "a", encoding="utf-8") as f:
    f.write(entry)

print(f"Appended That Should Be Me 20-min loop guide to {guide_file.name}")
