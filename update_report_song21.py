import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
rep = brain / "final_verification_report.md"

content = rep.read_text(encoding='utf-8')

# Target table row 20
target_row = "| **20** | **Paradise**<br>Coldplay | **Makoto Shinkai Twilight Celestial Dreamscape & Solitary Overlook** | Vast deep dark midnight indigo & twilight celestial sky (85%) with luminous crescent moon & stardust ribbon, soft ethereal pastel rose-violet clouds & solitary overlook (15%), directly visualizing 'Every time she closed her eyes / Dreaming of paradise', Spotify-style Poppins Bold sentence case typography, 50/50 balanced couplets | 25 | 7clouds (275s) | 158.0 MB | [20_Coldplay_Paradise_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/20_Coldplay_Paradise_Lyric_Video.mp4) |"

new_row = target_row + "\n" + "| **21** | **Clocks**<br>Coldplay | **Makoto Shinkai Cosmic Starlight & Midnight Ocean Bluffs** | Vast clean dark midnight sapphire celestial sky (85%) with ethereal cosmic clockwork orbits & sparkling diamond stars, quiet dark ocean bluffs & reflective tides (15%), directly visualizing 'Lights go out and I can't be saved / Tides that I tried to swim against', Studio zero-lag vocal sync with Whisper word timestamps, Spotify Poppins Bold, 50/50 balanced couplets | 18 | Dan Music (305s) | 185.0 MB | [21_Coldplay_Clocks_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/21_Coldplay_Clocks_Lyric_Video.mp4) |"

# Carousel slide 20
target_slide = "![Song 20: Paradise (Coldplay) — Twilight Celestial Dreamscape & Solitary Overlook](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_20_paradise_chorus1.png)"

# If unicode character was altered, handle both
if target_slide not in content:
    for line in content.splitlines():
        if "audit_20_paradise_chorus1.png" in line:
            target_slide = line
            break

new_slide = target_slide + "\n" + "<!-- slide -->\n" + "![Song 21: Clocks (Coldplay) — Cosmic Starlight & Midnight Ocean Bluffs](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_21_clocks_verse1.png)"

if target_row in content:
    content = content.replace(target_row, new_row)
else:
    print("Warning: target_row not found!")

if target_slide in content:
    content = content.replace(target_slide, new_slide)
else:
    print("Warning: target_slide not found!")

rep.write_text(content, encoding='utf-8')
print("Updated final_verification_report.md with Song 21!")
