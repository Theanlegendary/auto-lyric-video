import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
p = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"

with open(p, "r", encoding="utf-8") as f:
    text = f.read()

# Replace button 15 label and description
text = text.replace("15. Lonely (Cloud Nine Edition)", "15. Lonely (Clear Blue Anime Sky Edition)")
text = text.replace("15. Lonely (Official Lyric Video)", "15. Lonely (Clear Blue Anime Sky Edition)")
text = text.replace("Vibe Sky (Deep Blur)", "Clear Blue Sky (Ultra/Poppins)")
text = text.replace("Aesthetic Vibe Sunset Sky & Pine Ridge (Deep Blur)", "Makoto Shinkai Clear Blue Anime Sky & Towering Clouds")

with open(p, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated player.html successfully!")
