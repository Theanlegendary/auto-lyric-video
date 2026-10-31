import os, glob, datetime

now = datetime.datetime.now()
print("Current time:", now)

files = glob.glob("*.py")
for f in files:
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(f))
    if (now - mtime).total_seconds() < 7200: # last 2 hours
        print(f"{f}: {mtime}")
