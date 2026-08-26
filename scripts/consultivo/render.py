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
    return (f'    <div class="quiz-item">\n      <div class="quiz-options" id="{ident}">\n'
            + "\n".join(linhas) + "\n      </div>\n    </div>\n"
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


def r_nota(b, ident):
    """A nota que explica a atividade. Nasce FECHADA, sempre.

    Nao ha parametro para abrir: gabarito visivel antes da decisao e o ANA-017/PRO-002, e a
    unica forma de garantir que ele nao nasca aberto e nao existir o caminho."""
    return (f'    <div class="callout" id="{ident}-key" style="display:none">\n'
            f'      <div class="callout-title">{esc(b["titulo"])}</div>\n'
            f'      {esc(b["texto"])}\n    </div>')


RENDER = {"classificar": r_classificar, "escolha": r_escolha, "par": r_par,
          "frases": r_frases, "lacuna": r_lacuna}


def seccao(b, i):
    """Uma atividade completa: cabecalho, instrucoes, exercicio, checagem e nota."""
    ident = _ident(b, i)
    kind = b.get("kind")
    if kind not in RENDER:
        raise SystemExit(f"kind {kind!r} nao existe. Disponiveis: {sorted(RENDER)}")
    if kind != "frases" and not b.get("itens"):
        raise SystemExit(f"{ident}: exercicio sem itens.")

    partes = ['  <div class="exercise-section">']
    if b.get("titulo"):
        partes.append(f'    <div class="section-header-row"><h4>{b.get("n", i)} &middot; '
                      f'{esc(b["titulo"])}</h4></div>')
    for p in b.get("instr", []):
        partes.append(f'    <p class="task-instr">{esc(p)}</p>')
    partes.append(RENDER[kind](b, ident))
    if b.get("nota"):
        partes.append(r_nota(b["nota"], ident))
    partes.append("  </div>")
    return "\n".join(partes)


def blocos(lista):
    """As atividades de uma regiao, na ordem declarada."""
    return "\n".join(seccao(b, i + 1) for i, b in enumerate(lista))
