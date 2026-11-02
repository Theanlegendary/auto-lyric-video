import subprocess
from pathlib import Path
from PIL import Image

base = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video")
brain = Path(r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
song_dir = base / "songs" / "30_Ed_Sheeran_Perfect"
bg = song_dir / "perfect_80sky_20sea_bluefilter.png"
ass = song_dir / "test_hero_title.ass"
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

ass_esc = ass.as_posix().replace(":", "\\\\:")
vf = f"setpts=PTS+4/TB,subtitles={ass_esc}:fontsdir={fonts_escaped}"

out = brain / "audit_perfect_hero_middle_title.png"
crop = brain / "crop_perfect_hero_middle_title.png"

cmd = ["ffmpeg", "-y", "-i", str(bg), "-vf", vf, "-vframes", "1", str(out)]
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    im = Image.open(out)
    crop_im = im.crop((200, 250, 1720, 800))
    crop_im.save(crop)
    print("SUCCESS! Rendered middle hero title frame:", out.name, crop.name)
else:
    print("Error:", res.stderr[-500:])
