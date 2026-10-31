import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
rep = brain / "final_verification_report.md"

content = rep.read_text(encoding='utf-8')

# Target table row 19
target_row = "| **19** | **A Sky Full of Stars**<br>Coldplay | **Makoto Shinkai Cosmic Sapphire Starlit Sky & Solitary Overlook** | Vast clean dark sapphire/indigo cosmic sky (85%) with shimmering celestial starlight & shooting star, distant dark ridge overlook (15%), directly visualizing 'Cause you're a sky full of stars / I wanna die in your arms', Spotify-style Poppins Bold sentence case typography, 50/50 balanced couplets | 12 | Dan Music (267s) | 118.0 MB | [19_Coldplay_A_Sky_Full_of_Stars_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/19_Coldplay_A_Sky_Full_of_Stars_Lyric_Video.mp4) |"

new_row = target_row + "\n" + "| **20** | **Paradise**<br>Coldplay | **Makoto Shinkai Twilight Celestial Dreamscape & Solitary Overlook** | Vast deep dark midnight indigo & twilight celestial sky (85%) with luminous crescent moon & stardust ribbon, soft ethereal pastel rose-violet clouds & solitary overlook (15%), directly visualizing 'Every time she closed her eyes / Dreaming of paradise', Spotify-style Poppins Bold sentence case typography, 50/50 balanced couplets | 25 | 7clouds (275s) | 158.0 MB | [20_Coldplay_Paradise_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/20_Coldplay_Paradise_Lyric_Video.mp4) |"

# Carousel slide 19
target_slide = "![Song 19: A Sky Full of Stars (Coldplay) — Cosmic Sapphire Starlit Sky & Overlook](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_19_stars_hook.png)"

new_slide = target_slide + "\n" + "<!-- slide -->\n" + "![Song 20: Paradise (Coldplay) — Twilight Celestial Dreamscape & Solitary Overlook](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_20_paradise_chorus1.png)"

if target_row in content:
    content = content.replace(target_row, new_row)
else:
    print("Warning: target_row not found!")

if target_slide in content:
    content = content.replace(target_slide, new_slide)
else:
    print("Warning: target_slide not found!")

rep.write_text(content, encoding='utf-8')
print("Updated final_verification_report.md with Song 20!")
