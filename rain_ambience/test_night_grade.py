import subprocess
import os

clip = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_7843122_tin_roof_forest_rain.mp4"
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
out_night_frame = os.path.join(brain, "test_night_grade_frame.jpg")

# Day-for-night filter:
# 1. colorchannelmixer for deep midnight blue / moonlight tones
# 2. eq for dark ambient shadows & moonlit silver highlights
# 3. curves / vignette to eliminate blinding white sky
vf = (
    "scale=960:540,"
    "colorchannelmixer=rr=0.32:rg=0.08:rb=0.0:gr=0.05:gg=0.38:gb=0.18:br=0.05:bg=0.18:bb=0.85,"
    "eq=brightness=-0.12:contrast=1.35:saturation=0.80,"
    "vignette=PI/4"
)

cmd = [
    "ffmpeg", "-y",
    "-ss", "00:00:05",
    "-i", clip,
    "-vframes", "1",
    "-vf", vf,
    out_night_frame
]

subprocess.run(cmd, capture_output=True)
print("Extracted test night frame:", os.path.exists(out_night_frame))
