#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE — handler inline que chama FUNÇÃO INDEFINIDA (botão morto silencioso).

O GATE 7 (check_inline_js) só COMPILA o handler no V8 — pega erro de SINTAXE. Um
`onclick="verifyAllMatches('x')"` compila liso mesmo se `verifyAllMatches` NÃO existe;
só quebra no CLIQUE (ReferenceError), invisível pra todo mundo. Foi assim que o botão
"Check Answers" morto ficou escondido em 1400+ hubs. Este gate fecha esse buraco:
casa cada função CHAMADA num handler (`on*=`) com uma DEFINIÇÃO no <script> inline do
arquivo; a que não bate = botão morto.

LEGADO-TOLERANTE (padrão GATE 6/7): compara com a versão-base (origin/main). Arquivo NOVO
= tolerância zero (qualquer indefinida = FAIL). Arquivo MODIFICADO = só falha se PIOROU
(mais funções indefinidas que na base). O legado dos 1400 hubs não dispara nem exige retrofit.

USO: python3 scripts/check_undefined_handlers.py [--base REF] <arquivo.html> [...]
"""
import re, sys, os, subprocess, html as _html

# Builtins/keywords que aparecem como `nome(` mas NÃO são função de usuário no <script> do hub.
ALLOW = set('''if for while switch catch return typeof void new delete in of do else
    function alert confirm prompt setTimeout setInterval clearTimeout parseInt parseFloat
    isNaN Number String Boolean Array Object JSON Math Date RegExp Promise Set Map
    encodeURIComponent decodeURIComponent requestAnimationFrame
    rgb rgba hsl hsla var calc url min max clamp attr
    translate translateX translateY translate3d translateZ scale scaleX scaleY scale3d
    rotate rotateX rotateY rotateZ skew skewX skewY matrix matrix3d perspective
    linear-gradient radial-gradient conic-gradient repeating-linear-gradient
    blur brightness contrast grayscale invert saturate sepia opacity drop-shadow cubic-bezier'''.split())

CALL   = re.compile(r'(?<![.\w$])([A-Za-z_$][\w$]*)\s*\(')          # ident( não precedido de . ou \w
HANDLER= re.compile(r'on[a-z]+\s*=\s*"([^"]*)"')                    # on*="..." (aspas duplas — padrão do repo)
DEFS   = [re.compile(p) for p in (
    r'function\s+([A-Za-z_$][\w$]*)',
    r'\b(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=',
    r'window\.([A-Za-z_$][\w$]*)\s*=',
    r'([A-Za-z_$][\w$]*)\s*=\s*function',
)]

def scripts_inline(h):
    """concatena só os <script> SEM src (o JS que roda inline no arquivo)."""
    out = []
    for m in re.finditer(r'<script\b([^>]*)>(.*?)</script\s*>', h, re.S | re.I):
        if not re.search(r'\bsrc\s*=', m.group(1)):
            out.append(m.group(2))
    return '\n'.join(out)

def undefined_in(h):
    js = scripts_inline(h)
    defined = set()
    for rx in DEFS:
        defined |= set(rx.findall(js))
    called = set()
    for hm in HANDLER.finditer(h):
        for fn in CALL.findall(_html.unescape(hm.group(1))):
            called.add(fn)
    return {f for f in called if f not in defined and f not in ALLOW}

def base_version(ref, path):
    try:
        return subprocess.check_output(['git', 'show', f'{ref}:{path}'],
                                       stderr=subprocess.DEVNULL).decode('utf-8', 'replace')
    except subprocess.CalledProcessError:
        return None  # arquivo novo

def main():
    args = sys.argv[1:]
    ref = 'origin/main'
    if '--base' in args:
        i = args.index('--base'); ref = args[i+1]; del args[i:i+2]
    files = [a for a in args if a.endswith('.html') and os.path.exists(a)]
    fails = []
    for f in files:
        cur = undefined_in(open(f, encoding='utf-8').read())
        if not cur:
            continue
        base_src = base_version(ref, f)
        base = undefined_in(base_src) if base_src is not None else set()
        novos = cur - base                     # só o que PIOROU (ou tudo, se arquivo novo)
        if novos:
            fails.append((f, sorted(novos)))
    if fails:
        print("⛔ HANDLER CHAMANDO FUNÇÃO INDEFINIDA (botão morto — quebra no clique, gate 7 não pega):")
        for f, fns in fails:
            for fn in fns:
                print(f"   {os.path.basename(f)}: on*=\"{fn}(...)\" mas `function {fn}` não existe no <script> do arquivo")
        print(f"\n{sum(len(x[1]) for x in fails)} handler(s) morto(s) NOVO(s). Defina a função no arquivo (ou no modelo helen-mendes, se for função de shell).")
        sys.exit(1)
    print(f"✓ handlers OK ({len(files)} arquivo(s)) — nenhuma função indefinida nova")

if __name__ == '__main__':
    main()
