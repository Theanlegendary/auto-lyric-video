import sys, os
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

temp_dir = Path(os.environ.get("LOCALAPPDATA", "")) / "Temp"
subdirs = []

for item in temp_dir.iterdir():
    try:
        if item.is_dir():
            sz = sum(f.stat().st_size for f in item.rglob("*") if f.is_file()) / (1024 * 1024)
            if sz > 20:
                subdirs.append((item, sz))
    except Exception:
        pass

for p, sz in sorted(subdirs, key=lambda x: x[1], reverse=True)[:10]:
    print(f"{p.name}: {sz:.2f} MB")
