import subprocess
import os

clip = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_6252550_roof_trees_heavy_rain.mp4"
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
out_night_frame3 = os.path.join(brain, "test_night_grade_frame3.jpg")

vf = (
    "scale=960:540,"
    "colorchannelmixer=rr=0.40:rg=0.10:rb=0.0:gr=0.05:gg=0.48:gb=0.20:br=0.10:bg=0.25:bb=0.95,"
    "eq=brightness=-0.08:contrast=1.26:saturation=0.80,"
    "vignette=PI/5"
)

cmd = [
    "ffmpeg", "-y",
    "-ss", "00:00:05",
    "-i", clip,
    "-vframes", "1",
    "-vf", vf,
    out_night_frame3
]

subprocess.run(cmd, capture_output=True)
print("Extracted test night frame 3:", os.path.exists(out_night_frame3))
