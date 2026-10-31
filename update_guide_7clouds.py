import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

guide_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\Fade_Replay_YouTube_Upload_Guide.txt")
text = guide_path.read_text(encoding='utf-8', errors='ignore')

# Check if Song 28 is present and update its section
entry_28_new = """================================================================================
SONG 28: yung kai - blue (7clouds Clean Aesthetic Remaster)
================================================================================

TITLE (CTR Optimized):
yung kai - blue (Lyrics)

DESCRIPTION:
🔔 Don't forget to subscribe and turn on notifications!
🎧 Follow Fade Replay on Spotify: https://spoti.fi/fadereplay

"blue" is out now.

Follow yung kai:
https://instagram.com/yungkai
https://tiktok.com/@yungkai

Fade Replay:
Clean, peaceful aesthetic lyric videos inspired by 7clouds. High-definition pastel skies and synchronized couplets.

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
Cause you're so blue

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
Cause you're so blue

TIMESTAMPS:
0:00 blue - yung kai
0:18 Your morning eyes / I could stare like watching stars
0:33 Would you mind if I took your hand tonight?
0:47 I think I'll picture us, you with the waves
1:01 Will you be forever with me? / Cause you're so blue
1:46 My love will always stay by you
2:08 I'll imagine we fell in love
2:16 I think I'll picture us, you with the waves
2:30 Will you be forever with me? / Cause you're so blue

TAGS:
yung kai blue, blue yung kai, blue lyrics, yung kai blue lyrics, blue lyric video, i think ill picture us you with the waves, your morning eyes i could stare like watching stars, cause youre so blue, fade replay, 7clouds style lyric video, aesthetic lyrics, chill lyrics, indie pop 2024
"""

import re
# Replace SONG 28 section
pattern = r'={50,}\s*SONG 28: yung kai - blue.*?(?=={50,}\s*SONG 29|\Z)'
if re.search(pattern, text, flags=re.DOTALL):
    text = re.sub(pattern, entry_28_new + "\n", text, flags=re.DOTALL)
    print("Replaced SONG 28 section in guide.")
else:
    text += "\n\n" + entry_28_new
    print("Appended SONG 28 section to guide.")

guide_path.write_text(text, encoding='utf-8')
print("Guide updated successfully.")
