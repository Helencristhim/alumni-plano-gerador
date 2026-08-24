#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deriva os DOIS shells da anatomia `private-black` DO ARTEFATO, por script.

POR QUE POR SCRIPT, E NAO A MAO
-------------------------------
O artefato (`_build/model/artefatos/marcos-private-black.html`) e a ESPECIFICACAO da
interface: dele se COPIA, classe por classe. O porte a mao ja foi feito uma vez neste
projeto, em 11/08/2026, e renomeou cada peca (`reveal-item` virou `ic-reveal`,
`blank-input` virou `ic-blank`...); o inventario catalogou a REESCRITA, e o gate passou a
comparar a copia consigo mesma -- verde para sempre, medindo coerencia interna e chamando
isso de fidelidade. Quatro pecas do artefato (`callout`, 23,8 usos/aula; `tbl-wrap`;
`quiz-option`; `rule-box`) simplesmente nunca existiram no molde, e ninguem viu por meses.

Um script torna a derivacao AUDITAVEL: qualquer pessoa roda de novo e ve que o shell e o
artefato menos o que esta declarado aqui embaixo. Nada foi reescrito no caminho.

DOIS SHELLS, PORQUE A ENTREGA E DE DUAS URLS
--------------------------------------------
Regra da Stephanie, 24/08/2026, ja incorporada ao 00, ao 04, ao P1, ao P2 e ao P3:

    "A producao final deve gerar duas URLs distintas. A URL do professor contem a visao
     docente e permite alternar para uma previa da visao do aluno. A URL do aluno contem
     exclusivamente o conteudo destinado ao aluno. Gabaritos, Teacher's Guide, registros
     internos, hipoteses pedagogicas, evidencias reservadas e controles docentes nao podem
     estar apenas ocultos no HTML do aluno: nao devem integrar o arquivo, payload ou estado
     entregue por essa URL."

O artefato e UM arquivo com alternador -- e legitimo, porque e protótipo (P1 §0) e uma
pagina do claude.ai nao tem duas URLs. Para producao, o alternador continua existindo na
URL do professor (como previa) e NAO existe na do aluno, porque nao ha o outro lado dentro
dela.

    shells/black.html        professor: as 6 abas, o deck, o guia, a previa do aluno

O BUILD DO ALUNO E O PROXIMO PASSO, E NAO ESTA AQUI DE PROPOSITO
----------------------------------------------------------------
Ele nao e "o mesmo arquivo com pedacos escondidos": e outro build. Tentei deriva-lo junto
com este e o GATE 35 mostrou por que ele merece PR proprio -- remover o deck faz o boot
morrer em `deckInit`, na primeira linha, levando junto TODOS os construtores seguintes
(P2 §25: "uma excecao no boot nao fica onde nasceu"). Sem navegador isso nao aparece: o
HTML e valido e todo gate estatico fica verde.

Medido no navegador, o build do aluno precisa de:

  - um BOOT proprio, que chame so o que e dele (persInit, preKeys, preInit, audBuild,
    hubPaint, sfBuild, snapInit) e nenhum construtor de deck;
  - a remocao dos DADOS docentes do JS entregue -- PC_NOTAS (os gabaritos do pre-class,
    5,4 KB), GUIDE, CP, EP_MAPA, ESCALA, e os textos que so o deck usa;
  - a remocao das ROTAS docentes -- `?mode=teacher-guide` e o caminho que promove papel
    (P3 §3: "a URL do aluno nao possui alternador, rota de professor ou elevacao de papel
    por query, hash, armazenamento, atributo ou chamada direta").

Nada disso e cosmetico, e por isso vai com gate proprio (isolamento), que le os BYTES do
arquivo entregue -- nao a folha de estilo.

AS DUAS AULAS DO ARTEFATO FICAM NOS DOIS SHELLS
-----------------------------------------------
Nao e descuido, e o conserto de um erro que este repo ja pagou. No porte da story-quest eu
tirei a segunda aula "porque o molde carrega uma aula de exemplo"; medindo depois, a aula 2
levava embora mecanica que a aula 1 nao tem. Aqui vale igual: a 19 e Listening e a 20 e
Reading, e elas nao usam as mesmas pecas. Anatomia e o que a forma OFERECE; a aula escolhe.
O builder troca o conteudo inteiro, entao duas aulas de exemplo nao custam nada na geracao.

USO:
    python3 scripts/black/extrai_shell.py            # escreve os dois shells
    python3 scripts/black/extrai_shell.py --check    # nao escreve: confere o disco
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTEFATO = os.path.join(RAIZ, "_build", "model", "artefatos", "marcos-private-black.html")
SHELLS = os.path.join(RAIZ, "_build", "model", "shells")
SHELL_PROF = os.path.join(SHELLS, "black.html")
SHELL_ALUNO = os.path.join(SHELLS, "black-aluno.html")

CARIMBO = '<meta name="alumni-anatomia" content="private-black">'

# O shell fala os literais do MODELO (stephanie-vicente, a aluna-modelo do molde adulto).
# O builder troca por aluno. Trocar aqui e o mesmo que o base_swaps faz no imersivo.
NOMES = [
    ("Marcos Mansour", "Stephanie Vicente"),
    ("Mansour", "Vicente"),
    ("Marcos", "Stephanie"),
    ("marcos_pv_v1", "MODELO_STORE"),   # vira derivado do ARTEFATO.id, ver STORE_DERIVADO
]

# P1 §3: "dado pessoal em identificador tecnico vaza para fora da interface e sobrevive a
# toda troca de rotulo". O artefato guarda o estado em 'marcos_pv_v1' -- uma chave montada
# com o nome de uma pessoa. Isto NAO e divergencia do artefato: e o proprio P1 sendo
# obedecido onde o artefato, sendo pagina de uma pessoa so, nao precisou obedecer.
#
# A chave e LITERAL, montada no build, e nao 'pv_'+artefatoId()+'_v1' em tempo de execucao.
# Tentei a segunda forma primeiro e ela QUEBROU O BOOT INTEIRO: `var STORE` aparece na secao
# de persistencia, muito antes de `var ARTEFATO` ser declarado, entao artefatoId() rodava com
# ARTEFATO ainda undefined -- "Cannot read properties of undefined (reading 'id')". O HTML
# continuava valido, todo gate estatico continuava verde, e o boot morria na primeira linha
# levando junto TUDO o que vinha depois (P2 §25: a excecao no boot nao fica onde nasceu).
# Quem pegou foi o GATE 35, no navegador, comparando com o artefato -- que boota limpo.
MODELO_ID = "private-black-modelo"
STORE_DERIVADO = "var STORE='pv_" + MODELO_ID + "_v1';"



# ---------------------------------------------------------------- corte de JS
#
# Cortar funcao por "proximo } em coluna 0" nao serve: 34 das 186 funcoes deste JS cabem
# numa linha so, e o corte levaria junto tudo ate a proxima funcao multilinha. Entao o
# corte e por BALANCO de chaves, com um scanner que sabe o que e codigo e o que nao e --
# string ('..', "..", `..`), comentario (// e /* */) e literal de expressao regular. Sem
# isso, um `{` dentro de "/[^a-z]{2}/" ou de um comentario desequilibra a conta e o corte
# come o arquivo.
_ANTES_DE_REGEX = set("(,=:[!&|?{};\n+-*%~^<>")


def fim_do_bloco(js, i):
    """Indice logo APOS a chave que fecha o primeiro `{` em ou depois de i."""
    n = len(js)
    while i < n and js[i] != "{":
        i += 1
    if i >= n:
        raise SystemExit("bloco sem { a partir de " + str(i))
    prof = 0
    ultimo_signif = ""
    while i < n:
        c = js[i]
        if c in "'\"`":
            aspas = c
            i += 1
            while i < n:
                if js[i] == "\\":
                    i += 2
                    continue
                if js[i] == aspas:
                    break
                i += 1
            i += 1
            ultimo_signif = "x"
            continue
        if c == "/" and i + 1 < n and js[i + 1] == "/":
            i = js.find("\n", i)
            if i < 0:
                break
            continue
        if c == "/" and i + 1 < n and js[i + 1] == "*":
            i = js.find("*/", i) + 2
            continue
        if c == "/" and (ultimo_signif in _ANTES_DE_REGEX or ultimo_signif == ""):
            i += 1
            while i < n:
                if js[i] == "\\":
                    i += 2
                    continue
                if js[i] == "[":
                    while i < n and js[i] != "]":
                        i += 2 if js[i] == "\\" else 1
                if js[i] == "/":
                    break
                if js[i] == "\n":
                    break
                i += 1
            i += 1
            ultimo_signif = "x"
            continue
        if c == "{":
            prof += 1
        elif c == "}":
            prof -= 1
            if prof == 0:
                return i + 1
        if not c.isspace():
            ultimo_signif = c
        i += 1
    raise SystemExit("bloco nao fecha")


def remove_funcao(js, nome, rel):
    """Remove `function nome(...){...}` inteira, e os comentarios colados nela acima."""
    m = re.search(r"^function " + re.escape(nome) + r"\s*\(", js, re.M)
    if not m:
        rel.setdefault("js/nao-achou", []).append(nome)
        return js
    fim = fim_do_bloco(js, m.end())
    while fim < len(js) and js[fim] in ";\n":
        fim += 1
        if js[fim - 1] == "\n":
            break
    return js[: m.start()] + js[fim:]


def remove_var(js, nome, rel):
    """Remove `var NOME = ...;` de topo, seja objeto, array ou literal de uma linha."""
    m = re.search(r"^var " + re.escape(nome) + r"\s*=", js, re.M)
    if not m:
        rel.setdefault("js/nao-achou", []).append(nome)
        return js
    resto = js[m.end():].lstrip()
    if resto[:1] in "{[":
        fim = fim_do_bloco(js, m.end()) if resto[0] == "{" else None
        if fim is None:
            # array: mesmo balanco, com colchete
            i = js.index("[", m.end())
            prof, k = 0, i
            while k < len(js):
                if js[k] == "[":
                    prof += 1
                elif js[k] == "]":
                    prof -= 1
                    if prof == 0:
                        fim = k + 1
                        break
                k += 1
    else:
        fim = js.index("\n", m.end())
    while fim < len(js) and js[fim] in ";\n":
        fim += 1
        if js[fim - 1] == "\n":
            break
    return js[: m.start()] + js[fim:]


def fecha_tag(s, i, tag="div"):
    """Indice logo APOS o fechamento da tag aberta em i. Por BALANCO, nunca pelo primeiro
    </div> -- o primeiro fecha um filho (P2: 'nunca extrair bloco ate </div>')."""
    depth = 0
    for m in re.finditer(r"<" + tag + r"\b|</" + tag + r"\s*>", s[i:]):
        depth += 1 if not m.group(0).startswith("</") else -1
        if depth == 0:
            return i + m.end()
    raise SystemExit(f"tag <{tag}> aberta em {i} nao fecha")


def mascara_script_style(s):
    """Copia de s com o MIOLO de <script>/<style> neutralizado, mantendo os offsets.

    Sem isto, qualquer varredura por '<div' encontra '<div' dentro de string JS e de
    comentario CSS, e o balanco de tags passa a mentir."""
    out = list(s)
    for m in re.finditer(r"<(script|style)\b[^>]*>(.*?)</\1\s*>", s, re.S):
        for k in range(m.start(2), m.end(2)):
            if out[k] != "\n":
                out[k] = "."
    return "".join(out)


def corpo_do_artefato():
    """O documento REAL, sem a moldura do claude.ai.

    O .html que o navegador salva traz o frame-runtime do host: dois <script>, um <style>
    e um <body data-view="professor"> proprios. O documento do artefato comeca DEPOIS
    disso, e traz os proprios <meta>, <title> e <style> -- escritos como se fossem head,
    porque o host injeta tudo dentro do body."""
    with open(ARTEFATO, encoding="utf-8") as fh:
        h = fh.read()
    i = h.find('<body data-view="professor">')
    if i < 0:
        raise SystemExit("artefato sem <body data-view=...>: a moldura mudou de forma")
    ini = h.index(">", i) + 1
    fim = h.rindex("</body>")
    return h[ini:fim]


def monta_documento(corpo, lang="pt-BR", view="professor"):
    """Reconstroi um documento HTML de verdade: o que o artefato escreveu como se fosse
    head volta para o head."""
    # o head do artefato vai ate o fim do ULTIMO <style> antes do primeiro <div>
    prim_div = corpo.index("<div ")
    ult_style = corpo.rindex("</style>", 0, prim_div) + len("</style>")
    cabeca, resto = corpo[:ult_style], corpo[ult_style:]
    cabeca = cabeca.replace('<meta charset="UTF-8">', "", 1).strip()
    return (
        "<!DOCTYPE html>\n"
        f'<html lang="{lang}">\n<head>\n'
        '<meta charset="UTF-8">\n'
        f"{CARIMBO}\n"
        f"{cabeca}\n"
        f"</head>\n<body data-view=\"{view}\">\n"
        f"{resto.strip()}\n</body>\n</html>\n"
    )


def deriva_professor():
    rel = {}
    corpo = corpo_do_artefato()
    for velho, novo in NOMES:
        rel[f"swap/{velho}"] = corpo.count(velho)
        corpo = corpo.replace(velho, novo)
    # a chave de estado deixa de carregar nome de pessoa (P1 §3)
    antes = corpo
    corpo = re.sub(r"var STORE='MODELO_STORE';", STORE_DERIVADO, corpo)
    corpo = corpo.replace("localStorage.getItem('MODELO_STORE')",
                          "localStorage.getItem('pv_" + MODELO_ID + "_v1')")
    rel["store/derivado-do-artefato-id"] = 1 if corpo != antes else 0
    # o id tecnico do artefato passa a ser o do MODELO
    corpo, n = (re.subn(r"var ARTEFATO=\{id:'[^']*'\}",
                        "var ARTEFATO={id:'" + MODELO_ID + "'}", corpo))
    rel["artefato-id/modelo"] = n
    return monta_documento(corpo), rel



def remove_por_atributo(s, atributo, rel, rotulo):
    """Remove elementos INTEIROS cuja tag de abertura carrega o atributo.

    Acha as fronteiras sobre a MASCARA (o balanco tem de ignorar o miolo de script/style) e
    recorta o texto real nos mesmos offsets."""
    n = 0
    while True:
        hm = mascara_script_style(s)
        # <body data-view="professor"> tambem casa, e remove-lo levaria o DOCUMENTO INTEIRO.
        # Aconteceu na primeira tentativa: 604 KB viraram 105 KB e o erro so apareceu
        # tres passos adiante, quando o <script> nao foi encontrado. Elemento de estrutura
        # nao e conteudo: o papel dele se troca, nao se remove.
        m = None
        for cand in re.finditer(r"<(\w+)[^>]*\b" + re.escape(atributo) + r"[^>]*>", hm):
            if cand.group(1).lower() not in ("body", "html"):
                m = cand
                break
        if not m:
            break
        j = fecha_tag(hm, m.start(), m.group(1))
        # trava contra remocao desgovernada: nenhum elemento docente e um terco do arquivo
        if (j - m.start()) > len(s) // 3:
            raise SystemExit(
                f"{rotulo}: <{m.group(1)}> em {m.start()} levaria {j - m.start()} bytes "
                f"de {len(s)} — o balanco de tags saiu do lugar, nao remova as cegas")
        s = s[: m.start()] + s[j:]
        n += 1
        if n > 500:
            raise SystemExit("laco de remocao nao converge: " + rotulo)
    rel[rotulo] = n
    return s


def remove_elemento(s, abertura_rx, tag, rel, rotulo):
    n = 0
    while True:
        hm = mascara_script_style(s)
        m = re.search(abertura_rx, hm)
        if not m:
            break
        j = fecha_tag(hm, m.start(), tag)
        s = s[: m.start()] + s[j:]
        n += 1
    rel[rotulo] = n
    return s


# ============================================================ BUILD DO ALUNO
#
# Nao e "o mesmo arquivo com pedacos escondidos": e OUTRO BUILD. A regra e da Stephanie
# (24/08/2026), e esta no 00 §5, no 04 §13, no P1 §3.1, no P2 §3.2 e no P3 §3:
#
#     "A URL do aluno contem exclusivamente o conteudo destinado ao aluno. Gabaritos,
#      Teacher's Guide, registros internos, hipoteses pedagogicas, evidencias reservadas e
#      controles docentes nao podem estar apenas ocultos no HTML do aluno: nao devem
#      integrar o arquivo, payload ou estado entregue por essa URL."
#
# Tres camadas saem, e as tres importam:
#   1. o MARKUP docente (o que `data-view="professor"` marca, o deck, o painel do guia);
#   2. os DADOS docentes do JS -- e aqui mora o que mais doeria vazar: PC_NOTAS sao os
#      gabaritos das seis atividades do pre-class, 5,4 KB de resposta pronta;
#   3. as ROTAS -- `?mode=teacher-guide` e o alternador de visao. O P3 §3 e explicito:
#      "a URL do aluno nao possui alternador, rota de professor ou elevacao de papel por
#      query, hash, armazenamento, atributo ou chamada direta".

# Dados que nao sao do aluno. O comentario diz de quem e cada um, porque a lista sem motivo
# e a primeira coisa que alguem "limpa" no futuro.
VARS_DOCENTES = [
    "GUIDE",        # o Teacher's Guide inteiro, 14 campos por aula
    "TG_SEM_NOTA",  # rotulo do painel do guia
    "PC_NOTAS",     # OS GABARITOS do pre-class
    "CP", "CP_MINIMO",          # checkpoint: registro interno
    "EP_MAPA", "EP_SEM_AUTO",   # estado pedagogico do ciclo
    "ESCALA", "ENGAJ", "AVAL_CRIT",  # escalas do registro pos-aula
    "STAGES",                   # a espinha, que so o deck desenha
    "TALK_19",      # o dialogo do in-class
    "BRIEF_20",     # o documento de leitura do in-class
    # CAST, VOICE_PREF e MSG_20 FICAM: as vozes servem ao audio do pre-class, e a mensagem
    # do parceiro e conteudo do pre-class (#msg20-box). Eu os tinha tirado por prefixo, e
    # foi o proprio cruzamento de referencias que mostrou o erro.
    "GD_ITEMS", "GD_COLS", "GD_V",    # o sorting do guided discovery, no deck
    "RECAP19", "RECAP20", "CONF19", "CONF20", "CONF_LB",  # o fecho da aula, no deck
    "NUM_EXT",      # numeral por extenso: so o rotulo de etapas usa
]

# Funcoes docentes. Agrupadas pelo motivo, nao pelo prefixo.
FUNCOES_DOCENTES = [
    # O Teacher's Guide e a ROTA que o abre. O P3 §3 nomeia exatamente isto: "a URL do aluno
    # nao possui alternador, rota de professor ou elevacao de papel por query, hash,
    # armazenamento, atributo ou chamada direta".
    "tgAberto", "tgClose", "tgToggle", "tgURL", "tgAbrir", "tgLinha", "tgCabecaHTML",
    "tgModoPedido", "tgModoAplica", "tgModoIr", "tgModoPinta",
    # o alternador de visao
    "setView",
]

# POR QUE A LISTA E CURTA, E POR QUE ISSO ESTA CERTO
# --------------------------------------------------
# A primeira versao removia ~90 funcoes -- todo o deck, o registro pos-aula, os gabaritos, o
# sorting. Cruzando os nomes removidos com o que sobrava, apareceram 38 referencias orfas, e
# elas ensinaram duas coisas:
#
#   1. EU TINHA CLASSIFICADO ERRADO POR PREFIXO. `sayAs` toca o audio do PRE-CLASS,
#      `rcStart` grava a fala do ALUNO, `unlockTranscript` abre a transcricao do pre-class,
#      `abrirBloco` e o expansor de conteudo extra, `ask*` e o dialogo que o "Reset my
#      answers" usa. Levar tudo por prefixo teria quebrado o material do aluno.
#
#   2. O QUE A NORMA PROIBE E CONTEUDO E ROTA, NAO CODIGO INERTE. Uma funcao que desenha um
#      gabarito, sem o gabarito, nao entrega gabarito nenhum -- e ela e chamada so pelo boot,
#      que neste build nao a chama. O que nao pode existir e o DADO (PC_NOTAS, GUIDE, CP) e
#      o CAMINHO que promove papel (?mode=teacher-guide, o alternador).
#
# Remover menos tambem e mais seguro: cada funcao a menos e uma chance a menos de deixar uma
# chamada viva apontando para o vazio. O gate de isolamento cobra o resultado -- o que o
# arquivo ENTREGA --, nao o tamanho da lista.

# O boot do aluno chama SO o que e dele. Escrito aqui, e nao filtrado do boot do professor,
# porque a ordem entre estas chamadas e significativa (o cabecalho do boot original explica
# cada uma) e um filtro por nome a perderia em silencio.
BOOT_ALUNO = """/* ---------------- boot (build do aluno) ---------------- */
/* So o que e do aluno. Nao ha deck, nao ha guia, nao ha registro pos-aula -- e nao ha as
   funcoes que os construiriam: elas nao vieram neste build. */
document.addEventListener('DOMContentLoaded',function(){
  document.body.setAttribute('data-view','aluno');
  migraLinguagem();
  persInit();
  tabFromHash();
  window.addEventListener('hashchange',tabFromHash);
  pwRestore([['pw19-subject',null,'post_l19_subject'],['pw19-body','pw19-count','post_l19_writing'],
             ['pw20-subject',null,'post_l20_subject'],['pw20-body','pw20-count','post_l20_writing']]);
  preKeys();
  hubPaint();
  preInit();
  sfBuild();
  audBuild();
});"""


def deriva_aluno(html_prof):
    rel = {}
    s = html_prof
    # O documento nasce declarando o papel. O script inicial tambem o fixa, mas o ATRIBUTO
    # entregue tem de ser o certo: entre o byte servido e o boot existe uma janela, e nela a
    # folha de estilo do professor e que estaria valendo.
    s = s.replace('<body data-view="professor">', '<body data-view="aluno">', 1)
    rel["markup/papel-do-documento"] = 1

    # ---- 1. markup docente
    s = remove_por_atributo(s, 'data-view="professor"', rel, "markup/data-view=professor")
    s = remove_elemento(s, r'<div class="slides-wrapper"', "div", rel, "markup/deck")
    s = remove_elemento(s, r'<div class="stage-bar"', "div", rel, "markup/stage-bar")
    s = remove_elemento(s, r'<div class="teacher-t-panel"[^>]*>', "div", rel,
                        "markup/painel-do-guia")
    s = remove_elemento(s, r'<div class="view-switch"', "div", rel, "markup/alternador")
    # Estes dois sao docentes e NAO carregam data-view="professor" -- so apareceram quando
    # cruzei os nomes removidos com o que o HTML ainda chamava. Estrutura se acha pela
    # funcao, nao pela marca que alguem lembrou de por.
    s = remove_elemento(s, r'<div class="stage-labels"[^>]*>', "div", rel,
                        "markup/rotulos-de-etapa")
    s = remove_elemento(s, r'<div class="tg-guia"[^>]*>|<div[^>]*id="tgGuia"[^>]*>', "div",
                        rel, "markup/pagina-do-guia")
    s, n = re.subn(r'\s*data-teacher="[^"]*"', "", s)
    rel["markup/nota-do-professor"] = n
    # o gatilho do painel do guia (a tecla T tem um botao proprio, fora do painel)
    s, n = re.subn(r'<button[^>]*id="teacherT"[^>]*>.*?</button>', "", s, flags=re.S)
    rel["markup/botao-do-guia"] = n
    # O mapa do ciclo vem do artefato JA PINTADO na visao do professor -- com
    # onclick="openLesson(N)" em cada casa. O mapaPaint o refaz no boot, e na visao do aluno
    # a casa e informacao, nao botao (P1 §9). Esvaziar aqui e o que impede que a versao
    # docente seja ENTREGUE, mesmo que nunca chegue a ser vista.
    s, n = re.subn(r'(<div[^>]*id="cicloMapa"[^>]*>).*?(</div>)', r"\1\2", s, flags=re.S)
    rel["markup/mapa-repintado"] = n
    # Comentario de HTML e prosa interna entregue ao aluno. No build do professor ele e
    # memoria de trabalho; aqui e so byte que fala do que nao e dele.
    s, n = re.subn(r"<!--.*?-->", "", s, flags=re.S)
    rel["markup/comentarios"] = n

    # ---- 2. o JS entregue
    ini = s.rfind("<script>")
    cabeca, js = s[:ini], s[ini:]
    # O BOOT SAI PRIMEIRO. Trocado depois das remocoes, o marcador ja teria sido levado por
    # alguma delas -- e o corte cairia no lugar errado, em silencio.
    i = js.index("document.addEventListener('DOMContentLoaded',function(){\n  deckInit(")
    j = js.index("\n});", i) + len("\n});")
    js = js[:i] + BOOT_ALUNO + js[j:]
    rel["js/boot"] = 1

    # O ouvinte de teclado do DECK. Ele so age em slide-mode ou no modo guia -- nenhum dos
    # dois existe aqui --, mas e onde moram as ultimas citacoes de tgToggle e tgModoIr, e e
    # navegacao docente. Sai inteiro; o Escape do pre-class tem ouvinte proprio.
    i = js.find("document.addEventListener('keydown',function(e){")
    while i >= 0:
        fim = fim_do_bloco(js, js.index("{", i + 40))
        corpo = js[i:fim]
        if "slide-mode" in corpo:
            enc = js.find(");", fim)
            js = js[:i] + js[enc + 2:]
            rel["js/teclado-do-deck"] = 1
            break
        i = js.find("document.addEventListener('keydown',function(e){", fim)
    for v in VARS_DOCENTES:
        js = remove_var(js, v, rel)
    for f in FUNCOES_DOCENTES:
        js = remove_funcao(js, f, rel)
    s = cabeca + js

    # ---- 3. a visao NAO SE PROMOVE
    #
    # O script inicial do artefato le o papel gravado e cai em 'professor' por padrao. Num
    # build do aluno isso e uma ROTA: basta um valor no armazenamento para a pagina se
    # declarar docente. O P3 §3 nomeia essa porta -- "elevacao de papel por query, hash,
    # armazenamento, atributo ou chamada direta". Aqui o papel e constante.
    #
    # A primeira versao desta substituicao era uma regex que NAO CASOU, e o `rel` dizia 1 de
    # qualquer jeito -- relatorio que afirma o que nao mediu. Agora acha o script pelo
    # CONTEUDO e conta o que trocou.
    alvo = None
    for m in re.finditer(r"<script>(.*?)</script>", s, re.S):
        if "d.view===" in m.group(1) or "d.view ===" in m.group(1):
            alvo = m
            break
    if alvo is None:
        raise SystemExit("build do aluno: nao achei o script que fixa a visao inicial")
    s = (s[: alvo.start()] +
         "<script>\n/* Build do aluno: a visao e CONSTANTE. Nao se le do armazenamento e nao\n"
         "   ha outra para a qual alternar -- o papel nao se promove (P3 §3). */\n"
         "document.body.setAttribute('data-view','aluno');\n</script>" +
         s[alvo.end():])
    rel["js/visao-fixa"] = 1
    return s, rel


def escreve(caminho, conteudo, check):
    atual = None
    if os.path.exists(caminho):
        with open(caminho, encoding="utf-8") as fh:
            atual = fh.read()
    if check:
        return "IGUAL" if atual == conteudo else ("DIFERE" if atual is not None else "AUSENTE")
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(conteudo)
    return "escrito"


def main():
    check = "--check" in sys.argv
    prof, rel_p = deriva_professor()
    aluno, rel_a = deriva_aluno(prof)

    print("=== derivacao do artefato ===")
    for k, v in rel_p.items():
        print(f"  professor  {k:42s} {v}")
    for k, v in rel_a.items():
        print(f"  aluno      {k:42s} {v}")

    r1 = escreve(SHELL_PROF, prof, check)
    r2 = escreve(SHELL_ALUNO, aluno, check)
    print(f"\n  {os.path.relpath(SHELL_PROF, RAIZ):46s} {len(prof):8d} bytes  {r1}")
    print(f"  {os.path.relpath(SHELL_ALUNO, RAIZ):46s} {len(aluno):8d} bytes  {r2}")
    if check and (r1 != "IGUAL" or r2 != "IGUAL"):
        print("\nFALHOU — o shell no disco NAO e o que sairia do artefato hoje.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
