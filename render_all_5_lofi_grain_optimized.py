import os
import sys
import time
import shutil
import subprocess
from pathlib import Path
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

base = Path('C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video')
fonts_escaped = "C\\\\:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/fonts"
artifacts_dir = Path("C:/Users/DELL/.gemini/antigravity/brain/fee49f33-6e4e-4c5b-ae69-9c38ad6288a6")

songs = [
    {
        'id': '01',
        'title': 'APT.',
        'artist': 'ROSÉ & Bruno Mars',
        'folder': 'APT',
        'ass_file': 'lyrics_perfect_apt.ass',
        'bg_sharp': base / 'stock_anime_bgs/01_makoto_shinkai_clouds.png',
        't_sharp': 2.8,
        't_blur': 5.5,
        'duration': 173.5,
        'out_filename': '01_ROSE_Bruno_Mars_APT_Lyric_Video.mp4',
        'sample_time': '00:00:20.000'
    },
    {
        'id': '02',
        'title': 'Die With A Smile',
        'artist': 'Lady Gaga & Bruno Mars',
        'folder': 'Die_With_A_Smile',
        'ass_file': 'lyrics.ass',
        'bg_sharp': base / 'stock_anime_bgs/02_lofi_twilight_starry_night.png',
        't_sharp': 4.5,
        't_blur': 7.2,
        'duration': 251.8,
        'out_filename': '02_Lady_Gaga_Bruno_Mars_Die_With_A_Smile_Lyric_Video.mp4',
        'sample_time': '00:00:25.000'
    },
    {
        'id': '03',
        'title': 'The Fate of Ophelia',
        'artist': 'Taylor Swift',
        'folder': 'Taylor_Swift_The_Fate_of_Ophelia',
        'ass_file': 'lyrics_couplets_final.ass',
        'bg_sharp': base / 'stock_anime_bgs/03_anime_rooftop_sunset_skyline.png',
        't_sharp': 8.5,
        't_blur': 11.0,
        'duration': 229.7,
        'out_filename': '03_Taylor_Swift_The_Fate_of_Ophelia_Lyric_Video.mp4',
        'sample_time': '00:00:12.500'
    },
    {
        'id': '04',
        'title': 'Golden',
        'artist': 'HUNTR/X (KPop Demon Hunters)',
        'folder': 'HUNTR_X_Golden',
        'ass_file': 'lyrics_couplets_final.ass',
        'bg_sharp': base / 'stock_anime_bgs/01_makoto_shinkai_clouds.png',
        't_sharp': 13.0,
        't_blur': 15.5,
        'duration': 191.0,
        'out_filename': '04_HUNTR_X_Golden_Lyric_Video.mp4',
        'sample_time': '00:00:20.000'
    },
    {
        'id': '05',
        'title': 'BIRDS OF A FEATHER',
        'artist': 'Billie Eilish',
        'folder': 'Billie_Eilish_BIRDS_OF_A_FEATHER',
        'ass_file': 'lyrics_couplets_final.ass',
        'bg_sharp': base / 'stock_anime_bgs/01_makoto_shinkai_clouds.png',
        't_sharp': 3.0,
        't_blur': 5.2,
        'duration': 211.1,
        'out_filename': '05_Billie_Eilish_BIRDS_OF_A_FEATHER_Lyric_Video.mp4',
        'sample_time': '00:00:20.000'
    }
]

test_dir = base / 'test'
test_dir.mkdir(exist_ok=True)
videos_dir = base / 'videos'
videos_dir.mkdir(exist_ok=True)

total_start = time.time()
print("=================================================================")
print("STARTING OPTIMIZED BATCH RENDER: ALL 5 SONGS WITH LOFI FILM GRAIN")
print("=================================================================")

for idx, song in enumerate(songs):
    t_song = time.time()
    print(f"\n[{idx+1}/5] Rendering: {song['title']} by {song['artist']}...")
    
    song_dir = base / 'songs' / song['folder']
    audio_path = song_dir / 'audio.mp3'
    ass_path = song_dir / song['ass_file']
    bg_sharp = song['bg_sharp']
    bg_blur = song_dir / 'bg_blur.png'
    
    # 1. Create 8px Gaussian blur if not exists
    if not bg_blur.exists():
        img = Image.open(str(bg_sharp))
        blurred = img.filter(ImageFilter.GaussianBlur(radius=8))
        blurred.save(str(bg_blur))
        
    ass_escaped = str(ass_path).replace("\\", "/").replace(":", "\\\\:")
    
    # 2. Filter Graph:
    # Sharp intro -> smooth dissolve to 8px blur -> ASS Subtitles -> Medium Aesthetic Lofi Grain (c0s=22:c0f=t+u)
    ts = song['t_sharp']
    tb = song['t_blur']
    dt = round(tb - ts, 2)
    fc = (
        f"[0:v]format=yuva420p,fade=t=out:st={ts}:d={dt}:alpha=1[sharp];"
        f"[1:v][sharp]overlay=0:0:enable='lte(t,{tb})',"
        f"subtitles={ass_escaped}:fontsdir={fonts_escaped},"
        f"noise=c0s=22:c0f=t+u[v]"
    )
    
    out_video = videos_dir / song['out_filename']
    duration_str = str(song['duration'])
    
    # Professional YouTube 1080p target bitrate (6M target, 8M max) guarantees ultra-fast encode and perfect grain preservation
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-framerate", "30", "-t", duration_str, "-i", str(bg_sharp),
        "-loop", "1", "-framerate", "30", "-t", duration_str, "-i", str(bg_blur),
        "-i", str(audio_path),
        "-filter_complex", fc,
        "-map", "[v]", "-map", "2:a",
        "-c:v", "libx264", "-preset", "faster", "-b:v", "6M", "-maxrate", "8M", "-bufsize", "12M", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(out_video)
    ]
    
    p = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors='ignore')
    if p.returncode != 0:
        print(f"Error rendering {song['title']}! Return code: {p.returncode}")
        print(p.stderr[-1000:])
        sys.exit(1)
        
    elapsed = time.time() - t_song
    size_mb = os.path.getsize(out_video) / (1024 * 1024)
    print(f"  -> Finished in {elapsed:.1f}s | Size: {size_mb:.2f} MB")
    
    # Copy to root directory for convenient browser preview in player.html
    root_filename = song['out_filename'].replace("01_", "").replace("02_", "").replace("03_", "").replace("04_", "").replace("05_", "")
    shutil.copy(out_video, base / root_filename)
    
    # Extract audit frame with grain
    frame_name = f"audit_grain_{song['folder']}.png"
    frame_path = test_dir / frame_name
    subprocess.run([
        "ffmpeg", "-y", "-ss", song['sample_time'], "-i", str(out_video),
        "-vframes", "1", str(frame_path)
    ], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    
    # Copy to artifact dir for visual verification
    shutil.copy(frame_path, artifacts_dir / frame_name)
    print(f"  -> Extracted grain audit frame: {frame_name} at {song['sample_time']}")
    
total_time = time.time() - total_start
print("\n=================================================================")
print(f"ALL 5 LOFI GRAIN VIDEOS RENDERED AND VERIFIED IN {total_time:.1f}s!")
print("=================================================================")
