import sys, shutil, os
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

temp_dir = Path(os.environ.get("LOCALAPPDATA", "")) / "Temp"
patterns = ["GitHub Copilot-*-updater-*", "Diagnostics", "c-typo-*", "c-resp-*", "chrome-test-*", "metro-cache", "github-app-browser-previews"]

freed = 0
for pat in patterns:
    for p in temp_dir.glob(pat):
        try:
            sz = sum(f.stat().st_size for f in p.rglob("*") if f.is_file())
            shutil.rmtree(p, ignore_errors=True)
            freed += sz
            print(f"Removed {p.name}")
        except Exception:
            pass

print(f"Freed {freed / (1024*1024):.2f} MB")
