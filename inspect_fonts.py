import os
import sys

fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
sys.stdout.reconfigure(encoding='utf-8')

try:
    from fontTools.ttLib import TTFont
    for f in sorted(os.listdir(fonts_dir)):
        if f.endswith('.ttf') or f.endswith('.otf'):
            try:
                font = TTFont(os.path.join(fonts_dir, f))
                family = ''
                full_name = ''
                for record in font['name'].names:
                    if record.nameID == 1 and not family:
                        try:
                            family = record.toUnicode()
                        except:
                            pass
                    if record.nameID == 4 and not full_name:
                        try:
                            full_name = record.toUnicode()
                        except:
                            pass
                print(f"{f} -> Family: '{family}' | Full: '{full_name}'")
            except Exception as e:
                print(f"{f} -> Error: {e}")
except ImportError:
    print("fontTools not installed, listing files:")
    for f in sorted(os.listdir(fonts_dir)):
        print(f)
