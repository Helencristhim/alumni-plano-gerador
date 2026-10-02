#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sem_pista.py -- exercicio nao pode ser adivinhavel por padrao.

POR QUE ISTO EXISTE (02/10/2026)
--------------------------------
Alunos reclamaram que "a certa e sempre a B". A auditoria do repo inteiro achou
mais: 57% das certas na B e 34% na A (D quase nunca), a certa sendo a opcao mais
longa em 68% das perguntas, o "ordenar" ja aparecendo na ordem certa em 45 alunos
e o "ligar" com 1->a, 2->b. Nenhuma pagina embaralha ao abrir: o que esta no HTML
e o que o aluno ve. Quem escreve o conteudo poe a certa em segundo e a historia em
ordem; isto aqui desfaz isso na montagem, e o gate impede que volte.

O QUE FAZ (deterministico: mesma entrada, mesma saida)
- multipla escolha (.quiz-options / .ic-choices): a certa vai para uma posicao
  tirada de um saco equilibrado (A, B, C, D na mesma proporcao); as letras seguem
  A, B, C... na tela. Grupo cujo texto em volta CITA a letra ("Why C is the one",
  "a resposta e B") e pulado: reordenar faria o gabarito escrito mentir.
- ordenar (.order-container): nenhuma frase no proprio lugar, nunca invertido.
- ligar (.ic-match) e select (.match-grid): idem, quando metade ou mais esta no lugar.
- O que ele NAO resolve: a certa ser a opcao mais longa. Isso e conteudo -- uma
  opcao errada tem de ser reescrita mais longa, mantendo o MESMO erro. O gate mede.

USO
  como biblioteca:   from sem_pista import limpa, medir, problemas
  conserto manual:   python3 _build/model/sem_pista.py <slug> <aulas, ex. 5-8> [--dry]
                     (hub: so dentro de ex-lesson-N; deck: {slug}-aulaN inteiro;
                      professor primeiro, o aluno repete a decisao dele)
  checagem:          python3 _build/model/sem_pista.py --check arquivo.html [...]
"""
import hashlib, html as H, json, random, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CITA = re.compile(
    r'(?:\b(?:answer|answers|resposta|respostas|correct|certa|correta|option|opção|opcao|alternativa|key|gabarito)\b'
    r'[^<]{0,25}?\(?\b[A-Da-d]\b\)?(?![\w\'’])'
    r'|\bWhy \(?[A-D]\)? |\(\s*[a-dA-D]\s*\)|\b[1-9]\s*[-–:=]?\s*[a-dA-D]\b\s*(?:&middot;|·|,|;|<br>)'
    r'|\b(?:letra|letter)\s+[A-Da-d]\b)', re.I)


def rng(*parts):
    return random.Random(hashlib.sha1('|'.join(map(str, parts)).encode()).hexdigest())


def txt(s):
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def bloco(s, start):
    """fim do <div> que abre em start, por balanco"""
    d = 0
    for t in re.finditer(r'<div\b|</div\s*>', s[start:]):
        d += 1 if t.group(0).startswith('<div') else -1
        if d == 0:
            return start + t.end()
    raise ValueError('div nao fecha')


def filhos(inner, cls_re):
    """divide inner em (prefixo, [itens div de classe cls], sufixo) por balanco"""
    itens, pos, pre = [], 0, None
    for m in re.finditer(r'<div class="(?:%s)"' % cls_re, inner):
        if m.start() < pos:
            continue
        if pre is None:
            pre = inner[:m.start()]
        elif inner[pos:m.start()].strip():
            return None
        fim = bloco(inner, m.start())
        itens.append(inner[m.start():fim])
        pos = fim
    if pre is None:
        return None
    return pre, itens, inner[pos:]


def desarruma(n, r):
    if n < 2:
        return list(range(n))
    for _ in range(500):
        p = list(range(n)); r.shuffle(p)
        if all(i != v for i, v in enumerate(p)) and (n < 3 or p != list(range(n))[::-1]):
            return p
    return p


class Saco:
    def __init__(self, r, semente=None):
        self.r, self.sacos, self.ult, self.semente = r, {}, None, semente

    def pos(self, n):
        s = self.sacos.setdefault(n, [])
        if not s:
            s.extend(range(n)); self.r.shuffle(s)
            if n > 1 and s[-1] == self.ult:
                s.insert(0, s.pop())
        self.ult = s.pop()
        return self.ult


ST = dict(mc=0, mc_pulado=0, mc_salvo=0, mc_ja_ok=0, ordem=0, ligar=0, select=0)
DECISAO = {}     # (semente, opcoes) -> ordem ou None: o arquivo do professor decide, o do aluno repete
SALVOS = set()   # inicio (30 chars) do texto das opcoes que o aluno ja acertou, como o hub salva


def norm30(t):
    return re.sub(r'\s+', ' ', t).strip()[:30]


def mc_grupos(seg, unidade_re, saco, cls_opts, cls_opt, attr, letra_re):
    """reordena cada grupo de opcoes; unidade_re acha o container que pode citar letra"""
    out, pos = [], 0
    for m in re.finditer(r'<div class="%s"[^>]*>' % cls_opts, seg):
        if m.start() < pos:
            continue
        fim = bloco(seg, m.start())
        abre = m.group(0)
        inner = seg[m.end():fim - len('</div>')]
        f = filhos(inner, cls_opt)
        novo = seg[m.start():fim]
        if f:
            pre, itens, suf = f
            oks = [re.search(attr + r'="true"', i) is not None for i in itens]
            letras = [re.search(letra_re, i) for i in itens]
            if oks.count(True) == 1 and all(letras) and len(itens) >= 2:
                # unidade: o maior container conhecido em volta
                u0 = max([seg.rfind(x, 0, m.start()) for x in unidade_re])
                u1 = bloco(seg, u0) if u0 >= 0 else fim
                unidade = seg[u0:u1] if u0 >= 0 else novo
                chave = (str(saco.semente), tuple(txt(i) for i in itens))
                if chave in DECISAO:
                    dec = DECISAO[chave]
                elif any(norm30(H.unescape(re.sub(r'<[^>]+>', '', i))) in SALVOS for i, ok in zip(itens, oks) if ok):
                    dec = 'salvo'
                elif CITA.search(unidade.replace(novo, '')):
                    dec = 'cita'
                else:
                    alvo = saco.pos(len(itens))
                    c = oks.index(True)
                    resto = [i for i in range(len(itens)) if i != c]
                    dec = resto[:alvo] + [c] + resto[alvo:]
                DECISAO[chave] = dec
                if dec == 'salvo':
                    ST['mc_salvo'] += 1
                elif dec == 'cita':
                    ST['mc_pulado'] += 1
                else:
                    ordem = dec
                    rot = [l.group(1) for l in letras]
                    nov = []
                    for k, i in enumerate(ordem):
                        it = itens[i]
                        l = letras[i]
                        it = it[:l.start(1)] + rot[k] + it[l.end(1):]
                        nov.append(it)
                    if ordem == list(range(len(itens))):
                        ST['mc_ja_ok'] += 1
                    ST['mc'] += 1
                    novo = abre + pre + ''.join(nov) + suf + '</div>'
        out.append(seg[pos:m.start()]); out.append(novo); pos = fim
    out.append(seg[pos:])
    return ''.join(out)


def ordens(seg, r):
    def troca(m):
        abre = m.group(0)
        fim = bloco(seg, m.start())
        return abre, fim
    out, pos = [], 0
    for m in re.finditer(r'<div class="order-container"[^>]*>', seg):
        fim = bloco(seg, m.start())
        inner = seg[m.end():fim - 6]
        f = filhos(inner, r'order-item[^"]*')
        novo = seg[m.start():fim]
        if f and len(f[1]) >= 3:
            pre, itens, suf = f
            certos = [int(re.search(r'data-order="(\d+)"', i).group(1)) for i in itens]
            pela_certa = [itens[certos.index(k)] for k in sorted(certos)]
            no_lugar = sum(c == k for c, k in zip(certos, sorted(certos)))
            if no_lugar * 2 < len(itens) and certos != sorted(certos, reverse=True):
                out.append(seg[pos:m.start()]); out.append(novo); pos = fim
                continue
            p = desarruma(len(itens), rng('ordem', txt(inner)))
            sep = re.findall(r'\n\s*$', pre)
            junta = '\n' + pre.split('\n')[-1] if '\n' in pre else ''
            novo = m.group(0) + pre + junta.join(pela_certa[i] for i in p) + suf + '</div>'
            ST['ordem'] += 1
        out.append(seg[pos:m.start()]); out.append(novo); pos = fim
    out.append(seg[pos:])
    return ''.join(out)


def ligar_deck(seg):
    out, pos = [], 0
    for m in re.finditer(r'<div class="ic-match"[^>]*>', seg):
        fim = bloco(seg, m.start())
        blk = seg[m.start():fim]
        words = re.findall(r'<div class="ic-chip ic-word"[^>]*data-match="([^"]*)"', blk)
        defs = list(re.finditer(r'<div class="ic-chip ic-def"[^>]*data-k="([^"]*)"[^>]*>.*?</div>', blk, re.S))
        ks = [d.group(1) for d in defs]
        if len(words) >= 3 and defs and all(w in ks for w in words):
            fix = sum(ks.index(w) == i for i, w in enumerate(words))
            if fix * 2 >= len(words):
                # nova ordem das definicoes; letras ficam posicionais
                p = desarruma(len(defs), rng('ligar', txt(blk)))
                nova = [defs[i] for i in p]
                velho_para_novo = {}
                corpos = []
                for k, d in enumerate(nova):
                    nk = ks[k]
                    velho_para_novo[d.group(1)] = nk
                    t = d.group(0)
                    t = re.sub(r'data-k="[^"]*"', 'data-k="%s"' % nk, t, 1)
                    t = re.sub(r'(<span class="ic-k">)[^<]*(</span>)', r'\g<1>%s\g<2>' % nk, t, 1)
                    corpos.append(t)
                a, b = defs[0].start(), defs[-1].end()
                meio = blk[a:b]
                # separador entre chips
                seps = [blk[defs[i].end():defs[i + 1].start()] for i in range(len(defs) - 1)]
                if len(set(seps)) <= 1:
                    s0 = seps[0] if seps else ''
                    blk2 = blk[:a] + s0.join(corpos) + blk[b:]
                    blk2 = re.sub(r'(<div class="ic-chip ic-word"[^>]*data-match=")([^"]*)(")',
                                  lambda mm: mm.group(1) + velho_para_novo[mm.group(2)] + mm.group(3), blk2)
                    blk = blk2
                    ST['ligar'] += 1
        out.append(seg[pos:m.start()]); out.append(blk); pos = fim
    out.append(seg[pos:])
    return ''.join(out)


def selects(seg):
    out, pos = [], 0
    for g in re.finditer(r'<div class="match-grid"[^>]*>', seg):
        fim = bloco(seg, g.start())
        blk = seg[g.start():fim]
        rows = list(re.finditer(r'<div class="match-row" data-answer="([^"]*)">', blk))
        sels = list(re.finditer(r'(<select[^>]*>)(.*?)(</select>)', blk, re.S))
        if len(rows) >= 3 and len(sels) == len(rows):
            ops0 = re.findall(r'<option value="([^"]*)"', sels[0].group(2))
            ops0 = [o for o in ops0 if o]
            ans = [r.group(1) for r in rows]
            if all(a in ops0 for a in ans):
                fix = sum(ops0.index(a) == i for i, a in enumerate(ans))
                if fix * 2 >= len(ans):
                    p = desarruma(len(ops0), rng('select', txt(blk)))
                    novo_blk, last = [], 0
                    for s in sels:
                        opts = re.findall(r'[ \t]*<option value="([^"]*)">.*?</option>\n?', s.group(2))
                        linhas = re.findall(r'[ \t]*<option value="[^"]*">.*?</option>\n?', s.group(2))
                        vazio = [l for l in linhas if 'value=""' in l]
                        cheias = [l for l in linhas if 'value=""' not in l]
                        if len(cheias) != len(ops0):
                            break
                        corpo = s.group(2)
                        a, b = corpo.index(cheias[0]), corpo.rindex(cheias[-1]) + len(cheias[-1])
                        corpo = corpo[:a] + ''.join(cheias[i] for i in p) + corpo[b:]
                        novo_blk.append(blk[last:s.start()] + s.group(1) + corpo + s.group(3))
                        last = s.end()
                    else:
                        novo_blk.append(blk[last:])
                        blk = ''.join(novo_blk)
                        ST['select'] += 1
        out.append(seg[pos:g.start()]); out.append(blk); pos = fim
    out.append(seg[pos:])
    return ''.join(out)


def processa(seg, semente):
    saco = Saco(rng('saco', semente), semente)
    seg = mc_grupos(seg, ['<div class="quiz-item"'], saco, 'quiz-options', 'quiz-option[^"]*',
                    'data-correct', r'<span class="option-letter">\s*([A-Za-z])\s*</span>')
    seg = mc_grupos(seg, ['<div class="slide ', '<div class="slide"'], saco, 'ic-choices', 'ic-choice[^"]*',
                    'data-right', r'<span class="ic-opt">\s*([A-Za-z])\s*</span>')
    seg = ordens(seg, None)
    seg = ligar_deck(seg)
    seg = selects(seg)
    return seg




def limpa(fragmento, semente):
    """Tira as pistas de um pedaco de HTML (um card de aula ou um deck)."""
    return processa(fragmento, semente)


def medir(fragmento):
    """Metricas de adivinhacao de um pedaco de HTML."""
    from collections import Counter
    pos, longa, n, tam = Counter(), 0, 0, 0
    for cls, item, attr, let in (('quiz-options', 'quiz-option[^"]*', 'data-correct', 'option-letter'),
                                 ('ic-choices', 'ic-choice[^"]*', 'data-right', 'ic-opt')):
        for m in re.finditer(r'<div class="%s"[^>]*>' % cls, fragmento):
            f = filhos(fragmento[m.end():bloco(fragmento, m.start()) - 6], item)
            if not f:
                continue
            itens = f[1]
            oks = [re.search(attr + r'="true"', i) is not None for i in itens]
            if oks.count(True) != 1 or len(itens) < 2:
                continue
            ts = [txt(re.sub(r'<span class="(?:%s|ic-badge)">.*?</span>' % let, '', i)) for i in itens]
            if set(t.upper() for t in ts) <= {'TRUE', 'FALSE', 'T', 'F', 'NOT GIVEN'}:
                continue
            c = oks.index(True)
            n += 1
            tam += len(itens)
            pos[c] += 1
            L = [len(t) for t in ts]
            if L[c] == max(L) and L.count(max(L)) == 1:
                longa += 1
    ordem = 0
    for m in re.finditer(r'<div class="order-container"[^>]*>', fragmento):
        seq = [int(x) for x in re.findall(r'class="order-item[^"]*"[^>]*data-order="(\d+)"',
                                          fragmento[m.start():bloco(fragmento, m.start())])]
        if len(seq) >= 3 and (seq == sorted(seq) or seq == sorted(seq, reverse=True)):
            ordem += 1
    return dict(escolhas=n, por_posicao=dict(pos), certa_mais_longa=longa, ordenar_resolvido=ordem,
                opcoes_media=round(tam / n) if n else 3)


def _cauda(n, k, p):
    """P(X >= k) para X ~ Binomial(n, p): a chance de o padrao ser acaso."""
    from math import comb
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def problemas(met, limite=0.02):
    """O que reprova: so padrao que o acaso explica em menos de 2% das vezes.

    Com 6 perguntas de 3 opcoes, a certa ser a mais longa em 4 acontece por acaso em
    ~10% das aulas honestas; reprovar isso seria ruido. Em 5 de 6 (1,8%), nao e acaso.
    """
    out = []
    n = met['escolhas']
    k = met.get('opcoes_media') or 3
    if n >= 5:
        pos = met['por_posicao']
        c = max(pos, key=pos.get)
        if _cauda(n, pos[c], 1 / k) * k < limite:
            out.append('a certa esta na %s em %d de %d escolhas: rode '
                       '_build/model/sem_pista.py <slug> <aula> para sortear as posicoes'
                       % ('ABCDEFGH'[c], pos[c], n))
        if _cauda(n, met['certa_mais_longa'], 1 / k) < limite:
            out.append('a certa e a opcao mais longa em %d de %d escolhas: reescreva uma opcao '
                       'errada mais longa que a certa, mantendo o MESMO erro' % (met['certa_mais_longa'], n))
    if met['ordenar_resolvido']:
        out.append('%d exercicio(s) de ordenar ja aparecem na ordem certa (ou invertida): rode '
                   '_build/model/sem_pista.py <slug> <aula>' % met['ordenar_resolvido'])
    return out


def checar(paths):
    rc = 0
    for p in paths:
        s = open(p, encoding='utf-8').read()
        ps = problemas(medir(s))
        if ps:
            rc = 1
            print('❌ %s' % p)
            for x in ps:
                print('   ✗ ' + x)
        else:
            print('✅ %s: sem pista' % p)
    return rc


def faixa(s):
    out = set()
    for p in s.split(','):
        if '-' in p:
            a, b = p.split('-'); out |= set(range(int(a), int(b) + 1))
        elif p:
            out.add(int(p))
    return out


def main():
    if sys.argv[1:2] == ['--check']:
        sys.exit(checar(sys.argv[2:]))
    slug, aulas = sys.argv[1], faixa(sys.argv[2])
    dry = '--dry' in sys.argv
    for a in sys.argv[3:]:
        if a.startswith('--salvos='):
            SALVOS.update(norm30(t) for t in json.load(open(a[9:])))
    mudou = []
    for lado in ('professor', 'aluno'):
        hub = ROOT / 'public' / lado / (slug + '.html')
        if hub.exists():
            s = hub.read_text(encoding='utf-8')
            novo = s
            for m in sorted(re.finditer(r'<div class="lesson-card"[^>]*id="ex-lesson-(\d+)"', s), key=lambda m: -m.start()):
                n = int(m.group(1))
                if n not in aulas:
                    continue
                fim = bloco(novo, m.start())
                novo = novo[:m.start()] + processa(novo[m.start():fim], (slug, 'pc', n)) + novo[fim:]
            if novo != s:
                mudou.append(str(hub))
                if not dry:
                    hub.write_text(novo, encoding='utf-8')
        for n in sorted(aulas):
            d = ROOT / 'public' / lado / ('%s-aula%d.html' % (slug, n))
            if d.exists():
                s = d.read_text(encoding='utf-8')
                novo = processa(s, (slug, 'deck', n))
                if novo != s:
                    mudou.append(str(d))
                    if not dry:
                        d.write_text(novo, encoding='utf-8')
    print(json.dumps(dict(slug=slug, arquivos=len(mudou), **ST)))


if __name__ == '__main__':
    main()
