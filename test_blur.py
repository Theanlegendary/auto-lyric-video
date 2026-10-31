import subprocess

bg = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/clean_bg_1080.png'
out_test = 'C:/Users/DELL/.gemini/antigravity/scratch/auto_lyric_video/test/blur_transition_test.mp4'

# Create blurred background with gblur and blend using time T
filter_complex = (
    '[0:v]split[sharp][preblur];'
    '[preblur]gblur=sigma=30[blurred];'
    '[sharp][blurred]blend=all_expr=\'if(lte(T,3),A,if(between(T,3,5.5),A*(1-(T-3)/2.5)+B*(T-3)/2.5,B))\''
)

cmd = [
    'ffmpeg', '-y',
    '-loop', '1', '-framerate', '30', '-t', '10', '-i', bg,
    '-filter_complex', filter_complex,
    '-c:v', 'libx264', '-preset', 'veryfast', '-pix_fmt', 'yuv420p',
    out_test
]

p = subprocess.run(cmd, capture_output=True, text=True)
print('FFmpeg returncode:', p.returncode)
if p.returncode != 0:
    print('Error:', p.stderr[-500:])
else:
    print('Rendered blur transition test successfully!')
