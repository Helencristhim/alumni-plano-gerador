#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O BUILDER EMITE O EXERCICIO. Quem escreve a aula declara, nao digita HTML.

POR QUE ISTO EXISTE
-------------------
A queixa que abriu este trabalho nao era sobre o molde: era sobre o GERADOR repetir erro que
a auditora tinha ACABADO de corrigir no documento normativo. Gate nao resolve isso -- ele
barra no fim, quando o defeito ja nasceu, e a correcao volta a se perder no proximo prompt.

O imersivo passou por isso e a saida foi outra: o autor declara `{"kind": "...", ...}` e o
BUILDER emite o markup. Regra de forma vira impossivel de esquecer porque quem escreve a
aula nunca toca nela.

    o que se declara pode estar errado.
    o que nao se escreve nao pode.

O QUE ISTO TORNA IMPOSSIVEL (nao "detectavel" -- impossivel)
--------------------------------------------------------------
Medido numa unica seccao do molde: o id `m1` aparece QUATRO vezes -- no `match-grid`, no
argumento do `mCheck`, no `score-out` e na nota. Qualquer divergencia entre eles quebra o
exercicio EM SILENCIO: a checagem nao acha o grid, ou o resultado nao tem onde aparecer, ou
a nota nunca revela. E a familia "handler escreve num id que nao existe", que nenhum gate
estatico ve.

Aqui o id e gerado UMA vez e distribuido. Nao ha como divergir.

Junto vao embora:
  - item sem gabarito         -> `ok` e obrigatorio, e o assert fala antes do build sair
  - checagem esquecida        -> emitida sempre, junto do exercicio
  - gabarito visivel          -> a nota nasce `display:none`, e nao ha caminho para nascer aberta
  - letra de opcao trocada    -> o autor escreve o TEXTO da resposta certa; a letra e derivada
  - lista de opcoes divergente-> declarada uma vez, repetida por codigo nas N linhas
                                 (no molde: 7 opcoes x 6 linhas, digitadas a mao)

O QUE ISTO **NAO** FAZ
-----------------------
Conteudo. Qual e a pergunta, se a distincao vale a pena, se o exemplo e natural -- nada
disso muda de dono. O builder cuida da FORMA; o julgamento continua de quem escreve.

FIDELIDADE E BYTE A BYTE, E ISSO NAO E CAPRICHO
------------------------------------------------
Cada `kind` daqui emite exatamente o markup que ja existe nos fragmentos do molde -- mesma
indentacao, mesmas entidades, mesma ordem de atributo. E o que permite provar a equivalencia
declarando um exercicio existente e comparando os bytes (`--prova`), em vez de confiar que
"parece igual". Sem isso, migrar seria reescrever, e reescrever no porte foi exatamente o
que produziu o inventario falso que o GATE 20 teve de consertar.
"""
import html as _html
import re

LETRAS = "ABCDEFGHIJ"


def esc(t):
    """Texto do autor -> HTML. As aspas e o travessao viram entidade, como no molde.

    O autor escreve `"assim"` e `--`; o molde usa `&ldquo;`/`&rdquo;` e `&mdash;`. Deixar
    isso para quem escreve a aula e pedir para errar em metade dos itens."""
    t = _html.escape(t, quote=False)
    t = re.sub(r'"([^"]*)"', lambda m: "&ldquo;" + m.group(1) + "&rdquo;", t)
    t = t.replace("--", "&mdash;").replace("...", "&hellip;")
    # O apostrofo do ingles vira `&rsquo;`, como no molde. Nao e capricho tipografico: e o
    # que faz a declaracao voltar byte a byte, e byte a byte e o que prova que migrar nao
    # reescreve.
    t = t.replace("'", "&rsquo;").replace("\u2019", "&rsquo;")
    t = t.replace("\u00b7", "&middot;").replace("\u2013", "&ndash;")
    # `**assim**` e `*assim*` viram <strong>/<em>. O autor nao escreve tag: escrever tag num
    # campo de texto e o caminho mais curto para um `<` solto quebrar a tela.
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", t)
    return t


def crua(t):
    """Campo de PROSA que sai CRU (o autor escreve `<br>`, `<em>`, entidade) -- mas a
    marcacao curta continua valendo nele.

    O `esc()` converte `**assim**` em <strong>; estes campos nao passam por ele, e foi por
    isso que `**Ferraz:**` chegou LITERAL a tela do pre-class da aula 9 do Luiz. Quem
    escreve a aula nao tem como saber, campo a campo, qual passa pelo escape e qual nao
    passa: a marcacao vale em todos, e a diferenca entre eles e so o HTML permitido."""
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", t)
    return t


def _ident(bloco, i):
    """O id do exercicio. Vem do proprio bloco quando declarado; senao, e derivado."""
    return bloco.get("id") or f"ex{i}"


# ---------------------------------------------------------------------------
def r_classificar(b, ident):
    """Cada item recebe UMA classificacao, de uma lista fixa de opcoes.

    O autor escreve o TEXTO da opcao certa; a letra (`data-ok="B"`) e derivada. Trocar
    letra por engano era um dos jeitos silenciosos de o exercicio nascer errado -- o
    `data-ok` continuava valido, so apontava para outra coisa."""
    ops = b["opcoes"]
    idx = {o: LETRAS[i] for i, o in enumerate(ops)}
    linhas = []
    for it in b["itens"]:
        if it["ok"] not in idx:
            raise SystemExit(f'{ident}: a resposta {it["ok"]!r} nao esta entre as opcoes '
                             f'{ops}. O autor escreve o TEXTO da opcao certa.')
        alts = ''.join(f'<option value="{LETRAS[i]}">{esc(o)}</option>'
                       for i, o in enumerate(ops))
        linhas.append(
            f'      <div class="match-row"><span class="match-word">{esc(it["t"])}</span>'
            f'<select data-ok="{idx[it["ok"]]}">'
            f'<option value="" selected="selected">&mdash;</option>{alts}</select></div>')
    return (f'    <div class="match-grid" id="{ident}">\n' + "\n".join(linhas) + "\n    </div>\n"
            f'    <button class="verify-all-btn ghost" onclick="mCheck(this,\'{ident}\')">'
            f'Check</button>\n'
            f'    <div class="score-out" id="{ident}-out"></div>')


def r_completar(b, ident):
    """Cada enunciado tem os SEUS finais -- nao ha lista comum.

    Parece `classificar` na tela (mesmo `match-grid`, mesmo `mCheck`) e e outro exercicio.
    Em `classificar` a lista de opcoes e a MESMA em todas as linhas: e isso que faz ser
    classificacao, e e o que permite ao autor escrever a lista uma vez. Aqui cada frase
    cobra um final proprio, e reaproveitar a lista da primeira linha -- que era o que a
    leitura fazia -- trocava as respostas das outras em silencio: o `data-ok` continuava
    uma letra valida, so apontando para outro texto."""
    linhas = []
    for it in b["itens"]:
        alts = it["alts"]
        if it["ok"] not in alts:
            raise SystemExit(f'{ident}: a resposta {it["ok"]!r} nao esta entre os finais de '
                             f'{it["t"]!r}. O autor escreve o TEXTO do final certo.')
        ops = ''.join(f'<option value="{LETRAS[i]}">{esc(o)}</option>'
                      for i, o in enumerate(alts))
        linhas.append(
            f'      <div class="match-row"><span class="match-word">{esc(it["t"])}</span>'
            f'<select data-ok="{LETRAS[alts.index(it["ok"])]}">'
            f'<option value="" selected="selected">&mdash;</option>{ops}</select></div>')
    return (f'    <div class="match-grid" id="{ident}">\n' + "\n".join(linhas) + "\n    </div>\n"
            f'    <button class="verify-all-btn ghost" onclick="mCheck(this,\'{ident}\')">'
            f'Check</button>\n'
            f'    <div class="score-out" id="{ident}-out"></div>')


def r_escolha(b, ident):
    """Marque as que sao verdadeiras. `ok: true` no item; o resto e 0."""
    linhas = [f'        <div class="quiz-option" data-ok="{1 if it.get("ok") else 0}" '
              f'onclick="tog(this)"><span>{esc(it["t"])}</span></div>'
              for it in b["itens"]]
    # O `rationale` vive DENTRO do quiz-item, depois das opcoes. E a explicacao da
    # atividade -- diferente da `nota`, que fecha a seccao. Nasce escondido pelo CSS
    # (`.rationale{display:none}`), e por isso nao carrega style aqui.
    rat = (f'\n      <div class="rationale">{esc(b["rationale"])}</div>'
           if b.get("rationale") else "")
    # O PROMPT pode viver DENTRO do quiz-item, colado nas opcoes, em vez de na abertura.
    # E outra coisa: a instrucao da seccao ("Mark the two that...") descreve a TAREFA; esta
    # e a pergunta do item ("What is the speaker doing?"), e vem depois do audio que ela
    # cobra. Emitir na abertura mudaria a ordem na tela.
    pr = (f'      <p class="task-instr">{esc(b["prompt"])}</p>\n' if b.get("prompt") else "")
    return (f'    <div class="quiz-item">\n' + pr + f'      <div class="quiz-options" id="{ident}">\n'
            + "\n".join(linhas) + f"\n      </div>{rat}\n    </div>\n"
            f'    <button class="verify-all-btn ghost" onclick="selCheck(this,\'{ident}\')">'
            f'Check</button>\n'
            f'    <div class="score-out" id="{ident}-out"></div>')


def r_par(b, ident):
    """Duas leituras possiveis; qual delas e a que vale aqui."""
    linhas = []
    for it in b["itens"]:
        alts = it["alts"]
        if len(alts) != 2:
            raise SystemExit(f"{ident}: o par tem de ter exatamente duas alternativas, "
                             f"e {it['t']!r} tem {len(alts)}.")
        if it["ok"] not in alts:
            raise SystemExit(f'{ident}: a resposta de {it["t"]!r} nao esta entre as suas '
                             f'alternativas.')
        letra = "ab"[alts.index(it["ok"])]
        bots = "".join(
            f'\n        <button class="pair-opt" data-v="{"ab"[i]}" onclick="ppPick(this)">'
            f'{esc(a)}</button>' for i, a in enumerate(alts))
        linhas.append(f'      <div class="pair-row" data-ok="{letra}">\n'
                      f'        <span class="pair-word">{esc(it["t"])}</span>{bots}\n'
                      f'      </div>')
    return (f'    <div class="pair-grid" id="{ident}">\n' + "\n".join(linhas) + "\n    </div>\n"
            f'    <button class="verify-all-btn ghost" onclick="ppCheck(this,\'{ident}\')">'
            f'Check</button>\n'
            f'    <div class="score-out" id="{ident}-out"></div>')


def r_frases(b, ident):
    """Lista de frases-modelo. Sem gabarito: e insumo, nao exercicio."""
    return "\n".join(f'    <div class="phrase-row"><span class="phrase-en">{esc(f)}</span>'
                     f'</div>' for f in b["itens"])


def r_lacuna(b, ident, vocab=None):
    """Completar a frase. A lacuna vai ENTRE CHAVES, no meio do texto:

        "{The syllabus says} twenty hours, and the plan has eighteen."

    O autor escreve a frase inteira e marca o pedaco que sai. O `<input>`, o `data-ok`, o
    `style` e o `placeholder` sao do render -- sao quatro atributos identicos em cinquenta
    lacunas do molde, digitados um a um.

    O BANCO e obrigatorio no gap-fill de VOCABULARIO (REGRA 2.4 do imersivo, aprendida ali
    com uma aula que cobrava cinco palavras que ninguem tinha ensinado): sem as candidatas
    na tela, "complete a frase" nao e recuperacao lexical -- ou a palavra exata vem a
    cabeca, ou a aluna trava sem saida.

    E PROIBIDO no de GRAMATICA, pela mesma regra e pela razao oposta: ali a lacuna cobra a
    FORMA do verbo ("If it ___ taken that night"), e o banco entregaria a resposta.

    O criterio nao e um flag que alguem marca -- seria a mesma coisa que confiar na memoria.
    E derivado: se TODA resposta esta no vocabulario que a propria regiao ensina, o
    exercicio e de vocabulario e o banco e cobrado. `vocab` chega de `blocos()`, que ve as
    seccoes irmas.

    A trava chegou aqui do imersivo SEM essa distincao e recusava os dois casos igualmente:
    o gap-fill de gramatica da aula 11 do Luiz -- que existe justamente para medir precisao
    longe da pressao de conversa -- nao podia ser construido."""
    # A comparacao tolera FLEXAO: o vocabulario e apresentado na forma de citacao ("to
    # claim", "to leave something out") e a lacuna cobra a forma usada ("claims", "leave
    # out"). Comparar literal diria que sao palavras diferentes e classificaria um
    # gap-fill de vocabulario como de gramatica.
    def base(t):
        # `to be assigned to` e `assigned to` sao a mesma entrada: a forma de citacao
        # carrega o auxiliar e a lacuna nao. Sem tirar o `be`, o gap-fill de vocabulario
        # passava por gramatica e o banco obrigatorio era recusado.
        t = re.sub(r"^(to\s+be|to|an?|the)\s+", "", t.strip().lower())
        t = re.sub(r"\b(something|someone)\b", " ", t)
        return re.sub(r"\s+", " ", t).strip()

    def mesma(a, c):
        """Mesma expressao a menos de flexao do primeiro termo.

        Nao trunca sufixo -- truncar dizia que `states` e `stat` e que `as far as` e
        `a far as`, o que faz a comparacao mentir dos dois lados. Aqui o resto da
        expressao tem de bater exato, e so o primeiro termo aceita uma terminacao a mais."""
        pa, pc = base(a).split(), base(c).split()
        if pa == pc:
            return True
        if not pa or not pc or pa[1:] != pc[1:]:
            return False
        x, y = sorted((pa[0], pc[0]), key=len)
        return y in (x + "s", x + "es", x + "d", x + "ed", x + "ing", x[:-1] + "ies")

    respostas = [r.partition("|")[0].strip().lower()
                 for frase in b["itens"] for r in re.findall(r"\{([^}]+)\}", frase)]
    de_vocab = bool(vocab) and all(
        any(mesma(r, v) for v in vocab) for r in respostas)
    if de_vocab and not b.get("banco"):
        raise SystemExit(f"{ident}: gap-fill de VOCABULARIO sem banco de palavras. Todas as "
                         f"respostas sao palavras que esta aula ensinou; sem as candidatas "
                         f"na tela a aluna nao tem como recuperar -- so adivinhar.")
    if not de_vocab and b.get("banco"):
        raise SystemExit(f"{ident}: gap-fill de GRAMATICA com banco de palavras. A lacuna "
                         f"cobra a FORMA, e o banco entrega a resposta. Tire o `banco`.")
    linhas = []
    for frase in b["itens"]:
        if "{" not in frase:
            raise SystemExit(f"{ident}: a frase {frase[:40]!r} nao tem lacuna. Marque o "
                             f"trecho que sai entre chaves.")
        # A FRASE E ESCAPADA INTEIRA, e so entao a lacuna entra.
        #
        # Escapar pedaco a pedaco (partindo antes) deixa a aspa de abertura num pedaco e a
        # de fechamento noutro: nenhuma das duas acha o seu par, e a frase sai com `"` cru
        # onde o molde tem `&ldquo;`/`&rdquo;`. Foi o unico ponto em que a primeira versao
        # deixou de ser byte-a-byte igual.
        #
        # A RESPOSTA, ao contrario, vai CRUA no `data-ok`: e com ela que o que a aluna
        # digitou vai ser comparado. Uma entidade ali faria a resposta certa contar como
        # errada, e ninguem veria o porque.
        # A LARGURA E POR LACUNA, nao por exercicio: no molde a mesma atividade tem campos
        # de 140, 170, 180 e 190 px, dimensionados para a resposta que cabe em cada um.
        # Declarar uma largura para o exercicio inteiro parecia mais limpo e estava errado
        # -- duas atividades nao voltaram byte a byte por causa disso.
        # Sintaxe: `{resposta}` usa o padrao; `{resposta|180px}` manda a largura junto.
        respostas = re.findall(r"\{([^}]+)\}", frase)
        marcado = re.sub(r"\{[^}]+\}", "\x00", frase)
        montado = esc(marcado)
        for r in respostas:
            resp, _, larg = r.partition("|")
            montado = montado.replace(
                "\x00", f'<input class="blank-input" data-ok="{resp}" '
                         f'style="min-width:{larg or b.get("largura", "170px")}" '
                         f'placeholder="...">', 1)
        linhas.append(f'      <p class="chunk-line">{montado}</p>')
    # O de GRAMATICA sai sem o banco -- e nao com um banco vazio, que ocuparia espaco
    # anunciando ajuda que nao existe.
    #
    # O banco vem ANTES das frases, em caixa propria (FB28). Depois delas, num `.subprompt`,
    # ele herdava a margem de topo NEGATIVA dessa classe e subia por cima da ultima linha do
    # exercicio: era o que a revisao viu na atividade 6 da aula 9 do Luiz. E, mesmo sem a
    # sobreposicao, banco que aparece depois nao ajuda a fazer -- ajuda a conferir.
    banco_box = ""
    if b.get("banco"):
        palavras = " &middot; ".join(f"<em>{esc(x)}</em>" for x in b["banco"])
        rot = esc(b.get("rotulo_banco", "Use:")).rstrip(":")
        banco_box = (f'    <div class="word-bank">'
                     f'<span class="wb-rot">{rot}</span> {palavras}</div>\n')
    return (banco_box
            + f'    <div class="fill-list">\n' + "\n".join(linhas) + "\n    </div>\n"
            + f'    <button class="verify-all-btn ghost" onclick="czCheck(this)">Check</button>\n'
            f'    <div class="score-out" id="{ident}-out"></div>')


def r_recursos(b, ident):
    """O acervo do post-class: leitura, escuta, referencia. NAO e exercicio.

    O `link` e obrigatorio e vai ao recurso EXATO -- nao a uma busca, nao a uma home. E a
    licao que o imersivo pagou com um gate proprio: recomendacao sem link e recomendacao que
    ninguem abre, e link de busca faz a aluna procurar o que a aula ja tinha achado."""
    cartoes = []
    for r in b["itens"]:
        if not r.get("url", "").startswith("http"):
            raise SystemExit(f"{ident}: o recurso {r.get('titulo', '?')!r} nao tem link. "
                             f"Acervo sem link e acervo que ninguem abre.")
        cartoes.append(
            f'    <div class="res-card">\n'
            f'      <h5>{esc(r["titulo"])}</h5>\n'
            f'      <span class="res-src">{esc(r["fonte"])}</span>\n'
            f'      <p>{crua(r["texto"])}</p>\n'
            f'      <a class="res-link" href="{r["url"]}" target="_blank" rel="noopener">'
            f'{esc(r["cta"])} &rarr;</a>\n'
            f'    </div>')
    return "\n".join(cartoes)


def r_nota(b, ident):
    """A nota que explica a atividade. Nasce FECHADA, sempre.

    Nao ha parametro para abrir: gabarito visivel antes da decisao e o ANA-017/PRO-002, e a
    unica forma de garantir que ele nao nasca aberto e nao existir o caminho."""
    return (f'    <div class="callout" id="{ident}-key" style="display:none">\n'
            f'      <div class="callout-title">{esc(b["titulo"])}</div>\n'
            # CRU, como no `callout` e no `doc`. Escapando aqui, um texto que ja traz
            # `&mdash;` vira `&amp;mdash;` e a entidade aparece literal na tela. A nota e
            # prosa longa com marcacao propria -- o mesmo tratamento dos outros dois.
            f'      {crua(b["texto"])}\n    </div>')


RENDER = {"classificar": r_classificar, "completar": r_completar,
          "escolha": r_escolha, "par": r_par,
          "frases": r_frases, "lacuna": r_lacuna, "recursos": r_recursos}


def seccao(b, i, vocab=None):
    """Uma atividade completa: cabecalho, instrucoes, exercicio, checagem e nota."""
    ident = _ident(b, i)
    kind = b.get("kind")
    # Seccao SEM exercicio e legitima: o "Lesson recap" do post-class e conteudo puro, e o
    # acervo nao vira exercicio (ANA-013).
    if kind is not None and kind not in RENDER:
        raise SystemExit(f"kind {kind!r} nao existe. Disponiveis: {sorted(RENDER)}")
    if kind not in (None, "frases", "recursos") and not b.get("itens"):
        raise SystemExit(f"{ident}: exercicio sem itens.")

    # `nu: true` -- o bloco sai SEM a moldura `exercise-section`.
    #
    # A moldura e do PRE-CLASS, onde cada exercicio E uma seccao da pagina. No DECK o
    # exercicio vive dentro do `slide-inner`, que ja e a moldura da tela: embrulhar de novo
    # acrescenta um <div> que a folha de estilo do slide nao espera. Sem o flag, nada muda
    # -- o pre-class continua saindo byte a byte igual.
    #
    # E o que permite DECLARAR o exercicio do deck em vez de escrever `data-ok` a mao, que e
    # onde nasceram os dois defeitos de PRO-009 que escaparam ao gate (`an4`, `ev1`).
    # ---- campo que o emissor nao conhece NAO passa em silencio
    #
    # Escrevendo a aula 9 do Luiz eu declarei `chave: {titulo, texto}` num bloco, por analogia
    # com um campo que existe no blocos.json do molde -- e que o emissor tambem ignora. O
    # texto simplesmente nao saiu: sem erro, sem aviso, com o material parecendo pronto. Um
    # gabarito que o autor escreveu e que nunca chega a tela e pior que um que falta, porque
    # ninguem vai procurar.
    CONHECIDOS = {"kind", "id", "n", "nu", "titulo", "badge", "abertura", "instr", "itens",
                  "opcoes", "nota", "rationale", "prompt", "largura", "rotulo_banco",
                  "banco", "barra"}
    desconhecidos = set(b) - CONHECIDOS - {k for k in b if k.startswith("_")}
    if desconhecidos:
        raise SystemExit(f"{ident}: campo(s) que o emissor nao conhece e nao emitiria: "
                         f"{sorted(desconhecidos)}. Prefixe com _ se for comentario; se for "
                         f"conteudo, ele precisa de um campo que exista (a explicacao que "
                         f"abre no fim da atividade e `nota`).")

    nu = b.get("nu")
    partes = [] if nu else ['  <div class="exercise-section">']
    if b.get("titulo"):
        # O post-class NAO numera as seccoes ("Reading", "Listen & Watch"); o pre-class sim
        # ("3 · What the sentence is doing"). Quem decide e a presenca do `n`.
        rot = (f'{b["n"]} &middot; {esc(b["titulo"])}' if b.get("n")
               else esc(b["titulo"]))
        bdg = (f'<span class="badge badge-open">{esc(b["badge"])}</span>'
               if b.get("badge") else "")
        partes.append(f'    <div class="section-header-row"><h4>{rot}</h4>{bdg}</div>')
    # A ABERTURA E UMA SEQUENCIA, nao dois campos.
    #
    # No molde o documento que a aluna le fica ENTRE as duas instrucoes ("Read the lesson
    # plan..." / [o plano] / "Mark the two things..."). Com `instr` e `documento` como
    # campos separados, a ordem sai fixa e o material deixa de ser byte-a-byte igual --
    # foi o ultimo ponto em que o conversor recusou converter, e estava certo.
    #
    # Cada item da abertura e um paragrafo (string) ou o documento (objeto). Quem escreve a
    # aula decide a ordem escrevendo a ordem.
    # A ABERTURA E UMA SEQUENCIA, e cada item diz o que E.
    #
    # No molde o documento que a aluna le fica ENTRE as duas instrucoes; a tabela de recap
    # vem antes do callout que a fecha. Com campos separados a ordem sai fixa, e o material
    # deixa de ser byte-a-byte igual -- foi o ponto em que o conversor recusou converter, e
    # estava certo.
    #
    # A chave EXPLICITA importa porque ha TRES `callout` diferentes no molde: o `doc-block`
    # (o artefato que a aluna le), o `rule-box` visivel (a sintese) e o `id="X-key"`
    # escondido (a nota, que so abre depois). Distinguir por formato do dicionario seria
    # adivinhacao.
    for item in b.get("abertura", b.get("instr", [])):
        if isinstance(item, str):
            partes.append(f'    <p class="task-instr">{esc(item)}</p>')
        elif "doc" in item:
            # O titulo e OPCIONAL: ha documento que e so o texto (a cena que a aluna le,
            # sem cabecalho). Exigir `<strong>` deixava duas atividades sem converter.
            d0 = item["doc"]
            cab0 = (f'      <strong>{esc(d0["titulo"])}</strong><br>\n'
                    if d0.get("titulo") else "")
            partes.append(f'    <div class="callout rule-box doc-block">\n' + cab0 +
                          f'      {crua(d0["texto"])}\n    </div>')
        elif "callout" in item:
            c0 = item["callout"]
            partes.append(f'    <div class="callout rule-box">\n'
                          f'      <span class="callout-title">{esc(c0["titulo"])}</span>\n'
                          f'      {crua(c0["texto"])}\n    </div>')
        elif "tabela" in item:
            # N COLUNAS, com ou sem cabecalho. A primeira celula de cada linha e o rotulo e
            # vai em negrito -- e assim no recap de duas colunas e na referencia de tres.
            # A largura declarada pousa no <th> quando ha cabecalho, e na primeira <td>
            # quando nao ha: e onde o molde a escreve nos dois casos.
            t0 = item["tabela"]
            larg = item.get("largura_rotulo")
            cab = item.get("cabecalho")
            head = ""
            if cab:
                ths = "".join(
                    f'<th{f" style=\"width:{larg}\"" if (j == 0 and larg) else ""}>'
                    f'{esc(c)}</th>' for j, c in enumerate(cab))
                head = f"        <thead><tr>{ths}</tr></thead>\n"
            linhas = []
            for j, celulas in enumerate(t0):
                st = f' style="width:{larg}"' if (j == 0 and larg and not cab) else ""
                resto = "".join(f"<td>{c}</td>" for c in celulas[1:])
                linhas.append(f'          <tr><td{st}><strong>{esc(celulas[0])}</strong>'
                              f'</td>{resto}</tr>')
            partes.append('    <div class="tbl-wrap">\n'
                          f'      <table class="data" style="min-width:'
                          f'{item.get("min_width", "520px")}">\n' + head +
                          "        <tbody>\n" + "\n".join(linhas) +
                          "\n        </tbody>\n      </table>\n    </div>")
        elif "lista" in item:
            itens = "".join(f'\n      <li>{x}</li>' for x in item["lista"])
            partes.append(f'    <ul style="{item.get("estilo", "")}">{itens}\n    </ul>')
        elif "gravador" in item:
            # O ID APARECE OITO VEZES em seis elementos: o botao de gravar, o de parar, o
            # cronometro, o player, o painel de apagar e a mensagem de erro. E a cadeia mais
            # longa do molde, e cada elo que divergir quebra outra coisa: o Stop nao para, o
            # tempo nao anda, o audio nao aparece, o Delete nao acha o que apagar. Nada
            # disso da erro -- so nao funciona.
            g = item["gravador"]
            partes.append(
                f'    <div class="rec-bar">\n'
                f'      <button class="audio-btn-sm" id="{g}-start" '
                f'onclick="rcStart(\'{g}\')">&#9679; {esc(item.get("rotulo_gravar", "Start recording"))}</button>\n'
                f'      <button class="audio-btn-sm" id="{g}-stop" style="display:none;'
                f'background:var(--danger);border-color:var(--danger)" '
                f'onclick="rcStop(\'{g}\')">&#9632; Stop</button>\n'
                f'      <span class="rec-time" id="{g}-time">00:00</span>\n'
                f'    </div>\n'
                f'    <audio id="{g}-player" controls="controls" style="display:none;'
                f'width:100%;margin-top:var(--space-3)"></audio>\n'
                f'    <div id="{g}-done" style="display:none;gap:var(--space-2h);'
                f'margin-top:var(--space-2h);flex-wrap:wrap">\n'
                f'      <button class="audio-btn-sm ghost" onclick="rcApaga(\'{g}\')">'
                f'Delete recording</button>\n'
                f'    </div>\n'
                f'    <div class="callout warn" id="{g}-msg" style="display:none"></div>')
        elif "audio" in item:
            # A BARRA DE AUDIO de um exercicio: o acionador, o Stop e o estado. O texto vai
            # no `sayAs`, e o AUD_MAP resolve o arquivo -- ver check_audio_oficial (GATE 40).
            # O `data-rot` guarda o rotulo original porque o botao vira "Pause" enquanto
            # toca e precisa saber para o que voltar.
            au = item["audio"]
            linhas = [f'    <div style="display:flex;gap:var(--space-2h);flex-wrap:wrap;'
                      f'align-items:center;margin:var(--space-3h) 0" data-audgrupo="'
                      f'{au.get("grupo", "1")}">']
            # `velocidades` transforma a barra: entra o seletor Normal/Slower e o Play deixa
            # de tocar direto -- passa a chamar `audMain`, que toca a velocidade ESCOLHIDA.
            # Sem isso, um Play fixo em 0.95 ignoraria em silencio o que a aluna marcou.
            vel = au.get("velocidades")
            if vel:
                linhas.append('      <span class="aud-etiq">Speed</span>')
                for i, (rot, taxa) in enumerate(vel):
                    linhas.append(
                        f'      <button class="audio-btn-sm ghost aud-op" '
                        f'onclick="sayAs(\'{au["texto"]}\',{taxa},\'{au["voz"]}\')" '
                        f'data-aud-op="{i}" aria-pressed="{"true" if i == 0 else "false"}">'
                        f'{esc(rot)}</button>')
                linhas.append(
                    '      <button type="button" class="audio-btn-sm aud-main" '
                    'onclick="audMain(this)" data-aud-uni="1" data-rot="&#9654; Play">'
                    '&#9654; Play</button>'
                    '<button class="audio-btn-sm aud-stop" onclick="audStop(this)">'
                    '&#9632; Stop</button>')
            else:
                linhas.append(
                    f'      <button class="audio-btn-sm" onclick="sayAs(\'{au["texto"]}\','
                    f'{au.get("rate", "0.95")},\'{au["voz"]}\')" data-aud-uni="1" '
                    f'data-rot="&#9654; Play">&#9654; Play</button>')
                linhas.append('      <button type="button" class="audio-btn-sm aud-stop" '
                              'onclick="audStop(this)">&#9632; Stop</button>')
            linhas.append('      <span class="aud-estado" role="status" aria-live="polite">'
                          '</span>')
            linhas.append('    </div>')
            partes.append("\n".join(linhas))
        elif "recurso" in item:
            # UM cartao de acervo dentro da sequencia. O `kind: recursos` continua existindo
            # para a seccao que SO tem cartoes; este e para a que mistura -- tabela de
            # referencia mais o link onde ela e explicada. Sem ele, a conversao dessa seccao
            # DESCARTAVA o cartao em silencio, e so a comparacao de bytes viu.
            r0 = item["recurso"]
            if not r0.get("url", "").startswith("http"):
                raise SystemExit(f"{ident}: recurso sem link.")
            partes.append(
                f'    <div class="res-card">\n      <h5>{esc(r0["titulo"])}</h5>\n'
                f'      <span class="res-src">{esc(r0["fonte"])}</span>\n'
                f'      <p>{crua(r0["texto"])}</p>\n'
                f'      <a class="res-link" href="{r0["url"]}" target="_blank" '
                f'rel="noopener">{esc(r0["cta"])} &rarr;</a>\n    </div>')
        elif "escrita" in item:
            # CINCO IDENTIFICADORES EM TREZE LUGARES, e cruzados: o `pwCount` recebe o id do
            # corpo, o do contador E a chave de armazenamento; o `pwClear` recebe os pares
            # (id, chave) dos dois campos mais o contador. Errar um deles nao da erro --
            # so faz o contador parar, ou o Clear limpar a tela sem limpar o que foi salvo,
            # e a aluna perder o que escreveu ao recarregar.
            e = item["escrita"]
            i0, k0 = e["id"], e["chave"]
            partes.append(
                f'    <label class="mail-label" for="{i0}-subject">'
                f'{esc(e.get("rotulo_assunto", "Subject"))}</label>\n'
                f'    <input class="mail-subject" id="{i0}-subject" placeholder="" '
                f'oninput="save(\'{k0}_subject\',this.value)">\n'
                f'    <label class="mail-label" for="{i0}-body" '
                f'style="margin-top:var(--space-3)">{esc(e.get("rotulo_corpo", "Note"))}</label>\n'
                f'    <textarea class="writebox" id="{i0}-body" style="min-height:'
                f'{e.get("altura", "170px")}" placeholder="" '
                f'oninput="pwCount(\'{i0}-body\',\'{i0}-count\',\'{k0}_writing\')"></textarea>\n'
                f'    <div class="wc"><span id="{i0}-count">0 words</span></div>\n'
                f'    <button class="verify-all-btn ghost" onclick="pwClear(['
                f'[\'{i0}-subject\',\'{k0}_subject\'],[\'{i0}-body\',\'{k0}_writing\']],'
                f'\'{i0}-count\')">{esc(e.get("rotulo_limpar", "Clear and start again"))}'
                f'</button>')
        elif "titulo" in item and "texto" in item:
            # FORMA ANTIGA, de antes de a abertura ganhar chave de tipo: `{titulo, texto}`
            # sem etiqueta era sempre o documento. Continua lida porque ja ha declaracao
            # assim no repo -- quebrar o que ja foi migrado seria pedir para a migracao
            # parar no meio.
            partes.append(f'    <div class="callout rule-box doc-block">\n'
                          f'      <strong>{esc(item["titulo"])}</strong><br>\n'
                          f'      {crua(item["texto"])}\n    </div>')
        else:
            raise SystemExit(f"{ident}: item de abertura sem tipo conhecido: "
                             f"{sorted(item)}")
    if kind is not None:
        if kind == "lacuna":
            partes.append(RENDER[kind](b, ident, vocab))
        else:
            partes.append(RENDER[kind](b, ident))
    if b.get("nota"):
        partes.append(r_nota(b["nota"], ident))
    if not nu:
        partes.append("  </div>")
    return "\n".join(partes)


def vocab_da_regiao(lista):
    """As palavras que a regiao ENSINA -- o que um `par` de vocabulario apresenta.

    E daqui que sai a decisao entre gap-fill de vocabulario e de gramatica, em vez de um
    flag: se toda resposta da lacuna esta nesta lista, a lacuna cobra vocabulario."""
    fora = set()
    for b in lista:
        if b.get("kind") == "par":
            for it in b.get("itens", []):
                fora.add(str(it.get("t", "")).strip().lower())
    return fora


def blocos(lista, vocab=None):
    """As atividades de uma regiao, na ordem declarada.

    `vocab` e o vocabulario da AULA INTEIRA e vem do builder, que ve todas as chaves do
    `blocos.json`. Cai para o da propria regiao quando chamado sozinho (round-trip, testes)."""
    vocab = vocab if vocab is not None else vocab_da_regiao(lista)
    return "\n".join(seccao(b, i + 1, vocab) for i, b in enumerate(lista))
