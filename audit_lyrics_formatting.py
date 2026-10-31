import re
from pathlib import Path

def smart_format_lyric(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    
    # 1. Clean extra spaces
    text = re.sub(r"\s+", " ", text)
    
    # 2. Check if text has parenthetical ad-lib at end, e.g. "I'm trying to kiss your lips for real (uh-huh, uh-huh)"
    m_paren = re.search(r"^(.*?)\s*(\([^\)]+\))$", text)
    if m_paren:
        main_part = m_paren.group(1).strip()
        paren_part = m_paren.group(2).strip()
        if len(main_part) >= 12:
            return f"{main_part.upper()}\\N{paren_part.upper()}"
    
    # 3. Only split if line is long enough (34+ chars or 8+ words)
    words = text.split()
    if len(text) < 34 and len(words) < 8:
        # Keep as clean, bold single line!
        return text.upper()
    
    # 4. Check for natural comma split near the middle
    if "," in text:
        comma_indices = [m.start() for m in re.finditer(r",", text)]
        # Pick comma closest to the center
        midpoint = len(text) / 2
        best_comma = min(comma_indices, key=lambda idx: abs(idx - midpoint))
        p1 = text[:best_comma].strip()
        p2 = text[best_comma + 1:].strip()
        # Ensure both halves have reasonable length
        if len(p1) >= 10 and len(p2) >= 10:
            return f"{p1.upper()}\\N{p2.upper()}"
            
    # 5. Fallback: split long line at word midpoint
    mid_word = len(words) // 2
    p1 = " ".join(words[:mid_word]).strip()
    p2 = " ".join(words[mid_word:]).strip()
    return f"{p1.upper()}\\N{p2.upper()}"

# Audit on test lines
test_samples = [
    "Well, I want you to stay",  # Was awkwardly split before! Should be 1 line now.
    "Until I'm in the grave",    # Should be 1 line now!
    "Birds of a feather, we should stick together, I know",  # Long line -> 2 lines
    "If the world was ending, I'd wanna be next to you",     # 2 lines
    "I'm trying to kiss your lips for real (uh-huh, uh-huh)", # Clean split with paren
    "Apateu, apateu, apateu, apateu",                         # Hook
    "Yeah, yeah, yeah, yeah, yeah, I'm on my way"            # Split
]

print("=== AUDIT RESULTS ===")
for sample in test_samples:
    res = smart_format_lyric(sample)
    print(f"INPUT : {sample}")
    print(f"OUTPUT: {repr(res)}")
    print("-" * 40)
