import subprocess
import os
import sys

def main():
    video_raw = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\danny_louis_60s_raw.mp4"
    audio_wav = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\tin_roof_rain_thunder_60s_loop.wav"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    os.makedirs(out_dir, exist_ok=True)
    out_video = os.path.join(out_dir, "our_tin_roof_rain_seamless_loop.mp4")

    # Filter complex:
    # 1. Take first 30 seconds of the tin roof rain footage
    # 2. Duplicate and reverse it
    # 3. Concatenate forward (0->30s) + reverse (30s->0s) -> 60s seamless loop
    # 4. Apply high-contrast color grade (contrast 1.28, rich saturation, deep murky forest shadows)
    filter_str = (
        "[0:v]trim=start=0:duration=30,setpts=PTS-STARTPTS,split=2[fwd][to_rev];"
        "[to_rev]reverse,setpts=PTS-STARTPTS[rev];"
        "[fwd][rev]concat=n=2:v=1:a=0[pingpong];"
        "[pingpong]eq=contrast=1.28:brightness=-0.03:saturation=1.22[graded]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", video_raw,
        "-i", audio_wav,
        "-filter_complex", filter_str,
        "-map", "[graded]",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "fast", "-crf", "17", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "256k",
        "-t", "60.0",
        out_video
    ]

    print("Rendering 60s master 'Our Rain' video with ping-pong seamless loop & contrast grade...")
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        print("Error:", p.stderr[-500:])
        sys.exit(1)
    else:
        print("Success! Output size:", os.path.getsize(out_video), "bytes")

if __name__ == "__main__":
    main()
