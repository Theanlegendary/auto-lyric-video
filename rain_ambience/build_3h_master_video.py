import subprocess
import os
import sys

def main():
    clip_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_7843122_tin_roof_forest_rain.mp4"
    audio_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\tin_roof_rain_thunder_60s_loop.wav"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    os.makedirs(out_dir, exist_ok=True)
    
    opt_1min = os.path.join(out_dir, "monetizable_cozy_tin_roof_1min_optimized.mp4")
    master_3h = os.path.join(out_dir, "our_rain_cozy_tin_roof_3h_master.mp4")

    # Step 1: Encode pristine 60-second seamless loop at YouTube-optimized sleep bitrate
    # Video: 1080p, CRF 20, maxrate 1400k, bufsize 2800k (~950 kbps average)
    # Audio: 160k AAC (high fidelity rain and thunder)
    # Soft mist bloom + high contrast
    filter_complex = (
        "[0:v]trim=start=1:duration=15,setpts=PTS-STARTPTS,split=2[fwd1][torev1];"
        "[torev1]reverse,setpts=PTS-STARTPTS[rev1];"
        "[fwd1][rev1]concat=n=2:v=1:a=0,split=2[c1][c2];"
        "[c1][c2]concat=n=2:v=1:a=0,split=2[base][glow];"
        "[glow]boxblur=8:1[blurred];"
        "[base][blurred]blend=all_mode=lighten:all_opacity=0.20[softened];"
        "[softened]eq=contrast=1.22:brightness=-0.03:saturation=1.20[graded]"
    )

    cmd_opt = [
        "ffmpeg", "-y",
        "-i", clip_path,
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[graded]",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-maxrate", "1400k", "-bufsize", "2800k",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k",
        "-t", "60.0",
        opt_1min
    ]

    print("Step 1: Rendering optimized 60-second seamless loop...")
    p1 = subprocess.run(cmd_opt, capture_output=True, text=True)
    if p1.returncode != 0:
        print("Error in Step 1:", p1.stderr[-500:])
        sys.exit(1)
    
    sz_1m = os.path.getsize(opt_1min)
    print(f"Optimized 1-minute loop size: {sz_1m / (1024*1024):.2f} MB")

    # Step 2: Build 3-Hour Master Video (180 repetitions of 1-minute loop)
    # 180 * 60s = 10,800s = 3.0 Hours
    concat_txt = os.path.join(out_dir, "concat_3h.txt")
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
    p2 = subprocess.run(cmd_concat, capture_output=True, text=True)
    if os.path.exists(concat_txt):
        os.remove(concat_txt)

    if p2.returncode != 0:
        print("Error in Step 2:", p2.stderr[-500:])
        sys.exit(1)

    sz_3h = os.path.getsize(master_3h)
    print(f"\n========================================================")
    print(f"SUCCESS! 3-Hour Master Video Generated!")
    print(f"File: {master_3h}")
    print(f"Size: {sz_3h / (1024*1024*1024):.2f} GB ({sz_3h / (1024*1024):.1f} MB)")
    print(f"Duration: Exactly 3 Hours (10,800 seconds)")
    print(f"========================================================")

if __name__ == "__main__":
    main()
