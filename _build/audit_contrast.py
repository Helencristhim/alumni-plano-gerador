#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditor de CONTRASTE — substitui a revisao manual slide-a-slide.
Varre arquivos HTML de material, isola os slides escuros (.slide-dark / .slide.dark)
e reporta:
  1. Se o contrast-guard.js (auto-fix em runtime) esta linkado  -> blindagem sistemica.
  2. Anti-padroes EXPLICITOS de contraste dentro de slide escuro (proibidos no rulebook):
       - color: var(--text) / var(--text-dim) / var(--text-mid)   (cinza escuro = some no escuro)
       - color: rgba(255,255,255,0.x)  (branco parcial = ilegivel)
       - color:#fff / white em elemento de TEXTO com fundo claro inline  (branco-no-branco, CENARIO A)

Uso:  python3 audit_contrast.py <arquivo.html> [arquivo2.html ...]
      python3 audit_contrast.py <worktree> <slug> <N>   (audita prof+aluno da aula N)
Sai 0 se nenhum anti-padrao residual; 1 se houver (mesmo com guard, vale corrigir a fonte).
"""
import sys, os, re
from html.parser import HTMLParser

BANNED_COLOR = re.compile(r'color\s*:\s*(var\(--text(?:-dim|-mid)?\)|rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0?\.\d+\s*\))', re.I)
LIGHT_BG = re.compile(r'background(?:-color)?\s*:\s*(#fff(?:fff)?\b|white\b|rgba\(\s*255\s*,\s*255\s*,\s*255)', re.I)
LIGHT_TEXT = re.compile(r'color\s*:\s*(#fff(?:fff)?\b|white\b)', re.I)

def style_of(attrs):
    for k, v in attrs:
        if k == 'style': return v or ''
    return ''
def classes_of(attrs):
    for k, v in attrs:
        if k == 'class': return (v or '').split()
    return []

class Auditor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # list of dicts per open tag
        self.darkdepth = 0       # >0 quando dentro de um slide escuro
        self.issues = []
        self.curtext_owner = None
    def is_dark(self, classes):
        cs = ' '.join(classes)
        return ('slide-dark' in cs) or ('slide' in classes and 'dark' in classes)
    def handle_starttag(self, tag, attrs):
        classes = classes_of(attrs); style = style_of(attrs)
        dark = self.is_dark(classes)
        if dark: self.darkdepth += 1
        node = {'tag': tag, 'style': style, 'classes': classes, 'haslightbg': bool(LIGHT_BG.search(style)),
                'lighttext': bool(LIGHT_TEXT.search(style)), 'hastext': False, 'dark_at_open': self.darkdepth}
        self.stack.append(node)
        if self.darkdepth > 0 and tag not in ('script', 'style', 'svg', 'path', 'polygon', 'polyline', 'rect', 'circle', 'line'):
            m = BANNED_COLOR.search(style)
            if m:
                self.issues.append(('banned-color', tag, m.group(0)[:60]))
    def handle_data(self, data):
        if self.darkdepth > 0 and data.strip() and self.stack:
            self.stack[-1]['hastext'] = True
    def handle_endtag(self, tag):
        # fecha ate o tag correspondente (tolerante a HTML imperfeito)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]['tag'] == tag:
                node = self.stack[i]
                # CENARIO A: elemento de texto com fundo claro inline, sem cor escura propria, em slide escuro
                if node['dark_at_open'] > 0 and node['hastext'] and node['haslightbg'] and not re.search(r'color\s*:\s*#?(1a1a2e|000|111|222|333)', node['style'], re.I):
                    self.issues.append(('white-on-light', tag, node['style'][:70]))
                if self.is_dark(node['classes']) and self.darkdepth > 0:
                    self.darkdepth -= 1
                del self.stack[i:]
                break

def audit(path):
    h = open(path, encoding='utf-8').read()
    guard = '/lib/contrast-guard.js' in h
    a = Auditor(); a.feed(h)
    ndark = len(re.findall(r'class="[^"]*slide-dark|class="slide dark', h))
    return guard, ndark, a.issues

def main():
    args = sys.argv[1:]
    files = []
    if len(args) == 3 and os.path.isdir(args[0]):
        wt, slug, n = args
        for side in ('professor', 'aluno'):
            p = os.path.join(wt, 'public', side, '%s-aula%s.html' % (slug, n))
            if os.path.exists(p): files.append(p)
    else:
        files = args
    if not files:
        print('uso: audit_contrast.py <arquivo.html ...>  |  <worktree> <slug> <N>'); sys.exit(2)
    total_issues = 0
    for f in files:
        guard, ndark, issues = audit(f)
        print('=' * 64)
        print('CONTRASTE —', f)
        print('  contrast-guard.js (auto-fix runtime):', 'SIM (blindado)' if guard else 'NAO')
        print('  slides escuros:', ndark)
        if not issues:
            print('  anti-padroes residuais: 0  -> OK')
        else:
            total_issues += len(issues)
            print('  anti-padroes residuais:', len(issues))
            for kind, tag, snippet in issues[:40]:
                print('    [%s] <%s>  %s' % (kind, tag, snippet))
    print('-' * 64)
    if total_issues == 0:
        print('VERDE — nenhum anti-padrao de contraste; sem revisao manual necessaria')
    else:
        print('AMARELO — %d anti-padroes (corrigir na fonte; guard ja cobre em runtime se presente)' % total_issues)
    sys.exit(1 if total_issues else 0)

if __name__ == '__main__':
    main()
