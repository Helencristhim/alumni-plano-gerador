#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deriva o shell da anatomia `story-quest` DO ARTEFATO, por script.

POR QUE POR SCRIPT, E NAO A MAO
-------------------------------
O artefato (_build/model/artefatos/dante-kids-professor-view.html) e a
ESPECIFICACAO da interface: dele se COPIA, classe por classe (ver o README da
pasta e a licao de 11/08/2026, quando o porte a mao renomeou cada peca e o
GATE 20 passou a comparar a copia consigo mesma). Um script torna a derivacao
AUDITAVEL: qualquer pessoa roda de novo e ve que o shell e o artefato menos o
que esta declarado aqui embaixo — nada foi reescrito no caminho.

O QUE SAI DAQUI: TRES arquivos, todos do MESMO tronco — o artefato com a aula 2
fora (o molde carrega UMA aula de exemplo, como o da guided-discovery) e com os
literais do MODELO no lugar dos do Dante (e o base_swaps do builder que troca
por aluno).

    shells/story-quest.html            standalone: Planejamento + In Class + o deck
    shells/hub-story-quest.html        hub prof:   Planejamento + In Class + Post-class
    shells/hub-story-quest-aluno.html  hub aluno:  so Post-class

POR QUE TRES, SE O ARTEFATO E UM. O artefato resolve duas aulas numa URL so
porque uma pagina do claude.ai nao TEM duas URLs — e o proprio JS dele ja prevé
o outro caso: "Uma aula sozinha continua declarando LESSON direto, e nada muda
para ela", e curLesson sai do data-lesson do primeiro slide justamente para
isso. O split e arquitetura de producao (uma URL por aula, que e o que o
insert_hub, o dashboard e os links da aluna esperam), nao divergencia de
interface: cada arquivo leva as MESMAS pecas do artefato, so que repartidas.
A reparticao copia a que o Dante ja tem no ar: deck no standalone, percurso e
menus no hub, e o aluno so com o que e dele.

    python3 _build/model/extrai_shell_story_quest.py [--check]

--check nao escreve: so confere que os tres no disco sao o que sairia hoje.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(RAIZ)
ARTEFATO = os.path.join(RAIZ, '_build', 'model', 'artefatos',
                        'dante-kids-professor-view.html')
SHELLS = os.path.join(RAIZ, '_build', 'model', 'shells')
SHELL = os.path.join(SHELLS, 'story-quest.html')
HUB = os.path.join(SHELLS, 'hub-story-quest.html')
HUB_ALUNO = os.path.join(SHELLS, 'hub-story-quest-aluno.html')

# A paleta do artefato e a do Bento. O shell fala a paleta do MODELO porque o
# base_swaps() troca ESSES literais por aluno — mesma solucao do --mint no
# guided-discovery (artefatos/README.md). Nenhuma regra de CSS e editada: so o
# valor dentro dela.
PALETA = [
    ('#1E9E5F', '#BE123C'), ('#1e9e5f', '#be123c'),   # accent
    ('#3FD489', '#F43F5E'), ('#3fd489', '#f43f5e'),   # accent-light
    ('rgba(30,158,95', 'rgba(190,18,60'),
    ('rgba(30, 158, 95', 'rgba(190, 18, 60'),
]

# Nome e slug: o shell e do MODELO, e o builder troca por aluno.
NOMES = [
    ('dante-blecker-gregory', 'helen-mendes'),
    ('Dante Blecker Gregory', 'Helen Mendes'),
    ('Dante', 'Helen'),
    ('DANTE', 'HELEN'),
]


def fecha_tag(s, i, tag):
    """Indice logo APOS o fechamento da tag aberta em i. Por BALANCO, nunca pelo
    primeiro </div> — o primeiro fecha um filho."""
    depth = 0
    for m in re.finditer(r'<' + tag + r'\b|</' + tag + r'\s*>', s[i:]):
        depth += 1 if not m.group(0).startswith('</') else -1
        if depth == 0:
            return i + m.end()
    raise SystemExit(f'tag <{tag}> aberta em {i} nao fecha')


def remove(s, abertura_rx, tag, quantos=None):
    """Remove elementos inteiros cuja tag de abertura casa a regex."""
    n = 0
    while True:
        m = re.search(abertura_rx, s)
        if not m:
            break
        s = s[:m.start()] + s[fecha_tag(s, m.start(), tag):]
        n += 1
        if quantos and n >= quantos:
            break
    return s, n


def deriva():
    with open(ARTEFATO, encoding='utf-8') as fh:
        s = fh.read()
    rel = {}

    # 1. FORA A AULA 2 — o molde carrega UMA aula de exemplo.
    for nome, rx, tag in [
        ('slides',        r'<div class="slide[^"]*"[^>]*data-lesson="2"[^>]*>', 'div'),
        ('phase-bar',     r'<div class="phase-bar"[^>]*data-lesson="2"[^>]*>', 'div'),
        ('phase-labels',  r'<div class="phase-labels"[^>]*data-lesson="2"[^>]*>', 'div'),
        ('plano',         r'<div class="pv-plan"[^>]*data-plan-body="2"[^>]*>', 'div'),
        ('percurso',      r'<div class="pv-post"[^>]*data-post-body="2"[^>]*>', 'div'),
        ('pill',          r'<button class="pv-pill"[^>]*data-plan="2"[^>]*>', 'button'),
        ('card-inclass',  r'<button class="pv-card"[^>]*data-aula="2"[^>]*>', 'button'),
        ('card-postclass', r'<button class="pv-card"[^>]*data-post="2"[^>]*>', 'button'),
    ]:
        s, n = remove(s, rx, tag)
        rel[f'aula2/{nome}'] = n

    # O DADO da aula 2 tambem sai. O deck e data-driven: LESSONS['N'] = {hubLabel,
    # story, frame, build, imageQuiz, reset} alimenta as 10 telas. Deixar o objeto
    # da aula 2 num shell sem os slides dela e carregar conteudo do Dante para
    # dentro do molde — e o base_swaps nao tem como saber que aquilo e conteudo.
    m = re.search(r"LESSONS\['2'\]\s*=\s*\{", s)
    if m:
        depth, j = 0, m.end() - 1
        for t in re.finditer(r'\{|\}', s[j:]):
            depth += 1 if t.group(0) == '{' else -1
            if depth == 0:
                fim = j + t.end()
                break
        while fim < len(s) and s[fim] in ';\n\r\t ':
            fim += 1
        s = s[:m.start()] + s[fim:]
        rel['aula2/LESSONS'] = 1

    # O payload do percurso 2 sai do PV_POSTS pela CHAVE, nao por corte de texto.
    i = s.index('var PV_POSTS = ')
    import json
    obj, fim = json.JSONDecoder().raw_decode(s[i + len('var PV_POSTS = '):])
    obj.pop('2', None)
    s = (s[:i] + 'var PV_POSTS = ' + json.dumps(obj, ensure_ascii=False)
         + s[i + len('var PV_POSTS = ') + fim:])
    rel['aula2/payload'] = 1

    # 2. LITERAIS DO MODELO no lugar dos do Dante.
    for velho, novo in PALETA + NOMES:
        antes = s.count(velho)
        s = s.replace(velho, novo)
        rel[f'swap/{velho}'] = antes

    # 3. MARCADORES DE FECHO que o replace_between do builder ancora. O artefato
    #    fecha as abas com </div> mudo; sem o comentario o builder pega o </div>
    #    do primeiro filho (e o mesmo motivo do fim_da_aba no insert_hub).
    for tab in ('planning', 'inclass', 'postclass'):
        m = re.search(r'<div class="tab-content[^"]*" id="tab-' + tab + r'">', s)
        j = fecha_tag(s, m.start(), 'div')
        s = s[:j] + f'<!-- /tab-{tab} -->' + s[j:]
        rel[f'marcador/tab-{tab}'] = 1
    m = re.search(r'<div class="slides-container" id="slidesContainer">', s)
    j = fecha_tag(s, m.start(), 'div')
    s = s[:j] + '<!-- /slides-container -->' + s[j:]
    rel['marcador/slides-container'] = 1

    return s, rel


# O card do menu IN CLASS no hub e um LINK, nao um botao que abre inline: no
# artefato as duas aulas moram no mesmo documento, aqui cada uma tem URL. A
# INTERFACE continua a do artefato (.pv-card e as tres spans) — muda o elemento
# que a carrega, que e plumbing de producao. O insert_hub reconhece este formato
# e emite o card das proximas aulas igual (menu_card_do_hub).
CARD_HUB = ('<a class="pv-card" href="/{pasta}/helen-mendes-aula1.html?autostart=1">'
            '<span class="pv-card-n">01</span><span>'
            '<span class="pv-card-t">Dragon Rider</span>'
            '<span class="pv-card-m">He can fly, but he can\u2019t swim. \u00b7 6 stages</span>'
            '</span></a>')


# A UNICA LINHA DE JS QUE O SPLIT OBRIGA A MEXER, e por que.
#
# O boot do artefato abre com
#     PRISTINE_SLIDES = document.getElementById('slidesContainer').innerHTML;
# porque no artefato SEMPRE ha deck: as duas aulas moram no mesmo documento. No
# hub nao ha — o deck foi para o standalone —, entao o getElementById devolve
# null e o boot inteiro morre na primeira linha. Medido no chromium headless,
# nos dois hubs: "Uncaught TypeError: Cannot read properties of null (reading
# 'innerHTML')". Nada depois disso rodava: nem a restauracao da velocidade de
# audio, nem o resto. Sem abrir no navegador isso nao aparece — o HTML e valido,
# os handlers compilam, e todo gate estatico fica verde.
#
# O conserto e um GUARDA, nao uma reescrita: a parte do deck passa a rodar so
# quando ha deck; o que e do hub (velocidade do audio) roda sempre. E divergencia
# por LIMITACAO DO ARTEFATO — a categoria que o anatomias.json ja tem para
# "aqui o molde nao copia, de proposito, porque o artefato tem uma limitacao que
# ele resolve". Uma pagina do claude.ai nunca precisou existir sem deck.
BOOT_ARTEFATO = """  PRISTINE_SLIDES = document.getElementById('slidesContainer').innerHTML;   // foto pristina
  coreBuildAll();
  /* a contagem sai da AULA ATIVA, nao de todos os slides do documento */
  totalSlides = slidesDaAula().length;
  mostrarBarraDaAula();
  buildSlideDots();
  var hc = document.getElementById('hubSlideCount');
  if (hc && LESSON.hubLabel) hc.innerHTML = LESSON.hubLabel + ' &middot; ' + totalSlides + ' slides';
  updateNav();
"""

BOOT_HUB = """  /* SPLIT: o hub nao tem deck (ele mora em {slug}-aula{N}.html). Sem esta guarda
     o boot morre aqui e nem a velocidade do audio e restaurada. */
  var _sc = document.getElementById('slidesContainer');
  if (_sc) {
    PRISTINE_SLIDES = _sc.innerHTML;   // foto pristina
    coreBuildAll();
    /* a contagem sai da AULA ATIVA, nao de todos os slides do documento */
    totalSlides = slidesDaAula().length;
    mostrarBarraDaAula();
    buildSlideDots();
    var hc = document.getElementById('hubSlideCount');
    if (hc && LESSON.hubLabel) hc.innerHTML = LESSON.hubLabel + ' &middot; ' + totalSlides + ' slides';
    updateNav();
  }
"""

AUTOSTART_ARTEFATO = """  if (window.location.hash === '#slides' || new URLSearchParams(window.location.search).get('autostart')) {
    setTimeout(enterSlideMode, 100);
  }
"""
AUTOSTART_HUB = """  if (_sc && (window.location.hash === '#slides' || new URLSearchParams(window.location.search).get('autostart'))) {
    setTimeout(enterSlideMode, 100);
  }
"""


def tira_aba(s, nome):
    """Remove a aba `nome`: o botao e o corpo. Usada para repartir o artefato."""
    s, _ = remove(s, r'<button class="tab-btn[^"]*"[^>]*data-tab="' + nome + r'"[^>]*>',
                  'button', quantos=1)
    m = re.search(r'<div class="tab-content[^"]*" id="tab-' + nome + r'">', s)
    if m:
        j = fecha_tag(s, m.start(), 'div')
        j = s.index('-->', j) + 3          # leva junto o marcador de fecho
        s = s[:m.start()] + s[j:]
    return s


def primeira_aba_ativa(s):
    """A 1a aba que sobrou tem de nascer aberta — senao o hub abre em branco."""
    s = s.replace('class="tab-btn active"', 'class="tab-btn"')
    s = s.replace('class="tab-content active"', 'class="tab-content"')
    s = re.sub(r'<button class="tab-btn"', '<button class="tab-btn active"', s, count=1)
    return re.sub(r'<div class="tab-content"', '<div class="tab-content active"', s, count=1)


def variante_standalone(s):
    """A aula: Planejamento + In Class + o deck. O percurso mora no hub."""
    s = tira_aba(s, 'postclass')
    s, _ = remove(s, r'<div class="pv-post"[^>]*>', 'div')
    i = s.index('var PV_POSTS = ')
    import json
    _, fim = json.JSONDecoder().raw_decode(s[i + len('var PV_POSTS = '):])
    s = s[:i] + 'var PV_POSTS = {}' + s[i + len('var PV_POSTS = ') + fim:]
    return primeira_aba_ativa(s)


def variante_hub(s, aluno=False):
    """O hub: menus e percurso. O deck (slides-wrapper) mora no standalone."""
    s, _ = remove(s, r'<div class="slides-wrapper">', 'div')
    for antes, depois in ((BOOT_ARTEFATO, BOOT_HUB), (AUTOSTART_ARTEFATO, AUTOSTART_HUB)):
        if antes not in s:
            raise SystemExit('o boot do artefato mudou — reveja a guarda do split '
                             '(BOOT_ARTEFATO no extrator)')
        s = s.replace(antes, depois, 1)
    if aluno:
        s = tira_aba(s, 'planning')
        s = tira_aba(s, 'inclass')
        s, _ = remove(s, r'<div class="pv-pills">', 'div')
        s = s.replace('<span class="prof-badge">Professor View</span>',
                      '<span class="prof-badge">Aluno</span>')
    else:
        # o card do menu vira link para o standalone
        m = re.search(r'<button class="pv-card"[^>]*data-aula="1"[^>]*>', s)
        j = fecha_tag(s, m.start(), 'button')
        s = s[:m.start()] + CARD_HUB.format(pasta='professor') + s[j:]
    return primeira_aba_ativa(s)


def main():
    base, rel = deriva()
    saidas = [
        (SHELL, variante_standalone(base)),
        (HUB, variante_hub(base)),
        (HUB_ALUNO, variante_hub(base, aluno=True)),
    ]
    if '--check' in sys.argv:
        ruim = 0
        for caminho, esperado in saidas:
            nome = os.path.relpath(caminho, RAIZ)
            if not os.path.exists(caminho):
                print(f'FALTA {nome}')
                ruim += 1
            elif open(caminho, encoding='utf-8').read() != esperado:
                print(f'DIVERGE {nome}: nao e o que a derivacao produz hoje '
                      f'(editado a mao, ou o artefato mudou)')
                ruim += 1
        if ruim:
            return 1
        print('OK — os 3 shells no disco sao exatamente o artefato repartido, '
              'com os literais do modelo.')
        return 0
    os.makedirs(SHELLS, exist_ok=True)
    for caminho, conteudo in saidas:
        with open(caminho, 'w', encoding='utf-8') as fh:
            fh.write(conteudo)
        print(f'escrito {os.path.relpath(caminho, RAIZ):46} ({len(conteudo)/1024:5.0f} KB)')
    for k, v in rel.items():
        print(f'  {k:34} {v}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
