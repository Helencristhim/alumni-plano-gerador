#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Aula 5 nos hubs do Rubens (prof + aluno). ADD ONLY — nunca toca aulas 1-4.
O hub do Rubens é INLINE-MONOLÍTICO (153 slides, lessonRanges, enterSlideMode):
- prof: stamp5 + accordion ex-lesson-5 + SLIDES INLINE (data-slide 154-181) +
  lessonRanges 5 + card menu enterSlideMode(154) + JS da aula 5
  (revealVocab5/nextDialogueLine5) + audioMap merge + totalLessons 4->5
- aluno: stamp5 + accordion + audioMap merge + totalLessons 4->5"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SLUG = 'rubens-tofolo'
PROF = os.path.join(ROOT, 'public', 'professor', SLUG + '.html')
ALUN = os.path.join(ROOT, 'public', 'aluno', SLUG + '.html')
BASE = 153  # hub tem slides 1..153 (aulas 1-4)

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def must(h, old, new):
    assert h.count(old) == 1, 'anchor not unique (%d): %.70s' % (h.count(old), old)
    return h.replace(old, new)

pre = read(os.path.join(HERE, 'preclass.html'))
LESSON_CARD = ('\n<!-- ==================== LESSON 5: DESCRIBING PEOPLE & PLACES ==================== -->\n'
               + pre[pre.index('<div class="lesson-card" id="ex-lesson-5">'):].rstrip() + '\n')

STAMP5 = '\n        <div class="stamp" id="stamp5" data-label="Bel&eacute;m" style="background-image:url(\'https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=200&q=80\')"></div>'

# ---- slides inline: renumera e isola ids/funcoes da aula 5 ----
slides = read(os.path.join(HERE, 'slides.html'))
slides = re.sub(r'data-slide="(\d+)"', lambda m: 'data-slide="%d"' % (int(m.group(1)) + BASE), slides)
slides = slides.replace('class="slide active slide-dark"', 'class="slide slide-dark"', 1)
slides = (slides
          .replace('revealVocab(this)', 'revealVocab5(this)')
          .replace('id="vocabGrid1"', 'id="vocabGrid5a"').replace("'vocabGrid1'", "'vocabGrid5a'")
          .replace('id="vocabCount1"', 'id="vocabCount5a"')
          .replace('id="vocabGrid2"', 'id="vocabGrid5b"')
          .replace('id="vocabCount2"', 'id="vocabCount5b"')
          .replace('nextDialogueLine()', 'nextDialogueLine5()')
          .replace('id="nextLineBtn"', 'id="nextLineBtn5"'))
SLIDES_INLINE = '\n<!-- ===== AULA 5 (inline): slides 154-181 ===== -->\n' + slides + '\n'

JS5 = '''
// ===== AULA 5: DIALOGO + VOCAB =====
var dialogueLine5 = 1;
function nextDialogueLine5() {
  dialogueLine5++;
  var line = document.querySelector('#dialogue5 .dialogue-line[data-line="' + dialogueLine5 + '"]');
  if (line) {
    line.style.display = 'flex';
    line.classList.add('visible');
    if (dialogueLine5 >= 12) {
      document.getElementById('nextLineBtn5').textContent = 'Dialogue Complete';
      document.getElementById('nextLineBtn5').disabled = true;
      document.getElementById('nextLineBtn5').style.opacity = '0.5';
    }
  }
}
function revealVocab5(card) {
  card.classList.toggle('revealed');
  var front = card.querySelector('.vocab-front');
  var back = card.querySelector('.vocab-back');
  if (front && back) {
    var on = card.classList.contains('revealed');
    front.style.display = on ? 'none' : '';
    back.style.display = on ? '' : 'none';
  }
  var grid = card.closest('.vocab-grid');
  var count = grid.querySelectorAll('.vocab-card-ic.revealed').length;
  var total = grid.querySelectorAll('.vocab-card-ic').length;
  var counterId = grid.id === 'vocabGrid5a' ? 'vocabCount5a' : 'vocabCount5b';
  var el = document.getElementById(counterId);
  if (el) el.textContent = count + ' / ' + total + ' words revealed';
}
'''

MENU4_END = '<div><div style="font-weight:600;font-size:.95rem">Life Experiences</div><div style="font-size:.8rem;color:var(--text-dim)">Present Perfect with ever, never, already, yet -- 33 slides</div></div>\n    </div>\n'

MENU_CARD = '''    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(154)" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>
      <div><div style="font-weight:600;font-size:.95rem">Describing People &amp; Places</div><div style="font-size:.8rem;color:var(--text-dim)">Comparatives &amp; superlatives -- 28 slides</div></div>
    </div>
'''

aula5_prof = read(os.path.join(ROOT, 'public', 'professor', SLUG + '-aula5.html'))
m = re.search(r'var audioMap = \{(.*?)\n\}', aula5_prof, re.S)
assert m, 'audioMap da aula 5 nao encontrado'
A5_ENTRIES = m.group(1).strip().rstrip(',') + ','

def patch(path, is_aluno):
    h = read(path); before = (h.count('<div'), h.count('</div>'))
    m4 = re.search(r'<div class="stamp[^"]*" id="stamp4"[^>]*></div>', h)
    assert m4, 'stamp4 nao encontrado em %s' % path
    h = must(h, m4.group(0), m4.group(0) + STAMP5)
    h = must(h, '</div><!-- /tab-exercises -->', LESSON_CARD + '</div><!-- /tab-exercises -->')
    h = must(h, 'var audioMap = {', 'var audioMap = {\n  ' + A5_ENTRIES)
    h = must(h, 'totalLessons = 4', 'totalLessons = 5')
    if not is_aluno:
        h = must(h, '4: {start:121, end:153} };', '4: {start:121, end:153}, 5: {start:154, end:181} };')
        h = must(h, MENU4_END, MENU4_END + MENU_CARD)
        h = must(h, '</div><!-- /slides-container -->', SLIDES_INLINE + '</div><!-- /slides-container -->')
        h = must(h, 'var dialogueLine4 = 0;', JS5 + 'var dialogueLine4 = 0;')
    after = (h.count('<div'), h.count('</div>'))
    assert (after[0]-before[0]) == (after[1]-before[1]), 'div imbalance: %s -> %s' % (before, after)
    with open(path, 'w', encoding='utf-8') as f: f.write(h)
    print('patched %-6s div delta open=%d close=%d (balanced)' % ('aluno' if is_aluno else 'prof', after[0]-before[0], after[1]-before[1]))

patch(PROF, False)
patch(ALUN, True)
print('hub wired OK')
