import os
import subprocess
import time

def build_3h_master():
    vids_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    loop_video = os.path.join(vids_dir, "alpine_lake_master_loop_opt.mp4")
    master_video = os.path.join(vids_dir, "our_rain_alpine_lake_fireflies_3h_master.mp4")
    concat_list = os.path.join(vids_dir, "concat_alpine_180.txt")

    if not os.path.exists(loop_video):
        print(f"Error: {loop_video} does not exist!")
        return

    # 180 repetitions of 60.0s = 10,800s = 3.0 Hours exact
    repetitions = 180
    print(f"Generating concat list with {repetitions} repetitions for 3.0 Hours exact...")
    with open(concat_list, "w", encoding="utf-8") as f:
        for _ in range(repetitions):
            f.write(f"file '{loop_video}'\n")

    print(f"Running stream-copy concatenation to build 3-Hour Master: {master_video}...")
    t0 = time.time()
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list,
        "-c", "copy",
        "-movflags", "+faststart",
        master_video
    ]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)

    if os.path.exists(concat_list):
        os.remove(concat_list)

    elapsed = time.time() - t0
    if os.path.exists(master_video):
        sz_mb = os.path.getsize(master_video) / (1024 * 1024)
        print(f"SUCCESS! 3-Hour Master Video built in {elapsed:.1f}s!")
        print(f"Master File: {master_video}")
        print(f"Total Size: {sz_mb:.2f} MB")
        # Remove intermediate loop to save disk space
        if os.path.exists(loop_video):
            os.remove(loop_video)
            print("Cleaned up intermediate loop video to maximize free space.")
    else:
        print("Concatenation failed! Error:", res.stderr[-500:])

if __name__ == "__main__":
    build_3h_master()
