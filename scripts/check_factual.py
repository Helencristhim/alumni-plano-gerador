#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 25 — a fonte esta na tela, e o gabarito nao cita fonte que a aluna nao tem.

POR QUE ISTO EXISTE (11/08/2026)
--------------------------------
Camada "Factual" do 03 §6/§8, que ate hoje saia NAO VERIFICADO em todo relatorio de
validacao por nao ter gate nenhum. O documento pede:

    "Verificar existencia, autoria, data, trecho e estatuto documental."
    "Garantir que cada resposta-modelo seja sustentada pelo material apresentado ao aluno."
    "Distinguir fato, inferencia e simulacao; marcar cada um."

O QUE DA PARA AUTOMATIZAR — e o que NAO da
------------------------------------------
Conferir se uma fonte real diz o que a aula afirma exige LER a fonte: e trabalho humano, e
continua marcado como tal no relatorio. O que uma maquina consegue provar sao tres coisas,
todas medidas no artefato de referencia antes de virarem regra:

  (a) TODO texto na tela declara de onde veio. No artefato: 12 blocos `.evi` com texto, 12
      com `evi-src`. Sem isso, "diga de qual documento veio cada afirmacao" — que e um dos
      criterios do proprio ciclo — fica sem objeto: nao ha o que atribuir.
  (b) O GABARITO nao cita rotulo de fonte que nao esta na tela. Se a chave diz "Text B" e a
      aluna so tem A e C na frente, a resposta-modelo afirma mais do que a evidencia
      apresentada — exatamente o que o §6 proibe. No artefato os rotulos do gabarito sao
      subconjunto dos da tela.
  (c) MATERIAL SIMULADO NAO SE VESTE DE REAL. Cenario com link externo de veiculo real
      apresenta ficcao como documento — o pior defeito desta camada e o unico que se enxerga
      sem ler. A autenticidade sai do `syllabus.json` do aluno (`input.autenticidade`), que
      o GATE 24 ja obriga a existir.

Com `--online`, todo link externo dentro do material de leitura tambem tem de resolver
(HTTP < 400). Sem a flag, os links so sao checados quanto ao formato — o gate nao trava o
CI por rede intermitente.

ESCOPO — anatomia, nao repo
---------------------------
So os quatro frameworks da anatomia guided-discovery. `evi`/`evi-src` sao pecas do artefato;
o molde imersivo nao as tem e nao seria medido por aqui de todo jeito.

USO:
    python3 scripts/check_factual.py                 # repo inteiro
    python3 scripts/check_factual.py A.html
    python3 scripts/check_factual.py --online        # confere os links de verdade
    python3 scripts/check_factual.py --selftest
"""
import glob
import html as _html
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- O ESCOPO E O OBJETO FORAM REAPONTADOS (08/09/2026)
#
# Este gate media `<div class="evi">` + `<span class="evi-src">`, o markup do artefato da
# Erica. A anatomia que foi ao ar chama as mesmas duas coisas de `doc-brief` e `doc-fonte`.
# Medido antes do conserto: `blocos_evi()` devolvia ZERO nos seis materiais publicados --
# o gate dizia "0 falhas" porque nao achava o objeto, nao porque o material estivesse
# limpo. Trocar so o seletor de ARQUIVO teria produzido o mesmo verde falso.
# Ver `scripts/anatomia_quatro_modalidades.py`.
from anatomia_quatro_modalidades import ANATOMIA_PUBLICADA, no_escopo  # noqa: E402

ANATOMIA_GD = ('reading-into-speaking', 'listening-into-interaction',
               'grammar-for-communication', 'esp-real-world')

ROTULO_FONTE = re.compile(r'\b(?:Text|Texto|Document|Documento|Source|Fonte)\s+([A-D])\b')
MIN_TEXTO = 40  # abaixo disso o .evi e rotulo/legenda, nao material de leitura


def framework_de(h):
    m = re.search(r'<meta name="alumni-framework" content="([a-z-]+)"', h)
    return m.group(1) if m else None


def _fim_do_div(s, start):
    """Fim do <div> aberto em `start`, contando aninhamento.

    Regex nao-guloso ate o primeiro </div> pega o fecho do PRIMEIRO filho e mede o bloco
    errado — com ele, os 12 blocos de texto do artefato apareciam como 0.
    """
    i = s.index('>', start) + 1
    d = 1
    for m in re.finditer(r'<div\b|</div>', s[i:]):
        d += 1 if m.group(0) == '<div' else -1
        if d == 0:
            return i + m.end()
    return len(s)


def blocos_evi(h):
    out = []
    for m in re.finditer(r'<div class="evi"[^>]*>', h):
        out.append(h[m.start():_fim_do_div(h, m.start())])
    return out


def texto_puro(b):
    b = re.sub(r'<span class="evi-src">.*?</span>', '', b, flags=re.S)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', _html.unescape(b))).strip()


def documentos(h):
    """(titulo, tem_fonte) de cada documento reproduzido na tela, na anatomia publicada.

    `doc-brief` e o bloco; `doc-tit` o que ele e; `doc-fonte` de onde ele vem. Sao os
    mesmos tres papeis de `evi` / `evi-src` do artefato, com outro nome."""
    out = []
    for m in re.finditer(r'<div class="[^"]*\bdoc-brief\b[^"]*"[^>]*>', h):
        b = h[m.start():_fim_do_div(h, m.start())]
        t = re.search(r'class="doc-tit"[^>]*>(.*?)</p>', b, re.S)
        titulo = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', _html.unescape(t.group(1)))).strip() \
            if t else ""
        out.append((titulo, 'doc-fonte' in b))
    return out


def fonte_que_some(h):
    """O documento que se apresenta DUAS vezes e so uma delas diz de onde veio.

    POR QUE ESTA E A FORMA DA REGRA, e nao "todo bloco de texto declara fonte"
    ---------------------------------------------------------------------------
    Nem todo `doc-brief` e documento. Metade deles e BRIEFING DE CENA -- "The situation",
    "Who is on the call", "Your side" -- texto que o proprio material escreve para montar
    a tarefa. Briefing nao tem fonte porque nao veio de lugar nenhum, e exigir uma
    produziria dezoito linhas de ruido.

    Separar os dois por LEITURA do titulo seria um detector lexico, e o A05 §10.2 proibe
    aprovar ou reprovar linguagem por lista de palavras. Mas nao e preciso ler nada: o
    material JA diz quais blocos sao documento, ao atribuir fonte a eles. O que sobra e
    uma incoerencia que se mede sem dicionario -- o MESMO documento, pelo mesmo titulo,
    aparece atribuido numa tela e nu na outra.

    Medido em 08/09/2026, antes do conserto: `Witness account — Ms. Ferraz` aparece quatro
    vezes no material do Luiz e so a primeira diz de onde veio; `Incident report — officer
    on duty`, idem; `Hotel Marina · Lisbon, Portugal` aparece cinco vezes no da Vanessa e
    uma delas esta sem. A aluna reencontra o mesmo papel e na segunda vez ele nao tem
    procedencia."""
    por_titulo = {}
    for titulo, tem in documentos(h):
        if not titulo:
            continue
        por_titulo.setdefault(titulo, []).append(tem)
    return sorted(t for t, v in por_titulo.items() if any(v) and not all(v))


def autenticidade_do_syllabus(slug, n):
    p = os.path.join(RAIZ, '_build', slug, 'syllabus.json')
    if not os.path.exists(p):
        return None
    try:
        with open(p, encoding='utf-8') as fh:
            d = json.load(fh)
    except Exception:
        return None
    for a in d.get('aulas', []):
        if a.get('n') == n:
            return (a.get('input') or {}).get('autenticidade')
    return None


def verifica(paths, online=False):
    fails, checados = [], 0
    for p in paths:
        base = os.path.basename(p)
        if os.sep + 'aluno' + os.sep in p:
            continue
        with open(p, encoding='utf-8', errors='replace') as fh:
            h = fh.read()
        if not no_escopo(p, h):
            continue
        # A regra (c) precisa da aula para achar a `autenticidade` no syllabus. So a forma
        # antiga tem uma aula por arquivo; no consultivo o arquivo e o CICLO inteiro, e o
        # syllabus por aula nao existe nesse caminho. Sem os dois, (c) nao roda -- dizer
        # isto aqui e melhor do que inventar uma aula e medir a autenticidade da errada.
        m = re.search(r'^(.*)-aula(\d+)\.html$', base)
        slug, n = (m.group(1), int(m.group(2))) if m else (None, None)
        checados += 1
        rel = os.path.relpath(p, RAIZ)

        # (a') o documento que perde a fonte ao ser reapresentado (anatomia publicada)
        for titulo in fonte_que_some(h):
            fails.append(
                f'{rel}: o documento {titulo!r} aparece com <p class="doc-fonte"> numa tela '
                f'e SEM em outra. O mesmo papel, reapresentado, deixa de dizer de onde veio '
                f'— e atribuir a fonte e criterio do proprio ciclo (03 §6/§8).')

        # (a) texto na tela sem fonte declarada
        for i, b in enumerate(blocos_evi(h), 1):
            if len(texto_puro(b)) >= MIN_TEXTO and 'evi-src' not in b:
                fails.append(
                    f'{rel}: bloco de texto {i} sem <span class="evi-src"> — a aluna le o '
                    f'material e nao sabe de onde ele veio. Atribuir a fonte e criterio do '
                    f'proprio ciclo; sem o rodape nao ha o que atribuir.')

        # (b) gabarito citando fonte que nao esta na tela
        na_tela = set()
        for x in re.findall(r'<span class="evi-src">(.*?)</span>'
                            r'|<p class="doc-fonte">(.*?)</p>', h, re.S):
            x = x[0] or x[1]
            na_tela |= set(ROTULO_FONTE.findall(_html.unescape(re.sub(r'<[^>]+>', '', x))))
        gab = ' '.join(re.findall(r'<div class="rationale">(.*?)</div>', h, re.S))
        gab += ' '.join(re.findall(r'class="r-back">(.*?)</div>', h, re.S))
        no_gab = set(ROTULO_FONTE.findall(_html.unescape(re.sub(r'<[^>]+>', ' ', gab))))
        orfaos = sorted(no_gab - na_tela)
        if orfaos:
            fails.append(
                f'{rel}: o gabarito cita a fonte {orfaos} e a tela nao mostra esse rotulo '
                f'(na tela: {sorted(na_tela) or "nenhum"}). A resposta-modelo afirma mais do '
                f'que a evidencia apresentada.')

        # (c) simulado nao se veste de real + links
        links = re.findall(r'<a[^>]+href="(https?://[^"]+)"', ' '.join(blocos_evi(h)))
        aut = (autenticidade_do_syllabus(slug, n) or '').lower() if slug else ''
        if links and ('simulad' in aut or 'cenario' in aut or 'cenário' in aut):
            fails.append(
                f'{rel}: o syllabus declara o input como simulado ("{aut[:40]}...") e o '
                f'material de leitura carrega link externo {links[:2]}. Cenario com URL de '
                f'veiculo real apresenta ficcao como documento.')
        if online and links:
            import urllib.request
            for u in links:
                try:
                    req = urllib.request.Request(u, method='HEAD',
                                                 headers={'User-Agent': 'alumni-gate'})
                    urllib.request.urlopen(req, timeout=12)
                except Exception as e:
                    fails.append(f'{rel}: link do material nao resolve ({u}): {e}')
    return fails, checados


def _falso(corpo, fw='reading-into-speaking'):
    return (f'<meta name="alumni-framework" content="{fw}">'
            f'<div class="slide slide-light" data-slide="1">{corpo}</div>')


TEXTO = ('The syllabus published to families says ninety minutes per unit, and the plan for '
         'unit seven adds up to ninety-five minutes in total.')


def _consultivo(corpo):
    """Um material da anatomia publicada: carimbo de anatomia, nome que nao e `-aulaN`."""
    return (f'<meta name="alumni-anatomia" content="{ANATOMIA_PUBLICADA}">'
            f'<div class="slide slide-light" data-slide="1">{corpo}</div>')


def selftest():
    casos = [
        ('texto com fonte',
         _falso(f'<div class="evi-list"><div class="evi">'
                f'<span class="evi-src">School -- syllabus</span>{TEXTO}</div></div>'), False),
        ('texto SEM fonte',
         _falso(f'<div class="evi-list"><div class="evi">{TEXTO}</div></div>'), True),
        ('legenda curta sem fonte (nao e material de leitura)',
         _falso('<div class="evi-list"><div class="evi">Tom: yes.</div></div>'), False),
        ('gabarito citando fonte que esta na tela',
         _falso(f'<div class="evi"><span class="evi-src">Text A · plan</span>{TEXTO}</div>'
                f'<div class="rationale">Text A says ninety.</div>'), False),
        ('gabarito citando fonte que NAO esta na tela',
         _falso(f'<div class="evi"><span class="evi-src">Text A · plan</span>{TEXTO}</div>'
                f'<div class="rationale">Text B says ninety-five.</div>'), True),
        ('imersivo — nao e deste gate',
         _falso(f'<div class="evi-list"><div class="evi">{TEXTO}</div></div>',
                fw='imersivo-prototipo'), False),

        # ---- A ANATOMIA PUBLICADA: `doc-brief` / `doc-fonte`, e a fonte que some
        ('anatomia publicada: documento uma vez so, sem fonte — e briefing de cena',
         _consultivo('<div class="doc-brief"><p class="doc-tit">The situation</p>'
                     f'<p class="doc-para">{TEXTO}</p></div>'), False),
        ('anatomia publicada: as duas vezes com fonte',
         _consultivo('<div class="doc-brief"><p class="doc-tit">Witness account</p>'
                     '<p class="doc-fonte">Sample document.</p>'
                     f'<p class="doc-para">{TEXTO}</p></div>'
                     '<div class="doc-brief"><p class="doc-tit">Witness account</p>'
                     '<p class="doc-fonte">Sample document.</p>'
                     f'<p class="doc-para">{TEXTO}</p></div>'), False),
        ('anatomia publicada: reapresentado SEM a fonte que tinha',
         _consultivo('<div class="doc-brief"><p class="doc-tit">Witness account</p>'
                     '<p class="doc-fonte">Sample document.</p>'
                     f'<p class="doc-para">{TEXTO}</p></div>'
                     '<div class="doc-brief"><p class="doc-tit">Witness account</p>'
                     f'<p class="doc-para">{TEXTO}</p></div>'), True),
    ]
    import tempfile
    falhou = False
    for rotulo, htm, deve_falhar in casos:
        d = tempfile.mkdtemp()
        nome = 'zz-ciclo1.html' if 'alumni-anatomia' in htm else 'zz-aula1.html'
        p = os.path.join(d, 'professor', nome)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8') as fh:
            fh.write(htm)
        fails, _ = verifica([p])
        ok = bool(fails) == deve_falhar
        print(f"  {'OK  ' if ok else 'FALHA'}  {rotulo}")
        falhou |= not ok
    if falhou:
        print('\nSELFTEST FALHOU — o gate parou de morder.')
        return 1
    print(f'\nSELFTEST OK — os {len(casos)} casos.')
    return 0


def _sem_objeto(n_medidos):
    """Verde SEM OBJETO e o defeito que o P2 §13 nomeia: "checagem que nao falha, so nao faz
    nada". Quando este gate mede ZERO aula e existe material da anatomia consultivo no
    repo, ele diz isso -- em vez de imprimir OK e parecer cobertura.

    Nao reprova: ficar sem aula na forma antiga e estado legitimo e transitorio (o molde
    trocou de anatomia em 24/08/2026 e as aulas voltam uma por PR). O que nao pode e ficar
    invisivel."""
    import glob as _glob
    if n_medidos:
        return
    for _f in _glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")):
        try:
            with open(_f, encoding="utf-8", errors="replace") as _fh:
                if 'content="consultivo"' in _fh.read(4000):
                    print("  AVISO — SEM OBJETO: este gate mede a forma das quatro modalidades e nao"
                          " ha nenhuma aula dela no repo. O material da anatomia nova"
                          " (consultivo) NAO e coberto por ele. Reaponte-o para o"
                          " requisito, ou aposente-o com o motivo escrito (P2 §13/§23).")
                    return
        except OSError:
            pass


def main():
    if '--selftest' in sys.argv:
        return selftest()
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    paths = args or glob.glob(os.path.join(RAIZ, 'public', 'professor', '*.html'))
    fails, checados = verifica(paths, online='--online' in sys.argv)
    for f in fails:
        print(f'  FAIL  {f}')
    if fails:
        print(f'\n{len(fails)} problema(s) de fonte/gabarito em {checados} aula(s).')
        return 1
    print(f'OK — {checados} material(is) das quatro modalidades: todo texto na tela tem fonte, e o '
          f'gabarito so cita fonte que a aluna tem na frente.')
    _sem_objeto(checados)
    return 0


if __name__ == '__main__':
    sys.exit(main())
