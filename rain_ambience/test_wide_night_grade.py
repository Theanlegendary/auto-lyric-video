import subprocess
import os

clips = [
    ("12717007", r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_12717007_wide_rainforest_cabin.mp4"),
    ("13446069", r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_13446069_wide_foggy_pine_forest_rain.mp4")
]

brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

# Night grade filter:
# colorchannelmixer for deep midnight blue + dark contrast + vignette
vf = (
    "scale=960:540,"
    "colorchannelmixer=rr=0.38:rg=0.08:rb=0.0:gr=0.05:gg=0.45:gb=0.20:br=0.10:bg=0.25:bb=0.95,"
    "eq=brightness=-0.08:contrast=1.28:saturation=0.82,"
    "vignette=PI/5"
)

for vid, path in clips:
    out_p = os.path.join(brain, f"night_wide_graded_{vid}.jpg")
    cmd = ["ffmpeg", "-y", "-ss", "00:00:04", "-i", path, "-vframes", "1", "-vf", vf, out_p]
    subprocess.run(cmd, capture_output=True)
    print(f"Graded {vid}: {os.path.exists(out_p)}")
