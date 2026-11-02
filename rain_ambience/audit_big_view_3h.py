import cv2
import os
import sys

def audit_video(video_path):
    if not os.path.exists(video_path):
        print(f"File not found: {video_path}")
        return False

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Failed to open {video_path}")
        return False

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_sec = total_frames / fps if fps > 0 else 0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    file_size_gb = os.path.getsize(video_path) / (1024 * 1024 * 1024)

    print("================ VIDEO AUDIT REPORT ================")
    print(f"Path: {video_path}")
    print(f"Resolution: {width}x{height}")
    print(f"FPS: {fps:.2f}")
    print(f"Total Frames: {total_frames}")
    print(f"Duration: {duration_sec:.2f} seconds ({duration_sec / 3600:.2f} hours)")
    print(f"File Size: {file_size_gb:.3f} GB ({file_size_gb * 1024:.1f} MB)")
    print("=====================================================")

    # Sample audit frames at 3 key timepoints:
    # 1. 01:00:00 (3600s)
    # 2. 02:00:00 (7200s)
    # 3. 02:59:00 (10740s)
    timestamps = [
        ("hour1", 3600.0),
        ("hour2", 7200.0),
        ("hour2_59m", 10740.0)
    ]

    artifact_dir = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
    for label, ts in timestamps:
        target_frame = int(ts * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
        ret, frame = cap.read()
        if ret:
            out_img = os.path.join(artifact_dir, f"audit_big_view_3h_{label}.jpg")
            cv2.imwrite(out_img, frame)
            print(f"Extracted frame at {ts}s ({label}): {out_img}")
        else:
            print(f"Failed to read frame at {ts}s")

    cap.release()
    return duration_sec >= 10790.0

if __name__ == "__main__":
    vpath = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos\our_rain_big_view_cabin_night_3h_master.mp4"
    success = audit_video(vpath)
    if not success:
        sys.exit(1)
