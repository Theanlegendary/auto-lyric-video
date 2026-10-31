import subprocess
from pathlib import Path

base = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
song_dir = base / "songs" / "27_Adele_Skyfall"
src_audio = song_dir / "audio_original.mp3"

# -------------------------------------------------------------------
# FORMULA 1: Classic Golden Slowed + Reverb (0.865x Tape Varispeed)
# Speed: 0.865x (drops tempo from ~76 BPM to ~65.7 BPM, pitch down ~2.5 semitones)
# Reverb: Multi-tap stereo hall diffusion with low-end mud filtering (highpass 220Hz on reverb)
# Warmth: Gentle high-frequency softening (14.5kHz) for cassette/vinyl comfort
# -------------------------------------------------------------------

out_audio = song_dir / "audio_skyfall_slowed_reverb.mp3"

# FFmpeg filtergraph:
# 1. Resample varispeed: asetrate=44100*0.865,aresample=44100
# 2. Split into dry and wet paths:
#    dry: volume=0.82
#    wet: highpass=f=220,lowpass=f=9000,aecho=0.8:0.75:60|120|240|360|540:0.45|0.38|0.30|0.22|0.15,volume=0.35
# 3. Mix back together with amix
# 4. Final mastering: lowpass=f=15500, equalizer=f=160:t=q:w=1.2:g=1.5, volume=1.15

af = (
    "asetrate=44100*0.865,aresample=44100,"
    "asplit=2[dry][wet_in];"
    "[wet_in]highpass=f=200,lowpass=f=8500,"
    "aecho=0.85:0.78:55|110|220|350|520|750:0.45|0.38|0.30|0.22|0.15|0.08,"
    "volume=0.40[wet];"
    "[dry][wet]amix=inputs=2:weights=1.0 0.55:dropout_transition=0,"
    "lowpass=f=15500,"
    "equalizer=f=150:t=q:w=1.0:g=1.5,"
    "alimiter=limit=0.95"
)

cmd = [
    "ffmpeg", "-y",
    "-i", str(src_audio),
    "-filter_complex", af,
    "-c:a", "libmp3lame",
    "-b:a", "320k",
    str(out_audio)
]

print("Rendering Adele - Skyfall (Slowed + Reverb)...")
res = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
print("Process return code:", res.returncode)

if res.returncode == 0:
    print(f"Generated Slowed + Reverb Audio: {out_audio.name} ({out_audio.stat().st_size / (1024*1024):.2f} MB)")
else:
    print("Error:", res.stderr)
