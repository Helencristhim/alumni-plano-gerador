#!/usr/bin/env python3
"""
Move o slide de checagem do dialogo (Dialogue Review / Dialogue Comprehension)
para IMEDIATAMENTE depois do slide de dialogo, e renumera os data-slide.

Por que. A checagem existe para conferir o que a aluna acabou de ouvir. Parada
9 slides adiante, depois da gramatica, da pratica e dos tres role-plays, ela
deixa de ser conferencia e vira prova de memoria de longo prazo -- que e outra
habilidade. O modelo (helen-mendes) sempre poe a checagem colada no dialogo.

Idempotente: se a checagem ja e o slide seguinte ao dialogo, nao faz nada.
Renumera data-slide, ajusta o data-phase do slide movido para o da fase do
dialogo, e reescreve as referencias "slide N" dentro dos data-teacher.
"""

import re
import sys
from pathlib import Path

SLIDE_RE = re.compile(r'<div class="slide[^"]*"[^>]*data-slide="(\d+)"[^>]*>')


def split_slides(html):
    """(head, [(num, bloco)], tail). O bloco leva o comentario que o precede."""
    starts = [(m.start(), int(m.group(1))) for m in SLIDE_RE.finditer(html)]
    if not starts:
        return html, [], ""
    blocks, bounds = [], []
    for i, (pos, num) in enumerate(starts):
        # engloba o comentario "<!-- ===== SLIDE N ... -->" logo acima
        cm = list(re.finditer(r"<!--[^>]*?-->\s*$", html[: pos]))
        begin = cm[-1].start() if cm and pos - cm[-1].end() < 4 else pos
        bounds.append(begin)
    for i, begin in enumerate(bounds):
        end = bounds[i + 1] if i + 1 < len(bounds) else None
        blocks.append([starts[i][1], html[begin:end] if end else None])
    tail_start = None
    # o ultimo bloco termina no fechamento do slides-container
    last = html[bounds[-1] :]
    m = re.search(r"</div>\s*<!--\s*/slides-container", last)
    if not m:
        m = re.search(r"</div><!--\s*/slides-container", last)
    if m:
        blocks[-1][1] = last[: m.start()]
        tail_start = bounds[-1] + m.start()
    else:
        blocks[-1][1] = last
        tail_start = len(html)
    return html[: bounds[0]], blocks, html[tail_start:]


def is_dialogue(block):
    return "dialogue-line" in block


def is_check(block):
    return bool(re.search(r"Dialogue (Review|Comprehension)", block))


def process(path: Path, dry=False):
    html = path.read_text(encoding="utf-8")
    head, blocks, tail = split_slides(html)
    if not blocks:
        return f"{path.name}: sem slides"

    dlg = next((i for i, (n, b) in enumerate(blocks) if is_dialogue(b)), None)
    chk = next((i for i, (n, b) in enumerate(blocks) if is_check(b)), None)
    if dlg is None or chk is None:
        return f"{path.name}: dialogo={dlg} checagem={chk} -- nada a fazer"
    if chk == dlg + 1:
        return f"{path.name}: ja esta na ordem certa"

    old_dlg_num, old_chk_num = blocks[dlg][0], blocks[chk][0]
    phase = re.search(r'data-phase="(\d+)"', blocks[dlg][1])
    moved = blocks.pop(chk)
    if phase:  # a checagem passa a pertencer ao capitulo do dialogo
        moved[1] = re.sub(r'data-phase="\d+"', f'data-phase="{phase.group(1)}"', moved[1], count=1)
    blocks.insert(dlg + 1, moved)

    # renumera + mapeia antigo -> novo para consertar as referencias textuais
    remap = {}
    for new_num, blk in enumerate(blocks, start=1):
        remap[blk[0]] = new_num
        blk[1] = re.sub(r'data-slide="\d+"', f'data-slide="{new_num}"', blk[1], count=1)
        blk[1] = re.sub(
            r"(<!--\s*=*\s*SLIDE\s+)\d+", lambda m: m.group(1) + str(new_num), blk[1], count=1
        )
        blk[0] = new_num

    out = head + "".join(b[1] for b in blocks) + tail

    # "o dialogo do slide 19" / "volte ao slide 12" dentro dos data-teacher
    def fix_ref(m):
        n = int(m.group(2))
        return m.group(1) + str(remap.get(n, n))

    out = re.sub(r"(slide\s+)(\d+)", fix_ref, out, flags=re.I)

    if not dry:
        path.write_text(out, encoding="utf-8")
    return (
        f"{path.name}: checagem movida do slide {old_chk_num} para logo depois "
        f"do dialogo (slide {remap.get(old_dlg_num)}) -- {len(blocks)} slides renumerados"
    )


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    dry = "--dry-run" in sys.argv
    for f in args:
        print(process(Path(f), dry=dry))
