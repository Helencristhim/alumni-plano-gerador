#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 37 — a aula da anatomia `consultivo` e o que ela promete ser.

O QUE ELE E
-----------
O par do `validate_lesson.py`, para a outra anatomia. O de la mede as 25 telas, as cinco
etapas do pre-class e o survival card -- promessas do IMERSIVO -- e por isso ele sai fora
deste carimbo de proposito (`validate_lesson.py`, a saida do consultivo). Aplicar o gate
certo ao objeto errado nao e rigor: e ruido que ensina a ignorar gate.

POR QUE AQUI, E NAO DENTRO DO BUILDER
-------------------------------------
O `confere_aula()` do `build_consultivo.py` mede os FRAGMENTOS -- a ENTRADA do build. Este
gate mede o ARQUIVO PUBLICADO -- a SAIDA, que e o que professor e aluno abrem, e que pode
ser editado a mao depois do build, ou nascer de um build antigo. Sao perguntas diferentes:
"os fragmentos fecham o contrato?" e "o que foi publicado fecha o contrato?".

ESCOPO -- PELO CARIMBO, NUNCA PELO CAMINHO
-------------------------------------------
So olha arquivo com `<meta name="alumni-anatomia" content="consultivo">`. Sem o carimbo, o
arquivo nao e desta anatomia e o gate nao tem o que dizer sobre ele. E o que o `gates.json`
declara em `escopo.marcador`, e o que o GATE 17 obriga toda regra de anatomia a declarar.

O CONTRATO E LIDO, NUNCA DIGITADO
----------------------------------
As abas vem de `_build/model/anatomias.json` (a anatomia declara `abas` e `abas_aluno`); as
etapas e os minutos vem do proprio `var LESSONS` do arquivo. Numero digitado a mao aqui
seria o segundo lugar onde a mesma informacao esta escrita -- e o segundo lugar diverge do
primeiro na primeira edicao.

O JS E AVALIADO, NUNCA ADIVINHADO POR REGEX
--------------------------------------------
`var LESSONS` e `var GUIDE` sao objetos JS com strings que contem chave, colchete e
apostrofo. Contar chave com regex funciona ate a primeira aula cujo tema tenha um `{` no
texto -- e ai o gate passa a medir outra coisa em silencio. O bloco e recortado por
casamento de chaves e entregue ao **node**, que e quem sabe ler JavaScript. Mesma doutrina
do GATE 7 (compila no V8) e do GATE 30.

PROFESSOR E ALUNO SAO ARQUIVOS DIFERENTES, E ISSO E DECIDIDO PELA ABA
---------------------------------------------------------------------
A anatomia entrega DUAS URLs: a do professor tem a aba `inclass` (o deck) e o Teacher's
Guide; a do aluno nao tem nem uma coisa nem outra. Entao a presenca da aba `inclass` e que
decide quais regras valem -- e, decidido assim, a AUSENCIA do deck no arquivo do professor
REPROVA, em vez de virar um "pulei porque nao achei". Gate que pula em silencio mede menos
e diz que esta verde.

O que o gate NAO faz: conferir que o arquivo do ALUNO nao carrega conteudo docente. Isso e
o GATE 36 (`check_isolamento_aluno.py`), que mede bytes E elevacao de papel no navegador --
muito mais forte do que qualquer coisa que se meca aqui. Nao se duplica gate.

USO:
    python3 scripts/consultivo/validate_consultivo.py <arquivo.html> [...]
    python3 scripts/consultivo/validate_consultivo.py            # varre public/
    python3 scripts/consultivo/validate_consultivo.py --selftest
"""
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIAS = os.path.join(RAIZ, "_build", "model", "anatomias.json")
ANATOMIA = "consultivo"

# O contrato normativo desta anatomia (Doc 03 §6.1; Doc 04 §8.1).
ETAPAS = 8
# O PADRAO e 60 min de aula: 55 de percurso + 5 de margem (Doc 03 §2). Quando o CONTRATO do
# aluno tem outra duracao, o material publicado declara a sua em `CICLO.percurso` e o gate
# mede contra ela -- foi o caso do Caio, com aula de 45. O default so vale para arquivo que
# nao declara (os quatro anteriores a 31/08/2026).
PERCURSO_MIN = 55
PRECLASS_ATIVIDADES = 6

# Os campos do Teacher's Guide, na forma em que o ARTEFATO os implementa. A mesma lista que
# o `build_consultivo.py` cobra nos fragmentos -- e aqui ela e cobrada no arquivo publicado.
#
# NOTA PARA QUEM FOR MEXER: o Doc 04 §8.1 lista CATORZE campos, e o artefato implementa
# TREZE. Faltam `Lesson overview` e `Stage-by-stage procedure` (o §8.2, dez subcampos por
# etapa), e sobra `transcript`, que nao esta no §8.1. Isso NAO esta cobrado aqui de
# proposito: decidir se o §8.2 ja e servido pelas notas por tela (`data-teacher`) ou se
# falta mesmo e chamada pedagogica, nao medicao. Enquanto nao for decidido, o gate cobra o
# que o artefato de fato promete -- cobrar um campo que nunca existiu reprovaria o proprio
# molde e ensinaria a ignorar o gate.
CAMPOS_GUIA = ["identity", "goals", "product", "criteria", "prep", "language", "transcript",
               "difficulties", "scaffolding", "feedback", "evidence", "prepost", "key"]

VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"


# ─────────────────────────────────────────────────────────────────────────────
# leitura
# ─────────────────────────────────────────────────────────────────────────────
def carimbo(c):
    """A anatomia que o arquivo declara, ou None. So os primeiros 4 KB: o carimbo mora no
    <head>, e procurar no corpo inteiro acharia a MENCAO ao nome dentro de um comentario."""
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def abas_declaradas():
    """As abas que a anatomia promete, do inventario. Nunca digitadas aqui."""
    a = json.load(open(ANATOMIAS, encoding="utf-8"))["anatomias"][ANATOMIA]
    return a.get("abas") or [], a.get("abas_aluno") or []


def recorta_var(c, nome):
    """O fonte de `var NOME = {...}` recortado por casamento de chaves, ou None.

    So aceita a forma LITERAL (`= {` ou `= [`). `var STAGES = stagesOf(...)` e uma CHAMADA,
    nao um literal, e devolver None nela e o certo -- foi tentando ler uma dessas como
    objeto que uma medicao minha voltou "{} vazio" e quase virou um defeito inventado.
    """
    m = re.search(r"\bvar\s+" + re.escape(nome) + r"\s*=\s*([\{\[])", c)
    if not m:
        return None
    i = m.end() - 1
    abre = c[i]
    fecha = "}" if abre == "{" else "]"
    prof = 0
    for j in range(i, len(c)):
        ch = c[j]
        if ch == abre:
            prof += 1
        elif ch == fecha:
            prof -= 1
            if prof == 0:
                return c[i:j + 1]
    return None


SONDA = """
const out = {lessons: null, guide: null, ciclo: null};
if (typeof CICLO !== 'undefined' && CICLO) {
  out.ciclo = {percurso: Number(CICLO.percurso) || null, nominal: Number(CICLO.nominal) || null};
}
if (typeof LESSONS !== 'undefined' && LESSONS) {
  out.lessons = {};
  for (const k of Object.keys(LESSONS)) {
    const L = LESSONS[k] || {};
    const st = Array.isArray(L.stages) ? L.stages : [];
    out.lessons[k] = {
      etapas: st.length,
      min: st.reduce((a, s) => a + (Number(s && s.min) || 0), 0),
      semMin: st.filter(s => !(Number(s && s.min) > 0)).length,
      semNome: st.filter(s => !(s && String(s.n || '').trim())).length,
    };
  }
}
if (typeof GUIDE !== 'undefined' && GUIDE) {
  out.guide = {};
  for (const k of Object.keys(GUIDE)) out.guide[k] = Object.keys(GUIDE[k] || {});
}
console.log(JSON.stringify(out));
"""


def avalia(c):
    """Avalia `var LESSONS` e `var GUIDE` no node e devolve o resumo. node ausente = ERRO,
    nunca "pulei": o gate que pula sozinho e o gate que mente."""
    partes = []
    for nome in ("LESSONS", "GUIDE", "CICLO"):
        src = recorta_var(c, nome)
        if src is not None:
            partes.append(f"const {nome} = {src};")
    fonte = "\n".join(partes) + "\n" + SONDA
    with tempfile.NamedTemporaryFile("w", suffix=".mjs", delete=False, encoding="utf-8") as f:
        f.write(fonte)
        caminho = f.name
    try:
        r = subprocess.run(["node", caminho], capture_output=True, text=True, timeout=60)
    except FileNotFoundError:
        raise SystemExit("GATE 37 precisa do node para ler o JS da aula, e ele nao esta no PATH.")
    finally:
        os.unlink(caminho)
    if r.returncode != 0:
        return None, (r.stderr.strip().splitlines() or ["erro sem mensagem"])[-1][:200]
    return json.loads(r.stdout), None


def bloco_por_id(c, ident):
    """O HTML do <div id="..."> ate o seu proprio fechamento."""
    m = re.search(r'<div[^>]*id="' + re.escape(ident) + r'"[^>]*>', c)
    if not m:
        return None
    prof = 0
    for t in re.finditer(r"<div\b[^>]*>|</div>", c[m.start():]):
        prof += 1 if t.group(0).startswith("<div") else -1
        if prof == 0:
            return c[m.start():m.start() + t.end()]
    return None


# ─────────────────────────────────────────────────────────────────────────────
# as regras
# ─────────────────────────────────────────────────────────────────────────────
def confere(caminho):
    """Devolve (aplicou, erros). aplicou=False quando o arquivo nao e desta anatomia."""
    c = open(caminho, encoding="utf-8").read()
    if carimbo(c) != ANATOMIA:
        return False, []

    erros = []
    abas_prof, abas_aluno = abas_declaradas()
    tem = set(re.findall(r'id="tab-([a-z]+)"', c))
    eh_professor = "inclass" in tem
    esperadas = abas_prof if eh_professor else abas_aluno
    papel = "professor" if eh_professor else "aluno"

    # R1 · as abas que a anatomia declara existem
    faltam = [a for a in esperadas if a not in tem]
    if faltam:
        erros.append(f"ABAS: faltam {', '.join(faltam)} — a anatomia {ANATOMIA} declara "
                     f"{esperadas} para a URL do {papel} (_build/model/anatomias.json).")

    dados, erro_js = avalia(c)
    if erro_js:
        erros.append(f"O JS da aula nao avalia: {erro_js}. Sem isso nao ha o que medir.")
        return True, erros

    lessons = (dados or {}).get("lessons")
    if not lessons:
        erros.append("SEM var LESSONS: e dela que saem as etapas, os minutos e as aulas do "
                     "ciclo. Arquivo desta anatomia sem LESSONS nao tem contrato para conferir.")
        return True, erros

    for n in sorted(lessons, key=lambda x: int(x) if x.isdigit() else 0):
        L = lessons[n]

        # R2 · OITO etapas. Nunca oito telas (Doc 03 §6.1) — a contagem de telas e a R5.
        if L["etapas"] != ETAPAS:
            erros.append(f"aula {n}: {L['etapas']} etapas declaradas, e a arquitetura tem "
                         f"{ETAPAS}. (Telas podem ser quantas o conteudo pedir; ETAPAS, nao.)")

        # R3 · os minutos fecham o percurso essencial DECLARADO por este material
        percurso = ((dados or {}).get("ciclo") or {}).get("percurso") or PERCURSO_MIN
        if L["min"] != percurso:
            erros.append(f"aula {n}: os minutos das etapas somam {L['min']}, e o percurso "
                         f"essencial declarado e {percurso} (+5 de margem).")
        if L["semMin"]:
            erros.append(f"aula {n}: {L['semMin']} etapa(s) sem orcamento de minutos.")
        if L["semNome"]:
            erros.append(f"aula {n}: {L['semNome']} etapa(s) sem nome. O rotulo e autoral da "
                         f"aula, mas nao pode ser vazio — e o que a barra do topo mostra.")

        # R4 · o pre-class tem exatamente SEIS atividades reais (Doc 04 §4.2)
        bloco = bloco_por_id(c, f"pc{n}")
        if bloco is None:
            erros.append(f"aula {n}: nao ha bloco de pre-class id=\"pc{n}\" — a aba abre vazia "
                         f"para essa aula.")
        else:
            n_ativ = len(re.findall(r'class="exercise-section"', bloco))
            if n_ativ != PRECLASS_ATIVIDADES:
                erros.append(f"aula {n}: o pre-class tem {n_ativ} atividades, e sao exatamente "
                             f"{PRECLASS_ATIVIDADES} (Doc 04 §4.2).")

    if not eh_professor:
        return True, erros

    # ── daqui para baixo, so a URL do professor ────────────────────────────────
    # R5 · as telas representam as etapas, e na ordem — POR AULA.
    #
    # A etapa REINICIA em 1 a cada aula: o deck do molde e [1,1,2,3,4,5,6,7,8,8] quatro
    # vezes seguidas. Medir a ordem no arquivo inteiro acusa "fora de ordem" em toda
    # virada de aula -- foi o que a primeira versao deste gate fez. A tela carrega as
    # DUAS marcas (`data-lesson` e `data-stage`) no mesmo <div>, entao o par se le junto.
    telas = []
    for tag in re.finditer(r"<div[^>]*\bdata-stage=\"\d+\"[^>]*>", c):
        t = tag.group(0)
        ml = re.search(r'data-lesson="(\d+)"', t)
        ms = re.search(r'data-stage="(\d+)"', t)
        telas.append((ml.group(1) if ml else None, int(ms.group(1))))

    if not telas:
        erros.append("SEM TELA COM data-stage: a URL do professor tem a aba in-class, entao "
                     "tem deck — e sem data-stage nenhuma tela pertence a etapa nenhuma "
                     "(a barra do topo nao sabe onde a aula esta).")
    else:
        orfas = [s for l, s in telas if l is None]
        if orfas:
            erros.append(f"{len(orfas)} tela(s) com data-stage e SEM data-lesson: elas nao "
                         f"pertencem a aula nenhuma, e o deck nao sabe onde parar.")
        por_aula = {}
        for l, s in telas:
            if l is not None:
                por_aula.setdefault(l, []).append(s)

        for n in sorted(lessons, key=lambda x: int(x) if x.isdigit() else 0):
            seq = por_aula.get(n)
            if not seq:
                erros.append(f"aula {n}: existe em LESSONS e nao tem nenhuma tela "
                             f"(data-lesson=\"{n}\") no deck.")
                continue
            faltando = sorted(set(range(1, lessons[n]["etapas"] + 1)) - set(seq))
            if faltando:
                erros.append(f"aula {n}: as telas nao representam as etapas {faltando}. "
                             f"Nenhuma etapa fica sem representacao (Doc 03 §6.1).")
            if seq != sorted(seq):
                quebra = next(i for i in range(1, len(seq)) if seq[i] < seq[i - 1])
                erros.append(f"aula {n}: as etapas aparecem fora de ordem nas telas — a etapa "
                             f"{seq[quebra]} vem depois da {seq[quebra - 1]}. A ordem das oito "
                             f"etapas e normativa.")

    # R6 · o Teacher's Guide, aula a aula
    guide = (dados or {}).get("guide")
    if guide is None:
        erros.append("SEM var GUIDE: a URL do professor entrega o Teacher's Guide, e ele nao "
                     "esta no arquivo.")
    else:
        for n in sorted(lessons, key=lambda x: int(x) if x.isdigit() else 0):
            if n not in guide:
                erros.append(f"aula {n}: existe em LESSONS e nao tem Teacher's Guide.")
                continue
            faltam = [k for k in CAMPOS_GUIA if k not in guide[n]]
            if faltam:
                erros.append(f"aula {n}: o Teacher's Guide nao tem os campos {faltam} "
                             f"(Doc 04 §8.1).")

    # ─────────────────────────────────────────────────────────────────────────
    # REGRAS DE OBSERVACAO
    # ─────────────────────────────────────────────────────────────────────────
    # Daqui para baixo entram as regras que a OBSERVACAO trouxer -- cada erro que voltar a
    # aparecer numa aula gerada, depois de ja ter sido corrigido uma vez.
    #
    # Antes de escrever uma aqui, passe o item pelas tres perguntas, nesta ordem:
    #
    #   1. E sempre a mesma FORMA?      -> nao e regra: e EMISSAO. O builder passa a produzir
    #                                      aquele markup, e quem escreve a aula nunca mais o
    #                                      toca. Defeito que nao pode nascer nao precisa de
    #                                      gate.
    #   2. Da para DEDUZIR do que ja
    #      esta na aula?                -> nao e regra: e INJETOR. O builder extrai do que
    #                                      existe e emite o que falta (foi assim que o slide
    #                                      de tarefa deixou de depender de alguem lembrar).
    #   3. E contagem, ordem ou
    #      presenca?                    -> ASSERT em confere_aula(), que responde em dois
    #                                      segundos, no mesmo loop, com quem escreveu ainda
    #                                      no contexto.
    #
    # So o que nao cai em nenhuma das tres mora AQUI: o que precisa ser medido no arquivo
    # PUBLICADO, porque ele pode ser editado depois do build ou vir de um build antigo.
    #
    # E nao escreva regra a partir dos documentos normativos. A REGRA 2.1 do imersivo nasceu
    # assim -- o documento mandava esconder as perguntas do listening, o gerador obedeceu, e
    # o defeito nasceu em 224 arquivos. Regra boa e autopsia, nao profecia.

    return True, erros


# ─────────────────────────────────────────────────────────────────────────────
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


# ─────────────────────────────────────────────────────────────────────────────
# selftest — prova que cada regra ainda morde
# ─────────────────────────────────────────────────────────────────────────────
def _selftest():
    base = os.path.join(RAIZ, "public", "professor", "stephanie-vicente.html")
    if not os.path.exists(base):
        print("SELFTEST INCONCLUSIVO — o molde nao esta no lugar:", base)
        return 1
    limpo = open(base, encoding="utf-8").read()

    ok, erros = _confere_texto(limpo)
    if erros:
        print("SELFTEST INCONCLUSIVO — o molde JA esta reprovando:")
        for e in erros:
            print("   ", e)
        return 1

    casos = [
        ("aba removida",
         lambda s: s.replace('id="tab-syllabus"', 'id="tab-syllabusX"', 1),
         "ABAS"),
        ("uma etapa a menos",
         lambda s: s.replace("{n:'Prediction',min:3},", "", 1),
         "etapas declaradas"),
        ("minutos que nao fecham",
         lambda s: s.replace("{n:'Prediction',min:3}", "{n:'Prediction',min:9}", 1),
         "percurso"),
        ("etapa sem nome",
         lambda s: s.replace("{n:'Prediction',min:3}", "{n:'',min:3}", 1),
         "sem nome"),
        ("atividade a menos no pre-class",
         lambda s: s.replace('class="exercise-section"', 'class="exercise-sectionX"', 1),
         "atividades"),
        ("tela sem etapa",
         lambda s: re.sub(r'data-stage="1"', 'data-stageX="1"', s),
         "etapas"),
        ("etapa fora de ordem dentro da aula",
         lambda s: s.replace('data-stage="2"', 'data-stage="8"', 1),
         "fora de ordem"),
        ("tela sem aula",
         lambda s: s.replace('data-stage="1" data-lesson="1"', 'data-stage="1"', 1),
         "SEM data-lesson"),
        ("campo do guia faltando",
         lambda s: s.replace("prepost:", "prepostX:", 1),
         "Teacher's Guide"),
        ("carimbo de outra anatomia",
         lambda s: s.replace('content="consultivo"', 'content="imersivo"', 1),
         None),   # None = o gate deve IGNORAR o arquivo
    ]

    falhou = False
    for nome, muta, esperado in casos:
        aplicou, errs = _confere_texto(muta(limpo))
        if esperado is None:
            bom = (aplicou is False)
            motivo = "ignorado (carimbo de outra anatomia)" if bom else "NAO ignorou"
        else:
            bom = aplicou and any(esperado.lower() in e.lower() for e in errs)
            motivo = (errs[0][:70] if errs else "nao acusou nada")
        print(f"  {'OK  ' if bom else 'FALHA'}  {nome:34} {motivo}")
        if not bom:
            falhou = True

    print()
    if falhou:
        print("SELFTEST FALHOU — alguma regra parou de morder.")
        return 1
    print(f"SELFTEST OK — os {len(casos) - 1} defeitos sao pegos, e arquivo de outra "
          f"anatomia e ignorado.")
    return 0


def _confere_texto(texto):
    """confere() sobre um texto em memoria — so o selftest usa."""
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(texto)
        p = f.name
    try:
        return confere(p)
    finally:
        os.unlink(p)


def main():
    if "--selftest" in sys.argv:
        return _selftest()

    alvos = [a for a in sys.argv[1:] if a.endswith(".html")] or alvos_padrao()
    if not alvos:
        print(f"GATE 37 — nenhum arquivo com o carimbo {ANATOMIA}. Nada a conferir.")
        return 0

    print(f"=== GATE 37 — anatomia {ANATOMIA} ===")
    total = 0
    vistos = 0
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
            print(f"{VERDE}ok{ZERA}    {rel}")

    print()
    if total:
        print(f"{VERMELHO}GATE 37 — {total} problema(s) em {vistos} arquivo(s).{ZERA}")
        return 1
    print(f"GATE 37 OK — {vistos} arquivo(s) da anatomia {ANATOMIA} fecham o contrato.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
