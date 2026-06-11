#!/usr/bin/env python3
"""Extract every speakText('...') and data-phrase="..." literal from the authored
fragments and emit phrases.json (audio spec). Guarantees audioMap covers 100% of
the phrases the validator checks. Adds manual entries for the ordering audio and
the two listening MP3s (referenced via data-src, not speakText)."""
import os, re, json, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
FRAGMENTS = ['slides.html', 'preclass.html', 'welcome.html']

ORDER_TEXT = ("Dear Ms. Klein. I am writing to confirm our meeting on Friday. "
              "Could you please send the agenda? Please find attached the report. "
              "I look forward to hearing from you. Best regards, Nilo.")

# data-src listening scripts (sound-first, single MP3 each)
LISTENINGS = [
    {"file": "aula9_listening_email.mp3", "voice": "arthur",
     "text": ("Dear Ms. Klein. I am writing to confirm our compliance meeting on Friday. "
              "Could you please send the agenda before the meeting? Please find attached "
              "the compliance report. I look forward to hearing from you. Best regards, Nilo.")},
    {"file": "aula9_listening_reply.mp3", "voice": "ellen",
     "text": ("Thank you, Nilo. The email looks very professional. Your greeting is formal, "
              "and your request is polite. Please remember to check the subject line and the "
              "attachment before you send it.")},
]

def collect():
    phrases = []  # preserve first-seen order
    seen = set()
    for fn in FRAGMENTS:
        c = open(os.path.join(HERE, fn), encoding='utf-8').read()
        for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", c):
            p = m.group(1).replace("\\'", "'")
            if p not in seen:
                seen.add(p); phrases.append(p)
        for m in re.finditer(r'data-phrase="([^"]+)"', c):
            p = m.group(1)
            if p not in seen:
                seen.add(p); phrases.append(p)
        for m in re.finditer(r"data-phrase='([^']+)'", c):
            p = m.group(1)
            if p not in seen:
                seen.add(p); phrases.append(p)
    return phrases

def slug(p):
    w = re.sub(r"[^a-z0-9]+", "_", p.lower()).strip("_")[:40].strip("_")
    h = hashlib.md5(p.encode("utf-8")).hexdigest()[:6]
    return "aula9_%s_%s.mp3" % (w, h)

def main():
    phrases = collect()
    out = []
    arthur_turn = True
    for p in phrases:
        if p == "[order-l9]":
            out.append({"key": "[order-l9]", "text": ORDER_TEXT,
                        "file": "aula9_order_email.mp3", "voice": "arthur"})
            continue
        ntok = len(p.split())
        if ntok <= 2:
            voice = "arthur"
        else:
            voice = "arthur" if arthur_turn else "ellen"
            arthur_turn = not arthur_turn
        out.append({"key": p, "text": p, "file": slug(p), "voice": voice})
    # manual listening entries (key = full audio path so build puts them in audioMap & gen makes them)
    for L in LISTENINGS:
        out.append({"key": "/audio/nilo-mesquita-patucci/%s" % L["file"],
                    "text": L["text"], "file": L["file"], "voice": L["voice"]})
    json.dump(out, open(os.path.join(HERE, "phrases.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("phrases.json: %d entries (%d spoken + %d listening)" % (len(out), len(phrases), len(LISTENINGS)))

if __name__ == "__main__":
    main()
