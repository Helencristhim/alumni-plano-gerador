#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inline da Aula 5 (Andreia Heins) — Talking About Experience (Have You Ever...?).
O hub da Andreia é inline-monolítico PURO (sem standalones): este script injeta
preclass (accordion ex-lesson-5) + 28 slides (113-140) + menu + lessonRanges +
JS da aula + stamps + audioMap em AMBOS os hubs (aluno é espelho integral),
e gera phrases.json (prefixo a5_; listenings via data-src entram como SPECIAL).
Ver DIALETO.md neste diretório."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SLUG = 'andreia-heins'
PROF = os.path.join(ROOT, 'public', 'professor', SLUG + '.html')
ALUN = os.path.join(ROOT, 'public', 'aluno', SLUG + '.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def must(h, old, new):
    assert h.count(old) == 1, 'anchor not unique (%d): %.70s' % (h.count(old), old)
    return h.replace(old, new)

slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html')).rstrip() + '\n'
N = len(re.findall(r'data-slide="\d+"', slides)); assert N == 28, 'expected 28 slides, got %d' % N
nums = sorted(int(n) for n in re.findall(r'data-slide="(\d+)"', slides))
assert nums[0] == 113 and nums[-1] == 140, 'slides devem ser 113-140'

# ---------- AUDIO ----------
SPECIAL_FILES = [
  ('a5_listening_adams.mp3', 'arthur',
   "Hello Andreia, this is Doctor Adams, from the robotic surgery center in Chicago. I am "
   "visiting Hospital Albert Einstein next Friday, and I have heard excellent things about "
   "your team. I want to ask you about your experience with the robotic surgery program — "
   "the procedures, the training, everything you have done. See you on Friday!"),
  ('a5_listening_model.mp3', 'ellen',
   "Let me summarize my experience. In my career, I have assisted in hundreds of procedures. "
   "I have completed three certifications, here and abroad. I have supervised simulation "
   "sessions for new nurses, and I have trained my first team this year — my biggest "
   "milestone. And in all these years, I have never stopped learning."),
]
SPECIAL_KEYS = {
  '[order-l5]': ('a5_order_sequence.mp3', 'arthur',
   "Doctor Adams arrives at Einstein on Friday. He asks: have you ever worked with the newest "
   "console? Andreia presents her numbers: procedures and certifications. She says what she "
   "has never done — yet. He invites her to the exchange program."),
}

def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return 'a5_' + (s[:55].rstrip("_")) + ".mp3"

dialogue_voice = {}
for line in slides.splitlines():
    if 'data-voice="' in line and "speakText('" in line:
        v = re.search(r'data-voice="([^"]+)"', line)
        t = re.search(r"speakText\('((?:[^'\\]|\\.)*)'", line)
        if v and t:
            dialogue_voice[t.group(1).replace("\\'", "'")] = v.group(1)

seen, ordered = set(), []
for src in (preclass, slides):
    for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", src):
        t = m.group(1).replace("\\'", "'")
        if t not in seen:
            seen.add(t); ordered.append(t)
    for m in re.finditer(r'data-phrase="([^"]+)"', src):
        t = m.group(1)
        if t not in seen:
            seen.add(t); ordered.append(t)

audio_map = {}
phrases = [{'text': t, 'file': f, 'voice': v} for (f, v, t) in SPECIAL_FILES]
toggle = ['ellen', 'arthur']; ti = 0
for t in ordered:
    if t in SPECIAL_KEYS:
        fname, voice, narration = SPECIAL_KEYS[t]
        audio_map[t] = '/audio/%s/%s' % (SLUG, fname)
        phrases.append({'text': narration, 'file': fname, 'voice': voice})
        continue
    fname = slugify(t)
    audio_map[t] = '/audio/%s/%s' % (SLUG, fname)
    if t in dialogue_voice:
        voice = dialogue_voice[t]
    elif len(t.split()) <= 2:
        voice = 'arthur'
    else:
        voice = toggle[ti % 2]; ti += 1
    phrases.append({'text': t, 'file': fname, 'voice': voice})

A5_ENTRIES = ',\n'.join('  %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False))
                        for k, v in audio_map.items()) + ','

with open(os.path.join(HERE, 'phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases, f, ensure_ascii=False, indent=2)

# ---------- blocos ----------
STAMP5 = '\n        <div class="stamp" id="stamp5" data-label="Expertise" style="background-image:url(\'https://images.unsplash.com/photo-1551601651-2a8555f1a136?w=200&q=80\')"></div>'

MENU_CARD5 = '''    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(113);" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>
      <div><div style="font-weight:600;font-size:.95rem">Talking About Experience</div><div style="font-size:.8rem;color:var(--text-dim)">Have you ever...? Present perfect -- 28 slides</div></div>
    </div>
'''

JS5 = '''
// ===== AULA 5: DIALOGO =====
var dialogueLine5 = 1;
function nextDialogueLine5() {
  dialogueLine5++;
  var line = document.querySelector("#dialogueBox5 .dialogue-line[data-line=\\"" + dialogueLine5 + "\\"]");
  if (line) {
    line.classList.add("visible");
    if (dialogueLine5 >= 8) {
      document.getElementById("nextLineBtn5").textContent = "Dialogue Complete";
      document.getElementById("nextLineBtn5").disabled = true;
      document.getElementById("nextLineBtn5").style.opacity = "0.5";
    }
  }
}
'''

def patch(path, is_prof):
    h = read(path); before = (h.count('<div'), h.count('</div>'))
    m4 = re.search(r'<div class="stamp[^"]*" id="stamp4"[^>]*></div>', h)
    assert m4, 'stamp4 nao encontrado em %s' % path
    h = must(h, m4.group(0), m4.group(0) + STAMP5)
    h = must(h, '</div><!-- /tab-exercises -->', preclass + '</div><!-- /tab-exercises -->')
    h = must(h, 'var audioMap = {', 'var audioMap = {\n' + A5_ENTRIES)
    h = must(h, 'totalLessons = 4', 'totalLessons = 5')
    if is_prof:
        # o ALUNO da Andreia tem 2 abas (sem tab-inclass/menu); slides/ranges la sao codigo morto
        h = must(h, '4: { start: 85, end: 112 } }', '4: { start: 85, end: 112 }, 5: { start: 113, end: 140 } }')
        i = h.index('enterSlideMode(85)')
        j = h.index('</div>\n    </div>', i) + len('</div>\n    </div>') + 1
        h = h[:j] + MENU_CARD5 + h[j:]
        h = must(h, '</div><!-- /slides-container -->', '\n<!-- ===== AULA 5 (inline): slides 113-140 ===== -->\n' + slides + '\n</div><!-- /slides-container -->')
        h = must(h, 'var dialogueLine4 = ', JS5 + 'var dialogueLine4 = ')
    after = (h.count('<div'), h.count('</div>'))
    assert (after[0]-before[0]) == (after[1]-before[1]), 'div imbalance: %s -> %s' % (before, after)
    with open(path, 'w', encoding='utf-8') as f: f.write(h)
    print('patched %-6s div delta open=%d close=%d (balanced)' % ('prof' if is_prof else 'aluno', after[0]-before[0], after[1]-before[1]))

patch(PROF, True)
patch(ALUN, False)
print('OK inline aula5; audioMap keys=%d, phrases=%d, slides=%d' % (len(audio_map), len(phrases), N))
