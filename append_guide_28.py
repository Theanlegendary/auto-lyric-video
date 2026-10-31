import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

guide = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/Fade_Replay_YouTube_Upload_Guide.txt")

entry = """
================================================================================
SONG 28: yung kai - blue
================================================================================

TITLE (CTR Optimized):
yung kai - blue (Lyrics)
OR:
yung kai - blue (Slowed + Reverb) [Lyrics]

DESCRIPTION:
🔔 Don't forget to subscribe and turn on notifications!
🎵 Follow Fade Replay on Spotify

"blue" is out now.

Follow yung kai:
https://instagram.com/yungkai
https://tiktok.com/@yungkai

Fade Replay:
Dreamy aesthetic lyric videos with unique anime visuals and synchronized couplets.

(Lyrics):
[Verse 1]
Your morning eyes
I could stare like watching stars
I could walk you by
And I'll tell without a thought you'd be mine

[Pre-Chorus]
Would you mind if I took your hand tonight?
Know you're all that I want this life
I'll imagine we fell in love
I'll nap under moonlight skies with you

[Chorus]
I think I'll picture us, you with the waves
The ocean's colors on your face
I'll leave my heart with your air
So let me fly with you
Will you be forever with me?

[Verse 2]
My love will always stay by you
I'll keep it safe, so don't you worry a thing
I'll tell you I love you more
It's stuck with you forever
So promise you won't let it go
I'll trust the universe will always bring me to you

[Chorus]
I'll imagine we fell in love
I'll nap under moonlight skies with you
I think I'll picture us, you with the waves
The ocean's colors on your face
I'll leave my heart with your air
So let me fly with you
Will you be forever with me?

TAGS:
yung kai,blue,yung kai blue,blue lyrics,yung kai blue lyrics,your morning eyes i could stare like watching stars,ill nap under moonlight skies with you,the oceans colors on your face,blue slowed reverb,yung kai lyrics,fade replay,fade replay lyrics

#yungkai #blue #lyrics #FadeReplay #SlowedAndReverb #DreamyAesthetic
"""

content = guide.read_text(encoding="utf-8")
if "SONG 28: yung kai - blue" not in content:
    guide.write_text(content + entry, encoding="utf-8")
    print("Appended Song 28 to Fade_Replay_YouTube_Upload_Guide.txt")
else:
    print("Song 28 already in upload guide.")
