#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 73 -- a barra "Back to top" e o ULTIMO elemento da aba, e fala a lingua da tela.

O DEFEITO
---------
Dan, olhando o material no ar em 11/09/2026: *"visao aluno, aba Planning: botao 'Back to
top' esta no topo da pagina, deve vir no final da pagina."* Estava assim nos SEIS materiais
de ciclo, e eram dois defeitos com uma causa so:

  1. A BARRA VINHA PRIMEIRO. A aba Planning tem duas metades. A do professor (`perfil.html`)
     termina com a barra; o builder encaixa a do ALUNO depois dela. Na URL do professor isso
     nao aparece, porque a metade do aluno fica escondida -- na do aluno a metade do
     professor e REMOVIDA, e o que sobra e a barra seguida do conteudo. O botao de voltar ao
     topo era a primeira coisa da primeira aba que ela abre.

  2. O ROTULO CHEGAVA EM PORTUGUES. A barra do fragmento e a variante do professor
     (`Voltar ao topo`, sem os `data-view`), e o `deriva_aluno` nao tem o que trocar num
     texto que nao esta marcado por visao. REGRA 13 (A2+ = zero portugues na tela dela) e a
     regra das duas URLs, as duas violadas pela mesma linha.

POR QUE NENHUM GATE VIU
-----------------------
Cada metade estava bem formada. O HTML e valido, a barra existe, o botao funciona, o
`aoTopo()` acha o alvo, o contraste passa, nao ha overflow. O GATE 43 mede se algo vaza da
tela; o GATE 36 e o GATE 44 medem portugues na tela do aluno por LISTA DE PALAVRAS, e
"Voltar ao topo" nao e uma frase de aula. Nada media ORDEM de um elemento dentro da aba --
e ordem era o defeito.

O conserto e no builder (`ao_topo_do_shell`): a barra passa a vir do SHELL, sempre, por
ultimo, e a que o fragmento traz e descartada. Este gate e a trava de que continua assim.

O QUE ELE MEDE, no HTML publicado
---------------------------------
Para cada `<div class="tab-content" id="tab-...">` de cada material da anatomia:
  - se a aba tem barra `ao-topo`, ela e o ULTIMO no da aba (nada visivel depois dela);
  - a aba nao tem mais de uma barra;
  - no arquivo do ALUNO, o rotulo da barra esta em INGLES -- nenhum `Voltar ao topo`,
    nenhum `data-view="professor"` sobrevivente.

O QUE ELE NAO MEDE
------------------
Se a aba DEVE ter barra: ha aba curta que nao precisa. O que se mede e a barra que existe.

ESCOPO: `alumni-anatomia=consultivo`. Sem baseline -- no alumni-black nao ha legado.

USO:
    python3 scripts/consultivo/check_ao_topo_no_fim.py
    python3 scripts/consultivo/check_ao_topo_no_fim.py public/aluno/x.html
    python3 scripts/consultivo/check_ao_topo_no_fim.py --selftest
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"
MARCA = 'name="alumni-anatomia" content="consultivo"'
BARRA = '<div class="btn-bar ao-topo">'


def abas(t):
    """Cada `tab-content` e o seu corpo, pelo BALANCO de <div>.

    Nunca ate o primeiro `</div>`: a aba tem dezenas de filhos, e ler ate o primeiro
    fechamento mediria o primeiro paragrafo e chamaria isso de medir a aba -- foi
    exatamente o defeito que o GATE 41 carregou por meses no `quiz-options`."""
    for m in re.finditer(r'<div class="tab-content[^"]*" id="(tab-[a-z0-9-]+)"[^>]*>', t):
        # SEM FECHAR, o corpo e o resto do documento -- e nao o vazio. Com `i = m.end()`
        # a aba que nao fecha saia com corpo VAZIO, a barra nao era encontrada e o gate
        # pulava o arquivo em silencio: exatamente o modo de falha que ele existe para
        # acusar.
        nivel, i, fechou = 1, len(t), False
        for d in re.finditer(r"<div\b|</div>", t[m.end():]):
            nivel += 1 if d.group(0) == "<div" else -1
            if nivel == 0:
                i, fechou = m.end() + d.start(), True
                break
        yield m.group(1), t[m.end():i], fechou


def depois_da_barra(corpo):
    """O que sobra na aba depois da barra, sem espaco em branco nem comentario.

    Comentario nao chega ao olho de ninguem; quebra de linha e recuo, idem. O que conta e
    no visivel: se sobrar um, a barra nao e a ultima coisa da aba."""
    i = corpo.rfind(BARRA)
    j = corpo.find("</div>", i)
    resto = corpo[j + len("</div>"):]
    resto = re.sub(r"<!--.*?-->", "", resto, flags=re.S)
    return resto.strip()


def confere(caminho):
    t = open(caminho, encoding="utf-8", errors="replace").read()
    if MARCA not in t[:4000]:
        return [], 0
    rel = os.path.relpath(caminho, RAIZ)
    ehaluno = os.sep + "aluno" + os.sep in caminho
    falhas, medidas = [], 0
    for ident, corpo, fechou in abas(t):
        if BARRA not in corpo:
            continue
        medidas += 1
        if not fechou:
            falhas.append(f"{rel}: a aba '{ident}' nao fecha — qualquer veredito sobre a "
                          f"posicao da barra dentro dela e falso.")
            continue
        n = corpo.count(BARRA)
        if n > 1:
            falhas.append(f"{rel}: '{ident}' tem {n} barras `ao-topo`. A barra e o controle "
                          f"da aba, e ha um por aba — duas significam que o fragmento "
                          f"trouxe a dele junto com a do shell.")
        resto = depois_da_barra(corpo)
        if resto:
            falhas.append(f"{rel}: em '{ident}' a barra `ao-topo` NAO e o ultimo elemento — "
                          f"ha {len(resto)} caractere(s) de conteudo depois dela, comecando "
                          f"em {resto[:60]!r}. O botao de voltar ao topo aparece ANTES do "
                          f"que ele manda voltar.")
        if ehaluno:
            i = corpo.rfind(BARRA)
            barra = corpo[i:corpo.find("</div>", corpo.find("</button>", i)) + 6]
            if 'data-view="professor"' in barra:
                falhas.append(f"{rel}: a barra de '{ident}' ainda carrega "
                              f'data-view="professor" na URL do ALUNO.')
            visivel = re.sub(r"<[^>]+>", " ", barra)
            if re.search(r"\bVoltar ao topo\b", visivel):
                falhas.append(f"{rel}: a barra de '{ident}' diz 'Voltar ao topo' na tela da "
                              f"aluna. A2+ e ZERO portugues (REGRA 13) — o shell tem a forma "
                              f"certa, com `<span data-view=\"aluno\">Back to top</span>`.")
    return falhas, medidas


def materiais(alvos):
    if alvos:
        return alvos
    fora = []
    for sub in ("professor", "aluno"):
        for p in sorted(glob.glob(os.path.join(RAIZ, "public", sub, "*.html"))):
            with open(p, encoding="utf-8", errors="replace") as fh:
                if MARCA in fh.read(4000):
                    fora.append(p)
    return fora


def main(argv):
    falhas, abas_vistas, arquivos = [], 0, 0
    for p in materiais(argv):
        if not os.path.exists(p):
            continue
        arquivos += 1
        f, n = confere(p)
        falhas += f
        abas_vistas += n
    for f in falhas:
        print(f"{VERMELHO}FALHA{ZERA} {f}")
    if falhas:
        print(f"\n{VERMELHO}GATE 73 REPROVOU{ZERA} — {len(falhas)} problema(s) na barra "
              f"`ao-topo`.")
        return 1
    print(f"{VERDE}GATE 73 OK{ZERA} — {arquivos} material(is), {abas_vistas} aba(s) com "
          f"barra: em todas ela e o ultimo elemento, e na URL do aluno fala ingles.")
    return 0


BOM = ('<meta name="alumni-anatomia" content="consultivo">\n'
       '<div class="tab-content" id="tab-planning">\n'
       '  <p>Conteudo da aba.</p>\n'
       '  <div class="btn-bar ao-topo">\n'
       '    <button class="btn-ghost" onclick="aoTopo()">'
       '<span data-view="aluno">Back to top</span></button>\n'
       '  </div>\n'
       '</div>\n')


def selftest():
    import tempfile
    casos = [
        ("limpo", False, lambda s: s),
        ("barra antes do conteudo", True,
         lambda s: s.replace('  <p>Conteudo da aba.</p>\n', '')
                    .replace('</div>\n</div>\n', '</div>\n  <p>Conteudo da aba.</p>\n</div>\n')),
        ("rotulo em portugues na tela da aluna", True,
         lambda s: s.replace('<span data-view="aluno">Back to top</span>', 'Voltar ao topo')),
        ("data-view do professor sobrevivendo", True,
         lambda s: s.replace('<span data-view="aluno">Back to top</span>',
                             '<span data-view="professor">Voltar ao topo</span>'
                             '<span data-view="aluno">Back to top</span>')),
        ("duas barras na mesma aba", True,
         lambda s: s.replace('  <p>Conteudo da aba.</p>\n',
                             '  <div class="btn-bar ao-topo"><button class="btn-ghost" '
                             'onclick="aoTopo()">x</button></div>\n')),
        ("aba que nao fecha", True, lambda s: s.replace("</div>\n</div>\n", "</div>\n")),
    ]
    erros = 0
    for nome, deve, muta in casos:
        d = tempfile.mkdtemp()
        cam = os.path.join(d, "aluno", "x.html")
        os.makedirs(os.path.dirname(cam))
        try:
            open(cam, "w", encoding="utf-8").write(muta(BOM))
            pegou = bool(confere(cam)[0])
        finally:
            import shutil
            shutil.rmtree(d, ignore_errors=True)
        ok = pegou == deve
        erros += not ok
        print(f"  {(VERDE + 'ok' + ZERA) if ok else (VERMELHO + 'ERRO' + ZERA)}  {nome}: "
              f"esperado {'FALHA' if deve else 'passa'}, deu {'FALHA' if pegou else 'passa'}")
    print("SELFTEST OK" if not erros else f"SELFTEST com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--selftest"]
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(args))
