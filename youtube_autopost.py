#!/usr/bin/env python3
"""
YouTube Auto-Poster for Aesthetic Lyric Videos
Automates batch uploading of videos, custom thumbnails, titles, descriptions, and tags.
"""

import os
import sys
import json
import glob
import argparse
from typing import List, Dict, Optional

# Force UTF-8 encoding for Windows console output
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEOS_DIR = os.path.join(BASE_DIR, "videos")
THUMB_DIR = os.path.join(VIDEOS_DIR, "thumbnail")
CLIENT_SECRET_FILE = os.path.join(BASE_DIR, "client_secret.json")
TOKEN_FILE = os.path.join(BASE_DIR, "youtube_token.json")
HISTORY_FILE = os.path.join(BASE_DIR, "upload_history.json")

# Required OAuth Scopes for uploading video and setting custom thumbnail
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl"
]

# Catalog metadata for all 11 songs with high-CTR titles, descriptions, and tags
SONG_CATALOG = {
    0: {
        "title": "Justin Bieber - That Should Be Me (Lyrics)",
        "artist": "Justin Bieber",
        "song": "That Should Be Me",
        "video_match": "00_Justin_Bieber_That_Should_Be_Me",
        "tags": ["justin bieber that should be me lyrics", "that should be me lyrics", "justin bieber lyrics", "fade replay", "aesthetic lyric video", "pop lyrics"],
        "description": """🎵 Justin Bieber - That Should Be Me (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

Stream / Download "That Should Be Me":
https://justinbieber.lnk.to/MyWorld2

💬 Top Lyrics:
"That should be me, holdin' your hand
That should be me, makin' you laugh
That should be me, this is so sad
That should be me, that should be me..."

🎨 Visual Style: Spotify Glass Anime Sunset Sky
📝 Synchronized lyrics & design by Fade Replay.

⚠️ Copyright Disclaimer:
Under section 107 of the Copyright Act 1976, allowance is made for 'fair use' for purposes such as criticism, comment, news reporting, teaching, scholarship, and research.
All rights belong to their respective owners. Contact: fadereplay.contact@gmail.com

#ThatShouldBeMe #JustinBieber #Lyrics #FadeReplay #AestheticLyrics"""
    },
    1: {
        "title": "ROSÉ & Bruno Mars - APT. (Lyrics)",
        "artist": "ROSÉ & Bruno Mars",
        "song": "APT.",
        "video_match": "01_ROSE_Bruno_Mars_APT",
        "tags": ["apt lyrics", "rose bruno mars apt", "rose apt lyrics", "bruno mars apt lyrics", "apateu apateu lyrics", "blackpink rose apt", "fade replay", "aesthetic lyrics"],
        "description": """🎵 ROSÉ & Bruno Mars - APT. (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

Stream / Download "APT.":
https://rose.lnk.to/apt

💬 Top Lyrics:
"Apateu, apateu
Apateu, apateu
Apateu, apateu
Uh, uh-huh, uh-huh
Kissy face, kissy face, sent to your phone but
I'm tryna kiss your lips for real..."

🎨 Visual Style: Pastel Aesthetic Sky & Cloud Blur
📝 Synchronized lyrics & design by Fade Replay.

⚠️ Copyright Disclaimer:
Under section 107 of the Copyright Act 1976, allowance is made for 'fair use'.
All rights belong to their respective owners (THEBLACKLABEL / Atlantic Records). Contact: fadereplay.contact@gmail.com

#APT #Rose #BrunoMars #Lyrics #FadeReplay #Blackpink #Apateu"""
    },
    2: {
        "title": "Lady Gaga & Bruno Mars - Die With A Smile (Lyrics)",
        "artist": "Lady Gaga & Bruno Mars",
        "song": "Die With A Smile",
        "video_match": "02_Lady_Gaga_Bruno_Mars_Die_With_A_Smile",
        "tags": ["die with a smile lyrics", "lady gaga bruno mars die with a smile", "if the world was ending lyrics", "lady gaga lyrics", "bruno mars lyrics", "fade replay", "sad song lyrics"],
        "description": """🎵 Lady Gaga & Bruno Mars - Die With A Smile (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

Stream / Download "Die With A Smile":
https://ladygaga.lnk.to/DieWithASmile

💬 Top Lyrics:
"If the world was ending, I’d wanna be next to you
If the party was over and our time on Earth was through
I’d wanna hold you just for a while and die with a smile..."

🎨 Visual Style: Soft Twilight Starry Sky & Velvet Blur
📝 Synchronized lyrics & design by Fade Replay.

⚠️ Copyright Disclaimer:
Under section 107 of the Copyright Act 1976, allowance is made for 'fair use'.
All rights belong to Interscope / Atlantic Records. Contact: fadereplay.contact@gmail.com

#DieWithASmile #LadyGaga #BrunoMars #Lyrics #FadeReplay #SadSongs"""
    },
    3: {
        "title": "Taylor Swift - The Fate of Ophelia (Lyrics)",
        "artist": "Taylor Swift",
        "song": "The Fate of Ophelia",
        "video_match": "03_Taylor_Swift_The_Fate_of_Ophelia",
        "tags": ["taylor swift the fate of ophelia", "the fate of ophelia lyrics", "taylor swift lyrics", "ttpd lyrics", "fade replay", "aesthetic lyrics"],
        "description": """🎵 Taylor Swift - The Fate of Ophelia (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

Stream Taylor Swift:
https://taylorswift.lnk.to

💬 Top Lyrics:
"Drowning in the melancholy waves of what could have been..."

🎨 Visual Style: Shinjuku Twilight Rooftop Sunset
📝 Synchronized lyrics & design by Fade Replay.

⚠️ Copyright Disclaimer:
Under section 107 of the Copyright Act 1976, allowance is made for 'fair use'. Contact: fadereplay.contact@gmail.com

#TaylorSwift #TheFateOfOphelia #Lyrics #FadeReplay #Swifties"""
    },
    4: {
        "title": "HUNTR/X - Golden (Lyrics)",
        "artist": "HUNTR/X",
        "song": "Golden",
        "video_match": "04_HUNTR_X_Golden",
        "tags": ["huntrx golden lyrics", "golden lyrics", "kpop lyrics", "fade replay", "aesthetic lyric video"],
        "description": """🎵 HUNTR/X - Golden (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

💬 Top Lyrics:
"We shine like gold in the pouring rain..."

🎨 Visual Style: Neo-Tokyo Neon Rain Reflection
📝 Synchronized lyrics & design by Fade Replay.

#Golden #HUNTRX #Lyrics #FadeReplay"""
    },
    5: {
        "title": "Billie Eilish - BIRDS OF A FEATHER (Lyrics)",
        "artist": "Billie Eilish",
        "song": "BIRDS OF A FEATHER",
        "video_match": "05_Billie_Eilish_BIRDS_OF_A_FEATHER",
        "tags": ["birds of a feather lyrics", "billie eilish birds of a feather", "i want you to stay till im in the grave lyrics", "billie eilish lyrics", "fade replay"],
        "description": """🎵 Billie Eilish - BIRDS OF A FEATHER (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

Stream Billie Eilish:
https://billieeilish.lnk.to/HITMEHARDANDSOFT

💬 Top Lyrics:
"I want you to stay 'til I'm in the grave
'Til I'm rot, rot in pieces, dead and buried
'Til I'm in the casket you carry..."

🎨 Visual Style: Nostalgic Countryside Train Window & Clouds
📝 Synchronized lyrics & design by Fade Replay.

#BirdsOfAFeather #BillieEilish #Lyrics #FadeReplay"""
    },
    6: {
        "title": "Sabrina Carpenter - Espresso (Lyrics)",
        "artist": "Sabrina Carpenter",
        "song": "Espresso",
        "video_match": "06_Sabrina_Carpenter_Espresso",
        "tags": ["espresso lyrics", "sabrina carpenter espresso", "thats that me espresso lyrics", "sabrina carpenter lyrics", "fade replay"],
        "description": """🎵 Sabrina Carpenter - Espresso (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

Stream Sabrina Carpenter - Espresso:
https://sabrinacarpenter.lnk.to/Espresso

💬 Top Lyrics:
"Now he's thinkin' 'bout me every night, oh
Is it that sweet? I guess so
Say you can't sleep, baby, I know
That's that me, espresso..."

🎨 Visual Style: Italian Riviera Cafe & Coastal Waves
📝 Synchronized lyrics & design by Fade Replay.

#Espresso #SabrinaCarpenter #Lyrics #FadeReplay"""
    },
    7: {
        "title": "Benson Boone - Beautiful Things (Lyrics)",
        "artist": "Benson Boone",
        "song": "Beautiful Things",
        "video_match": "07_Benson_Boone_Beautiful_Things",
        "tags": ["beautiful things lyrics", "benson boone beautiful things", "please stay i want you i need you lyrics", "benson boone lyrics", "fade replay"],
        "description": """🎵 Benson Boone - Beautiful Things (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

Stream Benson Boone - Beautiful Things:
https://bensonboone.lnk.to/BeautifulThings

💬 Top Lyrics:
"Please stay, I want you, I need you, oh God
Don't take these beautiful things that I've got..."

🎨 Visual Style: Mountain Sunrise Sunbeams & Foggy Valley
📝 Synchronized lyrics & design by Fade Replay.

#BeautifulThings #BensonBoone #Lyrics #FadeReplay"""
    },
    8: {
        "title": "Chappell Roan - Good Luck, Babe! (Lyrics)",
        "artist": "Chappell Roan",
        "song": "Good Luck, Babe!",
        "video_match": "08_Chappell_Roan_Good_Luck_Babe",
        "tags": ["good luck babe lyrics", "chappell roan good luck babe", "youd have to stop the world just to stop the feeling lyrics", "chappell roan lyrics", "fade replay"],
        "description": """🎵 Chappell Roan - Good Luck, Babe! (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

Stream Chappell Roan - Good Luck, Babe!:
https://chappellroan.lnk.to/GoodLuckBabe

💬 Top Lyrics:
"You'd have to stop the world just to stop the feeling
Good luck, babe!
You're gonna have to find a way to live with yourself..."

🎨 Visual Style: Retro Synth Sunset & Palm Highway
📝 Synchronized lyrics & design by Fade Replay.

#GoodLuckBabe #ChappellRoan #Lyrics #FadeReplay"""
    },
    9: {
        "title": "Teddy Swims - Lose Control (Lyrics)",
        "artist": "Teddy Swims",
        "song": "Lose Control",
        "video_match": "09_Teddy_Swims_Lose_Control",
        "tags": ["lose control lyrics", "teddy swims lose control", "i lose control lyrics", "teddy swims lyrics", "fade replay"],
        "description": """🎵 Teddy Swims - Lose Control (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

Stream Teddy Swims - Lose Control:
https://teddyswims.lnk.to/LoseControl

💬 Top Lyrics:
"Something's got a hold of me lately
No, I don't know myself anymore
Feels like the walls are all closing in
And the devil's knocking at my door..."

🎨 Visual Style: Misty Forest Path & Morning Twilight
📝 Synchronized lyrics & design by Fade Replay.

#LoseControl #TeddySwims #Lyrics #FadeReplay"""
    },
    10: {
        "title": "Ruth B. - Dandelions (Lyrics)",
        "artist": "Ruth B.",
        "song": "Dandelions",
        "video_match": "10_Ruth_B_Dandelions",
        "tags": ["dandelions lyrics", "ruth b dandelions", "cause im in a field of dandelions lyrics", "ruth b lyrics", "fade replay"],
        "description": """🎵 Ruth B. - Dandelions (Lyrics)
🔔 Subscribe to Fade Replay for daily aesthetic lyric videos: https://www.youtube.com/@FadeReplay

Stream Ruth B. - Dandelions:
https://ruthb.lnk.to/Dandelions

💬 Top Lyrics:
"'Cause I'm in a field of dandelions
Wishing on every one that you'd be mine, mine..."

🎨 Visual Style: Dreamy Sunset Meadow & Fireflies
📝 Synchronized lyrics & design by Fade Replay.

#Dandelions #RuthB #Lyrics #FadeReplay"""
    }
}


def load_history() -> Dict:
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_history(history: Dict):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def get_available_items() -> List[Dict]:
    """Finds all video files and matches them with their metadata and thumbnails."""
    items = []
    video_files = sorted(glob.glob(os.path.join(VIDEOS_DIR, "*.mp4")))
    
    for vf in video_files:
        basename = os.path.basename(vf)
        matched_idx = None
        for idx, meta in SONG_CATALOG.items():
            if meta["video_match"].lower() in basename.lower():
                matched_idx = idx
                break
        
        meta = SONG_CATALOG.get(matched_idx, {
            "title": os.path.splitext(basename)[0],
            "artist": "Unknown Artist",
            "song": os.path.splitext(basename)[0],
            "tags": ["lyrics", "music"],
            "description": f"🎵 {os.path.splitext(basename)[0]}"
        })
        
        # Locate corresponding thumbnail
        name_no_ext = os.path.splitext(basename)[0]
        thumb_candidates = [
            os.path.join(THUMB_DIR, f"{name_no_ext}_title_thumbnail.png"),
            os.path.join(THUMB_DIR, f"{name_no_ext}.png"),
            os.path.join(BASE_DIR, "thumbnail", f"{name_no_ext}_title_thumbnail.png"),
        ]
        thumb_path = None
        for tc in thumb_candidates:
            if os.path.exists(tc):
                thumb_path = tc
                break
        
        items.append({
            "index": matched_idx if matched_idx is not None else 999,
            "filename": basename,
            "video_path": vf,
            "thumb_path": thumb_path,
            "title": meta["title"],
            "artist": meta["artist"],
            "song": meta["song"],
            "description": meta["description"],
            "tags": meta["tags"]
        })
    
    items.sort(key=lambda x: x["index"])
    return items


def print_setup_instructions():
    print("""
================================================================================
           YOUTUBE OAUTH SETUP INSTRUCTIONS (ONE-TIME ONLY)
================================================================================
To enable automated direct uploads to your YouTube channel, you need a Google
OAuth Client ID:

1. Open Google Cloud Console:
   👉 https://console.cloud.google.com/apis/dashboard

2. Create a new project (or select an existing one), e.g. "LyricVideoChannel".

3. Go to "APIs & Services" > "Library" > Search for "YouTube Data API v3" > Click "ENABLE".

4. Go to "APIs & Services" > "OAuth consent screen":
   - Select "External" > Click "Create"
   - App Name: "Lyric Video Poster"
   - Enter your email for support and developer contact.
   - Click "Save and Continue".
   - Under "Test Users", click "Add Users" and add your own YouTube/Google email address!

5. Go to "APIs & Services" > "Credentials":
   - Click "+ CREATE CREDENTIALS" > Select "OAuth client ID"
   - Application type: "Desktop app"
   - Name: "YouTube Desktop Uploader"
   - Click "Create"
   - Click the "DOWNLOAD JSON" button!

6. Rename that downloaded JSON file to:
   client_secret.json
   and place it in this folder:
   C:\\Users\\DELL\\.gemini\\antigravity\\scratch\\auto_lyric_video\\client_secret.json

Once done, simply run:
   python youtube_autopost.py --upload-all --privacy private
================================================================================
""")


def get_authenticated_service():
    """Authenticates using Google OAuth 2.0 flow and returns YouTube API service."""
    if not os.path.exists(CLIENT_SECRET_FILE):
        print("\n[ERROR] client_secret.json not found!")
        print_setup_instructions()
        sys.exit(1)
        
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build

    creds = None
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except Exception as e:
            print(f"[WARN] Error reading cached credentials: {e}")
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("[INFO] Refreshing expired access token...")
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"[WARN] Refresh token failed: {e}. Starting fresh login...")
                creds = None
                
        if not creds:
            print("[INFO] Starting OAuth 2.0 web authentication in your browser...")
            print("[INFO] A browser window will open. Sign in with the Google account managing your YouTube channel.")
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
            
        with open(TOKEN_FILE, "w", encoding="utf-8") as token_out:
            token_out.write(creds.to_json())
            print(f"[OK] Authentication credentials successfully saved to: {TOKEN_FILE}")

    return build("youtube", "v3", credentials=creds)


def upload_video(youtube, item: Dict, privacy_status: str = "private") -> Optional[str]:
    """Uploads a single video and custom thumbnail to YouTube."""
    from googleapiclient.http import MediaFileUpload
    import googleapiclient.errors

    video_path = item["video_path"]
    thumb_path = item.get("thumb_path")
    title = item["title"][:100]  # YouTube title limit 100 chars
    description = item["description"]
    tags = item["tags"]

    print(f"\n=======================================================")
    print(f"Uploading Video: {os.path.basename(video_path)}")
    print(f"Title:   {title}")
    print(f"Privacy: {privacy_status.upper()}")
    print(f"Thumbnail: {os.path.basename(thumb_path) if thumb_path else 'None'}")
    print(f"=======================================================")

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "10",  # Category 10 = Music
            "defaultLanguage": "en",
            "defaultAudioLanguage": "en"
        },
        "status": {
            "privacyStatus": privacy_status,
            "selfDeclaredMadeForKids": False
        }
    }

    # Resumable upload for reliable video delivery
    media_body = MediaFileUpload(video_path, chunksize=1024 * 1024 * 10, resumable=True)

    try:
        insert_request = youtube.videos().insert(
            part="snippet,status",
            body=body,
            media_body=media_body
        )

        response = None
        print("[1/2] Uploading video data in chunks...")
        while response is None:
            status, response = insert_request.next_chunk()
            if status:
                progress = int(status.progress() * 100)
                print(f"   Progress: {progress}%", end="\r", flush=True)

        video_id = response.get("id")
        video_url = f"https://youtu.be/{video_id}"
        print(f"\n[OK] Video successfully uploaded!")
        print(f"     YouTube ID:  {video_id}")
        print(f"     YouTube URL: {video_url}")

        # Set custom thumbnail if available
        if thumb_path and os.path.exists(thumb_path):
            print("[2/2] Uploading custom 1080p title thumbnail...")
            try:
                thumb_media = MediaFileUpload(thumb_path, mimetype="image/png")
                youtube.thumbnails().set(
                    videoId=video_id,
                    media_body=thumb_media
                ).execute()
                print(f"[OK] Custom thumbnail set successfully!")
            except Exception as te:
                print(f"[WARN] Thumbnail upload failed: {te}")
                print("       (Note: Custom thumbnails require account phone verification in YouTube Studio)")
        else:
            print("[2/2] No custom thumbnail found, skipping.")

        # Update local history
        history = load_history()
        history[item["filename"]] = {
            "video_id": video_id,
            "url": video_url,
            "title": title,
            "uploaded_at": str(os.path.getmtime(video_path)),
            "privacy": privacy_status
        }
        save_history(history)

        return video_id

    except googleapiclient.errors.HttpError as e:
        print(f"\n[FAIL] YouTube API error: {e}")
        return None
    except Exception as e:
        print(f"\n[FAIL] Unexpected error during upload: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="YouTube Auto-Poster for Aesthetic Lyric Videos")
    parser.add_argument("--list", action="store_true", help="List all detected videos and upload status")
    parser.add_argument("--upload-all", action="store_true", help="Batch upload all videos in queue")
    parser.add_argument("--upload-index", type=int, help="Upload a specific video by its index (0-10)")
    parser.add_argument("--privacy", choices=["private", "unlisted", "public"], default="private", help="Video privacy level (default: private)")
    parser.add_argument("--setup-guide", action="store_true", help="Show Google Cloud OAuth credential setup guide")

    args = parser.parse_args()

    if args.setup_guide:
        print_setup_instructions()
        return

    items = get_available_items()

    if args.list or (not args.upload_all and args.upload_index is None):
        history = load_history()
        print("\n==========================================================================================")
        print("                  DETECTED LYRIC VIDEOS & THUMBNAILS QUEUE")
        print("==========================================================================================")
        for it in items:
            fname = it["filename"]
            status_str = f"UPLOADED (https://youtu.be/{history[fname]['video_id']})" if fname in history else "READY TO POST"
            thumb_str = "YES (1080p)" if it["thumb_path"] else "MISSING"
            print(f"[{it['index']:02d}] {it['title']}")
            print(f"     Video:     {fname}")
            print(f"     Thumbnail: {thumb_str}")
            print(f"     Status:    {status_str}")
            print("------------------------------------------------------------------------------------------")
        
        print("\nCommands:")
        print("  python youtube_autopost.py --upload-all --privacy private")
        print("  python youtube_autopost.py --upload-index 2 --privacy private")
        print("  python youtube_autopost.py --setup-guide")
        return

    # User requested upload
    youtube = get_authenticated_service()

    if args.upload_index is not None:
        target = next((it for it in items if it["index"] == args.upload_index), None)
        if not target:
            print(f"[ERROR] No video found matching index {args.upload_index}")
            return
        upload_video(youtube, target, args.privacy)
    elif args.upload_all:
        print(f"[INFO] Starting batch upload for {len(items)} videos with privacy='{args.privacy}'...")
        history = load_history()
        for idx, it in enumerate(items, 1):
            fname = it["filename"]
            if fname in history:
                print(f"\n[SKIP] [{idx}/{len(items)}] {fname} is already uploaded (ID: {history[fname]['video_id']})")
                continue
            upload_video(youtube, it, args.privacy)
            print(f"[DONE] Completed {idx}/{len(items)}")

    print("\n[FINISHED] All operations completed.")


if __name__ == "__main__":
    main()
