import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

player_path = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\player.html")
content = player_path.read_text(encoding='utf-8')

# Update showcase card in player.html
new_desc = """☁️ <strong>yung kai — blue (7clouds Perfect Twilight Remaster • 3:34)</strong><br>• <strong>Visual</strong>: Signature 7clouds twilight anime aesthetic — deep sapphire & indigo clouds with soft moonlight rim glow and twinkling stars (`bg_34`).<br>• <strong>Motion</strong>: Subtle organic camera drift (zoompan) — zero clunky sliding sprites.<br>• <strong>Typography</strong>: Pure white handwriting font (`Patrick Hand`) with dark outline & soft shadow for maximum emotional contrast.<br>• <strong>Audio</strong>: Original 1.0x Full Mix."""

import re
content = re.sub(
    r"☁️ <strong>yung kai — blue \(7clouds Clean Aesthetic Remaster.*?Audio</strong>: Original 1\.0x Full Mix\.",
    new_desc,
    content,
    flags=re.DOTALL
)

player_path.write_text(content, encoding='utf-8')
print("Updated player.html with Perfect Twilight description.")
