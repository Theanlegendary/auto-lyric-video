import os
import sys
from fontTools.ttLib import TTFont

sys.stdout.reconfigure(encoding='utf-8')
p = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts\Ultra-Regular.ttf"
font = TTFont(p)
cmap = font.getBestCmap()

test_chars = ['★', '•', '✦', '✧', '~', '-', '♥', '♡', '♪', '♫']
for ch in test_chars:
    codepoint = ord(ch)
    present = codepoint in cmap
    print(f"Char '{ch}' (0x{codepoint:04X}): {'YES' if present else 'NO'}")
