#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 34 — o pacote normativo do consultivo esta INTEIRO e nao perdeu texto.

POR QUE ISTO EXISTE
-------------------
O Adendo 02 §13.3 e explicito:

    "A simples existencia do arquivo fora do pacote nao constitui carregamento nem
     conformidade. A ausencia de A01 ou A02 no lote deve bloquear a declaracao de
     conformidade integral."

Isto e uma regra sobre o REPO, nao sobre material, e por isso e um gate de processo que
roda sempre. Ela cobre dois defeitos que ja aconteceram neste projeto, um de cada lado:

  1. DOCUMENTO QUE NAO ESTA. Tres dos cinco normativos de agosto viviam em ~/Downloads, e
     por isso o banco de mecanicas e o processo do controlador nunca viraram nada: regra
     fora do repo nao e citavel nem verificavel. Aqui, faltar um arquivo REPROVA.

  2. DOCUMENTO QUE ESTA MAS ESVAZIOU. Os .md sao conversao mecanica dos .docx do Drive
     (scripts/consultivo/docx_to_md.py). Uma reimportacao de um .docx corrompido, ou um
     conversor que perca tabela, produz um arquivo que CONTINUA EXISTINDO, continua
     abrindo, e perdeu a regra. Nada acusaria. Por isso cada documento tem FRASES-CANARIO:
     trechos normativos que a conversao TEM de preservar.

ISTO JA ACONTECEU, e por isso o gate nao e teorico. Em 24/08/2026 a Stephanie atualizou
sete dos treze documentos. O 00 trocava exatamente a regra de etapas: saiu "Nao existe uma
quantidade universal de oito etapas" e entrou "Cada um dos quatro frameworks possui oito
etapas pedagogicas normativas" -- o OPOSTO. A ancora caiu, o gate reprovou, e foi assim que
soubemos que a regra que o molde ia implementar tinha mudado de sinal. Sem ele, a
reimportacao teria passado em silencio e o gate da espinha nasceria cobrando o contrario do
que a escola manda.

Ancora que cai NAO se conserta procurando uma frase parecida: le-se o que a regra passou a
dizer e a ancora nova e a frase NOVA.

As frases nao sao um resumo do documento nem uma segunda copia da regra -- sao ancoras.
Cada uma foi escolhida por ser (a) normativa e (b) de uma forma diferente: prosa, celula
de tabela, item de lista, identificador tecnico. Se a conversao perder qualquer uma dessas
formas, uma ancora cai.

USO:
    python3 scripts/consultivo/check_docs_pacote.py
    python3 scripts/consultivo/check_docs_pacote.py --selftest
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(RAIZ, "docs", "consultivo")

# nome do arquivo -> ancoras que a conversao tem de preservar
PACOTE = {
    "00-guia-de-uso-e-precedencia": [
        # 24/08/2026: a regra das etapas MUDOU de conteudo, e a ancora antiga caiu -- foi
        # este gate que avisou. A nova diz o oposto da anterior, e por isso a ancora nova
        # nao e "a frase parecida": e a frase que a regra passou a usar.
        "Cada um dos quatro frameworks possui oito etapas pedagógicas normativas",
        "não integra o arquivo, o HTML, o payload, o estado",
        "Acompanhamento docente",
        "requisito de plataforma",
    ],
    "01-perfil-do-aluno": [
        "hipótese pedagógica, não um diagnóstico",
        "catorze campos",
        "Descartada",
    ],
    "02-syllabus-do-ciclo": [
        "PRODUZIR SOMENTE UM BLOCO POR VEZ",
        "cinco blocos de quatro",
        "Grammar só é selecionada",
    ],
    "03-estrutura-dos-frameworks": [
        "55 minutos",
        "Personalized Real-World English",
        "EVIDÊNCIA → OPERAÇÃO COGNITIVA",
        "As oito etapas devem estar presentes e permanecer na ordem declarada",
        "É proibido converter a regra de oito etapas em exigência de oito slides",
    ],
    "04-planejamento-e-producao-da-aula": [
        "exatamente seis atividades reais",
        "núcleo protegido",
        "Teacher’s Guide",
        "A URL do aluno contém exclusivamente conteúdo discente",
    ],
    "05-ciclo-de-evolucao": [
        "Entry-ready",
        "A aula 21 é a primeira aula do novo ciclo",
    ],
    "06-prompt-controlador": [
        "ACOMPANHAMENTO_DOCENTE",
        "VOCÊ É O CONTROLADOR PEDAGÓGICO",
        "NÃO VERIFICADO",
        "PROFESSOR_URL",
        "ALUNO_URL",
    ],
    "P1-camada-funcional-html": [
        "Visão professor",
        "Reset lesson",
        "mode=teacher-guide",
        "speechSynthesis",
        "duas URLs e dois builds separados por papel",
        "Separação de entrega",
    ],
    "P2-protocolo-implementacao-e-qa": [
        "ABRA A PÁGINA e leia o console",
        "canário",
        "backup",
        "N = 8 por regra do Documento 03",
    ],
    "P3-matriz-de-conformidade": [
        "Carga limpa",
        "Mutações obrigatórias",
        "allow-popups",
        "fixar oito slides",
        "display:none não é separação",
    ],
    # O A03 chegou ao repo em 25/08/2026, com o pacote atualizado. Ate entao ele era citado
    # por ~20 itens do catalogo do auditor (A03 §§18-35) e simplesmente NAO ESTAVA AQUI --
    # e este gate, que promete que "o pacote so vale inteiro", passava verde, porque a lista
    # dele nao sabia que o documento existia. Gate so cobra o que alguem escreveu que ele
    # cobrasse: a lista E o contrato, e documento fora dela e documento invisivel.
    "A03-apoio-funcional-integridade-qa": [
        "apoio funcional em português",
        "Answer Key",
        "Guided Discovery",
    ],
    "A01-continuidade-transcript-navegacao": [
        "Show transcript",
        "Back to top",
        "continuidade pedagógica",
    ],
    "A02-safeguards-instrucao-atividades-audio": [
        "Embaralhamento funcional",
        "1–A, 2–B, 3–C",
        "microáudio",
    ],
    "ANEXO-P-A-audios-elevenlabs": [
        "eleven_v3",
        "transcript_hash",
        "Text to Dialogue",
    ],
}

# Cabecalho obrigatorio: o .md declara de onde veio. Sem isso, ele vira texto orfao que
# alguem edita achando que e a fonte -- e a partir dali o Drive e o repo divergem calados.
CABECALHO = "Documento normativo importado do Drive"

MIN_BYTES = 4000  # nenhum documento do pacote e menor que isto; truncagem cai aqui


def verifica(diretorio):
    erros = []
    for nome, ancoras in sorted(PACOTE.items()):
        caminho = os.path.join(diretorio, nome + ".md")
        if not os.path.exists(caminho):
            erros.append(f"{nome}.md: AUSENTE. O pacote so vale inteiro (A02 §13.3).")
            continue
        txt = open(caminho, encoding="utf-8").read()
        if len(txt) < MIN_BYTES:
            erros.append(f"{nome}.md: {len(txt)} bytes — abaixo do minimo. Conversao truncada?")
        if CABECALHO not in txt:
            erros.append(f"{nome}.md: sem o cabecalho de origem. De onde ele veio?")
        baixo = txt.lower()
        for a in ancoras:
            if a.lower() not in baixo:
                erros.append(f"{nome}.md: perdeu a ancora {a!r}.")
    idx = os.path.join(diretorio, "README.md")
    if not os.path.exists(idx):
        erros.append("README.md: AUSENTE. A composicao do pacote e normativa, nao opcional.")
    return erros


def _selftest():
    """Prova que o gate MORDE: documento ausente, truncado, sem cabecalho e sem ancora."""
    import shutil
    import tempfile
    base = tempfile.mkdtemp(prefix="pacote_")
    try:
        for nome, ancoras in PACOTE.items():
            with open(os.path.join(base, nome + ".md"), "w", encoding="utf-8") as fh:
                fh.write(CABECALHO + "\n" + "x" * MIN_BYTES + "\n" + "\n".join(ancoras))
        open(os.path.join(base, "README.md"), "w").write("indice")
        if verifica(base):
            print("FALHA: pacote integro reprovou.")
            return 1
        print("  OK    pacote integro passa")

        casos = []
        # 1 — documento ausente
        d1 = os.path.join(base, "_a")
        shutil.copytree(base, d1, ignore=shutil.ignore_patterns("_*"))
        os.remove(os.path.join(d1, "A02-safeguards-instrucao-atividades-audio.md"))
        casos.append(("documento ausente (A02)", d1, "AUSENTE"))
        # 2 — truncado
        d2 = os.path.join(base, "_b")
        shutil.copytree(base, d2, ignore=shutil.ignore_patterns("_*"))
        open(os.path.join(d2, "P3-matriz-de-conformidade.md"), "w").write(CABECALHO)
        casos.append(("documento truncado", d2, "abaixo do minimo"))
        # 3 — sem cabecalho de origem
        d3 = os.path.join(base, "_c")
        shutil.copytree(base, d3, ignore=shutil.ignore_patterns("_*"))
        p = os.path.join(d3, "01-perfil-do-aluno.md")
        open(p, "w", encoding="utf-8").write("x" * MIN_BYTES + "\n" +
                                             "\n".join(PACOTE["01-perfil-do-aluno"]))
        casos.append(("sem cabecalho de origem", d3, "sem o cabecalho"))
        # 4 — ancora perdida (a conversao esvaziou a regra sem esvaziar o arquivo)
        d4 = os.path.join(base, "_d")
        shutil.copytree(base, d4, ignore=shutil.ignore_patterns("_*"))
        p = os.path.join(d4, "02-syllabus-do-ciclo.md")
        t = open(p, encoding="utf-8").read().replace("PRODUZIR SOMENTE UM BLOCO POR VEZ", "")
        open(p, "w", encoding="utf-8").write(t)
        casos.append(("ancora perdida na conversao", d4, "perdeu a ancora"))
        # 5 — indice sumiu
        d5 = os.path.join(base, "_e")
        shutil.copytree(base, d5, ignore=shutil.ignore_patterns("_*"))
        os.remove(os.path.join(d5, "README.md"))
        casos.append(("indice do pacote ausente", d5, "composicao do pacote"))

        for rotulo, d, esperado in casos:
            errs = verifica(d)
            if not any(esperado in e for e in errs):
                print(f"FALHA: '{rotulo}' NAO foi pego. erros={errs}")
                return 1
            print(f"  OK    {rotulo}")
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print("\nSELFTEST OK — os 5 defeitos sao pegos.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    print("=== GATE 34 — pacote normativo consultivo ===")
    erros = verifica(DIR)
    if erros:
        for e in erros:
            print("  FALHA:", e)
        print(f"\nFALHOU — {len(erros)} problema(s). O pacote so vale inteiro (A02 §13.3).")
        return 1
    total = sum(os.path.getsize(os.path.join(DIR, n + ".md")) for n in PACOTE)
    print(f"OK — {len(PACOTE)} documentos, {total} bytes, todas as ancoras normativas de pe.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
