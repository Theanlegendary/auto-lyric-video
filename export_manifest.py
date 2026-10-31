#!/usr/bin/env python3
import sys
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))
from lyric_engine import LyricLayoutEngine, parse_lrc, analyze_region_luminance

engine = LyricLayoutEngine()

songs = [
    {
        'id': 'ophelia',
        'folder': 'Taylor_Swift_The_Fate_of_Ophelia',
        'title': 'The Fate of Ophelia',
        'artist': 'Taylor Swift',
        'featured_artist': '',
        'album': 'The Life of a Poet',
        'release_year': '2024',
        'watermark': 'Aesthetic Lyrics',
        'bg': 'stock_anime_bgs/03_anime_rooftop_sunset_skyline.png',
        'bg_blur': 'songs/Taylor_Swift_The_Fate_of_Ophelia/bg_blur.png',
        'recommended_preset': 'indie',
        'opening_start': 0.6,
        'opening_duration': 4.5
    },
    {
        'id': 'apt',
        'folder': 'APT',
        'title': 'APT.',
        'artist': 'ROSÉ',
        'featured_artist': 'Bruno Mars',
        'album': 'rosie',
        'release_year': '2024',
        'watermark': 'Aesthetic Lyrics',
        'bg': 'light_clouds_sharp_1080.png',
        'bg_blur': 'light_clouds_blur_1080.png',
        'recommended_preset': 'indie',
        'opening_start': 0.0,
        'opening_duration': 0.0  # Vocals begin immediately at 0.11s
    },
    {
        'id': 'die_with_a_smile',
        'folder': 'Die_With_A_Smile',
        'title': 'Die With A Smile',
        'artist': 'Lady Gaga & Bruno Mars',
        'featured_artist': '',
        'album': 'Die With A Smile - Single',
        'release_year': '2024',
        'watermark': 'Aesthetic Lyrics',
        'bg': 'stock_anime_bgs/02_lofi_twilight_starry_night.png',
        'bg_blur': 'songs/Die_With_A_Smile/twilight_blur.png',
        'recommended_preset': 'cinematic',
        'opening_start': 0.6,
        'opening_duration': 4.5
    },
    {
        'id': 'golden',
        'folder': 'HUNTR_X_Golden',
        'title': 'Golden',
        'artist': 'HUNTR/X',
        'featured_artist': '',
        'album': 'K-Pop Demon Hunters OST',
        'release_year': '2024',
        'watermark': 'Aesthetic Lyrics',
        'bg': 'stock_anime_bgs/01_makoto_shinkai_clouds.png',
        'bg_blur': 'stock_anime_bgs/01_makoto_shinkai_clouds_blur.png',
        'recommended_preset': 'modern',
        'opening_start': 0.8,
        'opening_duration': 4.8
    },
    {
        'id': 'birds_of_a_feather',
        'folder': 'Billie_Eilish_BIRDS_OF_A_FEATHER',
        'title': 'BIRDS OF A FEATHER',
        'artist': 'Billie Eilish',
        'featured_artist': '',
        'album': 'HIT ME HARD AND SOFT',
        'release_year': '2024',
        'watermark': 'Aesthetic Lyrics',
        'bg': 'stock_anime_bgs/01_makoto_shinkai_clouds.png',
        'bg_blur': 'stock_anime_bgs/01_makoto_shinkai_clouds_blur.png',
        'recommended_preset': 'indie',
        'opening_start': 0.4,
        'opening_duration': 2.8
    }
]

manifest = []
for s in songs:
    fdir = BASE_DIR / 'songs' / s['folder']
    lrc_path = fdir / 'lyrics.lrc'
    audio_path = fdir / 'audio.mp3'
    bg_path = BASE_DIR / s['bg']

    if lrc_path.exists() and audio_path.exists():
        raw_cues = parse_lrc(lrc_path)
        couplets = engine.build_couplets(raw_cues)
        first_vocal = raw_cues[0]['start'] if raw_cues else 0.0

        lum_analysis = analyze_region_luminance(bg_path) if bg_path.exists() else {
            'mean_lum': 60.0,
            'contrast_mode': 'dark_bg',
            'is_mixed': False
        }

        manifest.append({
            'id': s['id'],
            'title': s['title'],
            'artist': s['artist'],
            'featured_artist': s['featured_artist'],
            'album': s['album'],
            'release_year': s['release_year'],
            'watermark': s['watermark'],
            'folder': s['folder'],
            'audio_url': f"songs/{s['folder']}/audio.mp3",
            'bg_sharp': s['bg'],
            'bg_blur': s['bg_blur'],
            'recommended_preset': s['recommended_preset'],
            'first_vocal_start': first_vocal,
            'opening': {
                'enabled': s['opening_duration'] > 0 and first_vocal >= 2.0,
                'start_time': s['opening_start'],
                'duration': s['opening_duration'],
                'force_over_vocal': False
            },
            'luminance_info': lum_analysis,
            'couplets': couplets
        })
        print(f"Processed {s['title']} -> First Vocal: {first_vocal:.2f}s | Contrast: {lum_analysis['contrast_mode'].upper()} (Lum: {lum_analysis['mean_lum']}) | Couplets: {len(couplets)}")

manifest_path = BASE_DIR / 'songs_manifest.json'
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2)

print(f"Exported updated manifest: {manifest_path} ({manifest_path.stat().st_size} bytes)")
