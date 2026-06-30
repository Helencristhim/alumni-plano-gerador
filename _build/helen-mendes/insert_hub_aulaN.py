#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub_aulaN.py — integra uma AULA do MODELO (n>=4) no hub helen-mendes
(prof + aluno), 100% ADITIVO (REGRA 20 / padrão "hub SÓ ADITIVO"): NÃO toca as
aulas anteriores. Generaliza o insert_hub_aula3.py por N, lendo o build da aula
(_build/helen-mendes-aula{N}/) e reaproveitando as funções do builder canônico
(menu_card / normalize_complementary / extract_phrases / assign_voices) para que
o card, os complementares e o audioMap saiam IDÊNTICOS ao que o builder emitiria.

Insere por âncora de string (mesmas âncoras testadas no aula3):
  1. stampN na stamps-row do header (após stamp{N-1})
  2. accordion Pre-class ex-lesson-N (antes de </div><!-- /tab-exercises -->)
  3. card IN CLASS no menu (link p/ standalone) — só se ainda não houver
  4. bloco de Complementares lN- (antes de </div><!-- /tab-complementary -->)
  5. entradas pcN_ + [order-lN] no audioMap do hub (mescladas, sem duplicar)
  6. var totalLessons -> N

Idempotente: se ex-lesson-N já existe, não reinsere.
USO: python3 _build/helen-mendes/insert_hub_aulaN.py 4   (depois 5)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
MODELDIR = os.path.join(ROOT, '_build', 'model')
sys.path.insert(0, MODELDIR)
import build_from_model as B  # noqa: E402

PROF = os.path.join(ROOT, 'public', 'professor', 'helen-mendes.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'helen-mendes.html')


def read(p):
    return open(p, encoding='utf-8').read()


def write(p, s):
    open(p, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(p, ROOT)} ({len(s)//1024} KB)')


def hub_audiomap_lines(cfg, content_dir):
    """pcN_ (frases do preclass, via builder) + extra_audio ([order-lN]) keyed."""
    audio_base = f'/audio/{cfg["slug"]}/'
    n = cfg['lesson']['n']
    pc = read(os.path.join(content_dir, 'preclass.html'))
    entries = B.assign_voices(B.extract_phrases(pc), prefix=f'pc{n}_', cfg=cfg)
    lines = {}
    for text, meta in entries.items():
        lines[text] = audio_base + meta['file']
    for item in cfg['lesson'].get('extra_audio', []):
        lines[item['key']] = audio_base + item['file']
    return [f'  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v)},' for k, v in lines.items()]


def insert(hub_path, cfg, content_dir, is_aluno):
    n = cfg['lesson']['n']
    s = read(hub_path)
    if f'id="ex-lesson-{n}"' in s:
        print(f'  ex-lesson-{n} já presente em {os.path.basename(hub_path)} — pulando')
        return
    target = (f'/aluno/helen-mendes-aula{n}.html?autostart=1' if is_aluno
              else f'/professor/helen-mendes-aula{n}.html?autostart=1')
    card = B.menu_card(cfg, target)

    # 1. stampN — após stamp{N-1}
    st = next((x for x in cfg['stamps'] if x['id'] == n), None)
    assert st, f'config sem stamp id={n}'
    if f'id="stamp{n}"' not in s:
        stamp_html = (f'<div class="stamp" id="stamp{n}" data-label="{st["label"]}" '
                      f"style=\"background-image:url('{st['img']}')\"></div>\n")
        anchor = s.index(f'id="stamp{n-1}"')
        end = s.index('</div>', anchor) + len('</div>') + 1
        s = s[:end] + stamp_html + s[end:]

    # 2. accordion ex-lesson-N — antes de </div><!-- /tab-exercises -->
    preclass = read(os.path.join(content_dir, 'preclass.html')).strip()
    s = s.replace('</div><!-- /tab-exercises -->', '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1)

    # 3. card IN CLASS — antes de fechar a lista de cards do menu.
    #    Só o hub do PROFESSOR tem a aba IN CLASS (aluno = 2 abas, REGRA 3):
    #    no aluno a âncora não existe e o card é (corretamente) pulado.
    if f'helen-mendes-aula{n}.html' not in s.split('<!-- ========== TAB 4')[0]:
        mlist = re.search(r'(IN CLASS -- Selecione a Aula.*?)(\n\s*</div>\s*</div>\s*\n\s*<!-- ========== TAB 4)',
                          s, flags=re.S)
        if mlist:
            inject_at = mlist.start(2)
            s = s[:inject_at] + '\n' + card + s[inject_at:]

    # 4. Complementares lN- — antes de </div><!-- /tab-complementary -->
    comp = B.normalize_complementary(read(os.path.join(content_dir, 'complementary.html')), cfg).strip()
    assert f'data-media="l{n}-' in comp, f'complementary.html sem data-media="l{n}-..."'
    s = s.replace('</div><!-- /tab-complementary -->', '\n' + comp + '\n\n</div><!-- /tab-complementary -->', 1)

    # 5. audioMap: mescla pcN_/[order-lN] logo após "var audioMap = {"
    new_lines = hub_audiomap_lines(cfg, content_dir)

    def add_amap(m):
        existing = m.group(0)
        adds = '\n'.join(l for l in new_lines if l.split(':')[0].strip() not in existing)
        return 'var audioMap = {\n' + adds + '\n' if adds else m.group(0)
    s = re.sub(r'var audioMap = \{', add_amap, s, count=1)

    # 6. totalLessons -> N
    s = re.sub(r'var totalLessons\s*=\s*\d+', f'var totalLessons={n}', s)

    assert f'id="ex-lesson-{n}"' in s and f'id="stamp{n}"' in s and f'data-media="l{n}-' in s
    low = s.lower()
    assert 'roberto' not in low and 'pricila' not in low
    write(hub_path, s)


def main():
    n = int(sys.argv[1])
    content_dir = os.path.join(ROOT, '_build', f'helen-mendes-aula{n}')
    cfg = json.load(open(os.path.join(content_dir, 'config.json'), encoding='utf-8'))
    assert cfg['lesson']['n'] == n
    print(f'== hub professor (aula {n}) ==')
    insert(PROF, cfg, content_dir, is_aluno=False)
    print(f'== hub aluno (aula {n}) ==')
    insert(ALUNO, cfg, content_dir, is_aluno=True)


if __name__ == '__main__':
    main()
