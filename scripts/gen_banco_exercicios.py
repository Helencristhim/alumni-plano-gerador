#!/usr/bin/env python3
"""Gera public/data/exercicios.json — o BANCO DE EXERCÍCIOS que o builder sabe emitir.

POR QUE ISTO EXISTE
-------------------
O editor de frameworks do catálogo precisa oferecer uma lista de exercícios pra você
escolher. Essa lista NÃO pode ser digitada em lugar nenhum: uma lista paralela ao
builder diverge dele no primeiro dia — o catálogo passa a oferecer exercício que o
builder não monta, você monta um framework com ele, e a aula quebra na geração.

Então o banco é PROVADO, não declarado: para cada exercício, este script chama o
`render_block()` DO PRÓPRIO BUILDER com uma amostra e guarda as classes CSS que
saíram. Se o builder perder um exercício, a chamada falha aqui. Se o builder GANHAR
um exercício e ninguém escrever a amostra, o confronto com o código-fonte acusa.

O único texto humano é o rótulo e a descrição de cada exercício (AMOSTRAS abaixo) —
o que o exercício É, e não se ele existe.

Uso:  python3 scripts/gen_banco_exercicios.py [--check]
      --check falha (exit 1) se o JSON no disco estiver desatualizado (usado no CI).
"""

import argparse
import json
import os
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "public" / "data" / "exercicios.json"
BUILDER = RAIZ / "_build" / "model" / "build_from_model.py"

sys.path.insert(0, str(BUILDER.parent))
import build_from_model as B  # noqa: E402

# ── AS AMOSTRAS ───────────────────────────────────────────────────────────────
# Uma por exercício: o payload MÍNIMO que o builder aceita. Serve a três coisas ao
# mesmo tempo: prova que o exercício existe, revela as classes que ele emite (o que
# permite os gates casarem contrato × HTML), e documenta a forma do config.
#
# "grupo" é só pra UI do editor agrupar. "interativo" = o aluno clica e algo acontece.
AMOSTRAS = [
    ("reading", "Texto de leitura", "Texto central da aula, em parágrafos, com fonte opcional.",
     "input", False, {"kind": "reading", "rtitle": "The Title",
                      "paras": ["First paragraph.", "Second paragraph."],
                      "source": "The Guardian", "link": "https://example.com"}),
    ("gist", "Gist (achar a ideia principal)", "Três opções, uma é a ideia central do texto. Clique revela.",
     "compreensao", True, {"kind": "gist", "prompt": "What is the main idea?",
                           "choices": [["A", "The wrong one.", False],
                                       ["B", "The main idea.", True]]}),
    ("tf", "True / False com justificativa", "Afirmações sobre o texto; o clique revela veredito e a linha que prova.",
     "compreensao", True, {"kind": "tf", "items": [["The meeting was short.", "t", "line 3"]]}),
    ("questions", "Perguntas abertas", "Lista de perguntas, numerada ou com marcador.",
     "compreensao", False, {"kind": "questions", "title": "Think about it",
                            "items": ["Why did it happen?", "What would you do?"]}),
    ("guiding", "Perguntas guia", "As perguntas que conduzem a leitura/escuta antes da exposição.",
     "compreensao", False, {"kind": "guiding", "items": ["Who is speaking?"]}),
    ("analyse", "Analyse (numerada)", "Roteiro de análise da linguagem, sempre numerado.",
     "linguagem", False, {"kind": "analyse", "items": ["Underline the modal verbs."]}),
    ("matching", "Matching (palavra ↔ definição)", "Duas colunas clicáveis com gabarito e contador de acertos.",
     "vocabulario", True, {"kind": "matching", "title": "Match them",
                           "words": [["1", "deadline", "A"], ["2", "budget", "B"]],
                           "defs": [["A", "the last possible day"], ["B", "the money available"]]}),
    ("gapfill", "Gap-fill com banco", "Texto com lacunas + banco de palavras (embaralhado pelo builder).",
     "vocabulario", False, {"kind": "gapfill",
                            "parts": ["We need to ", ["1"], " the deadline.", ["2"], "."],
                            "bank": ["extend", "confirm"]}),
    ("bank", "Banco de linguagem útil", "Chips com as expressões de apoio da tarefa.",
     "vocabulario", False, {"kind": "bank", "label": "Useful language",
                            "items": ["I'd rather...", "What if we..."]}),
    ("vocabnote", "Nota de vocabulário", "Uma observação curta sobre uma palavra ou expressão.",
     "vocabulario", False, {"kind": "vocabnote", "text": "'Deadline' is countable."}),
    ("modals", "Guia de significado (modais)", "Cards comparando força/sentido — must, should, might.",
     "linguagem", False, {"kind": "modals", "title": "How strong?",
                          "cards": [["must", "strong", "No choice."]]}),
    ("lf", "Language focus (linha a linha)", "Frases com a estrutura-alvo destacada no meio.",
     "linguagem", False, {"kind": "lf", "title": "Read the advice",
                          "items": [["Advice", "You ", "should", " rest.", "strong"]]}),
    ("rephrase", "Rephrase (reescrever)", "Frase + pista entre parênteses e uma lacuna pra reescrever.",
     "producao", False, {"kind": "rephrase", "title": "Say it again",
                         "items": [["It is required.", "must"]]}),
    ("scenarios", "Cenários", "Situações curtas com o papel de quem fala.",
     "producao", False, {"kind": "scenarios",
                         "items": [["A client", "asks for a discount at the last minute."]]}),
    ("quickfire", "Quick Fire", "Uma situação por tela, com Tips que abrem e fecham, e contador.",
     "producao", True, {"kind": "quickfire",
                        "items": [{"situation": "Your flight is delayed.",
                                   "tips": ["Could you tell me...?"]}]}),
    ("whiteboard", "Lousa em branco", "Caixa vazia pro professor escrever a correção diferida.",
     "feedback", False, {"kind": "whiteboard", "label": "Focus on form"}),
    ("answer", "Gabarito (abre e fecha)", "Chave de respostas escondida atrás de um clique.",
     "feedback", True, {"kind": "answer", "title": "Reveal answer key", "key": ["extend"]}),
    ("followup", "Follow-up", "A pergunta que estica a resposta do aluno.",
     "producao", False, {"kind": "followup", "text": "And why do you think that is?"}),
]


# ── COMPONENTES DO SHELL ──────────────────────────────────────────────────────
# Nem todo exercício passa pelo render_block. O coração da aula padrão — vocab
# reveal, diálogo, player de listening, role-play — vem do SHELL do modelo
# (public/professor/helen-mendes-aula1.html), não dos inclass_blocks. Sem eles no
# banco, o contrato do framework de produção sairia VAZIO e o editor não teria o que
# oferecer pra montar uma aula normal.
#
# A prova aqui é outra, e mais fraca de propósito: a classe TEM de existir no shell
# do modelo (CSS + handler). Não dá pra "executar" um componente de template como se
# executa render_block, então o que se prova é que o molde sabe montá-lo.
COMPONENTES_SHELL = [
    ("vocab-reveal", "Vocab reveal", "Card que esconde a palavra atrás de uma dica e abre no clique.",
     "vocabulario", True, "vocab-card"),
    ("dialogo", "Diálogo line-by-line", "Falas que aparecem uma a uma, com voz por personagem.",
     "input", True, "dialogue-line"),
    ("listening-player", "Listening com player", "Player completo: seekbar, ±5s e velocidade no próprio slide.",
     "input", True, "lp-seekbar"),
    ("slide-tarefa", "Slide de tarefa", "As perguntas ANTES da exposição (REGRA 2.2).",
     "compreensao", False, "comp-q-task"),
    ("slide-predicao", "Slide de predição", "Primeira escuta só pra arriscar do que se trata (REGRA 2.3).",
     "compreensao", False, "ic-predict"),
    ("fill-blank", "Fill-in-the-blank", "Lacuna que confere a resposta no clique.",
     "vocabulario", True, "fill-item"),
    ("spot-error", "Spot the error", "Frase errada que vira certa no clique.",
     "linguagem", True, "error-card"),
    ("role-play", "Role-play", "Cenário com papéis e chips de apoio: guiado, semi-livre, livre.",
     "producao", False, "roleplay-scenario"),
    ("survival", "Survival card", "As 5 frases-chave da aula, com áudio.",
     "feedback", True, "survival-item-ic"),
    ("checklist", "What I learned", "Checkboxes do fim da aula — é o que marca a aula como dada.",
     "feedback", True, "check-item"),
]


def prova_shell():
    """Confere que cada componente do shell existe MESMO no molde. Se alguém 'limpar'
    uma classe do modelo, o banco para de oferecer o componente em vez de o editor
    prometer o que o builder não entrega."""
    shell = (RAIZ / "public" / "professor" / f"{B.MODEL}-aula1.html").read_text(
        encoding="utf-8", errors="replace")
    out = []
    for cid, label, desc, grupo, inter, classe in COMPONENTES_SHELL:
        assert re.search(r'[\s"\.]' + re.escape(classe) + r'[\s"{,:\.]', shell), (
            f'componente "{cid}": a classe .{classe} não existe mais no shell do modelo '
            f'({B.MODEL}-aula1.html). Ou o modelo perdeu o componente, ou o id da classe '
            f'mudou — nos dois casos o banco não pode continuar oferecendo isto.')
        out.append({
            "id": cid, "label": label, "descricao": desc, "grupo": grupo,
            "interativo": inter, "origem": "shell", "classes": [classe], "campos": [],
        })
    return out


def kinds_do_builder():
    """Os `kind` que o render_block realmente trata, lidos do CÓDIGO-FONTE.
    Serve pra pegar o caso perigoso: builder ganhou exercício novo e o banco não sabe."""
    src = BUILDER.read_text(encoding="utf-8")
    corpo = src[src.find("def render_block("):src.find("def expand_inclass_blocks(")]
    achados = set()
    for m in re.finditer(r"if k(?:ind)?\s*==\s*'([a-z]+)'", corpo):
        achados.add(m.group(1))
    for m in re.finditer(r"if k(?:ind)?\s+in\s*\(([^)]+)\)", corpo):
        achados.update(re.findall(r"'([a-z]+)'", m.group(1)))
    return achados


def coleta():
    do_builder = kinds_do_builder()
    nas_amostras = {a[0] for a in AMOSTRAS}

    faltando = do_builder - nas_amostras
    assert not faltando, (
        f"o builder emite {sorted(faltando)} e o banco não tem amostra pra isso. "
        f"Acrescente em AMOSTRAS — senão o editor do catálogo nunca vai oferecer "
        f"esse exercício, e ele fica invisível pra quem monta framework.")
    sobrando = nas_amostras - do_builder
    assert not sobrando, (
        f"o banco lista {sorted(sobrando)}, que o render_block NÃO trata mais. "
        f"Banco que promete exercício inexistente quebra a aula na geração.")

    exercicios = []
    for eid, label, desc, grupo, interativo, amostra in AMOSTRAS:
        html = B.render_block(dict(amostra))  # PROVA: o builder emite mesmo.
        classes = sorted({c for attr in re.findall(r'class="([^"]+)"', html)
                          for c in attr.split() if c.startswith("ic-") or c.startswith("qf-")})
        assert classes, f'{eid}: o HTML emitido não trouxe nenhuma classe ic-/qf- ({html[:80]})'
        exercicios.append({
            "id": eid,
            "origem": "bloco",
            "label": label,
            "descricao": desc,
            "grupo": grupo,
            "interativo": interativo,
            "classes": classes,       # é por aqui que o gate casa contrato × HTML da aula
            "campos": sorted(k for k in amostra if k != "kind"),
        })

    exercicios += prova_shell()

    # MARCADOR = classe que só ESTE exercício emite. É como o gate reconhece o
    # exercício dentro do HTML de uma aula. Nem todo exercício tem: o `bank` emite
    # ic-bank/ic-b, exatamente as classes que o `gapfill` também emite (o gapfill TEM
    # um banco dentro). Quando não há marcador, o gate não consegue afirmar a presença
    # daquele exercício sozinho — e isso fica ESCRITO aqui em vez de virar um gate que
    # aprova ou reprova por engano.
    todas = [set(e["classes"]) for e in exercicios]
    for i, e in enumerate(exercicios):
        outras = set().union(*(c for j, c in enumerate(todas) if j != i))
        e["marcadores"] = sorted(todas[i] - outras)
        e["verificavel"] = bool(e["marcadores"])

    return {
        "_fonte": "GERADO por scripts/gen_banco_exercicios.py — não editar à mão. Cada "
                  "exercício aqui foi PROVADO chamando render_block() do builder; as "
                  "classes são as que ele emitiu de verdade.",
        "version": 2,
        "_origem": {
            "bloco": "declarado em lesson.inclass_blocks do config e emitido por "
                     "render_block() do builder — provado executando",
            "shell": "vem do shell do modelo (helen-mendes-aula1.html) — provado pela "
                     "presenca da classe no molde",
        },
        "grupos": {
            "input": "Entrada (o que o aluno lê ou ouve)",
            "compreensao": "Compreensão",
            "vocabulario": "Vocabulário",
            "linguagem": "Foco na linguagem",
            "producao": "Produção",
            "feedback": "Feedback e correção",
        },
        "exercicios": exercicios,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    dados = coleta()
    novo = json.dumps(dados, indent=2, ensure_ascii=False) + "\n"

    if args.check:
        atual = SAIDA.read_text(encoding="utf-8") if SAIDA.exists() else ""
        if atual != novo:
            print("exercicios.json desatualizado — rode "
                  "python3 scripts/gen_banco_exercicios.py", file=sys.stderr)
            return 1
        print(f"exercicios.json em dia ({len(dados['exercicios'])} exercícios)")
        return 0

    SAIDA.write_text(novo, encoding="utf-8")
    print(f"{os.path.relpath(SAIDA, RAIZ)}: {len(dados['exercicios'])} exercícios provados")
    for e in dados["exercicios"]:
        print(f"  {e['id']:11} {e['grupo']:12} {', '.join(e['classes'][:4])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
