#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 22 — a ESPINHA da aula: etapas declaradas, telas dentro delas, minutos que fecham.

POR QUE ISTO EXISTE (11/08/2026)
--------------------------------
A unidade que quem conduz a aula enxerga NAO e a tela, e a ETAPA: 7 ou 8 delas, cada uma
agrupando de 1 a 6 telas, com o orcamento de minutos no rotulo. E o que o artefato de
referencia faz (stage-bar + stage-labels + data-stage por tela).

O molde PERDEU essa camada no porte, e ninguem viu: `data-stage`=0, `stage-seg`=0,
`stage-label`=0 nas quatro aulas publicadas. Sem o agrupamento, 15-18 telas leem como fila
linear de passos indistintos — e foi exatamente isso que o Dan abriu e estranhou
("ta com 16 slides...... nao foi assim que eu te criei"). O numero de telas estava certo;
o que faltava era a camada que as AGRUPA.

A espinha voltou no mesmo dia. Este gate existe para que ela nao possa sumir de novo em
silencio: `_build/model/anatomias.json -> estrutura._o_que_da_para_cobrar` listou as
quatro checagens em 11/08/2026 e registrou "levantado, NAO construido". Isto e a
construcao.

O QUE ELE COBRA
---------------
  (a) TODA tela tem `data-phase` — mapa com buraco e pior que mapa velho: o builder
      desiste de regenerar `slidePhases` e a barra passa a acender a etapa da OUTRA aula.
  (b) todo `data-phase` cai dentro do numero de etapas declaradas na barra.
  (c) sao 7 ou 8 etapas. NAO da para exigir igualdade com o contrato do framework: o
      proprio artefato condensa as 8 funcoes do ESP em 7 etapas de tela e mantem 8 no
      Reading. O intervalo e o que a referencia contem.
  (d) a soma dos minutos dos rotulos fecha o `percurso_min` do contrato (55). O builder
      ja cobra isso com assert na geracao; aqui a checagem sobrevive ao arquivo, nao ao
      processo — aula editada a mao depois do build tambem passa por aqui.

ESCOPO — anatomia, nao repo
---------------------------
So os quatro frameworks da anatomia guided-discovery. O imersivo tem phase-bar de
CAPITULOS da narrativa, sem orcamento de minutos: cobrar minuto la reprovaria 1.221
arquivos que nunca tiveram isso.

USO:
    python3 scripts/check_espinha.py                    # repo inteiro
    python3 scripts/check_espinha.py A.html B.html      # so estes
    python3 scripts/check_espinha.py --selftest         # prova que morde
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANATOMIA_GD = ('reading-into-speaking', 'listening-into-interaction',
               'grammar-for-communication', 'esp-real-world')

ETAPAS_MIN, ETAPAS_MAX = 7, 8


def _contratos():
    """percurso_min declarado por framework, de public/data/frameworks.json."""
    p = os.path.join(RAIZ, 'public', 'data', 'frameworks.json')
    try:
        with open(p, encoding='utf-8') as fh:
            d = json.load(fh)
    except Exception:
        return {}
    out = {}
    for cat in d.get('categorias', []):
        for f in cat.get('frameworks', []):
            c = f.get('contrato') or {}
            if c.get('percurso_min'):
                out[f['id']] = c['percurso_min']
    return out


def framework_de(html):
    m = re.search(r'<meta name="alumni-framework" content="([a-z-]+)"', html)
    return m.group(1) if m else None


def telas(html):
    """Os <div class="slide ..."> — NUNCA .slide-inner, .slide-dark casa como slide.

    A distincao importa: contar por substring 'class="slide' pega slide-inner e
    slides-container e infla o numero. Ancoramos no fim da palavra.
    """
    return re.findall(r'<div class="slide(?![-\w])[^"]*"[^>]*>', html)


def rotulos(html):
    """(nome, minutos) de cada rotulo da barra de etapas."""
    return [(m.group(1), int(m.group(2)) if m.group(2) else 0)
            for m in re.finditer(
                r'<span class="phase-label[^"]*"[^>]*data-name="([^"]*)"'
                r'(?:[^>]*data-min="(\d+)")?', html)]


def verifica(paths):
    fails, checados = [], 0
    contratos = _contratos()
    for p in paths:
        if not re.search(r'-aula\d+\.html$', os.path.basename(p)):
            continue
        with open(p, encoding='utf-8', errors='replace') as fh:
            h = fh.read()
        fw = framework_de(h)
        if fw not in ANATOMIA_GD:
            continue
        checados += 1
        rel = os.path.relpath(p, RAIZ)
        ts = telas(h)
        rs = rotulos(h)
        n_etapas = len(rs)

        # (c) 7 ou 8 etapas
        if not (ETAPAS_MIN <= n_etapas <= ETAPAS_MAX):
            fails.append(
                f'{rel}: {n_etapas} etapa(s) na barra. A anatomia guided-discovery tem '
                f'{ETAPAS_MIN} ou {ETAPAS_MAX} — o artefato condensa as 8 funcoes do ESP em 7 '
                f'etapas de tela e mantem 8 no Reading, e e esse o intervalo.')
            continue

        # (a) toda tela declara a etapa
        sem = [i for i, t in enumerate(ts, 1) if 'data-phase=' not in t]
        if sem:
            fails.append(
                f'{rel}: {len(sem)} de {len(ts)} telas sem data-phase (telas {sem[:6]}...). '
                f'Sem isso o builder nao regenera slidePhases e a barra acende a etapa que o '
                f'mapa da OUTRA aula mandar.')

        # (b) a etapa declarada existe
        fora = sorted({int(m) for t in ts
                       for m in re.findall(r'data-phase="(\d+)"', t)
                       if not (1 <= int(m) <= n_etapas)})
        if fora:
            fails.append(
                f'{rel}: tela(s) com data-phase {fora} e a barra so tem {n_etapas} etapas. '
                f'Segmento que nao existe nunca acende.')

        # (d) os minutos fecham o contrato
        soma = sum(m for _, m in rs)
        alvo = contratos.get(fw)
        if alvo and soma != alvo:
            fails.append(
                f'{rel}: os rotulos somam {soma} min e o contrato de "{fw}" declara '
                f'percurso_min={alvo}. A barra mostraria um percurso que o contrato nao '
                f'reconhece.')
        elif not soma:
            fails.append(
                f'{rel}: nenhum rotulo tem data-min. O orcamento de minutos por etapa e o que '
                f'da sentido a "o numero de telas deriva do orcamento" — sem ele nao ha de que '
                f'derivar.')
    return fails, checados


def _falso(n_etapas=8, n_telas=4, phase=lambda i: i, mins=None, fw='reading-into-speaking'):
    mins = mins if mins is not None else [4, 3, 5, 8, 8, 7, 14, 6][:n_etapas]
    lab = ''.join(f'<span class="phase-label" data-phase="{i+1}" data-name="E{i+1}" '
                  f'data-min="{mins[i]}">E{i+1}</span>' for i in range(n_etapas))
    sl = ''.join(f'<div class="slide slide-light" data-slide="{i+1}"'
                 + (f' data-phase="{phase(i+1)}"' if phase(i + 1) else '')
                 + '><div class="slide-inner">x</div></div>' for i in range(n_telas))
    return f'<meta name="alumni-framework" content="{fw}">{lab}{sl}'


def selftest():
    casos = [
        ('espinha correta', _falso(), False),
        ('tela sem data-phase', _falso(phase=lambda i: 0 if i == 2 else i), True),
        ('data-phase fora do numero de etapas', _falso(phase=lambda i: 9 if i == 1 else i), True),
        ('6 etapas', _falso(n_etapas=6, mins=[4, 3, 5, 8, 8, 27]), True),
        ('minutos que nao fecham 55', _falso(mins=[4, 3, 5, 8, 8, 7, 14, 5]), True),
        ('sem data-min nenhum', _falso(mins=[0] * 8), True),
        ('imersivo — nao e deste gate',
         _falso(n_etapas=3, mins=[0, 0, 0], fw='imersivo-prototipo'), False),
    ]
    import tempfile
    falhou = False
    for rotulo, html, deve_falhar in casos:
        d = tempfile.mkdtemp()
        p = os.path.join(d, 'x-aula1.html')
        with open(p, 'w', encoding='utf-8') as fh:
            fh.write(html)
        fails, _ = verifica([p])
        ok = bool(fails) == deve_falhar
        print(f"  {'OK  ' if ok else 'FALHA'}  {rotulo}")
        falhou |= not ok
    if falhou:
        print('\nSELFTEST FALHOU — o gate parou de morder.')
        return 1
    print(f'\nSELFTEST OK — os {len(casos)} casos.')
    return 0


def _sem_objeto(n_medidos):
    """Verde SEM OBJETO e o defeito que o P2 §13 nomeia: "checagem que nao falha, so nao faz
    nada". Quando este gate mede ZERO aula e existe material da anatomia private-black no
    repo, ele diz isso -- em vez de imprimir OK e parecer cobertura.

    Nao reprova: ficar sem aula na forma antiga e estado legitimo e transitorio (o molde
    trocou de anatomia em 24/08/2026 e as aulas voltam uma por PR). O que nao pode e ficar
    invisivel."""
    import glob as _glob
    if n_medidos:
        return
    for _f in _glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")):
        try:
            with open(_f, encoding="utf-8", errors="replace") as _fh:
                if 'content="private-black"' in _fh.read(4000):
                    print("  AVISO — SEM OBJETO: este gate mede a forma guided-discovery e nao"
                          " ha nenhuma aula dela no repo. O material da anatomia nova"
                          " (private-black) NAO e coberto por ele. Reaponte-o para o"
                          " requisito, ou aposente-o com o motivo escrito (P2 §13/§23).")
                    return
        except OSError:
            pass


def main():
    if '--selftest' in sys.argv:
        return selftest()
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    paths = args or (glob.glob(os.path.join(RAIZ, 'public', 'professor', '*.html'))
                     + glob.glob(os.path.join(RAIZ, 'public', 'aluno', '*.html')))
    fails, checados = verifica(paths)
    for f in fails:
        print(f'  FAIL  {f}')
    if fails:
        print(f'\n{len(fails)} problema(s) de espinha em {checados} aula(s) da anatomia '
              f'guided-discovery.')
        return 1
    print(f'OK — espinha integra em {checados} aula(s) guided-discovery '
          f'(etapas declaradas, telas dentro delas, minutos fechando o contrato).')
    _sem_objeto(checados)
    return 0


if __name__ == '__main__':
    sys.exit(main())
