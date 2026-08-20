# -*- coding: utf-8 -*-
"""Extrai o SHELL do molde (artefato Private Black) a partir do arquivo de referencia.

O que sai do arquivo: TODO o conteudo da Erica (header, 6 abas, deck) e os dados de
conteudo no JS. O que fica: o CSS, o motor e os hosts vazios -- e no lugar de cada regiao
de conteudo, um marcador que o build.py preenche com o conteudo do aluno.

O arquivo de referencia e um SNAPSHOT do DOM (pagina salva), nao o fonte: ele ja traz o
que os construtores injetaram no boot (.ak, transporte de audio, barra de etapas, mapa do
ciclo). Isso e inofensivo aqui porque tudo o que foi injetado vive DENTRO das regioes de
conteudo que este script remove; os hosts genericos sao reescritos no boot.
"""
import re, sys

SRC = "molde-black-private.reference.html"
OUT = "shell.html"

_linhas = open(SRC, encoding="utf-8").read().split("\n")
# As quatro primeiras linhas do arquivo salvo sao o runtime do visualizador de artefato
# (nao e do material) e o <title> da Erica. O documento comeca no <style>.
_cabeca = ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n'
           '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
           '<title>Alumni by Better</title>\n'
           '<style>:root{color-scheme:light}body{margin:0;padding:0;'
           'font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#faf9f5;color:#141413}'
           'img{max-width:100%}</style>\n</head>\n<body data-view="professor">\n')
s = _cabeca + "\n".join(_linhas[4:])

# Defeito do molde: o registro passou a chamar-se 'aluno' (P19) e dois pontos do pre-class
# continuaram lendo ld().aluna -> undefined. O boot inteiro morria na primeira linha do
# preInit, e nada depois dele rodava.
for _a, _b in [("var v=ld().aluna['pre_mec_'+bloco.id]", "var v=ld().aluno['pre_mec_'+bloco.id]"),
               ("var d=ld().aluna,pane=document.getElementById('tab-preclass')",
                "var d=ld().aluno,pane=document.getElementById('tab-preclass')")]:
    assert _a in s, "o defeito do ld().aluna mudou de forma: " + _a
    s = s.replace(_a, _b)

def corta(ini, fim, slot, incl_fim=False):
    """Troca o trecho [ini, fim) por <!--SLOT:x-->. fim e o texto que ABRE a proxima regiao."""
    global s
    i = s.index(ini)
    j = s.index(fim, i + len(ini))
    if incl_fim:
        j += len(fim)
    s = s[:i] + "<!--SLOT:%s-->\n" % slot + s[j:]

# --- header (nome, programa, passaporte do ciclo) ---
corta('<header class="header">', '</header>\n', 'HEADER', incl_fim=True)

# --- as seis abas, em ordem; cada uma vai ate a abertura da seguinte ---
corta('<div class="tab-content" id="tab-planning">',
      '<div class="tab-content" data-view="professor" id="tab-syllabus">', 'PLANNING')
corta('<div class="tab-content" data-view="professor" id="tab-syllabus">',
      '<div class="tab-content" id="tab-preclass"', 'SYLLABUS')
corta('<div class="tab-content" id="tab-preclass"',
      '<div class="tab-content active" data-view="professor" id="tab-inclass">', 'PRECLASS')
corta('<div class="tab-content active" data-view="professor" id="tab-inclass">',
      '<div class="tab-content" data-view="aluno" id="tab-feedback">', 'INCLASS')
corta('<div class="tab-content" data-view="aluno" id="tab-feedback">',
      '<div class="tab-content" id="tab-postclass">', 'FEEDBACK')
corta('<div class="tab-content" id="tab-postclass">',
      '</div><!-- /container -->', 'POSTCLASS')

# --- o deck: tudo dentro do slidesContainer ---
corta('<div class="slides-container" id="slidesContainer">\n',
      '</div><!-- /slides-container -->', 'DECKS')
s = s.replace("<!--SLOT:DECKS-->\n", '<div class="slides-container" id="slidesContainer">\n<!--SLOT:DECKS-->\n')

# --- barra de etapas e menu lateral: hosts vazios (o deckInit reescreve os dois) ---
s = re.sub(r'<div class="stage-bar" id="stageBar">.*?</div>\n', '<div class="stage-bar" id="stageBar"></div>\n', s, count=1, flags=re.S)
s = re.sub(r'<div class="stage-labels" id="stageLabels">.*?</div>\n', '<div class="stage-labels" id="stageLabels"></div>\n', s, count=1, flags=re.S)
s = re.sub(r'<div class="sm-list" id="smList">.*?</nav>', '<div class="sm-list" id="smList"></div>\n</nav>', s, count=1, flags=re.S)

# --- dados de conteudo no JS: um bloco so, no lugar do primeiro ---
corpo_js = s.index('<script>', s.index('<!--SLOT:DECKS-->'))
def corta_js(ini, fim, slot=None):
    global s
    i = s.index(ini, corpo_js)
    j = s.index(fim, i + len(ini))
    s = s[:i] + (("<!--SLOT:%s-->" % slot) if slot else "") + s[j:]

s = s.replace("var STORE='erica_pv_v1';", "/*SLOT:DADOS*/")
CORTES = [
    ("var CALL_L1=[",      "\nfunction playCall("),
    ('var SCRIPT_PRE2="',  "\ndocument.addEventListener('DOMContentLoaded',function(){"),
    ("var GD_COLS=",       "\nvar _gd=[]"),
    ("var GD_V=[",         "\nfunction gdvBuild("),
    ("var CP=[",           "\nfunction cpBuild("),
    ("var RECAP=[",        "\nfunction closeBuild("),
    ("var PC_NOTAS={",     "\nfunction pcSecs("),
    ("var LESSONS={",      "\nvar NUM_EXT="),
    ("var CICLO={",        "\n/* Registro da aluna"),
    ("var ARTEFATO={",     "\nfunction artefatoId("),
    ("var ALUNO={",        "\nfunction alunoNome("),
]
for ini, fim in CORTES:
    try:
        corta_js(ini, fim)
    except ValueError:
        raise SystemExit("ancora nao encontrada: %r ... %r" % (ini, fim))

# --- o numero de aulas para de ser 4 cravado no codigo ---
i = s.index('<script>', s.index('<!--SLOT:DECKS-->'))
cab, motor = s[:i], s[i:]
motor, n = re.subn(r'([nia]|_a)\s*<=\s*4\s*;', lambda m: m.group(0).replace('4', 'NAULAS'), motor)
s = cab + motor
print("loops de aula destravados:", n)

# --- o titulo do documento sai do registro do aluno ---
s = s.replace("' \\u2014 Business English Program | Alumni by Better'", "' \\u2014 '+CICLO.programa+' | Alumni by Better'")

for slot in ['HEADER','PLANNING','SYLLABUS','PRECLASS','INCLASS','FEEDBACK','POSTCLASS','DECKS']:
    assert ("<!--SLOT:%s-->" % slot) in s, "faltou o slot " + slot
assert "/*SLOT:DADOS*/" in s, "faltou o slot DADOS"
sobrou = [l for l in s.split(chr(10)) if 'Erica' in l and not (l.startswith((' ','\t','*','/*','//')) or l.strip().startswith(('*','/*','//')))]
assert not sobrou, "sobrou conteudo da Erica no shell: %r" % sobrou[:3]
open(OUT, "w", encoding="utf-8").write(s)
print("shell:", len(s), "bytes,", s.count("\n"), "linhas")
