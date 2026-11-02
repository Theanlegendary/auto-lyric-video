import subprocess
import os
import sys

def main():
    clip_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_7843122_tin_roof_forest_rain.mp4"
    audio_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\tin_roof_rain_thunder_60s_loop.wav"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    os.makedirs(out_dir, exist_ok=True)
    out_video = os.path.join(out_dir, "monetizable_cozy_tin_roof_rain_1min_sample.mp4")

    # 1. Video Filter:
    # - 15s Forward + 15s Reverse x 2 = 60.0s seamless ping-pong loop
    # - Soft mist bloom: split -> boxblur -> lighten blend -> rich contrast (1.20) & saturation (1.18)
    filter_complex = (
        "[0:v]trim=start=1:duration=15,setpts=PTS-STARTPTS,split=2[fwd1][torev1];"
        "[torev1]reverse,setpts=PTS-STARTPTS[rev1];"
        "[fwd1][rev1]concat=n=2:v=1:a=0,split=2[c1][c2];"
        "[c1][c2]concat=n=2:v=1:a=0,split=2[base][glow];"
        "[glow]boxblur=8:1[blurred];"
        "[base][blurred]blend=all_mode=lighten:all_opacity=0.20[softened];"
        "[softened]eq=contrast=1.22:brightness=-0.03:saturation=1.20[graded]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", clip_path,
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[graded]",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "320k",
        "-t", "60.0",
        out_video
    ]

    print("Rendering Monetizable 1-Minute Sample (Soft Mist + Real Nature Tin Roof)...")
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        print("FFmpeg error:", p.stderr[-600:])
        sys.exit(1)
    else:
        print("Successfully rendered master 1-minute sample!")
        print("Output:", out_video)
        print("File Size:", os.path.getsize(out_video), "bytes")

if __name__ == "__main__":
    main()
