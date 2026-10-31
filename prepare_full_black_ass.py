import re

base = "C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video"
source_ass = f"{base}/lyrics_perfect.ass"
target_ass = f"{base}/lyrics_full_black_text.ass"

with open(source_ass, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_styles = """Style: TitleCard,Patrick Hand,185,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,1,0,0,0,95,115,3,0,1,2,1,5,50,50,50,1
Style: Lyric,Patrick Hand,148,&H00151515,&H000000FF,&H00FFFFFF,&H30000000,0,0,0,0,95,115,1,0,1,1.8,0.8,5,50,50,50,1
"""

out_lines = []
in_styles = False

for line in lines:
    if line.startswith("Style:"):
        continue  # skip old styles
    if line.startswith("[Events]"):
        out_lines.append(new_styles)
        out_lines.append("\n")
        out_lines.append(line)
    else:
        out_lines.append(line)

with open(target_ass, "w", encoding="utf-8") as f:
    f.writelines(out_lines)

print(f"Generated {target_ass} with all {len(out_lines)} lines!")
