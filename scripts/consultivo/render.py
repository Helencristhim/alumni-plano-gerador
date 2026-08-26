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
    return (f'    <div class="quiz-item">\n      <div class="quiz-options" id="{ident}">\n'
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


def r_lacuna(b, ident):
    """Completar a frase. A lacuna vai ENTRE CHAVES, no meio do texto:

        "{The syllabus says} twenty hours, and the plan has eighteen."

    O autor escreve a frase inteira e marca o pedaco que sai. O `<input>`, o `data-ok`, o
    `style` e o `placeholder` sao do render -- sao quatro atributos identicos em cinquenta
    lacunas do molde, digitados um a um.

    O BANCO e obrigatorio (REGRA 2.4 do imersivo, aprendida ali com uma aula que cobrava
    cinco palavras que ninguem tinha ensinado): sem as candidatas na tela, "complete a
    frase" nao e recuperacao lexical -- ou a palavra exata vem a cabeca, ou a aluna trava
    sem saida."""
    if not b.get("banco"):
        raise SystemExit(f"{ident}: gap-fill sem banco de palavras. Sem as candidatas na "
                         f"tela a aluna nao tem como recuperar -- so adivinhar.")
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
        respostas = re.findall(r"\{([^}]+)\}", frase)
        marcado = re.sub(r"\{[^}]+\}", "\x00", frase)
        montado = esc(marcado)
        for r in respostas:
            montado = montado.replace(
                "\x00", f'<input class="blank-input" data-ok="{r}" '
                         f'style="min-width:170px" placeholder="...">', 1)
        linhas.append(f'      <p class="chunk-line">{montado}</p>')
    banco = " &middot; ".join(f"<em>{esc(x)}</em>" for x in b["banco"])
    return (f'    <div class="fill-list">\n' + "\n".join(linhas) + "\n    </div>\n"
            f'    <p class="subprompt">{esc(b.get("rotulo_banco", "Openings you can use:"))} '
            f'{banco}</p>\n'
            f'    <button class="verify-all-btn ghost" onclick="czCheck(this)">Check</button>\n'
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
            f'      <p>{r["texto"]}</p>\n'
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
            f'      {esc(b["texto"])}\n    </div>')


RENDER = {"classificar": r_classificar, "escolha": r_escolha, "par": r_par,
          "frases": r_frases, "lacuna": r_lacuna, "recursos": r_recursos}


def seccao(b, i):
    """Uma atividade completa: cabecalho, instrucoes, exercicio, checagem e nota."""
    ident = _ident(b, i)
    kind = b.get("kind")
    # Seccao SEM exercicio e legitima: o "Lesson recap" do post-class e conteudo puro, e o
    # acervo nao vira exercicio (ANA-013).
    if kind is not None and kind not in RENDER:
        raise SystemExit(f"kind {kind!r} nao existe. Disponiveis: {sorted(RENDER)}")
    if kind not in (None, "frases", "recursos") and not b.get("itens"):
        raise SystemExit(f"{ident}: exercicio sem itens.")

    partes = ['  <div class="exercise-section">']
    if b.get("titulo"):
        # O post-class NAO numera as seccoes ("Reading", "Listen & Watch"); o pre-class sim
        # ("3 · What the sentence is doing"). Quem decide e a presenca do `n`.
        rot = (f'{b["n"]} &middot; {esc(b["titulo"])}' if b.get("n")
               else esc(b["titulo"]))
        partes.append(f'    <div class="section-header-row"><h4>{rot}</h4></div>')
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
            d0 = item["doc"]
            partes.append(f'    <div class="callout rule-box doc-block">\n'
                          f'      <strong>{esc(d0["titulo"])}</strong><br>\n'
                          f'      {d0["texto"]}\n    </div>')
        elif "callout" in item:
            c0 = item["callout"]
            partes.append(f'    <div class="callout rule-box">\n'
                          f'      <span class="callout-title">{esc(c0["titulo"])}</span>\n'
                          f'      {c0["texto"]}\n    </div>')
        elif "tabela" in item:
            t0 = item["tabela"]
            larg = item.get("largura_rotulo")
            linhas = []
            for j, (rot, val) in enumerate(t0):
                st = f' style="width:{larg}"' if (j == 0 and larg) else ""
                linhas.append(f'          <tr><td{st}><strong>{esc(rot)}</strong></td>'
                              f'<td>{val}</td></tr>')
            partes.append('    <div class="tbl-wrap">\n'
                          f'      <table class="data" style="min-width:'
                          f'{item.get("min_width", "520px")}">\n        <tbody>\n'
                          + "\n".join(linhas) + "\n        </tbody>\n      </table>\n"
                          "    </div>")
        elif "lista" in item:
            itens = "".join(f'\n      <li>{x}</li>' for x in item["lista"])
            partes.append(f'    <ul style="{item.get("estilo", "")}">{itens}\n    </ul>')
        elif "titulo" in item and "texto" in item:
            # FORMA ANTIGA, de antes de a abertura ganhar chave de tipo: `{titulo, texto}`
            # sem etiqueta era sempre o documento. Continua lida porque ja ha declaracao
            # assim no repo -- quebrar o que ja foi migrado seria pedir para a migracao
            # parar no meio.
            partes.append(f'    <div class="callout rule-box doc-block">\n'
                          f'      <strong>{esc(item["titulo"])}</strong><br>\n'
                          f'      {item["texto"]}\n    </div>')
        else:
            raise SystemExit(f"{ident}: item de abertura sem tipo conhecido: "
                             f"{sorted(item)}")
    if kind is not None:
        partes.append(RENDER[kind](b, ident))
    if b.get("nota"):
        partes.append(r_nota(b["nota"], ident))
    partes.append("  </div>")
    return "\n".join(partes)


def blocos(lista):
    """As atividades de uma regiao, na ordem declarada."""
    return "\n".join(seccao(b, i + 1) for i, b in enumerate(lista))
