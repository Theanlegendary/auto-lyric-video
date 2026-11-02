import numpy as np
import wave
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

sample_rate = 44100
duration = 60.0 # 1 minute seamless loop
fade_sec = 8.0 # 8-second equal-power crossfade
total_dur = duration + fade_sec
n_total = int(total_dur * sample_rate)
n_loop = int(duration * sample_rate)
n_fade = int(fade_sec * sample_rate)

out_dir = Path(r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience")
out_dir.mkdir(parents=True, exist_ok=True)

def apply_equal_power_loop(audio):
    # audio shape: (2, N)
    main_part = audio[:, :n_loop].copy()
    tail_part = audio[:, n_loop:n_total].copy() # length n_fade
    
    t = np.linspace(0, 1, n_fade)
    fade_in = np.sin(t * np.pi / 2) # equal power fade in
    fade_out = np.cos(t * np.pi / 2) # equal power fade out
    
    # Blend the tail into the beginning
    main_part[:, :n_fade] = main_part[:, :n_fade] * fade_in + tail_part * fade_out
    return main_part

def save_wav(path, audio):
    # audio shape: (2, N), float -1 to 1
    audio = np.clip(audio, -0.98, 0.98)
    int16 = (audio * 32767).astype(np.int16)
    # Interleave stereo
    interleaved = np.empty((int16.shape[1] * 2,), dtype=np.int16)
    interleaved[0::2] = int16[0]
    interleaved[1::2] = int16[1]
    with wave.open(str(path), 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(interleaved.tobytes())
    print(f"Saved: {path.name} ({path.stat().st_size / 1024 / 1024:.2f} MB)")

np.random.seed(42)

# Helper: simple recursive IIR filter (pink / lowpass)
def filter_noise(white, b_coeff, a_coeff):
    # lfilter with pure numpy
    y = np.zeros_like(white)
    y[0] = b_coeff * white[0]
    for i in range(1, len(white)):
        y[i] = b_coeff * white[i] + a_coeff * y[i-1]
    return y

# Fast pink noise generator using Voss-McCartney algorithm
def generate_pink_noise(n_samples):
    n_rows = 16
    array = np.random.randn(n_rows, n_samples // 16 + 1)
    # interpolate
    pink = np.random.randn(n_samples)
    b = [0.049922035, -0.095993537, 0.050612699, -0.004408786]
    a = [1, -2.494956002, 2.017265875, -0.522189400]
    # Simple multi-pole filter for lush rain texture
    s = np.random.randn(n_samples)
    y1 = np.zeros(n_samples)
    y2 = np.zeros(n_samples)
    y3 = np.zeros(n_samples)
    for i in range(1, n_samples):
        y1[i] = 0.997 * y1[i-1] + s[i] * 0.05
        y2[i] = 0.985 * y2[i-1] + s[i] * 0.10
        y3[i] = 0.950 * y3[i-1] + s[i] * 0.25
    return (y1 + y2 + y3) * 0.7

print("Generating 3 distinct 1-minute seamless rain loops...")

# 1. BEDROOM: Soft rain on window glass + distant thunder swells
print("Synthesizing Track A: Cozy Bedroom Rain & Distant Thunder...")
left_rain = generate_pink_noise(n_total) * 0.35
right_rain = generate_pink_noise(n_total) * 0.35

# Droplet pitter-patter on window (random crisp impulses)
droplets_L = np.zeros(n_total)
droplets_R = np.zeros(n_total)
n_drops = int(total_dur * 60) # 60 drops per second
drop_indices = np.random.randint(0, n_total - 200, n_drops)
for idx in drop_indices:
    decay = np.exp(-np.linspace(0, 10, 200)) * np.sin(np.linspace(0, 40, 200))
    vol = np.random.uniform(0.08, 0.22)
    pan = np.random.uniform(0.2, 0.8)
    droplets_L[idx:idx+200] += decay * vol * (1 - pan)
    droplets_R[idx:idx+200] += decay * vol * pan

# Distant rolling thunder (two deep cinematic low rumbles at t=15s and t=45s)
thunder = np.zeros(n_total)
t_vec = np.linspace(0, total_dur, n_total)
# Rumble 1 at 18s
env1 = np.exp(-((t_vec - 18) ** 2) / 8.0)
# Rumble 2 at 46s
env2 = np.exp(-((t_vec - 46) ** 2) / 12.0)
thunder_raw = np.cumsum(np.random.randn(n_total)) * 0.005 # brown noise
thunder = thunder_raw * (env1 * 0.45 + env2 * 0.55)

bedroom_audio = np.vstack([
    left_rain + droplets_L + thunder,
    right_rain + droplets_R + thunder
])
bedroom_looped = apply_equal_power_loop(bedroom_audio)
save_wav(out_dir / "rain_bedroom_loop.wav", bedroom_looped)

# 2. TOKYO CAFE: Smooth steady street rain + warm indoor acoustic tone
print("Synthesizing Track B: Tokyo Coffee Shop Street Rain...")
cafe_L = generate_pink_noise(n_total) * 0.40
cafe_R = generate_pink_noise(n_total) * 0.40

# Soft low-pass smoothing (simulates hearing rain from inside a warm cafe)
smooth_L = np.convolve(cafe_L, np.ones(8)/8, mode='same')
smooth_R = np.convolve(cafe_R, np.ones(8)/8, mode='same')

# Cozy warm ambient drone (very subtle 220Hz / 440Hz warm room tone)
drone = (np.sin(2 * np.pi * 130.81 * t_vec) * 0.02 + np.sin(2 * np.pi * 196.00 * t_vec) * 0.015)
cafe_audio = np.vstack([
    smooth_L + drone,
    smooth_R + drone
])
cafe_looped = apply_equal_power_loop(cafe_audio)
save_wav(out_dir / "rain_coffeeshop_loop.wav", cafe_looped)

# 3. CABIN IN THE WOODS: Rain on tin roof + crackling fireplace embers
print("Synthesizing Track C: Forest Cabin Rain on Roof & Crackling Fireplace...")
roof_L = generate_pink_noise(n_total) * 0.45
roof_R = generate_pink_noise(n_total) * 0.45

# Fireplace crackles and pops (sharp micro-bursts of burning wood embers)
fireplace_L = np.zeros(n_total)
fireplace_R = np.zeros(n_total)
n_pops = int(total_dur * 18) # 18 pops/crackles per second
pop_indices = np.random.randint(0, n_total - 100, n_pops)
for p_idx in pop_indices:
    pop_shape = np.sin(np.linspace(0, 15, 80)) * np.exp(-np.linspace(0, 8, 80))
    vol = np.random.uniform(0.04, 0.28)
    pan = np.random.uniform(0.3, 0.7)
    fireplace_L[p_idx:p_idx+80] += pop_shape * vol * (1 - pan)
    fireplace_R[p_idx:p_idx+80] += pop_shape * vol * pan

# Warm gentle fire roar (low brown noise)
fire_rumble = np.cumsum(np.random.randn(n_total)) * 0.003
fire_rumble = np.convolve(fire_rumble, np.ones(32)/32, mode='same')

cabin_audio = np.vstack([
    roof_L * 0.75 + fireplace_L + fire_rumble * 0.4,
    roof_R * 0.75 + fireplace_R + fire_rumble * 0.4
])
cabin_looped = apply_equal_power_loop(cabin_audio)
save_wav(out_dir / "rain_cabin_loop.wav", cabin_looped)

print("All 3 seamless rain audio loops generated successfully!")
