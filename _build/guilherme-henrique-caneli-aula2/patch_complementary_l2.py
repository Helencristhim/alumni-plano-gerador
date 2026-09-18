#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sobe os Complementares da Aula 2 para o mesmo nivel das outras duas superficies.

O QUE MUDA, E O QUE NAO
-----------------------
Os TRES links ficam como estao. Eles sao reais, foram conferidos e estao no tema
(Mazzucato sobre valor publico e privado, Freakonomics sobre para onde vai o
capital, Dalio sobre como se decide antes de dizer sim). Trocar link bom por link
novo so cria risco de link morto, e a REGRA 17 existe justamente por isso.

O que muda e a TAREFA. Hoje o complementar pede "note three phrases" -- consumo
passivo, que e exatamente a critica do professor: para um C1+ isso nao e trabalho.
Cada card passa a carregar uma tarefa no formato da prova, sobre o mesmo video, e
o bloco final transforma a exposicao passiva em producao com criterio.

USO (da raiz): python3 _build/guilherme-henrique-caneli-aula2/patch_complementary_l2.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SLUG = 'guilherme-henrique-caneli'
HUBS = [os.path.join(ROOT, 'public', 'professor', SLUG + '.html'),
        os.path.join(ROOT, 'public', 'aluno', SLUG + '.html')]

TIPS = [
    'Exam task (Paper 3, Part 2): watch once with no subtitles and write your own eight sentence-completion '
    'notes. Then watch again with subtitles and count how many you paraphrased instead of writing the words '
    'she actually said. That count is your Part 2 score.',
    'Exam task (agency): open the transcript on the same page and find five passives with no agent. Restore '
    'the agent in each. Two of them will resist, and the reason they resist is the lesson.',
    'Exam task (Paper 1, Part 4): choose ninety seconds and transform three of his sentences, keeping the '
    'meaning and changing the structure. Three to eight words each, and read both versions aloud.',
]

BLOCO = '''<div class="media-extra-l2" style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:12px;padding:1.1rem 1.3rem;margin:.6rem 0 1.5rem">
  <div style="font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700;margin-bottom:.5rem">The register lab &middot; 20 minutes, any day this week</div>
  <p style="font-size:.9rem;line-height:1.7;margin:0 0 .7rem">Three short tasks on material you already read for work. No new sources, no screen time you were not going to spend anyway.</p>
  <ol style="font-size:.9rem;line-height:1.8;margin:0;padding-left:1.1rem">
    <li><b>Hunt the missing agent.</b> Take any term sheet, memo or press release that reaches you this week. Mark every action reported with no author. For each one, write the question you would ask on the call.</li>
    <li><b>The two-sentence test.</b> Take one fact from that document and write it twice: once naming the party who acted, once hiding them. Then decide which one you would send, and be able to say why.</li>
    <li><b>Read it as the fund reads it.</b> Give any article you read this week one pass for the argument and one pass for the queue: who is paid first, who waits, and what protects the person waiting. Two minutes each pass.</li>
  </ol>
</div>
'''


def main():
    for path in HUBS:
        s = open(path, encoding='utf-8').read()
        i = s.find('data-media="l2-talk"')
        assert i > 0, 'bloco de complementares da aula 2 nao encontrado em %s' % path
        ini = s.rfind('<h4', 0, i)
        fim = s.rfind('<h4', 0, s.find('data-media="l3-'))
        seg = s[ini:fim]
        novo = seg
        tips = re.findall(r'<p class="media-tip">.*?</p>', novo, re.S)
        assert len(tips) == 3, 'esperava 3 media-tip na aula 2, achei %d' % len(tips)
        for antigo, texto in zip(tips, TIPS):
            novo = novo.replace(antigo, '<p class="media-tip">%s</p>' % texto, 1)
        if 'media-extra-l2' not in novo:
            # entra logo depois do </div> que fecha a media-grid da aula 2
            k = novo.rindex('</div>\n</div>\n')
            novo = novo[:k + len('</div>\n</div>\n')] + BLOCO + novo[k + len('</div>\n</div>\n'):]
        if novo == seg:
            print('  = %s ja atualizado' % os.path.relpath(path, ROOT))
            continue
        out = s[:ini] + novo + s[fim:]
        assert (len(re.findall(r'<div\b', out)) - len(re.findall(r'</div\s*>', out))
                == len(re.findall(r'<div\b', s)) - len(re.findall(r'</div\s*>', s))), 'div desbalanceado'
        open(path, 'w', encoding='utf-8').write(out)
        print('  + %s: complementares da aula 2 atualizados (+%d bytes)' % (os.path.relpath(path, ROOT),
                                                                           len(out) - len(s)))
    # artefato do builder acompanha a pagina
    art = os.path.join(HERE, 'complementary.html')
    if os.path.exists(art):
        a = open(art, encoding='utf-8').read()
        tips = re.findall(r'<p class="media-tip">.*?</p>', a, re.S)
        for antigo, texto in zip(tips, TIPS):
            a = a.replace(antigo, '<p class="media-tip">%s</p>' % texto, 1)
        if 'media-extra-l2' not in a:
            a = a.rstrip() + '\n' + BLOCO
        open(art, 'w', encoding='utf-8').write(a)
        print('  + _build/.../complementary.html sincronizado')


if __name__ == '__main__':
    main()
