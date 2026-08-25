#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 23 — a nota do professor: existe em toda tela, tem tempo, e nao grita.

POR QUE ISTO EXISTE (11/08/2026)
--------------------------------
Item 2.15 da instrucao corretiva ao lote do molde:

    "As notas usam formulacoes enfaticas ou editoriais, como 'NAO ajude', 'force a
     resposta' e 'TEM de responder'. Reescreva as notas para orientar acao, timing,
     interacao, evidencia esperada e apoio condicional."

As tres expressoes citadas AINDA ESTAVAM no material quando este gate foi escrito, meses
depois da correcao pedida — porque a correcao era prosa num .docx e nada no repo a cobrava.

O QUE ELE COBRA — as tres coisas sao medidas no artefato, nao opinadas
---------------------------------------------------------------------
  (a) COBERTURA: toda tela tem `data-teacher`. Medido no artefato de referencia: 63 telas,
      63 notas. Nota e a UNICA forma de o professor receber instrucao durante a aula —
      tela sem nota e tela que ele conduz de cabeca.
  (b) TEMPO: toda nota abre com um orcamento ("3 min.", "(30 s)"). Medido no artefato:
      63 de 63 (61 em minutos, 2 em segundos). Sem o tempo na nota, os 55 minutos do
      percurso existem so na barra do topo, e quem conduz nao sabe quanto gastar ALI.
  (c) TOM: nenhuma nota com comando gritado ou enfase editorial. A lista abaixo sai das
      expressoes que a propria instrucao corretiva nomeia, mais as da mesma familia.

O QUE ELE NAO COBRA — e por que
-------------------------------
Caixa alta para MARCAR UMA PALAVRA no meio da frase ("uma UNICA vez", "as palavras DELA")
e recurso de leitura rapida, nao grito: a nota e escaneada em aula, com a aluna esperando.
O que o gate barra e o comando em caixa alta e o imperativo de forca — a diferenca entre
"pergunte UMA vez" e "NAO ajude".

ESCOPO — anatomia, nao repo
---------------------------
So os quatro frameworks da anatomia guided-discovery, e so no arquivo do PROFESSOR: o
espelho do aluno tem os data-teacher removidos pelo builder, de proposito.

USO:
    python3 scripts/check_teacher_notes.py                 # repo inteiro
    python3 scripts/check_teacher_notes.py A.html          # so este
    python3 scripts/check_teacher_notes.py --selftest      # prova que morde
"""
import glob
import html as _html
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANATOMIA_GD = ('reading-into-speaking', 'listening-into-interaction',
               'grammar-for-communication', 'esp-real-world')

# As tres primeiras sao citadas na instrucao corretiva, palavra por palavra.
TOM_PROIBIDO = [
    (r'n[aã]o\s+ajude', "'nao ajude' — diga o procedimento ('etapa diagnostica: sem apoio "
                        "durante a fala'), nao a proibicao gritada"),
    (r'\bforce\b', "'force' — o professor conduz, nao arranca. Use 'mantenha a resposta em X'"),
    (r'\bTEM\s+de\b', "'TEM de' em caixa alta — comando enfatico"),
    (r'\bN[AÃ]O\s+[a-zA-Zà-ÿ]', "'NAO' em caixa alta abrindo comando — reescreva como "
                                "procedimento ('sem exemplo, sem correcao durante a fala')"),
    (r'\bNUNCA\b', "'NUNCA' em caixa alta — comando enfatico"),
    (r'\bJAMAIS\b', "'JAMAIS' — comando enfatico"),
    (r'\bexija\b', "'exija' — imperativo de forca"),
    (r'\bobrigue\b', "'obrigue' — imperativo de forca"),
    (r'\bproiba\b', "'proiba' — imperativo de forca"),
]

TEMPO = re.compile(r'\d[\d,\.]*\s*(?:min|s\b|seg)', re.I)


def framework_de(h):
    m = re.search(r'<meta name="alumni-framework" content="([a-z-]+)"', h)
    return m.group(1) if m else None


def telas(h):
    return re.findall(r'<div class="slide(?![-\w])[^"]*"[^>]*>', h)


def notas(h):
    return [_html.unescape(x) for x in re.findall(r'data-teacher="([^"]*)"', h)]


def verifica(paths):
    fails, checados = [], 0
    for p in paths:
        base = os.path.basename(p)
        if not re.search(r'-aula\d+\.html$', base):
            continue
        if os.sep + 'aluno' + os.sep in p:
            continue  # o espelho do aluno nao tem nota, por desenho
        with open(p, encoding='utf-8', errors='replace') as fh:
            h = fh.read()
        if framework_de(h) not in ANATOMIA_GD:
            continue
        checados += 1
        rel = os.path.relpath(p, RAIZ)
        ts = telas(h)
        sem_nota = [i for i, t in enumerate(ts, 1) if 'data-teacher=' not in t]
        if sem_nota:
            fails.append(f'{rel}: {len(sem_nota)} de {len(ts)} telas sem data-teacher '
                         f'(telas {sem_nota[:8]}). No artefato que define a anatomia sao 63 de '
                         f'63 — tela sem nota e tela conduzida de cabeca.')
        for i, n in enumerate(notas(h), 1):
            texto = re.sub(r'<[^>]+>', ' ', n)
            if not TEMPO.search(texto):
                fails.append(f'{rel}: nota {i} sem orcamento de tempo. Abra com o tempo da '
                             f'tela ("3 min.", "(30 s)") — e assim no artefato, em 63 de 63.')
            for rx, porque in TOM_PROIBIDO:
                if re.search(rx, texto):
                    trecho = re.sub(r'\s+', ' ', texto).strip()[:90]
                    fails.append(f'{rel}: nota {i} com tom enfatico — {porque}. '
                                 f'Trecho: "{trecho}..."')
                    break
    return fails, checados


def _falso(nota='<strong>3 min.</strong> Leia as tres perguntas com ela.', com_nota=True,
           fw='reading-into-speaking'):
    t = (f'<div class="slide slide-light" data-slide="1"'
         + (f' data-teacher="{_html.escape(nota, quote=True)}"' if com_nota else '')
         + '><div class="slide-inner">x</div></div>')
    return f'<meta name="alumni-framework" content="{fw}">{t}'


def selftest():
    casos = [
        ('nota boa', _falso(), False),
        ('tela sem nota', _falso(com_nota=False), True),
        ('nota sem tempo', _falso('Leia as tres perguntas com ela.'), True),
        ("'nao ajude'", _falso('<strong>4 min. DIAGNOSTICA — nao ajude.</strong> Ela fala.'), True),
        ("'force a resposta'", _falso('<strong>3 min.</strong> force a resposta a ficar no verbo.'), True),
        ("'TEM de responder'", _falso('<strong>2 min.</strong> ela TEM de responder.'), True),
        ("'NAO de exemplo'", _falso('<strong>1 min.</strong> NAO de exemplo.'), True),
        ('caixa alta marcando palavra (permitido)',
         _falso('<strong>3 min.</strong> Pergunte UMA vez e use as palavras DELA.'), False),
        ('imersivo — nao e deste gate', _falso(com_nota=False, fw='imersivo-prototipo'), False),
    ]
    import tempfile
    falhou = False
    for rotulo, htm, deve_falhar in casos:
        d = tempfile.mkdtemp()
        p = os.path.join(d, 'professor', 'x-aula1.html')
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8') as fh:
            fh.write(htm)
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
    paths = args or glob.glob(os.path.join(RAIZ, 'public', 'professor', '*.html'))
    fails, checados = verifica(paths)
    for f in fails:
        print(f'  FAIL  {f}')
    if fails:
        print(f'\n{len(fails)} problema(s) em {checados} aula(s) guided-discovery.')
        return 1
    print(f'OK — {checados} aula(s) guided-discovery: nota em toda tela, com tempo, sem '
          f'comando gritado.')
    _sem_objeto(checados)
    return 0


if __name__ == '__main__':
    sys.exit(main())
