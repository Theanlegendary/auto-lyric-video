import sys
from pathlib import Path
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding='utf-8')

song_dir = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/songs/27_Joji_Glimpse_of_Us")
audio_path = song_dir / "audio.mp3"
words_path = song_dir / "whisper_words.txt"

print("Loading Whisper model (tiny.en or base.en for fast, accurate word alignment)...")
model = WhisperModel("base.en", device="cpu", compute_type="int8")

print("Transcribing with word timestamps...")
segments, info = model.transcribe(str(audio_path), word_timestamps=True, language="en")

with open(words_path, "w", encoding="utf-8") as f:
    for seg in segments:
        f.write(f"[{seg.start:.2f} -> {seg.end:.2f}] {seg.text}\n")
        for w in seg.words:
            f.write(f"   {w.start:6.2f} - {w.end:6.2f}: {w.word}\n")

print(f"Saved {words_path.name} ({words_path.stat().st_size} bytes)")
