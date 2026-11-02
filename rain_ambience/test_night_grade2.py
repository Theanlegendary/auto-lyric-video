import subprocess
import os

clip = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_7843122_tin_roof_forest_rain.mp4"
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
out_night_frame2 = os.path.join(brain, "test_night_grade_frame2.jpg")

# Balanced Night Grade:
# Preserves the glistening raindrops and roof texture, but cools the entire scene into dark midnight blue/slate
vf = (
    "scale=960:540,"
    "colorchannelmixer=rr=0.45:rg=0.10:rb=0.0:gr=0.05:gg=0.55:gb=0.20:br=0.10:bg=0.25:bb=0.95,"
    "eq=brightness=-0.07:contrast=1.24:saturation=0.85,"
    "vignette=PI/5"
)

cmd = [
    "ffmpeg", "-y",
    "-ss", "00:00:05",
    "-i", clip,
    "-vframes", "1",
    "-vf", vf,
    out_night_frame2
]

subprocess.run(cmd, capture_output=True)
print("Extracted test night frame 2:", os.path.exists(out_night_frame2))
