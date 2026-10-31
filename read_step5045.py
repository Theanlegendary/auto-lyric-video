import sys, json

sys.stdout.reconfigure(encoding='utf-8')

transcript_path = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get("step_index") == 5045:
            print("Tool calls in 5045:")
            for tc in data.get("tool_calls", []):
                print(tc['name'])
                print(tc.get('args', {}).get('Path'))
                print(tc.get('args', {}).get('Content'))
            break
