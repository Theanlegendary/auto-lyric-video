import os
import sys
import subprocess
import time
from pathlib import Path
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
brain = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")
raw_jpg = brain / "lonely_anime_night_sky_1793068246650.jpg"
stock_dir = base / "stock_anime_bgs"
song_dir = base / "songs" / "15_Akon_Lonely"
out_video = base / "videos" / "15_Akon_Lonely_Lyric_Video.mp4"
audio_path = song_dir / "audio_7clouds.mp3"
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"

# 1. Convert to 1920x1080 PNG if not exists
sharp_png = stock_dir / "20_lonely_starry_night_sunset_vibe.png"
if not sharp_png.exists():
    im = Image.open(raw_jpg).convert("RGB").resize((1920, 1080), Image.Resampling.LANCZOS)
    im.save(sharp_png, "PNG")
    print(f"Saved 20_lonely_starry_night_sunset_vibe.png: {sharp_png}")
else:
    im = Image.open(sharp_png).convert("RGB")

# 2. Master background: gentle dreamy blur (radius=10)
master_bg = song_dir / "starry_vibe_blurred_master.png"
if not master_bg.exists():
    im_blur = im.filter(ImageFilter.GaussianBlur(radius=10))
    scrim = Image.new("RGB", (1920, 1080), (10, 8, 18))
    bg_final = Image.blend(im_blur, scrim, 0.05)
    bg_final.save(master_bg, "PNG")
    print(f"Saved master background: {master_bg}")
else:
    print(f"Master background exists: {master_bg}")

# 3. 50/50 balanced Spotify ASS file:
ass_path = song_dir / "lyrics_spotify_rdr_orange.ass"
ass_escaped = ass_path.as_posix().replace(":", "\\\\:")

print("Rendering full master video for Akon - Lonely (20% Sunset / 80% Starry Night Vibe)...")
duration = 235.13
t_out = round(duration - 3.0, 2)

fc = (
    f"[0:v]format=yuv420p,"
    f"zoompan=z='min(zoom+0.00010,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,"
    f"fade=t=in:st=0:d=1.5,"
    f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
    f"noise=alls=5:allf=t+u,"
    f"fade=t=out:st={t_out}:d=3.0[v]"
)

af = f"afade=t=in:ss=0:d=1.8,afade=t=out:st={t_out}:d=3.0"

cmd_full = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", str(duration), "-i", str(master_bg),
    "-i", str(audio_path),
    "-filter_complex", fc,
    "-map", "[v]",
    "-map", "1:a",
    "-af", af,
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "18",
    "-c:a", "aac",
    "-b:a", "320k",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    str(out_video)
]

start_t = time.time()
res = subprocess.run(cmd_full, capture_output=True, text=True, errors='ignore')
elapsed = time.time() - start_t

if res.returncode == 0:
    size_mb = out_video.stat().st_size / (1024 * 1024)
    print(f"SUCCESS! Rendered master video {out_video.name} in {elapsed:.1f}s ({size_mb:.2f} MB)")
    
    # 4. Extract audit frames directly from final video
    preview_frames = [
        ("00:00:05", "audit_starry_vibe_title.png"),
        ("00:00:15", "audit_starry_vibe_intro_hook.png"),
        ("00:00:28", "audit_starry_vibe_spoken.png"),
        ("00:00:46", "audit_starry_vibe_verse1.png"),
        ("00:01:09", "audit_starry_vibe_chorus.png"),
        ("00:03:41", "audit_starry_vibe_outro.png"),
    ]
    
    for ss, fname in preview_frames:
        out_p = brain / fname
        cmd_f = [
            "ffmpeg", "-y",
            "-ss", ss,
            "-i", str(out_video),
            "-vframes", "1",
            str(out_p)
        ]
        subprocess.run(cmd_f, check=True)
        print(f"Rendered audit frame from video: {fname}")
else:
    print(f"FAILED with returncode {res.returncode}")
    print("\n".join(res.stderr.splitlines()[-30:]))
