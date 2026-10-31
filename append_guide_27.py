import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

guide = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/Fade_Replay_YouTube_Upload_Guide.txt")

entry = """
================================================================================
SONG 27: Joji - Glimpse of Us
================================================================================

TITLE (CTR Optimized):
Joji - Glimpse of Us (Lyrics)
OR:
Joji - Glimpse of Us (Slowed + Reverb) [Lyrics]

DESCRIPTION:
🔔 Don't forget to subscribe and turn on notifications!
🎵 Follow Fade Replay on Spotify

"Glimpse of Us" is out now.

Follow Joji:
https://instagram.com/sushitrash
https://twitter.com/sushitrash
https://facebook.com/jojiofficial

Fade Replay:
Atmospheric lyric videos with unique anime aesthetics and studio-synchronized couplets.

(Lyrics):
[Verse 1]
She'd take the world off my shoulders
If it was ever hard to move
She'd turn the rain to a rainbow
When I was living in the blue

[Pre-Chorus]
Why then, if she's so perfect
Do I still wish that it was you?
Perfect don't mean that it's working
So what can I do? (Ooh)
When you're out of sight in my mind

[Chorus]
'Cause sometimes I look in her eyes
And that's where I find a glimpse of us
And I try to fall for her touch
But I'm thinking of the way it was
Said, "I'm fine" and said, "I moved on"
I'm only here passing time in her arms
Hoping I'll find a glimpse of us

[Verse 2]
Tell me he savors your glory
Does he laugh the way I did?
Is this a part of your story?
One that I had never lived

[Bridge]
Maybe one day, you'll feel lonely
And in his eyes, you'll get a glimpse
Maybe you'll start slipping slowly
And find me again
When you're out of sight in my mind

[Chorus]
'Cause sometimes I look in her eyes
And that's where I find a glimpse of us
And I try to fall for her touch
But I'm thinking of the way it was
Said, "I'm fine" and said, "I moved on"
I'm only here passing time in her arms
Hoping I'll find a glimpse of us

[Chorus / Outro]
'Cause sometimes I look in her eyes
And that's where I find a glimpse of us
And I try to fall for her touch
But I'm thinking of the way it was
Said, "I'm fine" and said, "I moved on"
I'm only here passing time in her arms
Hoping I'll find a glimpse of us

TAGS:
joji,glimpse of us,glimpse of us lyrics,joji glimpse of us,joji glimpse of us lyrics,glimpse of us slowed,glimpse of us slowed reverb,cause sometimes i look in her eyes,and thats where i find a glimpse of us,im only here passing time in her arms,joji lyrics,fade replay,fade replay lyrics

#joji #glimpseofus #lyrics #FadeReplay #SlowedAndReverb #PianoBallad
"""

content = guide.read_text(encoding="utf-8")
if "SONG 27: Joji - Glimpse of Us" not in content:
    guide.write_text(content + entry, encoding="utf-8")
    print("Appended Song 27 to Fade_Replay_YouTube_Upload_Guide.txt")
else:
    print("Song 27 already in upload guide.")
