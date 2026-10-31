import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

guide = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/Fade_Replay_YouTube_Upload_Guide.txt")
lines = guide.read_text(encoding="utf-8").splitlines()

print("\n".join(lines[-25:]))
