import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
p = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6\final_verification_report.md"

with open(p, "r", encoding="utf-8") as f:
    text = f.read()

# Update table row for Song 15
old_row = '| **15** | **Lonely (Cloud Nine Edition)**<br>Akon | **Aesthetic Vibe Sunset Sky & Pine Ridge (Deep Blur)** | Requested Vibe Sky, deep blur (radius 24), warm scrim, & chunky handwritten Chewy font (Cloud Nine style, pure clean white) | 42 | 7clouds (18.1M) | 273.0 MB | [15_Akon_Lonely_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/15_Akon_Lonely_Lyric_Video.mp4) |'
new_row = '| **15** | **Lonely (Clear Blue Anime Sky Edition)**<br>Akon | **Makoto Shinkai Clear Blue Anime Sky & Towering Clouds** | Vibrant azure anime sky & cumulus clouds, Ultra Italic title, Poppins Black Italic lyrics, cute scale-bounce animation | 42 | 7clouds (18.1M) | 179.3 MB | [15_Akon_Lonely_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/15_Akon_Lonely_Lyric_Video.mp4) |'

if old_row in text:
    text = text.replace(old_row, new_row)
else:
    # Look for any row 15
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| **15** |"):
            lines[i] = new_row
            break
    text = "\n".join(lines)

# Update carousel slide
text = text.replace("audit_15_Akon_Lonely_chewy_chorus.png", "audit_15_Akon_Lonely_bluesky_chorus.png")
text = text.replace("audit_15_Akon_Lonely_chorus1.png", "audit_15_Akon_Lonely_bluesky_chorus.png")

with open(p, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated final_verification_report.md successfully!")
