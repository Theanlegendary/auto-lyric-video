import sys
from pathlib import Path

brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
rep = brain / "final_verification_report.md"

content = rep.read_text(encoding='utf-8')

# Target table row 15
target_row = "| **15** | **Lonely (Starry Twilight Vibe Edition)**<br>Akon | **Starry Celestial Night (80%) & Amber Sunset (20%) Solitary Vibe** | 80% deep celestial starry sky / 20% amber sunset horizon, solitary anime character on rocky ledge gazing upward, Spotify-style Poppins Bold sentence case typography, 50/50 balanced couplets | 42 | 7clouds (18.1M) | 120.9 MB | [15_Akon_Lonely_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/15_Akon_Lonely_Lyric_Video.mp4) |"

new_row = target_row + "\n" + "| **16** | **Love Yourself**<br>Justin Bieber | **Sunlit Coastal Terrace & Acoustic Guitar Breeze** | Warm sunlit room & panoramic terrace overlooking coastal town, acoustic guitar, sheer fluttering curtains, Spotify-style Poppins Bold sentence case typography, 50/50 balanced couplets | 25 | Cakes & Eclairs | 115.0 MB | [16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4](file:///C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/videos/16_Justin_Bieber_Love_Yourself_Lyric_Video.mp4) |"

# Carousel slide 15
target_slide = "![Song 15: Lonely (Akon) — 80% Starry Celestial Night & 20% Amber Sunset Solitary Vibe](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_starry_vibe_chorus.png)"

new_slide = target_slide + "\n" + "<!-- slide -->\n" + "![Song 16: Love Yourself (Justin Bieber) — Sunlit Coastal Terrace & Acoustic Guitar Breeze](/C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/audit_16_love_yourself_chorus.png)"

assert target_row in content, "Target row not found!"
assert target_slide in content, "Target slide not found!"

content = content.replace(target_row, new_row)
content = content.replace(target_slide, new_slide)

rep.write_text(content, encoding='utf-8')
print("Updated final_verification_report.md with Song 16!")
