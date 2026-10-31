import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
p = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html"

with open(p, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("15. Lonely (Clear Blue Anime Sky Edition)", "15. Lonely (Spotify Red Dead Sunset Edition)")
text = text.replace("Clear Blue Sky (Ultra/Poppins)", "Spotify Clear Orange (50/50)")
text = text.replace("Makoto Shinkai Clear Blue Anime Sky & Towering Clouds", "Red Dead & Vegas Desert Clear Glowing Orange Sky")

with open(p, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated player.html successfully!")
