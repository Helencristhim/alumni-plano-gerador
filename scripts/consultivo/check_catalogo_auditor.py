#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 41 — o catalogo do auditor, na parte que uma maquina consegue provar.

DE ONDE ISTO VEM
----------------
Do `catalogo_erros_recorrentes_auditor_private_black.xlsx` (25/08/2026): 72 modos de falha
consolidados dos 14 documentos normativos e das falhas COMPROVADAS em Erica, Marcos,
Marlene e Stephanie.

A coluna "Deteccao recomendada" do catalogo classifica 29 itens como "Semantico". Ela e uma
SUGESTAO, nao um limite -- varios desses tem manifestacao observavel se a pergunta for
reformulada. INT-002 ("contaminacao de ciclo") estava marcado como Script+semantico e foi
encontrado perguntando uma coisa so: *este arquivo fala de alguma aula que nao existe neste
ciclo?* A resposta era sim, em dois arquivos, e o aluno via.

O QUE ESTA AQUI, E O QUE NAO
-----------------------------
AQUI: as regras que consigo enunciar sem ambiguidade e provar com um caso plantado. Cada
uma carrega o ID do catalogo, e o selftest mostra o defeito que ela pega.

NAO AQUI, e de proposito: julgamento pedagogico. "Guided Discovery nominal", "producao
desalinhada ao objetivo", "perfil tratado como diagnostico" -- essas dependem de LER o
conteudo e decidir se ele faz o que promete. Um detector que fingisse medir isso daria
verde a torto e a direito e ensinaria a confiar num numero que nao existe. O criterio de
teste de cada uma esta no catalogo, para quem for ler.

POR QUE O MOLDE PASSA EM TODAS, E MESMO ASSIM ELAS VALEM
---------------------------------------------------------
Estas regras nasceram DEPOIS de o molde estar limpo. O gate nao existe para o arquivo de
hoje: existe para a aula que ainda vai ser gerada. Escrever a regra enquanto tudo esta
verde e barato; escrever depois do defeito custa o incidente.

ESCOPO: o carimbo `alumni-anatomia=consultivo`.

USO:
    python3 scripts/consultivo/check_catalogo_auditor.py [arquivo.html ...]
    python3 scripts/consultivo/check_catalogo_auditor.py --selftest
"""
import glob
import html
import os
import re
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIA = "consultivo"
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

MODALIDADES = ["Reading", "Listening", "Grammar", "ESP"]
POSTCLASS_MINIMO = ["Reading", "Listen", "Speak", "Write"]
# marcadores de processo interno que nao podem chegar ao aluno (INT-018)
INTERNOS = [r"\bhip[oó]tese\b", r"\ba validar\b", r"\bgerador\b", r"\bTODO\b", r"\bFIXME\b",
            r"\brationale interno\b", r"\bauditoria\b"]


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def sem_codigo(c):
    """HTML sem comentario, script e style. Base de tudo que fala de TELA."""
    c = re.sub(r"<!--.*?-->", " ", c, flags=re.S)
    return re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", c, flags=re.S | re.I)


def texto_do_aluno(c):
    """O que o ALUNO le. Sem `data-teacher`, que e do professor e continua em portugues."""
    c = re.sub(r'\sdata-teacher="[^"]*"', " ", sem_codigo(c))
    return " ".join(re.sub(r"<[^>]+>", " ", c).split())


def bloco_por_id(c, ident):
    m = re.search(r'<div[^>]*id="' + re.escape(ident) + r'"[^>]*>', c)
    if not m:
        return None
    prof = 0
    for t in re.finditer(r"<div\b[^>]*>|</div>", c[m.start():]):
        prof += 1 if t.group(0).startswith("<div") else -1
        if prof == 0:
            return c[m.start():m.start() + t.end()]
    return None


def aulas_de(c):
    return sorted({int(n) for n in re.findall(r"\b(\d+)\s*:\s*\{\s*n\s*:\s*\1\b", c)})


def eh_professor(c):
    return 'id="tab-inclass"' in c


# ---------------------------------------------------------------------------
# as regras. cada uma devolve [] ou uma lista de mensagens.
# ---------------------------------------------------------------------------
def r_transcript_fechado(c, ctx):
    """PRO-006 · SEQ-005 — transcript liberado cedo.

    Em listening, o transcript nao pode estar aberto antes da tentativa: ler o que foi dito
    responde a pergunta da escuta antes de ela ser feita. A caixa nasce FECHADA, e quem a
    abre e o botao."""
    fora = []
    for m in re.finditer(r'<div[^>]*class="[^"]*\btranscript-box\b[^"]*"[^>]*>', ctx["tela"]):
        tag = m.group(0)
        if "display:none" not in tag.replace(" ", "") and "hidden" not in tag:
            fora.append(f"PRO-006: caixa de transcript nasce ABERTA — {tag[:70]}. O aluno le "
                        f"o que deveria decodificar pelo ouvido.")
    return fora


def r_player_fora_do_listening(c, ctx):
    """ANA-012 — audio em pre-class de framework nao-Listening.

    Player no pre-class de Reading/Grammar/ESP introduz escuta sem autorizacao funcional: o
    pre-class antecipa o in-class, e o in-class daquela aula nao e de escuta."""
    fora = []
    for n in ctx["aulas"]:
        mod = re.search(r"\b" + str(n) + r":\{n:" + str(n) + r",bloco:\d+,mod:'([^']+)'", c)
        if not mod or mod.group(1) == "Listening":
            continue
        b = bloco_por_id(ctx["tela"], f"pc{n}")
        if b and re.search(r"say\(|sayAs\(|playTalk\(|audMain", b):
            fora.append(f"ANA-012: o pre-class da aula {n} ({mod.group(1)}) tem acionador de "
                        f"audio. Escuta no pre-class de framework nao-Listening precisa de "
                        f"autorizacao funcional.")
    return fora


def r_postclass_sem_exercicio(c, ctx):
    """ANA-013 — post-class transformado em exercicio obrigatorio.

    Reading, Listening/Watching e Language Reference sao ACERVO: nao levam quiz nem
    compreensao. So speaking/writing sao pratica, e opcional."""
    b = bloco_por_id(ctx["tela"], "tab-postclass")
    if not b:
        return []
    fora = []
    if re.search(r'class="[^"]*\bquiz\b', b) or re.search(r"\bselCheck\(|\bppCheck\(", b):
        fora.append("ANA-013: o post-class tem exercicio de compreensao. Reading, "
                    "Listen/Watch e Language Reference sao acervo — so speaking/writing "
                    "podem ser pratica, e opcional.")
    return fora


def r_postclass_componentes(c, ctx):
    """ANA-014 — post-class sem componentes minimos."""
    b = bloco_por_id(ctx["tela"], "tab-postclass")
    if not b:
        return []
    txt = " ".join(re.sub(r"<[^>]+>", " ", b).split())
    faltam = [x for x in POSTCLASS_MINIMO if x not in txt]
    return ([f"ANA-014: o post-class nao oferece {faltam}. O banco precisa de leitura, "
             f"escuta/video e apoio linguistico, alem das praticas opcionais."] if faltam else [])


def r_bloco1_diagnostico(c, ctx):
    """ANA-004 · SEQ-001 — diagnostico inicial incompleto.

    As aulas 1-4 cobrem Reading, Listening, Grammar e ESP uma vez cada. Depois da aula 4 a
    distribuicao e adaptativa (02 §2.2) e esta regra nao se aplica."""
    b1 = [n for n in ctx["aulas"] if n <= 4]
    if len(b1) < 4:
        return []
    mods = []
    for n in b1:
        m = re.search(r"\b" + str(n) + r":\{n:" + str(n) + r",bloco:\d+,mod:'([^']+)'", c)
        mods.append(m.group(1) if m else "?")
    faltam = [x for x in MODALIDADES if x not in mods]
    if faltam:
        return [f"ANA-004: o bloco 1 nao cobre {faltam} — as quatro primeiras aulas sao o "
                f"diagnostico real e cobrem as quatro modalidades. Tem: {mods}"]
    return []


def r_ciclo_declarado(c, ctx):
    """ANA-003 — ciclo diferente de 20 aulas."""
    m = re.search(r"var CICLO=\{[^}]*aulas:(\d+)", c)
    if not m:
        return ["ANA-003: sem var CICLO — nao da para saber de que ciclo este material e."]
    if int(m.group(1)) != 20:
        return [f"ANA-003: o ciclo declara {m.group(1)} aulas, e o ciclo regular tem 20 "
                f"(02 §1). Pacote fora disso precisa de decisao registrada."]
    return []


def r_metadado_interno(c, ctx):
    """INT-018 — metadado interno exposto ao aluno.

    So no ARQUIVO DO ALUNO, e so no que chega a TELA: comentario de codigo nao e conteudo, e
    reprova-lo ensinaria a apagar o comentario em vez do vazamento."""
    if ctx["professor"]:
        return []
    fora = []
    for rx in INTERNOS:
        m = re.search(rx, ctx["texto"], re.I if rx.islower() else 0)
        if m:
            fora.append(f"INT-018: marcador de processo interno na tela do aluno "
                        f"(/{rx}/): \"...{ctx['texto'][max(0, m.start()-50):m.start()+40]}...\"")
    return fora


def r_elenco_consistente(c, ctx):
    """REG-002 — terminologia divergente entre tela, midia e guia.

    Todo personagem declarado no elenco aparece na tela; e nenhuma FALA e atribuida a
    alguem que nao esta no elenco. Sao os dois lados do mesmo defeito."""
    cast = re.findall(r'\{n:"([^"]+)",g:"[fm]"\}', c)
    if not cast:
        return []
    fora = []
    for nome in cast:
        if not re.search(r"\b" + re.escape(nome) + r"\b", ctx["texto"]):
            fora.append(f"REG-002: {nome!r} esta no elenco e nao aparece em lugar nenhum da "
                        f"tela. Personagem declarado e personagem que fala.")
    # o outro lado: rotulo de falante fora do elenco
    for m in re.finditer(r'class="[^"]*\bspk-name\b[^"]*"[^>]*>([^<]{1,30})<', ctx["tela"]):
        quem = m.group(1).strip().rstrip(":")
        if quem and quem not in cast:
            fora.append(f"REG-002: a fala e atribuida a {quem!r}, que nao esta no elenco "
                        f"{cast}.")
    return fora


def r_avaliacao_declarada(c, ctx):
    """ANA-002 · AUT-003 — avaliacao indefinida, ou teste presumido.

    Na ausencia de escolha explicita o modelo e Acompanhamento docente (00 §5). O que NAO
    pode e o material preparar teste sem que a escolha por Avaliacao formal esteja escrita."""
    if not ctx["professor"]:
        return []
    tem_formal = bool(re.search(r"Avalia[çc][ãa]o formal", c))
    tem_acomp = bool(re.search(r"Acompanhamento docente", c))
    if not tem_formal and not tem_acomp:
        return ["ANA-002: nenhum modelo de avaliacao declarado. Sem decisao explicita, o "
                "material tem de dizer Acompanhamento docente (00 §5) — vazio nao vale."]
    # AUT-003 se mede na ESTRUTURA, nunca na frase.
    #
    # A primeira versao desta regra procurava "teste formal" no texto e reprovou o proprio
    # molde -- onde as tres ocorrencias sao NEGACOES ("nao ha teste formal previsto",
    # "a estimativa nao vem de teste formal"). Procurar a mencao encontra tanto quem cria o
    # teste quanto quem declara que nao ha; e a segunda e exatamente o comportamento certo.
    #
    # O que prova a criacao de um teste e uma AULA tipada como teste, nao uma frase sobre
    # testes.
    if not tem_formal:
        tipos = re.findall(r"mod:'([^']+)'", c)
        teste = [t for t in tipos if re.search(r"teste|test|prova|exam", t, re.I)]
        if teste:
            return [f"AUT-003: ha aula tipada como {teste} sem que a escolha por 'Avaliacao "
                    f"formal com teste' esteja declarada. O fallback obrigatorio e "
                    f"Acompanhamento docente (00 §5)."]
    return []


def r_recurso_duplicado(c, ctx):
    """ANA-015 — Reading e Language Reference duplicados.

    O mesmo LINK em duas categorias do post-class e o mesmo recurso pedindo a mesma
    operacao duas vezes. Tema comum nao e duplicacao; URL identica e."""
    b = bloco_por_id(ctx["tela"], "tab-postclass")
    if not b:
        return []
    urls = re.findall(r'href="(https?://[^"]+)"', b)
    rep = sorted({u for u in urls if urls.count(u) > 1})
    return ([f"ANA-015: o mesmo recurso aparece {urls.count(rep[0])}x no post-class "
             f"({rep[0][:70]}). Duas categorias, o mesmo link, a mesma operacao."] if rep else [])


LETRAS = "ABCDEFGHIJ"


def _grades(t, classe):
    """Toda grade de `classe`: (id, corpo, fechou).

    Conta o aninhamento em vez de supor o que vem depois. A versao anterior casava
    `</div>\\s*<button` -- o rabo que a grade tem no PRE-CLASS. No deck o botao esta noutro
    lugar, entao a regra via 10 das 14 grades e passava, calada, pelas outras 4. Uma delas
    era a `an4`, que alternava perfeitamente.

    E o mesmo defeito de sempre: a medida parecia bem-sucedida porque olhava o lugar errado.

    Devolve `fechou` porque a primeira tentativa de guarda que escrevi era VAZIA: eu
    comparava "quantas grades li" com "quantas existem", e as duas contagens saiam da MESMA
    regex de abertura -- nunca podiam diferir. Um guarda que nao pode disparar da a mesma
    sensacao de seguranca que um que funciona, e custa o mesmo em leitura. O que se mede de
    verdade e se o corpo FECHOU: sem isso o corpo e o resto do documento, e a chave lida
    dali nao e a da grade."""
    for m in re.finditer(r'<div class="%s" id="([^"]+)">' % classe, t):
        i, nivel, fechou = m.end(), 1, False
        for d in re.finditer(r"<div\b|</div>", t[m.end():]):
            nivel += 1 if d.group(0) == "<div" else -1
            if nivel == 0:
                i, fechou = m.end() + d.start(), True
                break
        yield m.group(1), t[m.end():i], fechou


def _grupos(seq):
    """Maior sequencia de valores iguais em fila."""
    maior = atual = 1
    for a, b in zip(seq, seq[1:]):
        atual = atual + 1 if a == b else 1
        maior = max(maior, atual)
    return maior if seq else 0


def r_resposta_previsivel(c, ctx):
    """PRO-009 — a resposta se acerta pela POSICAO, sem ler o item.

    Tres formas da mesma falha, e as tres estavam no molde em 26/08/2026:

    - `classificar`/`completar` cuja chave e a permutacao identidade: item 1 -> opcao A,
      item 2 -> opcao B... Quem percebe preenche em fila sem ler nada. Era o caso de `mo2`
      (seis itens, A B C D E F) e `nt4` (tres, A B C). E a mesma exigencia que a REGRA 24
      ja faz no imersivo.
    - `par` com a resposta sempre do mesmo lado, ou alternando perfeitamente. Os SEIS pares
      do molde alternavam (a b a b a b / b a b a b a): depois de dois, a aluna sabe o resto.
    - `escolha` de multipla marcacao com as certas todas coladas.

    Tambem barra sequencia de tres do mesmo lado no `par`: e o "agrupado por categoria" que
    o catalogo descreve, e foi o que uma primeira correcao minha produziu sem querer ao
    trocar "uma linha" de cada grade (`b a b` virou `b b b`)."""
    fora = []
    t = ctx["tela"]
    for ident, corpo, fechou in _grades(t, "match-grid"):
        if not fechou:
            fora.append(f"PRO-009: a grade '{ident}' nao fecha — a chave lida dali nao e a "
                        f"dela, e qualquer veredito sobre esta grade e falso.")
            continue
        ok = re.findall(r'<select data-ok="([A-J])"', corpo)
        if len(ok) < 3:
            continue
        if ok == sorted(ok) and len(set(ok)) == len(ok):
            fora.append(f"PRO-009: em '{ident}' a chave e {' '.join(ok)} — a opcao certa de "
                        f"cada item e a que esta na mesma posicao dele.")
        elif len(set(ok)) <= 2 and all(a != b for a, b in zip(ok, ok[1:])):
            # Duas categorias alternando e a MESMA falha do `par`, e a primeira versao
            # desta regra so a media no `par`. `se3`, `ce3` e `an4` passavam.
            fora.append(f"PRO-009: em '{ident}' as duas categorias alternam perfeitamente "
                        f"({' '.join(ok)}) — depois de dois itens o resto se adivinha.")
        elif len(set(ok)) <= 2 and _grupos(ok) > 2:
            fora.append(f"PRO-009: em '{ident}' ha tres respostas seguidas da mesma "
                        f"categoria ({' '.join(ok)}).")
        else:
            fixos = sum(1 for i, o in enumerate(ok) if i < len(LETRAS) and o == LETRAS[i])
            if fixos >= 3 and fixos >= 2 * (len(ok) / max(len(set(ok)), 1)):
                fora.append(f"PRO-009: em '{ident}' {fixos} de {len(ok)} itens tem a resposta "
                            f"na propria posicao ({' '.join(ok)}) — quem preenche em fila "
                            f"acerta a maioria sem ler.")

    for ident, corpo, fechou in _grades(t, "pair-grid"):
        if not fechou:
            fora.append(f"PRO-009: o par '{ident}' nao fecha.")
            continue
        ok = re.findall(r'<div class="pair-row" data-ok="([ab])"', corpo)
        if len(ok) < 3:
            continue
        if len(set(ok)) == 1:
            fora.append(f"PRO-009: em '{ident}' a resposta esta SEMPRE do mesmo lado "
                        f"({' '.join(ok)}).")
        elif all(a != b for a, b in zip(ok, ok[1:])):
            fora.append(f"PRO-009: em '{ident}' os lados alternam perfeitamente "
                        f"({' '.join(ok)}) — depois de dois itens o resto se adivinha.")
        elif _grupos(ok) > 2:
            fora.append(f"PRO-009: em '{ident}' ha tres respostas seguidas do mesmo "
                        f"lado ({' '.join(ok)}).")

    for m in re.finditer(r'<div class="quiz-options" id="([^"]+)">(.*?)</div>', t, re.S):
        ok = re.findall(r'data-ok="([01])"', m.group(2))
        pos = [i for i, x in enumerate(ok) if x == "1"]
        if len(pos) > 1 and len(pos) < len(ok) and all(b - a == 1 for a, b in zip(pos, pos[1:])):
            fora.append(f"PRO-009: em '{m.group(1)}' as respostas certas estao todas "
                        f"coladas ({''.join(ok)}).")
    return fora


# A voz do MATERIAL (instrucao, gabarito, nota) contra a voz de um ARTEFATO (o syllabus, a
# ficha de observacao, o e-mail). O syllabus pode dizer "in the last session" porque e o
# texto dele; a instrucao nao pode dizer "the third" porque a ordem e nossa e muda.
VOZ_DO_MATERIAL = (r'<p class="task-instr">(.*?)</p>'
                   r'|<div class="rationale">(.*?)</div>'
                   r'|<div class="callout"(?![^>]*doc-block)[^>]*>(.*?)</div>')
POSICIONAL = (r'\bthe (first|second|third|fourth|fifth|last) '
              r'(line|one|option|item|card|column|row|answer|example|sentence)\b'
              r'|\bis the (first|second|third|fourth|fifth|last)\b'
              r'|\bon the (left|right)\b'
              r'|\bthe (one|option) (above|below)\b')


def r_referencia_posicional(c, ctx):
    """PRO-008 — a instrucao ou o gabarito aponta por POSICAO onde ha rotulo estavel.

    Achado no molde: o gabarito de `mo2` dizia *"The one that decides the lesson is the
    THIRD: restating what someone else said"* — e ja dava o rotulo logo depois dos dois
    pontos. A posicao nao acrescentava nada e quebrava se as opcoes fossem reordenadas,
    que e exatamente o que a PRO-009 exige que se faca.

    Pior: o gabarito de `bk4` dizia *"Everything in the FIRST COLUMN is about the reason"*
    — e as respostas certas eram esquerda, direita, esquerda. A frase que orienta a aluna
    era FALSA, e nenhum gate via, porque cada metade estava bem formada.

    So varre a voz do MATERIAL. Dentro de um artefato ("the unit assessment is in the last
    session", no syllabus) a referencia posicional e o texto do documento, e fica."""
    fora = []
    for m in re.finditer(VOZ_DO_MATERIAL, ctx["tela"], re.S):
        t = html.unescape(re.sub(r"<[^>]+>", " ", m.group(0)))
        k = re.search(POSICIONAL, t, re.I)
        if k:
            fora.append(f"PRO-008: referencia posicional na voz do material — "
                        f"{k.group(0)!r} em {re.sub(chr(92)+'s+', ' ', t).strip()[:80]!r}. "
                        f"Aponte pelo rotulo: a ordem muda, o rotulo nao.")
    return fora


def r_regra_antes_da_tentativa(c, ctx):
    """SEQ-002 — a regra aparece antes de a aluna tentar.

    Guided discovery so e discovery se a tentativa vier primeiro. Mostrar a caixa de regra
    (`rule-box`) antes de qualquer tarefa da aula transforma descoberta em exposicao, e o
    resto da aula vira confirmacao do que ja foi dito."""
    fora = []
    telas = re.findall(r'<div class="slide[^"]*" data-slide="(\d+)" data-stage="\d+" '
                       r'data-lesson="(\d+)"(.*?)(?=<div class="slide[^"]*" data-slide=|$)',
                       ctx["tela"], re.S)
    por_aula = {}
    for n, aula, corpo in telas:
        por_aula.setdefault(aula, []).append((int(n), corpo))
    for aula, lista in por_aula.items():
        tentou = False
        for n, corpo in sorted(lista):
            if "rule-box" in corpo and not tentou:
                fora.append(f"SEQ-002: a aula {aula} mostra a caixa de regra na tela {n} "
                            f"sem nenhuma tentativa antes. A regra vem DEPOIS da tentativa.")
            if re.search(r"quiz-options|match-grid|pair-grid|blank-input|data-audgrupo", corpo):
                tentou = True
    return fora


def r_texto_corrompido(c, ctx):
    """REG-003 — fragmento de HTML vazou para o texto visivel.

    Sintoma de patch mecanico: entidade escapada duas vezes (`&amp;mdash;` aparece na tela
    como "&mdash;") ou marcacao literal no meio da frase. `&amp;` sozinho NAO conta: e o
    "e" comercial legitimo de "Listen & Watch", e acusa-lo daria doze falsos positivos no
    molde (medido)."""
    fora = []
    for m in re.finditer(r">([^<>]{2,})<", ctx["tela"]):
        t = m.group(1)
        if re.search(r"&amp;(amp|lt|gt|quot|nbsp|mdash|ndash|middot|rsquo|ldquo|rdquo|#\d+);"
                     r"|&lt;/?\w+&gt;", t):
            fora.append(f"REG-003: marcacao no texto visivel — {t.strip()[:70]!r}")
    return fora


def r_persistencia_ficticia(c, ctx):
    """REG-008 — a interface promete guardar e nao guarda.

    Botao que diz Save/Submit/Sync tem de chegar a alguma escrita real (`persSave`, o
    STORE, localStorage). Prometer historico e nao ter e pior que nao prometer: a aluna
    conta com o registro e ele nao existe."""
    fora = []
    for m in re.finditer(r"<button[^>]*>(.*?)</button>", ctx["tela"], re.S):
        rot = html.unescape(re.sub(r"<[^>]+>", " ", m.group(1))).strip()
        if not re.search(r"\b(save|submit|sync|upload|send)\b", rot, re.I):
            continue
        if not re.search(r"persSave|STORE|localStorage|storeSet|salva", m.group(0)):
            fora.append(f"REG-008: o botao {rot[:40]!r} promete guardar e nao chama "
                        f"nenhuma escrita.")
    return fora


def r_player_longe_da_resposta(c, ctx):
    """PRO-007 — o player e o controle de resposta em cartoes diferentes.

    A aluna ouve num lugar e responde noutro: perde o audio de vista, ou a pergunta. O
    player e a resposta da mesma tarefa vivem na MESMA seccao."""
    fora = []
    cortes = list(re.finditer(r'<div class="section-header-row"><h4>(.*?)</h4>',
                              ctx["tela"], re.S))
    for i, m in enumerate(cortes):
        fim = cortes[i + 1].start() if i + 1 < len(cortes) else len(ctx["tela"])
        tr = ctx["tela"][m.end():fim]
        if "data-audgrupo" not in tr:
            continue
        if not re.search(r"quiz-options|match-grid|pair-grid|blank-input|writebox|res-card", tr):
            tit = html.unescape(re.sub(r"<[^>]+>", " ", m.group(1))).strip()
            fora.append(f"PRO-007: a seccao {tit[:50]!r} tem player e nenhum controle de "
                        f"resposta — a tarefa da escuta esta noutro cartao.")
    return fora


def r_checkpoint_no_fim_do_bloco(c, ctx):
    """SEQ-006 — a ultima aula do bloco nao aponta para o checkpoint.

    O card da aula que fecha o bloco tem de dizer ao professor que o registro dela alimenta
    o checkpoint, e que o checkpoint le as aulas do bloco juntas. Sem isso o instrumento
    existe e ninguem o consulta na hora certa."""
    if not ctx["professor"]:
        return []
    ciclo = re.search(r"var CICLO=\{[^}]*primeira:(\d+)[^}]*porBloco:(\d+)", c)
    if not ciclo:
        return ["SEQ-006: nao consegui ler CICLO.primeira/porBloco para saber qual e a "
                "ultima aula do bloco."]
    ultima = int(ciclo.group(1)) + int(ciclo.group(2)) - 1
    card = re.search(r'data-lesson="%d"[^>]*data-teacher="([^"]*)"' % ultima, c)
    alvo = c[max(0, c.find('LESSONS')):]
    if not re.search(r"checkpoint", (card.group(1) if card else "") + alvo[:20000], re.I):
        return [f"SEQ-006: a aula {ultima} fecha o bloco e nao fala do checkpoint."]
    return []


REGRAS = [
    r_resposta_previsivel, r_referencia_posicional, r_regra_antes_da_tentativa,
    r_texto_corrompido, r_persistencia_ficticia, r_player_longe_da_resposta,
    r_checkpoint_no_fim_do_bloco,r_transcript_fechado, r_player_fora_do_listening, r_postclass_sem_exercicio,
          r_postclass_componentes, r_bloco1_diagnostico, r_ciclo_declarado,
          r_metadado_interno, r_elenco_consistente, r_avaliacao_declarada,
          r_recurso_duplicado]


def confere(caminho):
    c = open(caminho, encoding="utf-8").read()
    if carimbo(c) != ANATOMIA:
        return False, []
    ctx = {"tela": sem_codigo(c), "texto": texto_do_aluno(c),
           "aulas": aulas_de(c), "professor": eh_professor(c)}
    erros = []
    for regra in REGRAS:
        erros.extend(regra(c, ctx))
    return True, erros


def alvos_padrao():
    fora = []
    for p in sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")) +
                    glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html"))):
        try:
            with open(p, encoding="utf-8") as f:
                if carimbo(f.read(4000)) == ANATOMIA:
                    fora.append(p)
        except OSError:
            pass
    return fora


def _confere_texto(t):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(t)
        p = f.name
    try:
        return confere(p)
    finally:
        os.unlink(p)


def _selftest():
    prof = os.path.join(RAIZ, "public", "professor", "stephanie-vicente.html")
    alu = os.path.join(RAIZ, "public", "aluno", "stephanie-vicente.html")
    if not (os.path.exists(prof) and os.path.exists(alu)):
        print("SELFTEST INCONCLUSIVO — o molde nao esta no lugar.")
        return 1
    limpo_p = open(prof, encoding="utf-8").read()
    limpo_a = open(alu, encoding="utf-8").read()
    for rot, t in (("professor", limpo_p), ("aluno", limpo_a)):
        _, e = _confere_texto(t)
        if e:
            print(f"SELFTEST INCONCLUSIVO — o molde ({rot}) JA esta reprovando:")
            for x in e:
                print("   ", x)
            return 1

    casos = [
        ("PRO-006 transcript nasce aberto", limpo_p,
         lambda s: s.replace('class="transcript-box" style="display:none"',
                             'class="transcript-box"', 1), "PRO-006"),
        ("ANA-012 player no pre-class de Reading", limpo_p,
         lambda s: s.replace('<div id="pc1">',
                             '<div id="pc1"><button onclick="say(\'x\',1)">L</button>', 1),
         "ANA-012"),
        ("ANA-003 ciclo com 12 aulas", limpo_p,
         lambda s: re.sub(r"(var CICLO=\{[^}]*aulas:)\d+", r"\g<1>12", s, count=1), "ANA-003"),
        ("ANA-004 bloco 1 sem ESP", limpo_p,
         lambda s: s.replace("mod:'ESP'", "mod:'Reading'", 1), "ANA-004"),
        ("REG-002 personagem do elenco que nao aparece", limpo_p,
         lambda s: s.replace('{n:"Rachel",g:"f"}', '{n:"Zoraide",g:"f"}', 1), "REG-002"),
        ("INT-018 metadado interno na tela do ALUNO", limpo_a,
         lambda s: s.replace("</body>", "<p>Hipótese a validar pelo gerador</p></body>", 1),
         "INT-018"),
        ("AUT-003 aula de teste sem avaliacao formal declarada", limpo_p,
         # NAO tira "Acompanhamento docente": sem modelo declarado a ANA-002 dispara e
         # retorna antes, e a AUT-003 nunca seria exercitada. A mutacao tem de isolar o
         # defeito que ela quer provar.
         lambda s: s.replace("mod:'ESP'", "mod:'Teste'", 1), "AUT-003"),
        ("ANA-002 nenhum modelo declarado", limpo_p,
         lambda s: s.replace("Acompanhamento docente", "—"), "ANA-002"),
        ("ANA-015 mesmo link duas vezes no post-class", limpo_p,
         lambda s: re.sub(r'(<div[^>]*id="tab-postclass"[^>]*>)',
                          r'\1<a href="https://exemplo.com/x">a</a><a href="https://exemplo.com/x">b</a>',
                          s, count=1), "ANA-015"),        ("PRO-009 matching binario alternando", limpo_p,
         # `se3` e binario; devolve a alternancia perfeita que o molde tinha
         lambda s: re.sub(r'(<div class="match-grid" id="se3">.*?)(?=<button)',
                          lambda g: re.sub(r'data-ok="[AB]"',
                                           lambda h, c=[0]: (c.__setitem__(0, c[0] + 1) or
                                                             'data-ok="%s"' % "AB"[(c[0] - 1) % 2]),
                                           g.group(1)), s, count=1, flags=re.S), "PRO-009"),
        ("PRO-009 grade que nao fecha", limpo_p,
         # quebra o fechamento de UMA grade: a leitura por aninhamento passa a nao fechar,
         # e o guarda de cobertura tem de acusar em vez de dar OK com menos grades
         # uma grade cujo `</div>` nao existe: o corpo vira o resto do documento, e
         # qualquer chave lida dali e de outra coisa. Antes desta regra isso passava calado.
         lambda s: s.replace("</body>",
                             '<div class="match-grid" id="zz"><div class="match-row">'
                             '<span class="match-word">x</span>'
                             '<select data-ok="A"><option value="A">a</option></select>'
                             '</div></body>', 1),
         "nao fecha"),
        ("PRO-009 chave na ordem das opcoes", limpo_p,
         # devolve `nt4` a permutacao identidade: item 1 -> A, item 2 -> B, item 3 -> C
         lambda s: re.sub(r'(<div class="match-grid" id="nt4">.*?)</div>\s*<button',
                          lambda g: re.sub(r'data-ok="[A-J]"',
                                           lambda h, c=[0]: (c.__setitem__(0, c[0] + 1) or
                                                             'data-ok="%s"' % "ABC"[c[0] - 1]),
                                           g.group(1)) + '</div>\n    <button',
                          s, count=1, flags=re.S), "PRO-009"),
        ("PRO-009 par sempre do mesmo lado", limpo_p,
         lambda s: re.sub(r'(<div class="pair-grid" id="pp1">.*?)</div>\s*<button',
                          lambda g: g.group(1).replace('data-ok="b"', 'data-ok="a"')
                          + '</div>\n    <button', s, count=1, flags=re.S), "PRO-009"),
        ("PRO-008 gabarito aponta por posicao", limpo_p,
         lambda s: s.replace('<div class="rationale">',
                             '<div class="rationale">The one that matters is the third. ', 1),
         "PRO-008"),
        ("SEQ-002 regra antes de qualquer tentativa", limpo_p,
         lambda s: re.sub(r'(<div class="slide[^"]*" data-slide="2" data-stage="\d+" '
                          r'data-lesson="1"[^>]*>)',
                          r'\1<div class="callout rule-box">Rule first</div>', s, count=1),
         "SEQ-002"),
        ("REG-003 entidade escapada duas vezes", limpo_a,
         lambda s: s.replace("</body>", "<p>uma coisa &amp;mdash; outra</p></body>", 1),
         "REG-003"),
        ("REG-008 botao promete guardar e nao guarda", limpo_a,
         lambda s: s.replace("</body>", '<button onclick="nada()">Save</button></body>', 1),
         "REG-008"),
        ("PRO-007 player sem controle de resposta na seccao", limpo_a,
         lambda s: s.replace("</body>",
                             '<div class="section-header-row"><h4>9 &middot; Solto</h4></div>'
                             '<div data-audgrupo="9"><button>Play</button></div></body>', 1),
         "PRO-007"),
        ("SEQ-006 ultima aula do bloco sem checkpoint", limpo_p,
         lambda s: s.replace("checkpoint", "revisao"), "SEQ-006"),

    ]
    falhou = False
    for nome, base, muta, esperado in casos:
        _, errs = _confere_texto(muta(base))
        bom = any(esperado in e for e in errs)
        print(f"  {'OK  ' if bom else 'FALHA'}  {nome:44} "
              f"{(errs[0][:56] if errs else 'nao acusou nada')}")
        if not bom:
            falhou = True
    print()
    if falhou:
        print("SELFTEST FALHOU — alguma regra parou de morder.")
        return 1
    print(f"SELFTEST OK — {len(casos)} defeitos do catalogo, todos pegos.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    alvos = [a for a in sys.argv[1:] if a.endswith(".html")] or alvos_padrao()
    print(f"=== GATE 41 — catalogo do auditor (anatomia {ANATOMIA}) ===")
    total = vistos = 0
    for a in alvos:
        if not os.path.exists(a):
            continue
        aplicou, erros = confere(a)
        if not aplicou:
            continue
        vistos += 1
        rel = os.path.relpath(a, RAIZ)
        if erros:
            total += len(erros)
            print(f"{VERMELHO}FAIL{ZERA}  {rel}")
            for e in erros:
                print(f"        {e}")
        else:
            print(f"{VERDE}ok{ZERA}    {rel}  ({len(REGRAS)} regras)")
    print()
    if total:
        print(f"{VERMELHO}GATE 41 — {total} problema(s) em {vistos} arquivo(s).{ZERA}")
        return 1
    print(f"GATE 41 OK — {vistos} arquivo(s), {len(REGRAS)} regras do catalogo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
