#!/usr/bin/env python3
"""Generate ElevenLabs audio for vanessa-maluf.html with Arthur/Ellen alternation.
FIXED: Properly handles escaped apostrophes in speakText('I\\'m ...')
"""

import re, os, hashlib, json, time
from elevenlabs import ElevenLabs

ARTHUR = "sfJopaWaOtauCD3HKX6Q"  # Male, neutral American
ELLEN  = "BIvP0GN1cAtSRTxNHnWS"  # Female, calm American

HTML_FILE = os.path.join(os.path.dirname(__file__), "..", "public", "professor", "vanessa-maluf.html")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "public", "audio", "vanessa-maluf")
MAP_FILE = os.path.join(OUTPUT_DIR, "map.json")

def extract_phrases(html):
    """Extract all unique phrases from speakText() and data-phrase.
    Handles escaped apostrophes: speakText('I\\'m sorry') -> I'm sorry
    """
    phrases = set()
    # Pattern handles \\' inside single-quoted JS strings
    for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'\s*,", html):
        raw = m.group(1)
        clean = raw.replace("\\'", "'")
        phrases.add(clean)
    # Double-quoted speakText
    for m in re.finditer(r'speakText\("([^"]+)"\s*,', html):
        phrases.add(m.group(1))
    # data-phrase attributes
    for m in re.finditer(r'data-phrase="([^"]+)"', html):
        phrases.add(m.group(1))
    return sorted(phrases)

def extract_dialogue_voices(html):
    """Extract dialogue lines with their voice assignments."""
    voice_map = {}
    for m in re.finditer(r'data-voice="(arthur|ellen)"', html):
        start = m.end()
        sm = re.search(r"speakText\('((?:[^'\\]|\\.)*)'\s*,", html[start:start+500])
        if sm:
            phrase = sm.group(1).replace("\\'", "'")
            voice_map[phrase] = ARTHUR if m.group(1) == "arthur" else ELLEN
    return voice_map

def pick_voice(phrase, dialogue_voices, counter):
    """Pick Arthur or Ellen per CLAUDE.md rules."""
    if phrase in dialogue_voices:
        return dialogue_voices[phrase]
    words = phrase.strip().split()
    if len(words) <= 2:
        return ARTHUR
    counter[0] += 1
    return ARTHUR if counter[0] % 2 == 1 else ELLEN

def text_to_filename(text):
    slug = re.sub(r'[^a-z0-9\s]', '', text.lower().strip())
    slug = re.sub(r'\s+', '_', slug)[:55]
    h = hashlib.md5(text.encode()).hexdigest()[:6]
    return f"{slug}_{h}.mp3"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    phrases = extract_phrases(html)
    dialogue_voices = extract_dialogue_voices(html)
    print(f"Found {len(phrases)} unique phrases.")
    print(f"Dialogue voice assignments: {len(dialogue_voices)}")

    # Load existing map
    audio_map = {}
    if os.path.exists(MAP_FILE):
        with open(MAP_FILE, 'r') as f:
            audio_map = json.load(f)

    client = ElevenLabs()
    generated = skipped = errors = 0
    counter = [0]

    for i, phrase in enumerate(phrases, 1):
        filename = text_to_filename(phrase)
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Check if already exists (by phrase key or file on disk)
        if phrase in audio_map and os.path.exists(os.path.join(OUTPUT_DIR, audio_map[phrase])):
            skipped += 1
            continue
        if os.path.exists(filepath):
            audio_map[phrase] = filename
            skipped += 1
            continue

        voice = pick_voice(phrase, dialogue_voices, counter)
        voice_name = "Arthur" if voice == ARTHUR else "Ellen"
        print(f"[{i}/{len(phrases)}] {voice_name}: {phrase[:55]}...")

        try:
            audio_gen = client.text_to_speech.convert(
                text=phrase,
                voice_id=voice,
                model_id="eleven_multilingual_v2",
                output_format="mp3_44100_128",
            )
            audio_data = b"".join(audio_gen)
            with open(filepath, 'wb') as f:
                f.write(audio_data)
            audio_map[phrase] = filename
            generated += 1
            with open(MAP_FILE, 'w') as f:
                json.dump(audio_map, f, indent=2, ensure_ascii=False)
            if generated % 10 == 0:
                time.sleep(1)
        except Exception as e:
            print(f"  ERROR: {e}")
            errors += 1

    print(f"\nDone! Generated: {generated}, Skipped: {skipped}, Errors: {errors}, Total: {len(phrases)}")

    # Update the HTML audioMap with CORRECT keys (no truncation)
    print("\nUpdating audioMap in HTML...")

    # Build JS audioMap — escape for JS string (double quotes around key)
    js_map_lines = []
    for phrase in sorted(audio_map.keys()):
        # Escape for JS: backslash and double quotes
        escaped = phrase.replace("\\", "\\\\").replace('"', '\\"')
        path = audio_map[phrase]
        js_map_lines.append(f'    "{escaped}": "/audio/vanessa-maluf/{path}"')

    new_map = "var audioMap = {\n" + ",\n".join(js_map_lines) + "\n};"

    # Replace existing audioMap in HTML using DOTALL to match multiline
    # The audioMap block starts with "var audioMap = {" and ends with "};"
    # We need to find the LAST }; that closes the audioMap
    map_start = html.find('var audioMap = {')
    if map_start < 0:
        print("ERROR: audioMap not found!")
        return

    # Find the matching closing };
    brace_count = 0
    map_end = map_start
    for i in range(map_start, len(html)):
        if html[i] == '{':
            brace_count += 1
        elif html[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                map_end = i + 1
                # Skip the semicolon
                if map_end < len(html) and html[map_end] == ';':
                    map_end += 1
                break

    updated = html[:map_start] + new_map + html[map_end:]

    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(updated)

    # Verify
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        verify_html = f.read()

    verify_phrases = extract_phrases(verify_html)
    verify_keys = set()
    for m in re.finditer(r'"([^"]+)"\s*:\s*"/audio/vanessa-maluf/', verify_html):
        verify_keys.add(m.group(1))

    still_missing = set(verify_phrases) - verify_keys
    print(f"audioMap updated with {len(audio_map)} entries.")
    print(f"Verification: {len(verify_phrases)} phrases, {len(verify_keys)} map keys, {len(still_missing)} missing")
    if still_missing:
        for p in sorted(still_missing)[:5]:
            print(f"  STILL MISSING: {p[:60]}")

if __name__ == "__main__":
    main()
