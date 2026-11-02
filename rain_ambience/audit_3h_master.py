import cv2
import os

video_3h = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos\our_rain_cozy_tin_roof_3h_master.mp4"
brain = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"

cap = cv2.VideoCapture(video_3h)
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
dur_seconds = total_frames / fps
hours = dur_seconds / 3600.0

print(f"3-Hour Video Verification:")
print(f"  Total Duration: {dur_seconds:.2f} seconds ({hours:.2f} hours)")
print(f"  Frame Count: {total_frames}")
print(f"  FPS: {fps}")
print(f"  Resolution: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")

audit_points = [
    (3600.0, "audit_3h_hour_1.jpg"),
    (7200.0, "audit_3h_hour_2.jpg"),
    (10740.0, "audit_3h_hour_2h59m.jpg")
]

for sec, fname in audit_points:
    frame_idx = min(int(sec * fps), int(total_frames - 1))
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ret, frame = cap.read()
    if ret:
        small = cv2.resize(frame, (960, 540))
        out_p = os.path.join(brain, fname)
        cv2.imwrite(out_p, small)
        print(f"Extracted {fname} at frame {frame_idx} (Timestamp: {sec/3600.0:.2f}h)")

cap.release()
