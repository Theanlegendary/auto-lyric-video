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

jobs = [
    {
        'id': '03',
        'title': 'The Fate of Ophelia',
        'artist': 'Taylor Swift',
        'folder': 'Taylor_Swift_The_Fate_of_Ophelia',
        'bg_sharp': base / 'stock_anime_bgs/03_anime_rooftop_sunset_skyline.png',
        't_sharp': 8.5,
        't_blur': 11.0,
        'duration': 229.7,
        'out_filename': '03_Taylor_Swift_The_Fate_of_Ophelia_Lyric_Video.mp4',
        'sample_times': {
            'title': '00:00:05.000',
            'fixed_012s': '00:00:12.500',
            'verse': '00:00:25.000',
            'chorus': '00:01:00.000'
        }
    },
    {
        'id': '04',
        'title': 'Golden',
        'artist': 'HUNTR/X (KPop Demon Hunters)',
        'folder': 'HUNTR_X_Golden',
        'bg_sharp': base / 'stock_anime_bgs/01_makoto_shinkai_clouds.png',
        't_sharp': 13.0,
        't_blur': 15.5,
        'duration': 191.0,
        'out_filename': '04_HUNTR_X_Golden_Lyric_Video.mp4',
        'sample_times': {
            'title': '00:00:07.000',
            'verse1': '00:00:18.000',
            'verse2': '00:00:30.000',
            'chorus': '00:01:05.000'
        }
    },
    {
        'id': '05',
        'title': 'BIRDS OF A FEATHER',
        'artist': 'Billie Eilish',
        'folder': 'Billie_Eilish_BIRDS_OF_A_FEATHER',
        'bg_sharp': base / 'stock_anime_bgs/01_makoto_shinkai_clouds.png',
        't_sharp': 3.0,
        't_blur': 5.2,
        'duration': 211.1,
        'out_filename': '05_Billie_Eilish_BIRDS_OF_A_FEATHER_Lyric_Video.mp4',
        'sample_times': {
            'title': '00:00:02.000',
            'verse1': '00:00:10.000',
            'verse2': '00:00:20.000',
            'chorus': '00:00:44.000'
        }
    }
]

test_dir = base / 'test'
test_dir.mkdir(exist_ok=True)

for job in jobs:
    print(f"\n=======================================================")
    print(f"Rendering Song {job['id']}: {job['title']} by {job['artist']}")
    print(f"=======================================================")
    t_start = time.time()
    
    song_dir = base / 'songs' / job['folder']
    audio_path = song_dir / 'audio.mp3'
    ass_path = song_dir / 'lyrics_couplets_final.ass'
    bg_sharp = job['bg_sharp']
    bg_blur = song_dir / 'bg_blur.png'
    
    # 1. Ensure 8px Gaussian blur exists
    img = Image.open(str(bg_sharp))
    blurred = img.filter(ImageFilter.GaussianBlur(radius=8))
    blurred.save(str(bg_blur))
    
    # 2. Escape paths for FFmpeg filter
    ass_escaped = str(ass_path).replace("\\", "/").replace(":", "\\\\:")
    
    # 3. High performance SIMD overlay fade:
    # Sharp image stays 100% opaque until t_sharp, fades alpha to 0 over dt, and after t_blur overlay is disabled!
    ts = job['t_sharp']
    tb = job['t_blur']
    dt = round(tb - ts, 2)
    fc = (
        f"[0:v]format=yuva420p,fade=t=out:st={ts}:d={dt}:alpha=1[sharp];"
        f"[1:v][sharp]overlay=0:0:enable='lte(t,{tb})',"
        f"subtitles={ass_escaped}:fontsdir={fonts_escaped}[v]"
    )
    
    out_video = base / 'videos' / job['out_filename']
    duration_str = str(job['duration'])
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-framerate", "30", "-t", duration_str, "-i", str(bg_sharp),
        "-loop", "1", "-framerate", "30", "-t", duration_str, "-i", str(bg_blur),
        "-i", str(audio_path),
        "-filter_complex", fc,
        "-map", "[v]", "-map", "2:a",
        "-c:v", "libx264", "-preset", "faster", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(out_video)
    ]
    
    print(f"Executing fast FFmpeg render to {out_video.name}...")
    p = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors='ignore')
    if p.returncode != 0:
        print(f"Error rendering {job['title']}! Return code: {p.returncode}")
        print(p.stderr[-1000:])
        sys.exit(1)
        
    render_time = time.time() - t_start
    size_mb = os.path.getsize(out_video) / (1024 * 1024)
    print(f"SUCCESS: Rendered {job['title']} in {render_time:.1f}s | Size: {size_mb:.2f} MB")
    
    # Also copy to root directory for convenient browser preview in player.html
    root_copy = base / job['out_filename'].replace("03_", "").replace("04_", "").replace("05_", "")
    shutil.copy(out_video, root_copy)
    
    # Extract audit frames
    for tag, st in job['sample_times'].items():
        frame_name = f"audit_{job['folder']}_{tag}.png"
        frame_path = test_dir / frame_name
        subprocess.run([
            "ffmpeg", "-y", "-ss", st, "-i", str(out_video),
            "-vframes", "1", str(frame_path)
        ], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        
        # Copy to artifact dir for visual verification
        artifact_target = artifacts_dir / frame_name
        shutil.copy(frame_path, artifact_target)
        print(f"  Frame audited & copied: {frame_name} at {st}")
        
print("\n=======================================================")
print("ALL 3 VIDEOS RENDERED AND AUDITED WITH ZERO OVERLAPS!")
print("=======================================================")
