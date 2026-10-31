from pathlib import Path

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
rep = brain / "final_verification_report.md"

content = rep.read_text(encoding='utf-8')

target_row = "| **16** | **Love Yourself**<br>Justin Bieber | **Sunlit Coastal Terrace & Acoustic Guitar Breeze** | Warm sunlit room & panoramic terrace overlooking coastal town, acoustic guitar, sheer fluttering curtains, Spotify-style Poppins Bold sentence case typography, 50/50 balanced couplets | 25 | Cakes & Eclairs | 115.0 MB | [16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4) |"

replacement_row = "| **16** | **Love Yourself (Clean Dark Celestial Sky Edition)**<br>Justin Bieber | **Clean Dark Celestial Starry Night Sky & Solitary Ridge** | 85% vast dark sapphire celestial night sky with sparkling stars, 15% subtle dusk twilight rim & solitary ridge, requested clean dark sky for maximum white typography contrast, Spotify-style Poppins Bold sentence case, 50/50 balanced couplets | 24 | Cakes & Eclairs | 105.0 MB | [16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4) |"

target_slide = "![Song 16: Love Yourself (Justin Bieber) — Sunlit Coastal Terrace & Acoustic Guitar Breeze](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_16_love_yourself_chorus.png)"

replacement_slide = "![Song 16: Love Yourself (Justin Bieber) — Clean Dark Celestial Starry Sky & Solitary Ridge](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_16_love_yourself_v2_chorus.png)"

if target_row in content:
    content = content.replace(target_row, replacement_row)
if target_slide in content:
    content = content.replace(target_slide, replacement_slide)

rep.write_text(content, encoding='utf-8')
print("Updated final_verification_report.md for Love Yourself Dark Edition!")
