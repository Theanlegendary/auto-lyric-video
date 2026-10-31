import sys, os, time
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

temp_dir = Path(os.environ.get("LOCALAPPDATA", "")) / "Temp"
now = time.time()
freed = 0

for item in temp_dir.iterdir():
    try:
        if item.is_file():
            # Delete if older than 10 minutes
            if now - item.stat().st_mtime > 600:
                sz = item.stat().st_size
                item.unlink(missing_ok=True)
                freed += sz
        elif item.is_dir():
            # Only remove if not system locked
            pass
    except Exception:
        pass

print(f"Freed {freed / (1024*1024):.2f} MB from Temp.")
