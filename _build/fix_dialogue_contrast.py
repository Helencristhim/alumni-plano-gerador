#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FIX PERMANENTE do contraste de dialogo (REGRA contraste PART 2).
Causa: o bloco 'ANTI-TEXTO-INVISIVEL FIX UNIVERSAL v3' usa wildcards
[class*="bubble"]/[class*="box"] que forcam color:#1a1a2e (texto ESCURO) nos
.dialogue-bubble — que ficam sobre slide-dark => texto escuro sobre fundo escuro.
Solucao: injetar um bloco de override DEPOIS do v3 (antes de </style>) que volta o
texto do dialogo para BRANCO, deixa as bubbles mais opacas (contraste) e adiciona
uma 3a cor de falante (guest) para dialogos multi-party.

Como o build copia o CSS do monolito, corrigir o monolito conserta as aulas 1-5
inline E todas as aulas futuras automaticamente. Os standalones ja gerados
(aula6/aula7) sao corrigidos aqui tambem. Idempotente.
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FIX = (
"/* === DIALOGUE CONTRAST FIX (REGRA contraste PART 2) — texto BRANCO legivel em slide-dark === */\n"
"/* sobrescreve o wildcard [class*=\"bubble\"]/[class*=\"box\"] do FIX v3 que forcava texto escuro */\n"
".slide-dark .dialogue-bubble,.slide-dark .dialogue-bubble p,.slide-dark .dialogue-bubble span,.slide-dark .dialogue-line,.slide-dark .dialogue-box,.slide-dark .dialogue-text{color:#fff!important}\n"
".slide-dark .dialogue-bubble.james-bubble{background:rgba(91,155,213,.22)!important;border-color:rgba(91,155,213,.5)!important}\n"
".slide-dark .dialogue-bubble.eduarda-bubble{background:rgba(124,92,191,.30)!important;border-color:rgba(124,92,191,.55)!important}\n"
".dialogue-avatar.guest{background:#0891b2}\n"
".dialogue-bubble.guest-bubble{background:rgba(8,145,178,.12);border:1px solid rgba(8,145,178,.25)}\n"
".slide-dark .dialogue-bubble.guest-bubble{background:rgba(8,145,178,.28)!important;border-color:rgba(8,145,178,.5)!important}\n"
".slide-dark .dialogue-bubble .vocab-highlight{color:#C4A8FF!important}\n"
".slide-dark .dialogue-name{color:rgba(255,255,255,.85)!important}\n"
".slide-dark .dialogue-bubble .audio-inline svg{stroke:#fff!important}\n"
)
MARKER = 'DIALOGUE CONTRAST FIX'

CSS_FILES = [
    'public/professor/eduarda-gabriel.html',
    'public/aluno/eduarda-gabriel.html',
    'public/professor/eduarda-gabriel-aula6.html',
    'public/aluno/eduarda-gabriel-aula6.html',
    'public/professor/eduarda-gabriel-aula7.html',
    'public/aluno/eduarda-gabriel-aula7.html',
]
for rel in CSS_FILES:
    p = os.path.join(ROOT, rel)
    s = open(p, encoding='utf-8').read()
    if MARKER in s:
        print('  CSS skip (ja tem):', rel); continue
    assert s.count('</style>') == 1, '%s: %d </style>' % (rel, s.count('</style>'))
    s = s.replace('</style>', FIX + '</style>', 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('  CSS fixed:', rel)

# 3a cor de falante: Anna (aula 7) usava a MESMA bubble da Eduarda (roxo) -> vira 'guest' (ciano)
ANNA_OLD = '<div class="dialogue-avatar eduarda">A</div><div class="dialogue-bubble eduarda-bubble">'
ANNA_NEW = '<div class="dialogue-avatar guest">A</div><div class="dialogue-bubble guest-bubble">'
for rel in ['public/professor/eduarda-gabriel-aula7.html', '_build/eduarda-aula7/slides.html']:
    p = os.path.join(ROOT, rel)
    s = open(p, encoding='utf-8').read()
    n = s.count(ANNA_OLD)
    if n == 0:
        print('  Anna skip (ja guest ou ausente):', rel); continue
    s = s.replace(ANNA_OLD, ANNA_NEW)
    open(p, 'w', encoding='utf-8').write(s)
    print('  Anna->guest (%d linhas):' % n, rel)

print('OK')
