import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6\final_verification_report.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

row_24 = '| **24** | **The Night We Met**<br>Lord Huron | **Makoto Shinkai Cosmic Midnight Starlit Sky, Misty Pine Valley & Solitary Ridge Traveler** | Vast deep dark midnight sapphire & obsidian celestial sky (85%) with shimmering stardust ribbons, quiet misty pine valley & lone ridge silhouette (15%), directly visualizing \'Take me back to the night we met / I am not the only traveler\', Hooked Title Intro (170pt bold), Studio zero-lag vocal sync with Whisper word timestamps, Spotify Poppins Bold, 50/50 balanced couplets | 12 | Official Audio (208s) | 137.1 MB | [24_Lord_Huron_The_Night_We_Met_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/24_Lord_Huron_The_Night_We_Met_Lyric_Video.mp4) |'

row_25 = '| **25** | **Sweater Weather**<br>The Neighbourhood | **Makoto Shinkai Celestial Coastal Twilight & Solitary Knit Sweater Silhouette** | Vast deep dark midnight sapphire & indigo celestial sky (85%) with shimmering Milky Way & constellations, quiet wooden coastal overlook railing & solitary figure in cozy oversized knit sweater (15%), directly visualizing \'Use the sleeves of my sweater / Too cold for you here\', Hooked Title Intro (170pt bold), Studio zero-lag vocal sync with Whisper word timestamps, Spotify Poppins Bold, 50/50 balanced couplets | 24 | 7clouds (237s) | 155.0 MB | [25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4) |'

if row_24 in content:
    content = content.replace(row_24, row_24 + '\n' + row_25)

slide_24 = '![Song 24: The Night We Met (Lord Huron) — Cosmic Midnight Starlit Sky & Ridge Traveler](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_24_the_night_we_met_title.png)'
slide_25 = '''<!-- slide -->
![Song 25: Sweater Weather (The Neighbourhood) — Celestial Coastal Twilight Overlook](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_25_sweater_weather_bridge_title.png)'''

if slide_24 in content:
    content = content.replace(slide_24, slide_24 + '\n' + slide_25)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated final_verification_report.md successfully with Song 25!')
