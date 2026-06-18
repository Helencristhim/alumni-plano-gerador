#!/usr/bin/env python3
"""
fix_hub_orphans.py — conserta accordions/cards "órfãos" em hubs.

Bug: o insert_hub.py aditivo insere o novo card (Pre-class lesson-card no
tab-exercises, ou card IN CLASS no tab-inclass) IMEDIATAMENTE ANTES da abertura
do PRÓXIMO painel <div class="tab-content" id="...">. Mas o </div> que fecha o
painel atual fica logo antes dessa abertura. Resultado: o card novo entra DEPOIS
do fechamento do painel -> fica órfão (sibling dos painéis), sempre visível,
"vazando" pro complementary / controle.

Correção: para cada par de painéis tab-content adjacentes (A, B), se houver
conteúdo de elemento (<div) entre o fechamento de A e a abertura de B, realoca o
</div> de fechamento de A para logo antes da abertura de B (re-encapsulando os
órfãos dentro de A). Idempotente: no-op se já estiver correto.

Uso: python3 fix_hub_orphans.py <arquivo.html> [<arquivo.html> ...]
     python3 fix_hub_orphans.py --check <arquivo.html>   # só reporta, não edita
"""
import re
import sys

TOK = re.compile(r'<style\b|</style>|<script\b|</script>|<div\b[^>]*>|</div>', re.I)
PANEL_ID = re.compile(r'id="(tab-[a-z]+)"', re.I)


def find_panels(text):
    """Retorna [(id, open_start, close_end)] dos <div class=tab-content> via depth,
    ignorando <style>/<script>."""
    depth = 0
    instyle = inscript = False
    stack = []          # (depth_after_open, id, open_start)
    panels = []
    for m in TOK.finditer(text):
        tok = m.group(0)
        low = tok.lower()
        if low.startswith('<style'):
            instyle = True; continue
        if low.startswith('</style'):
            instyle = False; continue
        if low.startswith('<script'):
            inscript = True; continue
        if low.startswith('</script'):
            inscript = False; continue
        if instyle or inscript:
            continue
        if low.startswith('<div'):
            depth += 1
            pid = None
            if 'tab-content' in low:
                idm = PANEL_ID.search(tok)
                if idm:
                    pid = idm.group(1)
            stack.append((depth, pid, m.start()))
        elif low == '</div>':
            if stack:
                d, pid, start = stack.pop()
                if pid:
                    panels.append((pid, start, m.end()))
            depth -= 1
    panels.sort(key=lambda p: p[1])
    return panels


def fix_once(text):
    panels = find_panels(text)
    for i in range(len(panels) - 1):
        _, _, close_end = panels[i]
        nid, nopen, _ = panels[i + 1]
        between = text[close_end:nopen]
        if '<div' in between.lower():
            # realoca o </div> (6 chars) que está logo antes do 'between'
            close_start = close_end - len('</div>')
            assert text[close_start:close_end].lower() == '</div>'
            before = text[:close_start]
            moved = text[close_end:nopen].rstrip()
            after = text[nopen:]
            # indent do painel B p/ alinhar o </div> realocado
            line_start = before.rfind('\n') + 1
            new = before + moved + '\n</div>\n' + after
            return new, (panels[i][0], nid)
    return text, None


def process(path, check_only=False):
    text = open(path, encoding='utf-8').read()
    fixes = []
    cur = text
    while True:
        nxt, info = fix_once(cur)
        if info is None:
            break
        fixes.append(info)
        cur = nxt
    if not fixes:
        print(f"OK   {path} — sem órfãos")
        return False
    if check_only:
        print(f"VAZA {path} — órfãos entre: {fixes}")
        return True
    open(path, 'w', encoding='utf-8').write(cur)
    print(f"FIX  {path} — {len(fixes)} realocação(ões): {fixes}")
    return True


def main():
    args = sys.argv[1:]
    check = '--check' in args
    files = [a for a in args if a != '--check']
    any_bad = False
    for f in files:
        any_bad |= process(f, check_only=check)
    sys.exit(1 if (check and any_bad) else 0)


if __name__ == '__main__':
    main()
