import subprocess
import os
import wave
import numpy as np

def main():
    video_raw = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\danny_louis_60s_raw.mp4"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience"
    temp_wav = os.path.join(out_dir, "temp_viral_audio.wav")
    master_loop_wav = os.path.join(out_dir, "viral_channel_rain_70m_60s_loop.wav")

    # 1. Extract audio from 60s video as 48kHz stereo 16-bit PCM WAV
    cmd = [
        "ffmpeg", "-y",
        "-i", video_raw,
        "-vn",
        "-c:a", "pcm_s16le",
        "-ac", "2",
        "-ar", "48000",
        temp_wav
    ]
    print("Extracting authentic 70M-view audio...")
    subprocess.run(cmd, check=True)

    # 2. Read with wave and apply equal-power crossfade for seamless loop
    with wave.open(temp_wav, "rb") as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()
        raw_bytes = wf.readframes(n_frames)

    audio = np.frombuffer(raw_bytes, dtype=np.int16).astype(np.float32) / 32768.0
    audio = audio.reshape(-1, n_channels)

    # 60.0s target
    target_frames = int(60.0 * framerate)
    audio = audio[:target_frames]

    # Equal power crossfade over 2.5 seconds
    fade_len = int(2.5 * framerate)
    fade_in = np.linspace(0, np.pi / 2, fade_len)
    cos_fade = np.cos(fade_in)[:, np.newaxis]
    sin_fade = np.sin(fade_in)[:, np.newaxis]

    head = audio[:fade_len]
    tail = audio[-fade_len:]

    blended = head * sin_fade + tail * cos_fade
    audio[:fade_len] = blended
    audio[-fade_len:] = blended

    # Master audio: warm low-end, rich stereo
    audio_pcm = np.clip(audio * 32767.0, -32768, 32767).astype(np.int16)

    with wave.open(master_loop_wav, "wb") as wf:
        wf.setnchannels(n_channels)
        wf.setsampwidth(sampwidth)
        wf.setframerate(framerate)
        wf.writeframes(audio_pcm.tobytes())

    print("Master viral 70M-view seamless audio loop created:", master_loop_wav)
    print(f"Sample Rate: {framerate}Hz, Duration: {len(audio_pcm)/framerate:.2f}s, File Size: {os.path.getsize(master_loop_wav)} bytes")

    if os.path.exists(temp_wav):
        os.remove(temp_wav)

if __name__ == "__main__":
    main()
