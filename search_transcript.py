import sys, json

sys.stdout.reconfigure(encoding='utf-8')

transcript_path = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/.system_generated/logs/transcript.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        content = data.get("content", "")
        if "audio_sweater_weather_slowed_reverb" in content or "compare_sweater_2" in content:
            step = data.get("step_index")
            print(f"Step {step}:")
            print(content[:300])
            print("="*40)
