import os, glob

for f in glob.glob("*.py"):
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
            if "compare_sweater_2" in c or "audio_sweater_weather_slowed_reverb" in c:
                print(f"Match in: {f}")
    except Exception as e:
        pass
