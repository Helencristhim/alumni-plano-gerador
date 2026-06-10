#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build standalone Aula 4 (Aline Sberci) -- Looking Ahead: future plans (be going to / will).
Splices authored content into the proven Elaine aula15 scaffold (CSS+JS verbatim), swapping
accent + identity + audioMap + slugs + lesson number. Outputs prof + aluno."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF_SCAFFOLD  = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula15.html')
ALUNO_SCAFFOLD = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho-aula15.html')
HUB            = os.path.join(ROOT, 'public', 'professor', 'aline-sberci.html')
PROF_OUT  = os.path.join(ROOT, 'public', 'professor', 'aline-sberci-aula4.html')
ALUNO_OUT = os.path.join(ROOT, 'public', 'aluno', 'aline-sberci-aula4.html')
SLUG = 'aline-sberci'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
phrases  = json.loads(read(os.path.join(HERE, 'phrases.json')))
hub      = read(HUB)
N = len(re.findall(r'data-slide="\d+"', slides)); assert N == 28, 'expected 28 slides, got %d' % N

def slice_between(s, start, end):
    i = s.index(start); j = s.index(end, i + len(start))
    return s[i + len(start):j]
def replace_between(s, start, end, new_inner):
    i = s.index(start); j = s.index(end, i + len(start))
    return s[:i] + start + '\n' + new_inner + '\n' + end + s[j + len(end):]
def must(s, old, new):
    assert old in s, 'anchor missing: %.60s' % old
    return s.replace(old, new, 1)

# --- extract aline identity from her live hub ---
aline_header_inner = slice_between(hub, '<div class="header">', '<div class="container">')
aline_planning     = slice_between(hub, '<div class="tab-content active" id="tab-planning">', '</div><!-- /tab-planning -->')

AUDIOMAP = 'var audioMap = {\n' + ',\n'.join(
    '  %s: %s' % (json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/%s/' % SLUG + p['file'], ensure_ascii=False))
    for p in phrases) + '\n}'

AUDIT = '''<!--
SCENARIO FIT -- Aula 4 (Aline Sberci)
Can-do: "I can talk about my future plans, goals and predictions at work using 'be going to' and 'will'."
Gramatica-alvo: be going to (planos decididos) + will (previsoes, promessas, decisoes na hora) + time words (soon, next week/month).
Vocab-alvo: plan, goal, soon, next month, improve, launch, promise, probably.
Cenario escolhido: Aline, gerente de projetos na Novartis, planeja seu proximo projeto (Project Aurora) e conversa com o colega Daniel.
Por que elicita o alvo: planejar um projeto OBRIGA a falar de planos (going to), previsoes (will), metas (goal) e prazos (soon/next month). >70% dos itens-alvo elicitados.

CONTINUIDADE -- Aula 4
Itens novos: plan, goal, soon, next month, improve, launch, promise, probably; "be going to", "will".
Itens revisados (Aula 3): past simple do percurso de carreira.
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 itens da Aula 3 -- a aluna ouve e repete "Novartis hired me five years ago." e "I started my career in technology.", e faz a ponte: olhou para o passado, agora olha para o futuro.
-->
'''

def build(scaffold, is_aluno):
    h = scaffold
    # 1. identity: name, slug, lesson number, totals, titles
    h = h.replace('Elaine Mieko Pinho', 'Aline Sberci')
    h = h.replace('Elaine Pinho', 'Aline Sberci')  # neutralize name in inert scaffold JS residue
    h = h.replace('Indaiatuba, SP', 'São Paulo, SP').replace('Indaiatuba', 'São Paulo')
    h = h.replace('elaine-mieko-pinho', SLUG)
    h = h.replace('Aula 15 | Shopping: Stores | Travel English', 'Aula 4 | Looking Ahead | General + Business English')
    h = h.replace('aula9-professor', 'aula4-professor').replace('aula9-aluno', 'aula4-aluno')
    h = h.replace('window.TOTAL_AULAS=32', 'window.TOTAL_AULAS=48')

    # 2. accent palette (Roxo uva -> Azul eletrico)
    h = h.replace('#5E4B6D', '#2563EB')
    h = h.replace('#C4A8D8', '#3B82F6')
    h = h.replace('#E0CFF0', '#93B4FB')
    h = h.replace('94,75,109', '37,99,235')

    # 3. hero background (give white-on-image guaranteed contrast)
    h = must(h, "background:url('https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1400&q=80') center/cover no-repeat;",
             "background:linear-gradient(rgba(26,26,46,.85),rgba(26,26,46,.7)),url('https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1400&q=80') center/cover no-repeat;")

    # 4. audioMap
    i = h.index('var audioMap = {'); j = h.index('}', i)
    # find the matching close of the audioMap object (first '\n}' at col0 after start)
    j = h.index('\n}', i) + 2
    h = h[:i] + AUDIOMAP + h[j:]

    # 5. AUDIT comment after <body>
    h = must(h, '<body>\n', '<body>\n' + AUDIT)

    # 6. header identity (name, subtitle, role, stamps) from aline's live hub
    h = replace_between(h, '<div class="header">', '<div class="container">', aline_header_inner)

    # 7. Pre-class
    pre_start = '<div class="tab-content active" id="tab-exercises">' if 'active" id="tab-exercises"' in h else '<div class="tab-content" id="tab-exercises">'
    h = replace_between(h, pre_start, '</div><!-- /tab-exercises -->', preclass)

    # 8. Complementares
    h = replace_between(h, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', compl)

    if not is_aluno:
        # 9. Planning (professor only) from aline's live hub
        h = replace_between(h, '<div class="tab-content active" id="tab-planning">', '</div><!-- /tab-planning -->', aline_planning)

        # 10. IN CLASS menu
        MENU = ('  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 4</h3>\n'
                '  <div style="display:flex;flex-direction:column;gap:1rem">\n'
                '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(1,28)" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
                '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">04</div>\n'
                '      <div><div style="font-weight:600;font-size:.95rem">Looking Ahead -- Future Plans</div><div style="font-size:.8rem;color:var(--text-dim)">Plans, goals &amp; predictions -- 28 slides</div></div>\n'
                '    </div>\n  </div>\n')
        h = replace_between(h, '<div class="tab-content" id="tab-inclass">', '<!-- ========== TAB 4: COMPLEMENTARES ========== -->', MENU + '</div>\n\n')

        # 11. slides
        h = replace_between(h, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->', slides)

        # 12. autostart: fix broken enterSlideMode ref + support ?autostart=1 (aline hub convention)
        old_auto = "if (window.location.hash === '#slides') { document.addEventListener('DOMContentLoaded', function() { setTimeout(function(){ enterSlideMode(1); }, 100); }); }"
        new_auto = ("function enterSlideMode(n){ startLesson(1,28); }\n"
                    "if (window.location.hash === '#slides' || /[?&]autostart=1/.test(window.location.search)) { document.addEventListener('DOMContentLoaded', function() { setTimeout(function(){ startLesson(1,28); }, 100); }); }")
        h = must(h, old_auto, new_auto)

    return h

with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(build(read(PROF_SCAFFOLD), False))
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(build(read(ALUNO_SCAFFOLD), True))
print('OK aula4 built: %s slides, %d audio keys' % (N, len(phrases)))
print('  prof :', PROF_OUT)
print('  aluno:', ALUNO_OUT)
