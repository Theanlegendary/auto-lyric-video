import subprocess
import os

clip = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_7843122_tin_roof_forest_rain.mp4"
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
out_frame = os.path.join(brain, "soft_mist_real_nature_frame.jpg")

# Test cinematic soft bloom filter:
# 1. Split into sharp and blur
# 2. Blend with subtle screen/overlay opacity
# 3. Apply rich contrast & deep green saturation
vf = (
    "scale=960:540,"
    "split=2[base][glow];"
    "[glow]boxblur=10:2[blurred];"
    "[base][blurred]blend=all_mode=lighten:all_opacity=0.22[soft];"
    "[soft]eq=contrast=1.20:brightness=-0.03:saturation=1.18"
)

cmd = [
    "ffmpeg", "-y",
    "-ss", "00:00:05",
    "-i", clip,
    "-vframes", "1",
    "-vf", vf,
    out_frame
]

subprocess.run(cmd, capture_output=True)
print("Extracted soft mist frame:", os.path.exists(out_frame))
