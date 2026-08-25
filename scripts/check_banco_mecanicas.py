#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 27 — aula guided-discovery so usa mecanica que o artefato consegue montar.

POR QUE ISTO EXISTE (11/08/2026)
--------------------------------
Ordem do Dan, depois de ver a lista do que o documento promete e o artefato nao tem:

    "se nao tem no artefato nada parecido que o documento descreva, hora de remover"

Tres linhas do banco de mecanicas (03 §4) sairam: **Matching**, **Ordering/reconstruction**
e **Information gap**. Mais o kind `quickfire`, que nao e linha do banco mas tem o mesmo
problema. O criterio nao e etiqueta, e forma: True/False tambem nao existe com esse nome no
artefato, mas a forma de "escolha uma e veja por que" existe (quiz-item + rationale) e e com
ela que o true/false e montado. Matching precisaria de uma UI de pares que nao existe em
lugar nenhum — monta-la exigiria inventar, e inventar foi o que custou 119 classes de
reescrita em 07/08/2026.

O QUE ESTE GATE **NAO** FAZ — e por que
---------------------------------------
Nao remove nada do builder nem dos shells. Medido antes de decidir: `matching` esta em
**1.015 aulas publicadas** e 154 configs, `quickfire` em 290 configs — todas do molde
IMERSIVO, onde o artefato da Stephanie nunca foi a especificacao. Apagar o kind quebraria a
regeracao dessas aulas, e o legado nao se toca (REGRA 30). O GATE 18 tambem exige que os
dois shells nao derivem: tirar o CSS de um so criaria a deriva que ele existe para impedir.

A remocao vale ONDE A REGRA VALE: numa aula da anatomia guided-discovery.

O QUE ELE COBRA
---------------
  (a) nenhuma aula guided-discovery usa, DENTRO dos slides, o markup de uma mecanica
      removida (ic-match*, ic-chip, ic-word, ic-def, ic-pair, ic-sel, qf-card, qf-nav...);
  (b) toda mecanica declarada no `syllabus.json` de um aluno com ciclo existe no banco de
      `_build/model/ciclo.json` com status VALE.

O (b) e o que impede a lista de voltar pela porta do planejamento: adiantaria pouco proibir
o markup se o syllabus continuasse prometendo "information gap" para a aula 12.

ESCOPO — anatomia, nao repo
---------------------------
So os quatro frameworks da anatomia guided-discovery.

USO:
    python3 scripts/check_banco_mecanicas.py
    python3 scripts/check_banco_mecanicas.py A.html
    python3 scripts/check_banco_mecanicas.py --selftest
"""
import glob
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANATOMIA_GD = ('reading-into-speaking', 'listening-into-interaction',
               'grammar-for-communication', 'esp-real-world')

# markup das mecanicas removidas (segue existindo no shell, para o imersivo)
MARKUP_REMOVIDO = {
    'Matching': r'ic-match|ic-chip|ic-word|ic-def|ic-pair|ic-sel\b',
    'quickfire': r'qf-card|qf-nav|qf-tips',
}

# Nome que o syllabus usa para uma mecanica FORA do banco do 03 §4 e que caiu junto. Sem
# esta lista, "Replicas rapidas" (o quickfire) continuaria sendo prometido no planejamento:
# o cruzamento com o banco nao a alcanca, porque ela nunca esteve la.
FORA_DO_BANCO_REMOVIDAS = {
    'replicas rapidas': 'quickfire — sem forma no artefato. Monte com reveal-item: a aluna '
                        'responde a objecao e so entao compara.',
}


def norm(t):
    return unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()


def banco():
    p = os.path.join(RAIZ, '_build', 'model', 'ciclo.json')
    with open(p, encoding='utf-8') as fh:
        d = json.load(fh)
    linhas = (d.get('banco_de_mecanicas') or {}).get('linhas', [])
    return {norm(l['mecanica']): l for l in linhas}


def framework_de(h):
    m = re.search(r'<meta name="alumni-framework" content="([a-z-]+)"', h)
    return m.group(1) if m else None


def corpo_dos_slides(h):
    """So o que esta DENTRO dos slides. O CSS e o JS do shell continuam citando as classes
    removidas de proposito (o imersivo usa), e conta-los seria acusar o shell inteiro."""
    m = re.search(r'<div class="slides-container".*?</div><!-- /slides-container -->', h, re.S)
    return m.group(0) if m else ''


def verifica(paths, checar_syllabus=True):
    fails, checados = [], 0
    b = banco()
    for p in paths:
        if not re.search(r'-aula\d+\.html$', os.path.basename(p)):
            continue
        with open(p, encoding='utf-8', errors='replace') as fh:
            h = fh.read()
        if framework_de(h) not in ANATOMIA_GD:
            continue
        checados += 1
        rel = os.path.relpath(p, RAIZ)
        corpo = corpo_dos_slides(h)
        for nome, rx in MARKUP_REMOVIDO.items():
            achados = re.findall(rx, corpo)
            if achados:
                fails.append(
                    f'{rel}: usa o markup de "{nome}" ({len(achados)} ocorrencia(s): '
                    f'{sorted(set(achados))[:4]}), que saiu do banco por nao ter forma no '
                    f'artefato. Monte com o que existe la: sorting (cada item sob uma '
                    f'categoria), quiz-item (escolha + rationale) ou reveal-item '
                    f'(diga, depois compare).')

    if checar_syllabus:
        for sp in sorted(glob.glob(os.path.join(RAIZ, '_build', '*', 'syllabus.json'))):
            with open(sp, encoding='utf-8') as fh:
                d = json.load(fh)
            rel = os.path.relpath(sp, RAIZ)
            for a in d.get('aulas', []):
                for m in a.get('mecanicas', []):
                    chave = norm(m['mecanica'])
                    if chave in FORA_DO_BANCO_REMOVIDAS:
                        fails.append(
                            f'{rel}: a aula {a["n"]} declara "{m["mecanica"]}", que saiu junto '
                            f'com o banco: {FORA_DO_BANCO_REMOVIDAS[chave]}')
                        continue
                    linha = b.get(chave)
                    if linha is None:
                        continue  # mecanica fora do banco (declarada com no_banco: false)
                    if linha['status'] != 'VALE':
                        fails.append(
                            f'{rel}: a aula {a["n"]} declara "{m["mecanica"]}", que esta no '
                            f'banco como {linha["status"]} — o artefato nao tem com que '
                            f'monta-la ({linha["evidencia_no_artefato"][:60]}...).')
    return fails, checados


def selftest():
    import tempfile
    def aula(corpo, fw='reading-into-speaking'):
        return (f'<meta name="alumni-framework" content="{fw}">'
                f'<div class="slides-container" id="slidesContainer">{corpo}'
                f'</div><!-- /slides-container -->'
                f'<style>.ic-match{{display:grid}}.qf-card{{padding:0}}</style>')
    casos = [
        ('aula sem mecanica removida', aula('<div class="sortbox"></div>'), False),
        ('aula usando matching', aula('<div class="ic-match"><div class="ic-chip">x</div></div>'), True),
        ('aula usando quickfire', aula('<div class="qf-card">x</div>'), True),
        ('CSS do shell citando as classes (nao e uso)', aula('<div class="sortbox"></div>'), False),
        ('imersivo usando matching — nao e deste gate',
         aula('<div class="ic-match"></div>', fw='imersivo-prototipo'), False),
    ]
    falhou = False
    for rotulo, htm, deve_falhar in casos:
        d = tempfile.mkdtemp()
        p = os.path.join(d, 'professor', 'x-aula1.html')
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8') as fh:
            fh.write(htm)
        fails, _ = verifica([p], checar_syllabus=False)
        ok = bool(fails) == deve_falhar
        print(f"  {'OK  ' if ok else 'FALHA'}  {rotulo}")
        falhou |= not ok
    # o banco tem de estar legivel e com as tres removidas
    b = banco()
    for m in ('matching', 'ordering/reconstruction', 'information gap'):
        if b.get(m, {}).get('status') != 'REMOVIDA':
            print(f'  FALHA  banco: "{m}" deveria estar REMOVIDA')
            falhou = True
        else:
            print(f'  OK    banco: "{m}" REMOVIDA')
    if falhou:
        print('\nSELFTEST FALHOU — o gate parou de morder.')
        return 1
    print('\nSELFTEST OK.')
    return 0


def _sem_objeto(n_medidos):
    """Verde SEM OBJETO e o defeito que o P2 §13 nomeia: "checagem que nao falha, so nao faz
    nada". Quando este gate mede ZERO aula e existe material da anatomia consultivo no
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
                if 'content="consultivo"' in _fh.read(4000):
                    print("  AVISO — SEM OBJETO: este gate mede a forma guided-discovery e nao"
                          " ha nenhuma aula dela no repo. O material da anatomia nova"
                          " (consultivo) NAO e coberto por ele. Reaponte-o para o"
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
        print(f'\n{len(fails)} uso(s) de mecanica removida em {checados} aula(s) '
              f'guided-discovery.')
        return 1
    print(f'OK — {checados} aula(s) guided-discovery: nenhuma usa mecanica que o artefato '
          f'nao consegue montar, e nenhum syllabus promete uma.')
    _sem_objeto(checados)
    return 0


if __name__ == '__main__':
    sys.exit(main())
