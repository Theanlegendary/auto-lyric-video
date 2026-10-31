import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
rep = brain / "final_verification_report.md"

content = rep.read_text(encoding='utf-8')

# Target table row 22
target_row = "| **22** | **lovely**<br>Billie Eilish & Khalid | **Makoto Shinkai Ethereal Celestial Aurora Lake** | Vast deep dark midnight indigo & obsidian celestial sky (88-90% negative space) with subtle ribbons of northern lights / aurora borealis & brilliant diamond stars, still reflective frozen lake & solitary silhouette (10-12%), directly visualizing 'Isn't it lovely, all alone? / Even if it takes all night or a hundred years', Studio zero-lag vocal sync, Spotify Poppins Bold, 50/50 balanced couplets | 16 | 7clouds (201s) | 135.0 MB | [22_Billie_Eilish_Khalid_lovely_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/22_Billie_Eilish_Khalid_lovely_Lyric_Video.mp4) |"

new_row = target_row + "\n" + "| **23** | **Counting Stars**<br>OneRepublic | **Makoto Shinkai Celestial Shooting Star Night & Grassy Ridge** | Vast deep dark midnight sapphire celestial sky (85%) with sparkling stardust & dynamic shooting stars, quiet grassy hill bluff & lone silhouette (15%), directly visualizing 'No more counting dollars, we'll be counting stars', Hooked Title Intro (170pt bold), Studio zero-lag vocal sync, Spotify Poppins Bold, 50/50 balanced couplets | 29 | 7clouds (258s) | 165.0 MB | [23_OneRepublic_Counting_Stars_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/23_OneRepublic_Counting_Stars_Lyric_Video.mp4) |"

# Carousel slide 22
target_slide = ""
for line in content.splitlines():
    if "audit_22_lovely_hook1.png" in line:
        target_slide = line
        break

new_slide = target_slide + "\n" + "<!-- slide -->\n" + "![Song 23: Counting Stars (OneRepublic) — Celestial Shooting Star Night](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_23_counting_stars_title.png)"

if target_row in content:
    content = content.replace(target_row, new_row)
else:
    print("Warning: target_row not found!")

if target_slide and target_slide in content:
    content = content.replace(target_slide, new_slide)
else:
    print("Warning: target_slide not found!")

rep.write_text(content, encoding='utf-8')
print("Updated final_verification_report.md with Song 23!")
