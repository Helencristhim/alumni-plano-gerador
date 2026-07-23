#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere uma AULA (hub "snippets") no hub EXISTENTE de QUALQUER aluno.

Preenche a lacuna do build_from_model.py: em modo "snippets" o builder emite os
trechos mas NÃO toca o hub. Este tool faz a inserção de forma GENÉRICA e ADITIVA
(REGRA 20 — hub SÓ ADITIVO: NÃO toca as aulas anteriores), reaproveitando as
funções do builder (menu_card / normalize_complementary / extract_phrases /
assign_voices) para que card, complementares e audioMap saiam IDÊNTICOS ao que o
builder emitiria. Generaliza o _build/helen-mendes/insert_hub_aulaN.py por slug.

Insere por âncora de string, no hub prof E aluno:
  1. stampN na stamps-row do header (após stamp{N-1})
  2. accordion Pre-class ex-lesson-N (antes de </div><!-- /tab-exercises -->)
  3. card IN CLASS no menu, link p/ standalone (só no hub PROFESSOR — aluno tem 2 abas)
  4. bloco de Complementares lN- (antes de </div><!-- /tab-complementary -->)
  5. entradas pcN_ + [order-lN] no audioMap do hub (mescladas, sem duplicar)
  6. var totalLessons -> N

Idempotente: se ex-lesson-N já existe no hub, pula. Só faz sentido p/ hub "snippets"
(hub já existe). Aluno novo (1a aula) usa hub "new" no build_from_model.py.

USO (da raiz): python3 _build/model/insert_hub.py _build/{slug}-aula{N}/config.json
Depois: python3 _build/model/audit_hubs_struct.py --check public/professor/{slug}.html public/aluno/{slug}.html
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import build_from_model as B  # noqa: E402


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


def merge_audiomap(s, cfg, content_dir):
    """Mescla as entradas pcN_/[order-lN] no audioMap do hub.

    Dedup CONTRA AS CHAVES do audioMap existente — NÃO contra o documento inteiro:
    uma frase de Pre-class também aparece como data-phrase="..." no accordion, então
    `chave in s` dava falso-positivo e DERRUBAVA a entrada de áudio (frase ficava muda).

    Chave que JÁ EXISTE com valor DIFERENTE é ATUALIZADA, não descartada. Descartar
    deixava entrada podre no hub PARA SEMPRE: nenhum rebuild conseguia corrigir um MP3
    errado, porque o merge só olhava a chave e ignorava o valor. (Foi assim que a colisão
    de nome de arquivo do snake() sobreviveu ao rebuild — felipe-pimenta, 13/07/2026.)
    """
    # A chave PODE conter ':' ("Let me be unequivocal: we will not break the covenant.").
    # split(':')/partition(':') quebram DENTRO da chave, produzem um fragmento que nunca
    # bate com nada e a linha era re-inserida a cada insert -> chave DUPLICADA no audioMap.
    # Só um parser de verdade (chave entre aspas, com escapes) serve aqui.
    ENTRY = re.compile(r'^\s*("(?:[^"\\]|\\.)*")\s*:\s*("[^"]*")\s*,?\s*$')

    def parse(line):
        m = ENTRY.match(line)
        assert m, f'linha de audioMap não parseável: {line!r}'
        return m.group(1), m.group(2)

    existing = dict(re.findall(r'\n\s*("(?:[^"\\]|\\.)*")\s*:\s*("/audio[^"]*")', s))

    fresh = []
    for line in hub_audiomap_lines(cfg, content_dir):
        k, v = parse(line)
        old = existing.get(k)
        if old is None:
            fresh.append(line)
            existing[k] = v
        elif old != v:  # entrada podre: MESMA frase, arquivo DIFERENTE -> corrige
            s = re.sub(r'(\n\s*' + re.escape(k) + r'\s*:\s*)"/audio[^"]*"',
                       lambda m: m.group(1) + v, s)

    def add_amap(m):
        return 'var audioMap = {\n' + '\n'.join(fresh) + '\n' if fresh else m.group(0)
    s = re.sub(r'var audioMap = \{', add_amap, s, count=1)

    # dedup: chave duplicada no audioMap (herdada dos inserts com o parser quebrado).
    # Objeto JS aceita, o último vence — mas é podridão e esconde entrada errada.
    def dedup(m):
        seen, out = set(), []
        for line in m.group(1).split('\n'):
            if not line.strip():
                continue
            k = ENTRY.match(line)
            if k and k.group(1) in seen:
                continue
            if k:
                seen.add(k.group(1))
            out.append(line)
        return 'var audioMap = {\n' + '\n'.join(out) + '\n};'
    return re.sub(r'var audioMap = \{\n(.*?)\n\s*\};', dedup, s, count=1, flags=re.S)


def _block_end(s, start, open_tag='<div', close_tag='</div>'):
    """Dado `start` no '<' da tag de abertura, devolve o índice logo APÓS a tag de
    fechamento balanceada. Conta profundidade de open_tag/close_tag. HTML gerado pelo
    builder é bem-formado, então isto é exato. ('<div' não casa dentro de '</div>'.)"""
    depth, i = 0, start
    while i < len(s):
        no = s.find(open_tag, i)
        nc = s.find(close_tag, i)
        assert nc != -1, f'fechamento {close_tag} não encontrado a partir de {start}'
        if no != -1 and no < nc:
            depth += 1
            i = no + len(open_tag)
        else:
            depth -= 1
            i = nc + len(close_tag)
            if depth == 0:
                return i
    raise AssertionError('bloco não balanceado')


def _strip_enclosing(s, needle, open_tag='<div', close_tag='</div>'):
    """Remove o bloco balanceado (open_tag..close_tag) que CONTÉM `needle`.
    Devolve (s_sem_bloco, achou_bool). Remove também 1 linha em branco à esquerda."""
    pos = s.find(needle)
    if pos == -1:
        return s, False
    start = s.rfind(open_tag, 0, pos + len(needle))
    assert start != -1, f'abertura {open_tag} não encontrada antes de {needle!r}'
    end = _block_end(s, start, open_tag, close_tag)
    # apara whitespace/linha em branco imediatamente antes do bloco
    left = start
    while left > 0 and s[left - 1] in ' \t':
        left -= 1
    if left > 0 and s[left - 1] == '\n':
        left -= 1
    return s[:left] + s[end:], True


def remove_lesson_blocks(s, n, slug, is_aluno):
    """REPLACE-mode (re-nivelamento): remove SÓ os blocos da aula N do hub — accordion
    ex-lesson-N, os wrappers de Complementares lN-, o card do menu IN CLASS (só prof) e o
    stampN — para que a inserção normal recoloque as versões novas. NÃO toca em nenhuma
    outra aula. As entradas antigas de audioMap ficam como chaves órfãs inofensivas; as
    novas são mescladas/atualizadas por merge_audiomap na inserção."""
    s, _ = _strip_enclosing(s, f'id="ex-lesson-{n}"')          # accordion Pre-class
    while True:                                                # todos os media-card l{n}-
        s, found = _strip_enclosing(s, f'data-media="l{n}-')
        if not found:
            break
    if not is_aluno:                                           # card do menu (só prof)
        s, _ = _strip_enclosing(s, f'{slug}-aula{n}.html', open_tag='<a', close_tag='</a>')
    s, _ = _strip_enclosing(s, f'id="stamp{n}"')              # stamp do header
    assert f'id="ex-lesson-{n}"' not in s and f'data-media="l{n}-' not in s, \
        f'remoção incompleta da aula {n}'
    return s


def insert(hub_path, cfg, content_dir, is_aluno, replace=False):
    n = cfg['lesson']['n']
    slug = cfg['slug']
    s = read(hub_path)
    if f'id="ex-lesson-{n}"' in s:
        if replace:
            # Re-nivelamento explícito (--replace): troca os blocos da aula N pelos novos.
            s = remove_lesson_blocks(s, n, slug, is_aluno)
            print(f'  ex-lesson-{n} REMOVIDO (replace) em {os.path.basename(hub_path)} — reinserindo')
            # cai no fluxo normal de inserção abaixo
        else:
            # Aula já inserida: NÃO re-insere card/stamp/complementares (aditivo, nunca
            # duplica). Mas o audioMap AINDA é reconciliado — senão um MP3 errado no hub
            # é permanente, imune a qualquer rebuild.
            s2 = merge_audiomap(s, cfg, content_dir)
            if s2 != s:
                write(hub_path, s2)
                print(f'  ex-lesson-{n} já presente em {os.path.basename(hub_path)} — audioMap reconciliado')
            else:
                print(f'  ex-lesson-{n} já presente em {os.path.basename(hub_path)} — pulando')
            return
    folder = 'aluno' if is_aluno else 'professor'
    target = f'/{folder}/{slug}-aula{n}.html?autostart=1'
    card = B.menu_card(cfg, target)

    # 1. stampN — após stamp{N-1}. Se o config não define um stamp id=N (geração
    #    1-aula-por-vez além do bloco inicial de 5 stamps do modelo), sintetiza a
    #    partir do título da aula + recicla uma das imagens de stamp existentes.
    #    Assim nunca quebra e a stamps-row escala até N aulas (roster grande = 1
    #    stamp por aula, mesmo padrão de fabiana/rafael).
    st = next((x for x in cfg['stamps'] if x['id'] == n), None)
    if not st:
        base = cfg['stamps'][(n - 1) % len(cfg['stamps'])] if cfg.get('stamps') else {}
        label = (cfg['lesson'].get('menu_title', '').split(' -- ')[0]
                 .split(' — ')[0].strip()) or f'Lesson {n}'
        st = {'id': n, 'label': label, 'img': base.get('img', '')}
    if f'id="stamp{n}"' not in s:
        stamp_html = (f'<div class="stamp" id="stamp{n}" data-label="{st["label"]}" '
                      f"style=\"background-image:url('{st['img']}')\"></div>\n")
        anchor = s.index(f'id="stamp{n-1}"')
        end = s.index('</div>', anchor) + len('</div>') + 1
        s = s[:end] + stamp_html + s[end:]

    # 2. accordion ex-lesson-N — antes de </div><!-- /tab-exercises -->
    preclass = B.inject_kids_game(read(os.path.join(content_dir, 'preclass.html')).strip(), cfg)
    s = s.replace('</div><!-- /tab-exercises -->', '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1)

    # 3. card IN CLASS — antes de fechar a lista de cards do menu.
    #    Só o hub do PROFESSOR tem a aba IN CLASS (aluno = 2 abas, REGRA 3):
    #    no aluno a âncora não existe e o card é (corretamente) pulado.
    #    A âncora é a CLASSE/ID da aba (id="tab-inclass"), NUNCA o TEXTO do título:
    #    o título é PROSA e mudou ("Selecione a Aula" -> "Select your Lesson", REGRA 13),
    #    o que fazia esta busca falhar EM SILÊNCIO e o card do menu sumir do hub.
    if f'{slug}-aula{n}.html' not in s.split('<!-- ========== TAB 4')[0]:
        mlist = re.search(r'(id="tab-inclass".*?)(\n\s*</div>\s*</div>\s*\n\s*<!-- ========== TAB 4)',
                          s, flags=re.S)
        if mlist:
            inject_at = mlist.start(2)
            s = s[:inject_at] + '\n' + card + s[inject_at:]
        elif not is_aluno:
            raise AssertionError(f'{os.path.basename(hub_path)}: aba IN CLASS nao encontrada — '
                                 'card do menu NAO foi inserido (ancora id="tab-inclass")')

    # 4. Complementares lN- — antes de </div><!-- /tab-complementary -->
    comp = B.normalize_complementary(read(os.path.join(content_dir, 'complementary.html')), cfg).strip()
    assert f'data-media="l{n}-' in comp, f'complementary.html sem data-media="l{n}-..."'
    s = s.replace('</div><!-- /tab-complementary -->', '\n' + comp + '\n\n</div><!-- /tab-complementary -->', 1)

    # 5. audioMap: mescla pcN_/[order-lN] logo após "var audioMap = {"
    s = merge_audiomap(s, cfg, content_dir)

    # 6. totalLessons -> MAIOR aula presente no hub (a barra só enche até totalLessons —
    #    REGRA 18). NUNCA baixar: em --replace de uma aula do meio (ex: 13 num hub que já
    #    vai até 20), usar n=13 quebraria a barra. Pega o max de todas as ex-lesson-K.
    all_n = [int(x) for x in re.findall(r'id="ex-lesson-(\d+)"', s)] + [n]
    s = re.sub(r'var totalLessons\s*=\s*\d+', f'var totalLessons={max(all_n)}', s)

    assert f'id="ex-lesson-{n}"' in s and f'id="stamp{n}"' in s and f'data-media="l{n}-' in s
    assert is_aluno or f'{slug}-aula{n}.html' in s, f'card do menu IN CLASS ausente no hub prof (aula {n})'
    write(hub_path, s)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    replace = '--replace' in sys.argv  # re-nivelamento: troca os blocos de uma aula já no hub
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    cfg_path = os.path.abspath(args[0])
    content_dir = os.path.dirname(cfg_path)
    cfg = json.load(open(cfg_path, encoding='utf-8'))
    assert cfg.get('hub') == 'snippets', "insert_hub só p/ hub 'snippets' (hub existente)"
    slug, n = cfg['slug'], cfg['lesson']['n']
    prof = os.path.join(ROOT, 'public', 'professor', f'{slug}.html')
    aluno = os.path.join(ROOT, 'public', 'aluno', f'{slug}.html')
    assert os.path.exists(prof), f'hub prof inexistente: {prof} (aluno novo usa hub "new")'
    print(f'== hub professor (aula {n}){" REPLACE" if replace else ""} ==')
    insert(prof, cfg, content_dir, is_aluno=False, replace=replace)
    print(f'== hub aluno (aula {n}){" REPLACE" if replace else ""} ==')
    insert(aluno, cfg, content_dir, is_aluno=True, replace=replace)


if __name__ == '__main__':
    main()
