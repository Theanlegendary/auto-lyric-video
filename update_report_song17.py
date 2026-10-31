from pathlib import Path

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
rep = brain / "final_verification_report.md"

content = rep.read_text(encoding='utf-8')

# Target table row 16
target_row = "| **16** | **Love Yourself**<br>Justin Bieber | **Sunlit Coastal Terrace & Acoustic Guitar Breeze** | Warm sunlit room & panoramic terrace overlooking coastal town, acoustic guitar, sheer fluttering curtains, Spotify-style Poppins Bold sentence case typography, 50/50 balanced couplets | 25 | Cakes & Eclairs | 115.0 MB | [16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4) |"

new_row = target_row + "\n" + "| **17** | **The One That Got Away**<br>Katy Perry | **Mustang Coastal Cliff & Radiant Summer Sunset (Radiohead Vibe)** | Vintage 1960s Mustang on coastal grassy cliff overlooking ocean, solitary anime girl gazing at golden-lavender sunset, directly visualizing 'make out in your Mustang to Radiohead', Spotify-style Poppins Bold sentence case typography, 50/50 balanced couplets | 30 | 7clouds (18.1M) | 108.0 MB | [17_Katy_Perry_The_One_That_Got_Away_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/17_Katy_Perry_The_One_That_Got_Away_Lyric_Video.mp4) |"

# Carousel slide 16
target_slide = "![Song 16: Love Yourself (Justin Bieber) — Sunlit Coastal Terrace & Acoustic Guitar Breeze](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_16_love_yourself_chorus.png)"

new_slide = target_slide + "\n" + "<!-- slide -->\n" + "![Song 17: The One That Got Away (Katy Perry) — Mustang Coastal Cliff & Radiant Summer Sunset](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_17_the_one_chorus.png)"

if target_row in content:
    content = content.replace(target_row, new_row)
if target_slide in content:
    content = content.replace(target_slide, new_slide)

rep.write_text(content, encoding='utf-8')
print("Updated final_verification_report.md with Song 17!")
