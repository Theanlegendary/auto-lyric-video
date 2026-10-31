import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Current couplets from earlier:
# Let's inspect each line's length and balance them 50/50 in sentence case!

couplets_data = [
    # (start, end, type, text)
    (1.00, 9.50, "TITLE", "Lonely\nAkon"),
    (10.13, 20.20, "HOOK", "Lonely, I'm Mr. Lonely\nI have nobody for my own"),
    (20.74, 23.80, "HOOK", "I am so lonely\nI'm Mr. Lonely"),
    # Spoken Intro - let's balance 50/50!
    (24.38, 32.00, "SPOKEN", "Yo, this one here goes out\nTo all my players out there, you know"),
    (32.49, 38.20, "SPOKEN", "That got that one good girl\nWho's always been there, took all the bullshit"),
    (38.75, 42.50, "SPOKEN", "Then one day she can't take it no more\nAnd decide to leave, yeah"),
    # Verse 1 - balance 50/50
    (42.99, 47.80, "VERSE", "I woke up in the middle of the night\nAnd I noticed my girl wasn't by my side"),
    (48.21, 53.10, "VERSE", "Coulda sworn I was dreaming, for her I was feenin'\nSo I had to get up and take a little ride"),
    (53.55, 58.50, "VERSE", "Backtracking over these few years\nTryna figure out what I did to make it go bad"),
    (58.92, 63.80, "VERSE", "'Cause ever since my girl left me\nMy whole life came crashing and I'm so"),
    # Chorus 1 - balance 50/50
    (64.18, 68.50, "CHORUS", "Lonely (So lonely)\nI'm Mr. Lonely (Mr. Lonely)"),
    (68.88, 74.10, "CHORUS", "I have nobody (I have nobody)\nFor my own (To call my own, girl)"),
    (74.54, 79.20, "CHORUS", "I'm so lonely (So lonely)\nI'm Mr. Lonely (Mr. Lonely)"),
    (79.59, 85.20, "CHORUS", "I have nobody (I have nobody)\nFor my own (To call my own, girl)"),
    # Verse 2 - balance 50/50
    (85.64, 90.50, "VERSE", "Can't believe I had a girl like you\nAnd I just let you walk right outta my life"),
    (90.93, 95.80, "VERSE", "After all I put you through\nYou still stuck around and stayed by my side"),
    (96.25, 101.00, "VERSE", "What really hurt me is I broke your heart\nBaby, you a good girl and I had no right"),
    (101.46, 106.40, "VERSE", "I really wanna make things right\n'Cause without you in my life, girl, I'm so"),
    # Chorus 2 - balance 50/50
    (106.89, 111.00, "CHORUS", "Lonely (So lonely)\nI'm Mr. Lonely (Mr. Lonely)"),
    (111.38, 116.80, "CHORUS", "I have nobody (I have nobody)\nFor my own (To call my own, girl)"),
    (117.22, 121.60, "CHORUS", "I'm so lonely (So lonely)\nI'm Mr. Lonely (Mr. Lonely)"),
    (122.07, 127.90, "CHORUS", "I have nobody (I have nobody)\nFor my own (To call my own, baby)"),
    # Verse 3 - balance 50/50
    (128.44, 133.10, "VERSE", "Been all about the world, ain't never met a girl\nThat could take the things that you been through"),
    (133.51, 138.50, "VERSE", "Never thought the day would come where you would run\nAnd I would be out chasing you"),
    (138.99, 143.70, "VERSE", "'Cause ain't nowhere in the globe I'd rather be\nAin't no one in the globe I'd rather see"),
    (144.15, 149.10, "VERSE", "Than the girl of my dreams that made me be\nSo happy, but now so lonely"),
    # Chorus 3 - balance 50/50
    (149.54, 153.80, "CHORUS", "Lonely (So lonely)\nI'm Mr. Lonely (Mr. Lonely)"),
    (154.28, 159.50, "CHORUS", "I have nobody (I have nobody)\nFor my own (To call my own, no)"),
    (159.99, 164.20, "CHORUS", "I'm so lonely (So lonely)\nI'm Mr. Lonely (Mr. Lonely)"),
    (164.58, 169.80, "CHORUS", "I have nobody (I have nobody)\nFor my own (To call my own, girl)"),
    # Bridge - balance 50/50
    (170.36, 175.90, "BRIDGE", "Never thought that I'd be alone\nNever thought that I'd be all on my own"),
    (176.42, 181.20, "BRIDGE", "I didn't think you'd be gone this long\nI just want you to call my phone"),
    (181.63, 186.40, "BRIDGE", "Stop playing, girl, and come on home\nBaby girl, I didn't mean to shout"),
    (186.84, 191.40, "BRIDGE", "I want me and you to work it out\nI'd never wish to ever hurt my baby"),
    (191.90, 196.20, "CHORUS", "And it's driving me crazy 'cause I'm so\nLonely (So lonely)"),
    (196.72, 201.90, "CHORUS", "I'm Mr. Lonely (Mr. Lonely)\nI have nobody (I have nobody)"),
    (202.39, 206.90, "CHORUS", "For my own (To call my own, no)\nI'm so lonely (So lonely)"),
    (207.47, 212.30, "CHORUS", "I'm Mr. Lonely (Mr. Lonely)\nI have nobody (I have nobody)"),
    (212.80, 218.30, "CHORUS", "For my own (To call my own, girl)\nI am so lonely"),
    # Outro - balance 50/50
    (218.76, 224.30, "OUTRO", "So lonely (Lonely)\nSo lonely (So lonely)"),
    (224.78, 229.60, "OUTRO", "Mr. Lonely (Lonely)\nSo lonely (So lonely)"),
    (230.09, 234.50, "OUTRO", "So lonely (Lonely)\nSo lonely, Mr. Lonely"),
]

print("Checking 50/50 length ratio for each couplet:")
for i, (st, en, ctype, text) in enumerate(couplets_data):
    lines = text.split("\n")
    if len(lines) == 2:
        l1, l2 = len(lines[0]), len(lines[1])
        ratio = min(l1, l2) / max(l1, l2)
        print(f"#{i+1:02d} [{ctype}]: L1={l1} chars | L2={l2} chars (Balance: {ratio:.0%})")
        if ratio < 0.35:
            print(f"  WARNING: Unbalanced: {lines[0]} vs {lines[1]}")
