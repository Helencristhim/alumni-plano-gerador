#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGRA 38 no hub eduarda-gabriel.html (professor): Exit/Esc sai do slide-mode e volta
ao menu IN CLASS interno (aulas 1-5 inline); #inclass abre a aba IN CLASS ao voltar de
um arquivo standalone; links da aula 6 viram same-tab e o card do menu IN CLASS recebe
?autostart=1. Idempotente (aborta se ja patchado)."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HUB = os.path.join(ROOT, 'public', 'professor', 'eduarda-gabriel.html')

s = open(HUB, encoding='utf-8').read()
assert 'exitSlideMode' not in s, 'hub ja tem exitSlideMode — abortando p/ nao duplicar'

EXIT_CSS = (
".exit-btn{padding:7px 16px;border-radius:8px;border:1px solid var(--accent);background:var(--accent);color:#fff;font-size:.78rem;font-weight:600;cursor:pointer;font-family:'Inter',sans-serif;white-space:nowrap}\n"
".exit-btn:hover{opacity:.85}\n"
)
HUB_SCRIPT = (
'<script>\n'
'/* REGRA 38 — Exit/Esc sai do slide-mode e volta ao menu IN CLASS; #inclass abre a aba ao voltar de um standalone */\n'
'function exitSlideMode(){document.body.classList.remove("slide-mode");window.scrollTo({top:0});}\n'
'document.addEventListener("keydown",function(e){if(e.key==="Escape"&&document.body.classList.contains("slide-mode"))exitSlideMode();});\n'
'document.addEventListener("DOMContentLoaded",function(){if(window.location.hash==="#inclass"){var b=document.querySelector(\'.tab-btn[onclick*="inclass"]\');if(b)b.click();}});\n'
'</script>\n'
)

PRE_OLD = '<a href="/professor/eduarda-gabriel-aula6.html" target="_blank" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit;margin-bottom:1.5rem" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">'
PRE_NEW = PRE_OLD.replace(' target="_blank"', '')

IC_OLD = '<a href="/professor/eduarda-gabriel-aula6.html" target="_blank" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">'
IC_NEW = IC_OLD.replace(' target="_blank"', '').replace('eduarda-gabriel-aula6.html"', 'eduarda-gabriel-aula6.html?autostart=1"')

subs = [
    ('</style>', EXIT_CSS + '</style>', 'exit css'),
    ('<div class="nav-bar">\n  <button class="nav-btn" id="prevBtn"',
     '<div class="nav-bar">\n  <button class="exit-btn" onclick="exitSlideMode()" aria-label="Exit to lesson list">&#10005; Exit</button>\n  <button class="nav-btn" id="prevBtn"', 'exit button'),
    ('<script src="/lib/lesson-progress.js"></script>',
     HUB_SCRIPT + '<script src="/lib/lesson-progress.js"></script>', 'hub script'),
    (PRE_OLD, PRE_NEW, 'preclass link same-tab'),
    (IC_OLD, IC_NEW, 'inclass link autostart'),
]
for old, new, label in subs:
    assert s.count(old) == 1, 'anchor x%d for %s' % (s.count(old), label)
    s = s.replace(old, new)
open(HUB, 'w', encoding='utf-8').write(s)
print('hub patched:', HUB)
