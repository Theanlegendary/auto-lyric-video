import cv2
import numpy as np
import wave
import sys
import time
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience")
base_dir.mkdir(parents=True, exist_ok=True)

# 1. AUDIO SYNTHESIS: Gentle Light Rain + Distant Mellow Thunder
sample_rate = 44100
duration = 60.0
fade_sec = 8.0
total_dur = duration + fade_sec
n_total = int(total_dur * sample_rate)
n_loop = int(duration * sample_rate)
n_fade = int(fade_sec * sample_rate)

print("Synthesizing Gentle Light Rain + Mellow Thunder Audio...")
np.random.seed(101)

# Gentle pink noise generator
def gen_gentle_pink(n):
    s = np.random.randn(n)
    y1, y2, y3 = np.zeros(n), np.zeros(n), np.zeros(n)
    for i in range(1, n):
        y1[i] = 0.998 * y1[i-1] + s[i] * 0.03
        y2[i] = 0.988 * y2[i-1] + s[i] * 0.06
        y3[i] = 0.940 * y3[i-1] + s[i] * 0.12
    return (y1 + y2 + y3) * 0.4

# Light rain bed (soft, relaxing)
rain_L = gen_gentle_pink(n_total) * 0.28
rain_R = gen_gentle_pink(n_total) * 0.28

# Very delicate droplet sprinkles on leaves/glass (light pitter-patter)
droplets_L = np.zeros(n_total)
droplets_R = np.zeros(n_total)
n_drops = int(total_dur * 40) # light rain: 40 drops/sec
drop_indices = np.random.randint(0, n_total - 150, n_drops)
for idx in drop_indices:
    decay = np.exp(-np.linspace(0, 8, 150)) * np.sin(np.linspace(0, 30, 150))
    vol = np.random.uniform(0.04, 0.14) # gentle volume
    pan = np.random.uniform(0.25, 0.75)
    droplets_L[idx:idx+150] += decay * vol * (1 - pan)
    droplets_R[idx:idx+150] += decay * vol * pan

# Soft, distant rolling thunder (low frequency rumbles at t=18s and t=46s)
t_vec = np.linspace(0, total_dur, n_total)
# Low-frequency envelope
thunder_env1 = np.exp(-((t_vec - 18) ** 2) / 10.0) # 18s rumble
thunder_env2 = np.exp(-((t_vec - 46) ** 2) / 14.0) # 46s rumble

# Deep brown noise for thunder (< 80 Hz)
raw_brown = np.cumsum(np.random.randn(n_total)) * 0.003
# Smooth brown noise for mellow cinematic tone
thunder_smooth = np.convolve(raw_brown, np.ones(64)/64, mode='same')
thunder_audio = thunder_smooth * (thunder_env1 * 0.50 + thunder_env2 * 0.55)

# Mix gentle rain + light droplets + deep soft thunder
audio_stereo = np.vstack([
    rain_L + droplets_L + thunder_audio,
    rain_R + droplets_R + thunder_audio
])

# 8-second equal power seamless loop
main_audio = audio_stereo[:, :n_loop].copy()
tail_audio = audio_stereo[:, n_loop:n_total].copy()
t_fade = np.linspace(0, 1, n_fade)
fade_in = np.sin(t_fade * np.pi / 2)
fade_out = np.cos(t_fade * np.pi / 2)
main_audio[:, :n_fade] = main_audio[:, :n_fade] * fade_in + tail_audio * fade_out

# Save WAV
audio_wav_path = base_dir / "light_rain_forest_thunder_loop.wav"
main_audio = np.clip(main_audio, -0.98, 0.98)
int16 = (main_audio * 32767).astype(np.int16)
interleaved = np.empty((int16.shape[1] * 2,), dtype=np.int16)
interleaved[0::2] = int16[0]
interleaved[1::2] = int16[1]
with wave.open(str(audio_wav_path), 'wb') as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(interleaved.tobytes())
print(f"Generated Audio: {audio_wav_path.name} ({audio_wav_path.stat().st_size / 1024 / 1024:.2f} MB)")
