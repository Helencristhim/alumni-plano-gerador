#!/usr/bin/env python3
"""
Remove o slide "Common Mistake" (Right vs Wrong) dos materiais IN CLASS.

Pedido do coordenador (04/08/2026). PONTO DE RETORNO: tag `pre-remove-common-mistake`.
    git checkout pre-remove-common-mistake -- public/professor/<arquivo>.html

O QUE E REMOVIDO (o slide passivo que mostra o erro e a correcao lado a lado):
  - .mistake-card / .mistake-item / .mistake-wrong / .mistake-right
  - grid inline com "&#10007; WRONG" + "&#10003; RIGHT"
  - chapter-label "Common Mistake" em qualquer outro formato

O QUE NUNCA E TOCADO:
  - Spot the Error (.error-card / revealError) — e OUTRO exercicio, interativo.
    Um slide que contenha error-card jamais e removido, mesmo que tambem
    case alguma assinatura acima.

Remover um slide do meio quebra a navegacao, porque goToSlide(n) busca
`.slide[data-slide="n"]`. Entao o script tambem:
  - renumera data-slide 1..N nos slides sobreviventes
  - atualiza `var totalSlides`
  - recalcula `lessonRanges` a partir dos data-lesson
  - remapeia os literais enterSlideMode(N) / goToSlide(N)
  - corrige as contagens "-- NN slides" dos cards de menu (no proprio
    arquivo e nos hubs que apontam para arquivos de aula por <a href>)

Uso:
    python3 scripts/remove_common_mistake.py --check
    python3 scripts/remove_common_mistake.py --apply
    python3 scripts/remove_common_mistake.py --apply public/professor/x.html
"""
import glob
import os
import re
import sys

SLIDE_OPEN = re.compile(r'<div class="slide[ "][^>]*>')
DATA_SLIDE = re.compile(r'data-slide="(\d+)"')
DATA_LESSON = re.compile(r'data-lesson="(\d+)"')


def slice_slides(html):
    """Fatia o HTML nos blocos <div class="slide ...">...</div> por balanceamento.

    Devolve [(inicio, fim)]. Levanta ValueError se o balanceamento nao fechar
    ou se os blocos se sobrepuserem (sinal de <div> solto dentro de atributo).
    """
    spans = []
    for m in SLIDE_OPEN.finditer(html):
        i = m.start()
        depth = 0
        end = None
        for t in re.finditer(r'<div\b|</div>', html[i:]):
            depth += 1 if t.group(0) == '<div' else -1
            if depth == 0:
                end = i + t.end()
                break
        if end is None:
            raise ValueError('slide sem </div> de fechamento')
        spans.append((i, end))
    for (a, b), (c, _d) in zip(spans, spans[1:]):
        if b > c:
            raise ValueError('slides sobrepostos (div solto em atributo?)')
    return spans


def is_common_mistake(block):
    """True se o bloco e o slide Common Mistake. Spot the Error nunca conta."""
    if 'revealError(' in block or 'class="error-card' in block:
        return False
    if 'mistake-card' in block or '<div class="mistake-item' in block:
        return True
    if re.search(r'chapter-label"[^>]*>\s*Common Mistakes?\s*<', block):
        return True
    if ('&#10007; WRONG' in block) and ('&#10003; RIGHT' in block):
        return True
    return False


def tag_end(html, start=0):
    """Indice logo apos o '>' que fecha a tag iniciada em `start`.

    Respeita aspas: data-teacher="<strong>...</strong>" tem '>' DENTRO do
    atributo, e um find('>') ingenuo corta a tag no lugar errado.
    """
    quote = None
    for i in range(start, len(html)):
        ch = html[i]
        if quote:
            if ch == quote:
                quote = None
        elif ch in '"\'':
            quote = ch
        elif ch == '>':
            return i + 1
    return len(html)


def set_data_slide(block, new_num):
    """Reescreve data-slide apenas na tag de abertura do slide."""
    end = tag_end(block)
    head, rest = block[:end], block[end:]
    head, n = DATA_SLIDE.subn('data-slide="%d"' % new_num, head, count=1)
    return head + rest if n else block


def _balanced_div_spans(html):
    """Todos os <div>...</div> balanceados, como (inicio, fim)."""
    spans = []
    for m in re.finditer(r'<div\b', html):
        i = m.start()
        depth = 0
        for t in re.finditer(r'<div\b|</div>', html[i:]):
            depth += 1 if t.group(0) == '<div' else -1
            if depth == 0:
                spans.append((i, i + t.end()))
                break
    return spans


WRONG_MARK = re.compile(r'&#10007;|\bWRONG\b|mistake-wrong|--danger-bg|rgba\(220,38,38')
RIGHT_MARK = re.compile(r'&#10003;|\bRIGHT\b|\bCORRECT\b|mistake-right|--success-bg|rgba\(21,128,61')
# sinais de que sobrou exercicio de verdade no slide depois de tirar o par erro/correcao
LEFTOVER = re.compile(r'onclick="(?!this\.|event)|class="fill-grid|class="speech-card|'
                      r'class="quiz-|class="ic-bank|class="comp-questions')


def strip_cm_inline(block):
    """Tira SO o par erro/correcao de um slide, preservando o resto.

    Devolve None quando nao sobra exercicio — nesse caso o slide inteiro sai.
    """
    body_at = tag_end(block)
    head, body = block[:body_at], block[body_at:]

    # menor div balanceado que contenha ao mesmo tempo o lado errado e o certo
    victims = []
    for a, b in _balanced_div_spans(body):
        seg = body[a:b]
        if WRONG_MARK.search(seg) and RIGHT_MARK.search(seg):
            victims.append((b - a, a, b))
    if not victims:
        return None
    victims.sort()
    # Do menor para o maior, aceita so quem for DISJUNTO do que ja entrou.
    # Assim o par erro/correcao entra e o .slide-inner que o contem e rejeitado
    # — do contrario o slide inteiro seria esvaziado junto com a pratica.
    chosen = []
    for _size, a, b in victims:
        if any(not (b <= x or a >= y) for x, y in chosen):
            continue
        chosen.append((a, b))
    for a, b in sorted(chosen, reverse=True):
        body = body[:a] + body[b:]

    if not LEFTOVER.search(body):
        return None

    # o slide deixa de ser "Common Mistake"
    body = re.sub(r'(<div class="chapter-label"[^>]*>)\s*Common Mistakes?\s*(</div>)',
                  r'\1Practice\2', body)
    body = re.sub(r'(<h2 class="slide-heading"[^>]*>).*?(</h2>)',
                  r'\1Quick <span class="accent">Practice</span>\2', body, count=1, flags=re.S)
    body = re.sub(r'<h3([^>]*)>\s*Quick Practice\s*</h3>', '', body, count=1)
    return head + body


# comentario-cabecalho do slide, imediatamente antes do bloco
COMMENT_TAIL = re.compile(
    r'(?:[ \t]*<!--[^>]*?-->[ \t]*\n)*[ \t]*<!--[^>]*?SLIDE\s+\d+[^>]*?-->[ \t]*\n?\s*$',
    re.IGNORECASE)


def process_file(path, text):
    """Devolve (novo_texto, n_removidos, novo_total) ou (None, 0, 0) se nada a fazer.

    Levanta ValueError se o arquivo estiver fora do formato esperado — nesse
    caso o chamador PULA o arquivo em vez de escrever algo duvidoso.
    """
    if 'class="slide' not in text:
        return None, 0, 0, 0
    spans = slice_slides(text)
    if not spans:
        return None, 0, 0, 0

    blocks = [(a, b, text[a:b]) for a, b in spans]
    if not any(is_common_mistake(s) for _a, _b, s in blocks):
        return None, 0, 0, 0

    # todo slide precisa de data-slide, senao nao da pra remapear com seguranca
    nums = []
    for _a, _b, s in blocks:
        m = DATA_SLIDE.search(s[:tag_end(s)])
        if not m:
            raise ValueError('slide sem data-slide')
        nums.append(int(m.group(1)))
    if len(set(nums)) != len(nums):
        raise ValueError('data-slide duplicado')

    # Slide hibrido (Common Mistake + pratica na mesma tela) NAO e apagado:
    # tira-se so o par erro/correcao e a pratica continua viva.
    keep, stripped = [], {}
    for i, (_a, _b, s) in enumerate(blocks):
        if not is_common_mistake(s):
            keep.append(i)
            continue
        alt = strip_cm_inline(s)
        if alt is not None:
            stripped[i] = alt
            keep.append(i)
    removed = len(blocks) - len(keep)

    # old -> new (1..N). Um numero removido aponta para o proximo sobrevivente,
    # para que qualquer link legado caia no slide seguinte em vez de no vazio.
    old2new = {}
    for new_i, old_i in enumerate(keep, start=1):
        old2new[nums[old_i]] = new_i
    for old_i, old_num in enumerate(nums):
        if old_num in old2new:
            continue
        nxt = next((j for j in keep if j > old_i), None)
        old2new[old_num] = old2new[nums[nxt]] if nxt is not None else len(keep)

    # --- recorta os blocos removidos (com o comentario-cabecalho junto) ---
    out = []
    cursor = 0
    for i, (a, b, s) in enumerate(blocks):
        head = text[cursor:a]
        if i in keep:
            out.append(head)
            out.append(set_data_slide(stripped.get(i, s), old2new[nums[i]]))
            cursor = b
            continue
        out.append(COMMENT_TAIL.sub('', head))
        cursor = b
        # engole o \n que sobrou depois do bloco
        while cursor < len(text) and text[cursor] in '\r\n':
            cursor += 1
            if text[cursor - 1] == '\n':
                break
    out.append(text[cursor:])
    new_text = ''.join(out)

    total = len(keep)

    # --- var totalSlides ---
    new_text = re.sub(r'(var\s+totalSlides\s*=\s*)\d+', r'\g<1>%d' % total, new_text)

    # --- lessonRanges, recalculado pelos data-lesson sobreviventes ---
    if 'lessonRanges' in new_text:
        per_lesson = {}
        for new_i, old_i in enumerate(keep, start=1):
            m = DATA_LESSON.search(blocks[old_i][2][:tag_end(blocks[old_i][2])])
            if m:
                ln = int(m.group(1))
                lo, hi = per_lesson.get(ln, (new_i, new_i))
                per_lesson[ln] = (min(lo, new_i), max(hi, new_i))
        if per_lesson:
            body = ', '.join('%d: { start: %d, end: %d }' % (ln, lo, hi)
                             for ln, (lo, hi) in sorted(per_lesson.items()))
            new_text = re.sub(r'var\s+lessonRanges\s*=\s*\{.*?\}\s*;',
                              'var lessonRanges = { %s };' % body, new_text, count=1, flags=re.S)

    # --- literais enterSlideMode(N) / goToSlide(N) ---
    def remap_call(m):
        n = int(m.group(2))
        return '%s(%d)' % (m.group(1), old2new.get(n, n))

    new_text = re.sub(r'\b(enterSlideMode|goToSlide)\((\d+)\)', remap_call, new_text)

    # --- "-- NN slides" nos cards de menu do proprio arquivo (monolitico) ---
    if per_lesson_counts := _lesson_counts(blocks, keep):
        new_text = _fix_inline_counts(new_text, old2new, per_lesson_counts)

    return new_text, removed, total, len(stripped)


def _lesson_counts(blocks, keep):
    counts = {}
    for new_i, old_i in enumerate(keep, start=1):
        head = blocks[old_i][2][:tag_end(blocks[old_i][2])]
        m = DATA_LESSON.search(head)
        if m:
            counts.setdefault(int(m.group(1)), []).append(new_i)
    return {k: (min(v), len(v)) for k, v in counts.items()}


def _fix_inline_counts(text, old2new, lesson_counts):
    """Nos menus internos, o card chama enterSlideMode(start) e diz 'NN slides'."""
    start2count = {start: n for _ln, (start, n) in lesson_counts.items()}

    def fix(m):
        start = int(m.group(1))
        n = start2count.get(start)
        window = m.group(2)
        if n is None:
            return m.group(0)
        return m.group(0).replace(window, re.sub(r'\b\d+(\s+slides)', r'%d\1' % n, window, count=1))

    return re.sub(r'enterSlideMode\((\d+)\)(.{0,900}?\b\d+\s+slides)', fix, text, flags=re.S)


HREF_CARD = re.compile(
    r'<a\s+href="(/(?:professor|aluno)/([a-z0-9\-]+)\.html)[^"]*"(.{0,1200}?)</a>', re.S)


def fix_hub_counts(root, new_totals):
    """Fase B: hub 'split' diz '-- 27 slides' de um arquivo de aula que encolheu."""
    touched = []
    for d in ('professor', 'aluno'):
        for path in sorted(glob.glob(os.path.join(root, 'public', d, '*.html'))):
            text = open(path, encoding='utf-8', errors='replace').read()
            if ' slides' not in text:
                continue
            orig = text

            def fix(m):
                key = '%s/%s' % (d, m.group(2))
                n = new_totals.get(key)
                if n is None:
                    return m.group(0)
                return m.group(0).replace(
                    m.group(3), re.sub(r'\b\d+(\s+slides)', r'%d\1' % n, m.group(3)))

            text = HREF_CARD.sub(fix, text)
            if text != orig:
                open(path, 'w', encoding='utf-8').write(text)
                touched.append(path)
    return touched


def main():
    apply = '--apply' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    targets = args or sorted(glob.glob(os.path.join(root, 'public', 'professor', '*.html')) +
                             glob.glob(os.path.join(root, 'public', 'aluno', '*.html')))

    changed = removed_total = stripped_total = 0
    skipped = []
    new_totals = {}
    for path in targets:
        text = open(path, encoding='utf-8', errors='replace').read()
        try:
            new_text, removed, total, n_strip = process_file(path, text)
        except ValueError as e:
            if 'mistake' in text or 'Common Mistake' in text:
                skipped.append((path, str(e)))
            continue
        if not new_text:
            continue
        changed += 1
        removed_total += removed
        stripped_total += n_strip
        rel = os.path.relpath(path, os.path.join(root, 'public'))
        new_totals[rel[:-5]] = total
        if apply:
            open(path, 'w', encoding='utf-8').write(new_text)

    hubs = fix_hub_counts(root, new_totals) if apply else []

    print('arquivos com o slide : %d' % changed)
    print('slides removidos     : %d' % removed_total)
    print('slides hibridos limpos: %d (pratica preservada)' % stripped_total)
    print('hubs com contagem ok : %d' % len(hubs))
    if skipped:
        print('\nPULADOS (fora do formato — nao foram tocados): %d' % len(skipped))
        for p, why in skipped[:20]:
            print('   %s  -- %s' % (os.path.relpath(p, root), why))
    if not apply:
        print('\n(--check: nada foi escrito. Use --apply para valer.)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
