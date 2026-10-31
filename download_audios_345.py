import subprocess
from pathlib import Path

songs = [
    ("Taylor_Swift_The_Fate_of_Ophelia", "rbmdfEQODOw"),
    ("HUNTR_X_Golden", "BvYZXYPuuos"),
    ("Billie_Eilish_BIRDS_OF_A_FEATHER", "d5gf9dXbPi0")
]

base_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs")

for name, ytid in songs:
    s_dir = base_dir / name
    out_audio = s_dir / "audio.mp3"
    if out_audio.exists() and out_audio.stat().st_size > 100000:
        print(f"[{name}] Audio already downloaded.")
        continue
    print(f"[{name}] Downloading audio from YouTube ({ytid})...")
    cmd = [
        "yt-dlp",
        "-x", "--audio-format", "mp3",
        "-o", str(s_dir / "audio.%(ext)s"),
        f"https://www.youtube.com/watch?v={ytid}"
    ]
    subprocess.run(cmd, check=True)
    print(f"[{name}] Audio download complete!")
