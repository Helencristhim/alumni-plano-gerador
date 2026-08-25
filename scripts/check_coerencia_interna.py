#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 26 — a nota manda fazer o que a tela permite fazer.

POR QUE ISTO EXISTE (11/08/2026)
--------------------------------
Item 2.10 da instrucao corretiva:

    "Na aula de Reading, a Teacher's Note instrui 'toque o audio', embora a tarefa exija
     leitura de documentos. Faca auditoria slide a slide. Prompt, subprompt, midia, widget,
     Teacher's Note, answer key e turnos do professor devem solicitar a MESMA acao."

E a camada "Coerencia interna" do 03 §8. Ate hoje ela saia NAO VERIFICADO em todo relatorio
de validacao, porque nao havia gate nenhum: o GATE 23 cobre a EXISTENCIA e o TOM da nota,
nunca o que ela manda fazer contra o que a tela tem.

COMO ESTE GATE FOI CONSTRUIDO — o artefato e o oraculo
------------------------------------------------------
A primeira versao das regras disparou VINTE vezes no proprio artefato de referencia. Isso
nao prova defeito no artefato: prova que a regra estava errada. Ela caiu em duas armadilhas,
as duas da familia "medir por substring nao e ler":

  1. POLISSEMIA. A nota dizia "leia o quadro" e eu li como "escreva no quadro". O "quadro"
     ali e o `brief` (o cartao de cenario), que estava na tela. Palavra ambigua nao vira
     regra.
  2. PROSA QUE DESCREVE O PERCURSO. "a aluna vai ouvir a abertura de uma call" e resumo do
     que a aula faz, nao ordem para tocar agora. So o IMPERATIVO vira regra.

A versao que ficou e silenciosa nas 63 telas do artefato e nas 64 do molde, e mesmo assim
pegou um defeito real: a tela 5 da aula 2 mandava "use o segmento 'Just what each one
wants'" numa tela sem player nenhum — o player esta na tela da call, tres telas antes.

A REGRA
-------
Nota com IMPERATIVO de uma acao (tocar, ler o texto, preencher, classificar, cronometrar)
exige que a acao seja executavel DALI: ou o mecanismo esta na tela, ou a nota diz para onde
ir ("volte a...", "na etapa 3..."). Instrucao que nao se executa de onde o professor esta
nao e instrucao — e o defeito 2.10.

A saida de navegacao NAO e brecha: e a diferenca entre "toque o audio" (numa tela sem
player: impossivel) e "volte a tela da call e toque" (possivel). As duas coisas que o
professor precisa saber sao O QUE fazer e ONDE.

ESCOPO — anatomia, nao repo
---------------------------
So os quatro frameworks da anatomia guided-discovery, e so no arquivo do PROFESSOR: o
espelho do aluno perde o data-teacher por desenho.

USO:
    python3 scripts/check_coerencia_interna.py                # repo inteiro
    python3 scripts/check_coerencia_interna.py A.html
    python3 scripts/check_coerencia_interna.py --selftest
"""
import glob
import html as _html
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANATOMIA_GD = ('reading-into-speaking', 'listening-into-interaction',
               'grammar-for-communication', 'esp-real-world')

# A nota pode mandar ir para outra tela. Ai a acao e executavel, so nao e aqui.
NAVEGACAO = r'\bvolte\b|\bva para\b|\bna tela\b|\bna etapa\b|\bna fase\b|\btela anterior\b|\bde volta\b'

# (rotulo, imperativo na NOTA, marcador do mecanismo na TELA, o que dizer quando falha)
REGRAS = [
    ('audio',
     r'\btoque\b|\btoca o audio\b|\bde play\b|\bcoloque o audio\b|\breproduza\b'
     r'|\buse o segmento\b|\buse a call\b',
     r'data-speak|audio-btn|audio-player|ic-call|ic-seg|say\(|playCall|speakText\(',
     'a nota manda TOCAR e a tela nao tem player, botao de audio nem segmento'),
    ('leitura',
     r'\bleia o texto\b|\bleia os textos\b|\bleia o documento\b|\bleia os documentos\b'
     r'|\bleia o artigo\b',
     r'class="evi"|ic-reading|evi-list',
     'a nota manda LER O TEXTO e a tela nao tem texto nenhum'),
    ('escrita',
     r'\bpreencha\b|\bdigite\b|\bescreva no campo\b',
     r'writebox|blank-input|fb-field|textarea',
     'a nota manda ESCREVER e a tela nao tem campo'),
    ('classificacao',
     r'\bclassifique\b|\barraste\b',
     r'sortbox|sortcol|sortitem|ic-match',
     'a nota manda CLASSIFICAR e a tela nao tem colunas nem pares'),
    ('cronometro',
     r'\bcronometro\b',
     r'timerbox|timer-btn',
     'a nota cita o CRONOMETRO e a tela nao tem'),
]


def norm(t):
    return unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()


def framework_de(h):
    m = re.search(r'<meta name="alumni-framework" content="([a-z-]+)"', h)
    return m.group(1) if m else None


def telas(h):
    idx = [m.start() for m in re.finditer(r'<div class="slide(?![-\w])[^"]*"[^>]*>', h)]
    idx.append(len(h))
    return [h[idx[i]:idx[i + 1]] for i in range(len(idx) - 1)]


def verifica(paths):
    fails, checados = [], 0
    for p in paths:
        if not re.search(r'-aula\d+\.html$', os.path.basename(p)):
            continue
        if os.sep + 'aluno' + os.sep in p:
            continue
        with open(p, encoding='utf-8', errors='replace') as fh:
            h = fh.read()
        if framework_de(h) not in ANATOMIA_GD:
            continue
        checados += 1
        rel = os.path.relpath(p, RAIZ)
        for i, t in enumerate(telas(h), 1):
            m = re.search(r'data-teacher="([^"]*)"', t)
            if not m:
                continue
            nota = norm(_html.unescape(m.group(1)))
            if re.search(NAVEGACAO, nota):
                continue
            for rotulo, rx_nota, rx_tela, porque in REGRAS:
                achou = re.search(rx_nota, nota)
                if achou and not re.search(rx_tela, t):
                    fails.append(
                        f'{rel}: tela {i} — {porque} (a nota diz "{achou.group(0)}"). '
                        f'Ou o mecanismo entra nesta tela, ou a nota diz para onde ir '
                        f'("volte a…", "na etapa N…").')
                    break
    return fails, checados


def _falso(nota, corpo='<div class="slide-inner">x</div>', fw='reading-into-speaking'):
    t = (f'<div class="slide slide-light" data-slide="1" '
         f'data-teacher="{_html.escape(nota, quote=True)}">{corpo}</div>')
    return f'<meta name="alumni-framework" content="{fw}">{t}'


def selftest():
    casos = [
        ('nota que manda tocar, tela sem player',
         _falso('<strong>3 min.</strong> Toque o audio inteiro, uma vez.'), True),
        ('nota que manda tocar, tela COM player',
         _falso('<strong>3 min.</strong> Toque o audio inteiro.',
                '<div class="ic-call"><button class="ic-seg">Play</button></div>'), False),
        ('nota que manda tocar e diz para onde voltar',
         _falso('<strong>3 min.</strong> Volte a tela da call e toque o ultimo turno.'), False),
        ('nota que manda ler o texto, tela sem texto',
         _falso('<strong>4 min.</strong> Leia o texto com ela, uma vez.'), True),
        ('nota que manda ler o texto, tela COM texto',
         _falso('<strong>4 min.</strong> Leia o texto com ela.',
                '<div class="evi-list"><div class="evi">bla</div></div>'), False),
        ('nota que manda preencher, tela sem campo',
         _falso('<strong>2 min.</strong> Preencha os dois campos com ela.'), True),
        ('nota que DESCREVE o percurso (nao e ordem)',
         _falso('<strong>2 min.</strong> Apresente a aula pelo que ela vai ouvir no fim.'), False),
        ('polissemia: "leia o quadro" com o brief na tela',
         _falso('<strong>2 min.</strong> Leia o quadro em voz alta.',
                '<div class="brief"><dl><dt>Who</dt></dl></div>'), False),
        ('imersivo — nao e deste gate',
         _falso('<strong>3 min.</strong> Toque o audio.', fw='imersivo-prototipo'), False),
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
        print(f'\n{len(fails)} incoerencia(s) entre nota e tela em {checados} aula(s).')
        return 1
    print(f'OK — {checados} aula(s) guided-discovery: toda acao que a nota manda e '
          f'executavel de onde o professor esta.')
    _sem_objeto(checados)
    return 0


if __name__ == '__main__':
    sys.exit(main())
