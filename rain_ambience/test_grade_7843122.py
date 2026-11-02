import subprocess
import os

clip = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_7843122_tin_roof_forest_rain.mp4"
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
raw_frame = os.path.join(brain, "raw_frame_7843122.jpg")
graded_frame = os.path.join(brain, "graded_frame_7843122.jpg")

# Extract raw
cmd_raw = ["ffmpeg", "-y", "-ss", "00:00:05", "-i", clip, "-vframes", "1", "-vf", "scale=960:540", raw_frame]
subprocess.run(cmd_raw, capture_output=True)

# Extract graded: contrast=1.25, brightness=-0.03, saturation=1.22
cmd_graded = ["ffmpeg", "-y", "-ss", "00:00:05", "-i", clip, "-vframes", "1", "-vf", "scale=960:540,eq=contrast=1.25:brightness=-0.03:saturation=1.22", graded_frame]
subprocess.run(cmd_graded, capture_output=True)

print("Extracted raw & graded frames!")
