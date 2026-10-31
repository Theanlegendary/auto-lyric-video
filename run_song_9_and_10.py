import sys
import time
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
sys.path.insert(0, str(base))

from auto_producer import produce_song

print("Starting render for Song 9 (Teddy Swims - Lose Control)...")
t0 = time.time()
res9 = produce_song(9, "Lose Control", "Teddy Swims", preferred_vibe="rain")
print(f"Song 9 complete in {time.time()-t0:.1f}s! Size: {res9['size_mb']:.1f} MB")

print("\nStarting render for Song 10 (Ruth B. - Dandelions)...")
t1 = time.time()
res10 = produce_song(10, "Dandelions", "Ruth B.", preferred_vibe="sakura")
print(f"Song 10 complete in {time.time()-t1:.1f}s! Size: {res10['size_mb']:.1f} MB")
