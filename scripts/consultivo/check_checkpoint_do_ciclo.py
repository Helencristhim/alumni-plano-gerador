#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 78 — o painel de checkpoint fala das aulas do ciclo DESTE aluno.

DE ONDE ISTO VEIO (16/09/2026)
------------------------------
O painel de checkpoint do Registro pos-aula (aba do professor) saiu do artefato do Marcos com
os numeros do ciclo dele escritos em texto:

    Checkpoint da aula 22 · Decisao sobre as aulas 23–38 · Confirmar as aulas 23–38 ·
    Mesmo em caso de reconfiguracao, as aulas 19 a 22 continuam registradas...

Os oito materiais do consultivo carregavam isso. Na Adriana (bloco 4–7, ciclo 4–23) o
professor decidia sobre "as aulas 23–38", quinze delas fora do contrato; so na Gabriela
(19–22 / 19–38) o numero batia, por coincidencia. O JS ja derivava a aula do checkpoint de
`CICLO` (`cpAula()`), entao o painel LIBERAVA na aula certa e ANUNCIAVA a errada.

Nenhum gate viu. O GATE 39 procura `Aula N` / `Lesson N` com maiuscula e fora do intervalo do
ciclo -- "aulas 23–38" e minusculo, plural e intervalo.

O QUE ELE MEDE, no arquivo do PROFESSOR
---------------------------------------
Contra o `ciclo` do config do aluno (a fonte), e nao contra o proprio arquivo:

  1. o `var CICLO` do arquivo tem a mesma `primeira`, `porBloco` e `aulas` do config;
  2. o painel existe (sem ele o gate nao teria o que medir, e "nao achei" nao e "passou");
  3. dentro do painel -- do titulo "Checkpoint da aula N" ate a secao D -- e na lista `var CP`:
       - todo INTERVALO de aulas ("aulas X–Y", "aulas X a Y") e o bloco 1 (primeira a
         checkpoint) ou o restante do ciclo (checkpoint+1 ao fim);
       - toda aula ROTULADA como a do checkpoint ("Checkpoint da aula N", "registro da aula
         N", "Checklist do professor — aula N") e a ultima do bloco 1;
  4. nenhum marcador `{{CP_...}}` sobrou, nos dois arquivos;
  5. no painel INTEIRO -- do titulo ate o fim da secao D (o botao "Voltar ao topo") -- e na
     lista `var CP`:
       - toda aula citada ("aula N", "aulas N a M", "lesson N"), rotulada ou solta, esta
         dentro do ciclo do config (primeira a ultima);
       - todo nivel CEFR escrito (A0..C2, com ou sem "+") e o `ciclo.nivel` do config.

DE ONDE VEIO O ITEM 5 (16/09/2026, mesmo dia)
---------------------------------------------
Depois dos marcadores, o painel ainda carregava texto do perfil do Marcos: "a aula 29 se
confirma como Grammar", "nao se sustentar na aula 19", e a secao D oferecendo "Novo ciclo em
B1 / Modulo B1+ / Modulo B2" a alunas A1. O shell passou a trazer texto sem numero e sem
nivel (`extrai_shell.CORRECOES` `checkpoint-exemplo-*`, `checkpoint-rota-*`). O item 5 mede
dado contra dado -- numero contra o intervalo do ciclo, codigo CEFR contra o do config --, e
nao uma lista de palavras: exemplo escrito para outro aluno SEM numero e SEM nivel ("do
espanhol") nao e mensuravel assim, e o A05 §10.2 rejeita detector lexical.

Comentario de HTML/JS nao conta (nao chega ao olho de ninguem).

ESCOPO: o carimbo `alumni-anatomia=consultivo`.

USO:
    python3 scripts/consultivo/check_checkpoint_do_ciclo.py [arquivo.html ...]
    python3 scripts/consultivo/check_checkpoint_do_ciclo.py --selftest
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import checkpoint_ciclo  # noqa: E402  a MESMA conta que o builder usa para preencher

ANATOMIA = "consultivo"
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

RX_INICIO = re.compile(r'<h3 class="sub">Checkpoint da aula')
RX_FIM = re.compile(r'<h3 class="sub">D ·')
RX_INTERVALO = re.compile(r"\baulas\s+(\d+)\s*(?:–|—|-|a)\s*(\d+)\b")
RX_ROTULADA = re.compile(r"(?:Checkpoint da aula|registro da aula|"
                         r"Checklist do professor\s*—\s*aula)\s+(\d+)\b")
# Item 5. O fim do painel e o botao que fecha a area, logo depois da secao D.
RX_FIM_PAINEL = re.compile(r'<div class="btn-bar ao-topo">')
RX_AULA_CITADA = re.compile(r"\b(?:aulas?|lessons?)\s+(\d+)(?:\s*(?:–|—|-|a|to)\s*(\d+))?\b",
                            re.I)
RX_CEFR = re.compile(r"(?<![A-Za-z0-9#])([ABC][0-2])(\+?)(?![A-Za-z0-9])")


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def configs():
    """{nome do arquivo publicado sem .html: config} -- os mesmos nomes que o builder escreve."""
    saida = {}
    for p in sorted(glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "config.json"))):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        slug = d.get("slug")
        if not slug:
            continue
        if d.get("arquivo"):
            nomes = [d["arquivo"]]
        elif d.get("fase", "canonica") == "piloto":
            nomes = [f"{slug}-ciclo{(d.get('ciclo') or {}).get('numero')}"]
        else:
            nomes = [slug]
        for n in nomes:
            saida[n] = d
    return saida


def sem_comentarios(c):
    c = re.sub(r"<!--.*?-->", " ", c, flags=re.S)
    return re.sub(r"/\*.*?\*/", " ", c, flags=re.S)


def confere(caminho, cfgs, texto=None):
    """None se nao se aplica; lista de erros caso contrario."""
    c = texto if texto is not None else open(caminho, encoding="utf-8").read()
    if carimbo(c) != ANATOMIA:
        return None
    erros = []
    if "{{CP_" in c:
        erros.append("marcador {{CP_...}} sobrou no arquivo publicado: o builder nao "
                     "preencheu o painel de checkpoint.")
    lado = os.path.basename(os.path.dirname(caminho))
    if lado != "professor":
        return erros

    nome = os.path.basename(caminho)[:-len(".html")]
    cfg = cfgs.get(nome)
    if not cfg:
        return erros + [f"nenhum _build/consultivo/*/config.json escreve '{nome}.html': sem o "
                        f"ciclo declarado nao ha contra o que medir o painel."]
    valores, erro = checkpoint_ciclo.intervalo(cfg.get("ciclo"))
    if erro:
        return erros + [erro]
    pri, cp, resto, fim = valores

    no_arquivo = checkpoint_ciclo.ciclo_do_material(c) or {}
    for k in ("primeira", "porBloco", "aulas"):
        if no_arquivo.get(k) != cfg["ciclo"][k]:
            erros.append(f"var CICLO.{k} = {no_arquivo.get(k)} no arquivo e {cfg['ciclo'][k]} "
                         f"no config: o material foi montado com outro ciclo.")

    limpo = sem_comentarios(c)
    ini = RX_INICIO.search(limpo)
    if not ini:
        return erros + ["painel de checkpoint ausente (titulo 'Checkpoint da aula N' nao "
                        "encontrado). Sem ele o gate nao mede nada."]
    fim_m = RX_FIM.search(limpo, ini.end())
    if not fim_m:
        return erros + ["painel de checkpoint sem a secao D: nao ha onde a regiao termina."]
    regiao = limpo[ini.start():fim_m.start()]
    m_cp = re.search(r"var CP=\[(.*?)\];", limpo, re.S)
    if not m_cp:
        return erros + ["`var CP=[...]` (a lista do checklist do checkpoint) nao encontrada."]
    regiao += "\n" + m_cp.group(1)

    rotuladas = [int(x) for x in RX_ROTULADA.findall(regiao)]
    intervalos = [(int(a), int(b)) for a, b in RX_INTERVALO.findall(regiao)]
    if not rotuladas or (resto, fim) not in intervalos:
        erros.append(f"o painel nao traz o rotulo da aula do checkpoint e o intervalo "
                     f"{resto}–{fim}: a regiao medida nao e a que o gate nomeia.")
    for n in rotuladas:
        if n != cp:
            erros.append(f"o painel chama de aula do checkpoint a aula {n}; pelo ciclo do "
                         f"config (primeira {pri}, {cfg['ciclo']['porBloco']} por bloco) e "
                         f"a {cp}.")
    for a, b in intervalos:
        if (a, b) not in ((pri, cp), (resto, fim)):
            erros.append(f"o painel fala das aulas {a}–{b}; o bloco 1 e {pri}–{cp} e o "
                         f"restante do ciclo e {resto}–{fim}.")

    # 5. o painel inteiro, ate o fim da secao D
    fim_p = RX_FIM_PAINEL.search(limpo, fim_m.end())
    if not fim_p:
        return erros + ["painel de checkpoint sem o fechamento da area (botao 'Voltar ao "
                        "topo' depois da secao D): nao ha onde a secao D termina."]
    painel = limpo[ini.start():fim_p.start()] + "\n" + m_cp.group(1)
    for m in RX_AULA_CITADA.finditer(painel):
        for n in (m.group(1), m.group(2)):
            if n is not None and not (pri <= int(n) <= fim):
                erros.append(f"o painel cita '{m.group(0)}'; o ciclo do config vai da aula "
                             f"{pri} a {fim}. Exemplo escrito para o syllabus de outro aluno.")
                break
    nivel = str((cfg.get("ciclo") or {}).get("nivel") or "").strip().upper()
    visivel = re.sub(r"<[^>]+>", " ", painel)
    for m in RX_CEFR.finditer(visivel):
        achado = m.group(1) + m.group(2)
        if achado != nivel:
            erros.append(f"o painel escreve o nivel {achado}; o `ciclo.nivel` do config e "
                         f"{nivel or '(ausente)'}. Rota ou exemplo escrito para o nivel de "
                         f"outro aluno.")
    return erros


def alvos_padrao():
    return sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")) +
                  glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html")))


def main(argv):
    alvos = [a for a in argv if a.endswith(".html")] or alvos_padrao()
    cfgs = configs()
    print(f"=== GATE 78 — as aulas do painel de checkpoint (anatomia {ANATOMIA}) ===")
    total = vistos = 0
    for a in alvos:
        if not os.path.exists(a):
            continue
        r = confere(os.path.abspath(a), cfgs)
        if r is None:
            continue
        vistos += 1
        rel = os.path.relpath(os.path.abspath(a), RAIZ)
        if r:
            total += len(r)
            print(f"{VERMELHO}FAIL{ZERA}  {rel}")
            for e in r:
                print(f"        {e}")
        else:
            print(f"{VERDE}ok{ZERA}    {rel}")
    print()
    if not vistos:
        print(f"{VERMELHO}GATE 78 — nenhum material da anatomia encontrado.{ZERA}")
        return 1
    if total:
        print(f"{VERMELHO}GATE 78 — {total} problema(s) em {vistos} arquivo(s).{ZERA}")
        return 1
    print(f"GATE 78 OK — {vistos} arquivo(s): o painel de checkpoint fala do ciclo do aluno.")
    return 0


def selftest():
    base = os.path.join(RAIZ, "public", "professor", "stephanie-vicente.html")
    if not os.path.exists(base):
        print("SELFTEST INCONCLUSIVO — o molde nao esta no lugar.")
        return 1
    cfgs = configs()
    limpo = open(base, encoding="utf-8").read()
    erros = confere(base, cfgs, limpo)
    if erros:
        print("SELFTEST INCONCLUSIVO — o molde JA esta reprovando:")
        for e in erros:
            print("   ", e)
        return 1
    # o molde: ciclo 1-20, 4 por bloco -> checkpoint 4, restante 5-20
    casos = [
        ("o defeito real: intervalo do artefato no titulo C",
         lambda s: s.replace("C · Decisão sobre as aulas 5–20", "C · Decisão sobre as aulas 23–38", 1),
         "23–38"),
        ("aula do checkpoint errada no titulo",
         lambda s: s.replace("Checkpoint da aula 4<", "Checkpoint da aula 22<", 1),
         "aula 22"),
        ("bloco 1 errado na preservacao do percurso",
         lambda s: s.replace("as aulas 1 a 4 continuam", "as aulas 19 a 22 continuam", 1),
         "19–22"),
        ("intervalo errado so na lista JS do checklist",
         lambda s: s.replace('reconfigurar as aulas 5–20"\n];', 'reconfigurar as aulas 23–38"\n];', 1),
         "23–38"),
        ("marcador que o builder nao preencheu",
         lambda s: s.replace("Checkpoint da aula 4<", "Checkpoint da aula {{CP_AULA}}<", 1),
         "marcador"),
        ("CICLO do arquivo diferente do config",
         lambda s: s.replace("primeira:1,porBloco:4", "primeira:19,porBloco:4", 1),
         "var CICLO.primeira"),
        ("painel sumiu",
         lambda s: s.replace('<h3 class="sub">Checkpoint da aula 4</h3>', "<h3>x</h3>", 1),
         "ausente"),
        ("item 5: exemplo da secao C com aula solta de outro syllabus",
         lambda s: s.replace("a aula de Grammar \ndo próximo bloco se confirma",
                             "a aula 29 \nse confirma como Grammar", 1),
         "aula 29"),
        ("item 5: rota da secao D com nivel que nao e o do config",
         lambda s: s.replace("Novo ciclo no nível confirmado", "Novo ciclo em A2", 1),
         "nivel A2"),
        ("item 5: nivel na lista JS do checklist",
         lambda s: s.replace('"Complexidade tolerada e', '"Em B2, complexidade tolerada e', 1),
         "nivel B2"),
        ("item 5: o nivel DO config escrito no painel — nao pode reprovar",
         lambda s: s.replace("Novo ciclo no nível confirmado", "Novo ciclo em B1", 1),
         None),
        ("intervalo antigo em COMENTARIO dentro do painel — nao pode reprovar",
         lambda s: s.replace('<h3 class="sub">C · Decisão', '<!-- era aulas 23–38 no artefato -->'
                             '<h3 class="sub">C · Decisão', 1),
         None),
    ]
    falhou = False
    for nome, muta, esperado in casos:
        mutado = muta(limpo)
        if mutado == limpo:
            print(f"  FALHA  {nome:62} a mutacao nao casou no molde")
            falhou = True
            continue
        errs = confere(base, cfgs, mutado) or []
        if esperado is None:
            bom, motivo = not errs, ("ignorado, como deve" if not errs else errs[0][:60])
        else:
            bom = any(esperado in e for e in errs)
            motivo = errs[0][:60] if errs else "nao acusou nada"
        print(f"  {'OK   ' if bom else 'FALHA'}  {nome:62} {motivo}")
        falhou = falhou or not bom
    print()
    if falhou:
        print("SELFTEST FALHOU — o gate parou de morder, ou passou a morder demais.")
        return 1
    poupados = sum(1 for c in casos if c[2] is None)
    print(f"SELFTEST OK — {len(casos)} casos: {len(casos) - poupados} defeitos pegos, "
          f"{poupados} poupados como devem.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(main(sys.argv[1:]))
