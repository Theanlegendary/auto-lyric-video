import subprocess
import os

clip_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_5174040_alpine_lake_rain.mp4"
audio_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\tin_roof_rain_thunder_60s_loop.wav"
out_sample = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos\pure_nature_option1_alpine_lake_night_1min.mp4"

# 15s forward + 15s reverse x 2 = 60.0s seamless ping-pong loop
filter_complex = (
    "[0:v]trim=start=2:duration=15,setpts=PTS-STARTPTS,split=2[fwd][torev];"
    "[torev]reverse,setpts=PTS-STARTPTS[rev];"
    "[fwd][rev]concat=n=2:v=1:a=0,split=2[c1][c2];"
    "[c1][c2]concat=n=2:v=1:a=0[pingpong];"
    "[pingpong]colorchannelmixer=rr=0.40:rg=0.08:rb=0.0:gr=0.05:gg=0.45:gb=0.20:br=0.10:bg=0.25:bb=0.95,"
    "eq=brightness=-0.06:contrast=1.26:saturation=0.85,"
    "vignette=PI/5[night_lake]"
)

cmd = [
    "ffmpeg", "-y",
    "-i", clip_path,
    "-i", audio_path,
    "-filter_complex", filter_complex,
    "-map", "[night_lake]",
    "-map", "1:a",
    "-c:v", "libx264", "-preset", "medium", "-crf", "23",
    "-maxrate", "950k", "-bufsize", "1900k",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "128k",
    "-t", "60.0",
    "-movflags", "+faststart",
    out_sample
]

print("Rendering Option 1 (Alpine Mountain Lake) 1-minute sample...")
p = subprocess.run(cmd, capture_output=True, text=True)
if p.returncode == 0:
    print(f"Option 1 Sample ready! Size: {os.path.getsize(out_sample)/(1024*1024):.2f} MB")
else:
    print("Error:", p.stderr[-400:])
