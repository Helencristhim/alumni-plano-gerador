#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 18 — os shells nao derivam no que TEM de ser igual.

POR QUE ISTO EXISTE (07/08/2026)
--------------------------------
Ate hoje havia UM shell (`public/professor/helen-mendes-aula1.html`): o builder clonava
ele para todo mundo, e um conserto de estrutura chegava em todos os modelos de graca. Essa
propriedade e o que faz o sistema aguentar 1.221 aulas.

O molde stephanie-vicente precisa de outra ANATOMIA DE ABAS (entra Syllabus, entra
Evidencias, sai Complementares). Mexer nisso no shell compartilhado durante a construcao
significa editar o arquivo do qual descende tudo o que ja esta no ar. Decisao do Dan
(07/08/2026): clonar, **temporariamente**, para poder mexer sem afetar a helen.

    "precisamos clonar, temporariamente, um shell pra stephanie pra podermos modifica-lo
     sem afetar o da helen"

O RISCO, DITO SEM RODEIO
------------------------
"Temporario" e a palavra que mais mente em software. Fork temporario vira permanente no dia
em que um conserto entra num shell e nao no outro — e ninguem percebe, porque os DOIS
continuam funcionando. O defeito so aparece meses depois, num aluno, num clique.

Este gate transforma "temporario" de intencao em medicao: enquanto os dois shells
existirem, o CI garante que eles nao derivam NO QUE IMPORTA.

O QUE TEM DE SER IGUAL (e este gate cobra)
------------------------------------------
  - o conjunto de FUNCOES JS. Sao elas que fazem o material funcionar: speakText,
    updateProgress, saveState/loadState, startRecording, checkBlank... Uma funcao que
    existe num shell e nao no outro e um botao morto esperando a vez.
  - as CLASSES-MECANISMO no CSS. Se `.speech-result.show` existe num e nao no outro, o
    exercicio conta progresso num molde e nao conta no outro.

O QUE PODE DIFERIR (declarado, nao tolerado por omissao)
--------------------------------------------------------
Toda diferenca legitima entra em DIFERENCAS_ACEITAS com o motivo escrito. Diferenca que
nao esta na lista REPROVA. E isso que impede o fork de crescer no escuro.

    O DIA DA UNIFICACAO E VISIVEL: e quando DIFERENCAS_ACEITAS encolhe a zero.

USO:
    python3 scripts/check_shell_drift.py
    python3 scripts/check_shell_drift.py --selftest
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cada PAR: (shell da anatomia imersivo, clone da anatomia nova). Sao dois pares — a AULA
# e o HUB — porque as duas coisas foram clonadas e as duas podem derivar.
#
# A ANATOMIA story-quest (molde kids joaozinho) NAO ENTRA AQUI, e e de proposito.
# Este gate existe para CLONE: o guided-discovery nasceu copiando o helen-mendes, entao os
# dois TEM de ter o mesmo conjunto de funcoes e classes-mecanismo, e toda diferenca e
# suspeita ate ser declarada. A story-quest nao e clone de ninguem — ela e derivada, por
# script, de um artefato escrito fora do sistema, com outro vocabulario inteiro (flip-tile,
# story-frame, unj-chip...). Compara-la com o helen-mendes produziria centenas de
# "divergencias" que sao simplesmente a forma dela, e a lista de excecoes viraria ruido —
# que e o oposto do que este arquivo serve.
#
# O que cobra a story-quest e outro par de gates: o GATE 20 (o shell tem o que a anatomia
# declara) e o --check do extrator (o shell continua sendo o artefato). O que este gate
# protegeria e que ela ainda NAO tem — saveState/loadState/updateProgress/startRecording e
# os 4 scripts de Supabase (REGRA 28) — esta declarado no anatomias.json, no campo
# `_falta_a_camada_de_producao`, e tem de entrar antes de qualquer material de aluno.
# A ANATOMIA private-black (molde adulto novo, artefato do Marcos) TAMBEM NAO ENTRA, e
# pela MESMA razao da story-quest, dita de outro jeito: ela nao e clone. O shell dela e
# extraido de `_build/model/artefatos/marcos-private-black.html` -- outro vocabulario inteiro
# (callout, quiz-option, reveal-item, pair-opt, aud-stop, ak-*, mini-*), outro registro
# (ARTEFATO/ALUNO/CICLO/LESSONS/GUIDE) e outra anatomia de abas.
#
# E aqui a exclusao nao e so economia de ruido: enquanto este gate alcançasse o shell novo,
# ele OBRIGARIA o molde novo a ter as funcoes do imersivo -- isto e, seria o cano por onde os
# defeitos da helen entrariam, que e exatamente o que a fronteira do private-black existe para
# impedir. Ver docs/private-black/FRONTEIRA.md.
#
# O que cobra o private-black e outro conjunto: GATE 20 (o shell tem o que a anatomia
# declara), GATE 21 (a interface e a do artefato) e a suite P3 (navegador + mutacao).
PARES = [
    (os.path.join(RAIZ, "public", "professor", "helen-mendes-aula1.html"),
     os.path.join(RAIZ, "_build", "model", "shells", "guided-discovery.html")),
    (os.path.join(RAIZ, "public", "professor", "helen-mendes.html"),
     os.path.join(RAIZ, "_build", "model", "shells", "hub-guided-discovery.html")),
]
BASE = PARES[0][0]

# Funcoes que so fazem sentido numa das anatomias. Motivo OBRIGATORIO.
DIFERENCAS_ACEITAS = {
    "hub-guided-discovery.html": {
        # A aba Evidencias e a unica que traz JS proprio: e a ficha pos-aula + o checkpoint
        # da aula 4. A anatomia imersivo nao tem essa aba, entao nao tem essas funcoes.
        "funcoes_a_mais": {
            "icCpKey":   "aba Evidencias — ficha pos-aula (chave de persistencia)",
            "icCpLoad":  "idem",
            "icCpTick":  "idem (marcar item do checkpoint)",
            "icCpScore": "idem (contagem de concluidos)",
        },
        "funcoes_a_menos": {},
        "classes_a_menos": {},
        "classes_a_mais": {
            "syl-block": "aba Syllabus 20 aulas — nao existe na anatomia da helen",
            "evi-field": "aba Evidencias (ficha pos-aula + checkpoint) — idem",
            "ic-cp":     "o checklist do checkpoint, dentro da aba Evidencias",
        },
    },
    "guided-discovery.html": {
        # ══ O CHASSI DOS DOIS MOLDES E SEPARADO, POR DECISAO (11/08/2026) ══════════════
        # Palavras do Dan: "os dois moldes devem ser separados mesmo, em si".
        # O chassi do guided-discovery (.slide, .slide-inner, .slide-title, .slide-heading,
        # .chapter-label, .slide-subtitle, .slide-image::before, .audio-btn-sm,
        # .roleplay-card, .roleplay-kw, .stage-pill) passou a sair do ARTEFATO
        # (_build/model/artefatos/erica-professor-view.html), byte a byte. O chassi do
        # imersivo NAO MUDOU — nenhum aluno do molde antigo foi tocado.
        #
        # ESTE GATE NAO PEGA ISSO, e e de proposito: ele compara PRESENCA de funcao e de
        # classe entre os dois shells, nao o VALOR das regras. Um max-width revertido de
        # 940 para 920 passaria por aqui sem um pio. Quem tranca o valor do chassi e o
        # GATE 21 (scripts/check_artefato_paridade.py -> CHASSI), que compara o clone com
        # o artefato e tem selftest para isso.
        #
        # Consequencia pratica: NAO tente "unificar" o chassi dos dois shells. As classes
        # continuam com o mesmo NOME nos dois (por isso este gate segue verde); o que
        # diverge sao os VALORES, e isso agora e desenho, nao deriva.

        # As abas novas nao pediram JS nenhum — switchTab() ja e generico. O que pediu foi a
        # MECANICA de sorting, que a anatomia imersivo nao tem: la o Guided Discovery
        # acontece por reveal, aqui por classificacao em colunas. Portada do artefato da
        # Stephanie (.sortbox/.sortcol/.sortitem), corrigindo dois defeitos do original:
        # saida em portugues na tela do aluno e estado global (so cabia UM por aula).
        #
        # Se um dia o imersivo tambem precisar de sorting, estas quatro sobem para o shell
        # base e saem daqui — e a lista encolhe, que e a direcao certa.
        "funcoes_a_mais": {
            "icSortPaint": "mecanica sorting — nao existe na anatomia imersivo",
            "icSortMove":  "idem",
            "icSortCheck": "idem",
            "icSortReset": "idem",
            "icCallStop":  "call player — a anatomia imersivo toca UM arquivo; aqui a call e uma sequencia de turnos com falante",
            "icCallMark":  "idem (destaque de quem fala)",
            "icCallPlay":  "idem (recorte por segmento: a call inteira, so as apresentacoes, so a agenda)",
            "icWhyShow":    "racional por item — revela o porque DEPOIS de a aluna arriscar",
            "icTimerFmt":   "cronometro — o tempo como parte da tarefa",
            "icTimerRender":"idem",
            "icTimerStart": "idem",
            "icTimerReset": "idem",
            "icWriteSave": "area de escrita — o quadro de feedback tem CAMPO, nao so rotulo; a anatomia imersivo nao tem",
            "icPick":      "quiz-option do artefato: marca correct/wrong e revela o .rationale do item",
            "icSave":       "recap-item do artefato: o check do fecho, persistido",
            "icConfPick":  "conf-btn do artefato: uma escolha por .conf-scale + contador em .score-out",
            "icReveal":    "verify-all-btn do artefato: revela o .rationale seguinte (gabarito teacher-led)",
        },
        "funcoes_a_menos": {
            # A migracao de 11/08/2026 trocou as classes .ic-* pelas DO ARTEFATO
            # (_build/model/artefatos/erica-professor-view.html), e com elas os handlers:
            # o mecanismo passou a ser o do artefato, nao uma reimplementacao.
            "icPickGist":     "virou icPick() sobre .quiz-option/.rationale, a forma do artefato",
            "icRevealTf":     "o true/false passou a ser quiz-item + rationale, a forma do artefato",
            "icToggleAnswer": "o gabarito passou a ser .callout.rule-box + .rationale, revelado por icReveal()",
            "icToggleText":   "sem uso: nenhum bloco emitia o handler depois da migracao",
        },
        # O CSS de media-card continua nos DOIS shells: sai a ABA, nao a regra. Remover CSS
        # do clone seria deriva sem ganho — e reintroduzi-lo depois, na unificacao, e
        # trabalho a toa. Por isso nao ha classes_a_menos.
        "classes_a_menos": {
            "ic-tag": "o status na tela (Conditional/Extension) passou a usar .cond-tag/.ext-tag, "
                      "as classes DO ARTEFATO, na migracao de 11/08/2026.",
        },
        "classes_a_mais": {
            "syl-block": "aba Syllabus 20 aulas — nao existe na anatomia da helen",
            "evi-field": "aba Evidencias (ficha pos-aula + checkpoint) — idem",
            "ic-call":   "call player — mecanica de Listening into Interaction",
            "ic-spk":    "idem (o falante em destaque)",
            "ic-sortbox":"mecanica sorting",
            "ic-self":   "autoavaliacao de confianca no fecho",
            "ic-reveal": "cartao que vira (frente/verso) — o componente mais usado do artefato; o imersivo revela por accordion, que e outra pedagogia",
            "ic-evi":    "evidencia com a fonte que a sustenta",
            "ic-recap":  "recapitulacao do que a aula construiu",
            "ic-write":  "area de escrita — o quadro de feedback com campo de verdade",
            "ic-q":      "pergunta com subprompt (a instrucao de COMO responder)",
            "ic-phrase": "frase com a funcao que ela cumpre, lado a lado",
            "ic-why":    "racional por item, escondido ate a professora revelar",
            "ic-timer":  "cronometro — o tempo como parte da tarefa",
        },
    }
}

# Classes-mecanismo: se existem num shell e nao no outro, um exercicio deixa de funcionar
# ou de contar progresso naquele molde.
CLASSES_MECANISMO = [
    "vocab-card-pc", "match-row", "blank-input", "quiz-item", "quiz-option",
    "speech-card", "speech-result", "order-container", "order-item", "think-card",
    "lesson-card", "lesson-body", "mini-bar-fill", "slides-wrapper", "slide",
    "nav-bar", "lp-seekbar", "dialogue-line", "audio-btn", "btn-your-pronunciation",
    "syl-block", "evi-field", "ic-call", "ic-spk", "ic-sortbox", "ic-self", "ic-cp",
    "ic-reveal", "ic-tag", "ic-evi", "ic-recap", "ic-write", "ic-q", "ic-phrase",
    "ic-why", "ic-timer",
]


def le(p):
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def funcoes(html):
    return set(re.findall(r"function\s+([A-Za-z_$][\w$]*)\s*\(", html))


def classes_presentes(html):
    return {c for c in CLASSES_MECANISMO
            if re.search(r"[.\"' ]" + re.escape(c) + r"[\s{.,:\"']", html)}


def compara(base_html, clone_html, nome, aceitas):
    erros = []
    fb, fc = funcoes(base_html), funcoes(clone_html)

    a_mais = fc - fb
    a_menos = fb - fc
    ok_mais = set(aceitas.get("funcoes_a_mais", {}))
    ok_menos = set(aceitas.get("funcoes_a_menos", {}))

    for f in sorted(a_menos - ok_menos):
        erros.append(
            f"{nome}: funcao '{f}()' existe no shell da helen e NAO no clone. "
            f"Ou o clone perdeu um conserto, ou a diferenca e legitima e falta declarar "
            f"em DIFERENCAS_ACEITAS['funcoes_a_menos'] com o motivo."
        )
    for f in sorted(a_mais - ok_mais):
        erros.append(
            f"{nome}: funcao '{f}()' existe no clone e NAO no shell da helen. "
            f"Se e conserto, tem de subir para o shell base; se e da anatomia nova, "
            f"declare em DIFERENCAS_ACEITAS['funcoes_a_mais'] com o motivo."
        )

    cb, cc = classes_presentes(base_html), classes_presentes(clone_html)
    ok_cmais = set(aceitas.get("classes_a_mais", {}))
    ok_cmenos = set(aceitas.get("classes_a_menos", {}))
    for c in sorted((cb - cc) - ok_cmenos):
        erros.append(
            f"{nome}: classe-mecanismo '.{c}' sumiu no clone. Exercicio que depende dela "
            f"deixa de funcionar (ou de contar progresso) so neste molde."
        )
    for c in sorted((cc - cb) - ok_cmais):
        erros.append(f"{nome}: classe-mecanismo '.{c}' so existe no clone e nao foi declarada.")

    return erros


def roda():
    if not os.path.exists(BASE):
        print(f"shell base nao encontrado: {BASE}")
        return 1
    erros, checados = [], 0
    for base, clone in PARES:
        if not (os.path.exists(base) and os.path.exists(clone)):
            continue  # clone ainda nao existe — nada a comparar
        nome = os.path.basename(clone)
        erros += compara(le(base), le(clone), nome, DIFERENCAS_ACEITAS.get(nome, {}))
        checados += 1

    print("=== GATE 18 — deriva entre shells ===")
    if not checados:
        print("nenhum clone no disco — nada a comparar (shell unico, estado ideal).")
        return 0
    n_dif = sum(len(v.get(k, {})) for v in DIFERENCAS_ACEITAS.values()
                for k in ("funcoes_a_mais", "funcoes_a_menos", "classes_a_mais", "classes_a_menos"))
    print(f"{checados} clone(s) comparado(s); {n_dif} diferenca(s) declarada(s) como legitima(s).")
    print("O dia da unificacao e quando esse numero chegar a zero.")
    if erros:
        for e in erros:
            print(f"  ERRO  {e}")
        print(f"\n{len(erros)} deriva(s) nao declarada(s).")
        return 1
    print("OK — os shells nao derivam no que tem de ser igual.")
    return 0


def selftest():
    if not os.path.exists(BASE):
        print("SELFTEST INCONCLUSIVO — shell base ausente")
        return 1
    base_html = le(BASE)
    casos = [
        ("funcao sumida no clone",
         base_html.replace("function updateProgress(", "function __sumiu__(", 1),
         "existe no shell da helen e NAO no clone"),
        ("funcao nova nao declarada",
         base_html + "\n<script>function inventadaAqui(){}</script>",
         "e NAO no shell da helen"),
        ("classe-mecanismo sumida",
         base_html.replace("speech-result", "xxx-removida"),
         "sumiu no clone"),
    ]
    falhou = False
    for rotulo, mutante, esperado in casos:
        erros = compara(base_html, mutante, "mutante.html", {})
        pegou = any(esperado in e for e in erros)
        print(f"  {'OK  ' if pegou else 'FALHA'}  {rotulo}")
        if not pegou:
            falhou = True
            print(f"         esperava {esperado!r}; veio: {erros[:2]}")

    # O clone so pode alcancar quem tem shell proprio. Se um refactor no builder trocar a
    # escolha por slug por escolha por framework (ou por model), TODO aluno daquele
    # framework herdaria a anatomia nova no proximo rebuild — inclusive quem ja tem aula no
    # ar. Esta parte do selftest e o que impede isso de passar despercebido.
    print("\n  isolamento do clone (shell_path do builder):")
    try:
        import importlib.util
        alvo = os.path.join(RAIZ, "_build", "model", "build_from_model.py")
        spec = importlib.util.spec_from_file_location("_bfm", alvo)
        bfm = importlib.util.module_from_spec(spec)
        argv, sys.argv = sys.argv, ["x"]
        try:
            spec.loader.exec_module(bfm)
        finally:
            sys.argv = argv
        casa = "helen-mendes-aula1.html"
        for slug, esperado in [
            ("helen-mendes", casa), ("bento", casa), ("theo", casa),
            ("ana-claudia-veraldi-v2", casa), ("", casa),
            ("stephanie-vicente", "guided-discovery.html"),
        ]:
            got = os.path.basename(bfm.shell_path({"slug": slug} if slug else {}))
            ok = got == esperado
            print(f"    {'OK  ' if ok else 'FALHA'}  slug={slug or '(vazio)':24} -> {got}")
            falhou |= not ok
    except Exception as e:
        print(f"    FALHA  nao consegui checar shell_path: {e}")
        falhou = True

    if falhou:
        print("\nSELFTEST FALHOU — o gate parou de morder.")
        return 1
    print("\nSELFTEST OK — derivas pegas e clone isolado a quem tem shell proprio.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else roda())
