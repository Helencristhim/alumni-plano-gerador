#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_preclass_coherence.py — GATE de coerencia Pre-class <-> aula IN CLASS (REGRA 29).

As 4 abas de uma aula (Planning / Pre-class / IN CLASS / Complementares) DEVEM falar
da MESMA aula: mesmo TEMA, mesma GRAMATICA, mesmo VOCAB. O Pre-class PREVIEWA a aula —
nao e uma aula diferente. Quando a Helen edita o hub a mao, o bloco Pre-class
(id="ex-lesson-N" em {slug}.html) as vezes fica com tema/gramatica/vocab de OUTRA aula,
diferente do IN CLASS standalone ({slug}-aulaN.html). Incidente real: sandra-hayasaki
aula 5 — IN CLASS = "My Life in 3 Minutes" (vocab Grow up/Background/Turning point...) mas
o Pre-class do hub = "Review — My Life in 3 Minutes" (vocab Confident/Fluent/Improve...).

Para cada par (hub, aula N) o gate extrai e compara:
  IN CLASS  ({slug}-aulaN.html):  titulo (<title> ... Aula N -- TITULO), vocab dos
                                  reveal cards (.card-word / .vocab-card-word / .v-word),
                                  e gramatica da regiao "Grammar Discovery / Reveal the Rule
                                  / Language Focus".
  Pre-class (bloco id="ex-lesson-N" no hub): titulo (<h3>), vocab preview
                                  (.vocab-card-word) e gramatica do bloco "Grammar Tip".

HARD FAIL (exit !=0) se, fora uma aula de REVIEW:
  (c) VOCAB   — sobreposicao de vocab entre Pre-class e aula e ZERO (Pre-class deveria
                previewar o vocab da aula). Este e o sinal mais FORTE e de alta precisao:
                pega o caso Sandra e nunca reprova as coerentes (vocab batendo). OU
  (a+b) TITULO **e** GRAMATICA divergentes ao mesmo tempo, quando o vocab nao e legivel
                (markup a mao) — dois sinais independentes juntos => incoerente.

WARN (reportado, nao bloqueia sozinho) se SO o TITULO **ou** SO a GRAMATICA diverge:
  titulos narrativos do IN CLASS ("The Engine", "From Lab") sao de proposito diferentes do
  titulo literal do Pre-class ("Running a Meeting") sem serem incoerentes, e termos
  gramaticais genericos aparecem soltos no texto — por isso, sozinhos, sao so um aviso.

Aulas de REVIEW/consolidacao (titulo da AULA contem review/revisao/recap/checkpoint/
wrap-up/consolidat) sao EXCECAO — remixam vocab de proposito — e passam. A excecao olha
o titulo da AULA (IN CLASS), nao do Pre-class: se a aula e conversa mas o Pre-class diz
"Review", ISSO e o bug que queremos pegar.

Heuristica tolerante a markup variado (Helen escreve a mao): se um lado nao tem vocab/
gramatica detectavel, aquele sub-check e PULADO (indeterminado), nunca falsa-reprova.

USO:
  python3 _build/model/check_preclass_coherence.py public/professor/sandra-hayasaki.html
      -> audita TODOS os pares (ex-lesson-N + standalone aulaN) do aluno
  python3 _build/model/check_preclass_coherence.py public/professor/sandra-hayasaki-aula5.html
      -> casa com o hub {slug}.html no mesmo dir e checa so a aula 5
  python3 _build/model/check_preclass_coherence.py 'public/professor/*.html'   # roster inteiro
  python3 _build/model/check_preclass_coherence.py --selftest
Exit 1 se algum par for incoerente.
"""
import glob
import html
import os
import re
import sys
from collections import defaultdict

# Classes de "reveal card" de vocabulario emitidas pelo builder / legados da Helen.
# (match-word/pron-word/comp-words NAO sao vocab ensinado — ficam de fora de proposito.)
VOCAB_RE = re.compile(r'class="(?:card-word|vocab-card-word|v-word)"[^>]*>([^<]+)<')

# Termos gramaticais canonicos (mais longos primeiro p/ subsuncao presente perfect cont.).
GRAMMAR_TERMS = [
    'present perfect continuous', 'present perfect simple', 'past perfect continuous',
    'present perfect', 'past perfect', 'present continuous', 'past continuous',
    'future continuous', 'future perfect', 'present simple', 'past simple',
    'zero conditional', 'first conditional', 'second conditional', 'third conditional',
    'mixed conditional', 'conditional', 'passive voice', 'passive', 'reported speech',
    'relative clause', 'defining relative', 'comparative', 'superlative', 'modal verb',
    'modals', 'modal', 'phrasal verb', 'gerund', 'infinitive', 'countable', 'uncountable',
    'quantifier', 'imperative', 'tag question', 'question word', 'used to', 'going to',
    'can / could', 'have to',
]

REVIEW_RE = re.compile(r'review|revis[aã]o|recap|checkpoint|wrap-?up|consolidat', re.I)

TITLE_STOP = {
    'the', 'and', 'a', 'an', 'to', 'of', 'in', 'on', 'at', 'for', 'with', 'your', 'you',
    'my', 'is', 'are', 'be', 'it', 'this', 'that', 'aula', 'lesson', 'pre-class', 'preclass',
    'conversation', 'professor', 'view', 'part', 'i', 'ii', 'iii', 'iv',
}


def norm(w):
    w = html.unescape(w)
    w = re.sub(r'\s+', ' ', w).strip().lower()
    return w.strip('.,;:!?"\'()[]-—–·*')


def vocab_set(blob):
    out = set()
    for m in VOCAB_RE.findall(blob):
        n = norm(m)
        # descarta lixo de JS / strings longas que escaparam (vocab e curto)
        if n and len(n) <= 32 and not re.search(r'[{}()=;|\\"/]|&&|::', n):
            out.add(n)
    return out


def title_keywords(title):
    toks = re.findall(r"[a-z0-9]+", html.unescape(title).lower())
    return {t for t in toks if t not in TITLE_STOP and len(t) >= 3}


def grammar_terms(text):
    low = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html.unescape(text))).lower()
    found = set()
    for t in GRAMMAR_TERMS:
        if t in low:
            found.add(t)
    return found


def grammar_related(a, b):
    """Coerente se algum termo de A se relaciona com algum de B (igual ou substring —
    'present perfect' ~ 'present perfect continuous')."""
    for x in a:
        for y in b:
            if x == y or x in y or y in x:
                return True
    return False


def region_grammar(text, anchors, window=1800):
    low = text.lower()
    pos = min([p for p in (low.find(a) for a in anchors) if p >= 0], default=-1)
    if pos < 0:
        return set()
    return grammar_terms(text[pos:pos + window])


# ---------- extracao IN CLASS (standalone) ----------

def std_title(c):
    m = re.search(r'<title>([^<]*)</title>', c)
    t = m.group(1) if m else ''
    mm = re.search(r'Aula\s*\d+\s*[-–—]+\s*(.+)$', t)
    if mm:
        return mm.group(1).strip()
    st = re.search(r'class="slide-title"[^>]*>([^<]+)', c)
    return (st.group(1) if st else t).strip()


def std_grammar(c):
    return region_grammar(c, ['reveal the rule', 'grammar discovery', 'language focus',
                              'the code', 'diving deep'])


# ---------- extracao Pre-class (bloco do hub) ----------

def hub_blocks(hub_html):
    """-> dict {lesson_no: block_html} a partir do hub."""
    ids = [(m.start(), int(m.group(1)))
           for m in re.finditer(r'id="ex-lesson-(\d+)"', hub_html)]
    ids.sort()
    out = {}
    for i, (pos, n) in enumerate(ids):
        end = ids[i + 1][0] if i + 1 < len(ids) else len(hub_html)
        out[n] = hub_html[pos:end]
    return out


def hub_title(block):
    m = re.search(r'<h3[^>]*>(.*?)</h3>', block, re.S)
    return html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else ''


def hub_grammar(block):
    return region_grammar(block, ['grammar tip'], window=1400)


# ---------- comparacao de um par ----------

def check_pair(std_html, hub_block, n, slug=''):
    """-> (status, reasons). status in {'PASS','FAIL','WARN','SKIP','REVIEW'}.
    reasons traz os sinais; FAIL bloqueia, WARN so reporta."""
    st_title = std_title(std_html)
    pc_title = hub_title(hub_block)
    st_vocab = vocab_set(std_html)
    pc_vocab = vocab_set(hub_block)
    st_gram = std_grammar(std_html)
    pc_gram = hub_grammar(hub_block)

    if not pc_title and not pc_vocab:
        return 'SKIP', ['Pre-class sem titulo/vocab detectavel (markup nao reconhecido)']

    # excecao: a AULA (IN CLASS) e uma revisao -> remix de vocab e legitimo
    if REVIEW_RE.search(st_title):
        return 'REVIEW', [f'aula de review/consolidacao ("{st_title}") — coerencia de vocab dispensada']

    st_kw, pc_kw = title_keywords(st_title), title_keywords(pc_title)
    vocab_known = bool(st_vocab and pc_vocab)
    vocab_disjoint = vocab_known and not (st_vocab & pc_vocab)
    title_div = bool(st_kw and pc_kw and not (st_kw & pc_kw))
    gram_div = bool(st_gram and pc_gram and not grammar_related(st_gram, pc_gram))

    title_msg = (f'TITULO divergente — IN CLASS "{st_title}" vs Pre-class "{pc_title}" '
                 '(zero palavra-chave em comum)')
    gram_msg = f'GRAMATICA divergente — aula={sorted(st_gram)} vs Pre-class={sorted(pc_gram)}'

    reasons, warns = [], []

    # (c) VOCAB disjunto = HARD FAIL (alta precisao, pega o caso Sandra)
    if vocab_disjoint:
        reasons.append('VOCAB disjunto — Pre-class nao previewa o vocab da aula.\n'
                       f'        IN CLASS: {sorted(st_vocab)}\n'
                       f'        Pre-class: {sorted(pc_vocab)}')
        if title_div:
            reasons.append(title_msg)
        if gram_div:
            reasons.append(gram_msg)
        return 'FAIL', reasons

    # (a+b) sem vocab legivel, mas TITULO **e** GRAMATICA divergem juntos = HARD FAIL
    if not vocab_known and title_div and gram_div:
        return 'FAIL', [title_msg, gram_msg]

    # sinais isolados -> WARN (reportado, nao bloqueia)
    if title_div:
        warns.append(title_msg)
    if gram_div:
        warns.append(gram_msg)
    return ('WARN' if warns else 'PASS'), warns


# ---------- descoberta de pares a partir dos args ----------

def discover_pairs(args):
    """-> list de (slug, n, std_path, hub_path)."""
    files = []
    for a in args:
        files.extend(sorted(glob.glob(a)) or [a])
    pairs = {}
    for f in files:
        f = f.replace('\\', '/')
        if not os.path.exists(f):
            print(f'aviso: arquivo nao existe: {f}', file=sys.stderr)
            continue
        d = os.path.dirname(f)
        base = os.path.basename(f)
        m = re.match(r'(.+?)-aula(\d+)\.html$', base)
        if m:                                   # standalone -> casa com hub
            slug, n = m.group(1), int(m.group(2))
            hub = os.path.join(d, slug + '.html')
            if os.path.exists(hub):
                pairs[(slug, n)] = (f, hub)
            continue
        slug = base[:-5]
        if slug.endswith('-aluno') or '-aula' in slug:
            continue
        hub_html = open(f, encoding='utf-8').read()       # hub -> todos os pares
        for n in hub_blocks(hub_html):
            std = os.path.join(d, f'{slug}-aula{n}.html')
            if os.path.exists(std):
                pairs[(slug, n)] = (std, f)
    return [(s, n, p[0], p[1]) for (s, n), p in pairs.items()]


def main():
    raw = sys.argv[1:]
    if not raw:
        print(__doc__)
        sys.exit(2)
    if '--selftest' in raw:
        sys.exit(selftest())

    pairs = discover_pairs(raw)
    if not pairs:
        print('nenhum par hub/aula encontrado nos argumentos.')
        sys.exit(2)

    by_slug = defaultdict(list)
    for slug, n, std_path, hub_path in pairs:
        by_slug[slug].append((n, std_path, hub_path))

    fails = warns = 0
    hub_cache = {}
    for slug in sorted(by_slug):
        for n, std_path, hub_path in sorted(by_slug[slug]):
            std_html = open(std_path, encoding='utf-8').read()
            if hub_path not in hub_cache:
                hub_cache[hub_path] = hub_blocks(open(hub_path, encoding='utf-8').read())
            block = hub_cache[hub_path].get(n)
            if block is None:
                continue
            status, reasons = check_pair(std_html, block, n, slug)
            if status == 'FAIL':
                fails += 1
                print(f'FAIL  {slug} aula {n}')
                for r in reasons:
                    print(f'    - {r}')
            elif status == 'WARN':
                warns += 1
                print(f'WARN  {slug} aula {n}')
                for r in reasons:
                    print(f'    ~ {r}')
    if warns:
        print(f'\n({warns} aviso(s) WARN — sinal isolado de titulo/gramatica, nao bloqueia)')
    if fails:
        print(f'\n=== REGRA 29 VIOLADA: {fails} aula(s) com Pre-class incoerente — '
              'corrigir o bloco ex-lesson antes de mergear ===')
        sys.exit(1)
    print(f'OK: {len(pairs)} par(es) hub/aula sem incoerencia bloqueante (REGRA 29).')
    sys.exit(0)


# ---------- selftest (sem depender do repo) ----------

INCOHERENT_STD = '''<title>Professor View | Aula 5 -- My Life in 3 Minutes</title>
<div class="vocab-grid">
  <div class="card-word">Grow up</div><div class="card-word">Background</div>
  <div class="card-word">Turning point</div><div class="card-word">Milestone</div>
</div>
<div>Reveal the Rule</div> Language Focus: telling a story with the past simple.'''

INCOHERENT_HUB = '''<div class="lesson-card" id="ex-lesson-5">
  <h3>Review -- The Block 1 Toolkit</h3>
  <div class="vocab-card-word">Confident</div><div class="vocab-card-word">Fluent</div>
  <div class="vocab-card-word">Improve</div><div class="vocab-card-word">Proud</div>
  <h4>Grammar Tip</h4> A review of the four tenses, present perfect and present simple.
</div>'''

COHERENT_STD = '''<title>Professor View | Aula 3 -- Status Updates</title>
<div class="vocab-grid">
  <div class="card-word">Update</div><div class="card-word">Blocker</div>
  <div class="card-word">Pending</div><div class="card-word">Ongoing</div>
</div>
<div>Grammar Discovery</div> Present continuous vs present simple for status updates.'''

COHERENT_HUB = '''<div class="lesson-card" id="ex-lesson-3">
  <h3>Status Updates &amp; Ongoing Work</h3>
  <div class="vocab-card-word">Update</div><div class="vocab-card-word">Blocker</div>
  <div class="vocab-card-word">Pending</div><div class="vocab-card-word">Ongoing</div>
  <h4>Grammar Tip -- Present Continuous vs Present Simple</h4> ...
</div>'''

REVIEW_STD = '''<title>Professor View | Aula 10 -- Checkpoint Review</title>
<div class="card-word">Anything</div><div class="card-word">Goes</div>
<div>Language Focus</div> mixed tenses.'''


def selftest():
    cases = [
        ('incoerente (caso Sandra)', INCOHERENT_STD, INCOHERENT_HUB, 5, 'FAIL'),
        ('coerente (status updates)', COHERENT_STD, COHERENT_HUB, 3, 'PASS'),
        ('aula de review (excecao)', REVIEW_STD, INCOHERENT_HUB, 10, 'REVIEW'),
    ]
    ok = True
    for name, std, hub, n, expect in cases:
        status, reasons = check_pair(std, hub, n)
        good = status == expect
        ok = ok and good
        print(f'[{"ok" if good else "XX"}] {name}: esperado {expect}, obteve {status}')
        if not good:
            for r in reasons:
                print('       ', r)
    print('SELFTEST', 'PASS' if ok else 'FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    main()
