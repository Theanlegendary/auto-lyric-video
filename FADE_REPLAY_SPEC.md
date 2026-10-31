# Fade Replay — Technical Engineering Specification

This document provides exact technical parameters, mathematical formulas, and filter complex syntax used in the **Fade Replay** pipeline.

---

## 1. Substation Alpha (.ass) Style Specifications

### Style: 7clouds Standard Couplet
```ini
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Title7Clouds,Patrick Hand,170,&H00FFFFFF,&H000000FF,&H00101828,&H80000000,-1,0,0,0,100,100,5,0,1,4.0,2.5,5,180,180,110,1
Style: Lyric7Clouds,Patrick Hand,96,&H00FFFFFF,&H000000FF,&H00101828,&H80000000,-1,0,0,0,100,100,2,0,1,3.8,2.2,5,180,180,110,1
```

- **`PrimaryColour`**: `&H00FFFFFF` (Alpha 00, Blue FF, Green FF, Red FF = Pure Opaque White).
- **`OutlineColour`**: `&H00101828` (Deep navy/charcoal outline for crisp readability over bright clouds).
- **`BackColour`**: `&H80000000` (50% transparent soft drop shadow).
- **`Outline`**: `3.8` px width.
- **`Shadow`**: `2.2` px offset.
- **`Alignment`**: `5` (Top-center anchored to `\pos(960, 490)`).

### Dialogue Event Syntax
- **Title Hook Card**:
  ```ass
  Dialogue: 0,0:00:00.60,0:00:06.50,Title7Clouds,,0,0,0,,{\pos(960,460)\fad(500,400)}Song Title\N{\fs84\fsp6\b0}Artist Name
  ```
- **Couplet Subtitle**:
  ```ass
  Dialogue: 0,0:00:06.80,0:00:12.80,Lyric7Clouds,,0,0,0,,{\pos(960,490)\fad(200,150)}Line One of Couplet\NLine Two of Couplet
  ```

---

## 2. FFmpeg Video Pipeline

### Filter Complex
```
[0:v]format=yuv420p,
zoompan=z='min(zoom+0.00008,1.04)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,
fade=t=in:st=0:d=1.5,
subtitles=lyrics.ass:fontsdir=fonts,
noise=alls=4:allf=t+u,
fade=t=out:st=1295.38:d=3.5[v]
```

### Video Codec Flags
- **Codec**: `libx264`
- **Pixel Format**: `yuv420p`
- **Color Primaries**: `bt709`
- **Preset**: `fast` (single track) / `veryfast` (20-min loop)
- **CRF**: `18` (single track) / `21` (20-min loop)
- **GOP Size**: `-g 50 -keyint_min 25` (keyframe every 2 seconds for smooth scrubbing)
- **Flags**: `+faststart` (moves moov atom to beginning of file for instant web playback)

---

## 3. Audio Looping & Varispeed Formulas

### Extended 5-Time Replay Loop
To loop the track 6 times total:
```bash
ffmpeg -loop 1 -t <TOTAL_DURATION> -i wallpaper.png \
       -stream_loop 5 -i audio.mp3 \
       -t <TOTAL_DURATION> \
       -filter_complex "<fc>" \
       -af "afade=t=in:ss=0:d=1.5,afade=t=out:st=<T_OUT>:d=3.5" \
       -c:v libx264 -c:a aac -b:a 256k output_20min_loop.mp4
```

### Slowed + Reverb Varispeed
- **Speed Factor**: $R = 0.865$
- **Tempo Shift**: $85 \text{ BPM} \to 73.5 \text{ BPM}$
- **Pitch Shift**: $\approx -2.5 \text{ semitones}$
- **Filter**: `asetrate=44100*0.865,aresample=44100,aecho=0.8:0.88:60:0.4`
- **Timestamp Scaling**: $\text{start}' = \text{start} / 0.865$, $\text{end}' = \text{end} / 0.865$

---

## 4. Verification Contrast Calculation

```python
# Luminance calculation (Rec. 601)
lum = 0.299 * R + 0.587 * G + 0.114 * B
peak_lum = np.percentile(lum, 99.5)      # Top text core pixels
outline_lum = np.percentile(lum, 1.0)    # Dark border pixels
contrast_ratio = (peak_lum + 0.05) / (outline_lum + 0.05)

# Standard target: contrast_ratio >= 10.0:1
```
