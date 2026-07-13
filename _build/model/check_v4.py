#!/usr/bin/env python3
"""
GATE V4 — a aula obedece o Modelo V4 (Conteúdo Private Personalizada)?

Implementa mecanicamente a §11 (CHECKLIST) de _build/model/V4-SPEC.md. Referência
viva: `pricila-aula06 (1).html` (12 slides), a aula que a pedagogia entregou como
exemplo.

POR QUE ESTE GATE EXISTE
------------------------
O V4 não é um ajuste de estilo — é outra aula. 7-15 slides no lugar de 33; gramática
IMPLÍCITA no lugar de "The Code" + "Common Mistake"; UMA skill receptiva principal;
todo exercício com a resposta EXCLUSIVAMENTE no "Answer key:", nunca no corpo.

Um humano lendo a aula no olho não pega isso de forma confiável — e "olhei e pareceu
certo" foi exatamente o que deixou 324 botões mortos por três semanas. Regra desta
casa: se não há teste que falhe quando está errado, não se diz que está certo.

    python3 _build/model/check_v4.py public/professor/{slug}-aula{N}.html
"""
import html as _html
import re
import sys

# §1 — ordem FIXA. O prefixo do chapter-label de cada slide tem de sair desta lista,
# e a sequência ao longo do documento nunca pode ANDAR PARA TRÁS.
CAPITULOS = [
    "Let's Get Started",
    'Packing Words',
    'Brainstorming',
    'Diving Deep',
    'Practice',
    'Your Turn',
    'Wrap-up',
]

MIN_SLIDES, MAX_SLIDES = 7, 15
MIN_VOCAB, MAX_VOCAB = 8, 12
MINUTOS_AULA = 90


def texto(s):
    """tira tags e desescapa — o que o ALUNO lê na tela."""
    return _html.unescape(re.sub(r'<[^>]+>', ' ', s))


def checar(caminho):
    h = open(caminho, encoding='utf-8', errors='replace').read()
    falhas, avisos = [], []

    # ---- 1. tamanho da aula (§1: "NÃO é 25-30 do modelo velho")
    slides = re.findall(r'<div class="slide[ "]', h)
    n = len(slides)
    if not (MIN_SLIDES <= n <= MAX_SLIDES):
        falhas.append(f'SLIDES: {n} (V4 exige {MIN_SLIDES}-{MAX_SLIDES}). '
                      f'{"Aula do modelo VELHO — precisa ser refeita, não aparada." if n > 20 else ""}')

    # ---- 2. capítulos: existem, saem da lista, e estão em ORDEM
    labels = [texto(m.group(1)).strip()
              for m in re.finditer(r'class="chapter-label"[^>]*>(.*?)</', h, re.S)]
    if not labels:
        falhas.append('CAPÍTULOS: nenhum chapter-label. O V4 exige 1 por slide.')
    else:
        vistos = []
        for i, lab in enumerate(labels, 1):
            cap = next((c for c in CAPITULOS if lab.startswith(c)), None)
            if cap is None:
                falhas.append(f'CAPÍTULO slide {i}: "{lab[:40]}" não é um dos 7 do V4')
            else:
                vistos.append((i, cap))
        # a ordem não pode retroceder
        pos = -1
        for i, cap in vistos:
            p = CAPITULOS.index(cap)
            if p < pos:
                falhas.append(f'ORDEM: slide {i} volta para "{cap}" depois de um capítulo posterior. '
                              f'A ordem do V4 é fixa: {" > ".join(CAPITULOS)}')
                break
            pos = p
        faltando = [c for c in CAPITULOS if c not in {c for _, c in vistos}]
        if faltando:
            falhas.append(f'CAPÍTULOS FALTANDO: {", ".join(faltando)}')

    # ---- 3. Quick Fire é PROIBIDO (§10: herda "ZERO Quick Fire")
    if re.search(r'quick[- ]?fire|class="qf-', h, re.I):
        falhas.append('QUICK FIRE presente — o V4 herda a proibição do modelo (§10)')

    # ---- 4. gramática IMPLÍCITA (§1.4): sem prática gramatical explícita
    explicita = [p for p in ('Common Mistake', 'Grammar Practice', 'Reveal the Rule', 'The Code')
                 if re.search(re.escape(p), h, re.I)]
    if explicita:
        falhas.append(f'GRAMÁTICA EXPLÍCITA: {", ".join(explicita)}. No V4 a gramática é '
                      f'IMPLÍCITA — a linguagem funcional entra em "Diving Deep", sem drill de regra.')

    # ---- 5. Answer key (§4): a resposta vive SÓ ali
    if not re.search(r'Answer key', h, re.I):
        falhas.append('ANSWER KEY ausente: todo exercício controlado precisa de '
                      'PROMPT + VISUALIZAÇÃO (em branco) + "Answer key:"')

    # ---- 6. vocabulário 8-12 (§10)
    vocab = len(re.findall(r'class="[^"]*vocab-card', h))
    if vocab and not (MIN_VOCAB <= vocab <= MAX_VOCAB):
        avisos.append(f'VOCAB: {vocab} cards (V4 pede {MIN_VOCAB}-{MAX_VOCAB})')

    # ---- 7. minutagem soma 90 (§5) — o Teacher's Guide é o dono do tempo
    #
    # Lê SÓ dentro de data-teacher (o tempo é do professor; "3 min" num texto do aluno
    # não é minutagem). E aceita os três formatos que a referência de fato usa:
    #     "-- 8 min:"      "-- 7-8 min:"  (intervalo -> usa o topo)     "(12 min):"
    # A 1a versão só entendia o primeiro, lia 9 dos 12 slides, somava 66 e REPROVAVA a
    # aula que a própria pedagogia entregou como exemplo. Quando o gate discorda da
    # referência, o suspeito nº 1 é o gate.
    guias = re.findall(r'data-teacher="([^"]*)"', h)
    mins = []
    for g in guias:
        for m in re.finditer(r'(\d+)(?:\s*[-–]\s*(\d+))?\s*min\b', _html.unescape(g), re.I):
            mins.append(int(m.group(2) or m.group(1)))   # intervalo "7-8 min" -> 8
    if mins:
        soma = sum(mins)
        if abs(soma - MINUTOS_AULA) > 8:
            falhas.append(f'MINUTAGEM: soma {soma} min em {len(mins)} slides '
                          f'(V4 = aula de {MINUTOS_AULA} min). A minutagem por slide vive no '
                          f'data-teacher e tem de fechar 90.')
    else:
        avisos.append("MINUTAGEM ausente no Teacher's Guide (§5 pede min por slide, soma 90)")

    # ---- 8. rótulo do TIPO de exercício é metadado do PROFESSOR, não do aluno (§5)
    corpo = re.sub(r'data-teacher="[^"]*"', '', h)          # tira o guia do professor
    corpo = re.sub(r'<script\b[\s\S]*?</script>', '', corpo)
    vazou = [t for t in ('MATCHING', 'FILL IN THE BLANKS', 'ORDERING', 'MULTICHOICE',
                         'REPHRASING', 'SORTING', 'TRUE OR FALSE')
             if re.search(rf'\b{t}\b', texto(corpo))]
    if vazou:
        falhas.append(f'RÓTULO DE EXERCÍCIO NA TELA DO ALUNO: {", ".join(vazou)}. '
                      f'É metadado do professor — vai em PROCEDIMENTOS/data-teacher (§5).')

    return falhas, avisos


def main():
    arqs = [a for a in sys.argv[1:] if a.endswith('.html')]
    if not arqs:
        sys.exit('uso: check_v4.py <arquivo.html> [...]')

    ruim = False
    for a in arqs:
        falhas, avisos = checar(a)
        nome = a.split('/')[-1]
        if falhas:
            ruim = True
            print(f'\n✗ {nome}')
            for f in falhas:
                print(f'    {f}')
        elif avisos:
            print(f'\n~ {nome}')
        else:
            print(f'✅ {nome}: V4 OK')
        for w in avisos:
            print(f'    (aviso) {w}')

    if ruim:
        print('\nBLOQUEADO — a aula não é V4. Spec: _build/model/V4-SPEC.md')
        print('Exemplo vivo: "pricila-aula06 (1).html" (12 slides, 7 capítulos, Answer key).')
        return 1
    print('\n=== V4 OK ===')
    return 0


if __name__ == '__main__':
    sys.exit(main())
