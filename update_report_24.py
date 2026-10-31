import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6\final_verification_report.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace header if desired or keep table row
row_23 = '| **23** | **Counting Stars**<br>OneRepublic | **Makoto Shinkai Celestial Shooting Star Night & Grassy Ridge** | Vast deep dark midnight sapphire celestial sky (85%) with sparkling stardust & dynamic shooting stars, quiet grassy hill bluff & lone silhouette (15%), directly visualizing \'No more counting dollars, we\'ll be counting stars\', Hooked Title Intro (170pt bold), Studio zero-lag vocal sync, Spotify Poppins Bold, 50/50 balanced couplets | 29 | 7clouds (258s) | 165.0 MB | [23_OneRepublic_Counting_Stars_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/23_OneRepublic_Counting_Stars_Lyric_Video.mp4) |'

row_24 = '| **24** | **The Night We Met**<br>Lord Huron | **Makoto Shinkai Cosmic Midnight Starlit Sky, Misty Pine Valley & Solitary Ridge Traveler** | Vast deep dark midnight sapphire & obsidian celestial sky (85%) with shimmering stardust ribbons, quiet misty pine valley & lone ridge silhouette (15%), directly visualizing \'Take me back to the night we met / I am not the only traveler\', Hooked Title Intro (170pt bold), Studio zero-lag vocal sync with Whisper word timestamps, Spotify Poppins Bold, 50/50 balanced couplets | 12 | Official Audio (208s) | 137.1 MB | [24_Lord_Huron_The_Night_We_Met_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/24_Lord_Huron_The_Night_We_Met_Lyric_Video.mp4) |'

content = content.replace(row_23, row_23 + '\n' + row_24)

slide_23 = '![Song 23: Counting Stars (OneRepublic) — Celestial Shooting Star Night](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_23_counting_stars_title.png)'
slide_24 = '''<!-- slide -->
![Song 24: The Night We Met (Lord Huron) — Cosmic Midnight Starlit Sky & Ridge Traveler](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_24_the_night_we_met_title.png)'''

content = content.replace(slide_23, slide_23 + '\n' + slide_24)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated final_verification_report.md successfully with Song 24!')
