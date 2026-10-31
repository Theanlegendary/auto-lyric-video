import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6\final_verification_report.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

row_25 = '| **25** | **Sweater Weather**<br>The Neighbourhood | **Makoto Shinkai Celestial Coastal Twilight & Solitary Knit Sweater Silhouette** | Vast deep dark midnight sapphire & indigo celestial sky (85%) with shimmering Milky Way & constellations, quiet wooden coastal overlook railing & solitary figure in cozy oversized knit sweater (15%), directly visualizing \'Use the sleeves of my sweater / Too cold for you here\', Hooked Title Intro (170pt bold), Studio zero-lag vocal sync with Whisper word timestamps, Spotify Poppins Bold, 50/50 balanced couplets | 24 | 7clouds (237s) | 155.0 MB | [25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/25_The_Neighbourhood_Sweater_Weather_Lyric_Video.mp4) |'

row_26 = '| **26** | **Another Love**<br>Tom Odell | **Makoto Shinkai Clear Pink Aesthetic Sunset & Pine Ridge** | Expansive luminous pastel sunset sky (85%) with gentle peach, rose pink & lavender gradients, single delicate shooting star, serene pine ridge silhouette & solitary figure (15%), directly visualizing \'All my tears have been used up / On another love\', Until I Found You Clean Style, Large Patrick Hand Typography (102-114pt), 175pt Title Card, 50/50 balanced couplets | 21 | 7clouds (241s) | 158.0 MB | [26_Tom_Odell_Another_Love_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/26_Tom_Odell_Another_Love_Lyric_Video.mp4) |'

if row_25 in content:
    content = content.replace(row_25, row_25 + '\n' + row_26)

slide_25 = '![Song 25: Sweater Weather (The Neighbourhood) — Celestial Coastal Twilight Overlook](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_25_sweater_weather_bridge_title.png)'
slide_26 = '''<!-- slide -->
![Song 26: Another Love (Tom Odell) — Clear Pink Aesthetic Sunset & Pine Ridge](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_26_another_love_title.png)'''

if slide_25 in content:
    content = content.replace(slide_25, slide_25 + '\n' + slide_26)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated final_verification_report.md successfully with Song 26!')
