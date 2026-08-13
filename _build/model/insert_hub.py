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

Idempotente POR BLOCO (não por aula): insere o que falta, pula o que já existe. Um
hub que ficou meio inserido — Pre-class dentro, Complementares fora — se cura ao
rodar de novo. Até 10/08/2026 um único `if ex-lesson-N in s: return` decidia por
todos os blocos, e o meio-inserido era permanente: 9 aulas em 5 alunos ficaram sem
NENHUM card de Complementares. Só faz sentido p/ hub "snippets" (hub já existe).
Aluno novo (1a aula) usa hub "new" no build_from_model.py.

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


FIM_COMP = '</div><!-- /tab-complementary -->'


def fim_da_aba(s, tab_id, nome):
    """Índice do </div> que FECHA a aba `tab_id`, em hub SEM o marcador de comentário.

    Os marcadores (`</div><!-- /tab-... -->`) são convenção do hub que o builder emite
    ("new"), e só uma minoria dos hubs do repo os tem — os anteriores ao modelo fecham a
    aba com um </div> mudo. Sem este fallback o insert_hub aborta num assert em TODO hub
    legado (mark-kazuyoshi na aba Complementares, gabriela-pires nas abas Pre-class e IN
    CLASS), e a saída seria montar o hub à mão — exatamente o que a REGRA 20 proíbe.

    Fecha-se pelo BALANÇO de <div> a partir do id da aba. Emendar "no fim do arquivo" ou
    "antes da aba seguinte" jogaria o bloco FORA da aba, que é o defeito ORPHAN/ESCAPE que
    o audit_hubs_struct existe para pegar.
    """
    m = re.search(r'<div[^>]*id="' + re.escape(tab_id) + r'"[^>]*>', s)
    assert m, f'aba {nome} não encontrada no hub (id="{tab_id}")'
    depth = 1
    for t in re.finditer(r'<div\b|</div\s*>', s[m.end():]):
        depth += 1 if t.group(0).startswith('<div') else -1
        if depth == 0:
            return m.end() + t.start()
    raise AssertionError(f'aba {nome} não fecha (<div> desbalanceada no hub)')


def fim_tab_complementary(s):
    return fim_da_aba(s, 'tab-complementary', 'Complementares')


def fim_tab_exercises(s):
    return fim_da_aba(s, 'tab-exercises', 'Pre-class')


def menu_card_do_hub(s, cfg, target):
    """O card do menu IN CLASS **no formato QUE AQUELE HUB JÁ USA**.

    O builder emite o card FLEX do modelo. Boa parte dos hubs anteriores ao modelo usa o
    card HERO (`.inclass-lesson-card` + `.ilc-icon/.ilc-info/.ilc-number/.ilc-title/
    .ilc-desc/.ilc-arrow`), cujo CSS vive no próprio hub. Enfiar um card flex ali produz
    duas coisas ao mesmo tempo:

      * a REGRA 11.9 (uniformidade visual) quebrada — cards de tamanhos diferentes na
        mesma lista, que é exatamente o que a REGRA 2 proíbe ("NUNCA misturar formatos");
      * a flag **MENU_MIX** do audit_hubs_struct, que BLOQUEIA o PR.

    A saída NÃO é reescrever o menu do hub (isso é mexer no legado — REGRA 30): é o card
    novo NASCER no formato da casa. Detecta-se pelo que já está na região do tab-inclass;
    hub do modelo (sem `.inclass-lesson-card`) continua recebendo o card flex, byte a byte
    igual ao de antes.
    """
    i = s.find('id="tab-inclass"')
    j = s.find('id="tab-complementary"', i) if i >= 0 else -1
    if i < 0 or j < 0 or 'class="inclass-lesson-card"' not in s[i:j]:
        return B.menu_card(cfg, target)
    L = cfg['lesson']
    return (
        f'<a class="inclass-lesson-card" href="{target}" style="text-decoration:none;">\n'
        f'  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>'
        f'</svg></div>\n'
        f'  <div class="ilc-info">\n'
        f'    <div class="ilc-number">Lesson {L["menu_num"]}</div>\n'
        f'    <div class="ilc-title">{L["menu_title"]}</div>\n'
        f'    <div class="ilc-desc">{L["menu_desc"]}</div>\n'
        f'  </div>\n'
        f'  <div class="ilc-arrow">&rarr;</div>\n'
        f'</a>')


def hub_audiomap_lines(cfg, content_dir):
    """pcN_ (frases do preclass, via builder) + extra_audio ([order-lN]) keyed."""
    audio_base = f'/audio/{cfg["slug"]}/'
    n = cfg['lesson']['n']
    # MODELO KIDS: não há Pre-class. As frases do percurso vivem no AUDIO_MAP dele
    # (dentro do postclass.js, preenchido pelo builder), não no audioMap do hub.
    entries = {}
    if cfg.get('model') != 'kids':
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
    if replace and f'id="ex-lesson-{n}"' in s:
        # Re-nivelamento explícito (--replace): troca os blocos da aula N pelos novos.
        s = remove_lesson_blocks(s, n, slug, is_aluno)
        print(f'  ex-lesson-{n} REMOVIDO (replace) em {os.path.basename(hub_path)} — reinserindo')

    # ── IDEMPOTÊNCIA POR BLOCO, não por aula (10/08/2026) ────────────────────────
    # Antes, um único `if ex-lesson-N in s: return` decidia por TODOS os seis blocos.
    # Consequência: hub que ficou MEIO inserido nunca mais se curava. Se a primeira
    # execução colocou o accordion do Pre-class e abortou nos Complementares (era o
    # que o assert de `fim_tab_complementary` fazia em TODO hub legado, consertado
    # hoje), qualquer nova tentativa via o ex-lesson-N, dizia "já presente — pulando"
    # e ia embora. O aluno ficava com a aba Complementares VAZIA naquela aula, para
    # sempre, e nenhum rebuild consertava.
    #
    # Medido em 10/08/2026, no roster ativo: 9 aulas em 5 alunos sem NENHUM card de
    # Complementares — rafael-gasparelli-lima 6-10, e a aula 5 de mark-kazuyoshi,
    # dienane, andreia-heins e carolina-paludetto. Quatro alunos perdendo EXATAMENTE
    # a aula 5 não é coincidência: é assinatura desta trava.
    #
    # O padrão certo já existia no arquivo — stamp e card do menu sempre tiveram
    # guarda própria (`if id="stampN" not in s`). Faltava aplicá-lo aos outros dois,
    # e parar de sair antes de chegar neles.
    #
    # Cada bloco também só LÊ seu arquivo quando vai inserir: assim um conserto que
    # precisa só dos Complementares não exige um preclass.html que talvez nem exista
    # (é o caso das 9 aulas acima, cujo _build sumiu).
    # MODELO KIDS: o slot do Pre-class virou o PERCURSO (post-class) — decisão do Dan
    # (13/08/2026). "Já inserido" passa a ser o card do percurso, não o accordion.
    kids = cfg.get('model') == 'kids'
    tem_preclass = f'enterPostMode({n})' in s if kids else f'id="ex-lesson-{n}"' in s
    tem_comp = f'data-media="l{n}-' in s
    feitos, pulados = [], []
    folder = 'aluno' if is_aluno else 'professor'
    target = f'/{folder}/{slug}-aula{n}.html?autostart=1'
    card = menu_card_do_hub(s, cfg, target)

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
    if f'id="stamp{n}"' in s:
        pulados.append('stamp')
    else:
        feitos.append('stamp')
    if f'id="stamp{n}"' not in s:
        stamp_html = (f'<div class="stamp" id="stamp{n}" data-label="{st["label"]}" '
                      f"style=\"background-image:url('{st['img']}')\"></div>\n")
        if n > 1 and f'id="stamp{n-1}"' in s:
            anchor = s.index(f'id="stamp{n-1}"')
            end = s.index('</div>', anchor) + len('</div>') + 1
            s = s[:end] + stamp_html + s[end:]
        else:
            # AULA 1 (ou stamp anterior ausente): não existe stamp{n-1} para ancorar.
            # Acontece em --replace da aula 1 (o remove_lesson_blocks tira o stamp1 e a
            # reinserção procurava "stamp0" -> ValueError). O stamp entra como PRIMEIRO
            # da stamps-row. Nunca contornar montando o hub à mão (REGRA 20).
            m = re.search(r'<div class="stamps-row"[^>]*>', s)
            assert m, 'stamps-row não encontrada no hub — não dá para inserir o stamp'
            s = s[:m.end()] + '\n' + stamp_html + s[m.end():]

    # 2. accordion ex-lesson-N (só quando falta — ver idempotência por bloco acima)
    if kids:
        # KIDS: strip_preclass é idempotente (no 2º insert a aba já não existe) e
        # inject_kids_postclass é ADITIVO — lê o PV_POSTS que já está no hub e só
        # acrescenta este percurso.
        post = B.kids_post_payload(cfg, content_dir, [])
        assert post, (f'aula {n} de {slug} é kids mas não tem postclass.html — no modelo '
                      f'kids o homework É o percurso')
        s, era_ativa = B.strip_preclass(s, cfg)
        s = B.inject_kids_postclass(s, cfg, [post], ativar=era_ativa)
        (pulados if tem_preclass else feitos).append('post-class')
    elif tem_preclass:
        pulados.append('pre-class')
    else:
        preclass = B.inject_kids_game(read(os.path.join(content_dir, 'preclass.html')).strip(), cfg)
        # CARIMBO DE GERAÇÃO NO BLOCO. O hub nunca ganha <meta name="alumni-gen"> (o insert_hub
        # só injeta trechos num arquivo antigo), então gate escopado por geração era CEGO para
        # o Pre-class inteiro. Carimbar o hub seria pior: passaria a cobrar as invariantes novas
        # dos blocos LEGADOS que convivem nele (REGRA 30). O carimbo vai no accordion que ESTE
        # build emitiu — e o gate lê o bloco. Espelha build_from_model.build_hub_snippets().
        preclass = re.sub(r'<div class="lesson-card"(?![^>]*\bdata-gen=)',
                          f'<div class="lesson-card" data-gen="{B.BUILDER_GEN}"', preclass, count=1)
        # POSIÇÃO NUMÉRICA, nunca "no fim da aba". Mesma classe de bug já corrigida no menu IN
        # CLASS (incidente maria-claudia) — aqui tinha ficado para trás: em --replace de uma aula
        # do MEIO, o accordion voltava depois de todos os outros e a aluna via a aula 1 embaixo
        # da aula 2. Acha o 1º ex-lesson-K com K > n e insere ANTES dele; se nenhum, no fim.
        fim_aba = s.find('</div><!-- /tab-exercises -->')
        if fim_aba < 0:
            fim_aba = fim_tab_exercises(s)
        depois = [m.start() for m in re.finditer(r'<div class="lesson-card"[^>]*id="ex-lesson-(\d+)"',
                                                 s[:fim_aba]) if int(m.group(1)) > n]
        if depois:
            ini = s.rfind('\n', 0, min(depois)) + 1
            s = s[:ini] + preclass + '\n\n' + s[ini:]
        else:
            s = s[:fim_aba] + '\n' + preclass + '\n\n' + s[fim_aba:]
        feitos.append('pre-class')

    # 3. card IN CLASS — antes de fechar a lista de cards do menu.
    #    Só o hub do PROFESSOR tem a aba IN CLASS (aluno = 2 abas, REGRA 3):
    #    no aluno a âncora não existe e o card é (corretamente) pulado.
    #    A âncora é a CLASSE/ID da aba (id="tab-inclass"), NUNCA o TEXTO do título:
    #    o título é PROSA e mudou ("Selecione a Aula" -> "Select your Lesson", REGRA 13),
    #    o que fazia esta busca falhar EM SILÊNCIO e o card do menu sumir do hub.
    # O MARCADOR DE FIM E GENERICO. Era a string literal "TAB 4", o que amarrava o insert a
    # UMA ordem de abas: na anatomia guided-discovery o IN CLASS e a aba 4 e quem vem depois
    # e a 5, entao a ancora nunca casava e o card do menu nao entrava — a aula nascia ORFA.
    # O que importa e "o proximo comentario de aba", nao o numero dele.
    FIM_ABA = '<!-- ========== TAB '
    #
    #    AULA MONOLITICA NAO GANHA CARD. O card aponta para o standalone
    #    ({slug}-aula{N}.html). Em hub monolitico os slides moram DENTRO do hub e o menu
    #    abre por enterSlideMode(N) — o arquivo nao existe. Sem esta guarda, curar uma
    #    aula desse tipo plantava um <a href> para 404, DUPLICADO com o card que ja esta
    #    la. Medido em 10/08/2026: 8 das 9 aulas a consertar (rafael-gasparelli 6-10,
    #    mark-kazuyoshi 5, andreia-heins 5, carolina-paludetto 5) sao monoliticas.
    tem_standalone = os.path.exists(
        os.path.join(ROOT, 'public', 'aluno' if is_aluno else 'professor',
                     f'{slug}-aula{n}.html'))
    if not tem_standalone:
        pulados.append('card-menu(aula monolitica: abre por enterSlideMode)')
    elif f'{slug}-aula{n}.html' not in s.split(FIM_ABA)[0]:
        mlist = re.search(r'(id="tab-inclass".*?)(\n\s*</div>\s*</div>\s*\n\s*<!-- ========== TAB )',
                          s, flags=re.S)
        if not mlist and not is_aluno and 'id="tab-inclass"' in s:
            # HUB LEGADO: a âncora `<!-- ========== TAB 4` é convenção do hub que o builder
            # emite ("new"). O hub anterior ao modelo fecha a aba IN CLASS com um </div> mudo
            # e vai direto para a aba Complementares — a regex acima não casa e o card do
            # menu NÃO nascia (gabriela-pires, aula 21). Mesmo fallback por BALANÇO de <div>
            # das outras duas abas: o card entra DENTRO da aba, nunca depois dela (senão é o
            # ORPHAN/ESCAPE que o audit_hubs_struct pega).
            mi = re.search(r'<div[^>]*id="tab-inclass"[^>]*>', s)
            region_start, region_end = mi.end(), fim_da_aba(s, 'tab-inclass', 'IN CLASS')
            after = [region_start + m.start()
                     for m in re.finditer(re.escape(slug) + r'-aula(\d+)\.html',
                                          s[region_start:region_end])
                     if int(m.group(1)) > n]
            if after:
                line_start = s.rfind('\n', region_start, min(after)) + 1
                s = s[:line_start] + card + '\n' + s[line_start:]
            else:
                s = s[:region_end] + '\n' + card + '\n' + s[region_end:]
        elif mlist:
            region_start, region_end = mlist.start(1), mlist.start(2)
            # Insere o card na POSIÇÃO NUMÉRICA certa — nunca só "no fim da lista". O anchor
            # de fim fazia a ordem do MENU seguir a ORDEM DE INSERÇÃO em vez do número da
            # aula: gerar fora de ordem (aula 20 de review antes da 14) ou --replace de uma
            # aula do meio empilhava o card no lugar errado (incidente maria-claudia: o menu
            # saiu 20,19,18,17,16,15,14). Acha o 1º card cuja aula K > n e insere ANTES dele;
            # se nenhum (n é a maior), insere no fim — mesmo comportamento de antes.
            after = [region_start + m.start()
                     for m in re.finditer(re.escape(slug) + r'-aula(\d+)\.html',
                                          s[region_start:region_end])
                     if int(m.group(1)) > n]
            if after:
                line_start = s.rfind('\n', region_start, min(after)) + 1
                s = s[:line_start] + card + '\n' + s[line_start:]
            else:
                s = s[:region_end] + '\n' + card + s[region_end:]
        elif not is_aluno:
            raise AssertionError(f'{os.path.basename(hub_path)}: aba IN CLASS nao encontrada — '
                                 'card do menu NAO foi inserido (ancora id="tab-inclass")')

    # 4. Complementares lN-
    #    SO em anatomia que TEM a aba. A guided-discovery nao tem (decisao do Dan,
    #    06/08/2026), e ali o bloco nao teria onde entrar. Quem decide e a ANATOMIA
    #    DECLARADA, nunca o sintoma "o hub nao tem a aba" — 9 hubs LEGADOS tambem nao
    #    tem, e neles a ausencia e DEFEITO.
    if not B.tem_aba_complementares(cfg):
        pulados.append('complementares(anatomia sem a aba)')
    #    Onde entra: em POSIÇÃO NUMÉRICA dentro da aba. Mesma correção que o accordion
    #    (#2) e o card do menu (#3) já tinham: emendar "no fim da aba" só está certo
    #    quando a aula é a MAIS ALTA. Ao curar uma aula do meio (a 5 num hub que vai até
    #    a 24), o bloco caía depois da 24 e a aluna via "Aula 5" no pé da lista. Acha o
    #    1º l{K} com K > n e insere ANTES dele.
    elif tem_comp:
        pulados.append('complementares')
    else:
        comp = B.normalize_complementary(read(os.path.join(content_dir, 'complementary.html')), cfg).strip()
        assert f'data-media="l{n}-' in comp, f'complementary.html sem data-media="l{n}-..."'
        fim_comp_idx = s.find(FIM_COMP)
        if fim_comp_idx < 0:
            fim_comp_idx = fim_tab_complementary(s)
        ini_comp = s.find('id="tab-complementary"')
        depois_c = [m.start() for m in re.finditer(r'data-media="l(\d+)-',
                                                   s[ini_comp:fim_comp_idx])
                    if int(m.group(1)) > n]
        if depois_c:
            # Sobe ACIMA do CABECALHO do grupo da aula K, nao so do card.
            # A aba e uma sequencia de grupos:
            #     <h4>Lesson K — ...</h4>
            #     <div class="media-grid"> ...3 cards... </div>
            # Parar no primeiro `media-card-wrapper` emendava DENTRO da media-grid da
            # aula K: o <h4> da aula N virava uma celula do grid da aula K (que e
            # grid-template-columns:repeat(auto-fill,minmax(280px,1fr))), aparecendo
            # sob o titulo errado e com os 3 cards espremidos numa celula. Reproduzido
            # nos 5 alunos em 10/08/2026.
            alvo = ini_comp + min(depois_c)
            # O mais EXTERNO que existir antes do card: <h4> do grupo, senao a
            # media-grid, senao o proprio wrapper. Nesta ordem, sempre.
            marco = next((k for k in (s.rfind('<h4', ini_comp, alvo),
                                      s.rfind('<div class="media-grid"', ini_comp, alvo),
                                      s.rfind('<div class="media-card-wrapper"', ini_comp, alvo))
                          if k > 0), alvo)
            ini = s.rfind('\n', ini_comp, marco) + 1
            s = s[:ini] + comp + '\n\n' + s[ini:]
        elif FIM_COMP in s:
            s = s.replace(FIM_COMP, '\n' + comp + '\n\n' + FIM_COMP, 1)
        else:
            fim = fim_tab_complementary(s)
            s = s[:fim] + '\n' + comp + '\n\n' + s[fim:]
        feitos.append('complementares')

    # 5. audioMap: mescla pcN_/[order-lN] logo após "var audioMap = {"
    #    Depende do preclass.html (é dele que saem as frases). Num conserto que só
    #    repõe Complementares num hub antigo, esse arquivo não existe mais — e o
    #    audioMap do Pre-class daquela aula já está no hub desde a geração original.
    if os.path.exists(os.path.join(content_dir, 'preclass.html')) and not kids:
        s = merge_audiomap(s, cfg, content_dir)

    # 6. totalLessons -> MAIOR aula presente no hub (a barra só enche até totalLessons —
    #    REGRA 18). NUNCA baixar: em --replace de uma aula do meio (ex: 13 num hub que já
    #    vai até 20), usar n=13 quebraria a barra. Pega o max de todas as ex-lesson-K.
    if kids:
        # sem Pre-class não há exercício para o updateProgress contar. A barra do
        # pacote (aulas concluídas) continua vindo do lesson-progress.js.
        s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=0', s)
    else:
        all_n = [int(x) for x in re.findall(r'id="ex-lesson-(\d+)"', s)] + [n]
        s = re.sub(r'var totalLessons\s*=\s*\d+', f'var totalLessons={max(all_n)}', s)

    # A conferencia final exige TUDO que a anatomia daquele hub tem — nem mais, nem menos.
    # O data-media so entra na conta quando a anatomia TEM a aba: senao esta linha
    # reprovava o insert que ela mesma acabou de fazer corretamente.
    if kids:
        assert f'enterPostMode({n})' in s and f'id="pc-root-{n}"' in s, \
            f'percurso (post-class) ausente no hub (aula {n})'
        assert 'id="tab-exercises"' not in s, 'Pre-class ainda no hub kids'
    else:
        assert f'id="ex-lesson-{n}"' in s, f'accordion do Pre-class ausente no hub (aula {n})'
    assert f'id="stamp{n}"' in s, f'stamp ausente no hub (aula {n})'
    if B.tem_aba_complementares(cfg):
        assert f'data-media="l{n}-' in s, f'complementares ausentes no hub (aula {n})'
    assert is_aluno or not tem_standalone or f'{slug}-aula{n}.html' in s, \
        f'card do menu IN CLASS ausente no hub prof (aula {n})'
    # Diz o que ENTROU e o que já estava. Num hub meio inserido a diferença entre
    # "curou" e "não fez nada" é exatamente isto — e antes não aparecia em lugar nenhum.
    if feitos or pulados:
        print(f'  aula {n} em {os.path.basename(hub_path)}: '
              f'inserido={feitos or "-"} ja_existia={pulados or "-"}')
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
