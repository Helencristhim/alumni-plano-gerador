#!/usr/bin/env python3
"""
retrofit_complementary.py — normaliza a aba Complementares de hubs EXISTENTES ao
layout canônico (igual maria-claudia): por aula, 1 <h4>Lesson N &mdash; Título</h4>
seguido de <div class="media-grid"> envolvendo os cards daquela aula; o link
<p><a> fica DENTRO de .media-info (último filho).

Conserta 3 classes de defeito acumuladas por insert_hub variados:
  - NO-GRID  (cards soltos em coluna única, link fora do .media-info)  ex: marcos/walyson
  - grids != aulas (h4 aninhado dentro do grid anterior)               ex: graziele 12-17
  - falta de <h4> por aula (grids ok, sem cabeçalho)                    ex: elaine/tania

INVARIANTE DE SEGURANÇA: o conjunto de data-media (cards) NUNCA muda — nenhum card
é perdido, duplicado ou reordenado dentro da aula. Idempotente.

Uso: python3 retrofit_complementary.py <hub1.html> [hub2.html ...]
     (edita in-place; imprime relatório por arquivo)
"""
import re
import sys

CANON_A_STYLE = ('display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);'
                 'font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)')

SPANISH_SLUGS = {'daniel-bastos', 'juliana-marques', 'helio-santana'}


def _match_div_end(s, start):
    """start = índice de um '<div'; retorna índice logo após o '</div>' que o fecha."""
    depth = 0
    for m in re.finditer(r'<(/?)div\b', s[start:], re.I):
        if m.group(1) == '':
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                gt = s.index('>', start + m.end())
                return gt + 1
    return -1


def _extract_comp(html):
    """Retorna (pre, body, post) onde body é o conteúdo da tab-complementary.
    Usa o sentinela <!-- /tab-complementary --> se existir; senão fecha pelo
    matching div da tab-content."""
    i = html.find('id="tab-complementary"')
    if i < 0:
        return None
    open_div = html.rfind('<div', 0, i)
    body_start = html.index('>', i) + 1
    sent = html.find('<!-- /tab-complementary -->', i)
    if sent >= 0:
        body_end = html.rfind('</div>', body_start, sent)
        post_start = body_end
    else:
        end = _match_div_end(html, open_div)
        body_end = html.rfind('</div>', body_start, end)
        post_start = body_end
    return html[:body_start], html[body_start:body_end], html[post_start:]


def _cards(body):
    """Lista de (lesson_n, card_html) em ordem de aparição."""
    out = []
    for m in re.finditer(r'<div class="media-card-wrapper" data-media="l(\d+)-[^"]*">', body):
        s = m.start()
        e = _match_div_end(body, s)
        if e < 0:
            raise RuntimeError('media-card-wrapper sem fechamento')
        out.append((int(m.group(1)), body[s:e]))
    return out


def _normalize_card(card):
    """Move o link <p><a> que está FORA do .media-info para DENTRO (último filho),
    e normaliza o style do <a> para o canônico. Idempotente."""
    mi = card.find('<div class="media-info">')
    if mi < 0:
        return card
    mi_end = _match_div_end(card, mi)            # logo após </div> do media-info
    tail = card[mi_end:]
    m = re.search(r'\s*<p[^>]*>\s*(<a\b.*?</a>)\s*</p>', tail, re.S)
    if not m:
        # já está dentro (ou não há link) — só normaliza style do <a> dentro do media-info
        return _canon_a(card)
    a_tag = m.group(1)
    new_tail = tail[:m.start()] + tail[m.end():]
    mi_block = card[mi:mi_end]
    cut = mi_block.rstrip().rfind('</div>')
    new_mi = mi_block[:cut].rstrip('\n') + '\n      <p>' + a_tag + '</p>\n    ' + mi_block[cut:]
    return _canon_a(card[:mi] + new_mi + new_tail)


def _canon_a(card):
    """Padroniza o style inline do <a> de link para o canônico (maria)."""
    def repl(m):
        return m.group(1) + CANON_A_STYLE + m.group(3)
    return re.sub(r'(<a\b[^>]*?\bstyle=")([^"]*)(")', repl, card)


def _title_maps(html):
    """(label, {n: title}) — label = 'Lección'/'Clase'/'Lesson'. Títulos vêm dos
    <h4> já existentes na aba; complementados pelos cards do menu IN CLASS."""
    body = _extract_comp(html)
    label = 'Lesson'
    titles = {}
    if body:
        for m in re.finditer(r'<h4[^>]*>\s*(Lesson|Lección|Lecci&oacute;n|Clase)\s+(\d+)\s*&mdash;\s*(.*?)</h4>',
                             body[1], re.S):
            label = m.group(1).replace('&oacute;', 'ó')
            titles[int(m.group(2))] = m.group(3).strip()
    # Pre-class: <div ... id="ex-lesson-N"> ... <h3>TITLE</h3> (fonte canônica do título da aula)
    for m in re.finditer(r'id="ex-lesson-(\d+)"', html):
        seg = html[m.end():m.end() + 800]
        t = re.search(r'<h3[^>]*>(.*?)</h3>', seg, re.S)
        if t:
            titles.setdefault(int(m.group(1)), re.sub(r'\s+', ' ', t.group(1)).strip())
    # menu IN CLASS: <div ...badge...>NN</div><div><div style="font-weight:600;font-size:.95rem">TITLE</div>
    for m in re.finditer(
            r'flex-shrink:0;background:var\(--accent\);[^>]*>\s*(\d+)\s*</div>\s*'
            r'<div>\s*<div style="font-weight:600;font-size:\.95rem">(.*?)</div>', html, re.S):
        n = int(m.group(1))
        titles.setdefault(n, m.group(2).strip())
    return label, titles


def retrofit(path):
    html = open(path, encoding='utf-8').read()
    ex = _extract_comp(html)
    if ex is None:
        return 'sem tab-complementary'
    pre, body, post = ex
    # repara tags de fechamento corrompidas no legado: "</div" sem o ">" (ex: roberto-rezende
    # l12) — fazia o parser de div engolir conteúdo da aula seguinte. Só toca a aba complementar.
    body = re.sub(r'</div(?!>)', '</div>', body)
    cards = _cards(body)
    if not cards:
        return 'sem cards'
    before_ids = sorted(re.findall(r'data-media="(l\d+-[^"]*)"', body))

    slug = path.rsplit('/', 1)[-1].replace('.html', '')
    label, titles = _title_maps(html)
    if slug in SPANISH_SLUGS and label == 'Lesson':
        label = 'Clase'

    # intro (h3 + p) = tudo antes do 1º <h4> ou 1ª media-grid/card
    first = body.find('<h4')
    g = body.find('<div class="media-grid"')
    c = body.find('<div class="media-card-wrapper"')
    cut = min(x for x in (first, g, c) if x >= 0)
    intro = body[:cut].strip()

    # agrupa por aula preservando ordem
    from collections import OrderedDict
    groups = OrderedDict()
    for n, card in cards:
        groups.setdefault(n, []).append(_normalize_card(card))

    parts = [intro, '']
    for n in sorted(groups):
        t = titles.get(n, '').strip()
        head = f'{label} {n}' + (f' &mdash; {t}' if t else '')
        parts.append(f'<h4 style="font-size:.95rem;margin:1.5rem 0 .8rem">{head}</h4>')
        parts.append('<div class="media-grid">')
        parts.append('\n'.join(groups[n]))
        parts.append('</div>')
    new_body = '\n'.join(parts) + '\n'

    new_html = pre + '\n' + new_body + post
    # INVARIANTE: mesmo conjunto de cards
    after_ids = sorted(re.findall(r'data-media="(l\d+-[^"]*)"', _extract_comp(new_html)[1]))
    if before_ids != after_ids:
        raise RuntimeError(f'{slug}: INVARIANTE QUEBRADA cards {len(before_ids)}->{len(after_ids)}')

    open(path, 'w', encoding='utf-8').write(new_html)
    nl = len(groups)
    return f'OK aulas={nl} cards={len(cards)} h4={nl} grids={nl} (label={label})'


if __name__ == '__main__':
    for p in sys.argv[1:]:
        try:
            print(f'{p.rsplit("/",1)[-1]:42} {retrofit(p)}')
        except Exception as e:
            print(f'{p.rsplit("/",1)[-1]:42} ERRO: {e}')
