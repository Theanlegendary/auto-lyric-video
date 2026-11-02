import subprocess
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import cv2

def main():
    clip_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\real_nature_clips\clip_6252550_roof_trees_heavy_rain.mp4"
    audio_path = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\rain_ambience\tin_roof_rain_thunder_60s_loop.wav"
    out_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\videos"
    brain_dir = r"C:\Users\DELL\.gemini\antigravity\brain\fee49f33-6e4e-4c5b-ae69-9c38ad6288a6"
    thumb_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\thumbnail"
    fonts_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\auto_lyric_video\fonts"
    
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(thumb_dir, exist_ok=True)
    
    out_video = os.path.join(out_dir, "real_nature_tin_roof_night_1min_sample.mp4")

    # 1. Video Filter for NIGHT FOCUS:
    # 10s forward + 10s reverse x 3 = 60.0s seamless ping-pong loop
    # Night grading: deep midnight blue, silver glistening raindrops, dark silhouette canopy, vignette
    vf = (
        "[0:v]trim=start=1:duration=10,setpts=PTS-STARTPTS,split=2[fwd1][torev1];"
        "[torev1]reverse,setpts=PTS-STARTPTS[rev1];"
        "[fwd1][rev1]concat=n=2:v=1:a=0,split=3[c1][c2][c3];"
        "[c1][c2][c3]concat=n=3:v=1:a=0[pingpong];"
        "[pingpong]colorchannelmixer=rr=0.38:rg=0.08:rb=0.0:gr=0.05:gg=0.45:gb=0.20:br=0.10:bg=0.25:bb=0.95,"
        "eq=brightness=-0.08:contrast=1.28:saturation=0.82,"
        "vignette=PI/5[night_graded]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", clip_path,
        "-i", audio_path,
        "-filter_complex", vf,
        "-map", "[night_graded]",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "256k",
        "-t", "60.0",
        out_video
    ]

    print("Rendering Night-Focus Real Nature Rain Master Sample...")
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        print("Error:", p.stderr[-500:])
        sys.exit(1)
    print("Success! Created:", out_video, "Size:", os.path.getsize(out_video))

    # 2. Extract a frame and generate NIGHT Thumbnails
    cap = cv2.VideoCapture(out_video)
    cap.set(cv2.CAP_PROP_POS_MSEC, 10000)
    ret, frame = cap.read()
    cap.release()

    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        base = Image.fromarray(frame_rgb)
        W, H = base.size

        # Thumbnail A: 7clouds Style (Edo SZ Brush Font)
        thumb_7c = base.copy()
        edo_font = ImageFont.truetype(os.path.join(fonts_dir, "edosz.ttf"), 170)
        sub_font = ImageFont.truetype(os.path.join(fonts_dir, "Poppins-Bold.ttf"), 52)

        title = "RAIN ON TIN ROOF AT NIGHT"
        sub = "HEAVY RAIN & DEEP THUNDER • DARK SCREEN FOR SLEEP"

        draw_d = ImageDraw.Draw(thumb_7c)
        bbox_t = draw_d.textbbox((0, 0), title, font=edo_font)
        tw, th = bbox_t[2] - bbox_t[0], bbox_t[3] - bbox_t[1]
        bbox_s = draw_d.textbbox((0, 0), sub, font=sub_font)
        sw, sh = bbox_s[2] - bbox_s[0], bbox_s[3] - bbox_s[1]

        gap = 36
        total_h = th + gap + sh
        start_y = (H - total_h) // 2 - 15
        tx = (W - tw) // 2 - bbox_t[0]
        sx = (W - sw) // 2 - bbox_s[0]

        s_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(s_layer)
        sd.text((tx + 8, start_y + 12), title, font=edo_font, fill=(0, 0, 0, 245))
        sd.text((sx + 5, start_y + th + gap + 7), sub, font=sub_font, fill=(0, 0, 0, 220))
        s_layer = s_layer.filter(ImageFilter.GaussianBlur(5))
        thumb_7c = Image.alpha_composite(thumb_7c.convert("RGBA"), s_layer)

        t_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        td = ImageDraw.Draw(t_layer)
        td.text((tx, start_y), title, font=edo_font, fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(10, 15, 25, 180))
        td.text((sx, start_y + th + gap), sub, font=sub_font, fill=(235, 245, 255, 245), stroke_width=1, stroke_fill=(10, 15, 25, 150))
        thumb_7c = Image.alpha_composite(thumb_7c, t_layer).convert("RGB")

        out_7c = os.path.join(brain_dir, "night_rain_thumb_7clouds.jpg")
        thumb_7c.save(out_7c, quality=95)
        thumb_7c.save(os.path.join(thumb_dir, "night_rain_thumb_7clouds.jpg"), quality=95)
        print("Saved Night 7clouds Thumbnail:", out_7c)

        # Thumbnail B: LatinHype Style (Bebas Neue Condensed)
        thumb_lh = base.copy()
        bebas_font = ImageFont.truetype(os.path.join(fonts_dir, "BebasNeue-Regular.ttf"), 185)

        title_lh = "HEAVY RAIN ON TIN ROOF AT NIGHT"
        sub_lh = "DARK SCREEN FOR SLEEP • INSOMNIA RELIEF"

        bbox_tlh = draw_d.textbbox((0, 0), title_lh, font=bebas_font)
        tlw, tlh = bbox_tlh[2] - bbox_tlh[0], bbox_tlh[3] - bbox_tlh[1]
        bbox_slh = draw_d.textbbox((0, 0), sub_lh, font=sub_font)
        slw, slh = bbox_slh[2] - bbox_slh[0], bbox_slh[3] - bbox_slh[1]

        total_hlh = tlh + gap + slh
        start_ylh = (H - total_hlh) // 2 - 15
        tlx = (W - tlw) // 2 - bbox_tlh[0]
        slx = (W - slw) // 2 - bbox_slh[0]

        s_layer2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd2 = ImageDraw.Draw(s_layer2)
        sd2.text((tlx + 7, start_ylh + 9), title_lh, font=bebas_font, fill=(0, 5, 10, 245))
        sd2.text((slx + 5, start_ylh + tlh + gap + 7), sub_lh, font=sub_font, fill=(0, 5, 10, 220))
        s_layer2 = s_layer2.filter(ImageFilter.GaussianBlur(1.5))
        thumb_lh = Image.alpha_composite(thumb_lh.convert("RGBA"), s_layer2)

        t_layer2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        td2 = ImageDraw.Draw(t_layer2)
        td2.text((tlx, start_ylh), title_lh, font=bebas_font, fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(10, 15, 20, 180))
        td2.text((slx, start_ylh + tlh + gap), sub_lh, font=sub_font, fill=(235, 245, 255, 245), stroke_width=1, stroke_fill=(10, 15, 20, 150))
        thumb_lh = Image.alpha_composite(thumb_lh, t_layer2).convert("RGB")

        out_lh = os.path.join(brain_dir, "night_rain_thumb_latinhype.jpg")
        thumb_lh.save(out_lh, quality=95)
        thumb_lh.save(os.path.join(thumb_dir, "night_rain_thumb_latinhype.jpg"), quality=95)
        print("Saved Night LatinHype Thumbnail:", out_lh)

if __name__ == "__main__":
    main()
