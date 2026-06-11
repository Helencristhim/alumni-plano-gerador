#!/usr/bin/env python3
"""Reaplica o fix do 3699b606 (audio-inline SVG genérico) nos arquivos
restaurados de 6cd5b3b9~1 — o fix da Helen rodou em cima das versões velhas,
então as versões boas restauradas precisam dele de novo.

- CSS: seletor `.dialogue-bubble .audio-inline svg, .oral-model .audio-inline svg`
  vira global `.audio-inline svg`
- SVG inline sem fill: <svg viewBox="0 0 24 24"> ganha fill=none stroke=currentColor
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FILES = [
    'public/professor/eduarda-gabriel.html',
    'public/professor/gabriela-paulucci.html',
    'public/professor/gabriela-pires.html',
    'public/professor/patricia-ruffo-aula1.html',
    'public/professor/patricia-ruffo-aula2.html',
    'public/professor/pricila-adamo-aula4.html',
    'public/professor/pricila-adamo-aula5.html',
    'public/professor/pricila-adamo.html',
    'public/professor/roberto-pires-aula1.html',
]

CSS_RE = re.compile(r'\.dialogue-bubble \.audio-inline svg,\s*\.oral-model \.audio-inline svg\s*')

for rel in FILES:
    f = ROOT / rel
    html = f.read_text(encoding='utf-8')
    html, n_css = CSS_RE.subn('.audio-inline svg ', html)
    n_svg = html.count('<svg viewBox="0 0 24 24">')
    html = html.replace(
        '<svg viewBox="0 0 24 24">',
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">',
    )
    f.write_text(html, encoding='utf-8')
    print(f'{rel}: css={n_css} svg={n_svg}')
