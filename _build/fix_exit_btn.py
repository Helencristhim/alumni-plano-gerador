#!/usr/bin/env python3
"""Variante 3 do fix de nav-bar (complementa o #76): arquivos com botões
icon-only (setas SVG) e SEM botão EXIT — o template Elaine aula15 e todas as
aulas geradas a partir dele (Simone a3, Gleice a4, Rubens a4, Karina a4,
Aline a4, Nilo a9, etc.).

Substitui pelo layout canônico do Milton (#61/#76): EXIT + lessonLabel +
dots ocultos + Previous/Next com texto. O EXIT chama exitSlideMode() quando o
arquivo define a função (limpa .active — evita o bug do título fantasma),
senão remove a classe slide-mode direto.

Uso: python3 _build/fix_exit_btn.py  (a partir da raiz do worktree)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# nav-bar icon-only: prevBtn/nextBtn com <svg> dentro, dots no meio (ocultos ou nao)
OLD_RE = re.compile(
    r'<div class="nav-bar">\s*'
    r'<button class="nav-btn" id="prevBtn" onclick="changeSlide\(-1\)" disabled[^>]*><svg.*?</button>\s*'
    r'<div class="slide-dots" id="slideDots"[^>]*></div>\s*'
    r'<button class="nav-btn" id="nextBtn" onclick="changeSlide\(1\)"[^>]*><svg.*?</button>\s*'
    r'</div>',
    re.DOTALL,
)

NEW = '''<div class="nav-bar" style="justify-content:space-between;">
    <button onclick="{exit}" aria-label="Exit presentation" style="background:transparent;border:1px solid rgba(255,255,255,.35);color:rgba(255,255,255,.85);border-radius:8px;padding:.55rem 1.1rem;font-size:.72rem;font-weight:700;letter-spacing:1px;cursor:pointer;flex:0 0 auto;">&#10005; EXIT</button>
    <span id="lessonLabel" style="color:rgba(255,255,255,.5);font-size:.72rem;font-weight:600;letter-spacing:1px;flex:0 0 auto;">LESSON {n}</span>
    <div class="slide-dots" id="slideDots" style="display:none;"></div>
    <div style="display:flex;gap:.6rem;align-items:center;flex:0 0 auto;">
      <button id="prevBtn" onclick="changeSlide(-1)" disabled style="background:transparent;border:1.5px solid var(--accent);color:var(--accent);border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer;">&#8592; Previous</button>
      <button id="nextBtn" onclick="changeSlide(1)" style="background:var(--accent);border:1.5px solid var(--accent);color:#fff;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer;">Next &#8594;</button>
    </div>
  </div>'''


def lesson_num(path: Path) -> str:
    m = re.search(r'-aula(\d+)', path.stem)
    return m.group(1) if m else '1'  # hubs: JS atualiza via lessonLabel quando existe


def main():
    changed = 0
    for sub in ('professor', 'aluno'):
        for f in sorted((ROOT / 'public' / sub).glob('*.html')):
            html = f.read_text(encoding='utf-8')
            exit_js = ('exitSlideMode()' if 'function exitSlideMode' in html
                       else "document.body.classList.remove('slide-mode')")
            new = NEW.replace('{exit}', exit_js).replace('{n}', lesson_num(f))
            new_html, n = OLD_RE.subn(new, html)
            if n:
                f.write_text(new_html, encoding='utf-8')
                changed += 1
                print(f'fix {f.relative_to(ROOT)} (LESSON {lesson_num(f)}, exit={exit_js[:14]})')
    print(f'\n{changed} arquivos corrigidos')
    return 0 if changed else 1


if __name__ == '__main__':
    sys.exit(main())
