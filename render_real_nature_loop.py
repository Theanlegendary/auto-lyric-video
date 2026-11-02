import subprocess
import os
import sys

def main():
    video_in = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_roof_rain_5210318.mp4"
    audio_in = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\tin_roof_rain_thunder_60s_loop.wav"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    os.makedirs(out_dir, exist_ok=True)
    video_out = os.path.join(out_dir, "real_nature_tin_roof_rain_seamless_loop.mp4")

    # Filter complex:
    # 1. Take first 30 seconds of video
    # 2. Duplicate and reverse it
    # 3. Concat forward + reverse -> 60s continuous loop with zero jump cut
    # 4. Apply eq contrast boost & rich saturation
    filter_str = (
        "[0:v]trim=start=0:duration=30,setpts=PTS-STARTPTS,split=2[fwd][to_rev];"
        "[to_rev]reverse,setpts=PTS-STARTPTS[rev];"
        "[fwd][rev]concat=n=2:v=1:a=0[pingpong];"
        "[pingpong]eq=contrast=1.22:brightness=-0.04:saturation=1.18[graded]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", video_in,
        "-i", audio_in,
        "-filter_complex", filter_str,
        "-map", "[graded]",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "256k",
        "-t", "60.0",
        video_out
    ]

    print("Rendering 60s real nature seamless ping-pong loop...")
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        print("FFmpeg error:", p.stderr[-500:])
        sys.exit(1)
    else:
        print("Render complete! Output file:", video_out)
        print("Size:", os.path.getsize(video_out), "bytes")

if __name__ == "__main__":
    main()
