#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_from_model.py — builder GENÉRICO de aulas a partir da aluna modelo (Helen Mendes).

A REGRA 20 manda: layout vem SEMPRE do modelo; conteúdo vem do perfil 360 do aluno.
Este builder clona o shell do modelo (public/professor/helen-mendes-aula1.html, que
carrega TODOS os fixes globais: EXIT->exitSlideMode, handler de Escape fora do <script src>,
player completo de listening, revealError dinâmico, contrast-guard, nav-bar flex,
3a cor de diálogo guest) e injeta slug/paleta/conteúdo/audioMap do aluno.

USO (da raiz do repo):
  python3 _build/model/build_from_model.py _build/{slug}-aula{N}/config.json

ARQUIVOS DE CONTEÚDO (no mesmo diretório do config.json):
  slides.html            slides da aula (obrigatório)
  preclass.html          accordion Pre-class da aula (p/ hub novo ou snippet)
  planning.html          aba Planejamento (só hub "new")
  complementary.html     Complementares: aba inteira (hub "new") ou bloco da AULA (snippets — OBRIGATÓRIO)

CONFIG (JSON):
{
  "slug": "fulano-de-tal",
  "student_name": "Fulano de Tal",          // <h1> e títulos
  "first_name": "Fulano",                   // regra de voz em 1a pessoa
  "gender": "m",                            // m=arthur, f=ellen p/ falas do aluno
  "program": "Business English",
  "total_aulas": 10,
  "palette": { "accent": "#0D7377", "accent_light": "#14919B" },
  "header": ["A2", "S&#227;o Paulo, SP", "Gerente de TI", "60 min / Online"],
  "characters": { "fulano": "arthur", "sarah": "ellen" },  // classe CSS -> voz; 1o = ALUNO
  "stamps": [ {"id": 1, "label": "First Impressions", "img": "https://..."} ],
  "lesson": {
    "n": 1, "menu_num": "01",
    "menu_title": "...", "menu_desc": "... -- 27 slides",
    "subtitle": "Aula 1 -- ...",
    "title_tag": "Professor View -- Fulano | Aula 1 -- ...",
    "grammar_point": "past perfect",   // OPCIONAL: ponto gramatical canônico da aula.
                                       // Emite data-grammar no slide de Grammar Discovery
                                       // (REGRA 22, lido por check_grammar_progression.py).
                                       // Sem ele, nenhum marcador é emitido (config legado ok).
    "phases": ["...", "...", "...", "...", "...", "...", "..."],
    "listenings": [ {"file": "a1_listening1.mp3", "voice": "ellen", "text": "..."} ],
    "extra_audio": [ {"key": "[order-l1]", "file": "pc_order_l1.mp3", "voice": "arthur", "text": "..."} ]
  },
  "hub": "snippets"   // "new" = gera hub prof+aluno do zero | "snippets" = só trechos p/ hub existente | "none"
}

SAÍDAS:
  public/professor/{slug}-aula{N}.html      standalone professor
  public/aluno/{slug}-aula{N}.html          espelho aluno (REGRA 34)
  public/professor/{slug}.html + aluno      (só hub "new")
  _build/{slug}-aula{N}/audio_manifest.json (consumido por _build/model/gen_audio.py)
  _build/{slug}-aula{N}/hub_snippets.html   (só hub "snippets")

AULAS PASSADAS NÃO SÃO TOCADAS: o builder só escreve os arquivos da aula nova
(e o hub apenas no modo "new", de aluno que ainda não tem hub).
"""
import hashlib
import json
import os
import re
import sys
import unicodedata
# `from ... import` de propósito: vários parâmetros aqui se chamam `html` e
# importar o módulo inteiro o sombrearia.
from html import unescape as html_unescape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PROF = os.path.join(ROOT, 'public', 'professor')
ALUNO = os.path.join(ROOT, 'public', 'aluno')

VOICES = json.load(open(os.path.join(HERE, 'voices.json'), encoding='utf-8'))

MODEL = 'helen-mendes'
MODEL_ACCENT = ('#BE123C', '#be123c')
MODEL_ACCENT_LIGHT = ('#F43F5E', '#f43f5e')
MODEL_ACCENT_RGB = 'rgba(190,18,60'
MODEL_CHARS = ['helen', 'james']  # classes de diálogo do shell, em ordem (1o = aluno)


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'  wrote {os.path.relpath(p, ROOT)} ({len(s)//1024} KB)')


def replace_between(s, start, end, new_inner):
    i = s.index(start)
    j = s.index(end, i + len(start))
    return s[:i + len(start)] + new_inner + s[j:]


def snake(text, maxlen=48):
    t = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    t = re.sub(r"[^a-z0-9]+", '_', t.lower()).strip('_')
    return t[:maxlen].rstrip('_')


def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# ============================================================================
# B2 IN-CLASS BLOCKS (aditivo) — render estático dos blocos portados de
# artefato-b2-exercicios.html. O config declara os blocos por slide e o builder
# emite o HTML; um placeholder <!--IC-BLOCKS:chave--> no slides.html marca o ponto
# de injeção. Tipos antigos NÃO mudam: aula que não usa inclass_blocks fica idêntica.
#
# SCHEMA (config.lesson.inclass_blocks = { "chave": [ {bloco}, ... ], ... }):
#   {"kind":"gist","prompt":"...","choices":[["a","texto",false],["b","texto",true]]}   (interativo)
#   {"kind":"tf","items":[["statement","t|f","justification"], ...]}                       (interativo)
#   {"kind":"answer","title":"Reveal answer key","key":["1 = c", ...]}                     (interativo, accordion)
#   {"kind":"answer","title":"...","list":["resposta 1", ...],"note":"opcional"}
#   {"kind":"reading","rtitle":"...","paras":["...", ...],"source":"...","link":"..."}
#   {"kind":"matching","title":"...","words":[["1","word"], ...],"defs":[["a","def"], ...]}
#   {"kind":"gapfill","parts":["texto ",["1"]," mais texto"],"bank":["w1","w2"]}
#   {"kind":"modals","cards":[["should","Strong","..."],["could","Softer","..."]]}
#   {"kind":"rephrase","title":"...","items":[["cue sentence","modal"], ...]}
#   {"kind":"scenarios","items":[["Scenario 1","texto"], ...]}
#   {"kind":"quickfire","items":[{"situation":"...","tips":["...","..."]}, ...]}  (Prev/Next + Tips toggle)
#   {"kind":"questions","title":"...","ordered":true,"items":["q1", ...]}        (questions/guiding/analyse)
#   {"kind":"guiding","items":[...]}  {"kind":"analyse","title":"...","items":[...]}
#   {"kind":"lf","items":[["A","prefix ","should"," suffix","strong|soft"], ...]}
#   {"kind":"vocabnote","text":"..."}  {"kind":"followup","text":"..."}
#   {"kind":"bank","label":"...","items":["frase 1", ...]}
# ============================================================================
def _esc(t):
    return '' if t is None else str(t)


def render_block(b):
    """Emite o HTML estático de UM bloco B2. Espelha renderBlock() do artefato,
    com classes .ic-* (escopadas) e handlers que existem no shell do modelo."""
    k = b['kind']
    if k == 'vocabnote':
        return f'<div class="ic-note">{_esc(b["text"])}</div>'
    if k == 'followup':
        return f'<div class="ic-followup">{_esc(b["text"])}</div>'
    if k in ('questions', 'guiding', 'analyse'):
        tag = 'ol' if b.get('ordered') or k == 'analyse' else 'ul'
        extra = ' ic-guiding' if k == 'guiding' else ''
        bullet = '&#8250;' if k == 'guiding' else None
        lis = ''.join(
            f'<li><span class="ic-qnum">{bullet if bullet else i + 1}</span><span>{_esc(q)}</span></li>'
            for i, q in enumerate(b['items']))
        head = f'<div class="ic-card-h3"><span class="ic-tag">{_esc(b["title"])}</span></div>' if b.get('title') else ''
        return f'<div class="ic-card">{head}<{tag} class="ic-qs{extra}">{lis}</{tag}></div>'
    if k == 'matching':
        words = ''.join(f'<div class="ic-chip ic-word"><span class="ic-k">{_esc(w[0])}</span><span>{_esc(w[1])}</span></div>' for w in b['words'])
        defs = ''.join(f'<div class="ic-chip ic-def"><span class="ic-k">{_esc(d[0])}</span><span>{_esc(d[1])}</span></div>' for d in b['defs'])
        head = f'<div class="ic-card-h3">{_esc(b["title"])}</div>' if b.get('title') else ''
        return (f'<div class="ic-card">{head}<div class="ic-match">'
                f'<div class="ic-match-col"><h4>Words &amp; expressions</h4>{words}</div>'
                f'<div class="ic-match-col"><h4>Definitions</h4>{defs}</div></div></div>')
    if k == 'gapfill':
        html = ''
        for p in b['parts']:
            if isinstance(p, list):
                html += f'<span class="ic-blank"><span class="ic-n">{_esc(p[0])}</span>&nbsp;&nbsp;&nbsp;</span>'
            else:
                html += _esc(p)
        bank = ''.join(f'<span class="ic-b">{_esc(w)}</span>' for w in b['bank'])
        return f'<div class="ic-card"><div class="ic-gaptext">{html}</div><div class="ic-bank ic-soft">{bank}</div></div>'
    if k == 'reading':
        ps = ''.join(f'<p>{_esc(p)}</p>' for p in b['paras'])
        src = ''
        if b.get('source'):
            link = f' <a href="{_esc(b["link"])}" target="_blank" rel="noopener">{_esc(b["link"])}</a>' if b.get('link') else ''
            src = f'<div class="ic-src">{_esc(b["source"])}{link}</div>'
        rtitle = f'<div class="ic-rtitle">{_esc(b["rtitle"])}</div>' if b.get('rtitle') else ''
        return f'<div class="ic-reading">{rtitle}{ps}{src}</div>'
    if k == 'gist':
        ch = ''
        for c in b['choices']:
            right = 'true' if c[2] else 'false'
            ch += (f'<div class="ic-choice" data-right="{right}" onclick="icPickGist(this)">'
                   f'<span class="ic-opt">{_esc(c[0])}</span><span>{_esc(c[1])}</span>'
                   f'<span class="ic-badge">&#10003; Main idea</span></div>')
        return f'<div class="ic-card"><div class="ic-card-h3">{_esc(b["prompt"])}</div><div class="ic-choices">{ch}</div></div>'
    if k == 'tf':
        rows = ''
        for i, it in enumerate(b['items']):
            just = f'<span class="ic-just">&#8594; {_esc(it[2])}</span>' if len(it) > 2 and it[2] else ''
            ans = str(it[1]).strip().lower()
            assert ans in ('t', 'f', 'true', 'false'), f'tf item[1] deve ser t/f (lido da afirmação): {it!r}'
            answer = 'true' if ans in ('t', 'true') else 'false'
            rows += (f'<div class="ic-tfrow" data-answer="{answer}" onclick="icRevealTf(this)">'
                     f'<span class="ic-qnum">{i + 1}</span>'
                     f'<span class="ic-stmt">{_esc(it[0])}{just}</span>'
                     f'<span class="ic-verdict ic-t">TRUE</span><span class="ic-verdict ic-f">FALSE</span></div>')
        return f'<div class="ic-card"><div class="ic-tf">{rows}</div></div>'
    if k == 'lf':
        rows = ''
        for it in b['items']:
            strong = ' ic-strong' if (len(it) > 4 and it[4] == 'strong') else ''
            rows += (f'<div class="ic-lf"><span class="ic-lbl">{_esc(it[0])}</span>'
                     f'<span>{_esc(it[1])}<span class="ic-mod{strong}">{_esc(it[2])}</span>{_esc(it[3])}</span></div>')
        head = f'<div class="ic-card-h3"><span class="ic-tag">Analyse</span>{_esc(b.get("title", "Read the advice"))}</div>'
        return f'<div class="ic-card">{head}<div class="ic-lf-list">{rows}</div></div>'
    if k == 'modals':
        cards = ''.join(f'<div class="ic-modal-c"><div class="ic-m">{_esc(c[0])}</div>'
                        f'<div class="ic-strength">{_esc(c[1])}</div><p>{_esc(c[2])}</p></div>' for c in b['cards'])
        head = f'<div class="ic-card-h3">{_esc(b.get("title", "Meaning guide"))}</div>'
        return f'<div class="ic-card">{head}<div class="ic-modals">{cards}</div></div>'
    if k == 'rephrase':
        rows = ''
        for i, it in enumerate(b['items']):
            rows += (f'<li><span class="ic-qnum">{i + 1}</span>'
                     f'<span>{_esc(it[0])}<span class="ic-rephrase-cue">({_esc(it[1])})</span>'
                     f'<span class="ic-blank" style="min-width:7rem;margin-left:.4rem">&nbsp;</span></span></li>')
        head = f'<div class="ic-card-h3">{_esc(b["title"])}</div>' if b.get('title') else ''
        return f'<div class="ic-card">{head}<ol class="ic-qs">{rows}</ol></div>'
    if k == 'scenarios':
        items = ''.join(f'<div class="ic-scenario"><div class="ic-who">{_esc(it[0])}</div><p>{_esc(it[1])}</p></div>' for it in b['items'])
        return f'<div class="ic-block">{items}</div>'
    if k == 'quickfire':
        # Quick Fire BIDIRECIONAL + Tips. Situacoes ABERTAS (REGRA 27.D): cada item
        # tem "situation" (cenario realista) e "tips" (frases de apoio/estrutura,
        # NAO um gabarito). Navega Previous/Next (qfNav, shell) com contador; Tips
        # faz toggle (qfTips, REGRA 27.E). Vai num placeholder <!--IC-BLOCKS:quickfire-->.
        items = b['items']
        assert items, 'quickfire sem items'
        btn_st = ('background:var(--accent);color:#fff;border:none;border-radius:8px;'
                  'padding:.5rem 1.2rem;font-size:.85rem;font-weight:600;cursor:pointer')
        nav_prev = ('background:transparent;color:var(--accent);border:2px solid var(--accent);'
                    'border-radius:8px;padding:.5rem 1.2rem;font-size:.85rem;font-weight:600;cursor:pointer')
        cards = ''
        for i, it in enumerate(items):
            disp = '' if i == 0 else 'display:none;'
            tips = ''.join(f'<li style="margin-bottom:.3rem">{_esc(t)}</li>' for t in it['tips'])
            cards += (
                f'<div class="qf-card" data-qf="{i + 1}" style="{disp}background:var(--bg-card);'
                f'border:1px solid var(--border);border-radius:12px;padding:1.2rem;margin-bottom:.8rem">'
                f'<p class="qf-situation" style="font-size:.92rem;font-weight:600;margin-bottom:.6rem">{_esc(it["situation"])}</p>'
                f'<button class="primary-btn qf-tips-btn" onclick="qfTips(this)" style="{btn_st}">Tips</button>'
                f'<div class="qf-tips" style="display:none;margin-top:.6rem">'
                f'<ul style="font-size:.84rem;color:var(--text-mid);padding-left:1.1rem;margin:0">{tips}</ul></div></div>')
        score = (f'<p style="text-align:center;font-size:.82rem;color:var(--text-dim);margin-top:.3rem">'
                 f'<span id="qfScore">1 / {len(items)}</span></p>')
        nav = ('<div class="qf-nav" style="display:flex;gap:.6rem;justify-content:center;margin-top:1rem">'
               f'<button class="qf-prev" onclick="qfNav(-1)" style="{nav_prev}">&#8592; Previous</button>'
               f'<button class="primary-btn qf-next" onclick="qfNav(1)" style="{btn_st}">Next &#8594;</button></div>')
        return f'{score}<div id="qfContainer" style="max-width:560px;margin:1rem auto 0">{cards}{nav}</div>'
    if k == 'bank':
        items = ''.join(f'<span class="ic-b">{_esc(w)}</span>' for w in b['items'])
        head = f'<div class="ic-card-h3">{_esc(b.get("label", "Useful language"))}</div>'
        return f'<div class="ic-card">{head}<div class="ic-bank">{items}</div></div>'
    if k == 'answer':
        title = _esc(b.get('title', 'Reveal answer key'))
        if b.get('key'):
            chips = ''.join(f'<span class="ic-a">{_esc(a)}</span>' for a in b['key'])
            inner = f'<div class="ic-akey">{chips}</div>'
        elif b.get('list'):
            note = f'<div style="font-size:.78rem;color:var(--text-dim);margin-bottom:.6rem">{_esc(b["note"])}</div>' if b.get('note') else ''
            ol = ''.join(f'<li>{_esc(a)}</li>' for a in b['list'])
            inner = f'{note}<ol>{ol}</ol>'
        else:
            inner = ''
        return (f'<div class="ic-answer"><div class="ic-ans-head" onclick="icToggleAnswer(this)">'
                f'<span class="ic-ico">+</span>{title}</div>'
                f'<div class="ic-ans-body"><div class="ic-ans-inner">{inner}</div></div></div>')
    raise AssertionError(f'inclass_blocks: kind desconhecido "{k}"')


def expand_inclass_blocks(slides, cfg):
    """Substitui placeholders <!--IC-BLOCKS:chave--> em slides.html pelo HTML dos
    blocos declarados em config.lesson.inclass_blocks[chave]. Sem placeholders =
    no-op (aula antiga fica byte-a-byte idêntica)."""
    blocks_cfg = cfg.get('lesson', {}).get('inclass_blocks', {})
    used = set()

    def sub(m):
        key = m.group(1).strip()
        assert key in blocks_cfg, f'placeholder IC-BLOCKS:{key} sem entrada em lesson.inclass_blocks'
        used.add(key)
        return '\n'.join(render_block(b) for b in blocks_cfg[key])

    out = re.sub(r'<!--\s*IC-BLOCKS:([^>]+?)\s*-->', sub, slides)
    unused = set(blocks_cfg) - used
    assert not unused, f'inclass_blocks declarados mas sem placeholder no slides.html: {sorted(unused)}'
    return out


# ============================================================================
# A TAREFA VEM ANTES DA EXPOSIÇÃO (CLAUDE.md REGRA 2.2)
# ============================================================================
def _texto(s):
    """texto puro de um fragmento HTML (sem tags, espaços normalizados)."""
    return ' '.join(re.sub(r'<[^>]+>', ' ', s).split())


def _estrutura(ch):
    """O slide SEM o data-teacher.

    Detecção de estrutura NUNCA pode olhar o data-teacher: ele é PROSA para o professor e
    pode conter qualquer palavra — inclusive o nome das classes que estamos procurando.
    Foi exatamente o que aconteceu: o data-teacher do slide de True/False da aula 3 cita
    "ic-reading", a busca por substring achou que aquele slide era uma LEITURA, abortou o
    lookahead e o slide de tarefa da leitura não nasceu no arquivo do PROFESSOR — mas
    nasceu no do ALUNO, onde o data-teacher é removido. Prof e aluno divergiram.
    Estrutura se lê na CLASSE, não no texto do professor.
    """
    return re.sub(r'\sdata-teacher="(?:[^"\\]|\\.)*"', '', ch)


def _exposicao(ch):
    """'dialogue' | 'reading' | None — pela CLASSE, no slide sem data-teacher."""
    est = _estrutura(ch)
    if 'class="dialogue-line' in est:
        return 'dialogue'
    if 'class="ic-reading"' in est:
        return 'reading'
    return None


def _perguntas_da_checagem(ch):
    """(kind, [perguntas]) do slide de CHECAGEM — a fonte ÚNICA das perguntas.

    dialogue -> .q-text do slide de Comprehension
    reading  -> .ic-stmt do True/False, SEM a justificativa (.ic-just), que é gabarito.
    """
    ch = _estrutura(ch)
    if 'ic-tfrow' in ch:
        out = []
        for st in re.findall(r'<span class="ic-stmt">(.*?)</span>\s*<span class="ic-verdict', ch, re.S):
            out.append(_texto(re.sub(r'<span class="ic-just">.*?</span>', '', st, flags=re.S)))
        return 'tf', [q for q in out if q]
    if 'class="comp-q"' in ch and 'mock-player' not in ch:
        return 'comp', [_texto(q) for q in re.findall(r'<div class="q-text">(.*?)</div>', ch, re.S)]
    return None, []


def _slide_de_tarefa(kind, perguntas, phase):
    """O slide de TAREFA. Só a pergunta — o gabarito NÃO existe no HTML (nem escondido:
    o professor compartilha a tela, e 'display:none' ainda está no DOM, a um Ctrl+U
    de distância). Sem onclick: não há o que revelar aqui."""
    if kind == 'reading':
        label, head, acc = 'Before you read', 'Read', 'for this'
        t = ('<strong>Antes do texto (1 min):</strong> LEIA ESTAS PERGUNTAS EM VOZ ALTA COM A ALUNA '
             'ANTES de mostrar o texto. É isto que ela vai procurar enquanto lê — sem a tarefa antes, '
             'compreensão vira teste de MEMÓRIA. NÃO revele as respostas aqui: elas saem no slide '
             'de checagem, depois.')
    else:
        label, head, acc = 'Before you listen', 'Listen', 'for this'
        t = ('<strong>Antes do diálogo (1 min):</strong> LEIA ESTAS PERGUNTAS EM VOZ ALTA COM A ALUNA '
             'ANTES de abrir o diálogo. É isto que ela vai procurar enquanto ouve — sem a tarefa antes, '
             'compreensão vira teste de MEMÓRIA. NÃO revele as respostas aqui: elas saem no slide '
             'de checagem, depois.')
    qs = '\n      '.join(
        f'<div class="comp-q comp-q-task"><div class="q-text">{q}</div></div>' for q in perguntas)
    return (f'<div class="slide slide-light" data-slide="0" data-phase="{phase}" '
            f'data-task-for="{kind}" data-teacher="{t}">\n'
            f'  <div class="slide-inner">\n'
            f'    <div class="chapter-label">{label}</div>\n'
            f'    <h2 class="slide-heading">{head} <span class="accent">{acc}</span></h2>\n'
            f'    <div style="display:flex;flex-direction:column;gap:1rem;max-width:520px;margin:1.2rem auto 0">\n'
            f'      {qs}\n'
            f'    </div>\n'
            f'  </div>\n'
            f'</div>\n\n')


def inject_task_slides(slides):
    """Emite o slide de TAREFA antes de todo diálogo / leitura. IDEMPOTENTE.

    O PRINCÍPIO: o aluno tem de saber O QUE PROCURAR antes de ser exposto ao conteúdo.
    Sem a tarefa antes, compreensão vira teste de MEMÓRIA — que é outra habilidade.

        [TAREFA: as perguntas, sem resposta]  ->  [o diálogo / o texto]  ->  [checagem: as
        MESMAS perguntas, com click-to-reveal]

    UMA FONTE, DOIS SLIDES: as perguntas do slide de tarefa são EXTRAÍDAS do slide de
    checagem que já existe. É impossível os dois divergirem — e o autor do conteúdo não
    precisa lembrar de nada. Foi exatamente por depender da memória do autor que o
    DEFEITO 2 (perguntas escondidas) se replicou em 224 arquivos: a regra dizia uma
    coisa, o LLM obedeceu, e ninguém viu.

    NÃO toca no slide de ARTEFATO (email/boarding pass): lá as perguntas já dividem a
    tela com o objeto, e o aluno pode olhar enquanto responde. Não é o mesmo defeito.
    """
    partes = re.split(r'(?=<div class="slide )', slides)
    out, i = [], 0
    while i < len(partes):
        ch = partes[i]
        kind = _exposicao(ch)
        # já tem slide de tarefa antes? (idempotência)
        ja_tem = bool(out and 'data-task-for=' in out[-1])
        if kind and not ja_tem:
            perguntas, phase = [], (re.search(r'data-phase="(\d+)"', ch) or [None, '1'])[1]
            for j in range(i + 1, min(i + 6, len(partes))):
                nxt = partes[j]
                if _exposicao(nxt):
                    break  # outra exposição antes da checagem: para
                _, qs = _perguntas_da_checagem(nxt)
                if qs:
                    perguntas = qs
                    break
            if perguntas:
                out.append(_slide_de_tarefa(kind, perguntas, phase))
        out.append(ch)
        i += 1
    novo = ''.join(out)
    # RENUMERA data-slide em ordem de documento (a inserção desloca todo mundo).
    cont = [0]

    def _n(m):
        cont[0] += 1
        return f'data-slide="{cont[0]}"'

    return re.sub(r'data-slide="\d+"', _n, novo)


def extract_phrases(html):
    """(texto, voz_sugerida|None) em ordem de documento; data-voice na mesma linha vence.

    O TEXTO SAI DAQUI JÁ DESESCAPADO — e isso é a espinha de todo o áudio.

    Este é o ponto de entrada que envenenava a cadeia inteira. Ele lia a frase COMO
    ESTÁ ESCRITA NO HTML — ou seja, com as entidades: "Rachel&#39;s task". Mas em
    runtime o navegador desescapa o atributo e entrega ao speakText o texto de
    verdade: "Rachel's task". As duas chaves NUNCA casavam. Consequência em cascata:

      audioMap    chave "Rachel&#39;s task"  -> lookup falha em runtime -> TTS robótico
      manifest    text  "Rachel&#39;s task"  -> a ElevenLabs FALA a entidade
      arquivo     snake("Rachel&#39;s task") -> nome de MP3 lixo

    Foi por isso que 127 frases nunca ganharam áudio e 36 apontavam para MP3
    inexistente. A chave tem de ser o que o speakText RECEBE, não o que está
    ESCRITO no arquivo. (Ver scripts/check_inline_js.mjs e PR #1261.)
    """
    out = []
    for line in html.split('\n'):
        mv = re.search(r'data-voice="([a-z]+)"', line)
        hint = mv.group(1) if mv else None
        # forma ANTIGA: o texto dentro da string JS. Frágil — apóstrofo do inglês
        # quebra o handler (o browser desescapa antes de compilar). Ainda lida para
        # não cegar o áudio das aulas legadas.
        for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", line):
            t = html_unescape(m.group(1).replace("\\'", "'"))
            if not t.startswith('['):
                out.append((t, hint))
        # forma NOVA (correta): o texto vive num ATRIBUTO, onde apóstrofo e aspa são
        # caracteres comuns e não há string JS para fechar.
        for m in re.finditer(r'data-speak="([^"]*)"', line):
            t = html_unescape(m.group(1))
            if not t.startswith('['):
                out.append((t, hint))
        for m in re.finditer(r'data-phrase="([^"]*)"', line):
            out.append((html_unescape(m.group(1)), hint))
    return out


def audio_filename(text, prefix, taken):
    """Nome do MP3 a partir da frase — GARANTIDAMENTE UNICO.

    snake() trunca em 48 chars e NAO e injetivo: duas frases distintas que
    compartilham o mesmo prefixo de 48 chars caem no MESMO arquivo. Quando isso
    acontece, o audioMap fica com DUAS chaves apontando pro MESMO MP3 e uma delas
    toca o audio da OUTRA frase — o aluno clica em "It was the approvals cycle
    that broke the quarter, not the market." e ouve "...that broke the quarter."
    Bug silencioso: nenhum gate pega, porque o arquivo EXISTE.
    (felipe-pimenta, 13/07/2026: 3 colisoes nas aulas 7, 8 e 9.)

    Frase sem colisao mantem o nome IDENTICO ao de antes (hash so entra no
    desempate), entao material ja gerado nao muda de nome.
    """
    base = snake(text)
    name = f'{prefix}{base}.mp3'
    if taken.get(name, text) == text:
        taken[name] = text
        return name
    # colisao real: 2 frases distintas, mesmo prefixo de 48 chars
    h = hashlib.sha1(text.encode('utf-8')).hexdigest()[:6]
    name = f'{prefix}{base}_{h}.mp3'
    assert taken.get(name, text) == text, f'colisao de nome de audio irredutivel: {text!r}'
    taken[name] = text
    return name


def assign_voices(phrases, prefix, cfg):
    """REGRA 7: 1-2 palavras = arthur; frases alternam; data-voice (diálogo) vence;
    falas em 1a pessoa do aluno = voz do gênero do aluno."""
    student_voice = 'ellen' if cfg['gender'] == 'f' else 'arthur'
    first = re.escape(cfg['first_name'])
    first_person = re.compile(rf"\bI am {first}\b|\bI'm {first}\b|\bMy name is {first}\b")
    entries = {}
    taken = {}
    alt = 0
    for text, hint in phrases:
        if text in entries:
            # data-voice (diálogo) vence mesmo se a frase já apareceu antes
            # sem hint (ex.: a mesma pergunta no slide de gramática e na fala
            # de um personagem): o personagem define a voz do MP3 único.
            if hint and entries[text]['voice'] != hint:
                entries[text]['voice'] = hint
            continue
        if hint:
            voice = hint
        elif len(text.split()) <= 2:
            voice = 'arthur'
        elif first_person.search(text):
            voice = student_voice
        else:
            voice = 'ellen' if alt % 2 == 0 else 'arthur'
            alt += 1
        assert voice in VOICES, f'voz desconhecida "{voice}" (disponíveis: {sorted(VOICES)})'
        entries[text] = dict(voice=voice, file=audio_filename(text, prefix, taken))
    return entries


def audio_map_js(entries, audio_base, extra=None):
    lines = ['var audioMap = {']
    for text, meta in entries.items():
        lines.append(f'  {json.dumps(text, ensure_ascii=False)}: {json.dumps(audio_base + meta["file"])},')
    for item in (extra or []):
        lines.append(f'  {json.dumps(item["key"], ensure_ascii=False)}: {json.dumps(audio_base + item["file"])},')
    lines.append('};')
    return '\n'.join(lines)


def base_swaps(s, cfg, n=None):
    """Paleta + slug + nome + personagens + programa. SEMPRE antes de injetar conteúdo."""
    accent = cfg['palette']['accent']
    light = cfg['palette']['accent_light']
    r, g, b = hex_to_rgb(accent)
    for tok in MODEL_ACCENT:
        s = s.replace(tok, accent)
    for tok in MODEL_ACCENT_LIGHT:
        s = s.replace(tok, light)
    s = s.replace(MODEL_ACCENT_RGB, f'rgba({r},{g},{b}')
    # personagens do diálogo: classes do shell -> classes do aluno
    chars = list(cfg['characters'])
    for old, new in zip(MODEL_CHARS, chars):
        s = s.replace(f'.dialogue-avatar.{old}', f'.dialogue-avatar.{new}')
        s = s.replace(f'.dialogue-bubble.{old}-bubble', f'.dialogue-bubble.{new}-bubble')
    if n:
        s = s.replace(f'{MODEL}-aula1', f'{cfg["slug"]}-aula{n}')
        s = s.replace(f'{MODEL}-aula2', f'{cfg["slug"]}-aula{n}')
    s = s.replace(MODEL, cfg['slug'])
    s = s.replace('Helen Mendes', cfg['student_name'])
    s = s.replace('Helen', cfg['first_name'])
    s = re.sub(r'window\.TOTAL_AULAS=\d+', f'window.TOTAL_AULAS={cfg["total_aulas"]}', s)
    s = re.sub(r'Business English (--|—) 30 Aulas', f'{cfg["program"]} \\1 {cfg["total_aulas"]} Aulas', s)
    return s


def apply_ui_strings(s, cfg):
    """OPT-IN i18n: troca micro-strings de UI do shell (cravadas em inglês/PT no JS e nas
    tabs compartilhadas) por traduções vindas do config. Só roda se cfg tiver 'ui_strings' —
    alunos de inglês não passam essa chave, então o caminho deles fica IDÊNTICO. Substituição
    exata de substring; aplicar SEMPRE por último (depois dos swaps aluno-específicos)."""
    for en, tr in cfg.get('ui_strings', {}).items():
        s = s.replace(en, tr)
    return s


def stamps_html(cfg):
    rows = ['<div class="stamps-row">']
    for st in cfg['stamps']:
        rows.append(f'<div class="stamp" id="stamp{st["id"]}" data-label="{st["label"]}" '
                    f'style="background-image:url(\'{st["img"]}\')"></div>')
    rows.append('</div>\n')
    return '\n'.join(rows)


def patch_header(s, cfg, subtitle):
    s = re.sub(r'<p class="subtitle">[^<]*</p>', f'<p class="subtitle">{subtitle}</p>', s, count=1)
    info = '\n'.join(f'      <span>{x}</span>' for x in cfg['header'])
    s = re.sub(r'<div class="student-info">.*?</div>',
               '<div class="student-info">\n' + info + '\n    </div>', s, count=1, flags=re.S)
    i = s.index('<div class="stamps-row">')
    m = re.search(r'\n</div>\n', s[i:])
    s = s[:i] + stamps_html(cfg) + s[i + m.end() - 1:]
    return s


def menu_card(cfg, target):
    """Card padrão do menu IN CLASS. target = 'enterSlideMode' (standalone) ou href (hub)."""
    L = cfg['lesson']
    if target == 'enterSlideMode':
        opener = 'onclick="enterSlideMode();"'
        tag, endtag, href = 'div', 'div', ''
    else:
        opener = ''
        tag, endtag, href = 'a', 'a', f' href="{target}" '
    return (
        f'    <{tag}{href} style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" {opener} onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
        f'      <div style="width:48px;height:48px;flex-shrink:0;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">{L["menu_num"]}</div>\n'
        f'      <div><div style="font-weight:600;font-size:.95rem">{L["menu_title"]}</div><div style="font-size:.8rem;color:var(--text-dim)">{L["menu_desc"]}</div></div>\n'
        f'    </{endtag}>')


def inclass_menu(cards):
    # Título do menu IN CLASS: vai pra TELA DO ALUNO (o espelho /aluno/ também tem a aba).
    # Estava em português ("Selecione a Aula") — viola a REGRA 13 em A2+. Aluno A0/A1
    # traduz via ui_strings no config. (apply_ui_strings roda no write, por último.)
    return ('\n  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS -- Select your Lesson</h3>\n'
            '  <div style="display:flex;flex-direction:column;gap:1rem">\n' + '\n'.join(cards) + '\n  </div>\n</div>\n\n')


def final_asserts(s, cfg, label, is_hub=False):
    low = s.lower()
    # A própria aluna MODELO (helen-mendes) é o único slug em que "helen" e a paleta
    # do modelo são LEGÍTIMOS no output — são o nome/paleta do aluno, não vazamento.
    # As aulas-referência do modelo (helen-mendes-aula4/5) nascem do mesmo builder;
    # exatamente por isso ficaram de fora antes. Os dois asserts anti-vazamento só
    # fazem sentido para OUTROS alunos, então pulamos quando o slug é o do modelo.
    is_model = cfg['slug'] == MODEL
    if not is_model:
        assert 'helen' not in low, f'{label}: sobrou referência ao modelo (helen)'
    assert '/lib/contrast-guard.js' in s, f'{label}: contrast-guard NÃO plugado'
    # "Plugado" tem de significar QUE RODA, não que a string aparece. Este assert já
    # passava com a tag <script src="/lib/contrast-guard.js"> carregando 7.812 bytes de
    # JS morto dentro dela: a string estava lá, o contrast-guard carregava, e o corpo
    # inline era descartado pelo navegador (spec do HTML: src => conteúdo ignorado).
    # Verde falso. O builder clona o shell do modelo, então isso se replicou sozinho.
    for m in re.finditer(r'<script\b[^>]*\bsrc\s*=[^>]*>(.*?)</script\s*>', s, re.S | re.I):
        assert len(m.group(1).strip()) <= 50, (
            f'{label}: <script src> com {len(m.group(1).strip()):,} bytes de JS inline — o '
            f'navegador IGNORA esse corpo. Feche a tag do src e ponha o JS num <script> próprio.')
    assert "class=\"check-item\" onclick=\"this.classList.toggle('checked')\"" not in s, \
        f'{label}: checklist com onclick inline não persiste (use toggleCheck(this) — REGRA 28)'
    if 'class="check-item"' in s:
        for g in re.findall(r'<div class="check-grid"[^>]*>', s):
            assert 'data-lesson=' in g, \
                f'{label}: check-grid sem data-lesson — lesson-progress.js não detecta a aula, ' \
                f'inclass_done nunca salva (barra do pacote/stamps travados — REGRA 28)'
    assert 'toggleListening' not in s, f'{label}: listening fake presente'
    # A FORMA carrega o bilíngue; o NÍVEL decide se ele é usado.
    # helen-mendes é A2, então o conteúdo dela não tem .sp-pt/.speech-translation — mas o
    # CSS deles DEVE continuar no shell, senão nenhum aluno A0/A1 pode mais existir
    # (o material sairia com a tradução SEM ESTILO). A ausência de PT no modelo é
    # consequência do NÍVEL dele, não uma propriedade da FORMA. REGRA 13.
    if is_hub:
        for cls in ('.sp-pt', '.speech-translation'):
            assert re.search(re.escape(cls) + r'\s*\{', s), (
                f'{label}: o CSS de {cls} sumiu do shell — isso MATA o bilíngue de A0/A1 '
                f'(a traducao sai sem estilo). O modelo e A2 e nao USA a classe, mas a FORMA '
                f'tem de continuar suportando o nivel que USA. NAO remover.')
    if not is_hub:
        assert 'function mpToggle' in s or 'slidesContainer' not in s, f'{label}: player de listening ausente'
    if not is_model:
        assert MODEL_ACCENT[0] not in s and MODEL_ACCENT[0].lower() not in low.replace(cfg['palette']['accent'].lower(), ''), \
            f'{label}: paleta do modelo vazou'


def _attr_escape(v):
    """Escapa uma string para caber com segurança dentro de um atributo HTML (aspas duplas)."""
    return (str(v).replace('&', '&amp;').replace('"', '&quot;')
            .replace('<', '&lt;').replace('>', '&gt;'))


def _opening_tag_end(s, start):
    """Índice do '>' que FECHA a tag aberta em `start`, respeitando aspas.
    O data-teacher dos slides contém HTML ('<strong>...</strong>'), então um
    s.find('>') ingênuo pararia DENTRO do valor do atributo. Aqui pulamos as
    strings entre aspas para achar o '>' real da tag."""
    i, q = start, None
    while i < len(s):
        c = s[i]
        if q:
            if c == q:
                q = None
        elif c in '"\'':
            q = c
        elif c == '>':
            return i
        i += 1
    return -1


def inject_grammar_marker(slides, grammar_point):
    """REGRA 22 (gramática não repete) — o IRMÃO gramatical do vocab-card-word.

    Marca o slide de Grammar Discovery com data-grammar="<ponto canônico>". É esse
    marcador — uniforme, um-por-aula, emitido pelo BUILDER — que o
    check_grammar_progression.py lê para saber qual gramática a aula ENSINA como nova.
    Espelha o que o vocab-card-word faz para o vocabulário: um-conceito-por-elemento,
    posto pelo builder, impossível de divergir.

    Tolerante por construção: sem `lesson.grammar_point` no config (config legado, ou
    aula de leitura/review sem slide de Grammar Discovery), NÃO injeta nada. A aula
    passa incólume e o gate simplesmente a ignora (nunca compara aula sem marcador —
    é assim que o legado nunca dispara falso-positivo). Idempotente: não duplica."""
    if not grammar_point:
        return slides
    g = ' '.join(str(grammar_point).split()).strip()
    if not g:
        return slides
    marker = 'chapter-label">Grammar Discovery'
    idx = slides.find(marker)
    if idx == -1:
        return slides  # aula sem slide de Grammar Discovery — no-op silencioso
    start = slides.rfind('<div class="slide', 0, idx)
    if start == -1:
        return slides
    tag_end = _opening_tag_end(slides, start)
    if tag_end == -1:
        return slides
    if 'data-grammar=' in slides[start:tag_end]:
        return slides  # idempotente
    return slides[:tag_end] + f' data-grammar="{_attr_escape(g)}"' + slides[tag_end:]


def build_standalone(cfg, content_dir, manifest):
    L = cfg['lesson']
    n = L['n']
    audio_base = f'/audio/{cfg["slug"]}/'
    slides = read(os.path.join(content_dir, 'slides.html'))
    slides = expand_inclass_blocks(slides, cfg)  # B2 blocks (no-op se a aula não usar)
    # A TAREFA VEM ANTES DA EXPOSIÇÃO (REGRA 2.2): emite o slide de perguntas antes de
    # todo diálogo/leitura, a partir das perguntas do slide de checagem. Idempotente e
    # renumera os data-slide. Aula sem diálogo nem leitura = no-op.
    slides = inject_task_slides(slides)
    # REGRA 28: o checklist "What I Learned" DEVE chamar toggleCheck(this) — é ele que o
    # lesson-progress.js faz wrap para salvar inclass_done (barra do pacote + stamps).
    # onclick="this.classList.toggle('checked')" só alterna a classe visual: os tics somem
    # ao recarregar e o progresso do pacote nunca avança. Normaliza aqui, na fonte.
    slides = slides.replace(
        'class="check-item" onclick="this.classList.toggle(\'checked\')"',
        'class="check-item" onclick="toggleCheck(this)"')
    # O check-grid do "What I Learned" DEVE ter data-lesson=N — é assim que o
    # lesson-progress.js detecta a aula e grava inclass_done (barra do pacote + stamps).
    # Template antigo usava id="checklist-N" (inconsistente entre alunos) SEM data-lesson,
    # e nesses casos o save nunca disparava. Normaliza na fonte (N = número da aula).
    slides = re.sub(r'<div class="check-grid"(?![^>]*\bdata-lesson=)',
                    f'<div class="check-grid" data-lesson="{n}"', slides)
    # REGRA 22 (gramática não repete): marca o slide de Grammar Discovery com
    # data-grammar=<ponto canônico>, o irmão gramatical do vocab-card-word. É esse
    # marcador que o check_grammar_progression.py lê. Campo OPCIONAL (lesson.grammar_point):
    # sem ele — config legado ou aula sem Grammar Discovery — não injeta nada e a aula passa
    # incólume (o gate ignora aula sem marcador, então o legado nunca dispara).
    gp = L.get('grammar_point')
    if gp:
        slides = inject_grammar_marker(slides, gp)
    elif 'chapter-label">Grammar Discovery' in slides:
        # Nudge não-bloqueante: a aula ENSINA gramática mas o config não declarou o ponto,
        # então o gate da REGRA 22 fica cego para ela. Não é erro (campo opcional p/ não
        # quebrar config legado), mas o autor deveria preencher lesson.grammar_point.
        print(f'  aviso: aula {n} tem slide de Grammar Discovery mas sem "grammar_point" no '
              f'config — data-grammar NÃO emitido (gate de gramática não cobre esta aula).',
              file=sys.stderr)
    # Common Mistake: riscar a FRASE INTEIRA (<s>"..."</s>) fica ilegível/feio. O erro já
    # vem marcado com <strong>; move o <s> para envolver SÓ o <strong>, deixando o resto
    # da frase legível ("I <s><strong>check always</strong></s> the schedule first.").
    slides = re.sub(r'<s>"([^"<]*)<strong>([^<]*)</strong>([^"<]*)"</s>',
                    r'"\1<s><strong>\2</strong></s>\3"', slides)
    # Common Mistake: padding:1rem deixa as frases apertadas em cima/embaixo. Mais respiro.
    slides = slides.replace(
        'class="mistake-item" style="display:flex;align-items:flex-start;gap:.8rem;padding:1rem;',
        'class="mistake-item" style="display:flex;align-items:flex-start;gap:.8rem;padding:1.4rem 1.2rem;')
    # Common Mistake: margem UNIFORME nos 4 lados. O card ganha padding+gap+stretch; os blocos
    # coloridos preenchem (max-width:none) e o divisor (border-bottom) sai — antes topo/base
    # encostavam na borda enquanto as laterais tinham margem (max-width:500px centralizado).
    slides = re.sub(r'(class="mistake-card" style="[^"]*?border-radius:12px);overflow:hidden"',
                    r'\1;padding:1.1rem;display:flex;flex-direction:column;gap:1.1rem;align-items:stretch"', slides)
    slides = slides.replace(
        'gap:.8rem;padding:1.4rem 1.2rem;border-bottom:1px solid var(--border);background:var(--danger-bg)"',
        'gap:.8rem;padding:1.4rem 1.2rem;background:var(--danger-bg);max-width:none"')
    slides = slides.replace(
        'gap:.8rem;padding:1.4rem 1.2rem;background:var(--success-bg)"',
        'gap:.8rem;padding:1.4rem 1.2rem;background:var(--success-bg);max-width:none"')

    s = read(os.path.join(PROF, f'{MODEL}-aula1.html'))
    s = base_swaps(s, cfg, n=n)
    s = re.sub(r'<title>[^<]*</title>', f'<title>{L["title_tag"]}</title>', s, count=1)
    s = re.sub(r'<h1>[^<]*</h1>', f'<h1>{cfg["student_name"]}</h1>', s, count=1)
    s = patch_header(s, cfg, L['subtitle'])

    labels = '\n' + '\n'.join(
        f'  <span class="phase-label{" current" if i == 0 else ""}" data-phase="{i+1}">{name}</span>'
        for i, name in enumerate(L['phases'])) + '\n'
    s = replace_between(s, '<div class="phase-labels" id="phaseLabels">', '</div>', labels)

    s = replace_between(s, '<div class="tab-content active" id="tab-inclass">', '<!-- ========== TAB 4',
                        inclass_menu([menu_card(cfg, 'enterSlideMode')]))
    s = replace_between(s, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->',
                        '\n' + slides + '\n')
    s = s.replace('>LESSON 1<', f'>LESSON {n}<')
    # Update totalSlides to match actual slide count
    actual_slides = len(re.findall(r'data-slide=', slides))
    s = re.sub(r'var totalSlides = \d+', f'var totalSlides = {actual_slides}', s)

    entries = assign_voices(extract_phrases(slides), prefix=f'a{n}_', cfg=cfg)
    extra = L.get('extra_audio', [])
    s = re.sub(r'var audioMap = \{.*?\};', lambda _: audio_map_js(entries, audio_base, extra), s, count=1, flags=re.S)

    for text, meta in entries.items():
        manifest.append(dict(text=text, voice=meta['voice'], file=meta['file']))
    for li in L.get('listenings', []):
        assert li['voice'] in VOICES, f'listening com voz desconhecida: {li["voice"]}'
        manifest.append(dict(text=li['text'], voice=li['voice'], file=li['file']))
    for item in extra:
        assert item['voice'] in VOICES, f'extra_audio com voz desconhecida: {item["voice"]}'
        manifest.append(dict(text=item['text'], voice=item['voice'], file=item['file']))

    final_asserts(s, cfg, f'prof aula{n}')
    write(os.path.join(PROF, f'{cfg["slug"]}-aula{n}.html'), apply_ui_strings(s, cfg))

    # espelho ALUNO (REGRA 34): sem instruções de professor, exit volta ao hub do aluno
    # (deriva de `s` em INGLÊS — apply_ui_strings só no write, depois dos swaps do aluno)
    a = s.replace('<title>Professor View --', '<title>Aluno --')
    a = a.replace('<span class="prof-badge">Professor View</span>', '<span class="prof-badge">Aluno</span>')
    a = a.replace('>PROFESSOR VIEW<', '>ALUNO<')
    a = re.sub(r'\sdata-teacher="(?:[^"\\]|\\.)*"', '', a)
    a = a.replace('</style>', '.teacher-t{display:none !important}\n</style>')
    a = a.replace(f"window.location.href = '/professor/{cfg['slug']}.html#inclass'",
                  f"window.location.href = '/aluno/{cfg['slug']}.html#inclass'")
    a = a.replace(f'{cfg["slug"]}-aula{n}-professor', f'{cfg["slug"]}-aula{n}-aluno')
    final_asserts(a, cfg, f'aluno aula{n}')
    write(os.path.join(ALUNO, f'{cfg["slug"]}-aula{n}.html'), apply_ui_strings(a, cfg))
    return entries


def _match_div_end(s, start):
    """Dado o índice de um '<div' em s, retorna o índice logo após o </div> que o fecha."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        if m.group(0) == '</div>':
            depth -= 1
            if depth == 0:
                return start + m.end()
        else:
            depth += 1
    return -1


def _wrap_card_run(body):
    """Envolve o bloco contíguo de .media-card-wrapper de `body` num <div class="media-grid">
    (layout 2+1 da maria-claudia). Preserva o que vem antes/depois dos cards."""
    if 'media-card-wrapper' not in body:
        return body
    first = body.find('<div class="media-card-wrapper"')
    i, end = first, first
    while i >= 0:
        e = _match_div_end(body, i)
        if e < 0:
            break
        end = e
        i = body.find('<div class="media-card-wrapper"', e)
    inner = body[first:end].strip('\n')
    return body[:first] + '<div class="media-grid">\n' + inner + '\n</div>\n' + body[end:]


def _lesson_h4(cfg):
    """Cabeçalho canônico da aula nos Complementares: <h4>Lesson N &mdash; Título</h4>
    (Lección para aulas de espanhol). Título vem do config (lesson.menu_title)."""
    L = cfg['lesson']
    label = 'Clase' if cfg.get('lang') == 'es' else 'Lesson'
    title = (L.get('menu_title') or L.get('subtitle') or '').strip()
    title = re.sub(r'&(?!#?\w+;)', '&amp;', title)  # escapa & solto
    return (f'<h4 style="font-size:.95rem;margin:1.5rem 0 .8rem">'
            f'{label} {L["n"]} &mdash; {title}</h4>')


def normalize_complementary(html, cfg=None):
    """Normaliza Complementares ao estilo canônico (REGRA 17: classes CSS) e GARANTE o
    layout media-grid (2 cards em cima + 1 embaixo) com 1 <h4> de cabeçalho por aula,
    igual à maria-claudia. Autores às vezes escrevem com style inline / cards soltos /
    <h4> divergente; aqui convertemos para classes e agrupamos. Idempotente: se já houver
    media-grid, não duplica."""
    # separadores <hr> do estilo inline
    html = re.sub(r'[ \t]*<hr style="border:none;border-top:1px solid var\(--border\)[^>]*>\n?', '', html)
    # sub-header <h4 font-size:.95rem> da aula: removido e re-emitido do config (título canônico,
    # "Lesson/Lección N — ..."), NÃO deixado de fora como antes (bug: aula saía sem h4)
    html = re.sub(r'[ \t]*<h4 style="font-size:\.95rem[^>]*>.*?</h4>\n?', '', html, flags=re.S)
    # style inline no media-thumb (CSS .media-thumb assume tamanho/cor)
    html = re.sub(r'<div class="media-thumb" style="[^"]*">', '<div class="media-thumb">', html)
    # style inline no <p> de descrição
    html = re.sub(r'<p style="font-size:\.82rem;color:var\(--text-mid\)">', '<p>', html)
    # style inline no media-tip
    html = re.sub(r'<p class="media-tip" style="[^"]*">', '<p class="media-tip">', html)
    # GARANTE 1 h4 de cabeçalho da aula (do config) antes dos cards/grid — mesmo quando o
    # autor JÁ mandou os cards dentro de um <div class="media-grid"> (antes o h4 sumia nesse
    # caso: a condição exigia ausência de media-grid). Insere antes do grid, ou do 1º card.
    if cfg is not None and 'media-card-wrapper' in html:
        anchor = html.find('<div class="media-grid"')
        if anchor < 0:
            anchor = html.find('<div class="media-card-wrapper"')
        if anchor >= 0:
            html = html[:anchor] + _lesson_h4(cfg) + '\n' + html[anchor:]
    # ENVOLVE os cards de cada aula (sob seu h4) num <div class="media-grid"> — idempotente
    if 'media-card-wrapper' in html and 'class="media-grid"' not in html:
        parts = re.split(r'(<h4\b[^>]*>.*?</h4>)', html, flags=re.S)
        out = [parts[0]]
        i = 1
        while i < len(parts):
            out.append(parts[i])                                   # o <h4>
            out.append(_wrap_card_run(parts[i + 1] if i + 1 < len(parts) else ''))
            i += 2
        html = ''.join(out)
    return html


def build_hub_new(cfg, content_dir, manifest):
    """Hub completo (aluno NOVO, sem hub existente). Clona os hubs do modelo."""
    L = cfg['lesson']
    audio_base = f'/audio/{cfg["slug"]}/'
    preclass = read(os.path.join(content_dir, 'preclass.html'))
    planning = read(os.path.join(content_dir, 'planning.html'))
    complementary = normalize_complementary(read(os.path.join(content_dir, 'complementary.html')), cfg)

    entries = assign_voices(extract_phrases(preclass), prefix='pc_', cfg=cfg)
    extra = L.get('extra_audio', [])
    amap = audio_map_js(entries, audio_base, extra)
    for text, meta in entries.items():
        manifest.append(dict(text=text, voice=meta['voice'], file=meta['file']))

    card = menu_card(cfg, f'/professor/{cfg["slug"]}-aula{L["n"]}.html?autostart=1')

    s = read(os.path.join(PROF, f'{MODEL}.html'))
    s = base_swaps(s, cfg)
    s = re.sub(r'<title>[^<]*</title>',
               f'<title>Professor View -- {cfg["student_name"]} | {cfg["program"]}</title>', s, count=1)
    s = re.sub(r'<h1>[^<]*</h1>', f'<h1>{cfg["student_name"]}</h1>', s, count=1)
    s = patch_header(s, cfg, cfg.get('hub_subtitle', cfg['program']))
    s = replace_between(s, '<div class="tab-content active" id="tab-planning">', '</div><!-- /tab-planning -->', '\n' + planning + '\n')
    s = replace_between(s, '<div class="tab-content" id="tab-exercises">', '</div><!-- /tab-exercises -->', '\n' + preclass + '\n')
    s = replace_between(s, '<div class="tab-content" id="tab-inclass">', '<!-- ========== TAB 4', inclass_menu([card]))
    s = replace_between(s, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', '\n' + complementary + '\n')
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=1', s)
    s = re.sub(r'var audioMap = \{.*?\};', lambda _: amap, s, count=1, flags=re.S)
    final_asserts(s, cfg, 'hub prof', is_hub=True)
    write(os.path.join(PROF, f'{cfg["slug"]}.html'), apply_ui_strings(s, cfg))

    a = read(os.path.join(ALUNO, f'{MODEL}.html'))
    a = base_swaps(a, cfg)
    a = re.sub(r'<title>[^<]*</title>', f'<title>{cfg["student_name"]} | {cfg["program"]} -- Alumni</title>', a, count=1)
    a = re.sub(r'<h1>[^<]*</h1>', f'<h1>{cfg["student_name"]}</h1>', a, count=1)
    a = patch_header(a, cfg, cfg.get('hub_subtitle', cfg['program']))
    a = replace_between(a, '<div class="tab-content active" id="tab-exercises">', '</div><!-- /tab-exercises -->', '\n' + preclass + '\n')
    a = replace_between(a, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', '\n' + complementary + '\n')
    a = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=1', a)
    a = re.sub(r'var audioMap = \{.*?\};', lambda _: amap, a, count=1, flags=re.S)
    final_asserts(a, cfg, 'hub aluno', is_hub=True)
    write(os.path.join(ALUNO, f'{cfg["slug"]}.html'), apply_ui_strings(a, cfg))


def build_hub_snippets(cfg, content_dir, out_dir, slide_entries):
    """Aluno EXISTENTE: NÃO toca o hub dele. Gera trechos prontos pra inserir
    (card IN CLASS, stamp, accordion Pre-class, entradas de audioMap)."""
    L = cfg['lesson']
    audio_base = f'/audio/{cfg["slug"]}/'
    parts = ['<!-- ============ SNIPPETS pro hub de ' + cfg['slug'] + ' (aula ' + str(L['n']) + ') ============ -->\n']
    parts.append('<!-- 1. CARD do menu IN CLASS (inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->\n')
    parts.append(menu_card(cfg, f'/professor/{cfg["slug"]}-aula{L["n"]}.html?autostart=1') + '\n\n')
    st = next((x for x in cfg['stamps'] if x['id'] == L['n']), None)
    if st:
        parts.append('<!-- 2. STAMP (inserir na stamps-row do header) -->\n')
        parts.append(f'<div class="stamp" id="stamp{st["id"]}" data-label="{st["label"]}" style="background-image:url(\'{st["img"]}\')"></div>\n\n')
    pc_path = os.path.join(content_dir, 'preclass.html')
    pc_entries = {}
    if os.path.exists(pc_path):
        pc = read(pc_path)
        pc_entries = assign_voices(extract_phrases(pc), prefix=f'pc{L["n"]}_', cfg=cfg)
        parts.append('<!-- 3. ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->\n')
        parts.append(pc + '\n\n')
    # COMPLEMENTARES da aula: obrigatório (classe de bug do PR #106 — aula sem
    # complementares no hub). data-media deve usar prefixo l{N}- (validador cobra).
    comp_path = os.path.join(content_dir, 'complementary.html')
    assert os.path.exists(comp_path), (
        f'complementary.html FALTANDO em {os.path.relpath(content_dir, ROOT)} — '
        f'toda aula precisa do bloco de Complementares (data-media="l{L["n"]}-...")')
    comp = normalize_complementary(read(comp_path), cfg)
    assert f'data-media="l{L["n"]}-' in comp, (
        f'complementary.html sem data-media="l{L["n"]}-..." — use o prefixo da aula')
    parts.append(f'<!-- 3b. COMPLEMENTARES da aula {L["n"]} (inserir na tab-complementary, prof E aluno) -->\n')
    parts.append(comp + '\n\n')
    parts.append('<!-- 4. ENTRADAS de audioMap (mesclar no audioMap do hub, prof E aluno) -->\n<script>\n')
    for text, meta in {**slide_entries, **pc_entries}.items():
        parts.append(f'  {json.dumps(text, ensure_ascii=False)}: {json.dumps(audio_base + meta["file"])},\n')
    parts.append('</script>\n')
    parts.append('<!-- 5. Ajustar: var totalLessons / window.TOTAL_AULAS no hub, se mudou -->\n')
    write(os.path.join(out_dir, 'hub_snippets.html'), ''.join(parts))
    return pc_entries


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    cfg_path = os.path.abspath(sys.argv[1])
    content_dir = os.path.dirname(cfg_path)
    cfg = json.load(open(cfg_path, encoding='utf-8'))
    assert len(cfg['characters']) <= 3, 'máx 3 personagens por diálogo (e só há 2 vozes — ver voices.json)'
    for v in cfg['characters'].values():
        assert v in VOICES, f'voz desconhecida no characters: {v}'

    manifest = []
    print('== standalone ==')
    entries = build_standalone(cfg, content_dir, manifest)

    hub_mode = cfg.get('hub', 'snippets')
    if hub_mode == 'new':
        print('== hub (novo) ==')
        build_hub_new(cfg, content_dir, manifest)
    elif hub_mode == 'snippets':
        print('== hub (snippets p/ hub existente — hub NÃO é tocado) ==')
        pc_entries = build_hub_snippets(cfg, content_dir, content_dir, entries)
        for text, meta in pc_entries.items():
            manifest.append(dict(text=text, voice=meta['voice'], file=meta['file']))

    seen, dedup = set(), []
    for e in manifest:
        if e['file'] in seen:
            continue
        seen.add(e['file'])
        dedup.append(e)
    write(os.path.join(content_dir, 'audio_manifest.json'), json.dumps(dedup, ensure_ascii=False, indent=1))
    print(f'manifest: {len(dedup)} áudios -> rode: ELEVENLABS_API_KEY=... python3 _build/model/gen_audio.py {os.path.relpath(cfg_path, ROOT)}')
    print(f'valide:   python3 _build/model/validate_lesson.py public/professor/{cfg["slug"]}-aula{cfg["lesson"]["n"]}.html public/aluno/{cfg["slug"]}-aula{cfg["lesson"]["n"]}.html')


if __name__ == '__main__':
    main()
