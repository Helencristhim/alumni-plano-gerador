#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch the hub (monolithic eduardo-chiba.html, professor + aluno) for Aula 5:
  - Pre-class: ex-lesson-5 ACCORDION inline (REGRA 34 hub-accordion variant, prompt OBRIGATORIO #1)
  - audioMap: add aula5 Pre-class phrase keys (so accordion audio works)
  - stamps-row: stamp5
  - updateProgress: totalLessons 4 -> 5
  - (prof only) IN CLASS menu: <a href> card to standalone aula5 (REGRA 34b)
  - (prof only) #inclass deep-link handler (REGRA 38)
Idempotent: asserts the anchor is present and the patch not already applied."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
WT   = os.path.dirname(os.path.dirname(HERE))
SLUG = 'eduardo-chiba'
PROF = os.path.join(WT, 'public', 'professor', f'{SLUG}.html')
ALUNO= os.path.join(WT, 'public', 'aluno', f'{SLUG}.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)

accordion = read(os.path.join(HERE, 'preclass.html')).rstrip()
phrases   = json.loads(read(os.path.join(HERE, 'phrases.json')))

# preclass audio keys (speakText + data-phrase in the accordion)
pk = set(re.findall(r"speakText\('((?:[^'\\]|\\.)*)'", accordion))
pk |= set(re.findall(r'data-phrase="((?:[^"\\]|\\.)*)"', accordion))
pk = {k.replace("\\'", "'").replace('\\"', '"') for k in pk}

AUDIO_ANCHOR = '  "The ROI for our partners has been consistently positive.": "/audio/eduardo-chiba/aula4_preclass_survival_5.mp3"\n};'
PRECLASS_ANCHOR = '</div><!-- /lesson-card lesson-4 -->\n\n</div><!-- /tab-exercises -->'
STAMP_ANCHOR = '<div class="stamp" id="stamp4" data-label="Data" style="background-image:url(\'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80\')"></div>'
STAMP5 = STAMP_ANCHOR + '\n        <div class="stamp" id="stamp5" data-label="Elevator Pitch" style="background-image:url(\'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=200&q=80\')"></div>'

def patch_common(html, fname):
    # 1. audioMap additions
    assert AUDIO_ANCHOR in html, f'{fname}: audioMap anchor missing'
    existing = set(re.findall(r'"((?:[^"\\]|\\.)*)":\s*"/audio/%s/' % re.escape(SLUG), html))
    existing = {k.replace('\\"', '"') for k in existing}
    adds = []
    for p in phrases:
        if p['key'] in pk and p['key'] not in existing:
            adds.append('  %s: %s' % (json.dumps(p['key'], ensure_ascii=False),
                                      json.dumps('/audio/%s/%s' % (SLUG, p['file']), ensure_ascii=False)))
    if adds:
        new_tail = AUDIO_ANCHOR.replace('\n};', ',\n' + ',\n'.join(adds) + '\n};')
        html = html.replace(AUDIO_ANCHOR, new_tail, 1)
    # 2. Pre-class accordion
    assert PRECLASS_ANCHOR in html, f'{fname}: pre-class anchor missing'
    assert 'id="ex-lesson-5"' not in html, f'{fname}: ex-lesson-5 already present'
    html = html.replace(PRECLASS_ANCHOR,
        '</div><!-- /lesson-card lesson-4 -->\n\n<!-- LESSON 5 (Block 1 Review) -->\n' + accordion +
        '\n\n</div><!-- /tab-exercises -->', 1)
    # 3. stamp5
    assert STAMP_ANCHOR in html, f'{fname}: stamp4 anchor missing'
    assert 'id="stamp5"' not in html, f'{fname}: stamp5 already present'
    html = html.replace(STAMP_ANCHOR, STAMP5, 1)
    # 4. totalLessons 4 -> 5
    assert 'var totalLessons = 4;' in html, f'{fname}: totalLessons anchor missing'
    html = html.replace('var totalLessons = 4;', 'var totalLessons = 5;')
    return html, len(adds)

# ---- PROFESSOR ----
prof = read(PROF)
prof, nadd_p = patch_common(prof, 'professor')
# 5. IN CLASS menu card (standalone link, REGRA 34b)
MENU_ANCHOR = '    </div>\n  </div>\n</div>\n\n<!-- ========== TAB 4: COMPLEMENTARES ========== -->'
assert MENU_ANCHOR in prof, 'professor: inclass menu anchor missing'
CARD5 = ('    <a href="/professor/eduardo-chiba-aula5.html" target="_blank" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
  '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>\n'
  '      <div><div style="font-weight:600;font-size:.95rem">Block 1 Review -- The Elevator Pitch</div><div style="font-size:.8rem;color:var(--text-dim)">Identity, value &amp; comparatives, polite asks, present perfect -- 27 slides</div></div>\n'
  '    </a>\n')
prof = prof.replace(MENU_ANCHOR, '    </div>\n' + CARD5 + '  </div>\n</div>\n\n<!-- ========== TAB 4: COMPLEMENTARES ========== -->', 1)
# 6. #inclass deep-link handler (REGRA 38)
HANDLER_ANCHOR = '</script>\n<script src="/lib/lesson-progress.js"></script>'
assert HANDLER_ANCHOR in prof, 'professor: handler anchor missing'
assert "hash === '#inclass'" not in prof, 'professor: handler already present'
HANDLER = ('</script>\n<script>\n'
  'document.addEventListener("DOMContentLoaded", function() {\n'
  '  if (window.location.hash === "#inclass") {\n'
  '    var inclassBtn = document.querySelector(\'.tab-btn[onclick*="inclass"]\');\n'
  '    if (inclassBtn) inclassBtn.click();\n'
  '  }\n});\n</script>\n<script src="/lib/lesson-progress.js"></script>')
prof = prof.replace(HANDLER_ANCHOR, HANDLER, 1)
write(PROF, prof)

# ---- ALUNO (no IN CLASS, no handler) ----
aluno = read(ALUNO)
aluno, nadd_a = patch_common(aluno, 'aluno')
write(ALUNO, aluno)

print('professor: %d audioMap adds, stamp5+accordion+menu+handler applied' % nadd_p)
print('aluno    : %d audioMap adds, stamp5+accordion applied' % nadd_a)
