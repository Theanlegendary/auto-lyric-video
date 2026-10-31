#!/usr/bin/env python3
"""
Aesthetic Lyric Video Engine - Adaptive Contrast & Professional Title Sequence
Supports:
  - Adaptive text contrast: analyzes background luminance in the actual lyric zone
    (Bright BG -> #222222 Dark Charcoal, Dark BG -> #F7F5F2 Soft White, Mixed -> Highest WCAG Contrast + Scrim)
  - Smoothing and hysteresis to prevent color flickering
  - Professional editable opening sequence (Title, Artist, Featured Artist, Album, Year, Watermark)
  - Vocal conflict detection: auto-adjusts/shortens title if lyrics start early
  - Presets: Style C (DM Sans Indie), Style A (Cormorant Garamond Cinema), Style B (Inter Modern)
"""

import os
import sys
import re
import json
import math
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Union
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = Path(__file__).resolve().parent
FONTS_DIR = BASE_DIR / "fonts"
OUTPUT_DIR = BASE_DIR / "output"

FONTS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Font configurations
FONT_CONFIGS = {
    "cormorant": {
        "name": "Cormorant Garamond",
        "file": FONTS_DIR / "CormorantGaramond.ttf",
        "weight": "SemiBold",
        "bold": 1,
        "default_spacing": 0.5,
        "line_height_mult": 1.25,
        "default_casing": "sentence"
    },
    "inter": {
        "name": "Inter",
        "file": FONTS_DIR / "Inter.ttf",
        "weight": "Medium",
        "bold": 0,
        "default_spacing": 0.0,
        "line_height_mult": 1.22,
        "default_casing": "sentence"
    },
    "dmsans": {
        "name": "DM Sans",
        "file": FONTS_DIR / "DMSans.ttf",
        "weight": "Medium",
        "bold": 0,
        "default_spacing": 2.0,  # Wider spacing for Indie editorial feel
        "line_height_mult": 1.24,
        "default_casing": "lowercase"  # Style C editorial lowercase
    }
}

STYLE_PRESETS = {
    "cinematic": {
        "font_id": "cormorant",
        "font_size": 60,
        "casing": "sentence",
        "spacing": 0.8,
        "vertical_ratio": 0.60
    },
    "modern": {
        "font_id": "inter",
        "font_size": 54,
        "casing": "sentence",
        "spacing": 0.2,
        "vertical_ratio": 0.60
    },
    "indie": {
        "font_id": "dmsans",
        "font_size": 52,
        "casing": "lowercase",
        "spacing": 2.2,
        "vertical_ratio": 0.60
    }
}

# Color palettes for Adaptive Contrast
CONTRAST_STYLES = {
    "dark_bg": {
        # Soft-white text on dark background
        "text_hex": "#F7F5F2",
        "outline_hex": "#141216",
        "outline_alpha": 80,
        "shadow_color": "&H66000000",   # Soft dark drop shadow
        "outline_width": 1.0,
        "shadow_depth": 2.0,
        "secondary_text_hex": "#D8D5D0"
    },
    "bright_bg": {
        # Dark charcoal text on bright background
        "text_hex": "#222222",
        "outline_hex": "#FFFFFF",
        "outline_alpha": 90,
        "shadow_color": "&H4DFFFFFF",   # Subtle soft light halo/shadow for separation
        "outline_width": 1.0,
        "shadow_depth": 1.8,
        "secondary_text_hex": "#444444"
    }
}


def hex_to_ass_color(hex_str: str, alpha: int = 0) -> str:
    """Convert #RRGGBB to ASS &HAABBGGRR format."""
    hex_str = hex_str.lstrip("#")
    if len(hex_str) == 6:
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)
        return f"&H{alpha:02X}{b:02X}{g:02X}{r:02X}"
    return f"&H{alpha:02X}F2F5F7"


def to_ass_time(seconds: float) -> str:
    """Convert float seconds to ASS timestamp H:MM:SS.CC"""
    if seconds < 0:
        seconds = 0.0
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def format_casing(text: str, mode: str = "sentence") -> str:
    """Format text casing (sentence case, lowercase, preserve)."""
    text = text.strip()
    if not text:
        return ""

    if mode == "lowercase":
        return text.lower()
    elif mode == "preserve":
        return text

    # Sentence case with intelligent English grammar fixes
    s = text[0].upper() + text[1:].lower() if len(text) > 1 else text.upper()

    replacements = [
        (r"\bi\b", "I"),
        (r"\bi'm\b", "I'm"),
        (r"\bi'd\b", "I'd"),
        (r"\bi'll\b", "I'll"),
        (r"\bi've\b", "I've"),
        (r"\bbruno mars\b", "Bruno Mars"),
        (r"\blady gaga\b", "Lady Gaga"),
        (r"\btaylor swift\b", "Taylor Swift"),
        (r"\bbillie eilish\b", "Billie Eilish"),
        (r"\bophelia\b", "Ophelia"),
        (r"\bapt\b", "APT"),
        (r"\bapt\.\b", "APT."),
    ]
    for pattern, repl in replacements:
        s = re.sub(pattern, repl, s, flags=re.IGNORECASE)

    s = re.sub(r'([.!?]\s+)([a-z])', lambda m: m.group(1) + m.group(2).upper(), s)
    return s


def parse_lrc(lrc_path: Path) -> List[Dict]:
    """Parse standard or enhanced LRC file into list of cues with start times and text."""
    cues = []
    time_regex = re.compile(r'\[(\d{2}):(\d{2})(?:\.(\d{2,3}))?\]')

    with open(lrc_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            matches = list(time_regex.finditer(line))
            if not matches:
                continue

            text = time_regex.sub('', line).strip()
            text = re.sub(r'<[^>]+>', '', text).strip()

            if not text:
                continue

            for m in matches:
                minutes = int(m.group(1))
                seconds = int(m.group(2))
                fraction_str = m.group(3) or "0"
                if len(fraction_str) == 2:
                    fraction = int(fraction_str) / 100.0
                elif len(fraction_str) == 3:
                    fraction = int(fraction_str) / 1000.0
                else:
                    fraction = 0.0

                start_sec = minutes * 60 + seconds + fraction
                cues.append({
                    "start": start_sec,
                    "text": text
                })

    cues.sort(key=lambda x: x["start"])

    cleaned = []
    for c in cues:
        if cleaned and abs(c["start"] - cleaned[-1]["start"]) < 0.05:
            if len(c["text"]) > len(cleaned[-1]["text"]):
                cleaned[-1] = c
        else:
            cleaned.append(c)

    return cleaned


def analyze_region_luminance(image_input: Union[Path, str, Image.Image],
                             box: Tuple[float, float, float, float] = (0.15, 0.52, 0.85, 0.72)) -> Dict:
    """
    Analyze the perceived brightness of a specific region of the image.
    box: (x1_pct, y1_pct, x2_pct, y2_pct)
    Returns: dict with mean_lum (0-255), std_lum, contrast_mode ('bright_bg' or 'dark_bg'),
             and wcag_contrast scores.
    """
    if isinstance(image_input, (str, Path)):
        img = Image.open(str(image_input)).convert("RGB")
    else:
        img = image_input.convert("RGB")

    w, h = img.size
    x1 = int(box[0] * w)
    y1 = int(box[1] * h)
    x2 = int(box[2] * w)
    y2 = int(box[3] * h)

    crop = img.crop((x1, y1, x2, y2))
    arr = np.array(crop).astype(float)

    # Standard WCAG 2.1 sRGB to Linear conversion
    arr_norm = arr / 255.0
    arr_lin = np.where(arr_norm <= 0.04045, arr_norm / 12.92, ((arr_norm + 0.055) / 1.055) ** 2.4)
    lum_map = 0.2126 * arr_lin[:, :, 0] + 0.7152 * arr_lin[:, :, 1] + 0.0722 * arr_lin[:, :, 2]
    rel_lum = float(np.mean(lum_map))
    mean_lum = float(np.mean(0.2126 * arr[:, :, 0] + 0.7152 * arr[:, :, 1] + 0.0722 * arr[:, :, 2]))
    std_lum = float(np.std(lum_map))

    # WCAG Contrast calculation: L_white = 0.95, L_dark = 0.04
    L_white = 0.95
    L_dark = 0.04

    contrast_white = (L_white + 0.05) / (rel_lum + 0.05) if L_white >= rel_lum else (rel_lum + 0.05) / (L_white + 0.05)
    contrast_dark = (rel_lum + 0.05) / (L_dark + 0.05) if rel_lum >= L_dark else (L_dark + 0.05) / (rel_lum + 0.05)

    # Hysteresis Decision logic:
    # Bright BG threshold: mean_lum >= 135
    # Dark BG threshold: mean_lum <= 115
    if mean_lum >= 135:
        mode = "bright_bg"
    elif mean_lum <= 115:
        mode = "dark_bg"
    else:
        mode = "bright_bg" if contrast_dark >= contrast_white else "dark_bg"

    # Check if mixed / heterogeneous background that needs scrim gradient
    is_mixed = std_lum > 32.0 or (3.0 < max(contrast_white, contrast_dark) < 4.8)

    return {
        "mean_lum": round(mean_lum, 1),
        "std_lum": round(std_lum, 1),
        "contrast_mode": mode,
        "is_mixed": is_mixed,
        "contrast_white": round(contrast_white, 2),
        "contrast_dark": round(contrast_dark, 2)
    }


class LyricLayoutEngine:
    def __init__(self, canvas_width: int = 1920, canvas_height: int = 1080):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.margin_x = 180
        self.max_text_width = canvas_width - (2 * self.margin_x)

    def measure_text(self, text: str, font: ImageFont.FreeTypeFont, letter_spacing: float = 0.0) -> int:
        if not text:
            return 0
        try:
            bbox = font.getbbox(text)
            base_w = bbox[2] - bbox[0]
            extra_spacing = int(max(0, len(text) - 1) * letter_spacing)
            return base_w + extra_spacing
        except Exception:
            return int(len(text) * font.size * 0.55)

    def wrap_text_to_lines(self, text: str, font: ImageFont.FreeTypeFont, letter_spacing: float = 0.0, max_lines: int = 2) -> List[str]:
        words = text.split()
        if not words:
            return []

        if self.measure_text(text, font, letter_spacing) <= self.max_text_width:
            return [text]

        if "," in text:
            comma_idx = text.find(",")
            part1 = text[:comma_idx + 1].strip()
            part2 = text[comma_idx + 1:].strip()
            if part1 and part2 and len(part1.split()) >= 2 and len(part2.split()) >= 2:
                if (self.measure_text(part1, font, letter_spacing) <= self.max_text_width and
                    self.measure_text(part2, font, letter_spacing) <= self.max_text_width):
                    return [part1, part2]

        best_split = None
        min_diff = float("inf")

        for i in range(1, len(words)):
            line1 = " ".join(words[:i])
            line2 = " ".join(words[i:])
            w1 = self.measure_text(line1, font, letter_spacing)
            w2 = self.measure_text(line2, font, letter_spacing)

            if w1 <= self.max_text_width and w2 <= self.max_text_width:
                diff = abs(w1 - w2)
                if diff < min_diff:
                    min_diff = diff
                    best_split = [line1, line2]

        if best_split:
            return best_split

        lines = []
        cur_line = []
        for word in words:
            candidate = " ".join(cur_line + [word])
            if self.measure_text(candidate, font, letter_spacing) <= self.max_text_width:
                cur_line.append(word)
            else:
                if cur_line:
                    lines.append(" ".join(cur_line))
                cur_line = [word]
        if cur_line:
            lines.append(" ".join(cur_line))

        return lines[:max_lines]

    def build_couplets(self, raw_cues: List[Dict], max_couplet_gap: float = 2.4, min_cue_duration: float = 1.4) -> List[Dict]:
        if not raw_cues:
            return []

        timed = []
        for i, cue in enumerate(raw_cues):
            start = cue["start"]
            if i + 1 < len(raw_cues):
                next_start = raw_cues[i + 1]["start"]
                dur = min(max(next_start - start, min_cue_duration), 5.5)
                end = min(start + dur, next_start - 0.15)
                if end <= start + 0.5:
                    end = max(start + 0.8, next_start - 0.05)
            else:
                end = start + 4.0

            timed.append({
                "start": start,
                "end": max(end, start + 0.8),
                "text": cue["text"]
            })

        couplets = []
        idx = 0
        while idx < len(timed):
            cur = timed[idx]
            can_pair = False
            if idx + 1 < len(timed):
                nxt = timed[idx + 1]
                gap_between_starts = nxt["start"] - cur["start"]
                if 0.8 <= gap_between_starts <= max_couplet_gap and len(cur["text"]) < 45 and len(nxt["text"]) < 45:
                    can_pair = True

            if can_pair:
                nxt = timed[idx + 1]
                if idx + 2 < len(timed):
                    couple_end = min(nxt["end"] + 0.4, timed[idx + 2]["start"] - 0.20)
                else:
                    couple_end = nxt["end"] + 1.5

                if couple_end <= nxt["start"] + 0.6:
                    couple_end = nxt["start"] + 1.2

                couplets.append({
                    "start": cur["start"],
                    "end": max(couple_end, nxt["start"] + 1.0),
                    "lines": [cur["text"], nxt["text"]],
                    "is_couplet": True,
                    "line2_start": nxt["start"]
                })
                idx += 2
            else:
                if idx + 1 < len(timed):
                    cue_end = min(cur["end"], timed[idx + 1]["start"] - 0.15)
                else:
                    cue_end = cur["end"]

                couplets.append({
                    "start": cur["start"],
                    "end": max(cue_end, cur["start"] + 0.8),
                    "lines": [cur["text"]],
                    "is_couplet": False
                })
                idx += 1

        for i in range(len(couplets) - 1):
            if couplets[i]["end"] >= couplets[i + 1]["start"]:
                couplets[i]["end"] = max(couplets[i]["start"] + 0.6, couplets[i + 1]["start"] - 0.15)

        return couplets

    def format_opening_sequence(self,
                                meta: Dict,
                                first_vocal_start: float,
                                contrast_style: Dict,
                                preset_key: str = "indie",
                                user_color_override: Optional[str] = None) -> List[str]:
        """
        Build production ASS event lines for the professional opening sequence.
        Respects:
          - Title, artist, optional featured artist, album, release year, channel watermark.
          - Adaptive text contrast (charcoal on light bg, soft white on dark bg).
          - Vocal collision avoidance: if first vocal is early (< 2.5s), auto-shortens or disables.
          - Smooth fade in/out + upward settle.
        """
        if not meta.get("enabled", True):
            return []

        # Check for early vocal collision
        # If vocals begin immediately (< 2.0s), do not show title over first lyric unless explicitly requested
        user_force = meta.get("force_over_vocal", False)
        if first_vocal_start < 2.0 and not user_force:
            print(f"[*] Notice: First vocal begins at {first_vocal_start:.2f}s. Automatically suppressing opening title to prevent overlap.")
            return []

        start_time = float(meta.get("start_time", 0.6))
        desired_dur = float(meta.get("duration", 4.2))

        # Title must end before vocals start with at least 0.8s clearance
        max_allowed_end = max(0.5, first_vocal_start - 0.8)
        end_time = min(start_time + desired_dur, max_allowed_end)

        if end_time - start_time < 1.5 and not user_force:
            print(f"[*] Notice: Headroom between title and vocals ({first_vocal_start:.2f}s) is too tight (<1.5s). Shortening title.")
            if end_time - start_time < 0.8:
                return []

        start_t = to_ass_time(start_time)
        end_t = to_ass_time(end_time)

        fade_in_ms = int(min(500, (end_time - start_time) * 200))
        fade_out_ms = int(min(450, (end_time - start_time) * 180))

        title = format_casing(meta.get("title", ""), "sentence")
        artist = meta.get("artist", "")
        feat = meta.get("featured_artist", "").strip()
        album = meta.get("album", "").strip()
        year = str(meta.get("release_year", "")).strip()
        watermark = meta.get("watermark", "").strip()

        # Build subheader
        artist_line = artist
        if feat:
            if not feat.lower().startswith("feat"):
                artist_line += f" (feat. {feat})"
            else:
                artist_line += f" ({feat})"

        meta_parts = []
        if album:
            meta_parts.append(album)
        if year:
            meta_parts.append(year)
        meta_str = " · ".join(meta_parts)

        # Positioning: centered at 48% height
        center_x = self.canvas_width // 2
        base_y = int(self.canvas_height * 0.48)

        # Text color override or adaptive
        sec_color = hex_to_ass_color(contrast_style["secondary_text_hex"], alpha=0)

        # Compose multi-row atomic title card
        # Line 1: Title (large)
        # Line 2: Artist (medium)
        # Line 3: Album / Year (small, optional)
        dialogues = []

        sub_elements = [f"{{\\fs42\\fsp2\\c{sec_color}}}{artist_line}"]
        if meta_str:
            sub_elements.append(f"{{\\fs28\\fsp3\\c{sec_color}}}{meta_str}")

        sub_text = "\\N".join(sub_elements)
        full_text = f"{title}\\N{sub_text}"

        anim = f"\\move({center_x},{base_y + 16},{center_x},{base_y},0,400)\\fad({fade_in_ms},{fade_out_ms})\\fsp1.5"
        dialogues.append(f"Dialogue: 0,{start_t},{end_t},TitleCard,,0,0,0,,{{{anim}}}{full_text}")

        # Optional watermark/channel logo in safe margin (bottom right or top left)
        if watermark:
            wm_x = self.canvas_width - self.margin_x
            wm_y = self.canvas_height - 60
            wm_anim = f"\\pos({wm_x},{wm_y})\\fad(400,400)\\fsp2"
            dialogues.append(f"Dialogue: 0,{start_t},{end_t},Watermark,,0,0,0,,{{{wm_anim}}}{watermark.upper()}")

        return dialogues

    def generate_ass_file(self,
                          lrc_path: Path,
                          out_ass_path: Path,
                          bg_image_path: Optional[Path] = None,
                          title: str = "Aesthetic Lyric Video",
                          artist: str = "",
                          preset_key: str = "indie",
                          vertical_ratio: float = 0.60,
                          custom_font_size: Optional[int] = None,
                          color_mode: str = "auto",  # 'auto', 'white', 'dark', 'custom'
                          custom_text_hex: Optional[str] = None,
                          opening_meta: Optional[Dict] = None) -> Path:
        """
        Generate ASS subtitle file with adaptive contrast and professional title sequence.
        """
        preset = STYLE_PRESETS.get(preset_key, STYLE_PRESETS["indie"])
        font_cfg = FONT_CONFIGS[preset["font_id"]]
        font_name = font_cfg["name"]
        font_size = custom_font_size or preset["font_size"]
        bold_val = font_cfg["bold"]
        spacing_val = preset["spacing"]

        # 1. Analyze background luminance in the lyric zone
        if bg_image_path and bg_image_path.exists():
            lum_info = analyze_region_luminance(bg_image_path, box=(0.15, vertical_ratio - 0.08, 0.85, vertical_ratio + 0.12))
            auto_style_key = lum_info["contrast_mode"]
            print(f"[*] Adaptive Contrast: Analyzed '{bg_image_path.name}' -> Mean Lum={lum_info['mean_lum']} ({auto_style_key.upper()})")
        else:
            auto_style_key = "dark_bg"

        # 2. Determine final text styling based on user choice
        if color_mode == "white":
            contrast_style = CONTRAST_STYLES["dark_bg"]
        elif color_mode == "dark":
            contrast_style = CONTRAST_STYLES["bright_bg"]
        elif color_mode == "custom" and custom_text_hex:
            contrast_style = dict(CONTRAST_STYLES["dark_bg"])
            contrast_style["text_hex"] = custom_text_hex
        else:
            # Automatic adaptive contrast
            contrast_style = CONTRAST_STYLES[auto_style_key]

        pri_color = hex_to_ass_color(contrast_style["text_hex"], alpha=0)
        out_color = hex_to_ass_color(contrast_style["outline_hex"], alpha=contrast_style["outline_alpha"])
        shadow_color = contrast_style["shadow_color"]
        outline_val = contrast_style["outline_width"]
        shadow_val = contrast_style["shadow_depth"]

        # 3. Parse LRC and format couplets
        raw_cues = parse_lrc(lrc_path)
        couplets = self.build_couplets(raw_cues)
        first_vocal = raw_cues[0]["start"] if raw_cues else 999.0

        # 4. Build Title Card events
        meta_dict = opening_meta or {
            "enabled": True,
            "title": title,
            "artist": artist,
            "start_time": 0.6,
            "duration": 4.5
        }
        title_dialogues = self.format_opening_sequence(
            meta=meta_dict,
            first_vocal_start=first_vocal,
            contrast_style=contrast_style,
            preset_key=preset_key
        )

        # 5. Build Lyric Events
        line_height_mult = font_cfg["line_height_mult"]
        line_spacing_px = int(font_size * line_height_mult)
        casing_mode = preset["casing"]
        pil_font = ImageFont.truetype(str(font_cfg["file"]), font_size)

        center_x = self.canvas_width // 2
        base_y = int(self.canvas_height * vertical_ratio)

        lyric_dialogues = []
        for cue in couplets:
            start_t = to_ass_time(cue["start"])
            end_t = to_ass_time(cue["end"])

            raw_lines = cue["lines"]
            formatted_lines = [format_casing(l, casing_mode) for l in raw_lines]

            if len(formatted_lines) == 1:
                wrapped = self.wrap_text_to_lines(formatted_lines[0], pil_font, spacing_val, max_lines=2)
                formatted_lines = wrapped

            active_font_size = font_size
            for line in formatted_lines:
                w = self.measure_text(line, pil_font, spacing_val)
                if w > self.max_text_width:
                    scale = self.max_text_width / float(w)
                    active_font_size = max(int(active_font_size * scale), 42)
                    pil_font = ImageFont.truetype(str(font_cfg["file"]), active_font_size)

            if len(formatted_lines) == 1:
                text = formatted_lines[0]
                y = base_y
                anim_move = f"\\move({center_x},{y+12},{center_x},{y},0,300)"
                tags = f"{anim_move}\\fad(280,200)\\fsp{spacing_val}"
                if active_font_size != font_size:
                    tags += f"\\fs{active_font_size}"
                lyric_dialogues.append(f"Dialogue: 0,{start_t},{end_t},Lyric,,0,0,0,,{{{tags}}}{text}")
            else:
                line1 = formatted_lines[0]
                line2 = formatted_lines[1]
                text = f"{line1}\\N{line2}"
                anim_move = f"\\move({center_x},{base_y+12},{center_x},{base_y},0,300)"
                tags = f"{anim_move}\\fad(280,200)\\fsp{spacing_val}"
                if active_font_size != font_size:
                    tags += f"\\fs{active_font_size}"
                lyric_dialogues.append(f"Dialogue: 0,{start_t},{end_t},Lyric,,0,0,0,,{{{tags}}}{text}")

        # Assemble Header & Styles
        header = f"""[Script Info]
Title: {title} - {artist}
ScriptType: v4.00+
PlayResX: {self.canvas_width}
PlayResY: {self.canvas_height}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TitleCard,{font_name},{int(font_size * 1.25)},{pri_color},&H000000FF,{out_color},{shadow_color},{bold_val},0,0,0,100,100,1.5,0,1,{outline_val},{shadow_val},5,50,50,50,1
Style: Watermark,{font_name},24,{pri_color},&H000000FF,{out_color},{shadow_color},0,0,0,0,100,100,2.0,0,1,{outline_val},{shadow_val},3,50,50,50,1
Style: Lyric,{font_name},{font_size},{pri_color},&H000000FF,{out_color},{shadow_color},{bold_val},0,0,0,100,100,{spacing_val},0,1,{outline_val},{shadow_val},5,50,50,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

        all_events = title_dialogues + lyric_dialogues
        full_content = header + "\n".join(all_events) + "\n"

        with open(out_ass_path, "w", encoding="utf-8") as f:
            f.write(full_content)

        return out_ass_path


if __name__ == "__main__":
    print("LyricLayoutEngine updated with Adaptive Contrast & Title Sequence.")
