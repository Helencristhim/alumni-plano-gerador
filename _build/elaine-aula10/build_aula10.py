#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build standalone Aula 10 (Elaine Mieko Pinho) — Special Requests / Allergies.
SEPARATE files per REGRA 34. Splices authored content into the proven aula9 scaffold
(CSS + JS verbatim), changing ONLY what aula 10 needs.

Scaffolds (proven-complete CSS/JS, contrast overrides, slide nav, lesson-progress):
  - public/professor/elaine-mieko-pinho-aula9.html  -> professor (4 tabs)
  - public/aluno/elaine-mieko-pinho-aula9.html       -> aluno (2 tabs)
Authored fragments (this dir):
  - slides.html         (28 slides, IN CLASS)        [prof only]
  - preclass.html       (welcome + lesson-card-10)   [prof + aluno]
  - complementary.html  (3 real media cards)         [prof + aluno]
  - phrases.json        (canonical audio list)        -> audioMap + generator
Outputs:
  - public/professor/elaine-mieko-pinho-aula10.html
  - public/aluno/elaine-mieko-pinho-aula10.html
  - scripts/generate-elaine-aula10-audio.js
NEVER touches the aula9 files or the monolith.

JS changes applied to the scaffold (REGRA 26 = copy integrally, change only data):
  - head audioMap object -> aula10 audioMap (from phrases.json)
  - var dialogueLine = 0  -> 1   (slide-16 dialogue: line 1 pre-visible)
  - nextDialogueLine threshold >= 8 -> >= 12 (12-line dialogue)
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))                 # wt-elaine/
PROF_SCAFFOLD  = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula9.html')
ALUNO_SCAFFOLD = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho-aula9.html')
PROF_OUT  = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula10.html')
ALUNO_OUT = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho-aula10.html')
GEN_OUT   = os.path.join(ROOT, 'scripts', 'generate-elaine-aula10-audio.js')
SLUG = 'elaine-mieko-pinho'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
phrases  = json.loads(read(os.path.join(HERE, 'phrases.json')))

N = len(re.findall(r'data-slide="\d+"', slides))
assert N == 28, 'expected 28 slides, got %d' % N

# ---------- helpers ----------
def replace_between(s, start, end, new_inner, label):
    i = s.index(start)
    j = s.index(end, i + len(start))
    return s[:i] + start + '\n' + new_inner + '\n' + end + s[j + len(end):]

def must_replace(s, old, new, label, count=1):
    assert s.count(old) >= count, 'anchor not found: %s' % label
    return s.replace(old, new, count)

# ---------- audioMap from phrases.json ----------
def audiomap_object():
    lines = []
    for p in phrases:
        k = json.dumps(p['key'], ensure_ascii=False)
        v = json.dumps('/audio/%s/' % SLUG + p['file'], ensure_ascii=False)
        lines.append('  %s: %s' % (k, v))
    return 'var audioMap = {\n' + ',\n'.join(lines) + '\n}'

AUDIOMAP = audiomap_object()

# ---------- SCENARIO FIT + CONTINUIDADE audit (REGRA 36 + 37, BLOQUEANTE) ----------
AUDIT = '''<!--
SCENARIO FIT — Aula 10
Can-do: "I can explain my food allergies and ask the waiter to change a dish."
Gramatica-alvo: "I am allergic to + food"; "Can you + verb...?" (pedido educado); "Does it have + food + in it?" (pergunta sobre ingrediente).
Vocab-alvo: allergic, allergy, nuts, shellfish, gluten, dairy, spicy, ingredient (+ without / instead como funcionais).
Cenario escolhido: o MESMO restaurante da Aula 9 (Grand Central Bistro), agora pedindo mudancas por causa de alergias — falar a alergia ao garcom, perguntar ingredientes, pedir o prato sem o alergeno.
Por que elicita o alvo: para comer com seguranca, o aluno PRECISA dizer "I am allergic to nuts", perguntar "Does the salad have nuts in it?" e pedir "Can you make it without dairy?". >70% dos itens-alvo sao naturalmente elicitados.

CONTINUIDADE — Aula 10
Itens novos desta aula: allergic, allergy, nuts, shellfish, gluten, dairy, spicy, ingredient; "I am allergic to..."; "Can you...?"; "Does it have... in it?".
Itens revisados (da Aula 9): menu, waiter, appetizer, main course, dessert, order; "I would like..."; "Could I have...?".
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 itens da Aula 9 — o aluno ouve e repete "Could I have the menu, please?" e "I would like the grilled chicken, please.", e faz a ponte: agora, antes de pedir, precisa avisar o garcom sobre a alergia.
-->
'''

# ---------- shared replacements (prof + aluno) ----------
def common(html):
    # title
    html = must_replace(html, 'Aula 9 | Restaurant Basics', 'Aula 10 | Special Requests -- Allergies', 'title')
    # head audioMap object  (var audioMap = { ... })
    i = html.index('var audioMap = {')
    j = html.index('};', i)
    html = html[:i] + AUDIOMAP + html[j + 1:]   # replace through the '}', keep trailing ';'
    # stamp10 after stamp9
    stamp9 = '<div class="stamp" id="stamp9" data-label="Restaurant" style="background-image:url(\'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=200&q=80\')"></div>'
    stamp10 = '<div class="stamp" id="stamp10" data-label="Allergies" style="background-image:url(\'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=200&q=80\')"></div>'
    html = must_replace(html, stamp9, stamp9 + '\n' + stamp10, 'stamp10')
    # audit comment right after <body>
    html = must_replace(html, '<body>\n', '<body>\n' + AUDIT, 'audit')
    # pre-class tab content
    html = replace_between(html, '<div class="tab-content active" id="tab-exercises">' if 'active" id="tab-exercises"' in html else '<div class="tab-content" id="tab-exercises">',
                           '</div><!-- /tab-exercises -->', preclass, 'tab-exercises')
    # complementary tab content
    html = replace_between(html, '<div class="tab-content" id="tab-complementary">',
                           '</div><!-- /tab-complementary -->', compl, 'tab-complementary')
    return html

# ---------- PROFESSOR ----------
prof = read(PROF_SCAFFOLD)
prof = common(prof)
# IN CLASS menu card
INCLASS_MENU = '''  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 10</h3>
  <div style="display:flex;flex-direction:column;gap:1rem">
    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(1,28)" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">10</div>
      <div><div style="font-weight:600;font-size:.95rem">Special Requests -- Allergies</div><div style="font-size:.8rem;color:var(--text-dim)">Allergies &amp; polite requests -- 28 slides</div></div>
    </div>
  </div>
'''
prof = replace_between(prof, '<div class="tab-content" id="tab-inclass">',
                       '<!-- ========== TAB 4: COMPLEMENTARES ========== -->',
                       INCLASS_MENU + '</div>\n', 'tab-inclass')
# slides
prof = replace_between(prof, '<div class="slides-container" id="slidesContainer">',
                       '</div><!-- /slides-container -->', slides, 'slides')
# JS: dialogue init + threshold
prof = must_replace(prof, 'var dialogueLine = 0;', 'var dialogueLine = 1;', 'dialogueLine-init')
prof = must_replace(prof,
    "    if (dialogueLine >= 8) {\n      document.getElementById('nextLineBtn').textContent = 'Dialogue Complete';",
    "    if (dialogueLine >= 12) {\n      document.getElementById('nextLineBtn').textContent = 'Dialogue Complete';",
    'dialogue-threshold')

# ---------- ALUNO ----------
aluno = read(ALUNO_SCAFFOLD)
aluno = common(aluno)

with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(prof)
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(aluno)

# ---------- audio generator (Node) ----------
gen_phrases = ',\n'.join(
    '  { text: %s, file: %s, voice: %s }' % (
        json.dumps(p['text'], ensure_ascii=False), json.dumps(p['file']), json.dumps(p['voice']))
    for p in phrases)
GEN = '''#!/usr/bin/env node
/**
 * ElevenLabs audio for Elaine Mieko Pinho - Aula 10 (Special Requests / Allergies).
 * Voices: Ellen (Elaine / student) + Arthur (waiter Daniel). Roster per REGRA 35/C1.
 * Skips files that already exist (REGRA C9 - never overwrite MP3s).
 */
const fs = require('fs');
const path = require('path');
const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = { arthur: 'sfJopaWaOtauCD3HKX6Q', ellen: 'BIvP0GN1cAtSRTxNHnWS', josh: 'TxGEqnHWrfWFTfGW9XjX', rachel: '21m00Tcm4TlvDq8ikWAM', domi: 'AZnzlk1XvdvUeBnXmlld', bella: 'EXAVITQu4vr4xnSDxMaL' };
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', '%SLUG%');
if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const phrases = [
%PHRASES%
];

async function generateAudio(text, filename, voiceId) {
  const filePath = path.join(OUTPUT_DIR, filename);
  if (fs.existsSync(filePath)) return { skipped: true };
  const response = await fetch(`${API_URL}/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true } })
  });
  if (!response.ok) throw new Error(`${response.status} for "${text.substring(0,40)}..."`);
  fs.writeFileSync(filePath, Buffer.from(await response.arrayBuffer()));
  return { skipped: false };
}

async function main() {
  console.log(`Generating ${phrases.length} audio files for Aula 10...`);
  let gen = 0, skip = 0, err = 0;
  for (const p of phrases) {
    try {
      const r = await generateAudio(p.text, p.file, VOICES[p.voice]);
      if (r.skipped) { skip++; process.stdout.write('.'); }
      else { gen++; process.stdout.write('+'); await new Promise(r => setTimeout(r, 300)); }
    } catch (e) { err++; console.error(`\\n  [ERROR] ${e.message}`); }
  }
  console.log(`\\n\\nDone: ${gen} generated, ${skip} skipped, ${err} errors`);
}
main().catch(console.error);
'''
GEN = GEN.replace('%SLUG%', SLUG).replace('%PHRASES%', gen_phrases)
with open(GEN_OUT, 'w', encoding='utf-8') as f: f.write(GEN)

print('OK  (N=%d slides)' % N)
print('  professor:', PROF_OUT, len(prof), 'bytes')
print('  aluno    :', ALUNO_OUT, len(aluno), 'bytes')
print('  generator:', GEN_OUT)
print('  audioMap keys:', len(phrases))
