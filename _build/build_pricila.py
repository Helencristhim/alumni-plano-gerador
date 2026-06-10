#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder genérico das aulas standalone da Pricila Adamo (REGRA 34/38).
Uso: python3 _build/build_pricila.py N
Lê _build/pricila-aula{N}/ : meta.json, slides.html, preclass.html, complementary.html, phrases.json
Scaffold (CSS + engine JS + Planejamento + phase-bar) = public/professor/pricila-adamo.html.
Esqueleto fixo de 29 slides (mesma distribuição de fases da aula 6).
"""
import os, re, json, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                              # wt-pricila/
SLUG = 'pricila-adamo'
D = os.path.join(HERE, 'pricila-aula%d' % N)
MONO     = os.path.join(ROOT, 'public', 'professor', SLUG + '.html')
PROF_OUT = os.path.join(ROOT, 'public', 'professor', '%s-aula%d.html' % (SLUG, N))
ALUNO_OUT= os.path.join(ROOT, 'public', 'aluno', '%s-aula%d.html' % (SLUG, N))

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

meta     = json.loads(read(os.path.join(D, 'meta.json')))
mono     = read(MONO)
slides   = read(os.path.join(D, 'slides.html'))
preclass = read(os.path.join(D, 'preclass.html'))
compl    = read(os.path.join(D, 'complementary.html'))
phrases  = json.loads(read(os.path.join(D, 'phrases.json')))

NS = len(re.findall(r'data-slide="\d+"', slides))
assert NS == 29, 'esqueleto fixo de 29 slides, got %d' % NS
SLIDE_PHASES = ('{1:1,2:1,3:1,4:2,5:2,6:2,7:2,8:3,9:3,10:3,11:3,12:4,13:4,14:4,15:4,16:4,'
                '17:5,18:5,19:5,20:5,21:6,22:6,23:6,24:6,25:6,26:7,27:7,28:7,29:7}')

STAMPS_TABLE = {
 1:("Who Is","photo-1501785888041-af3ef285b470"), 2:("Life","photo-1506784983877-45594efa4cbe"),
 3:("Retire","photo-1507525428034-b723cf961d3e"), 4:("Travel","photo-1476514525535-07fb3b4ae5f1"),
 5:("Health","photo-1544367567-0f2fcb009e0b"),    6:("Airport","photo-1436491865332-7a61a109cc05"),
 7:("Hotel","photo-1566073771259-6a8506099945"),  8:("Transport","photo-1502602898657-3e91760cbb34"),
 9:("Dining","photo-1517248135467-4c7edcad34c4"), 10:("Market","photo-1488459716781-31db52582fe9"),
}

# ---- CSS + EXIT helpers ----
css = mono[mono.index('<style>'):mono.index('</style>')+len('</style>')]
EXIT_CSS = (
".exit-btn{padding:7px 16px;border-radius:8px;border:1px solid var(--accent);background:var(--accent);color:#fff;font-size:.78rem;font-weight:600;cursor:pointer;font-family:'Inter',sans-serif;white-space:nowrap}\n"
".exit-btn:hover{opacity:.85}\n"
".hub-back{display:inline-flex;align-items:center;gap:.3rem;margin-left:1rem;padding:5px 12px;border-radius:7px;border:1px solid var(--border);background:var(--bg-card);color:var(--accent);font-size:.78rem;font-weight:600;text-decoration:none;font-family:'Inter',sans-serif}\n"
".hub-back:hover{background:var(--accent);color:#fff;border-color:var(--accent)}\n"
"body.slide-mode .hub-back{display:none}\n"
"[contenteditable][data-placeholder]:empty:before{content:attr(data-placeholder);color:var(--text-dim);font-style:italic}\n"
)
css = css.replace('</style>', EXIT_CSS + '</style>')

# ---- JS engine (anchor em var totalSlides) + patches ----
anchor   = mono.index('var totalSlides =')
js_start = mono.rfind('<script>', 0, anchor)
js_end   = mono.index('</script>', anchor) + len('</script>')
js = mono[js_start:js_end]
js, n = re.subn(r'var totalSlides = \d+;', 'var totalSlides = %d;' % NS, js); assert n == 1
js, n = re.subn(r'var slidePhases = \{.*?\};', 'var slidePhases = ' + SLIDE_PHASES + ';', js, flags=re.S); assert n == 1
ch = ',\n'.join("  { prompt: %s, answer: %s }" % (json.dumps(c['prompt']), json.dumps(c['answer'])) for c in meta['challenges'])
CHAL = 'var challenges = [\n' + ch + '\n];\nvar challengeIndex = 0; var challengeCorrect = 0;'
js, n = re.subn(r'var challenges = \[.*?\];\s*var challengeIndex = 0; var challengeCorrect = 0;', lambda m: CHAL, js, flags=re.S); assert n == 1
js, n = re.subn(r"var dotsEl = document\.getElementById\('slideDots'\);",
                "var dotsEl = document.getElementById('slideDots'); if(!dotsEl) return;", js); assert n == 1
js = js.replace("'alumni-progress-pricila-adamo'", "'alumni-progress-pricila-adamo-aula%d'" % N)
EXTRA_JS = (
"\n// ===== REGRA 38 — Exit volta ao hub (IN CLASS) =====\n"
"function exitSlideMode() {\n  document.body.classList.remove('slide-mode');\n  window.location.href = '/professor/pricila-adamo.html#inclass';\n}\n"
"document.addEventListener('keydown', function(e) { if (e.key === 'Escape' && document.body.classList.contains('slide-mode')) exitSlideMode(); });\n"
"document.addEventListener('DOMContentLoaded', function() {\n  var first = document.querySelector('.slide[data-slide=\"1\"]');\n  if (first && new URLSearchParams(window.location.search).get('autostart') === '1') enterSlideMode();\n});\n"
)
assert js.count('</script>') == 1
js = js.replace('</script>', EXTRA_JS + '</script>')

# ---- slices ----
planning  = mono[mono.index('<div class="tab-content active" id="tab-planning">'):mono.index('</div><!-- /tab-planning -->')+len('</div><!-- /tab-planning -->')]
phase_bar = mono[mono.index('<div class="phase-bar"'):mono.index('<div class="slides-container"')]

welcome = meta['welcome']

def audiomap_js():
    lines = ['  %s: %s' % (json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/%s/%s' % (SLUG, p['file']), ensure_ascii=False)) for p in phrases]
    return 'var audioMap = {\n' + ',\n'.join(lines) + '\n};'
AUDIOMAP = audiomap_js()

def head(title):
    return ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<meta name="robots" content="noindex, nofollow">\n<title>' + title + '</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
        '<script>\n' + AUDIOMAP + '\n</script>\n' + css + '\n'
        '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>\n'
        '<script src="/lib/supabase-config.js"></script>\n'
        "<script>window.STUDENT_SLUG='pricila-adamo';window.TOTAL_AULAS=40;</script>\n</head>\n")

def stamps_row():
    out = ['<div class="stamps-row">']
    for i in range(1, N + 1):
        lbl, img = STAMPS_TABLE[i]
        out.append('<div class="stamp" id="stamp%d" data-label="%s" style="background-image:url(\'https://images.unsplash.com/%s?w=200&q=80\')"></div>' % (i, lbl, img))
    out.append('</div>')
    return '\n'.join(out)

SPEED = ('<div class="speed-control">\n  <span class="speed-label">Velocidade:</span>\n'
  '  <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>\n'
  '  <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>\n'
  '  <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>\n'
  '  <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>\n</div>\n\n')

def header(badge, hubhref):
    return ('<body>\n\n<div class="logo-bar">\n  <img src="/assets/logo-alumni.png" alt="Alumni by Better">\n'
      '  <span class="prof-badge">' + badge + '</span>\n'
      '  <a href="' + hubhref + '" class="hub-back" title="Voltar para a lista de aulas">&#8592; Aulas</a>\n'
      '  <span class="slide-counter" id="slideCounter">01 / %02d</span>\n</div>\n\n' % NS
      + '<div class="main-content">\n\n<div class="header">\n  <div class="header-content">\n'
      '    <div class="passport-badge">Travel English -- 40 Aulas</div>\n    <h1>Pricila Adamo</h1>\n'
      '    <p class="subtitle">De &ldquo;eu sei o que quero dizer mas n&atilde;o consigo dizer&rdquo; para &ldquo;passaporte pronto, ingl&ecirc;s pronto&rdquo;</p>\n'
      '    <div class="student-info">\n      <span>B1+ (B2 operacional)</span>\n      <span>Araras, SP</span>\n'
      '      <span>Dentista em transi&ccedil;&atilde;o para aposentadoria</span>\n      <span>60 min / Online</span>\n    </div>\n'
      '    <div class="progress-passport">\n      <div class="progress-label"><span>' + meta['header_label'] + '</span><span id="progressPercent">0%</span></div>\n'
      '      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>\n'
      + stamps_row() + '\n    </div>\n  </div>\n</div>\n\n<div class="container">\n\n' + SPEED)

TABS_PROF = ('<div class="tabs-wrapper">\n  <div class="tabs">\n'
  "    <button class=\"tab-btn active\" onclick=\"switchTab('planning')\">Planejamento</button>\n"
  "    <button class=\"tab-btn\" onclick=\"switchTab('exercises')\">Pre-class</button>\n"
  "    <button class=\"tab-btn\" onclick=\"switchTab('inclass')\">IN CLASS</button>\n"
  "    <button class=\"tab-btn\" onclick=\"switchTab('complementary')\">Complementares</button>\n  </div>\n</div>")
TABS_ALUNO = ('<div class="tabs-wrapper">\n  <div class="tabs">\n'
  "    <button class=\"tab-btn active\" onclick=\"switchTab('exercises')\">Pre-class</button>\n"
  "    <button class=\"tab-btn\" onclick=\"switchTab('complementary')\">Complementares</button>\n  </div>\n</div>")

INCLASS_MENU = ('<div class="tab-content" id="tab-inclass">\n'
  '  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula %d</h3>\n' % N
  + '  <div style="display:flex;flex-direction:column;gap:1rem">\n'
  '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode()" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
  '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">%02d</div>\n' % N
  + '      <div><div style="font-weight:600;font-size:.95rem">' + meta['card_title'] + '</div><div style="font-size:.8rem;color:var(--text-dim)">' + meta['card_sub'] + ' &mdash; ' + str(NS) + ' slides</div></div>\n'
  '    </div>\n  </div>\n</div>')

TAIL = ('<!-- TEACHER T -->\n<div class="teacher-t">T<div class="teacher-t-panel" id="teacherPanel"></div></div>\n\n'
  '<!-- CONFETTI -->\n<div class="confetti-container" id="confettiContainer"></div>\n\n'
  '<!-- NAV BAR -->\n<div class="nav-bar">\n'
  '  <button class="exit-btn" onclick="exitSlideMode()" aria-label="Exit to lesson list">&#10005; Exit</button>\n'
  '  <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" aria-label="Previous slide"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>\n'
  '  <div class="slide-dots" id="slideDots"></div>\n'
  '  <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)" aria-label="Next slide"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></button>\n</div>')

TAIL_SCRIPTS = ('<script src="/lib/lesson-progress.js"></script>\n<script src="/lib/controle-aulas.js"></script>\n'
  '<script src="/lib/activity-sync.js"></script>\n<script src="/lib/contrast-guard.js"></script>\n')

ACC_OPEN = ('<div class="lesson-card open" id="ex-lesson-%d">\n' % N
  + '  <div class="lesson-header" onclick="toggleLesson(this)">\n'
  + '    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/' + meta['stamp_img'] + '?w=600&q=80\')"></div>\n'
  + '    <div class="lesson-header-content">\n      <div class="lesson-number">Aula %02d -- Pre-class</div>\n' % N
  + '      <h3>' + meta['accordion_h3'] + '</h3>\n'
  + '      <div class="lesson-desc">' + meta['accordion_desc'] + '</div>\n'
  + '      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="%d" style="width:0%%"></div></div><span class="mini-percent" data-lesson-pct="%d">0%%</span></div>\n' % (N, N)
  + '    </div>\n    <div class="expand-icon">&#9660;</div>\n  </div>\n'
  + '  <div class="lesson-body">\n' + welcome + '\n' + preclass + '\n  </div>\n</div>\n')

prof = (head(meta['title_full'] + ' | Professor View &mdash; Pricila Adamo | Aula %d | Alumni by Better' % N)
  + header('PROFESSOR VIEW', '/professor/pricila-adamo.html#inclass')
  + meta['audit'] + '\n'
  + TABS_PROF + '\n\n'
  + '<!-- TAB 1: PLANEJAMENTO -->\n' + planning + '\n\n'
  + '<!-- TAB 2: PRE-CLASS -->\n<div class="tab-content" id="tab-exercises">\n' + ACC_OPEN + '</div>\n\n'
  + '<!-- TAB 3: IN CLASS -->\n' + INCLASS_MENU + '\n\n'
  + '<!-- TAB 4: COMPLEMENTARES -->\n<div class="tab-content" id="tab-complementary">\n' + compl + '\n</div><!-- /tab-complementary -->\n\n'
  + '</div><!-- /container -->\n</div><!-- /main-content -->\n\n'
  + '<div class="slides-wrapper">\n\n' + phase_bar + slides + '\n</div><!-- /slides-container -->\n</div><!-- /slides-wrapper -->\n\n'
  + TAIL + '\n\n' + js + '\n' + TAIL_SCRIPTS + '</body>\n</html>\n')

aluno = (head(meta['title_full'] + ' | Aluno &mdash; Pricila Adamo | Aula %d | Alumni by Better' % N)
  + header('ALUNO', '/aluno/pricila-adamo.html')
  + TABS_ALUNO + '\n\n'
  + '<!-- TAB: PRE-CLASS -->\n<div class="tab-content active" id="tab-exercises">\n' + ACC_OPEN + '</div>\n\n'
  + '<!-- TAB: COMPLEMENTARES -->\n<div class="tab-content" id="tab-complementary">\n' + compl + '\n</div><!-- /tab-complementary -->\n\n'
  + '</div><!-- /container -->\n</div><!-- /main-content -->\n\n'
  + '<div class="confetti-container" id="confettiContainer"></div>\n\n' + js + '\n' + TAIL_SCRIPTS + '</body>\n</html>\n')

open(PROF_OUT, 'w', encoding='utf-8').write(prof)
open(ALUNO_OUT, 'w', encoding='utf-8').write(aluno)
print('OK aula %d (NS=%d)  prof=%d bytes  aluno=%d bytes  audioMap=%d' % (N, NS, len(prof), len(aluno), len(phrases)))
