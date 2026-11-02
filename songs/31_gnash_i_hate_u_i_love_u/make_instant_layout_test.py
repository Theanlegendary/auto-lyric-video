from PIL import Image, ImageDraw, ImageFont

bg_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\songs\31_gnash_i_hate_u_i_love_u\bg_clear_sky_sea_blue.png"
font_edo = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts\edosz.ttf"
font_sans = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts\Poppins-SemiBold.ttf"

base = Image.open(bg_path).convert("RGBA")
overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Top header title card that coexists with instant lyrics
f_track = ImageFont.truetype(font_edo, 42)
f_artist = ImageFont.truetype(font_sans, 22)

# Shadow & text for top title
for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2), (0, 3)]:
    draw.text((960 + dx, 120 + dy), "i hate u, i love u", font=f_track, fill=(10, 20, 35, 180), anchor="mm")
    draw.text((960 + dx, 162 + dy), "gnash ft. olivia o'brien", font=f_artist, fill=(10, 20, 35, 180), anchor="mm")

draw.text((960, 120), "i hate u, i love u", font=f_track, fill=(255, 255, 255, 240), anchor="mm")
draw.text((960, 162), "gnash ft. olivia o'brien", font=f_artist, fill=(255, 255, 255, 210), anchor="mm")

# Lyrics at 53%
f_lyric = ImageFont.truetype(font_edo, 60)
for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (0, 4)]:
    draw.text((960 + dx, 572 + dy), "Feeling used, but I'm\nStill missing you", font=f_lyric, fill=(10, 20, 35, 180), anchor="mm", align="center")
draw.text((960, 572), "Feeling used, but I'm\nStill missing you", font=f_lyric, fill=(255, 255, 255, 255), anchor="mm", align="center")

out = Image.alpha_composite(base, overlay).convert("RGB")
out.save(r"C:\Users\DELL\.gemini\antigravity\brain\d46be2a3-51af-4b7e-8ca8-fe1d429e1056\concept_instant_start_layout.png")
print("Saved concept_instant_start_layout.png!")
