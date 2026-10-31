from PIL import ImageFont
from pathlib import Path

font_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts\PatrickHand.ttf"
font = ImageFont.truetype(font_path, 102)

song_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\00_Justin_Bieber_That_Should_Be_Me")
ass_text = (song_dir / "lyrics_single.ass").read_text(encoding="utf-8")

max_w = 0
longest_line = ""
for line in ass_text.splitlines():
    if line.startswith("Dialogue:"):
        parts = line.split(",,")[-1]
        clean = parts
        while "{" in clean and "}" in clean:
            s = clean.find("{")
            e = clean.find("}")
            clean = clean[:s] + clean[e+1:]
        sub_lines = clean.split(r"\N")
        for sl in sub_lines:
            sl = sl.strip()
            if sl:
                bbox = font.getbbox(sl)
                w = bbox[2] - bbox[0]
                if w > max_w:
                    max_w = w
                    longest_line = sl

print(f"Max line pixel width: {max_w}px (Screen width: 1920px, Safe max: 1600px)")
print(f"Longest line: '{longest_line}'")
if max_w < 1600:
    print("VERIFICATION PASS: All lines easily fit within 1920x1080 without truncation!")
else:
    print("WARNING: Line exceeds safe width!")
