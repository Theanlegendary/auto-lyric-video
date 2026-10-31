import sys, os
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

candidates = [
    Path(os.environ.get("LOCALAPPDATA", "")) / "Temp",
    Path(os.environ.get("USERPROFILE", "")) / ".cache" / "huggingface",
    Path(os.environ.get("LOCALAPPDATA", "")) / "pip" / "cache",
    Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/thumbnail_test")
]

for p in candidates:
    if p.exists():
        try:
            sz = sum(f.stat().st_size for f in p.rglob("*") if f.is_file()) / (1024 * 1024)
            print(f"{p}: {sz:.2f} MB")
        except Exception as e:
            print(f"{p}: error {e}")
