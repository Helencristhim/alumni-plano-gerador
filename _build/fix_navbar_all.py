#!/usr/bin/env python3
"""Replica o fix do Milton (#61) em todos os hubs/aulas: nav-bar antigo
(slide-dots empurravam Previous/Next pra fora da tela) -> layout do standalone
(EXIT + lessonLabel + dots ocultos + Previous/Next sempre visiveis).

Regenera o PR #62 em cima do main atual (cobre tambem aulas mergeadas depois).
Uso: python3 _build/fix_navbar_all.py  (a partir da raiz do worktree)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# nav-bar antigo: prevBtn + slideDots + nextBtn dentro de <div class="nav-bar">
OLD_RE = re.compile(
    r'<div class="nav-bar">\s*'
    r'<button class="nav-btn" id="prevBtn"[^>]*>[^<]*</button>\s*'
    r'<div class="slide-dots" id="slideDots"></div>\s*'
    r'<button class="nav-btn" id="nextBtn"[^>]*>[^<]*</button>\s*'
    r'</div>'
)

NEW = '''<div class="nav-bar" style="justify-content:space-between;">
    <button onclick="document.body.classList.remove('slide-mode')" aria-label="Exit presentation" style="background:transparent;border:1px solid rgba(255,255,255,.35);color:rgba(255,255,255,.85);border-radius:8px;padding:.55rem 1.1rem;font-size:.72rem;font-weight:700;letter-spacing:1px;cursor:pointer;flex:0 0 auto;">&#10005; EXIT</button>
    <span id="lessonLabel" style="color:rgba(255,255,255,.5);font-size:.72rem;font-weight:600;letter-spacing:1px;flex:0 0 auto;">LESSON {n}</span>
    <div class="slide-dots" id="slideDots" style="display:none;"></div>
    <div style="display:flex;gap:.6rem;align-items:center;flex:0 0 auto;">
      <button id="prevBtn" onclick="changeSlide(-1)" disabled style="background:transparent;border:1.5px solid var(--accent);color:var(--accent);border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer;">&#8592; Previous</button>
      <button id="nextBtn" onclick="changeSlide(1)" style="background:var(--accent);border:1.5px solid var(--accent);color:#fff;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer;">Next &#8594;</button>
    </div>
  </div>'''


def lesson_num(path: Path) -> str:
    m = re.search(r'-aula(\d+)', path.stem)
    return m.group(1) if m else '1'  # hubs: JS troca via lessonLabel quando existe


# variante 2 (ex.: Eduarda): nav-bar ja tem exit-btn proprio, mas dots visiveis
# entre Previous/Next -> mesmo overflow; basta ocultar os dots.
DOTS_OLD = '<div class="slide-dots" id="slideDots"></div>'
DOTS_NEW = '<div class="slide-dots" id="slideDots" style="display:none;"></div>'


def main():
    changed = 0
    for sub in ('professor', 'aluno'):
        for f in sorted((ROOT / 'public' / sub).glob('*.html')):
            html = f.read_text(encoding='utf-8')
            new_html, n = OLD_RE.subn(NEW.replace('{n}', lesson_num(f)), html)
            if DOTS_OLD in new_html:
                new_html = new_html.replace(DOTS_OLD, DOTS_NEW)
                n += 1
            if n:
                if n > 1:
                    print(f'AVISO: {n} nav-bars em {f.relative_to(ROOT)}')
                f.write_text(new_html, encoding='utf-8')
                changed += 1
                print(f'fix {f.relative_to(ROOT)} (LESSON {lesson_num(f)})')
    print(f'\n{changed} arquivos corrigidos')
    return 0 if changed else 1


if __name__ == '__main__':
    sys.exit(main())
