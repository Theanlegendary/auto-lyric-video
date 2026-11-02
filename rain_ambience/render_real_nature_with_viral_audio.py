import subprocess
import os
import sys

def render_real_nature_master():
    clip_1 = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_7843122_tin_roof_forest_rain.mp4"
    audio_wav = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\viral_channel_rain_70m_60s_loop.wav"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    os.makedirs(out_dir, exist_ok=True)
    out_video_1 = os.path.join(out_dir, "real_nature_tin_roof_rain_70m_channel_sound.mp4")

    # 15s forward + 15s reverse x 2 = 60.0s seamless loop
    # Filter complex:
    filter_str_1 = (
        "[0:v]trim=start=1:duration=15,setpts=PTS-STARTPTS,split=2[fwd1][torev1];"
        "[torev1]reverse,setpts=PTS-STARTPTS[rev1];"
        "[fwd1][rev1]concat=n=2:v=1:a=0,split=2[cycle1][cycle2];"
        "[cycle1][cycle2]concat=n=2:v=1:a=0[pingpong];"
        "[pingpong]eq=contrast=1.26:brightness=-0.04:saturation=1.22[graded]"
    )

    cmd_1 = [
        "ffmpeg", "-y",
        "-i", clip_1,
        "-i", audio_wav,
        "-filter_complex", filter_str_1,
        "-map", "[graded]",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "fast", "-crf", "17", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "256k",
        "-t", "60.0",
        out_video_1
    ]

    print("Rendering Primary Real Nature Rain Master with 70M-view Channel Sound...")
    p1 = subprocess.run(cmd_1, capture_output=True, text=True)
    if p1.returncode != 0:
        print("Error 1:", p1.stderr[-500:])
        sys.exit(1)
    print("Success! Created:", out_video_1, "Size:", os.path.getsize(out_video_1))

    # Render Option 2: Pine Forest Tin Roof View (clip 4169229)
    clip_2 = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_4169229_corrugated_tin_pine_forest.mp4"
    out_video_2 = os.path.join(out_dir, "real_nature_pine_forest_tin_roof_rain_70m_sound.mp4")

    filter_str_2 = (
        "[0:v]trim=start=0:duration=15,setpts=PTS-STARTPTS,split=2[fwd2][torev2];"
        "[torev2]reverse,setpts=PTS-STARTPTS[rev2];"
        "[fwd2][rev2]concat=n=2:v=1:a=0,split=2[cycle2a][cycle2b];"
        "[cycle2a][cycle2b]concat=n=2:v=1:a=0[pingpong2];"
        "[pingpong2]eq=contrast=1.24:brightness=-0.03:saturation=1.22[graded2]"
    )

    cmd_2 = [
        "ffmpeg", "-y",
        "-i", clip_2,
        "-i", audio_wav,
        "-filter_complex", filter_str_2,
        "-map", "[graded2]",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "fast", "-crf", "17", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "256k",
        "-t", "60.0",
        out_video_2
    ]

    print("Rendering Secondary Pine Forest Real Nature Rain Master...")
    p2 = subprocess.run(cmd_2, capture_output=True, text=True)
    if p2.returncode != 0:
        print("Error 2:", p2.stderr[-500:])
        sys.exit(1)
    print("Success! Created:", out_video_2, "Size:", os.path.getsize(out_video_2))

if __name__ == "__main__":
    render_real_nature_master()
