#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta o material da anatomia `consultivo` a partir do shell e dos fragmentos da aula.

O QUE O BUILDER FAZ, E O QUE ELE NAO FAZ
----------------------------------------
FAZ: pega o shell (a FORMA, derivada do artefato por extrai_shell.py) e enfia nele o
REGISTRO do aluno e os FRAGMENTOS de cada aula. Emite os DOIS builds -- professor e aluno --
e o do aluno sai da mesma funcao que o extrator usa, `deriva_aluno`. Isso importa: o
isolamento nao e uma lista de cuidados que o builder repete, e uma propriedade estrutural do
caminho. Aula nova nao pode "esquecer" de isolar.

NAO FAZ: conteudo. Quem escreve a aula e quem escreve a aula. O builder monta, confere o que
da para conferir por construcao, e recusa se nao fechar.

O CIRCULO QUE PROVA QUE ELE REPRODUZ
------------------------------------
    artefato -> extrai_fragmentos -> builder -> material == artefato

`--round-trip` monta com os fragmentos tirados do proprio artefato e compara REGIAO POR
REGIAO com ele. Se o builder perder alguma coisa no caminho, o gate diz qual regiao e quantos
bytes. E o "prove o superset" do P2 §38 aplicado a geracao.

ASSERTS DE BUILD (recusam a geracao, nao o PR)
----------------------------------------------
  - as OITO etapas do framework, na ordem declarada, com os minutos fechando o percurso
    (Doc 03; Stephanie, 24/08/2026). NUNCA oito telas: uma etapa pode ocupar varias, e duas
    podem dividir uma.
  - o pre-class com exatamente SEIS atividades reais (Doc 04 §4.2)
  - o Teacher's Guide com os CATORZE campos (Doc 04 §8.1)

USO:
    python3 scripts/consultivo/build_consultivo.py _build/consultivo/{slug}/config.json
    python3 scripts/consultivo/build_consultivo.py --round-trip
"""
import importlib.util
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SHELL = os.path.join(RAIZ, "_build", "model", "shells", "consultivo.html")
ARTEFATO = os.path.join(RAIZ, "_build", "model", "artefatos", "marcos-consultivo.html")

_spec = importlib.util.spec_from_file_location(
    "extrai_shell", os.path.join(os.path.dirname(os.path.abspath(__file__)), "extrai_shell.py"))
extrai_shell = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(extrai_shell)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audio_surface  # noqa: E402  a MESMA lista que o gerador usa
import render  # noqa: E402  o builder EMITE o exercicio -- ver o cabecalho de render.py

CAMPOS_GUIA = ["identity", "goals", "product", "criteria", "prep", "language", "transcript",
               "difficulties", "scaffolding", "feedback", "evidence", "prepost", "key"]
ETAPAS = 8
PERCURSO_MIN = 55


def mascara(s):
    return extrai_shell.mascara_script_style(s)


def fecha(s, i, tag="div"):
    return extrai_shell.fecha_tag(s, i, tag)


def troca_bloco_por_id(html, ident, novo, tag="div"):
    hm = mascara(html)
    m = re.search(r"<" + tag + r'[^>]*id="' + re.escape(ident) + r'"[^>]*>', hm)
    if not m:
        raise SystemExit(f"o shell nao tem o bloco id={ident!r}")
    return html[:m.start()] + novo + html[fecha(hm, m.start(), tag):]


def troca_var(js, nome, valor):
    """Troca `var NOME = <objeto ou array>` inteiro.

    O delimitador importa: `fim_do_bloco` conta CHAVES, e num array de objetos a primeira
    chave e a do PRIMEIRO ELEMENTO. Usado sem distinguir, ele trocou apenas
    `{n:'Nadia',g:'f'}` e deixou `,{n:'Tom',g:'m'}];` pendurado -- JS invalido, e a pagina
    inteira morreu com "Invalid destructuring assignment target". Quem pegou foi o GATE 35,
    no navegador; nenhuma checagem de texto veria isso."""
    m = re.search(r"^var " + re.escape(nome) + r"\s*=", js, re.M)
    if not m:
        raise SystemExit(f"o shell nao declara var {nome}")
    resto = js[m.end():].lstrip()
    if resto[:1] == "[":
        i = js.index("[", m.end())
        prof, k = 0, i
        while k < len(js):
            if js[k] == "[":
                prof += 1
            elif js[k] == "]":
                prof -= 1
                if prof == 0:
                    break
            k += 1
        fim = k + 1
    else:
        fim = extrai_shell.fim_do_bloco(js, m.end())
    return js[:m.start()] + f"var {nome}={valor}" + js[fim:]




CRITERIOS_AVAL = [
    ("fala", "Fala e interacao",
     "Capacidade de manter e desenvolver a interacao oral com autonomia crescente."),
    ("escuta", "Compreensao auditiva",
     "Capacidade de compreender informacao oral e reagir de forma pertinente."),
    ("precisao", "Precisao estrutural",
     "Estabilidade de forma quando a atencao esta na mensagem."),
]

# O cartao da aula na aba In-class. Ele vinha do artefato com o conteudo do MARCOS --
# titulo, objetivo, produto e a preparacao das aulas dele. hubPaint/lessonsPaint repintam o
# percurso e as etapas, mas nao o resto: o material da Stephanie abria a aba In-class
# descrevendo uma recepcao de congresso de valuation. Residuo de outro perfil (Doc 04 §12.1),
# e quem o encontrou primeiro foi o CATALOGO DE MODELOS, que le o cabecalho para descrever a
# persona e descreveu a Stephanie com o perfil do Marcos.
CARTAO = """<div class="lesson-card" id="lc{n}">
        <div class="lc-head">
          <span class="lc-badge">Aula {nn}</span>
          <span class="lc-fw">Bloco {bloco} &middot; {mod} / {cod}</span>
          <span class="lc-status" id="lcst{n}">N&atilde;o iniciada</span>
        </div>
        <h3 class="lc-title">{tema}</h3>
        <p class="lc-desc">{objetivo}</p>
        <p class="lc-meta">{telas} telas &middot; {minutos} min de percurso essencial</p>
        <div class="btn-bar" style="justify-content:flex-start;margin-top:var(--space-3)">
          <button class="btn-ghost" data-painel="lcprep{n}" aria-expanded="false" onclick="cartaoPainel('lcprep{n}',this)">Estrutura e prepara&ccedil;&atilde;o</button>
          <button class="btn-primary" onclick="openLesson({n})">Abrir a aula</button>
          <button class="btn-ghost" data-view="professor" onclick="tgAbrir({n},this)"><span>Abrir o <span lang="en">Teacher&rsquo;s Guide</span></span></button>
          <button class="btn-ghost" data-painel="lcfb{n}" aria-expanded="false" onclick="cartaoPainel('lcfb{n}',this)">Registro p&oacute;s-aula</button>
        </div>
        <p class="tg-aviso-cartao" id="tgAviso{n}" data-view="professor" hidden="">O navegador n&atilde;o abriu a janela. O Teacher&rsquo;s Guide continua dispon&iacute;vel dentro da aula.</p>
        <div id="lcprep{n}" style="display:none;margin-top:var(--space-4)">
          <h5 class="prep-h">A &middot; Objetivo e produto</h5>
          <p class="prep-p"><strong>Objetivo comunicativo:</strong> {objetivo}</p>
          <p class="prep-p"><strong>Produto principal:</strong> {produto}</p>
          <h5 class="prep-h">B &middot; Percurso da aula</h5>
          <p class="prep-p" data-lf="percurso"></p>
          <p class="prep-p" data-lf="etapas"></p>
          <h5 class="prep-h">C &middot; Antes de abrir a aula</h5>
          <ul class="prep-list">{preparar}</ul>
        </div>
        <div id="lcfb{n}" style="display:none;margin-top:var(--space-4)">
          <div class="fb-grid">
            <div class="fb-item"><label for="af{n}-data">Data de realiza&ccedil;&atilde;o</label><input type="date" id="af{n}-data" class="blank-input" data-k="af_l{n}_data" oninput="persSave(this)"></div>
            <div class="fb-item"><label for="af{n}-status">Status</label><select id="af{n}-status" data-k="af_l{n}_status" onchange="persSave(this)"><option value="" selected="selected">N&atilde;o iniciada</option><option value="Em andamento">Em andamento</option><option value="Realizada">Realizada</option></select></div>
          </div>
          <h5 class="prep-h">Desempenho &mdash; mesma escala nas aulas do bloco</h5>
          <div class="aval-grid">{aval}</div>
          <h5 class="prep-h">Engajamento</h5>
          <div class="aval-item"><p class="aval-crit">Engajamento</p><p class="aval-desc">Participa&ccedil;&atilde;o e envolvimento. Fica FORA da m&eacute;dia de desempenho lingu&iacute;stico.</p><div class="aval-escala" data-esc="engaj" data-aval="af_l{n}_engaj" role="radiogroup" aria-label="Engajamento"></div></div>
          <div class="fb-grid">
            <div class="fb-item"><label for="af{n}-evidencia">Evid&ecirc;ncia observ&aacute;vel</label><textarea id="af{n}-evidencia" class="writebox" data-k="af_l{n}_evidencia" oninput="persSave(this)"></textarea></div>
            <div class="fb-item"><label for="af{n}-dificuldade">Ponto priorit&aacute;rio de desenvolvimento</label><textarea id="af{n}-dificuldade" class="writebox" data-k="af_l{n}_dificuldade" oninput="persSave(this)"></textarea></div>
            <div class="fb-item"><label for="af{n}-acao">Pr&oacute;xima a&ccedil;&atilde;o</label><textarea id="af{n}-acao" class="writebox" data-k="af_l{n}_acao" oninput="persSave(this)"></textarea></div>
          </div>
          <h5 class="prep-h">O que chega ao aluno</h5>
          <div class="fb-grid">
            <div class="fb-item"><label for="sf{n}-worked-in">What worked</label><textarea id="sf{n}-worked-in" class="writebox" data-k="sfb_l{n}_worked" oninput="persSave(this)"></textarea></div>
            <div class="fb-item"><label for="sf{n}-develop-in">Keep developing</label><textarea id="sf{n}-develop-in" class="writebox" data-k="sfb_l{n}_develop" oninput="persSave(this)"></textarea></div>
          </div>
          <p class="aval-desc" id="avalSalvo{n}"></p>
        </div>
      </div>"""


# O bloco de feedback de UMA aula, na aba do aluno. Byte-a-byte igual ao do artefato --
# travessao LITERAL, nao `&mdash;`: a diferenca de 18 bytes por bloco foi o que o
# `--round-trip` acusou na primeira versao, e e exatamente para isso que ele existe.
FEEDBACK_BLOCO = """<div id="sf{n}"{oculto}>
    <h3 class="sub">Lesson {n:02d} — <em>{tema}</em></h3>
    <div class="brief" id="sf{n}-box" style="display:none">
      <dl>
        <dt>What worked</dt><dd id="sf{n}-worked">—</dd>
        <dt>Keep developing</dt><dd id="sf{n}-develop">—</dd>
      </dl>
    </div>
    <p class="subprompt" id="sf{n}-empty" style="display: block;">Feedback will be available after the lesson.</p>
  </div>"""


def cartao_de_aula(n, reg, dados, telas, minutos):
    def campo(nome, padrao=""):
        m = re.search(nome + r":'([^']*)'", reg)
        return m.group(1) if m else padrao
    aval = "".join(
        '<div class="aval-item"><p class="aval-crit">%s</p><p class="aval-desc">%s</p>'
        '<div class="aval-escala" data-aval="af_l%d_%s" role="radiogroup" aria-label="%s">'
        '</div></div>' % (rot, desc, n, k, rot)
        for k, rot, desc in CRITERIOS_AVAL)
    return CARTAO.format(
        n=n, nn="%02d" % n,
        bloco=(re.search(r"bloco:(\d+)", reg) or [None, "1"])[1],
        mod=campo("mod"), cod=campo("cod"), tema=campo("tema"),
        objetivo=dados.get("objetivo", ""), produto=dados.get("produto", ""),
        telas=telas, minutos=minutos,
        preparar="".join("<li>%s</li>" % x for x in dados.get("preparar", [])),
        aval=aval)


def troca_blocos_de_aula(html, tab_id, prefixo, seletor, aulas, rotulos, conteudos):
    """Refaz, dentro de uma aba, a barra de selecao de aula e os blocos por aula.

    O shell traz os blocos do MODELO (`pc19`, `pc20`) e os botoes que alternam entre eles.
    Um material de outras aulas nao tem onde encaixar: procurar `pc1` no shell devolve nada,
    e foi assim que a primeira geracao parou. Aqui a regiao inteira e reconstruida a partir
    do config -- quantas aulas ele declarar, tantos botoes e tantos blocos.
    """
    hm = mascara(html)
    m = re.search(r'<div[^>]*id="' + tab_id + r'"[^>]*>', hm)
    if not m:
        raise SystemExit(f"o shell nao tem a aba id={tab_id!r}")
    ini_aba, fim_aba = m.start(), fecha(hm, m.start())

    # 1. a barra de selecao: e a que chama o seletor desta aba
    barras = [mm for mm in re.finditer(r'<div class="btn-bar"[^>]*>', hm[ini_aba:fim_aba])]
    alvo = None
    for mm in barras:
        a = ini_aba + mm.start()
        b = fecha(hm, a)
        if f"{seletor}(" in html[a:b]:
            alvo = (a, b)
            break
    if alvo is None:
        raise SystemExit(f"{tab_id}: nao achei a barra que chama {seletor}()")
    botoes = []
    for i, n in enumerate(aulas):
        cls = "btn-primary" if i == 0 else "btn-ghost"
        pt, en = rotulos[n]
        botoes.append(f'<button class="{cls}" id="{prefixo}b{n}" onclick="{seletor}({n})">'
                      f'<span data-view="professor">{pt}</span>'
                      f'<span data-view="aluno">{en}</span></button>')
    nova_barra = ('<div class="btn-bar" style="justify-content:flex-start;'
                  'margin-bottom:var(--space-4)">\n    ' + "\n    ".join(botoes) + "\n  </div>")
    html = html[:alvo[0]] + nova_barra + html[alvo[1]:]

    # 2. os blocos por aula: do primeiro ao fim do ultimo
    hm = mascara(html)
    m = re.search(r'<div[^>]*id="' + tab_id + r'"[^>]*>', hm)
    ini_aba, fim_aba = m.start(), fecha(hm, m.start())
    blocos = [mm for mm in re.finditer(r'<div[^>]*id="' + prefixo + r'\d+"[^>]*>',
                                       hm[ini_aba:fim_aba])]
    if not blocos:
        raise SystemExit(f"{tab_id}: nao achei os blocos {prefixo}N do modelo")
    a = ini_aba + blocos[0].start()
    b = fecha(hm, ini_aba + blocos[-1].start())
    return html[:a] + "\n".join(conteudos) + html[b:]


def expande_blocos(fragmento, decl, usadas, rotulo):
    """Troca `<!--BLOCOS:chave-->` pelo HTML das atividades declaradas em `blocos.json`.

    Sem placeholder = no-op: a aula que ainda escreve HTML a mao fica byte-a-byte igual, e a
    migracao pode ser feita um exercicio por vez. Isso importa mais do que parece -- migrar
    tudo de uma vez seria reescrever, e reescrever no porte foi o que produziu o inventario
    falso que o GATE 20 teve de consertar depois.

    O `usadas` e COMPARTILHADO pelos tres fragmentos da aula de proposito: o `blocos.json` e
    por AULA, e uma chave declarada pode ser consumida pelo pre-class, pelo post-class ou
    pelos slides. Conferir "declarado e nao usado" fragmento a fragmento acusa a primeira
    chave em todo build -- foi o que a primeira versao fez, e o proprio assert pegou.
    """
    # O vocabulario que a AULA ensina, nao o da seccao.
    #
    # Cada `<!--BLOCOS:chave-->` e uma chamada isolada de `render.blocos`, entao uma seccao
    # nunca ve as irmas -- e o gap-fill do pre-class ficava sem saber que o `par` da seccao
    # 2 tinha ensinado justamente aquelas palavras. Resultado: um gap-fill de vocabulario
    # era classificado como de gramatica, e o builder recusava o banco que a REGRA 2.4 exige.
    vocab_da_aula = set()
    for blocos_da_chave in decl.values():
        vocab_da_aula |= render.vocab_da_regiao(blocos_da_chave)

    def sub(m):
        chave = m.group(1).strip()
        if chave not in decl:
            raise SystemExit(f"{rotulo}: placeholder BLOCOS:{chave} sem entrada no "
                             f"blocos.json da aula")
        usadas.add(chave)
        return render.blocos(decl[chave], vocab_da_aula)

    # Consome o recuo que vem ANTES do placeholder: quem manda na indentacao do bloco e o
    # render, e nao o lugar onde o comentario foi escrito. Sem isto o bloco sai com o recuo
    # do placeholder MAIS o proprio, e o material deixa de ser byte-a-byte igual -- que e
    # exatamente a prova que este caminho precisa dar.
    return re.sub(r"[ \t]*<!--\s*BLOCOS:([^>]+?)\s*-->", sub, fragmento)


def blocos_da_aula(pasta):
    caminho = os.path.join(pasta, "blocos.json")
    return json.load(open(caminho, encoding="utf-8")) if os.path.exists(caminho) else {}


def troca_slides(html, por_aula):
    """Substitui TODAS as telas do deck pelas das aulas pedidas, na ordem, e renumera
    data-slide -- o numero e posicao no deck, nao identidade da tela."""
    hm = mascara(html)
    m = re.search(r'<div class="slides-container"[^>]*>|<div class="slides-wrapper"[^>]*>', hm)
    if not m:
        raise SystemExit("o shell nao tem o container do deck")
    # o container das telas e o filho que as guarda: acha a primeira tela e a ultima
    prim = re.search(r'<div class="slide[^"]*"[^>]*data-lesson="\d+"[^>]*>', hm)
    if not prim:
        raise SystemExit("o shell nao tem tela com data-lesson")
    ini = prim.start()
    fim = ini
    for mm in re.finditer(r'<div class="slide[^"]*"[^>]*data-lesson="\d+"[^>]*>', hm):
        fim = fecha(hm, mm.start(), "div")
    novo = "\n\n".join(por_aula)
    k = 0
    def renumera(mo):
        nonlocal k
        k += 1
        return f'data-slide="{k}"'
    novo = re.sub(r'data-slide="\d+"', renumera, novo)
    return html[:ini] + novo + html[fim:], k


def monta(cfg, base_frag):
    html = open(SHELL, encoding="utf-8").read()
    aulas = cfg["aulas"]

    # ---- registro
    lessons, guides, slides, erros = [], [], [], []
    # O blocos.json e por AULA e e consumido por TRES fragmentos, que o builder monta em
    # lacos diferentes. Por isso a declaracao e o conjunto de chaves usadas vivem aqui
    # fora, e a conferencia de "declarado e nao usado" acontece no fim, quando os tres ja
    # passaram. Confendo dentro do laco, o primeiro fragmento acusava sempre.
    # ---- os fragmentos existem ANTES de qualquer leitura
    #
    # Sem isto, aula sem fragmento estourava um FileNotFoundError cru no meio do `monta` --
    # e essa e a condicao MAIS COMUM de todas: a primeira geracao de um aluno novo, em que
    # o config ja existe e o conteudo ainda nao. A pilha de excecao nao diz o que falta nem
    # onde, e faz parecer defeito do builder o que e trabalho por fazer.
    OBRIGATORIOS = ("registro.js", "guide.js", "slides.html", "preclass.html",
                    "postclass.html")
    faltando = []
    for n in aulas:
        pasta = os.path.join(base_frag, f"aula{n}")
        if not os.path.isdir(pasta):
            faltando.append(f"    aula {n}: a pasta {os.path.relpath(pasta, RAIZ)} nao existe")
            continue
        for arq in OBRIGATORIOS:
            if not os.path.exists(os.path.join(pasta, arq)):
                faltando.append(f"    aula {n}: falta {arq}")
    if faltando:
        return "", 0, ["fragmento(s) ausente(s) — nada foi escrito:\n" + "\n".join(faltando)]

    declarado = {n: blocos_da_aula(os.path.join(base_frag, f"aula{n}")) for n in aulas}
    usado = {n: set() for n in aulas}
    for n in aulas:
        pasta = os.path.join(base_frag, f"aula{n}")
        reg = open(os.path.join(pasta, "registro.js"), encoding="utf-8").read().strip()
        gui = open(os.path.join(pasta, "guide.js"), encoding="utf-8").read().strip()
        lessons.append(f" {n}:{reg}")
        guides.append(f" {n}:{gui}")
        slides.append(expande_blocos(
            open(os.path.join(pasta, "slides.html"), encoding="utf-8").read().strip(),
            declarado[n], usado[n], f"aula {n} slides"))

    ini = html.rfind("<script>")
    cabeca, js = html[:ini], html[ini:]
    js = troca_var(js, "ARTEFATO", "{id:%r}" % cfg["artefato_id"])
    js = troca_var(js, "ALUNO", "{nome:%r,sobrenome:%r}" % (cfg["aluno"]["nome"],
                                                            cfg["aluno"]["sobrenome"]))
    c = cfg["ciclo"]
    js = troca_var(js, "CICLO",
                   "{numero:%d,aulas:%d,primeira:%d,porBloco:%d,nivel:%r,"
                   "rotulo:'Aulas neste ciclo',rotuloAluno:'Lessons in this cycle'}"
                   % (c["numero"], c["aulas"], c["primeira"], c["porBloco"], c["nivel"]))
    js = troca_var(js, "LESSONS", "{\n" + ",\n".join(lessons) + "\n}")
    js = troca_var(js, "GUIDE", "{\n" + ",\n".join(guides) + "\n}")
    # ---- a chave de progresso tem de ter O ALUNO dentro
    #
    # Vinha do `artefato_id` ('pv_consultivo-c01-01-20_v1'): o CICLO e o intervalo de aulas,
    # sem nada que distinga uma pessoa da outra. Como localStorage e por ORIGEM, dois alunos
    # de mesmo ciclo abertos no mesmo navegador -- o da professora, no dia a dia -- gravavam
    # um por cima do outro. Nada avisa: o segundo material simplesmente abre com o progresso
    # do primeiro, coerente e errado.
    #
    # Agora e `pv_{slug}-c{N}_v1`. O ciclo continua na chave porque o material E por ciclo:
    # quando o aluno passar ao ciclo 2, o progresso do 1 fica onde esta, em vez de ser
    # sobrescrito pelo material novo.
    chave = "pv_%s-c%02d_v1" % (re.sub(r"[^A-Za-z0-9_-]", "-", cfg["slug"]), c["numero"])
    js = js.replace("var STORE='pv_consultivo-modelo_v1';", "var STORE='%s';" % chave)
    js = js.replace("localStorage.getItem('pv_consultivo-modelo_v1')",
                    "localStorage.getItem('%s')" % chave)
    # ---- o que o artefato deixou CRAVADO em numero de aula
    #
    # O boot do artefato chama `closeBuild(19,RECAP19,CONF19); closeBuild(20,...)`, a tabela
    # BUILDERS aponta para os hosts `recapList19`/`recapList20`, e o post-class restaura por
    # ids `pw19-*`. Sao os numeros das DUAS aulas dele. Copiados como estao, a aula 1 de
    # qualquer aluno nasceria muda: o fecho nao se constroi e o texto do post-class nao volta
    # -- sem erro no console, porque `if(!host)return` engole tudo.
    #
    # Numero que descreve o MODELO e nao o MATERIAL trunca em silencio. Aqui tudo isso sai do
    # registro: quantas aulas o config declarar, tantas chamadas e tantos hosts.
    for velho in sorted(set(re.findall(r"\bvar (RECAP\d+|CONF\d+)\s*=", js))):
        js = extrai_shell.remove_var(js, velho, {})

    # PC_NOTAS: a camada do professor no pre-class. Guarda SO o que nao existe em lugar
    # nenhum do material -- alternativas que a correcao nao aceita mas o professor deve, o
    # porque, o que costuma travar, a ligacao com a aula. O gabarito em si NAO entra aqui: ele
    # e derivado do `data-ok` da propria atividade, para nao existir uma segunda versao da
    # mesma informacao, livre para divergir da primeira.
    notas = {}
    for n in aulas:
        nj = os.path.join(base_frag, f"aula{n}", "notas.json")
        if os.path.exists(nj):
            notas.update(json.load(open(nj, encoding="utf-8")))
    if notas:
        js = troca_var(js, "PC_NOTAS", json.dumps(notas, ensure_ascii=False, indent=1))

    # TALKS: o dialogo de cada aula que tem um. O shell traz o do artefato; um material de
    # outro aluno com o dialogo do Marcos e o mesmo defeito do cabecalho, so que audivel.
    talks = {}
    for n in aulas:
        tj = os.path.join(base_frag, f"aula{n}", "talk.json")
        if os.path.exists(tj):
            falas = json.load(open(tj, encoding="utf-8"))
            if falas:
                talks[str(n)] = falas
    # O ELENCO e do MATERIAL, nao do artefato. `CAST` casa o indice do falante com um nome e
    # um genero, e e o que o transcript imprime e o que escolhe a voz. Ficando o do artefato,
    # a call de tres vozes da Stephanie sairia com dois nomes do congresso do Marcos -- e o
    # terceiro falante nao teria nome nenhum. Os indices das falas apontam para esta lista.
    if cfg.get("cast"):
        js = troca_var(js, "CAST", "[" + ",".join(
            "{n:%s,g:%s}" % (json.dumps(c["n"], ensure_ascii=False),
                             json.dumps(c["g"], ensure_ascii=False))
            for c in cfg["cast"]) + "]")

    if talks:
        js = troca_var(js, "TALKS", "{" + ",".join(
            "%s:[%s]" % (k, ",".join('{s:%d,t:%s}' % (f["s"], json.dumps(f["t"], ensure_ascii=False))
                                      for f in v))
            for k, v in talks.items()) + "}")
    else:
        js = troca_var(js, "TALKS", "{}")
    chamadas, restaura = [], []
    for n in aulas:
        cj = os.path.join(base_frag, f"aula{n}", "close.json")
        if not os.path.exists(cj):
            erros.append(f"aula {n}: falta close.json (o recap e a escala de confianca do "
                         f"fecho). Sem ele a ultima tela nasce vazia, e sem erro no console.")
        else:
            fecho = json.load(open(cj, encoding="utf-8"))
            js = js.replace("\n/* ---------------- boot",
                            "\nvar RECAP%d=%s;\nvar CONF%d=%s;\n/* ---------------- boot"
                            % (n, json.dumps(fecho["recap"], ensure_ascii=False),
                               n, json.dumps(fecho["conf"], ensure_ascii=False)), 1)
            chamadas.append(f"closeBuild({n},RECAP{n},CONF{n});")
        restaura.append("['pw%d-subject',null,'post_l%d_subject'],"
                        "['pw%d-body','pw%d-count','post_l%d_writing']" % (n, n, n, n, n))

    # DENTRO DO BOOT, e so ali. A primeira versao usou re.sub com count=1 sobre o arquivo
    # inteiro e acertou a tabela BUILDERS, que vem antes: o boot ficou com as chamadas
    # antigas e a tabela ficou corrompida. Anteceder o alvo pelo bloco que o contem e a
    # diferenca entre trocar a chamada e trocar a primeira coisa parecida com ela.
    ib = js.index("/* ---------------- boot ---------------- */")
    fb = js.index("\n});", ib) + len("\n});")
    boot = js[ib:fb]
    boot = re.sub(r"closeBuild\(\d+,RECAP\d+,CONF\d+\);(\s*closeBuild\(\d+,RECAP\d+,CONF\d+\);)*",
                  " ".join(chamadas) if chamadas else "", boot, count=1)
    boot = re.sub(r"pwRestore\(\[.*?\]\);", "pwRestore([" + ",".join(restaura) + "]);",
                  boot, count=1, flags=re.S)
    js = js[:ib] + boot + js[fb:]

    html = cabeca + js

    # ---- regioes de conteudo
    for ident, arq in (("tab-planning", "perfil.html"), ("tab-syllabus", "syllabus.html")):
        caminho = os.path.join(base_frag, arq)
        if os.path.exists(caminho):
            html = troca_bloco_por_id(html, ident,
                                      open(caminho, encoding="utf-8").read().strip())
    rotulos, pre, post, fb = {}, [], [], []
    for i, n in enumerate(aulas):
        pasta = os.path.join(base_frag, f"aula{n}")
        reg = open(os.path.join(pasta, "registro.js"), encoding="utf-8").read()
        mod = (re.search(r"mod:'([^']+)'", reg) or [None, "—"])[1]
        tema = (re.search(r"tema:'([^']*)'", reg) or [None, ""])[1]
        rotulos[n] = (f"Aula {n:02d} &middot; {mod}", f"Lesson {n:02d}")
        pre.append(expande_blocos(
            open(os.path.join(pasta, "preclass.html"), encoding="utf-8").read().strip(),
            declarado[n], usado[n], f"aula {n} pre-class"))
        post.append(expande_blocos(
            open(os.path.join(pasta, "postclass.html"), encoding="utf-8").read().strip(),
            declarado[n], usado[n], f"aula {n} post-class"))
        # O CONTROLE DE ROLAGEM E DA ABA, NAO DA AULA (FB28).
        #
        # A aba ja termina com a sua barra `ao-topo`, fora dos blocos por aula, como no
        # artefato. Um botao igual no fim do fragmento aparece colado no outro -- dois
        # controles com o mesmo destino, um em ingles e outro em portugues, foi o que a
        # revisao viu no post-class do Luiz. O fragmento nao e o lugar dele.
        if "btn-bar ao-topo" in post[-1]:
            raise SystemExit(f"aula {n} post-class: o bloco da aula traz uma barra "
                             f"'ao-topo'. Esse controle e da ABA e ja existe uma vez, no "
                             f"fim dela -- tire a do fragmento.")
        fb.append(FEEDBACK_BLOCO.format(
            n=n, tema=tema, oculto="" if i == 0 else ' style="display:none"'))
        erros += confere_aula(n, open(os.path.join(pasta, "registro.js"), encoding="utf-8").read().strip(),
                              open(os.path.join(pasta, "guide.js"), encoding="utf-8").read().strip(),
                              pasta, slides[aulas.index(n)], pre[-1])
        sobrando = set(declarado[n]) - usado[n]
        if sobrando:
            raise SystemExit(f"aula {n}: blocos declarados e sem placeholder em nenhum "
                             f"fragmento: {sorted(sobrando)}. Trabalho escrito que nao "
                             f"chega a tela.")
    # os cartoes da aba In-class, gerados do registro + cartao.json
    cartoes = []
    for n in aulas:
        pasta = os.path.join(base_frag, f"aula{n}")
        reg = open(os.path.join(pasta, "registro.js"), encoding="utf-8").read()
        cj = os.path.join(pasta, "cartao.json")
        if not os.path.exists(cj):
            erros.append(f"aula {n}: falta cartao.json (objetivo, produto e preparacao do "
                         f"cartao da aba In-class). Sem ele o cartao fica com o conteudo do "
                         f"artefato -- residuo de outro perfil.")
            continue
        dados = json.load(open(cj, encoding="utf-8"))
        etapas = re.findall(r"\{n:'[^']+',min:(\d+)\}", reg)
        telas = len(re.findall(r'data-slide="',
                               open(os.path.join(pasta, "slides.html"),
                                    encoding="utf-8").read()))
        cartoes.append(cartao_de_aula(n, reg, dados, telas, sum(int(x) for x in etapas)))
    # Os cartoes PENDENTES: as aulas do bloco vigente que ainda nao foram produzidas.
    # O artefato traz os dele (21 e 22, com titulo e objetivo do Marcos) e eles sobreviviam
    # ao lado dos da Stephanie -- com numeros que nem existem no ciclo dela. Aqui saem do
    # SYLLABUS: titulo, objetivo e produto da linha daquela aula.
    syl = cfg.get("syllabus")
    if syl:
        caminho_syl = os.path.join(RAIZ, syl)
        if os.path.exists(caminho_syl):
            linhas = {x["n"]: x for x in json.load(
                open(caminho_syl, encoding="utf-8")).get("aulas", [])}
            c = cfg["ciclo"]
            bloco_ini = c["primeira"]
            while bloco_ini + c["porBloco"] <= max(aulas):
                bloco_ini += c["porBloco"]
            for n in range(bloco_ini, bloco_ini + c["porBloco"]):
                if n in aulas or n not in linhas:
                    continue
                x = linhas[n]
                mod = {"reading-into-speaking": ("Reading", "R"),
                       "listening-into-interaction": ("Listening", "L"),
                       "grammar-for-communication": ("Grammar", "G"),
                       "esp-real-world": ("ESP", "E")}.get(x.get("framework"), ("—", "?"))
                cartoes.append(
                    '<div class="lesson-card lc-pendente" id="lc%d">\n'
                    '          <div class="lc-head">\n'
                    '            <span class="lc-badge">Aula %02d</span>\n'
                    '            <span class="lc-fw">%s &middot; %s</span>\n'
                    '            <span class="lc-status">Ainda n&atilde;o produzida</span>\n'
                    '          </div>\n'
                    '          <h3 class="lc-title">%s</h3>\n'
                    '          <p class="lc-desc"><strong>Objetivo comunicativo:</strong> %s'
                    '<br><strong>Produto principal:</strong> %s</p>\n'
                    '        </div>' % (n, n, x.get("bloco", ""), mod[0],
                                        x.get("titulo", ""), x.get("objetivo_comunicativo", ""),
                                        x.get("produto", "")))

    if cartoes:
        hm2 = mascara(html)
        m2 = re.search(r'<div class="lesson-card[^"]*"[^>]*id="lc\d+"[^>]*>', hm2)
        if not m2:
            raise SystemExit("o shell nao tem cartao de aula na aba In-class")
        ini2 = m2.start()
        fim2 = ini2
        for mm in re.finditer(r'<div class="lesson-card[^"]*"[^>]*id="lc\d+"[^>]*>', hm2):
            fim2 = fecha(hm2, mm.start())
        html = html[:ini2] + "\n      ".join(cartoes) + html[fim2:]

    html = troca_blocos_de_aula(html, "tab-preclass", "pc", "preSel", aulas, rotulos, pre)
    html = troca_blocos_de_aula(html, "tab-postclass", "ps", "postSel", aulas, rotulos, post)
    # A ABA FEEDBACK TAMBEM E POR AULA, e ficou de fora ate 25/08/2026.
    #
    # Ela tem a MESMA forma das outras duas (barra com fbSel(N) + blocos sfN), e mesmo assim
    # nunca foi reconstruida: o material publicado saiu com `Lesson 19` e `Lesson 20`, os
    # titulos do artefato do Marcos ("Reading the room", "From evidence to a briefing"), num
    # ciclo que tem as aulas 1 a 4. Nos DOIS arquivos -- e a aba e `data-view="aluno"`, entao
    # quem via as duas aulas inexistentes era o ALUNO.
    #
    # E o catalogo do auditor chama isso de INT-002 (contaminacao de ciclo, BLOCKER):
    # "aparecem numeros de aula, bloco, checkpoint ou decisoes de outro ciclo".
    #
    # Nenhum gate viu porque todos olhavam para o que o builder EMITE. Este defeito e do que
    # ele NAO emite: a regiao ficou intacta, valida, bonita e de outro aluno. Quem cobra
    # agora e o GATE 39 (check_ciclo_limpo.py), que le o intervalo do ciclo e reprova
    # referencia a aula fora dele.
    html = troca_blocos_de_aula(html, "tab-feedback", "sf", "fbSel", aulas, rotulos, fb)
    html, n_telas = troca_slides(html, slides)

    # O TITULO DO MENU DE SLIDES NASCE COM O NUMERO DA AULA DO ARTEFATO.
    #
    # `smPaint()` reescreve `#smTitle` com a aula corrente, entao na pratica a tela quase
    # sempre mostra o numero certo. Mas o texto CRAVADO no arquivo continua sendo o do
    # artefato ("Lesson 19 · 10 slides"), e estado inicial e o que sobra quando a pintura
    # nao roda -- e neste shell isso ja aconteceu: uma excecao no boot leva junto todos os
    # construtores seguintes (P2 §25). O aluno abriria o menu e leria uma aula que nao
    # existe no ciclo dele.
    #
    # Estado inicial e conteudo, nao detalhe: quem nasce contaminado passa em todo gate
    # estatico e so aparece quando o JS falha, que e exatamente quando ninguem esta olhando.
    if aulas:
        # A contagem sai das TELAS da primeira aula, nunca do tamanho do HTML dela: a
        # primeira versao disto escreveu "27946 slides" -- len() de uma string.
        n_prim = len(re.findall(r'<div class="slide[^"]*"[^>]*data-slide=',
                                slides[0] if slides else ""))
        html = re.sub(r'(<span id="smTitle">)[^<]*(</span>)',
                      lambda m: f"{m.group(1)}Lesson {aulas[0]:02d} &middot; "
                                f"{n_prim} slides{m.group(2)}",
                      html, count=1)

    # ---- O AUD_MAP: de que ARQUIVO sai cada som (AUT-004 / Anexo P-A)
    #
    # O shell derivado nao sintetiza mais nada: ele PROCURA. `say`/`sayAs` procuram pelo
    # proprio texto; `playTalk` procura pela chave do trecho (#talkN:de:ate). Quem responde
    # e este mapa.
    #
    # A lista sai de `audio_surface`, o MESMO modulo que o gerador usa para saber o que
    # produzir. Duas descobertas independentes divergiriam, e a divergencia aqui se
    # manifesta como audio que nao toca -- sem erro em lugar nenhum.
    #
    # Os TURNOS (o instante em que cada falante comeca) so existem depois de gerar, entao
    # vem do manifesto quando ele ja existe. Sem manifesto o mapa ainda sai, com os nomes de
    # arquivo -- que sao deterministicos pelo hash do transcript. E por isso que build e
    # geracao podem rodar em qualquer ordem.
    mapa = {}
    manifesto_path = os.path.join(base_frag, "audio_manifest.json")
    gerado_antes = {}
    if os.path.exists(manifesto_path):
        gerado_antes = {x["asset_id"]: x
                        for x in json.load(open(manifesto_path, encoding="utf-8"))}
    for item in audio_surface.manifesto(cfg, base_frag):
        entrada = {"src": f"/audio/{cfg['slug']}/{item['file']}"}
        turnos = (gerado_antes.get(item["asset_id"]) or {}).get("turnos")
        if turnos:
            entrada["turnos"] = turnos
        mapa[item["chave"]] = entrada
    if mapa:
        blob = json.dumps(mapa, ensure_ascii=False).replace("</", "<\\/")
        # LAMBDA, nunca string crua: no re.sub o replacement e TEMPLATE, e `\n`/`\"` do
        # JSON virariam newline e aspa de verdade. Mesmo cuidado do PV_POSTS e do audioMap.
        html = re.sub(r"var AUD_MAP=\(typeof AUD_MAP!=='undefined'\)\?AUD_MAP:\{\};",
                      lambda _: f"var AUD_MAP={blob};", html, count=1)
    erros_audio = [k for k in mapa if f'"{k}"' not in html and k not in html]


    # A tabela BUILDERS diz quem preenche qual host, e e o que faz o Reset de aula
    # reconstruir a tela em vez de deixa-la vazia. Ela vinha com os hosts do MODELO. Aqui e
    # regenerada a partir do que o material tem de fato: host que nao existe sai, e cada aula
    # declarada ganha o seu. Entrada apontando para host inexistente nao quebra nada -- e por
    # isso mesmo passaria despercebida.
    ib = html.index("var BUILDERS=[")
    ie = html.index("\n];", ib) + len("\n];")
    originais = re.findall(r"\{h:'([^']+)',\s*also:\[([^\]]*)\],\s*f:function\(\)\{([^}]*)\}\}",
                           html[ib:ie])
    entradas = []
    # 1. o que o MODELO trazia so continua se o host existir no material gerado. Entrada
    #    apontando para host inexistente nao quebra nada -- e por isso mesmo passaria
    #    despercebida, ate o dia em que um Reset deixasse a tela vazia.
    for host, also, corpo in originais:
        if "closeBuild(" in corpo or "tsBuild(" in corpo:
            continue          # fecho e transcript sao por aula: entram na volta seguinte
        if f'id="{host}"' in html:
            entradas.append("  {h:'%s', also:[%s],f:function(){%s}}" % (host, also, corpo))
    # 2. o transcript de cada aula que tem um. `tsBuild` percorre todas as caixas, mas o
    #    BUILDERS precisa da entrada por HOST para que o Reset daquela aula a reconstrua.
    for n in aulas:
        if f'id="ts{n}"' in html:
            entradas.append("  {h:'ts%d', also:[],f:function(){tsBuild();}}" % n)
    # 3. o fecho de cada aula declarada
    for n in aulas:
        if f'id="recapList{n}"' in html:
            entradas.append("  {h:'recapList%d', also:['confList%d'],"
                            "f:function(){closeBuild(%d,RECAP%d,CONF%d);}}" % (n, n, n, n, n))
    html = html[:ib] + "var BUILDERS=[\n" + ",\n".join(entradas) + "\n];" + html[ie:]

    # ---- os dados de conteudo do ARTEFATO que este material nao usa
    #
    # TALK_19 (o dialogo), BRIEF_20 (o documento), GD_* (o sorting), MSG_20 e SCRIPT_PRE19
    # sao conteudo das aulas DELE. Ficam no shell porque o shell e o artefato menos o
    # declarado; num material de outro aluno sao texto de outra pessoa entregue junto.
    ini2 = html.rfind("<script>")
    cab2, js2 = html[:ini2], html[ini2:]
    for velho in sorted(set(re.findall(
            r"\bvar (TALK_\d+|BRIEF_\d+|MSG_\d+|SCRIPT_PRE\d+|GD_ITEMS|GD_COLS|GD_V)\s*=",
            js2))):
        js2 = extrai_shell.remove_var(js2, velho, {})
    html = cab2 + js2

    # ---- o CABECALHO, que hubPaint() nao repinta
    #
    # O nome e o ciclo saem do registro e sao repintados no boot. O subtitulo, a linha de
    # contexto e o mapa do ciclo, nao: eles ficam como o artefato os salvou. Sem trocar aqui,
    # o material da Stephanie abria dizendo "Engenheiro de avaliacao e perito avaliador" --
    # a profissao do Marcos, no cabecalho dela. Isto e o "residuo de outro perfil" que o
    # Doc 04 §12.1 proibe, e quem o encontrou foi o catalogo de modelos, que le o cabecalho
    # para descrever a persona: ele descreveu a Stephanie com o perfil do Marcos.
    cab = cfg.get("header") or {}
    if cab.get("subtitulo"):
        html = re.sub(r'<p class="subtitle">.*?</p>',
                      '<p class="subtitle">%s</p>' % cab["subtitulo"], html, count=1, flags=re.S)
    if cab.get("info"):
        html = re.sub(r'<div class="student-info">.*?</div>',
                      '<div class="student-info">\n      %s\n    </div>'
                      % "\n      ".join(f"<span>{x}</span>" for x in cab["info"]),
                      html, count=1, flags=re.S)
    # O mapa do ciclo vem PINTADO com as aulas do artefato (19..38). mapaPaint() o refaz no
    # boot a partir de CICLO, mas o que se ENTREGA e o do artefato -- e por um instante e o
    # que a tela mostra.
    html = re.sub(r'(<div class="ciclo-mapa" id="cicloMapa"[^>]*>).*?(</div>)', r"\1\2",
                  html, count=1, flags=re.S)

    art = open(ARTEFATO, encoding="utf-8").read()
    m_alu = re.search(r"var ALUNO=\{nome:'([^']*)'", art)
    mesmo_aluno = bool(m_alu) and m_alu.group(1) == cfg["aluno"]["nome"]

    # ---- os comentarios que descrevem o material DO ARTEFATO
    #
    # O shell carrega os comentarios do artefato -- e eles sao memoria util, no shell. No
    # material de OUTRO aluno eles descrevem uma aula que nao esta ali ("Recepcao de abertura
    # de um congresso internacional de valuation") e nomeiam a pessoa do artefato. Comentario
    # e byte entregue: sai do material, e continua no shell, que e onde a memoria serve.
    if not mesmo_aluno:
        nome_art = m_alu.group(1) if m_alu else None
        if nome_art:
            html, n_com = re.subn(r"/\*(?:(?!\*/)[\s\S])*?\b" + re.escape(nome_art) +
                                  r"\b(?:(?!\*/)[\s\S])*?\*/", "", html,
                                  flags=re.IGNORECASE)
        else:
            n_com = 0

    # ---- residuo: nenhuma linha de identidade do artefato pode sobreviver
    # No round-trip o material E o do artefato: as linhas dele sobreviverem ali e o esperado,
    # e cobrar residuo seria cobrar que ele nao seja ele mesmo.
    m_sub = re.search(r'<p class="subtitle">(.*?)</p>', art, re.S)
    digitais = [re.sub(r"\s+", " ", m_sub.group(1)).strip()] if m_sub else []
    m_inf = re.search(r'<div class="student-info">(.*?)</div>', art, re.S)
    if m_inf:
        digitais += [re.sub(r"\s+", " ", x).strip()
                     for x in re.findall(r"<span>(.*?)</span>", m_inf.group(1), re.S)]
    plano = re.sub(r"\s+", " ", html)
    for d in digitais:
        if d and not mesmo_aluno and d in plano \
                and d not in json.dumps(cfg, ensure_ascii=False):
            erros.append(f"residuo do artefato no material: {d[:70]!r} sobreviveu. "
                         f"Doc 04 §12.1 — nenhum fragmento de outro perfil.")

    nome_inteiro = f"{cfg['aluno']['nome']} {cfg['aluno']['sobrenome']}".strip()
    prog = cfg.get("titulo", "Business English Program")
    html = re.sub(r"<title>.*?</title>",
                  f"<title>{nome_inteiro} — {prog} | Alumni by Better</title>",
                  html, count=1, flags=re.S)
    # ---- e o titulo que o SCRIPT escreve, que e o que a aba do navegador mostra
    #
    # O shell traz `document.title = alunoNome() + ' — Business English Program | ...'` com o
    # nome do programa CRAVADO, e essa linha roda depois do parser: a substituicao da tag
    # acima e desfeita em runtime, em todo material. O gate estatico le a tag e ve o titulo
    # certo; o navegador mostra outro. So medindo com o navegador aberto isso aparece.
    alvo = re.search(r"document\.title\s*=\s*alunoNome\(\)\s*\+\s*'([^']*)'", html)
    if not alvo:
        raise SystemExit("o shell nao tem mais o `document.title = alunoNome() + ...` que "
                         "este passo corrige. Se a linha mudou de forma, ajuste aqui; se "
                         "sumiu, apague este passo. Passar adiante devolveria o defeito.")
    html = html.replace(alvo.group(0),
                        f"document.title=alunoNome()+' — {prog} | Alumni by Better'", 1)
    return html, n_telas, erros


def confere_aula(n, registro_js, guide_js, pasta, slides_txt=None, pre_txt=None):
    """Os asserts que a norma permite provar por construcao.

    `slides_txt` e `pre_txt` sao os fragmentos JA EXPANDIDOS. Medir o arquivo cru contaria o
    placeholder `<!--BLOCOS:...-->` como zero atividade -- e foi o que aconteceu no primeiro
    exercicio migrado: o assert das SEIS atividades acusou cinco, corretamente, porque a
    sexta ainda nao tinha sido emitida. O contrato se confere no que vai para a tela."""
    erros = []
    etapas = re.findall(r"\{n:'([^']+)',min:(\d+)\}", registro_js)
    if len(etapas) != ETAPAS:
        erros.append(f"aula {n}: {len(etapas)} etapas declaradas, e a arquitetura do "
                     f"Documento 03 tem {ETAPAS}. (Telas podem ser quantas o conteudo pedir; "
                     f"ETAPAS, nao.)")
    soma = sum(int(m) for _, m in etapas)
    if etapas and soma != PERCURSO_MIN:
        erros.append(f"aula {n}: os minutos das etapas somam {soma}, e o percurso essencial "
                     f"e {PERCURSO_MIN} (+5 de margem).")
    slides = (slides_txt if slides_txt is not None
              else open(os.path.join(pasta, "slides.html"), encoding="utf-8").read())
    fases = [int(x) for x in re.findall(r'data-stage="(\d+)"', slides)]
    if fases:
        if sorted(set(fases)) != list(range(1, len(etapas) + 1)) and etapas:
            faltam = sorted(set(range(1, len(etapas) + 1)) - set(fases))
            erros.append(f"aula {n}: as telas nao representam as etapas {faltam}. "
                         f"Nenhuma etapa fica sem representacao (Doc 03 §6.1).")
        if fases != sorted(fases):
            erros.append(f"aula {n}: as etapas aparecem fora de ordem nas telas: {fases}. "
                         f"A ordem e normativa.")
    pre = (pre_txt if pre_txt is not None
           else open(os.path.join(pasta, "preclass.html"), encoding="utf-8").read())
    n_ativ = len(re.findall(r'class="exercise-section"', pre))
    if n_ativ != 6:
        erros.append(f"aula {n}: o pre-class tem {n_ativ} atividades, e sao exatamente SEIS "
                     f"(Doc 04 §4.2).")
    faltam = [c for c in CAMPOS_GUIA if not re.search(r"\b" + c + r"\s*:", guide_js)]
    if faltam:
        erros.append(f"aula {n}: o Teacher's Guide nao tem os campos {faltam} (Doc 04 §8.1).")
    return erros


def round_trip():
    """Monta com os fragmentos do proprio artefato e compara regiao por regiao."""
    base = os.path.join(RAIZ, "_build", "consultivo", "_do-artefato")
    if not os.path.isdir(base):
        print("rode antes: python3 scripts/consultivo/extrai_fragmentos.py", file=sys.stderr)
        return 1
    cfg = {
        "slug": "_round-trip",
        "artefato_id": "consultivo-c02-19-38",
        "aluno": {"nome": "Marcos", "sobrenome": "Mansour"},
        "ciclo": {"numero": 2, "aulas": 20, "primeira": 19, "porBloco": 4, "nivel": "B1"},
        "aulas": [19, 20],
        # O elenco e as vozes do PROPRIO artefato. Sem eles o round-trip nao exercitaria o
        # caminho do audio, e o AUD_MAP -- que e o que faz o som existir depois da troca do
        # motor (AUT-004) -- ficaria fora do circulo que prova que o builder reproduz.
        "cast": [{"n": "Nadia", "g": "f"}, {"n": "Tom", "g": "m"}],
        "voices": {"Nadia": "BIvP0GN1cAtSRTxNHnWS", "Tom": "sfJopaWaOtauCD3HKX6Q",
                   "_neutra": "sfJopaWaOtauCD3HKX6Q", "_f": "BIvP0GN1cAtSRTxNHnWS",
                   "_m": "sfJopaWaOtauCD3HKX6Q"},
    }
    gerado, n_telas, erros = monta(cfg, base)
    art = open(ARTEFATO, encoding="utf-8").read()
    hm_a, hm_g = mascara(art), mascara(gerado)

    def regiao(h, hm, ident):
        m = re.search(r'<div[^>]*id="' + ident + r'"[^>]*>', hm)
        return h[m.start():fecha(hm, m.start())] if m else ""

    print("=== round-trip: artefato -> fragmentos -> builder -> material")
    dif = 0
    for ident in ("tab-planning", "tab-syllabus", "pc19", "pc20", "ps19", "ps20",
                  "sf19", "sf20"):
        a, g = regiao(art, hm_a, ident), regiao(gerado, hm_g, ident)
        igual = a.strip() == g.strip()
        dif += 0 if igual else 1
        print(f"  {'igual' if igual else 'DIFERE'}  {ident:14s} artefato={len(a):7d}B  gerado={len(g):7d}B")
    # O CARTAO da aba In-class entra no circulo pelos CAMPOS, nao pelos bytes: o builder o
    # gera de um molde proprio, entao o espacamento difere de proposito. O que tem de voltar
    # igual e o que e autoral -- titulo, objetivo, produto e a contagem de itens da
    # preparacao. Sem isto, uma extracao que perdesse a preparacao passaria despercebida: o
    # cartao continuaria existindo, so que vazio.
    def campos_cartao(t, n):
        i = t.find(f'id="lc{n}"')
        if i < 0:
            return None
        j = t.find('id="lcfb', i)
        seg = t[i:j if j > i else i + 12000]
        tit = re.search(r'<h3 class="lc-title">(.*?)</h3>', seg, re.S)
        obj = re.search(r"<strong>Objetivo comunicativo:</strong>\s*(.*?)</p>", seg, re.S)
        prod = re.search(r"<strong>Produto principal:</strong>\s*(.*?)</p>", seg, re.S)
        norm = lambda x: re.sub(r"\s+", " ", x).strip() if x else ""
        return (norm(tit.group(1) if tit else ""), norm(obj.group(1) if obj else ""),
                norm(prod.group(1) if prod else ""),
                len(re.findall(r"<li>", seg)))
    for n in (19, 20):
        ca, cg = campos_cartao(art, n), campos_cartao(gerado, n)
        igual = ca == cg
        print(f"  {'igual' if igual else 'DIFERE'}  cartao lc{n}     "
              f"{'titulo/objetivo/produto/itens' if igual else str(ca) + ' != ' + str(cg)}")
        if not igual:
            dif += 1

    # O JS por aula tambem entra no circulo: a tabela BUILDERS diz quem reconstroi cada host,
    # e uma entrada perdida so aparece no dia em que alguem usa o Reset. Comparar CONJUNTO,
    # nao ordem -- a ordem de montagem e do builder, e nao muda o que a tabela promete.
    def hosts(t):
        i = t.index("var BUILDERS=[")
        return sorted(re.findall(r"\{h:'([^']+)'", t[i:t.index("\n];", i)]))
    ha, hg = hosts(art), hosts(gerado)
    print(f"  {'igual' if ha == hg else 'DIFERE'}  BUILDERS       artefato={ha}")
    if ha != hg:
        print(f"                        gerado  ={hg}")
        dif += 1
    telas_a = len(re.findall(r'data-lesson="\d+"', hm_a))
    print(f"  {'igual' if telas_a == n_telas else 'DIFERE'}  telas          artefato={telas_a}  gerado={n_telas}")
    dif += 0 if telas_a == n_telas else 1
    for e in erros:
        print("  ASSERT:", e)
    if dif or erros:
        print(f"\nFALHOU — {dif} regiao(oes) divergente(s), {len(erros)} assert(s).")
        return 1
    print("\nOK — o builder devolve o artefato a partir dos fragmentos dele.")
    return 0


def _selftest():
    """Prova que os asserts MORDEM. Cada mutacao e um defeito que ja custou material real
    noutro molde: etapa a menos, minuto que nao fecha, atividade a mais no pre-class, campo
    do guia ausente, etapa fora de ordem."""
    import shutil
    import tempfile
    base = os.path.join(RAIZ, "_build", "consultivo", "_do-artefato")
    if not os.path.isdir(base):
        print("rode antes: python3 scripts/consultivo/extrai_fragmentos.py")
        return 1
    tmp = tempfile.mkdtemp(prefix="bb_")
    try:
        shutil.copytree(base, os.path.join(tmp, "f"))
        f = os.path.join(tmp, "f")
        pasta = os.path.join(f, "aula19")

        def carrega():
            return (open(os.path.join(pasta, "registro.js"), encoding="utf-8").read(),
                    open(os.path.join(pasta, "guide.js"), encoding="utf-8").read())

        reg0, gui0 = carrega()
        casos = []

        # 1 — uma etapa a menos
        reg = reg0.replace("{n:'Feedback + replay',min:7}", "", 1).replace(",\n      \n", "\n")
        casos.append(("etapa a menos", reg, gui0, "etapas declaradas"))
        # 2 — os minutos nao fecham
        reg = reg0.replace("{n:'Prediction',min:3}", "{n:'Prediction',min:4}", 1)
        casos.append(("minutos que nao fecham", reg, gui0, "somam"))
        # 3 — campo do guia ausente
        gui = re.sub(r"\n\s*evidence:", "\n  NAO_E_EVIDENCE:", gui0, count=1)
        casos.append(("campo do guia ausente", reg0, gui, "nao tem os campos"))

        for rotulo, reg, gui, esperado in casos:
            open(os.path.join(pasta, "registro.js"), "w", encoding="utf-8").write(reg)
            open(os.path.join(pasta, "guide.js"), "w", encoding="utf-8").write(gui)
            erros = confere_aula(19, reg, gui, pasta)
            if not any(esperado in e for e in erros):
                print(f"FALHA: '{rotulo}' NAO foi pego. erros={erros}")
                return 1
            print(f"  OK    {rotulo}")
        open(os.path.join(pasta, "registro.js"), "w", encoding="utf-8").write(reg0)
        open(os.path.join(pasta, "guide.js"), "w", encoding="utf-8").write(gui0)

        # 4 — atividade a menos no pre-class
        pre = os.path.join(pasta, "preclass.html")
        p0 = open(pre, encoding="utf-8").read()
        open(pre, "w", encoding="utf-8").write(p0.replace('class="exercise-section"', 'class="x"', 1))
        erros = confere_aula(19, reg0, gui0, pasta)
        open(pre, "w", encoding="utf-8").write(p0)
        if not any("atividades" in e for e in erros):
            print(f"FALHA: pre-class com 5 atividades NAO foi pego. erros={erros}")
            return 1
        print("  OK    pre-class com atividade a menos")

        # 5 — etapa fora de ordem nas telas
        sl = os.path.join(pasta, "slides.html")
        s0 = open(sl, encoding="utf-8").read()
        open(sl, "w", encoding="utf-8").write(s0.replace('data-stage="2"', 'data-stage="7"', 1))
        erros = confere_aula(19, reg0, gui0, pasta)
        open(sl, "w", encoding="utf-8").write(s0)
        if not any("fora de ordem" in e for e in erros):
            print(f"FALHA: etapa fora de ordem NAO foi pega. erros={erros}")
            return 1
        print("  OK    etapa fora de ordem nas telas")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("\nSELFTEST OK — os 5 asserts mordem.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    if "--round-trip" in sys.argv:
        return round_trip()
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cfg_path = sys.argv[1]
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    base = os.path.join(RAIZ, cfg.get("fragmentos", os.path.dirname(cfg_path)))
    prof, n_telas, erros = monta(cfg, base)
    if erros:
        for e in erros:
            print("  RECUSADO:", e)
        print(f"\n{len(erros)} problema(s). O material NAO foi escrito.")
        return 1
    # ---- o molde nao e aluno, e o arquivo tem de dizer isso
    #
    # `stephanie-vicente` e ficcao: nao tem contrato, nao esta em perfis. O config sempre
    # disse isso -- em PROSA, num campo `_o_que_e` que nenhuma maquina le. Resultado: o
    # indice que alimenta a aba "Alunos Consultivo" contava 1 aluno, e o aluno era ela.
    # Agora e declaracao, e viaja DENTRO do arquivo: quem le o disco nao precisa saber de
    # cor quais slugs sao molde.
    if cfg.get("molde"):
        marca = '<meta name="alumni-molde" content="1">'
        if marca not in prof:
            prof = prof.replace('<meta name="alumni-anatomia" content="consultivo">',
                                '<meta name="alumni-anatomia" content="consultivo">\n'
                                + marca, 1)
    aluno, _ = extrai_shell.deriva_aluno(prof)
    # ---- ONDE ESCREVER: a URL do aluno nao se toca enquanto ele tem aula no material velho
    #
    # O SUFIXO E `-cicloN`, POR EXTENSO, e isso nao e estetica (FB28): `luiz-bressane-c1`
    # se le como o NIVEL C1 do CEFR, e o aluno e B1+. A URL e a primeira coisa que alguem
    # ve do material, e nela `c1` nao tem como significar "ciclo" -- todo o resto do sistema
    # usa aquela letra e aquele numero para nivel.
    #
    # `fase: "piloto"` escreve em `{slug}-ciclo{N}.html`, ao lado do material atual, sem
    # encostar nele. E a fase de transicao: o aluno continua tendo aula no antigo pelo link
    # de sempre, e o novo existe em paralelo para ser testado. Quem mostra os dois no painel
    # e o `materiais-extra.json`, que confere cada caminho por HTTP antes de virar botao.
    #
    # Sem `fase` (ou `fase: "canonica"`) escreve em `{slug}.html` -- o cutover, que so
    # acontece por decisao explicita, aluno a aluno, e exige `[cutover]` no commit (GATE 47).
    #
    # O sufixo fica sempre no que e PROVISORIO (`-c1`, durante o piloto) ou no que ja
    # CONGELOU (`-anterior`, depois do cutover). Nunca na URL viva: foi o que se fez com
    # `-v2` em daniela-feitoza e percival-jr, e aqueles dois carregam o sufixo ate hoje,
    # mais dois redirects cada no vercel.json.
    slug = cfg["slug"]
    fase = cfg.get("fase", "canonica")
    if fase not in ("canonica", "piloto"):
        print(f"  RECUSADO: fase {fase!r} nao existe. Use 'piloto' ou 'canonica'.")
        return 1
    nome = f"{slug}-ciclo{cfg['ciclo']['numero']}" if fase == "piloto" else slug
    p1 = os.path.join(RAIZ, "public", "professor", f"{nome}.html")
    p2 = os.path.join(RAIZ, "public", "aluno", f"{nome}.html")
    for caminho, conteudo in ((p1, prof), (p2, aluno)):
        with open(caminho, "w", encoding="utf-8") as fh:
            fh.write(conteudo)
    print(f"OK — {len(cfg['aulas'])} aula(s), {n_telas} telas")
    print(f"  {os.path.relpath(p1, RAIZ)}  {len(prof)}B")
    print(f"  {os.path.relpath(p2, RAIZ)}  {len(aluno)}B")
    return 0


if __name__ == "__main__":
    sys.exit(main())
