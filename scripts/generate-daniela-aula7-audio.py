#!/usr/bin/env python3
"""Generate ElevenLabs audio for Daniela Feitoza — Aula 7 (Past Simple).
Parses the audioMap in public/professor/daniela-feitoza-aula7.html and creates
one mp3 per unique file path. Voices match the approved setup
(arthur = male / ellen = female). Idempotent: skips files that already exist.
"""
import json, os, re, sys, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROF = os.path.join(ROOT, "public", "professor", "daniela-feitoza-aula7.html")

VOICES = {
    "arthur": "sfJopaWaOtauCD3HKX6Q",  # male, neutral American
    "ellen":  "BIvP0GN1cAtSRTxNHnWS",  # female, calm American
}

# Load API key
API_KEY = os.environ.get("ELEVENLABS_API_KEY")
if not API_KEY:
    env = open(os.path.join(ROOT, ".env.local"), encoding="utf-8").read()
    m = re.search(r"ELEVENLABS_API_KEY=(\S+)", env)
    API_KEY = m.group(1) if m else None
if not API_KEY:
    sys.exit("No ELEVENLABS_API_KEY found")

# Lines spoken by James (male) -> arthur. Everything else default ellen.
JAMES_LINES = {
    "So Daniela, tell me about a big project you worked on last year.",
    "That sounds big. What was the biggest challenge?",
    "Wow. How did you solve that problem?",
    "And what happened in the end?",
    "That is a great result. Did you achieve your main goal?",
    "How did you solve that problem?",       # listening cue (James)
    "Did you achieve your main goal?",        # listening cue (James)
}
VOCAB_WORDS = {"Launch","Solve","Achieve","Challenge","Deadline","Milestone",
               "Result","Improve","Workflow","Module","Implement","Deploy"}

# Special: the ordering exercise plays ONE file of the 5 sentences in order.
ORDER_TEXT = ("Last year, we started a new SAP project. "
              "At first, the deadline was very tight. "
              "We made a plan and worked together every day. "
              "We solved the problems and launched the system. "
              "In the end, we achieved our goal.")

def voice_for(key):
    if key in JAMES_LINES: return "arthur"
    if key in VOCAB_WORDS: return "arthur"
    return "ellen"

# Parse audioMap (key -> /audio/.../file.mp3)
html = open(PROF, encoding="utf-8").read()
block = re.search(r"var audioMap = \{(.*?)\};", html, re.S).group(1)
pairs = re.findall(r'"((?:[^"\\]|\\.)*)":\s*"([^"]+\.mp3)"', block)

# Dedupe by output path; pick tts text + voice
jobs = {}  # relpath -> (text, voice)
for key, relpath in pairs:
    key = key.replace('\\"', '"')
    if relpath in jobs:
        continue
    if key.startswith("[order-l7]"):
        jobs[relpath] = (ORDER_TEXT, "ellen")
    else:
        jobs[relpath] = (key, voice_for(key))

print(f"Daniela Feitoza — Aula 7 Audio Generator")
print(f"Unique audio files: {len(jobs)}")
print("---")

def generate_one(text, voice_id, retries=2):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    body = json.dumps({
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }).encode("utf-8")
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=body, method="POST", headers={
            "Content-Type": "application/json", "xi-api-key": API_KEY, "Accept": "audio/mpeg",
        })
        try:
            with urllib.request.urlopen(req, timeout=120) as res:
                return res.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print("  Rate limited, waiting 30s..."); time.sleep(30); continue
            if attempt == retries:
                raise RuntimeError(f"HTTP {e.code}: {e.read().decode('utf-8','ignore')[:200]}")
            time.sleep(5)
        except Exception as e:
            if attempt == retries: raise
            time.sleep(5)

gen = skip = fail = 0
items = sorted(jobs.items())
for i, (relpath, (text, voice)) in enumerate(items, 1):
    outpath = os.path.join(ROOT, "public", relpath.lstrip("/"))
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    if os.path.exists(outpath):
        skip += 1; continue
    short = text[:48] + ("..." if len(text) > 48 else "")
    print(f"[{i}/{len(items)}] ({voice}) \"{short}\" ", end="", flush=True)
    try:
        buf = generate_one(text, VOICES[voice])
        with open(outpath, "wb") as fh: fh.write(buf)
        gen += 1; print("OK")
        time.sleep(0.15)
    except Exception as e:
        fail += 1; print(f"FAILED: {e}")

print(f"\nDone! Generated: {gen}, Skipped: {skip}, Failed: {fail}")
sys.exit(1 if fail else 0)
