#!/usr/bin/env python3
"""Porte Python do build-lesson-counts.js (node não existe no ambiente de dev).

Varre public/professor/*.html e conta as aulas REAIS por aluno:
  total = nº de id="ex-lesson-" no hub + standalones {slug}-aulaN.html com N
          acima do maior ex-lesson-N do hub.
Gera public/data/lesson-counts.json (mesmo formato do script node).

Uso: python3 scripts/build_lesson_counts.py
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROF_DIR = ROOT / 'public' / 'professor'
OUT_FILE = ROOT / 'public' / 'data' / 'lesson-counts.json'

SKIP_PATTERNS = [
    r'-aula\d', r'-backup', r'-test', r'-v-[ab]', r'V2\.', r'-new-?aula',
    r'-new\.', r'-listening\.', r'-palestra\.', r'-speech-training\.',
    r'^helen-mendes\.',  # aluna MOCK (modelo de template) — não entra no controle
]
STANDALONE_AULA_RE = re.compile(r'^(.+)-aula(\d+)\.html$')


def is_main_file(name):
    return not any(re.search(p, name) for p in SKIP_PATTERNS)


def extract_name(html, slug):
    m = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
    if m:
        return m.group(1).strip()
    return ' '.join(w.capitalize() for w in slug.split('-'))


def main():
    all_files = sorted(f.name for f in PROF_DIR.glob('*.html'))
    standalone = {}
    for f in all_files:
        m = STANDALONE_AULA_RE.match(f)
        if m:
            standalone.setdefault(m.group(1), []).append(int(m.group(2)))

    results = []
    for fname in all_files:
        if not is_main_file(fname):
            continue
        slug = fname[:-5]
        html = (PROF_DIR / fname).read_text(encoding='utf-8', errors='replace')
        lesson_count = len(re.findall(r'id="ex-lesson-', html))
        nums_in_main = [int(n) for n in re.findall(r'id="ex-lesson-(\d+)"', html)]
        max_in_main = max(nums_in_main, default=0)
        extra = [n for n in standalone.get(slug, []) if n > max_in_main]
        total = lesson_count + len(extra)
        if total == 0:
            continue
        results.append({
            'slug': slug,
            'name': extract_name(html, slug),
            'aulasHtml': total,
        })

    results.sort(key=lambda r: r['name'].lower())
    out = {
        'generatedAt': datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
        'students': results,
    }
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Generated {OUT_FILE.relative_to(ROOT)} with {len(results)} students')
    return 0


if __name__ == '__main__':
    sys.exit(main())
