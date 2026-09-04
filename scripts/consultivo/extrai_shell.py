#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deriva os DOIS shells da anatomia `consultivo` DO ARTEFATO, por script.

POR QUE POR SCRIPT, E NAO A MAO
-------------------------------
O artefato (`_build/model/artefatos/marcos-consultivo.html`) e a ESPECIFICACAO da
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

    shells/consultivo.html        professor: as 6 abas, o deck, o guia, a previa do aluno

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
    python3 scripts/consultivo/extrai_shell.py            # escreve os dois shells
    python3 scripts/consultivo/extrai_shell.py --check    # nao escreve: confere o disco
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTEFATO = os.path.join(RAIZ, "_build", "model", "artefatos", "marcos-consultivo.html")
SHELLS = os.path.join(RAIZ, "_build", "model", "shells")
SHELL_PROF = os.path.join(SHELLS, "consultivo.html")
SHELL_ALUNO = os.path.join(SHELLS, "consultivo-aluno.html")

import _motor_audio  # a troca do motor de audio (AUT-004), declarada em modulo proprio

CARIMBO = '<meta name="alumni-anatomia" content="consultivo">'

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
MODELO_ID = "consultivo-modelo"
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


# ---------------------------------------------------------------------------
# CORRECOES AO ARTEFATO — revisao de 28/08/2026 (material do Luiz Bressane)
#
# Cada entrada e (rotulo, ancora, substituicao). A ancora e um trecho do ARTEFATO e tem de
# casar exatamente uma vez: se o artefato mudar embaixo, a extracao PARA e diz qual correcao
# perdeu o pe -- em vez de aplicar no lugar errado ou sumir em silencio.
CORRECOES = [

 # ---- A ESCRITA DO POST-CLASS PRECISA DE UM "PRONTO" (revisao de 04/09/2026)
 #
 # O texto ja era salvo a cada tecla (`pwCount` chama `save`), e a aluna nao tinha como
 # saber disso: a unica acao visivel embaixo da caixa era "Clear and start again" -- um
 # botao que APAGA. Escrever sem nenhum sinal de que ficou guardado e escrever sem saber se
 # valeu, e num material em que ela ja abandonou um curso por achar que o problema era ela,
 # a diferenca nao e cosmetica.
 #
 # O Confirm nao inventa persistencia nova: ele salva o que ja seria salvo e DIZ que salvou.
 # Fica ao lado do Clear, que continua sendo a saida para recomecar. O rotulo vem do
 # EMISSOR (`render.rot_confirm`), porque so ele sabe se o material e bilingue -- o mesmo
 # caminho do `data-redo` do botao de conferir.
 ("post-class-escrita-confirm",
  """function pwRestore(pares) {""",
  """function pwOk(idTexto, chave, idAviso, btn) {
  var el = document.getElementById(idTexto); if (!el) return;
  save(chave, el.value);
  save(chave + '_ok', el.value.trim() ? '1' : '');
  var av = document.getElementById(idAviso);
  if (av) {
    av.textContent = el.value.trim()
      ? (btn && btn.getAttribute('data-ok') || 'Saved')
      : (btn && btn.getAttribute('data-vazio') || 'Nothing written yet');
    av.style.display = 'block';
  }
}
function pwRestore(pares) {"""),

 # ---- O MATERIAL NAO E MAIS PROTOTIPO (revisao de 02/09/2026)
 #
 # O pre-class abria com "Prototype audio: the voices in this version are temporary." Era
 # verdade quando o artefato foi escrito e deixou de ser: o audio do consultivo e gerado pelo
 # `gen_audio_consultivo.py`, sai do ElevenLabs com Voice ID por PAPEL (Anexo P-A §4) e passa
 # pelo GATE 40, que reprova sintese de navegador. As vozes que a aluna ouve sao as vozes.
 #
 # E a linha nao e neutra: ela e a primeira coisa que o aluno le na aba que ele mais usa, e
 # diz que o que ele tem na mao e um rascunho. Aviso de provisoriedade que sobrevive ao
 # provisorio ensina a nao acreditar no material.
 ("sem-aviso-de-prototipo",
  """<p class="nota-sigla" id="avisoAudioProto" lang="en">Prototype audio: the voices in this version are temporary.</p>
""",
  """"""),

 # ---- O TEACHER'S GUIDE EXTERNO PERDE O CABECALHO DE AULA (revisao de 02/09/2026)
 #
 # A janela do guia tinha duas pecas empilhadas: um CABECALHO com treze campos da aula
 # (Goals, Communicative product, Teacher preparation, Lesson overview, Answer key...) e,
 # embaixo, o PROCEDIMENTO da tela corrente, que muda a cada Previous/Next.
 #
 # O cabecalho era escrito uma vez e ficava. Como so o procedimento troca, a professora
 # atravessava os treze campos DE NOVO a cada tela para chegar na unica parte que tinha
 # mudado -- dez vezes por aula. O guia que existe para ser lido DURANTE a aula estava
 # organizado como documento de preparacao.
 #
 # E ele ja e documento de preparacao em outro lugar: o cartao da aula, na aba Aulas, tem
 # "Estrutura e preparacao" (`lcprep{N}`) com objetivo, produto, percurso, o que ler antes e
 # como conduzir -- em portugues, que e a lingua do professor brasileiro. O cabecalho do guia
 # era a mesma coisa em ingles, no lugar errado.
 #
 # Isto continua a decisao de 31/08/2026, que ja havia tirado `Lesson identity` dali pelo
 # mesmo argumento (metadado de producao no alto da pagina que se abre para dar aula). O que
 # muda agora e o alcance: sai o cabecalho inteiro, e a janela passa a ser o que o titulo
 # dela sempre prometeu -- "Stage-by-stage procedure".
 #
 # Sao tres ancoras porque a peca tem tres partes: o no do DOM, as funcoes que o montam e a
 # linha que o preenche. Tirar so uma deixaria codigo morto ou um buraco na tela.
 ("guia-sem-cabecalho/dom",
  """<div class="tg-guia-cabeca" id="tgGuiaCabeca"></div>
<p class="tg-guia-proc">Stage-by-stage procedure</p>""",
  """<!-- O cabecalho de treze campos saiu em 02/09/2026: ele nao mudava de tela em tela e
     empurrava o procedimento para baixo em todas elas. A preparacao da aula vive no cartao
     da aula ("Estrutura e preparacao"), que e onde se prepara. Aqui e a hora da aula. -->
<p class="tg-guia-proc">Stage-by-stage procedure</p>"""),

 ("guia-sem-cabecalho/funcoes",
  """function tgLinha(rot,txt){
  if(!txt)return '';
  return '<div class="tg-campo"><b>'+rot+'</b><div>'+txt+'</div></div>';
}
function tgCabecaHTML(n){
  var G=GUIDE[n]; if(!G)return '';
  var L=LESSONS[n]||{},h='',i,s=stagesOf(n)||[];
  h+=tgLinha('Lesson identity',G.identity);
  h+=tgLinha('Goals',G.goals);
  h+=tgLinha('Communicative product',G.product);
  h+=tgLinha('Success criteria',G.criteria);
  h+=tgLinha('Teacher preparation',G.prep);
  var ov='<ul class="tg-ov">';
  for(i=0;i<s.length;i++)ov+='<li><span>'+(i+1)+' &middot; '+s[i].n+'</span><em>'+s[i].min+' min</em></li>';
  ov+='</ul><p class="tg-ov-tot">'+somaEtapas(n)+' minutes of essential path, plus 5 minutes of operational margin.</p>';
  h+=tgLinha('Lesson overview',ov);
  h+=tgLinha('Language focus',G.language);
  /* Campo proprio, e nao uma linha perdida na preparacao: o adendo normativo exige que o
     guia declare QUANDO abrir o transcript, e uma regra que vive dentro de outro campo e uma
     regra que ninguem acha na hora da aula. */
  h+=tgLinha('Transcript',G.transcript);
  h+=tgLinha('Anticipated difficulties',G.difficulties);
  h+=tgLinha('Scaffolding and challenge',G.scaffolding);
  h+=tgLinha('Feedback and retask',G.feedback);
  h+=tgLinha('Evidence to record',G.evidence);
  h+=tgLinha('Pre/post-class connection',G.prepost);
  h+=tgLinha('Answer key / possible answers',G.key);
  return h;
}
""",
  """/* `tgLinha` e `tgCabecaHTML` sairam com o cabecalho, em 02/09/2026. Funcao que ninguem
   chama e a forma mais silenciosa de um pedaco removido voltar: basta alguem reintroduzir a
   chamada sem reabrir a decisao. `GUIDE` continua no arquivo -- ele e a fonte declarada da
   aula e outros gates o leem -- mas ja nao pinta nada nesta janela. */
"""),

 ("guia-sem-cabecalho/css",
  """/* --- cabecalho do Teacher's Guide, na janela separada ---
   O painel dentro do deck mostra a NOTA da tela. A janela mostra o GUIA: os catorze campos
   primeiro, e o procedimento tela a tela depois, navegavel. Duas pecas, um lugar cada. */
.tg-guia-cabeca{margin-bottom:var(--space-6);padding-bottom:var(--space-5);
  border-bottom:1px solid rgba(255,255,255,.22)}
.tg-campo{margin-bottom:var(--space-4h)}
.tg-campo>b{display:block;font-family:var(--font-interface);font-size:.72rem;
  font-weight:var(--peso-forte);letter-spacing:var(--ls-rotulo);text-transform:uppercase;
  color:var(--d-accent);margin-bottom:var(--space-2)}
.tg-campo>div{font-size:.95rem;line-height:var(--lh-corpo);color:var(--d-text-mid)}
.tg-campo strong{color:var(--d-text)}
.tg-campo em{color:var(--d-text-dim);font-style:italic}
.tg-campo ul,.tg-campo ol{margin:var(--space-2) 0 0;padding-left:var(--space-4h)}
.tg-campo li{margin-bottom:var(--space-2)}
.tg-ov{list-style:none;margin:var(--space-2) 0 0;padding:0}
.tg-ov li{display:flex;justify-content:space-between;gap:var(--space-4);
  padding:var(--space-2) 0;border-bottom:1px solid rgba(255,255,255,.14);margin:0}
.tg-ov li em{font-style:normal;font-variant-numeric:tabular-nums;color:var(--d-text-dim)}
.tg-ov-tot{margin:var(--space-3) 0 0;font-size:.86rem;color:var(--d-text-dim)}
.tg-guia-proc{""",
  """/* --- o Teacher's Guide, na janela separada ---
   A janela mostra o PROCEDIMENTO da tela corrente, e so ele. As regras do cabecalho
   (.tg-guia-cabeca, .tg-campo, .tg-ov) sairam junto com ele em 02/09/2026: CSS de peca que
   nao existe mais e um convite a que a peca volte sem que ninguem decida isso. */
.tg-guia-proc{"""),

 ("guia-sem-cabecalho/pintura",
  """  el=document.getElementById('tgGuiaCabeca');
  if(el&&!el.getAttribute('data-pronto')){
    el.innerHTML=tgCabecaHTML(_tgN);
    el.setAttribute('data-pronto','1');
  }
  el=document.getElementById('tgGuiaPos');""",
  """  el=document.getElementById('tgGuiaPos');"""),

 # ---- O CARD EXPANDIVEL CARREGA A FOLGA DEPOIS DELE (revisao de 02/09/2026)
 #
 # Mesma correcao que o apoio em portugues ja recebeu em 01/09 (`render.apoio_pt`), agora
 # como REGRA da forma em vez de um estilo inline num emissor. O gatilho de um card
 # expandivel saia com margem so no topo: fechado -- que e como ele nasce -- o proximo
 # elemento encostava nele. Na tela 5 da aula 9 da Joice, o botao "The invitation" ficava
 # colado no primeiro item do exercicio, sem um pixel entre os dois.
 #
 # A MARGEM DE BAIXO E DO GATILHO, NAO DO QUE VEM DEPOIS. Se ela vivesse no exercicio, cada
 # peca que algum dia venha depois de um card teria de lembrar de trazer a sua.
 #
 # A regra pega o gatilho pelo COMPORTAMENTO (`onclick` que chama `toggleEl`) e so quando ele
 # e filho direto de `.slide-inner`, isto e, um controle que ocupa a linha inteira. O gatilho
 # que vive dentro de uma barra flex -- os "Show transcript" ao lado dos controles de audio --
 # fica de fora de proposito: ali a folga ja e da barra, e margem inferior num item de flex
 # com `align-items:center` desalinha a linha em vez de espacar.
 #
 # O painel `.transcript-box` ganha a sua pelo mesmo motivo do `.callout` do apoio em PT:
 # aberto, ele encostava na lista de perguntas logo abaixo.
 ("card-expandivel-tem-folga",
  """.transcript-box{margin-top:var(--space-3h);padding:var(--space-4) var(--space-4h);
  background:rgba(255,255,255,.6);border:1px solid var(--border);border-radius:10px}""",
  """.transcript-box{margin:var(--space-3h) 0 var(--space-4h);padding:var(--space-4) var(--space-4h);
  background:rgba(255,255,255,.6);border:1px solid var(--border);border-radius:10px}

/* Todo card expandivel tem folga DEPOIS do gatilho -- ver o comentario da correcao
   `card-expandivel-tem-folga` em scripts/consultivo/extrai_shell.py. */
.slide-inner > [onclick^="toggleEl("]{margin-bottom:var(--space-4)}"""),

 # ---- O QUE E AZUL-MARINHO NAO SE LE NO ESCURO (revisao de 02/09/2026)
 #
 # `.task-instr` e `.verify-all-btn.ghost` nasceram com as cores do fundo CLARO
 # (`--text-mid` #33405E e `--accent` #003080) e nunca ganharam a variante escura que os
 # vizinhos tem (`.btn-ghost`, `.audio-btn-sm.ghost`, `.aud-estado` -- todos com regra
 # `.slide-dark`/`.slide-open` logo acima). Numa tela escura o resultado, medido no
 # navegador com a razao WCAG computada:
 #
 #     .verify-all-btn.ghost   1.49 : 1   (minimo 4.5)   -- o botao "Check" some
 #     .task-instr             1.75 : 1   (minimo 4.5)   -- a pergunta do exercicio some
 #
 # Sao 28 ocorrencias em 4 dos 6 materiais. A pergunta apagada e a pior das duas: o
 # enunciado de `escolha` sai como `.task-instr`, entao a tela mostra as alternativas e
 # esconde o que esta sendo perguntado.
 #
 # As cores nao sao novas -- sao as mesmas `--d-accent` e `--d-text-mid` que as regras
 # vizinhas ja usam, e que medem 6.58 e 12.01 sobre `--dark`. Faltava so escrever a regra.
 ("contraste-no-escuro-do-check-e-da-instrucao",
  """.slide-dark .audio-btn-sm.ghost,.slide-open .audio-btn-sm.ghost{color:var(--d-accent);border-color:var(--d-accent);background:transparent}""",
  """.slide-dark .audio-btn-sm.ghost,.slide-open .audio-btn-sm.ghost{color:var(--d-accent);border-color:var(--d-accent);background:transparent}
/* Ver a correcao `contraste-no-escuro-do-check-e-da-instrucao`: as duas regras abaixo
   faltavam, e no escuro davam 1.49:1 e 1.75:1. */
.slide-dark .verify-all-btn.ghost,.slide-open .verify-all-btn.ghost{color:var(--d-accent);border-color:var(--d-accent)}
.slide-dark .verify-all-btn.ghost:hover,.slide-open .verify-all-btn.ghost:hover{background:var(--d-accent);color:var(--dark)}
.slide-dark .task-instr,.slide-open .task-instr{color:var(--d-text-mid)}"""),

 ("answer-key-sem-no-in-class",
  """      if(nota.duvida)h+=akLinha('Pode gerar dúvida',nota.duvida);
      if(nota.inclass)h+=akLinha('No in-class',nota.inclass);""",
  """/* O pre-aula NAO antecipa a aula. A linha "No in-class" dizia a professora, dentro do
     gabarito de cada exercicio, em que etapa aquele conteudo voltaria -- e com isso ensinava
     o material a se escrever como ensaio do que vem: o autor precisava saber a etapa para
     preencher a linha, e o exercicio passava a existir em funcao dela. O pre-aula prepara,
     e prepara de OUTRA forma; a aula e o primeiro encontro com aquilo, nao o segundo.
     (Revisao da Joice, 31/08/2026.) */
      if(nota.duvida)h+=akLinha('Pode gerar dúvida',nota.duvida);"""),

 ("check-so-da-aluna",
  """#tab-preclass[data-consulta="1"] [data-k]{cursor:default}""",
  """#tab-preclass[data-consulta="1"] [data-k]{cursor:default}
/* O Check e o placar sao da aluna. Na visao do professor o gabarito ja esta a um clique no
   Answer Key de cada exercicio -- e o comentario acima ja dizia que botao ativo que nao deve
   ser usado e um convite. Faltava a regra que o tira da tela.

   Ela pende do PAPEL (`body[data-view]`), nunca de `data-consulta`: aquele atributo nasce
   cravado com "1" no HTML da aba e so o boot o corrige. Escrita sobre ele, a regra escondia
   o Check da ALUNA na janela entre o byte servido e o boot. Papel se le no papel. */
body[data-view="professor"] #tab-preclass .verify-all-btn,
body[data-view="professor"] #tab-preclass .score-out{display:none}"""),

 ("banco-correcao-e-porque",
  """.subprompt{font-size:.87rem;opacity:.62;line-height:var(--lh-corpo);max-width:72ch;margin-top:calc(-1 * var(--space-3h));margin-bottom:var(--space-4h)}""",
  """.subprompt{font-size:.87rem;opacity:.62;line-height:var(--lh-corpo);max-width:72ch;margin-top:calc(-1 * var(--space-3h));margin-bottom:var(--space-4h)}

/* Banco de palavras do gap-fill. Ele saia como `.subprompt` DEPOIS das frases, e essa classe
   nasce com margem de topo NEGATIVA -- existe para colar o subprompt no prompt de cima. No
   fim do exercicio, o mesmo -0.875rem puxava o banco para cima da ultima linha: as palavras
   ficavam sobrepostas. Aqui ele tem caixa propria, e o emissor o poe ANTES das frases, que e
   onde um banco serve para alguma coisa. */
.word-bank{display:flex;flex-wrap:wrap;align-items:baseline;gap:var(--space-2) var(--space-3);
  margin:0 0 var(--space-4h);padding:var(--space-3) var(--space-3h);
  border:1px solid var(--border);border-radius:8px;background:var(--bg-elevated)}
.word-bank .wb-rot{font-size:.72rem;font-weight:var(--peso-forte);letter-spacing:var(--ls-largo);text-transform:uppercase;opacity:.62}
.word-bank em{font-style:normal;font-weight:var(--peso-medio);color:var(--accent)}
.slide-dark .word-bank,.slide-open .word-bank{background:rgba(255,255,255,.06);border-color:var(--d-border)}
.slide-dark .word-bank em,.slide-open .word-bank em{color:var(--d-accent)}

/* A resposta certa, ao lado do item errado. A marca vermelha diz que errou; isto diz o que
   era. Discreto de proposito: e correcao, nao veredito. */
.row-fix{margin-left:var(--space-2h);font-size:.8rem;font-weight:var(--peso-medio);color:var(--accent);white-space:nowrap}
.slide-dark .row-fix,.slide-open .row-fix{color:var(--d-accent)}

/* E o PORQUE daquele item, que e outra coisa ainda: a cor diz que errou, o `row-fix` diz o
   que era, e so isto diz por que. Nasce FECHADO e abre ao conferir -- gabarito visivel antes
   da decisao continua sendo defeito. `flex-basis:100%` porque a linha e flex: assim ele cai
   embaixo, com a largura toda, em vez de disputar espaco com a resposta. */
.item-why{display:none;flex-basis:100%;margin-top:var(--space-2);padding-top:var(--space-2);border-top:1px solid rgba(201,211,228,.55);font-size:.8rem;line-height:var(--lh-corpo);color:var(--text-mid)}
.item-why.show{display:block;animation:fadeIn .25s ease}
.item-why em,.item-why strong{color:var(--accent)}
.quiz-option + .item-why{margin:calc(-1 * var(--space-1)) 0 var(--space-2);padding:0 var(--space-3h);border-top:none}
.slide-dark .item-why,.slide-open .item-why{color:var(--d-text-mid);border-top-color:var(--d-border)}
.slide-dark .item-why em,.slide-dark .item-why strong,.slide-open .item-why em,.slide-open .item-why strong{color:var(--d-accent)}

/* E a TRADUCAO daquele item -- outra coisa ainda que o porque. No material real-beginner o
   que falta a aluna sozinha no pre-class nao e mais uma explicacao em ingles: e saber o que
   a frase dizia. Mesma caixa, mesma abertura ao conferir; muda a barra na lateral e o
   italico, para ela distinguir num relance a traducao da explicacao. */
.item-pt{font-style:italic;border-top:none;margin-top:var(--space-1h);padding:var(--space-1h) 0 var(--space-1h) var(--space-3);border-left:2px solid var(--accent);color:var(--text-mid)}
.quiz-option + .item-pt{margin:calc(-1 * var(--space-1)) 0 var(--space-2h);padding:0 var(--space-3h) 0 var(--space-3)}
.chunk-line + .item-pt{font-family:var(--font-corpo);font-size:.82rem;margin:calc(-1 * var(--space-2)) 0 var(--space-3)}
.slide-dark .item-pt,.slide-open .item-pt{border-left-color:var(--d-accent);color:var(--d-text-mid)}

/* O APOIO EM PORTUGUES NA TELA DO DECK, e a diferenca dele para o `.item-pt`.
   O `.item-pt` traduz o exercicio e so abre quando a aluna confere -- no pre-class ela esta
   sozinha e a traducao antes da tentativa mataria a tentativa. Aqui ha uma professora na
   frente: o portugues nao substitui a instrucao, ele SITUA a aluna enquanto a professora
   conduz em ingles. Por isso e visivel desde a entrada na tela, e por isso e curto: uma
   linha por instrucao, menor e mais clara que o ingles acima dela, nunca um paragrafo. */
.slide-pt{display:block;font-family:var(--font-corpo);font-style:italic;font-weight:var(--peso-leve);font-size:.82rem;line-height:var(--lh-corpo);color:var(--text-mid);margin-top:var(--space-1h);max-width:60ch}
.slide-dark .slide-pt,.slide-open .slide-pt{color:var(--d-text-mid)}
/* O TAMANHO E O PESO SAO ABSOLUTOS, e por que isso importa (revisao de 03/09/2026).
   A regra acima dizia `font-size:.86em` e nao dizia peso nenhum -- as duas coisas herdadas
   do elemento que hospeda o apoio. Dentro de `.slide-question` (clamp ate 1.9rem, peso 600)
   o portugues saia com 26px e NEGRITO ao lado de um ingles de 30px: medido no navegador em
   03/09/2026, na aula 1 da Vanessa. O apoio competia de igual para igual com a frase que
   ele deveria apenas situar, e o olho ia nele primeiro -- exatamente o que o paragrafo
   acima diz que ele NAO pode fazer.
   `em` herda o corpo; `rem` nao. E o peso vai declarado, e nao deixado ao host. */
.slide-question .slide-pt,.q-item .slide-pt,.slide-subtitle .slide-pt,.slide-lead .slide-pt{
  font-size:.82rem;font-weight:var(--peso-leve);font-style:italic}

/* A PERGUNTA CENTRALIZADA TEM DE FICAR CENTRADA (revisao de 03/09/2026).
   `.slide-question` tem `max-width:38ch`. Num slide de abertura -- `.slide-open`, cujo
   `.slide-inner` e `text-align:center` -- o TEXTO se centraliza dentro da caixa, mas a
   CAIXA continua encostada a esquerda: 577px de pergunta num inner de 940px deixavam 363px
   de sobra so do lado direito. O texto parecia centralizado e nao estava. Medido na tela 1
   da aula 1 da Vanessa. Centrar a caixa e o que faltava; nas telas alinhadas a esquerda
   nada muda, porque a regra so vale onde o inner ja centraliza. */
.slide-open .slide-question{margin-left:auto;margin-right:auto}

/* E O APOIO EM PORTUGUES TAMBEM (revisao de 03/09/2026, a mesma tela de novo).
   A regra acima centrou a CAIXA da pergunta e parou ali. O `.slide-pt` tem `max-width:60ch`
   e e ele proprio um bloco: dentro do subtitulo da tela de abertura a caixa saia com 437px
   encostada na esquerda de um inner de 940 -- 503px de sobra de um lado so -- e o texto,
   centralizado DENTRO dela, parecia desalinhado do ingles logo acima. Medido no navegador
   na tela 1 da aula 1 da Vanessa, depois da correcao anterior: o mesmo defeito, na peca ao
   lado, porque o conserto foi escrito para UM seletor e nao para a causa (bloco com
   max-width dentro de um inner que centraliza).
   Vale so onde o inner ja centraliza -- nas telas alinhadas a esquerda nada muda. */
.slide-open .slide-pt{margin-left:auto;margin-right:auto}

/* LISTA DE ESCOLHAS CURTAS: CADA UMA E UM BLOCO, E ELAS VAO LADO A LADO.
   A `.qlist` e uma coluna, e para uma lista de PERGUNTAS isso e o certo: cada pergunta e uma
   linha de leitura. Mas a mesma classe recebe as ESCOLHAS de um "quais destas?" -- e sete
   escolhas de tres palavras empilhadas gastaram 522px de altura na tela 2 da aula 1 da
   Vanessa (medido no navegador: 990px de conteudo num deck de 900, com duas escolhas abaixo
   da dobra). Pedido da professora em 03/09/2026: "cada opcao um bloco sozinho, um ao lado do
   outro na horizontal".
   Quem poe a classe e o BUILDER, medindo os itens (`marca_qlist_de_escolhas`) -- nao o autor
   do conteudo, que teria de lembrar. Uma lista de perguntas nunca a recebe.
   O seletor e `.qlist.qlist-escolhas` (as duas classes) e nao `.qlist-escolhas`: a regra
   base `.qlist{flex-direction:column}` esta MAIS ABAIXO no arquivo, e com a mesma
   especificidade quem vem depois vence. Medido no navegador: com uma classe so, a lista
   recebia o cartao e continuava empilhada. */
.qlist.qlist-escolhas{flex-direction:row;flex-wrap:wrap;align-items:stretch;gap:var(--space-3)}
.qlist.qlist-escolhas .q-item{flex:0 1 auto;max-width:100%;padding:var(--space-2h) var(--space-3h);
  border-left:3px solid var(--accent);border-radius:0 8px 8px 0;background:rgba(0,48,128,.05);
  font-size:clamp(1.05rem,1.4vw,1.16rem)}
.slide-dark .qlist.qlist-escolhas .q-item,.slide-open .qlist.qlist-escolhas .q-item{background:rgba(255,255,255,.06)}"""),

 ("conferir-explica-mcheck",
  """function mCheck(btn,id){
  if(preConsulta(btn))return;
  var host=document.getElementById(id); if(!host)return;
  var rows=host.querySelectorAll('.match-row'),n=0,i,sel,ok;
  for(i=0;i<rows.length;i++){
    sel=rows[i].querySelector('select'); if(!sel)continue;
    ok=(sel.value===sel.getAttribute('data-ok'));
    rows[i].classList.toggle('correct',ok);
    rows[i].classList.toggle('wrong',!ok&&sel.value!=='');
    if(ok)n++;
  }
  var out=document.getElementById(id+'-out'); if(out)out.textContent=n+' / '+rows.length;
  var key=document.getElementById(id+'-key'); if(key&&n===rows.length)key.style.display='block';
}""",
  """/* CONFERIR TEM DE EXPLICAR, NAO SO PINTAR.
   Duas coisas faltavam nas tres checagens abaixo:

   1. A EXPLICACAO da atividade so abria com a pontuacao CHEIA (`n===rows.length`). Quem
      errou um item -- exatamente quem precisa dela -- via vermelho e mais nada, e a nota
      escrita para explicar o item dificil ficava fechada para sempre.
   2. O item errado nao dizia QUAL era a resposta. Marca vermelha sozinha ensina que errou,
      nao o que era. */
function fixRotulo(alvo,texto){
  if(!alvo)return;
  var el=alvo.querySelector('.row-fix');
  if(!el){ el=document.createElement('span'); el.className='row-fix'; alvo.appendChild(el); }
  el.textContent=texto?('\\u2192 '+texto):'';
  el.style.display=texto?'':'none';
}
/* A explicacao DAQUELE item (`.item-why`, emitida pelo builder a partir do campo `porque`).
   Abre ao conferir, para acerto e para erro: quem acertou confirma o porque, quem errou
   descobre. Sem ela, conferir devolve so uma cor. */
function porqueAbre(host){
  if(!host)return;
  var w=host.querySelectorAll('.item-why'),i;
  for(i=0;i<w.length;i++)w[i].classList.add('show');
}
function mCheck(btn,id){
  if(preConsulta(btn))return;
  var host=document.getElementById(id); if(!host)return;
  var rows=host.querySelectorAll('.match-row'),n=0,i,sel,ok,certa;
  for(i=0;i<rows.length;i++){
    sel=rows[i].querySelector('select'); if(!sel)continue;
    ok=(sel.value===sel.getAttribute('data-ok'));
    rows[i].classList.toggle('correct',ok);
    rows[i].classList.toggle('wrong',!ok&&sel.value!=='');
    certa=sel.querySelector('option[value="'+sel.getAttribute('data-ok')+'"]');
    fixRotulo(rows[i],(!ok&&certa)?certa.textContent:'');
    if(ok)n++;
  }
  var out=document.getElementById(id+'-out'); if(out)out.textContent=n+' / '+rows.length;
  var key=document.getElementById(id+'-key'); if(key)key.style.display='block';
  porqueAbre(host);
}"""),

 ("conferir-explica-czcheck",
  """  var f=host.querySelectorAll('.blank-input'),n=0,i,v,ok;
  for(i=0;i<f.length;i++){
    v=(f[i].value||'').trim().toLowerCase().replace(/[.,]/g,'');
    ok=(v===(f[i].getAttribute('data-ok')||'').toLowerCase());
    f[i].classList.toggle('correct',ok);
    f[i].classList.toggle('wrong',!ok&&v!=='');
    if(ok)n++;
  }
  var out=document.getElementById(id+'-out'); if(out)out.textContent=n+' / '+f.length;
  var key=document.getElementById(id+'-key'); if(key&&n===f.length)key.style.display='block';""",
  """  var f=host.querySelectorAll('.blank-input'),n=0,i,v,ok,dica;
  for(i=0;i<f.length;i++){
    v=(f[i].value||'').trim().toLowerCase().replace(/[.,]/g,'');
    ok=(v===(f[i].getAttribute('data-ok')||'').toLowerCase());
    f[i].classList.toggle('correct',ok);
    f[i].classList.toggle('wrong',!ok&&v!=='');
    dica=f[i].nextSibling&&f[i].nextSibling.className==='row-fix'?f[i].nextSibling:null;
    if(!dica){ dica=document.createElement('span'); dica.className='row-fix';
               f[i].parentNode.insertBefore(dica,f[i].nextSibling); }
    dica.textContent=ok?'':('\\u2192 '+f[i].getAttribute('data-ok'));
    dica.style.display=ok?'none':'';
    if(ok)n++;
  }
  var out=document.getElementById(id+'-out'); if(out)out.textContent=n+' / '+f.length;
  var key=document.getElementById(id+'-key'); if(key)key.style.display='block';
  porqueAbre(host);"""),

 ("conferir-explica-ppcheck",
  """  var rows=host.querySelectorAll('.pair-row'),n=0,i,sel,ok;
  for(i=0;i<rows.length;i++){
    sel=rows[i].querySelector('.pair-opt.sel'); if(!sel)continue;
    ok=(sel.getAttribute('data-v')===rows[i].getAttribute('data-ok'));
    rows[i].classList.toggle('correct',ok);
    rows[i].classList.toggle('wrong',!ok);
    if(ok)n++;
  }
  var out=document.getElementById(id+'-out'); if(out)out.textContent=n+' / '+rows.length;
  var key=document.getElementById(id+'-key'); if(key&&n===rows.length)key.style.display='block';""",
  """  var rows=host.querySelectorAll('.pair-row'),n=0,i,sel,ok,certa;
  for(i=0;i<rows.length;i++){
    sel=rows[i].querySelector('.pair-opt.sel'); if(!sel)continue;
    ok=(sel.getAttribute('data-v')===rows[i].getAttribute('data-ok'));
    rows[i].classList.toggle('correct',ok);
    rows[i].classList.toggle('wrong',!ok);
    certa=rows[i].querySelector('.pair-opt[data-v="'+rows[i].getAttribute('data-ok')+'"]');
    fixRotulo(rows[i],(!ok&&certa)?certa.textContent:'');
    if(ok)n++;
  }
  var out=document.getElementById(id+'-out'); if(out)out.textContent=n+' / '+rows.length;
  var key=document.getElementById(id+'-key'); if(key)key.style.display='block';
  porqueAbre(host);"""),

 ("conferir-explica-selcheck",
  """  var out=document.getElementById(id+'-out'); if(out)out.textContent=acertos+' / '+alvo;
  var r=host.parentNode.querySelector('.rationale'); if(r)r.classList.add('show');
}""",
  """  var out=document.getElementById(id+'-out'); if(out)out.textContent=acertos+' / '+alvo;
  var r=host.parentNode.querySelector('.rationale'); if(r)r.classList.add('show');
  porqueAbre(host.parentNode);
}"""),

 # ---- REFAZER UM EXERCICIO (revisao da professora, 03/09/2026 -- aula 1 da Vanessa)
 #
 # Depois de conferir, o botao continuava escrito "Check", e um segundo clique so repintava
 # o mesmo resultado. Para tentar de novo, a aluna tinha de usar o "Reset my answers" -- que
 # limpa a AULA INTEIRA. Nao havia caminho para refazer UM exercicio, e o botao que ela
 # acabara de usar era justamente o que parecia oferece-lo.
 #
 #     "Ao clicar em check/checar e o exercicio mostrar as respostas, o botao pode mudar
 #      para Refazer ou Limpar."
 #
 # A copia sai na PRIMEIRA conferida, antes de qualquer marca: assim nao depende da ordem do
 # boot e vale igual no pre-class e no deck -- `mCheck` e `selCheck` rodam nos dois.
 ("refazer-o-exercicio/helpers",
  """function porqueAbre(host){
  if(!host)return;
  var w=host.querySelectorAll('.item-why'),i;
  for(i=0;i<w.length;i++)w[i].classList.add('show');
}""",
  """function porqueAbre(host){
  if(!host)return;
  var w=host.querySelectorAll('.item-why'),i;
  for(i=0;i<w.length;i++)w[i].classList.add('show');
}
/* ---------------- REFAZER: o botao que confere vira o botao que limpa ----------------
   O rotulo de ida sai do `data-redo` que o EMISSOR escreve (so ele sabe se o material e
   bilingue); o de volta sai do proprio botao, guardado em `data-check` na primeira vez. */
var _exSnap={};
function exGuarda(id,host){
  if(!id||!host||_exSnap[id]!==undefined)return;
  /* A COPIA SAI LIMPA, e nao como a tela estava. Ela e tirada na primeira conferida --
     quando as escolhas da aluna JA estao marcadas --, entao guardar `innerHTML` cru fazia
     o "Refazer" devolver o exercicio com as mesmas alternativas ainda selecionadas: com
     cara de respondido, sem estar conferido. Refazer e comecar de novo.
     Nao ha o que limpar em <select> nem em <input>: a escolha do usuario vive na
     PROPRIEDADE, e `innerHTML` serializa o atributo -- eles ja voltam vazios. */
  var d=document.createElement('div'); d.innerHTML=host.innerHTML;
  var el=d.querySelectorAll('.sel,.correct,.wrong'),i;
  for(i=0;i<el.length;i++)el[i].classList.remove('sel','correct','wrong');
  _exSnap[id]=d.innerHTML;
}
function exFeito(btn,id){
  if(!btn||_exSnap[id]===undefined)return;
  if(!btn.getAttribute('data-check'))btn.setAttribute('data-check',btn.textContent);
  btn.setAttribute('data-estado','feito');
  btn.textContent=btn.getAttribute('data-redo')||'Redo';
}
function exRefaz(btn,id){
  if(!btn||btn.getAttribute('data-estado')!=='feito')return false;
  var host=document.getElementById(id),i,el;
  if(host&&_exSnap[id]!==undefined)host.innerHTML=_exSnap[id];
  el=document.getElementById(id+'-out'); if(el)el.textContent='';
  el=document.getElementById(id+'-key'); if(el)el.style.display='none';
  /* A explicacao da atividade e a traducao sao IRMAS do host, dentro do quiz-item:
     restaurar o host nao as fecha, e elas ficariam abertas sobre um exercicio em branco. */
  if(host&&host.parentNode){
    el=host.parentNode.querySelectorAll('.rationale.show,.item-why.show');
    for(i=0;i<el.length;i++)el[i].classList.remove('show');
  }
  btn.setAttribute('data-estado','');
  btn.textContent=btn.getAttribute('data-check')||'Check';
  /* O REGISTRO ACOMPANHA A TELA, ou a limpeza dura ate o F5: `preInit` devolveria o valor
     digitado (pelos campos) e `preMecRestaura` as marcas (pelas classes), e a aluna veria
     de volta exatamente o que acabou de refazer. Vale so no pre-class -- no deck nao ha
     bloco `pc*` nem persistencia. */
  var bl=btn.closest?btn.closest('[id^="pc"]'):null;
  if(bl&&typeof preMecSalva==='function'){
    var mortas=[];
    if(host){ el=host.querySelectorAll('[data-k]');
              for(i=0;i<el.length;i++)mortas.push(el[i].getAttribute('data-k')); }
    if(mortas.length&&typeof drop==='function')drop(mortas);
    preMecSalva(bl);
    /* Os campos restaurados sao NOVOS: sem tirar a marca de ligado, `preInit` os pularia e
       eles ficariam sem ouvinte -- digitar deixaria de gravar, sem erro nenhum. */
    if(host){ el=host.querySelectorAll('[data-lig]');
              for(i=0;i<el.length;i++)el[i].removeAttribute('data-lig'); }
    if(typeof preKeys==='function'){ preKeys(); preInit(); preModo(); }
  }
  return true;
}"""),

 ("refazer-o-exercicio/mcheck",
  """function mCheck(btn,id){
  if(preConsulta(btn))return;
  var host=document.getElementById(id); if(!host)return;
  var rows=host.querySelectorAll('.match-row'),n=0,i,sel,ok,certa;""",
  """function mCheck(btn,id){
  if(preConsulta(btn))return;
  if(exRefaz(btn,id))return;
  var host=document.getElementById(id); if(!host)return;
  exGuarda(id,host);
  var rows=host.querySelectorAll('.match-row'),n=0,i,sel,ok,certa;"""),

 ("refazer-o-exercicio/ppcheck",
  """function ppCheck(btn,id){
  if(preConsulta(btn))return;
  var host=document.getElementById(id); if(!host)return;""",
  """function ppCheck(btn,id){
  if(preConsulta(btn))return;
  if(exRefaz(btn,id))return;
  var host=document.getElementById(id); if(!host)return;
  exGuarda(id,host);"""),

 ("refazer-o-exercicio/czcheck",
  """function czCheck(btn,id){
  if(preConsulta(btn))return;
  var host=document.getElementById(id); if(!host)return;""",
  """function czCheck(btn,id){
  if(preConsulta(btn))return;
  if(exRefaz(btn,id))return;
  var host=document.getElementById(id); if(!host)return;
  exGuarda(id,host);"""),

 ("refazer-o-exercicio/selcheck",
  """function selCheck(btn,id){
  if(preConsulta(btn))return;
  var host=document.getElementById(id); if(!host)return;""",
  """function selCheck(btn,id){
  if(preConsulta(btn))return;
  if(exRefaz(btn,id))return;
  var host=document.getElementById(id); if(!host)return;
  exGuarda(id,host);"""),

 # O rabo de cada uma: o botao so vira "Refazer" DEPOIS de conferir de verdade. Cada ancora
 # leva a linha SEGUINTE junto, porque o fim das tres primeiras e identico -- sem isso a
 # ancora casaria 3x e a extracao pararia, como manda o contrato do CORRECOES.
 ("refazer-o-exercicio/mcheck-fim",
  """  porqueAbre(host);
}
/* cloze com gabarito por campo */""",
  """  porqueAbre(host);
  exFeito(btn,id);
}
/* cloze com gabarito por campo */"""),

 ("refazer-o-exercicio/czcheck-fim",
  """  var out=document.getElementById(id+'-out'); if(out)out.textContent=n+' / '+f.length;
  var key=document.getElementById(id+'-key'); if(key)key.style.display='block';
  porqueAbre(host);""",
  """  var out=document.getElementById(id+'-out'); if(out)out.textContent=n+' / '+f.length;
  var key=document.getElementById(id+'-key'); if(key)key.style.display='block';
  porqueAbre(host);
  exFeito(btn,id);"""),

 ("refazer-o-exercicio/ppcheck-fim",
  """  porqueAbre(host);
}

/* ---------------- guarda de papel no pre-class ----------------""",
  """  porqueAbre(host);
  exFeito(btn,id);
}

/* ---------------- guarda de papel no pre-class ----------------"""),

 ("refazer-o-exercicio/selcheck-fim",
  """  porqueAbre(host.parentNode);
}""",
  """  porqueAbre(host.parentNode);
  exFeito(btn,id);
}"""),

 ("razao-abre-com-qualquer-escolha",
  """  if(ok){var r=box.parentNode.querySelector('.rationale'); if(r)r.classList.add('show');}""",
  """  /* A razao abre com QUALQUER escolha: reserva-la ao acerto e dar a explicacao a quem
     ja nao precisava dela. */
  var r=box.parentNode.querySelector('.rationale'); if(r)r.classList.add('show');"""),

 # ---- O DOCUMENTO NA TELA ESCURA (revisao de 03/09/2026)
 #
 # `.doc-brief` nasceu com `background:rgba(255,255,255,.62)` e sem par escuro, porque no
 # artefato ele so aparece em tela clara. Posto numa `.slide-dark` -- a tela 8 da aula 1 da
 # Vanessa, onde a reserva agora abre como apoio -- o fundo vira um cinza claro e o texto
 # continua sendo o texto CLARO do slide escuro: claro sobre claro.
 #
 # E o GATE 52 nao veria: ele pula `display:none`, e este bloco NASCE fechado, para o
 # professor abrir so se a aluna precisar. Por isso a correcao vem em par com a mudanca no
 # gate, que passa a abrir os blocos recolhiveis antes de medir. Peca sem par escuro nao e
 # peca de tela clara: e peca que ainda nao foi usada no escuro.
 ("doc-brief-no-escuro",
  """.doc-para:last-child{margin-bottom:0}""",
  """.doc-para:last-child{margin-bottom:0}
.slide-dark .doc-brief,.slide-open .doc-brief{background:rgba(255,255,255,.06);
  border-color:var(--d-border);border-left-color:var(--d-accent)}
.slide-dark .doc-tit,.slide-open .doc-tit{color:var(--d-accent)}
.slide-dark .doc-fonte,.slide-open .doc-fonte{color:var(--d-text-mid);border-bottom-color:var(--d-border)}
.slide-dark .doc-para,.slide-open .doc-para{color:var(--d-text)}"""),

 ("uma-aula-por-vez",
  """  _preAtual=CICLO.primeira;""",
  """  _preAtual=CICLO.primeira;
  /* Uma aula por vez, no pre-class e no post-class. Os blocos das outras aulas nascem no
     HTML e ninguem os fechava: a aba abria com as quatro empilhadas, e a barra de selecao
     so passava a valer depois do primeiro clique. Fechar aqui, e nao no fragmento, e o que
     impede a proxima aula de nascer aberta de novo. */
  preSel(CICLO.primeira); postSel(CICLO.primeira);"""),
]


def deriva_professor():
    rel = {}
    corpo = corpo_do_artefato()
    for velho, novo in NOMES:
        rel[f"swap/{velho}"] = corpo.count(velho)
        corpo = corpo.replace(velho, novo)

    # ---- O DIALOGO DEIXA DE SER O DA AULA 19
    #
    # `playTalk` e `tsBuild` leem `TALK_19` direto -- o dialogo da unica aula de Listening do
    # artefato. Copiado assim, QUALQUER aula de Listening de qualquer aluno tocaria a
    # conversa do congresso do Marcos. E o mesmo tipo de defeito do `closeBuild(19,...)`:
    # numero que descreve o MODELO cravado no codigo do MOLDE.
    #
    # A divergencia e por LIMITACAO DO ARTEFATO -- ele tem UMA aula com dialogo, e uma pagina
    # com uma aula nunca precisou perguntar "de qual aula?". O molde tem N.
    #
    # A aula sai do proprio botao: ele vive dentro de uma `.slide[data-lesson]`. Nada de
    # variavel global de estado -- o mesmo botao responde certo em qualquer aula.
    corpo = corpo.replace(
        "var TALK_19=[",
        "/* Dialogos por aula. O builder troca este objeto pelo do material; a chave e o\n"
        "   numero da aula, e quem escolhe e o proprio botao, pelo data-lesson da tela. */\n"
        "function talkDe(alvo){\n"
        "  var s=alvo&&alvo.closest?alvo.closest('.slide'):null;\n"
        "  var n=s?s.getAttribute('data-lesson'):null;\n"
        "  if(n&&TALKS[n])return TALKS[n];\n"
        "  for(var k in TALKS)return TALKS[k];   /* material de uma aula so */\n"
        "  return [];\n"
        "}\n"
        "var TALKS={19:[", 1)
    # fecha o objeto: o array do artefato termina em `];`
    i = corpo.index("var TALKS={19:[")
    j = corpo.index("\n];", i)
    corpo = corpo[:j] + "\n]};" + corpo[j + len("\n];"):]
    # os tres usos passam a ler o dialogo da aula do botao
    corpo = corpo.replace(
        "var vs=pickCast(),fb=enVoices()[0]||null,a=(from==null?0:from),"
        "b=(to==null?TALK_19.length-1:to),i;",
        "var TK=talkDe(alvo);\n"
        "  var vs=pickCast(),fb=enVoices()[0]||null,a=(from==null?0:from),"
        "b=(to==null?TK.length-1:to),i;", 1)
    corpo = corpo.replace("})(TALK_19[i]);", "})(TK[i]);", 1)
    corpo = corpo.replace(
        "  for(i=0;i<TALK_19.length;i++){\n    t=TALK_19[i];",
        "  var TK=talkDe(host);\n  for(i=0;i<TK.length;i++){\n    t=TK[i];", 1)
    rel["js/dialogo-por-aula"] = 1

    # ---- O TRANSCRIPT DEIXA DE SER O DA AULA 19
    # `tsBuild` escreve em `#ts19` -- a caixa da unica aula de Listening do artefato. Num
    # material com outra numeracao ela nao existe, o `if(!host)return` engole, e a aula
    # entrega um botao "Show transcript" que nao mostra nada. Mesma familia do closeBuild.
    corpo = corpo.replace(
        "function tsBuild(){\n  var host=document.getElementById('ts19'); if(!host)return;",
        "function tsBuild(){\n"
        "  /* todas as caixas de transcript do documento, uma por aula */\n"
        "  var caixas=document.querySelectorAll('.transcript-box[id^=\"ts\"]'),ci;\n"
        "  for(ci=0;ci<caixas.length;ci++)tsUma(caixas[ci]);\n"
        "}\n"
        "function tsUma(host){\n  if(!host)return;", 1)
    rel["js/transcript-por-aula"] = 1

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

    # ---- O AUDIO DEIXA DE SER SINTESE DO NAVEGADOR (AUT-004)
    # Ver o cabecalho de scripts/consultivo/_motor_audio.py: a troca mora la porque e
    # grande, e o que fica aqui e a APLICACAO dela -- cada substituicao tem de casar
    # exatamente uma vez, senao a derivacao para.
    for rotulo, velho, novo in _motor_audio.TROCAS:
        if corpo.count(velho) != 1:
            raise SystemExit(
                f"troca do motor de audio ({rotulo}): o trecho casou "
                f"{corpo.count(velho)} vez(es), e tem de casar exatamente 1. O artefato "
                f"mudou -- atualize scripts/consultivo/_motor_audio.py em vez de afrouxar "
                f"a busca.")
        corpo = corpo.replace(velho, novo, 1)
        rel["audio/" + rotulo] = 1
    for nome in _motor_audio.FORA:
        corpo = remove_funcao(corpo, nome, rel)
    # A guarda olha CODIGO, nunca prosa: os comentarios que explicam a troca CITAM a
    # tecnologia proibida, e um `in corpo` cru reprovaria a propria explicacao. E o mesmo
    # criterio do GATE 36 -- "a mencao nao e a expressao" (P2 §15).
    codigo = re.sub(r"/\*.*?\*/|//[^\n]*", " ", corpo, flags=re.S)
    sobrou = [t for t in ("speechSynthesis", "SpeechSynthesisUtterance") if t in codigo]
    if sobrou:
        raise SystemExit(f"o motor de audio ainda usa {sobrou} depois da troca. O Anexo P-A "
                         f"proibe no build oficial -- a troca esta incompleta.")

    # ---- CORRECOES DA REVISAO DE 28/08/2026
    #
    # O shell NAO se edita a mao: ele e derivado do artefato, e o gate de extracao compara
    # o disco com o que sairia daqui hoje. Correcao que nasce no arquivo derivado dura ate
    # a proxima extracao e some sem aviso -- por isso ela mora AQUI, como troca declarada,
    # com ancora que tem de casar exatamente uma vez.
    for rotulo, velho, novo in CORRECOES:
        if corpo.count(velho) != 1:
            raise SystemExit(
                f"correcao {rotulo!r}: a ancora casou {corpo.count(velho)}x no artefato "
                f"(o esperado e 1). O artefato mudou embaixo da correcao -- releia o trecho "
                f"antes de reescrever a ancora.")
        corpo = corpo.replace(velho, novo, 1)
        rel[f"correcao/{rotulo}"] = 1

    # A mesma linha "No in-class", ja RENDERIZADA no pre-aula do artefato. A troca acima
    # tira quem a EMITE; estas sao as que ja estavam escritas no HTML. Sao muitas e cada
    # uma com texto proprio, entao a ancora nao pode ser literal -- mas a contagem esperada
    # e declarada, e uma divergencia para a extracao em vez de limpar o que nao devia.
    ESPERADO_NO_IN_CLASS = 9
    rx_ak = re.compile(r'<div class="ak-linha"><b>No in-class</b>.*?</div>(?=</div>|<div class="ak-linha")',
                       re.S)
    achadas = len(rx_ak.findall(corpo))
    if achadas != ESPERADO_NO_IN_CLASS:
        raise SystemExit(
            f"'No in-class' renderizado: achei {achadas} no artefato e o declarado e "
            f"{ESPERADO_NO_IN_CLASS}. O artefato mudou -- confira antes de ajustar o numero.")
    corpo = rx_ak.sub("", corpo)
    rel["correcao/no-in-class-renderizado"] = achadas

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
    # `tgLinha` e `tgCabecaHTML` sairam desta lista em 02/09/2026: a correcao
    # `guia-sem-cabecalho/funcoes` ja as remove do artefato, entao pedi-las aqui era pedir a
    # remocao de algo que nao existe mais -- e o relatorio passava a dizer "nao achou" para
    # sempre, que e como um nome errado nesta lista se esconde.
    "tgAberto", "tgClose", "tgToggle", "tgURL", "tgAbrir",
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
  /* A COPIA DO PRE-CLASS, E POR QUE ELA FALTAVA AQUI (revisao de 03/09/2026).
     `preResetGo` restaura `_preSnap[n]` -- e so restaura `if(_preSnap[n]!==undefined)`.
     Este boot e escrito a mao (nao e o do professor filtrado), e nunca chamou `preSnap()`:
     no arquivo DA ALUNA o mapa ficava vazio, a condicao era falsa e o "Reset my answers"
     saia sem tocar na tela. Ele apagava o armazenamento -- entao a limpeza era real e
     invisivel -- e as alternativas conferidas continuavam verdes. Clicar em Check de novo
     "resolvia", porque o `classList.toggle('correct',sel&&ok)` recalculava sem `.sel`.
     Medido no navegador em 03/09/2026, no arquivo publicado da Vanessa.
     ANTES de `preInit`, como no boot do professor: tirada depois, a copia ja conteria as
     respostas restauradas, e o Reset devolveria exatamente o que devia apagar. */
  preSnap();
  preInit();
  /* O PRE-CLASS DELA NASCE EM MODO DE RESPOSTA. O atributo `data-consulta="1"` vem CRAVADO
     no HTML da aba -- e o modo de leitura do professor, e ele desliga o ponteiro das opcoes
     (`pointer-events:none`). No build do professor quem o desfaz e o setView do boot; aqui
     nao havia ninguem, e a aluna abria o material dela sem conseguir clicar em exercicio
     nenhum. Medido no navegador em 28/08/2026, no arquivo publicado. */
  preModo();
  /* Uma aula por vez, no pre-class e no post-class -- como no build do professor. */
  preSel(CICLO.primeira); postSel(CICLO.primeira);
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
    # O `pwRestore` do boot do aluno E O DO MATERIAL, nao o do modelo.
    #
    # O builder reescreve a lista de campos do post-class DENTRO do boot do professor, a
    # partir das aulas do config. Este boot, escrito aqui, e estatico -- e trazia os ids
    # `pw19-*`/`pw20-*` do artefato do Marcos. Substituindo o boot depois da reescrita, os
    # numeros do modelo VOLTAVAM, e so no arquivo da aluna: o que ela tinha escrito no
    # post-class nunca era restaurado, sem erro nenhum no console.
    boot_prof = js[i:j]
    m_pw = re.search(r"pwRestore\(\[.*?\]\);", boot_prof, re.S)
    boot_aluno = BOOT_ALUNO
    if m_pw:
        boot_aluno = re.sub(r"pwRestore\(\[.*?\]\);", lambda _: m_pw.group(0), boot_aluno,
                            count=1, flags=re.S)
    js = js[:i] + boot_aluno + js[j:]
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
