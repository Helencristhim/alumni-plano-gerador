#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""transcripts.py — o TRANSCRIPT do listening numa caixa que abre e fecha.

PARA QUE SERVE
--------------
Pedido de duas professoras, de dois alunos diferentes:

  Rafael Pelizaro  — *"Sinto que ele fica frustrado com os audios. (...) ele se sente
                     muito inseguro."*
  Joice Lopes Leite — *"a partir da aula 4, para as atividades de listening, podemos
                     acrescentar o script do audio. (...) Mas seria interessante colocar
                     de uma forma que ele nao ficasse exposto 100% do tempo. Talvez
                     colocar um botao ou algo assim que revele esse script e esconde."*

NAO QUEBRA O SOUND-FIRST (REGRAS 2.1 e 2.3). O que a regra protege e a DECODIFICACAO
PELO OUVIDO na escuta de exposicao — e a caixa **nasce fechada**. O transcript e a
CONFERENCIA depois: o aluno ve o que perdeu, que e exatamente a inseguranca relatada.
E toggle (REGRA 27-E): clicou sem querer, fecha no clique seguinte.

COMO SE LIGA (o "jeito facil" que o Dan pediu)
---------------------------------------------
  aula NOVA      -> "transcript": true no config.json da aula; o builder injeta sozinho
  aula JA GERADA -> python3 _build/model/apply_transcripts.py <slug> --aulas 4-20

Os dois caminhos chamam as MESMAS funcoes daqui. Quem nao liga a chave nao ve diferenca
nenhuma: sem a flag, nem o CSS entra. Feature opt-in por aluno — o Black Private admite
personalizacao exclusiva (memoria black-private-personalizacao-por-aluno).

UMA FONTE
---------
O texto sai de `lesson.listenings[].text` do config — o MESMO campo de que o MP3 nasceu.
E impossivel o transcript divergir do audio: se divergisse, o audio e que estaria errado
(e ai quem apita e o GATE 5c). O autor da aula nao escreve nem lembra de nada.
"""
import html as _html
import re
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import htmlpatch  # noqa: E402

CSS = """/* ===== Transcript accordion: o script do listening, escondido ate o clique ===== */
.ts-box { border:1px solid rgba(255,255,255,.18);border-radius:10px;overflow:hidden;background:rgba(255,255,255,.05);max-width:500px;margin:1rem auto 0;text-align:left; }
.ts-head { width:100%;display:flex;align-items:center;justify-content:space-between;gap:.6rem;padding:.7rem .9rem;background:transparent;border:none;color:#fff;font:600 .82rem/1.4 'Inter',-apple-system,sans-serif;cursor:pointer;letter-spacing:.4px; }
.ts-head:hover { background:rgba(255,255,255,.06); }
.ts-head:focus-visible { outline:3px solid var(--accent);outline-offset:-3px; }
.ts-chev { font-size:.7rem;color:rgba(255,255,255,.65);transition:transform .25s ease; }
.ts-box.open .ts-chev { transform:rotate(180deg); }
.ts-body { display:none;padding:0 .9rem .9rem;font-size:.86rem;line-height:1.75;color:rgba(255,255,255,.88); }
.ts-box.open .ts-body { display:block; }
@media (prefers-reduced-motion:reduce) { .ts-chev { transition:none; } }"""

JS = """// ===== Transcript accordion: abre/fecha o script do listening (REGRA 27-E: toggle) =====
function tsToggle(btn) {
  var box = btn.closest('.ts-box');
  if (!box) return;
  var open = box.classList.toggle('open');
  btn.setAttribute('aria-expanded', open ? 'true' : 'false');
}"""

# O que o professor precisa saber, e que NAO da para adivinhar olhando a tela.
TEACHER_NOTE = (' <strong>TRANSCRIPT:</strong> a caixa nasce FECHADA e assim fica nas duas '
                'escutas. Abra SO depois de corrigir as perguntas, para ele conferir o que '
                'perdeu &mdash; e ai vale reouvir lendo junto.')

# Instrucao que vira MENTIRA com a caixa na tela. Substituicao literal, nunca regex guloso.
_MENTIRAS = [
    ('Toque 2 vezes, sem transcricao.', 'Toque 2 vezes com a caixa Transcript FECHADA.'),
    ('Toque 2 vezes, sem transcrição.', 'Toque 2 vezes com a caixa Transcript FECHADA.'),
    ('sem transcricao,', 'com a caixa Transcript fechada,'),
    ('NAO mostre o texto.', 'Mantenha a caixa Transcript fechada nesta escuta.'),
    ('no text on screen.', 'transcript box closed for now.'),
]


def _div_end(s, start):
    """Indice logo apos o </div> que fecha o '<div' que comeca em `start`."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        if m.group(0) == '</div>':
            depth -= 1
            if depth == 0:
                return start + m.end()
        else:
            depth += 1
    return -1


def _box(pid, text):
    body = _html.escape(text, quote=False)
    return (f'\n    <div class="ts-box" id="ts-{pid}">'
            f'<button class="ts-head" type="button" aria-expanded="false" '
            f'aria-controls="ts-body-{pid}" onclick="tsToggle(this)">'
            f'<span>Transcript</span><span class="ts-chev">&#9660;</span></button>'
            f'<div class="ts-body" id="ts-body-{pid}"><p>{body}</p></div></div>')


def ensure_assets(s):
    """CSS e JS no arquivo. Idempotente. Quem nao usa a feature nunca recebe nada disto."""
    if '.ts-box {' not in s:
        s = s.replace('</style>', CSS + '\n</style>', 1)
    if 'function tsToggle' not in s:
        # NUNCA "antes do ultimo </script>": o arquivo pode terminar com <script src=...>,
        # e conteudo inline de script com src o navegador IGNORA (ver htmlpatch.py).
        s = htmlpatch.append_to_inline_script(s, JS)
    return s


def inject(s, listenings):
    """Injeta a caixa em cada player de listening de EXPOSICAO.

    QUEM E "PLAYER DE EXPOSICAO" — o criterio e o AUDIO QUE ELE TOCA, nunca o nome do id.
    O id nao e identidade: aula escrita a mao usa `mp-listen1`, aula emitida pelo builder
    usa `mp-a1` (expand_audio_players numera por ordem). Casar por id fazia a feature
    funcionar num caminho e falhar calada no outro. Vale o `data-src`: se o arquivo esta
    em `lesson.listenings`, aquele player toca o audio de que temos o script.

    O slide de PREDICAO fica de FORA de proposito: ali a tarefa e arriscar uma hipotese
    ouvindo (REGRA 2.3), e um transcript ao lado mataria a predicao — o olho vai no texto
    e ninguem arrisca nada. Ele se reconhece pelo `.ic-predict` no slide.

    Idempotente: a caixa ja existente e pulada pelo id derivado do player.
    """
    by_file = {l['file']: l.get('text', '') for l in (listenings or []) if l.get('file')}
    if not by_file:
        return s, 0
    n = 0
    while True:
        alvo = None
        for m in re.finditer(r'<div class="mock-player[^"]*"[^>]*>', s):
            tag = m.group(0)
            mid = re.search(r'id="([^"]+)"', tag)
            msrc = re.search(r'data-src="[^"]*?([^"/]+\.mp3)"', tag)
            if not mid or not msrc or msrc.group(1) not in by_file:
                continue
            pid = mid.group(1)
            if f'id="ts-{pid}"' in s:
                continue
            sl = s.rfind('<div class="slide ', 0, m.start())
            sl_end = s.find('<div class="slide ', m.start())
            if 'ic-predict' in s[sl:sl_end if sl_end > 0 else len(s)]:
                continue                      # slide de predicao: sem transcript (REGRA 2.3)
            alvo = (m, pid, by_file[msrc.group(1)])
            break
        if not alvo:
            break
        m, pid, text = alvo
        # onde entra: depois das perguntas de compreensao (para nao separar tarefa e audio);
        # se o slide nao as tiver, logo apos o player.
        pend_i = _div_end(s, m.start())
        q = re.search(r'<div class="comp-questions"', s[pend_i:pend_i + 4000])
        at = _div_end(s, pend_i + q.start()) if q else pend_i
        s = s[:at] + _box(pid, text) + s[at:]
        n += 1
    return s, n


def fix_teacher_notes(s):
    """Tira do data-teacher a instrucao que a caixa torna mentira, e diz o que fazer.

    Sem isto o professor le 'toque 2 vezes, sem transcricao' com um botao Transcript na
    tela dele. Instrucao que contradiz a tela e pior que instrucao nenhuma.
    """
    for velho, novo in _MENTIRAS:
        s = s.replace(velho, novo)

    def _add(m):
        att = m.group(0)
        if 'TRANSCRIPT:' in att or 'Listening' not in att:
            return att
        return att[:-1] + TEACHER_NOTE + '"'

    return re.sub(r'data-teacher="(?:[^"\\]|\\.)*"', _add, s)
