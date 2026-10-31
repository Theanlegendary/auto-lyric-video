import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
rep = brain / "final_verification_report.md"

content = rep.read_text(encoding='utf-8')

# Target table row 21
target_row = "| **21** | **Clocks**<br>Coldplay | **Makoto Shinkai Cosmic Starlight & Midnight Ocean Bluffs** | Vast clean dark midnight sapphire celestial sky (85%) with ethereal cosmic clockwork orbits & sparkling diamond stars, quiet dark ocean bluffs & reflective tides (15%), directly visualizing 'Lights go out and I can't be saved / Tides that I tried to swim against', Studio zero-lag vocal sync with Whisper word timestamps, Spotify Poppins Bold, 50/50 balanced couplets | 18 | Dan Music (305s) | 185.0 MB | [21_Coldplay_Clocks_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/21_Coldplay_Clocks_Lyric_Video.mp4) |"

new_row = target_row + "\n" + "| **22** | **lovely**<br>Billie Eilish & Khalid | **Makoto Shinkai Ethereal Celestial Aurora Lake** | Vast deep dark midnight indigo & obsidian celestial sky (88-90% negative space) with subtle ribbons of northern lights / aurora borealis & brilliant diamond stars, still reflective frozen lake & solitary silhouette (10-12%), directly visualizing 'Isn't it lovely, all alone? / Even if it takes all night or a hundred years', Studio zero-lag vocal sync, Spotify Poppins Bold, 50/50 balanced couplets | 16 | 7clouds (201s) | 135.0 MB | [22_Billie_Eilish_Khalid_lovely_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/22_Billie_Eilish_Khalid_lovely_Lyric_Video.mp4) |"

# Carousel slide 21
target_slide = "![Song 21: Clocks (Coldplay) — Cosmic Starlight & Midnight Ocean Bluffs](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_21_clocks_verse1.png)"

# If unicode character was altered, handle both
if target_slide not in content:
    for line in content.splitlines():
        if "audit_21_clocks_verse1.png" in line:
            target_slide = line
            break

new_slide = target_slide + "\n" + "<!-- slide -->\n" + "![Song 22: lovely (Billie Eilish & Khalid) — Ethereal Celestial Aurora Lake](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_22_lovely_hook1.png)"

if target_row in content:
    content = content.replace(target_row, new_row)
else:
    print("Warning: target_row not found!")

if target_slide in content:
    content = content.replace(target_slide, new_slide)
else:
    print("Warning: target_slide not found!")

rep.write_text(content, encoding='utf-8')
print("Updated final_verification_report.md with Song 22!")
