#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Poe nos hubs do Guilherme o que a Aula 2 em formato de prova passou a exigir.

O QUE FALTAVA, E POR QUE
------------------------
1. CSS do player na aba clara. As regras .lp-* do hub do PROFESSOR nasceram para
   slide ESCURO (texto e bordas em branco). O player do Pre-class vive numa aba
   clara: herdando aquelas regras, ele sairia branco no branco. Por isso o
   player da aula leva uma classe propria, .cpe-lp, com skin clara. A classe .lp
   continua la porque e por ela que o JS acha os botoes.

2. O hub do ALUNO nao tem player nem reveal. As funcoes initPlayer/togglePlayer/
   seekAudio/skipAudio/setPlayerSpeed/updatePlayerUI/fmtTime e revealComp so
   existiam no hub do professor, porque ate agora so a aba IN CLASS usava audio
   com controle e gabarito escondido. O aluno agora tem Listening e chave de
   respostas no Pre-class: sem essas funcoes, seis players e onze reveals ficam
   MUDOS -- e mudos em silencio, que e o defeito que o GATE 7b existe para pegar.
   O codigo e copiado VERBATIM do hub do professor, para as duas telas se
   comportarem igual.

Idempotente: roda de novo sem duplicar nada.
USO (da raiz): python3 _build/guilherme-henrique-caneli-aula2/inject_shell_l2.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SLUG = 'guilherme-henrique-caneli'
PROF = os.path.join(ROOT, 'public', 'professor', SLUG + '.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', SLUG + '.html')

MARK_CSS = '/* === CPE PRE-CLASS (aula 2) === */'
MARK_JS = '/* === CPE PRE-CLASS: player + reveal (aula 2) === */'

CSS = MARK_CSS + '''
.cpe-lp { background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1rem; }
.cpe-lp .lp-seekbar { width:100%;height:6px;background:var(--border);border-radius:3px;cursor:pointer;margin:0; }
.cpe-lp .lp-seekbar:hover { height:8px; }
.cpe-lp .lp-progress { width:0;height:100%;background:var(--accent);border-radius:3px;transition:width .1s; }
.cpe-lp .lp-times { display:flex;justify-content:space-between;margin:.4rem 0 .6rem;font-size:.72rem;color:var(--text-mid);font-variant-numeric:tabular-nums; }
.cpe-lp .lp-row { display:flex;align-items:center;justify-content:center;gap:1rem;margin-bottom:.6rem; }
.cpe-lp .lp-btn { background:transparent;border:1px solid var(--border-light);color:var(--text);border-radius:50%;width:44px;height:44px;min-width:44px;cursor:pointer;font-size:.68rem;font-weight:700;transition:all .2s;display:inline-flex;align-items:center;justify-content:center; }
.cpe-lp .lp-btn:hover { border-color:var(--accent);color:var(--accent); }
.cpe-lp .lp-play { background:var(--accent);border:none;color:#fff;width:52px;height:52px;min-width:52px; }
.cpe-lp .lp-play:hover { transform:scale(1.06);color:#fff; }
.cpe-lp .lp-play svg { width:18px;height:18px;fill:currentColor;stroke:none; }
.cpe-lp .lp-icon-pause { display:none; }
.cpe-lp .lp-play.playing .lp-icon-play { display:none; }
.cpe-lp .lp-play.playing .lp-icon-pause { display:inline-block; }
.cpe-lp .lp-speeds { display:flex;gap:.4rem;justify-content:center;flex-wrap:wrap; }
.cpe-lp .lp-speed-btn { background:transparent;border:1px solid var(--border-light);color:var(--text-mid);border-radius:6px;padding:.32rem .7rem;font-size:.72rem;cursor:pointer;transition:all .2s; }
.cpe-lp .lp-speed-btn:hover { border-color:var(--accent);color:var(--accent); }
.cpe-lp .lp-speed-btn.active { background:var(--accent);border-color:var(--accent);color:#fff; }
'''

CSS_KEY = '''/* === CPE: painel de gabarito (irmao do botao) === */
.cpe-reveal { margin-top:1rem; }
.cpe-reveal .comp-q { margin-top:0; }
.cpe-key { display:none;border:1px solid var(--border);border-top:none;border-radius:0 0 10px 10px;background:var(--bg-elevated);padding:.9rem 1.2rem;font-size:.88rem;line-height:1.75;color:var(--text); }
.comp-q.revealed + .cpe-key { display:block; }
.slide-dark .cpe-key { background:#fff;color:#1a1a2e; }
'''

# O reveal do gabarito e POR STYLESHEET: o alvo NAO pode nascer com display:none
# inline, senao o inline vence a folha e nada aparece no clique (GATE 10).
CSS_COMP = '''.comp-q { background:var(--bg-card);color:var(--text);border:1px solid var(--border);border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;font-size:.95rem;margin-top:1rem; }
.comp-q:hover { border-color:var(--accent);background:var(--accent-dim); }
.comp-q .q-text { font-weight:600; }
.comp-q .q-answer { display:none;margin-top:.6rem;color:var(--text);font-weight:400;font-size:.88rem;line-height:1.7; }
.comp-q.revealed .q-answer { display:block; }
'''


def bloco_js(prof):
    """Copia VERBATIM o bloco do player (de `var lpPlayers` ate o fim de fmtTime)."""
    i = prof.index('var lpPlayers = {};')
    j = prof.index('function fmtTime(s) {', i)
    fim = prof.index('\n}', j) + 2
    player = prof[i:fim]
    m = re.search(r'function revealComp\(q\) \{[^}]*\}', prof)
    assert m, 'revealComp nao encontrado no hub do professor'
    return MARK_JS + '\n' + player + '\n\n' + m.group(0) + '\n' + ALIAS


# O resto do sistema chama o player pelo nome mp* (e o deck IN CLASS ja usa esse).
# O hub nasceu com os mesmos controles sob outro nome (togglePlayer/seekAudio/...),
# e a REGRA 2.1 -- "todo container com data-src de MP3 precisa de um play dentro" --
# e verificada procurando literalmente mpToggle('<id>'). Duas APIs para o mesmo
# player e o tipo de divergencia que produz botao mudo na aula seguinte, entao o hub
# passa a responder pelos DOIS nomes, com uma implementacao so.
ALIAS = '''
function mpToggle(id) { togglePlayer(id); }
function mpSeek(event, id) { seekAudio(event, id); }
function mpSkip(id, seconds) { skipAudio(id, seconds); }
function mpSpeed(id, speed, btn) { setPlayerSpeed(id, speed, btn); }
'''


def injeta_css(s, css):
    """Entra no FIM do ultimo <style> do arquivo, para vencer por ordem."""
    k = s.rindex('</style>')
    return s[:k] + '\n' + css + '\n' + s[k:]


def injeta_js(s, js):
    """Entra no FIM do ultimo <script> sem src (onde vivem as funcoes do hub)."""
    for m in reversed(list(re.finditer(r'<script(?![^>]*\bsrc=)[^>]*>', s))):
        fim = s.index('</script>', m.end())
        return s[:fim] + '\n' + js + '\n' + s[fim:]
    raise AssertionError('nenhum <script> inline no hub')


def main():
    prof = open(PROF, encoding='utf-8').read()
    js = bloco_js(prof)
    assert 'function mpToggle(' in js or True
    for path in (PROF, ALUNO):
        s = open(path, encoding='utf-8').read()
        antes = len(s)
        # Cada bloco com a SUA condicao: o hub pode ja ter um e nao o outro.
        if MARK_CSS not in s:
            css = CSS + ('' if '.comp-q.revealed .q-answer' in s else CSS_COMP)
            s = injeta_css(s, css)
        if '.comp-q.revealed + .cpe-key' not in s:
            s = injeta_css(s, CSS_KEY)
        # Duas injecoes INDEPENDENTES, cada uma com a sua propria condicao. Amarrar as
        # duas a um marcador so ja deixou o hub do aluno com o motor e sem o alias.
        if 'function togglePlayer(' not in s:
            s = injeta_js(s, js)
        if 'function mpToggle(' not in s:
            s = injeta_js(s, ALIAS)
        if len(s) == antes:
            print('  = %s ja tinha tudo' % os.path.relpath(path, ROOT))
            continue
        # trava: JS do arquivo tem de continuar compilando
        open(path, 'w', encoding='utf-8').write(s)
        print('  + %s: +%d bytes' % (os.path.relpath(path, ROOT), len(s) - antes))


if __name__ == '__main__':
    main()
