import sys

sys.stdout.reconfigure(encoding='utf-8')

for mod in ["whisper", "syncedlyrics", "faster_whisper"]:
    try:
        __import__(mod)
        print(f"Module {mod} is AVAILABLE")
    except ImportError:
        print(f"Module {mod} is NOT installed")
