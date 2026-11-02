import subprocess
import os
import sys

def build_long_video(duration_hours=3, input_sample=None, output_path=None):
    if input_sample is None:
        input_sample = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos\monetizable_cozy_tin_roof_rain_1min_sample.mp4"
    
    if output_path is None:
        out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
        output_path = os.path.join(out_dir, f"our_rain_monetizable_{duration_hours}h_master.mp4")

    # 1-minute sample needs 60 repetitions per hour
    repeat_count = int(duration_hours * 60)
    list_file = os.path.join(os.path.dirname(input_sample), f"concat_{duration_hours}h_list.txt")

    print(f"Generating {duration_hours}-hour video from seamless 1-minute loop...")
    print(f"Repetitions required: {repeat_count}")

    with open(list_file, "w", encoding="utf-8") as f:
        for _ in range(repeat_count):
            f.write(f"file '{input_sample}'\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", list_file,
        "-c", "copy",
        "-movflags", "+faststart",
        output_path
    ]

    print("Running stream copy concatenation (instant, zero quality loss)...")
    p = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(list_file):
        os.remove(list_file)

    if p.returncode != 0:
        print("Error:", p.stderr[-500:])
        return False
    else:
        print(f"Successfully generated {duration_hours}h master video!")
        print("Output:", output_path)
        print("Size:", os.path.getsize(output_path), "bytes")
        return True

if __name__ == "__main__":
    hours = 3
    if len(sys.argv) > 1:
        hours = float(sys.argv[1])
    build_long_video(hours)
