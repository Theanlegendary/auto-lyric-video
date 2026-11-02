import subprocess
import os
import sys

def main():
    clip_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_12717007_wide_rainforest_cabin.mp4"
    audio_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\tin_roof_rain_thunder_60s_loop.wav"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    os.makedirs(out_dir, exist_ok=True)
    
    opt_1min = os.path.join(out_dir, "big_view_cabin_night_1min_optimized.mp4")
    master_3h = os.path.join(out_dir, "our_rain_big_view_cabin_night_3h_master.mp4")

    # Step 1: Render optimized 60s seamless loop at YouTube-optimized sleep bitrate
    # 10s forward + 10s reverse x 3 = 60.0s seamless ping-pong loop
    # Deep midnight blue grade + soft mist bloom + vignette
    filter_complex = (
        "[0:v]trim=start=1:duration=10,setpts=PTS-STARTPTS,split=2[fwd][torev];"
        "[torev]reverse,setpts=PTS-STARTPTS[rev];"
        "[fwd][rev]concat=n=2:v=1:a=0,split=3[c1][c2][c3];"
        "[c1][c2][c3]concat=n=3:v=1:a=0[pingpong];"
        "[pingpong]colorchannelmixer=rr=0.38:rg=0.08:rb=0.0:gr=0.05:gg=0.45:gb=0.20:br=0.10:bg=0.25:bb=0.95,"
        "eq=brightness=-0.07:contrast=1.28:saturation=0.82,"
        "vignette=PI/5[night_wide]"
    )

    cmd_opt = [
        "ffmpeg", "-y",
        "-i", clip_path,
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[night_wide]",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "21",
        "-maxrate", "1200k", "-bufsize", "2400k",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k",
        "-t", "60.0",
        opt_1min
    ]

    print("Step 1: Rendering optimized 60-second seamless loop for Big View Cabin at Night...")
    sys.stdout.flush()
    p1 = subprocess.run(cmd_opt, capture_output=True, text=True)
    if p1.returncode != 0:
        print("Error in Step 1:", p1.stderr[-500:])
        sys.exit(1)
    
    sz_1m = os.path.getsize(opt_1min)
    print(f"Optimized 1-minute loop size: {sz_1m / (1024*1024):.2f} MB")
    sys.stdout.flush()

    # Step 2: Stream-copy concatenate 180 loops into 3-Hour Master Video
    # 180 * 60s = 10,800s = 3.0 Hours
    concat_txt = os.path.join(out_dir, "concat_big_view_3h.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for _ in range(180):
            f.write(f"file '{opt_1min}'\n")

    cmd_concat = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_txt,
        "-c", "copy",
        "-movflags", "+faststart",
        master_3h
    ]

    print("Step 2: Stream-copying 180 loops into 3-Hour Master Video...")
    sys.stdout.flush()
    p2 = subprocess.run(cmd_concat, capture_output=True, text=True)
    if os.path.exists(concat_txt):
        os.remove(concat_txt)

    if p2.returncode != 0:
        print("Error in Step 2:", p2.stderr[-500:])
        sys.exit(1)

    sz_3h = os.path.getsize(master_3h)
    print(f"\n========================================================")
    print(f"SUCCESS! Big-View Cabin at Night 3-Hour Master Generated!")
    print(f"File: {master_3h}")
    print(f"Size: {sz_3h / (1024*1024*1024):.2f} GB ({sz_3h / (1024*1024):.1f} MB)")
    print(f"Duration: Exactly 3 Hours (10,800 seconds)")
    print(f"========================================================")

if __name__ == "__main__":
    main()
