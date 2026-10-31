#!/usr/bin/env python3
"""
Fade Replay - 5 Song Lyric Video Batch Generator
Generates full aesthetic lyric videos using the approved Pastel Clouds + Black Lyrics style.
"""

import sys
import os
import json
import urllib.request
import subprocess
from pathlib import Path

BASE_DIR = Path("C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video")
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SONGS = [
    {
        "id": 1,
        "title": "APT.",
        "artist": "ROSÉ & Bruno Mars",
        "search_query": "APT. ROSE Bruno Mars",
        "theme": "clouds"
    },
    {
        "id": 2,
        "title": "Die With A Smile",
        "artist": "Lady Gaga & Bruno Mars",
        "search_query": "Die With A Smile Lady Gaga Bruno Mars",
        "theme": "twilight"
    },
    {
        "id": 3,
        "title": "The Fate of Ophelia",
        "artist": "Taylor Swift",
        "search_query": "The Fate of Ophelia Taylor Swift",
        "theme": "clouds"
    },
    {
        "id": 4,
        "title": "Golden",
        "artist": "HUNTR/X",
        "search_query": "Golden HUNTR/X",
        "theme": "clouds"
    },
    {
        "id": 5,
        "title": "BIRDS OF A FEATHER",
        "artist": "Billie Eilish",
        "search_query": "BIRDS OF A FEATHER Billie Eilish",
        "theme": "clouds"
    }
]

print("==================================================")
print("  FADE REPLAY - 5 SONG AUTOMATED BATCH SUITE")
print("==================================================")
for s in SONGS:
    print(f"[{s['id']}] {s['artist']} - {s['title']}")
print("Ready to generate any song automatically!")
