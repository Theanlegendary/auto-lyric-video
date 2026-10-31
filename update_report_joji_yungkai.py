import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

report = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/final_verification_report.md")
content = report.read_text(encoding="utf-8")

# 1. Update the table
target_table = """| **26** | **Another Love**<br>Tom Odell | **Makoto Shinkai Clear Pink Aesthetic Sunset & Pine Ridge** | Expansive luminous pastel sunset sky (85%) with gentle peach, rose pink & lavender gradients, single delicate shooting star, serene pine ridge silhouette & solitary figure (15%), directly visualizing 'All my tears have been used up / On another love', Until I Found You Clean Style, Large Patrick Hand Typography (102-114pt), 175pt Title Card, 50/50 balanced couplets | 21 | 7clouds (241s) | 158.0 MB | [26_Tom_Odell_Another_Love_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/26_Tom_Odell_Another_Love_Lyric_Video.mp4) |"""

new_table_rows = """| **26** | **Another Love**<br>Tom Odell | **Makoto Shinkai Clear Pink Aesthetic Sunset & Pine Ridge** | Expansive luminous pastel sunset sky (85%) with gentle peach, rose pink & lavender gradients, single delicate shooting star, serene pine ridge silhouette & solitary figure (15%), directly visualizing 'All my tears have been used up / On another love', Until I Found You Clean Style, Large Patrick Hand Typography (102-114pt), 175pt Title Card, 50/50 balanced couplets | 21 | 7clouds (241s) | 158.0 MB | [26_Tom_Odell_Another_Love_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/26_Tom_Odell_Another_Love_Lyric_Video.mp4) |
| **27A** | **Glimpse of Us (Normal 1.0x Mix)**<br>Joji | **Makoto Shinkai Moody Indigo Twilight Sky & Solitary Rain Ledge** | Deep sapphire & moody rain-twilight color clouds (85% clean reading space) with solitary silhouette on rain-slicked ledge (`bg_33`), seamless live cloud drift (14px/s), Patrick Hand 200pt Hook Title, glowing pure white 2-row couplets, zero-lag timing | 24 | 7clouds (234s) | 161.7 MB | [27_Joji_Glimpse_of_Us_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/27_Joji_Glimpse_of_Us_Lyric_Video.mp4) |
| **27B** | **Glimpse of Us (Slowed + Reverb Brand Master)**<br>Joji | **Makoto Shinkai Moody Indigo Twilight Sky & Solitary Rain Ledge** | 0.865x tape varispeed slowdown (85 &rarr; 73.5 BPM), 3.0s cathedral reverb hall, -2.5 semitones pitch drop, warm 15.5kHz cassette tape shelf, seamless live cloud drift (12px/s), Patrick Hand 200pt Hook Title, glowing pure white 2-row couplets | 24 | Brand Master (271s) | 186.7 MB | [27_Joji_Glimpse_of_Us_Slowed_Reverb_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/27_Joji_Glimpse_of_Us_Slowed_Reverb_Lyric_Video.mp4) |
| **28A** | **blue (Normal 1.0x Mix)**<br>yung kai | **Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook** | Serene pastel cyan & soft morning azure clouds (85% clean reading space) with grassy coastal cliff overlook (`bg_34`), seamless live cloud drift (14px/s), Patrick Hand 200pt Hook Title, glowing pure white 2-row couplets | 17 | Vibe Music (215s) | 154.0 MB | [28_yung_kai_blue_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/28_yung_kai_blue_Lyric_Video.mp4) |
| **28B** | **blue (Slowed + Reverb Brand Master)**<br>yung kai | **Makoto Shinkai Dreamy Pastel Dawn Sky & Coastal Overlook** | 0.865x tape varispeed slowdown, 3.0s cathedral reverb hall, -2.5 semitones pitch drop, warm 15.5kHz cassette tape shelf, seamless live cloud drift (12px/s), Patrick Hand 200pt Hook Title, glowing pure white 2-row couplets | 17 | Brand Master (249s) | 174.5 MB | [28_yung_kai_blue_Slowed_Reverb_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/28_yung_kai_blue_Slowed_Reverb_Lyric_Video.mp4) |"""

content = content.replace(target_table, new_table_rows)

# 2. Update the carousel
target_carousel_end = """<!-- slide -->
![Song 26: Another Love (Tom Odell) — Clear Pink Aesthetic Sunset & Pine Ridge](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_26_another_love_title.png)
````"""

new_carousel_slides = """<!-- slide -->
![Song 26: Another Love (Tom Odell) — Clear Pink Aesthetic Sunset & Pine Ridge](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_26_another_love_title.png)
<!-- slide -->
![Song 27: Glimpse of Us (Joji) — Title Hook Card (200pt Pure White Glow)](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/crop_audit_joji_normal_title.png)
<!-- slide -->
![Song 27: Glimpse of Us (Joji) — Chorus Couplet (A Glimpse of Us)](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/crop_audit_joji_normal_chorus.png)
<!-- slide -->
![Song 28: blue (yung kai) — Title Hook Card (200pt Pure White Glow)](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/crop_audit_yungkai_normal_title.png)
<!-- slide -->
![Song 28: blue (yung kai) — Chorus Couplet (Picture Us / Waves)](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/crop_audit_yungkai_normal_chorus.png)
````"""

content = content.replace(target_carousel_end, new_carousel_slides)
report.write_text(content, encoding="utf-8")
print("final_verification_report.md updated successfully.")
