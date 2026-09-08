#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O escopo das regras da anatomia de QUATRO MODALIDADES, escrito uma vez.

POR QUE ESTE ARQUIVO EXISTE
---------------------------
Seis gates (19, 22, 23, 25, 26, 27) nasceram em agosto/2026 a partir do mesmo pacote
normativo e do artefato da Erica, e todos os seis selecionavam o material assim:

    if not re.search(r'-aula\\d+\\.html$', base):          continue
    if framework_de(h) not in ANATOMIA_GD:                continue

Medido em 08/09/2026: **zero** arquivos publicados carregam
`<meta name="alumni-framework">` com uma das quatro modalidades. Os seis rodavam no CI,
imprimiam `0 aula(s)` e um `AVISO — SEM OBJETO`, e passavam verdes sobre um repo que nunca
mediram. A regra existia; o objeto dela, nao.

O objeto existe -- com outro nome. A anatomia que foi ao ar e a `consultivo`, seis
materiais, carimbada `<meta name="alumni-anatomia" content="consultivo">` e nomeada
`{slug}-ciclo1.html` / `{slug}-c1.html`, nao `{slug}-aulaN.html`. Sao AS MESMAS quatro
modalidades: Reading into Speaking, Listening into Interaction, Grammar for Communication e
Personalized Real-World English. O que mudou entre o artefato e o que se publicou foi o
carimbo e o nome do arquivo -- e os dois filtros liam exatamente essas duas coisas.

    "Gate que nomeia uma regiao e mede outra passa verde sobre o defeito."

Este modulo e a resposta: UM lugar que diz o que esta no escopo, para os cinco gates que
foram repontados. O sexto (GATE 22) foi APOSENTADO -- o `check_espinha.py` explica porque.

A FORMA ANTIGA CONTINUA ACEITA, e de proposito: e o que o `gates.json` declara em
`escopo.framework`, e o que os selftests dos cinco constroem. Se um material com o meta
`alumni-framework` aparecer, ele entra no escopo sem mais nenhuma mudanca.
"""
import re

# As quatro modalidades, pelos ids tecnicos. `esp-real-world` e id LEGADO, preservado por
# compatibilidade pelo Documento 06 -- o nome que a tela mostra e "Personalized Real-World
# English", e quem cobra isso e o GATE 64.
ANATOMIA_GD = ('reading-into-speaking', 'listening-into-interaction',
               'grammar-for-communication', 'esp-real-world')

RX_FRAMEWORK = re.compile(r'<meta name="alumni-framework" content="([a-z-]+)"')
RX_ANATOMIA = re.compile(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"')
RX_NOME_AULA = re.compile(r'-aula\d+\.html$')

ANATOMIA_PUBLICADA = "consultivo"


def framework_de(html):
    """A modalidade declarada no `<head>`, ou None. So a forma antiga a declara."""
    m = RX_FRAMEWORK.search(html)
    return m.group(1) if m else None


def anatomia_de(html):
    """A anatomia carimbada no `<head>`, ou None. So os primeiros 4 KB: o carimbo mora la,
    e o corpo de uma aula cita nomes de anatomia em prosa."""
    m = RX_ANATOMIA.search(html[:4000])
    return m.group(1) if m else None


def no_escopo(caminho, html):
    """O arquivo e material das quatro modalidades, em qualquer das duas formas?"""
    import os
    if anatomia_de(html) == ANATOMIA_PUBLICADA:
        return True
    return bool(RX_NOME_AULA.search(os.path.basename(caminho))) and \
        framework_de(html) in ANATOMIA_GD
