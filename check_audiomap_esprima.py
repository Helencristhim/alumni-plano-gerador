#!/usr/bin/env python3
# Validate the audioMap object literal in a hub HTML parses cleanly (no missing comma -> undefined var).
import re, sys
import esprima

def extract_audiomap(html):
    # find "var audioMap = { ... };" or "audioMap = {...}"
    m = re.search(r'audioMap\s*=\s*\{', html)
    if not m:
        return None
    start = m.end() - 1  # at the '{'
    depth = 0
    i = start
    in_str = None
    esc = False
    while i < len(html):
        ch = html[i]
        if in_str:
            if esc:
                esc = False
            elif ch == '\\':
                esc = True
            elif ch == in_str:
                in_str = None
        else:
            if ch in '"\'':
                in_str = ch
            elif ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    return html[start:i+1]
        i += 1
    return None

ok = True
for path in sys.argv[1:]:
    html = open(path, encoding='utf-8').read()
    obj = extract_audiomap(html)
    if obj is None:
        print(f'❌ {path}: audioMap not found'); ok = False; continue
    # normalize optional-chaining-ish keys not relevant; wrap as expression
    try:
        esprima.parseScript('var __m = ' + obj + ';')
        n = obj.count('": "') + obj.count("': '")
        print(f'✅ {path}: audioMap parses OK (~{n} entries)')
    except Exception as e:
        print(f'❌ {path}: audioMap PARSE ERROR: {e}'); ok = False

sys.exit(0 if ok else 1)
