#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE — a Pre-class PREPARA a aula; nao repete os exercicios dela.

DE ONDE VEIO
------------
Feedback do professor Andre Marinho, 22/09/2026, sobre a aula 2 do Guilherme:
"dei uma olhada no pre class do material e esta exatamente a mesma coisa; pre
class e licao sao exatamente a mesma coisa". Estava mesmo: 53 dos 69 itens de
exercicio eram identicos nas duas telas, porque as duas superficies liam o mesmo
arquivo de conteudo. O aluno fazia a prova em casa e refazia a MESMA prova, com
os mesmos itens, na aula.

A regra ja existia e ninguem a executava:
  docs/REGRAS-138-A-146.md:184  "PROIBIDO: Material do Professor repetindo os
                                MESMOS exercicios do Pre-class"
  docs/REGRAS-119-A-137.md:122  "Mesmo vocabulario, APLICACOES TOTALMENTE
                                DIFERENTES nas 3 pecas"
  docs/RULEBOOK-PEDAGOGICO.md:203  "Pre-class prepara, aula aprofunda"

O GATE 61 (check_preclass_nao_entrega.py) e vizinho mas mede outra coisa: ele
impede que a pre-class entregue o TRANSCRIPT do audio. Nao mede exercicio, e diz
isso de si mesmo.

O QUE ELE NAO MEDE
------------------
VOCABULARIO. A REGRA 1 EXIGE que a pre-class previeja o lexico da aula: palavra,
definicao e frase de exemplo repetem de proposito, e o proprio professor liberou
("ate o 2.3 pode ficar como esta, porque e so matching de vocabulario"). Por isso
tudo que aparece como vocabulario no hub e DESCONTADO dos dois lados antes de
comparar. O que sobra e tarefa: enunciado, opcao, lacuna, afirmacao.

O TETO, E POR QUE ELE E RELATIVO
--------------------------------
Medido nos 1.924 pares (hub, aula) que existem hoje: a MEDIANA e 0% e a media e
5,2%. Aula sa marca zero. Mas 257 pares passam de 10%, e alguns marcam 100% --
gente que nao e o Guilherme, com a mesma pergunta de compreensao e as mesmas
opcoes nas duas telas. O problema e mais velho e mais largo do que esta aula.

Por isso o gate e de REGRESSAO, e nao um teto absoluto. Ele compara com a base
(origin/main):

  aula que ja existe  -> reprova se a sobreposicao AUMENTAR
  aula nova           -> reprova se passar de 15%

Assim ninguem e obrigado a consertar divida que nao e sua para mergear, e ao
mesmo tempo nao entra defeito novo nem piora o que ja esta ruim. As 257 ficam
para um levantamento proprio; estao listadas por `--all`.

USO
---
  python3 scripts/check_preclass_nao_repete.py --selftest
  python3 scripts/check_preclass_nao_repete.py --base origin/main <arquivos mudados...>
  python3 scripts/check_preclass_nao_repete.py --all
"""
import html
import os
import re
import subprocess
import sys
import unicodedata

TETO = 0.15              # so para aula NOVA; aula que ja existe e medida contra a base
TOLERANCIA = 0.02        # ruido de reformatacao nao e regressao
MIN_PALAVRAS = 5          # item curto e rotulo, nao tarefa
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# tarefa: o que o aluno tem de resolver
SEL_TAREFA = [
    r'class="ic-choice"[^>]*>(.*?)</div>\s*</div>',
    r'class="ic-lf"[^>]*>(.*?)</div>',
    r'class="q-text"[^>]*>(.*?)</div>',
    r'class="ic-stmt"[^>]*>(.*?)</span>',
    r'class="fill-item"[^>]*>(.*?)</div>',
    r'class="cpe-sent"[^>]*>(.*?)</div>\s*</div>',
    r'class="ic-chip ic-def"[^>]*>.*?</span><span>(.*?)</span>',
    r'class="quiz-question"[^>]*>(.*?)</div>',
    r'class="quiz-option"[^>]*>(.*?)</div>',
    r'class="fill-blank-sentence"[^>]*>(.*?)</div>',
    r'class="ic-card-h3"[^>]*>(.*?)</div>',
    r'class="ic-gaptext"[^>]*>(.*?)</div>',
]
# vocabulario: repete de proposito (REGRA 1), sai da conta dos dois lados
SEL_VOCAB = [
    r'class="vocab-card-word"[^>]*>(.*?)</div>',
    r'class="vocab-card-def"[^>]*>(.*?)</div>',
    r'class="vocab-card-example"[^>]*>(.*?)</div>',
    r'class="card-word"[^>]*>(.*?)</div>',
    r'class="card-def"[^>]*>(.*?)</div>',
    r'class="card-example"[^>]*>(.*?)</div>',
    r'class="match-word"[^>]*>(.*?)</',
    r'class="sp-en"[^>]*>(.*?)</span>',
    r'class="survival-phrase"[^>]*>(.*?)</div>',
    r'data-answer="([^"]*)"',
    r'<option[^>]*>(.*?)</option>',
]


def norm(s):
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    s = unicodedata.normalize('NFKD', s).lower()
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', s)).strip()


def colhe(texto, seletores):
    out = set()
    for sel in seletores:
        for m in re.findall(sel, texto, re.S):
            t = norm(m)
            if len(t.split()) >= MIN_PALAVRAS:
                out.add(t)
    return out


def bloco_preclass(hub, n):
    """Só a aula N dentro do hub: o hub carrega TODAS as aulas do aluno, e um
    item da aula 5 casaria com o deck da aula 5 sem isso ter nada a ver."""
    m = re.search(r'id="ex-lesson-%d"' % n, hub)
    if not m:
        return None
    f = re.search(r'id="ex-lesson-%d"' % (n + 1), hub)
    return hub[m.start(): f.start() if f else len(hub)]


def mede(hub_txt, deck_txt, n):
    bloco = bloco_preclass(hub_txt, n)
    if bloco is None:
        return None
    deck_txt = re.sub(r'data-teacher="[^"]*"', '', deck_txt)
    vocab = colhe(bloco, SEL_VOCAB) | colhe(deck_txt, SEL_VOCAB)
    tarefas_deck = colhe(deck_txt, SEL_TAREFA) - vocab
    pre = norm(bloco)
    repete = {t for t in tarefas_deck if t in pre}
    if not tarefas_deck:
        return 0.0, 0, 0, []
    return len(repete) / len(tarefas_deck), len(repete), len(tarefas_deck), sorted(repete)[:5]


def da_base(base, caminho):
    """O arquivo como ele esta na base. None se nao existe la (aula nova)."""
    rel = os.path.relpath(os.path.abspath(caminho), RAIZ)
    r = subprocess.run(['git', 'show', '%s:%s' % (base, rel)],
                       capture_output=True, text=True, cwd=RAIZ)
    return r.stdout if r.returncode == 0 else None


def pares(arquivos):
    """(slug, n, caminho do hub, caminho do deck) para cada aula tocada."""
    vistos = set()
    for f in arquivos:
        m = re.search(r'public/(?:professor|aluno)/([a-z0-9-]+?)(?:-aula(\d+))?\.html$', f)
        if not m:
            continue
        slug, n = m.group(1), m.group(2)
        ns = [int(n)] if n else None
        hub = os.path.join(RAIZ, 'public', 'professor', slug + '.html')
        if not os.path.exists(hub):
            continue
        if ns is None:
            h = open(hub, encoding='utf-8').read()
            ns = sorted(int(x) for x in set(re.findall(r'id="ex-lesson-(\d+)"', h)))
        for k in ns:
            deck = os.path.join(RAIZ, 'public', 'professor', '%s-aula%d.html' % (slug, k))
            if os.path.exists(deck) and (slug, k) not in vistos:
                vistos.add((slug, k))
                yield slug, k, hub, deck


def selftest():
    """Prova que o gate ainda morde: um par sintetico 100% repetido tem de
    reprovar, e um par sem repeticao tem de passar."""
    frase = 'the development bank agreed to take the first loss on the solar cluster'
    outra = 'the committee met twice before it approved the revised traffic forecast'
    deck = '<div class="q-text">%s</div>' % frase
    hub_mau = '<div id="ex-lesson-1"><div class="quiz-question">%s</div></div>' % frase
    hub_bom = '<div id="ex-lesson-1"><div class="quiz-question">%s</div></div>' % outra
    mau = mede(hub_mau, deck, 1)
    bom = mede(hub_bom, deck, 1)
    assert mau and mau[0] == 1.0, 'selftest: repeticao total deveria dar 100%%, deu %s' % (mau,)
    assert bom and bom[0] == 0.0, 'selftest: par limpo deveria dar 0%%, deu %s' % (bom,)
    # e o vocabulario NAO pode contar
    hub_vocab = ('<div id="ex-lesson-1"><div class="vocab-card-def">%s</div>'
                 '<div class="quiz-question">%s</div></div>' % (frase, frase))
    deck_vocab = '<div class="ic-chip ic-def" data-k="A"><span>A</span><span>%s</span></div>' % frase
    v = mede(hub_vocab, deck_vocab, 1)
    assert v and v[0] == 0.0, 'selftest: vocabulario nao pode contar, deu %s' % (v,)
    print('selftest OK — o gate morde repeticao de tarefa e ignora vocabulario.')


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if '--selftest' in sys.argv:
        selftest()
        return 0
    if '--all' in sys.argv:
        d = os.path.join(RAIZ, 'public', 'professor')
        args = [os.path.join('public/professor', f) for f in os.listdir(d)
                if f.endswith('.html') and '-aula' not in f]
    if not args:
        print('GATE pre-class nao repete: nenhum arquivo para checar — OK')
        return 0

    base = None
    for a in sys.argv[1:]:
        if a.startswith('--base'):
            base = a.split('=', 1)[1] if '=' in a else None
    if base is None and '--base' in sys.argv:
        i = sys.argv.index('--base')
        if i + 1 < len(sys.argv):
            base = sys.argv[i + 1]
            args = [x for x in args if x != base]

    ruins, checados = [], 0
    for slug, n, hub_p, deck_p in pares(args):
        hub_txt = open(hub_p, encoding='utf-8').read()
        deck_txt = open(deck_p, encoding='utf-8').read()
        r = mede(hub_txt, deck_txt, n)
        if r is None:
            continue
        pct, rep, tot, exemplos = r
        checados += 1

        antes = None
        if base:
            hb, db = da_base(base, hub_p), da_base(base, deck_p)
            if hb is not None and db is not None:
                rb = mede(hb, db, n)
                antes = rb[0] if rb else None

        if antes is None:                       # aula nova: vale o teto
            ruim = pct > TETO
            nota = 'aula nova, teto %d%%' % round(100 * TETO)
        else:                                   # ja existia: vale a regressao
            ruim = pct > antes + TOLERANCIA
            nota = 'na base era %d%%' % round(100 * antes)

        if ruim:
            ruins.append((slug, n, pct, rep, tot, exemplos, nota))
        if ruim or pct > 0.15:
            print('%s %-38s aula %-2d  %3d%%  (%d de %d itens de tarefa)  %s'
                  % ('\u274c' if ruim else '  ', slug, n, round(100 * pct), rep, tot, nota))

    print('\n=== pre-class x in class: %d aula(s) checada(s)%s ==='
          % (checados, (' — base %s' % base) if base else ''))
    if not ruins:
        print('OK — nenhuma pre-class repete os exercicios da sua aula.')
        return 0
    print('\nREPROVADO. A pre-class PREPARA a aula, nao a repete (REGRA 146).')
    for slug, n, pct, rep, tot, exemplos, nota in ruins:
        print('\n  %s, aula %d: %d%% dos itens de tarefa do deck ja estao na pre-class '
              '(%d de %d; %s).' % (slug, n, round(100 * pct), rep, tot, nota))
        for e in exemplos:
            print('      - %s' % e[:96])
    print('\n  Conserto: itens DIFERENTES na pre-class, sobre o mesmo lexico e a mesma')
    print('  gramatica. Vocabulario pode repetir; tarefa, nao.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
