import sys, json

sys.stdout.reconfigure(encoding='utf-8')

transcript_path = "C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get("step_index") in [5045, 5046, 5047, 5048, 5049, 5050]:
            print(f"Step {data.get('step_index')}:")
            tool_calls = data.get("tool_calls", [])
            for tc in tool_calls:
                print("  Tool call:", tc.get("tool_name"))
                args = tc.get("arguments", {})
                for k, v in args.items():
                    print(f"    {k}: {str(v)[:200]}")
