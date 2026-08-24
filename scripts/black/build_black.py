#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta o material da anatomia `private-black` a partir do shell e dos fragmentos da aula.

O QUE O BUILDER FAZ, E O QUE ELE NAO FAZ
----------------------------------------
FAZ: pega o shell (a FORMA, derivada do artefato por extrai_shell.py) e enfia nele o
REGISTRO do aluno e os FRAGMENTOS de cada aula. Emite os DOIS builds -- professor e aluno --
e o do aluno sai da mesma funcao que o extrator usa, `deriva_aluno`. Isso importa: o
isolamento nao e uma lista de cuidados que o builder repete, e uma propriedade estrutural do
caminho. Aula nova nao pode "esquecer" de isolar.

NAO FAZ: conteudo. Quem escreve a aula e quem escreve a aula. O builder monta, confere o que
da para conferir por construcao, e recusa se nao fechar.

O CIRCULO QUE PROVA QUE ELE REPRODUZ
------------------------------------
    artefato -> extrai_fragmentos -> builder -> material == artefato

`--round-trip` monta com os fragmentos tirados do proprio artefato e compara REGIAO POR
REGIAO com ele. Se o builder perder alguma coisa no caminho, o gate diz qual regiao e quantos
bytes. E o "prove o superset" do P2 §38 aplicado a geracao.

ASSERTS DE BUILD (recusam a geracao, nao o PR)
----------------------------------------------
  - as OITO etapas do framework, na ordem declarada, com os minutos fechando o percurso
    (Doc 03; Stephanie, 24/08/2026). NUNCA oito telas: uma etapa pode ocupar varias, e duas
    podem dividir uma.
  - o pre-class com exatamente SEIS atividades reais (Doc 04 §4.2)
  - o Teacher's Guide com os CATORZE campos (Doc 04 §8.1)

USO:
    python3 scripts/black/build_black.py _build/black/{slug}/config.json
    python3 scripts/black/build_black.py --round-trip
"""
import importlib.util
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SHELL = os.path.join(RAIZ, "_build", "model", "shells", "black.html")
ARTEFATO = os.path.join(RAIZ, "_build", "model", "artefatos", "marcos-private-black.html")

_spec = importlib.util.spec_from_file_location(
    "extrai_shell", os.path.join(os.path.dirname(os.path.abspath(__file__)), "extrai_shell.py"))
extrai_shell = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(extrai_shell)

CAMPOS_GUIA = ["identity", "goals", "product", "criteria", "prep", "language", "transcript",
               "difficulties", "scaffolding", "feedback", "evidence", "prepost", "key"]
ETAPAS = 8
PERCURSO_MIN = 55


def mascara(s):
    return extrai_shell.mascara_script_style(s)


def fecha(s, i, tag="div"):
    return extrai_shell.fecha_tag(s, i, tag)


def troca_bloco_por_id(html, ident, novo, tag="div"):
    hm = mascara(html)
    m = re.search(r"<" + tag + r'[^>]*id="' + re.escape(ident) + r'"[^>]*>', hm)
    if not m:
        raise SystemExit(f"o shell nao tem o bloco id={ident!r}")
    return html[:m.start()] + novo + html[fecha(hm, m.start(), tag):]


def troca_var(js, nome, valor):
    m = re.search(r"^var " + re.escape(nome) + r"\s*=", js, re.M)
    if not m:
        raise SystemExit(f"o shell nao declara var {nome}")
    fim = extrai_shell.fim_do_bloco(js, m.end())
    return js[:m.start()] + f"var {nome}={valor}" + js[fim:]



def troca_blocos_de_aula(html, tab_id, prefixo, seletor, aulas, rotulos, conteudos):
    """Refaz, dentro de uma aba, a barra de selecao de aula e os blocos por aula.

    O shell traz os blocos do MODELO (`pc19`, `pc20`) e os botoes que alternam entre eles.
    Um material de outras aulas nao tem onde encaixar: procurar `pc1` no shell devolve nada,
    e foi assim que a primeira geracao parou. Aqui a regiao inteira e reconstruida a partir
    do config -- quantas aulas ele declarar, tantos botoes e tantos blocos.
    """
    hm = mascara(html)
    m = re.search(r'<div[^>]*id="' + tab_id + r'"[^>]*>', hm)
    if not m:
        raise SystemExit(f"o shell nao tem a aba id={tab_id!r}")
    ini_aba, fim_aba = m.start(), fecha(hm, m.start())

    # 1. a barra de selecao: e a que chama o seletor desta aba
    barras = [mm for mm in re.finditer(r'<div class="btn-bar"[^>]*>', hm[ini_aba:fim_aba])]
    alvo = None
    for mm in barras:
        a = ini_aba + mm.start()
        b = fecha(hm, a)
        if f"{seletor}(" in html[a:b]:
            alvo = (a, b)
            break
    if alvo is None:
        raise SystemExit(f"{tab_id}: nao achei a barra que chama {seletor}()")
    botoes = []
    for i, n in enumerate(aulas):
        cls = "btn-primary" if i == 0 else "btn-ghost"
        pt, en = rotulos[n]
        botoes.append(f'<button class="{cls}" id="{prefixo}b{n}" onclick="{seletor}({n})">'
                      f'<span data-view="professor">{pt}</span>'
                      f'<span data-view="aluno">{en}</span></button>')
    nova_barra = ('<div class="btn-bar" style="justify-content:flex-start;'
                  'margin-bottom:var(--space-4)">\n    ' + "\n    ".join(botoes) + "\n  </div>")
    html = html[:alvo[0]] + nova_barra + html[alvo[1]:]

    # 2. os blocos por aula: do primeiro ao fim do ultimo
    hm = mascara(html)
    m = re.search(r'<div[^>]*id="' + tab_id + r'"[^>]*>', hm)
    ini_aba, fim_aba = m.start(), fecha(hm, m.start())
    blocos = [mm for mm in re.finditer(r'<div[^>]*id="' + prefixo + r'\d+"[^>]*>',
                                       hm[ini_aba:fim_aba])]
    if not blocos:
        raise SystemExit(f"{tab_id}: nao achei os blocos {prefixo}N do modelo")
    a = ini_aba + blocos[0].start()
    b = fecha(hm, ini_aba + blocos[-1].start())
    return html[:a] + "\n".join(conteudos) + html[b:]


def troca_slides(html, por_aula):
    """Substitui TODAS as telas do deck pelas das aulas pedidas, na ordem, e renumera
    data-slide -- o numero e posicao no deck, nao identidade da tela."""
    hm = mascara(html)
    m = re.search(r'<div class="slides-container"[^>]*>|<div class="slides-wrapper"[^>]*>', hm)
    if not m:
        raise SystemExit("o shell nao tem o container do deck")
    # o container das telas e o filho que as guarda: acha a primeira tela e a ultima
    prim = re.search(r'<div class="slide[^"]*"[^>]*data-lesson="\d+"[^>]*>', hm)
    if not prim:
        raise SystemExit("o shell nao tem tela com data-lesson")
    ini = prim.start()
    fim = ini
    for mm in re.finditer(r'<div class="slide[^"]*"[^>]*data-lesson="\d+"[^>]*>', hm):
        fim = fecha(hm, mm.start(), "div")
    novo = "\n\n".join(por_aula)
    k = 0
    def renumera(mo):
        nonlocal k
        k += 1
        return f'data-slide="{k}"'
    novo = re.sub(r'data-slide="\d+"', renumera, novo)
    return html[:ini] + novo + html[fim:], k


def monta(cfg, base_frag):
    html = open(SHELL, encoding="utf-8").read()
    aulas = cfg["aulas"]

    # ---- registro
    lessons, guides, slides, erros = [], [], [], []
    for n in aulas:
        pasta = os.path.join(base_frag, f"aula{n}")
        reg = open(os.path.join(pasta, "registro.js"), encoding="utf-8").read().strip()
        gui = open(os.path.join(pasta, "guide.js"), encoding="utf-8").read().strip()
        lessons.append(f" {n}:{reg}")
        guides.append(f" {n}:{gui}")
        slides.append(open(os.path.join(pasta, "slides.html"), encoding="utf-8").read().strip())
        erros += confere_aula(n, reg, gui, pasta)

    ini = html.rfind("<script>")
    cabeca, js = html[:ini], html[ini:]
    js = troca_var(js, "ARTEFATO", "{id:%r}" % cfg["artefato_id"])
    js = troca_var(js, "ALUNO", "{nome:%r,sobrenome:%r}" % (cfg["aluno"]["nome"],
                                                            cfg["aluno"]["sobrenome"]))
    c = cfg["ciclo"]
    js = troca_var(js, "CICLO",
                   "{numero:%d,aulas:%d,primeira:%d,porBloco:%d,nivel:%r,"
                   "rotulo:'Aulas neste ciclo',rotuloAluno:'Lessons in this cycle'}"
                   % (c["numero"], c["aulas"], c["primeira"], c["porBloco"], c["nivel"]))
    js = troca_var(js, "LESSONS", "{\n" + ",\n".join(lessons) + "\n}")
    js = troca_var(js, "GUIDE", "{\n" + ",\n".join(guides) + "\n}")
    js = js.replace("var STORE='pv_private-black-modelo_v1';",
                    "var STORE='pv_%s_v1';" % re.sub(r"[^A-Za-z0-9_-]", "-", cfg["artefato_id"]))
    js = js.replace("localStorage.getItem('pv_private-black-modelo_v1')",
                    "localStorage.getItem('pv_%s_v1')"
                    % re.sub(r"[^A-Za-z0-9_-]", "-", cfg["artefato_id"]))
    # ---- o que o artefato deixou CRAVADO em numero de aula
    #
    # O boot do artefato chama `closeBuild(19,RECAP19,CONF19); closeBuild(20,...)`, a tabela
    # BUILDERS aponta para os hosts `recapList19`/`recapList20`, e o post-class restaura por
    # ids `pw19-*`. Sao os numeros das DUAS aulas dele. Copiados como estao, a aula 1 de
    # qualquer aluno nasceria muda: o fecho nao se constroi e o texto do post-class nao volta
    # -- sem erro no console, porque `if(!host)return` engole tudo.
    #
    # Numero que descreve o MODELO e nao o MATERIAL trunca em silencio. Aqui tudo isso sai do
    # registro: quantas aulas o config declarar, tantas chamadas e tantos hosts.
    for velho in sorted(set(re.findall(r"\bvar (RECAP\d+|CONF\d+)\s*=", js))):
        js = extrai_shell.remove_var(js, velho, {})

    # PC_NOTAS: a camada do professor no pre-class. Guarda SO o que nao existe em lugar
    # nenhum do material -- alternativas que a correcao nao aceita mas o professor deve, o
    # porque, o que costuma travar, a ligacao com a aula. O gabarito em si NAO entra aqui: ele
    # e derivado do `data-ok` da propria atividade, para nao existir uma segunda versao da
    # mesma informacao, livre para divergir da primeira.
    notas = {}
    for n in aulas:
        nj = os.path.join(base_frag, f"aula{n}", "notas.json")
        if os.path.exists(nj):
            notas.update(json.load(open(nj, encoding="utf-8")))
    if notas:
        js = troca_var(js, "PC_NOTAS", json.dumps(notas, ensure_ascii=False, indent=1))
    chamadas, restaura = [], []
    for n in aulas:
        cj = os.path.join(base_frag, f"aula{n}", "close.json")
        if not os.path.exists(cj):
            erros.append(f"aula {n}: falta close.json (o recap e a escala de confianca do "
                         f"fecho). Sem ele a ultima tela nasce vazia, e sem erro no console.")
        else:
            fecho = json.load(open(cj, encoding="utf-8"))
            js = js.replace("\n/* ---------------- boot",
                            "\nvar RECAP%d=%s;\nvar CONF%d=%s;\n/* ---------------- boot"
                            % (n, json.dumps(fecho["recap"], ensure_ascii=False),
                               n, json.dumps(fecho["conf"], ensure_ascii=False)), 1)
            chamadas.append(f"closeBuild({n},RECAP{n},CONF{n});")
        restaura.append("['pw%d-subject',null,'post_l%d_subject'],"
                        "['pw%d-body','pw%d-count','post_l%d_writing']" % (n, n, n, n, n))

    # DENTRO DO BOOT, e so ali. A primeira versao usou re.sub com count=1 sobre o arquivo
    # inteiro e acertou a tabela BUILDERS, que vem antes: o boot ficou com as chamadas
    # antigas e a tabela ficou corrompida. Anteceder o alvo pelo bloco que o contem e a
    # diferenca entre trocar a chamada e trocar a primeira coisa parecida com ela.
    ib = js.index("/* ---------------- boot ---------------- */")
    fb = js.index("\n});", ib) + len("\n});")
    boot = js[ib:fb]
    boot = re.sub(r"closeBuild\(\d+,RECAP\d+,CONF\d+\);(\s*closeBuild\(\d+,RECAP\d+,CONF\d+\);)*",
                  " ".join(chamadas) if chamadas else "", boot, count=1)
    boot = re.sub(r"pwRestore\(\[.*?\]\);", "pwRestore([" + ",".join(restaura) + "]);",
                  boot, count=1, flags=re.S)
    js = js[:ib] + boot + js[fb:]

    html = cabeca + js

    # ---- regioes de conteudo
    for ident, arq in (("tab-planning", "perfil.html"), ("tab-syllabus", "syllabus.html")):
        caminho = os.path.join(base_frag, arq)
        if os.path.exists(caminho):
            html = troca_bloco_por_id(html, ident,
                                      open(caminho, encoding="utf-8").read().strip())
    rotulos, pre, post = {}, [], []
    for n in aulas:
        pasta = os.path.join(base_frag, f"aula{n}")
        reg = open(os.path.join(pasta, "registro.js"), encoding="utf-8").read()
        mod = (re.search(r"mod:'([^']+)'", reg) or [None, "—"])[1]
        rotulos[n] = (f"Aula {n:02d} &middot; {mod}", f"Lesson {n:02d}")
        pre.append(open(os.path.join(pasta, "preclass.html"), encoding="utf-8").read().strip())
        post.append(open(os.path.join(pasta, "postclass.html"), encoding="utf-8").read().strip())
    html = troca_blocos_de_aula(html, "tab-preclass", "pc", "preSel", aulas, rotulos, pre)
    html = troca_blocos_de_aula(html, "tab-postclass", "ps", "postSel", aulas, rotulos, post)
    html, n_telas = troca_slides(html, slides)

    # A tabela BUILDERS diz quem preenche qual host, e e o que faz o Reset de aula
    # reconstruir a tela em vez de deixa-la vazia. Ela vinha com os hosts do MODELO. Aqui e
    # regenerada a partir do que o material tem de fato: host que nao existe sai, e cada aula
    # declarada ganha o seu. Entrada apontando para host inexistente nao quebra nada -- e por
    # isso mesmo passaria despercebida.
    ib = html.index("var BUILDERS=[")
    ie = html.index("\n];", ib) + len("\n];")
    originais = re.findall(r"\{h:'([^']+)',\s*also:\[([^\]]*)\],\s*f:function\(\)\{([^}]*)\}\}",
                           html[ib:ie])
    entradas = []
    # 1. o que o MODELO trazia so continua se o host existir no material gerado. Entrada
    #    apontando para host inexistente nao quebra nada -- e por isso mesmo passaria
    #    despercebida, ate o dia em que um Reset deixasse a tela vazia.
    for host, also, corpo in originais:
        if "closeBuild(" in corpo:
            continue          # o fecho e por aula: entra na volta seguinte
        if f'id="{host}"' in html:
            entradas.append("  {h:'%s', also:[%s],f:function(){%s}}" % (host, also, corpo))
    # 2. o fecho de cada aula declarada
    for n in aulas:
        if f'id="recapList{n}"' in html:
            entradas.append("  {h:'recapList%d', also:['confList%d'],"
                            "f:function(){closeBuild(%d,RECAP%d,CONF%d);}}" % (n, n, n, n, n))
    html = html[:ib] + "var BUILDERS=[\n" + ",\n".join(entradas) + "\n];" + html[ie:]

    nome_inteiro = f"{cfg['aluno']['nome']} {cfg['aluno']['sobrenome']}".strip()
    html = re.sub(r"<title>.*?</title>",
                  f"<title>{nome_inteiro} — {cfg.get('titulo','Business English Program')} "
                  f"| Alumni by Better</title>", html, count=1, flags=re.S)
    return html, n_telas, erros


def confere_aula(n, registro_js, guide_js, pasta):
    """Os asserts que a norma permite provar por construcao."""
    erros = []
    etapas = re.findall(r"\{n:'([^']+)',min:(\d+)\}", registro_js)
    if len(etapas) != ETAPAS:
        erros.append(f"aula {n}: {len(etapas)} etapas declaradas, e a arquitetura do "
                     f"Documento 03 tem {ETAPAS}. (Telas podem ser quantas o conteudo pedir; "
                     f"ETAPAS, nao.)")
    soma = sum(int(m) for _, m in etapas)
    if etapas and soma != PERCURSO_MIN:
        erros.append(f"aula {n}: os minutos das etapas somam {soma}, e o percurso essencial "
                     f"e {PERCURSO_MIN} (+5 de margem).")
    slides = open(os.path.join(pasta, "slides.html"), encoding="utf-8").read()
    fases = [int(x) for x in re.findall(r'data-stage="(\d+)"', slides)]
    if fases:
        if sorted(set(fases)) != list(range(1, len(etapas) + 1)) and etapas:
            faltam = sorted(set(range(1, len(etapas) + 1)) - set(fases))
            erros.append(f"aula {n}: as telas nao representam as etapas {faltam}. "
                         f"Nenhuma etapa fica sem representacao (Doc 03 §6.1).")
        if fases != sorted(fases):
            erros.append(f"aula {n}: as etapas aparecem fora de ordem nas telas: {fases}. "
                         f"A ordem e normativa.")
    pre = open(os.path.join(pasta, "preclass.html"), encoding="utf-8").read()
    n_ativ = len(re.findall(r'class="exercise-section"', pre))
    if n_ativ != 6:
        erros.append(f"aula {n}: o pre-class tem {n_ativ} atividades, e sao exatamente SEIS "
                     f"(Doc 04 §4.2).")
    faltam = [c for c in CAMPOS_GUIA if not re.search(r"\b" + c + r"\s*:", guide_js)]
    if faltam:
        erros.append(f"aula {n}: o Teacher's Guide nao tem os campos {faltam} (Doc 04 §8.1).")
    return erros


def round_trip():
    """Monta com os fragmentos do proprio artefato e compara regiao por regiao."""
    base = os.path.join(RAIZ, "_build", "black", "_do-artefato")
    if not os.path.isdir(base):
        print("rode antes: python3 scripts/black/extrai_fragmentos.py", file=sys.stderr)
        return 1
    cfg = {
        "slug": "_round-trip",
        "artefato_id": "private-black-c02-19-38",
        "aluno": {"nome": "Marcos", "sobrenome": "Mansour"},
        "ciclo": {"numero": 2, "aulas": 20, "primeira": 19, "porBloco": 4, "nivel": "B1"},
        "aulas": [19, 20],
    }
    gerado, n_telas, erros = monta(cfg, base)
    art = open(ARTEFATO, encoding="utf-8").read()
    hm_a, hm_g = mascara(art), mascara(gerado)

    def regiao(h, hm, ident):
        m = re.search(r'<div[^>]*id="' + ident + r'"[^>]*>', hm)
        return h[m.start():fecha(hm, m.start())] if m else ""

    print("=== round-trip: artefato -> fragmentos -> builder -> material")
    dif = 0
    for ident in ("tab-planning", "tab-syllabus", "pc19", "pc20", "ps19", "ps20"):
        a, g = regiao(art, hm_a, ident), regiao(gerado, hm_g, ident)
        igual = a.strip() == g.strip()
        dif += 0 if igual else 1
        print(f"  {'igual' if igual else 'DIFERE'}  {ident:14s} artefato={len(a):7d}B  gerado={len(g):7d}B")
    # O JS por aula tambem entra no circulo: a tabela BUILDERS diz quem reconstroi cada host,
    # e uma entrada perdida so aparece no dia em que alguem usa o Reset. Comparar CONJUNTO,
    # nao ordem -- a ordem de montagem e do builder, e nao muda o que a tabela promete.
    def hosts(t):
        i = t.index("var BUILDERS=[")
        return sorted(re.findall(r"\{h:'([^']+)'", t[i:t.index("\n];", i)]))
    ha, hg = hosts(art), hosts(gerado)
    print(f"  {'igual' if ha == hg else 'DIFERE'}  BUILDERS       artefato={ha}")
    if ha != hg:
        print(f"                        gerado  ={hg}")
        dif += 1
    telas_a = len(re.findall(r'data-lesson="\d+"', hm_a))
    print(f"  {'igual' if telas_a == n_telas else 'DIFERE'}  telas          artefato={telas_a}  gerado={n_telas}")
    dif += 0 if telas_a == n_telas else 1
    for e in erros:
        print("  ASSERT:", e)
    if dif or erros:
        print(f"\nFALHOU — {dif} regiao(oes) divergente(s), {len(erros)} assert(s).")
        return 1
    print("\nOK — o builder devolve o artefato a partir dos fragmentos dele.")
    return 0


def _selftest():
    """Prova que os asserts MORDEM. Cada mutacao e um defeito que ja custou material real
    noutro molde: etapa a menos, minuto que nao fecha, atividade a mais no pre-class, campo
    do guia ausente, etapa fora de ordem."""
    import shutil
    import tempfile
    base = os.path.join(RAIZ, "_build", "black", "_do-artefato")
    if not os.path.isdir(base):
        print("rode antes: python3 scripts/black/extrai_fragmentos.py")
        return 1
    tmp = tempfile.mkdtemp(prefix="bb_")
    try:
        shutil.copytree(base, os.path.join(tmp, "f"))
        f = os.path.join(tmp, "f")
        pasta = os.path.join(f, "aula19")

        def carrega():
            return (open(os.path.join(pasta, "registro.js"), encoding="utf-8").read(),
                    open(os.path.join(pasta, "guide.js"), encoding="utf-8").read())

        reg0, gui0 = carrega()
        casos = []

        # 1 — uma etapa a menos
        reg = reg0.replace("{n:'Feedback + replay',min:7}", "", 1).replace(",\n      \n", "\n")
        casos.append(("etapa a menos", reg, gui0, "etapas declaradas"))
        # 2 — os minutos nao fecham
        reg = reg0.replace("{n:'Prediction',min:3}", "{n:'Prediction',min:4}", 1)
        casos.append(("minutos que nao fecham", reg, gui0, "somam"))
        # 3 — campo do guia ausente
        gui = re.sub(r"\n\s*evidence:", "\n  NAO_E_EVIDENCE:", gui0, count=1)
        casos.append(("campo do guia ausente", reg0, gui, "nao tem os campos"))

        for rotulo, reg, gui, esperado in casos:
            open(os.path.join(pasta, "registro.js"), "w", encoding="utf-8").write(reg)
            open(os.path.join(pasta, "guide.js"), "w", encoding="utf-8").write(gui)
            erros = confere_aula(19, reg, gui, pasta)
            if not any(esperado in e for e in erros):
                print(f"FALHA: '{rotulo}' NAO foi pego. erros={erros}")
                return 1
            print(f"  OK    {rotulo}")
        open(os.path.join(pasta, "registro.js"), "w", encoding="utf-8").write(reg0)
        open(os.path.join(pasta, "guide.js"), "w", encoding="utf-8").write(gui0)

        # 4 — atividade a menos no pre-class
        pre = os.path.join(pasta, "preclass.html")
        p0 = open(pre, encoding="utf-8").read()
        open(pre, "w", encoding="utf-8").write(p0.replace('class="exercise-section"', 'class="x"', 1))
        erros = confere_aula(19, reg0, gui0, pasta)
        open(pre, "w", encoding="utf-8").write(p0)
        if not any("atividades" in e for e in erros):
            print(f"FALHA: pre-class com 5 atividades NAO foi pego. erros={erros}")
            return 1
        print("  OK    pre-class com atividade a menos")

        # 5 — etapa fora de ordem nas telas
        sl = os.path.join(pasta, "slides.html")
        s0 = open(sl, encoding="utf-8").read()
        open(sl, "w", encoding="utf-8").write(s0.replace('data-stage="2"', 'data-stage="7"', 1))
        erros = confere_aula(19, reg0, gui0, pasta)
        open(sl, "w", encoding="utf-8").write(s0)
        if not any("fora de ordem" in e for e in erros):
            print(f"FALHA: etapa fora de ordem NAO foi pega. erros={erros}")
            return 1
        print("  OK    etapa fora de ordem nas telas")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("\nSELFTEST OK — os 5 asserts mordem.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    if "--round-trip" in sys.argv:
        return round_trip()
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cfg_path = sys.argv[1]
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    base = os.path.join(RAIZ, cfg.get("fragmentos", os.path.dirname(cfg_path)))
    prof, n_telas, erros = monta(cfg, base)
    if erros:
        for e in erros:
            print("  RECUSADO:", e)
        print(f"\n{len(erros)} problema(s). O material NAO foi escrito.")
        return 1
    aluno, _ = extrai_shell.deriva_aluno(prof)
    slug = cfg["slug"]
    p1 = os.path.join(RAIZ, "public", "professor", f"{slug}.html")
    p2 = os.path.join(RAIZ, "public", "aluno", f"{slug}.html")
    for caminho, conteudo in ((p1, prof), (p2, aluno)):
        with open(caminho, "w", encoding="utf-8") as fh:
            fh.write(conteudo)
    print(f"OK — {len(cfg['aulas'])} aula(s), {n_telas} telas")
    print(f"  {os.path.relpath(p1, RAIZ)}  {len(prof)}B")
    print(f"  {os.path.relpath(p2, RAIZ)}  {len(aluno)}B")
    return 0


if __name__ == "__main__":
    sys.exit(main())
