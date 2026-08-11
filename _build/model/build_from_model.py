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
    "stages": [ {"n": "The brief", "min": 5}, ... ],   // AS ETAPAS DA AULA (a espinha).
                                       // 7 ou 8, cada uma agrupando 1-6 telas; o data-phase
                                       // de cada tela diz a qual pertence. O rotulo e AUTORAL
                                       // da aula (o normativo fixa a funcao, nao o nome) e os
                                       // minutos somam o percurso_min do contrato (55).
                                       // Emite phase-bar + phase-labels; o shell pinta
                                       // completed/current/upcoming.
    "phases": ["...", "..."],          // FORMA ANTIGA de "stages", so nomes, sem minutos.
                                       // Continua valendo (anatomia imersivo: a barra la e de
                                       // CAPITULOS da narrativa e nunca teve orcamento).
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
# Voz de sotaque e decisao POR ALUNO: entra em cfg['voices'] da aula, nunca no
# voices.json global (que vale pro roster inteiro). O gen_audio.py e o
# validate_lesson.py resolvem pelo MESMO caminho — se o builder nao resolvesse,
# ele abortaria em material correto antes mesmo de o gate rodar. Preenchido em
# main(), assim que o config e lido. Ver README, secao 'Vozes'.

MODEL = 'helen-mendes'


# ANATOMIA: a forma da AULA — quantas abas, se o slide rola, quantas telas por etapa.
# Nao confundir com `model` (a PELE: fonte, cor, tom) nem com `framework` (a arquitetura
# pedagogica: quais etapas, em que ordem).
#
# O nome da anatomia e o da FORMA, nunca o de uma pessoa. Ordem do Dan (07/08/2026):
#
#     "o helen mendes nao e soberano ao stephanie, ele e so um tipo de framework"
#
# Enquanto existia uma anatomia so, o shell era a aula publicada de alguem — e por isso
# todo molde novo precisava clonar a aula da Helen para existir. Isso e a soberania que
# esta ordem desfaz: `imersivo` e `guided-discovery` sao pares, nenhuma e padrao.
def tem_aba_complementares(cfg):
    """A aba existe nesta anatomia? Pergunta a ANATOMIA DECLARADA, nunca ao HTML do hub.

    Ler o SINTOMA ('id="tab-complementary"' ausente) ja custou caro: 9 hubs LEGADOS
    tambem nao tem a aba, e ali a ausencia e DEFEITO, nao desenho. Um guard por sintoma
    silenciou os 33 defeitos deles de uma vez (o GATE 8 pegou: -17 -> -50). Anatomia nao
    declarada => comportamento do legado (a aba existe), que e o default seguro.
    """
    anat = ANATOMIA_POR_SLUG.get(cfg.get('slug'), 'imersivo')
    abas = ANATOMIAS_DECLARADAS.get(anat, {}).get('abas')
    return 'complementary' in abas if abas else True


def sem_aba_complementares(s):
    """A anatomia guided-discovery nao tem a aba. Chamar replace_between nela estouraria
    com ValueError; devolver o HTML intacto e o comportamento certo."""
    return 'id="tab-complementary"' not in s


ANATOMIAS = {
    # DIVIDA DECLARADA: a anatomia `imersivo` ainda aponta para uma AULA PUBLICADA, que
    # acumula ser aula e template. Extrair para shells/imersivo.html criaria uma COPIA, e
    # copia deriva; a extracao de verdade exige a aula 1 da Helen passar a ser GERADA, o
    # que mexe em material no ar. Fica assim, com o nome da divida escrito, ate haver ordem
    # explicita para o refactor.
    'imersivo': ('public/professor', 'helen-mendes-aula1.html'),
    'guided-discovery': ('_build/model/shells', 'guided-discovery.html'),
}

# O HUB tem anatomia propria: no imersivo as aulas sao lista corrida; no guided-discovery
# sao agrupadas por BLOCO (Build/Explore/Organize/Challenge/Transfer), que e a unidade
# pedagogica do ciclo. Ordem do Dan (07/08/2026): "o hub dessa nova versao e dividido em
# blocos e queremos isso". Lista plana de 20 esconde exatamente isso.
#
# O hub do imersivo tambem e um par prof/aluno de arquivos PUBLICADOS — mesma divida
# declarada do shell de aula.
# Sao DOIS arquivos por anatomia: o hub do professor e o do aluno. Nao e duplicacao a toa —
# a aba ativa e o conjunto de abas diferem (o aluno nao ve Planejamento nem Evidencias).
HUBS = {
    'imersivo': None,  # usa {MODEL}.html em public/professor e public/aluno
    'guided-discovery': ('_build/model/shells',
                         'hub-guided-discovery.html',
                         'hub-guided-discovery-aluno.html'),
}


def hub_path(cfg, aluno=False):
    """De qual arquivo sai o HUB. None => o hub publicado da anatomia imersivo."""
    anat = ANATOMIA_POR_SLUG.get(cfg.get('slug'), 'imersivo')
    alvo = HUBS.get(anat)
    if alvo is None:
        base = ALUNO if aluno else PROF
        return os.path.join(base, f'{MODEL}.html')
    p = os.path.join(ROOT, alvo[0], alvo[2] if aluno else alvo[1])
    if not os.path.exists(p):
        raise SystemExit(f'hub da anatomia "{anat}" nao encontrado: {p}')
    return p

# Que anatomia cada persona usa. Quem nao esta aqui usa `imersivo` — que e o que gera tudo
# o que existe hoje, entao nenhum material muda de origem.
def _carrega_anatomias():
    """O inventario declarado (anatomias.json) e a fonte de quais abas cada anatomia tem.
    Ausente => {} , e todo mundo cai no comportamento do legado."""
    p = os.path.join(ROOT, '_build', 'model', 'anatomias.json')
    if not os.path.exists(p):
        return {}
    with open(p, encoding='utf-8') as fh:
        return json.load(fh).get('anatomias', {})


ANATOMIAS_DECLARADAS = _carrega_anatomias()


ANATOMIA_POR_SLUG = {
    'stephanie-vicente': 'guided-discovery',
}


def shell_path(cfg):
    """De QUAL arquivo sai o shell desta aula.

    Resolve pela ANATOMIA da persona (ANATOMIA_POR_SLUG), nao pelo framework. O shell e
    forma, e forma pertence ao molde: declarar no framework faria QUALQUER aluno daquele
    framework herdar a anatomia nova no proximo rebuild — inclusive quem ja tem aula no ar.

    O GATE 18 (scripts/check_shell_drift.py) vigia as anatomias entre si: reprova quando
    divergem nas funcoes JS ou nas classes-mecanismo, e exige que toda diferenca legitima
    esteja declarada com motivo.
    """
    anat = ANATOMIA_POR_SLUG.get(cfg.get('slug'), 'imersivo')
    pasta, arquivo = ANATOMIAS[anat]
    p = os.path.join(ROOT, pasta, arquivo)
    if not os.path.exists(p):
        raise SystemExit(f'shell da anatomia "{anat}" nao encontrado: {p}')
    return p
# EIXO FRAMEWORK (public/data/frameworks.json é a FONTE ÚNICA — ver _build/model/FRAMEWORKS.md).
# `model` no config = CATEGORIA (adulto/kids/teens). `framework` = o MÉTODO dentro dela.
# Config sem a chave => o framework da casa, que é o que gera tudo hoje.
FRAMEWORK_DEFAULT = 'imersivo-prototipo'

# Versão do BUILDER que gerou a aula (<meta name="alumni-gen">). Sobe UMA vez por
# invariante nova, e a aula carrega para sempre a versão em que nasceu. É isso que
# permite criar gate novo sem acusar o passado: o gate roda só em quem nasceu depois
# dele (ver check_player_vivo / check_predicao em validate_lesson.py).
#   1 = player de listening completo · pergunta de predição · banco do gap-fill
#       desembaralhado · tarefa de pré-leitura em nível de GIST · input de volta na
#       etapa de detalhe (28/07/2026, feedback da chefe nos mocks de framework)
#   2 = a predição do listening em SLIDE PRÓPRIO, antes das perguntas (1a escuta confere
#       o palpite; a 2a, com as perguntas na tela, responde) · banco de palavras também
#       no gap-fill de vocabulário autorado em .fill-grid (29/07/2026, feedback da chefe
#       na aula 1 da Ana Claudia)
BUILDER_GEN = 2
MODEL_ACCENT = ('#BE123C', '#be123c')
MODEL_ACCENT_LIGHT = ('#F43F5E', '#f43f5e')
MODEL_ACCENT_RGB = 'rgba(190,18,60'
MODEL_CHARS = ['helen', 'james']  # classes de diálogo do shell, em ordem (1o = aluno)


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def contrato_versao(fw):
    """Versão ATUAL do contrato daquele framework, ou None se ele não tem contrato.
    Fonte única: public/data/frameworks.json (o mesmo arquivo que o catálogo edita).
    Ilegível/ausente => None: o carimbo some, o GATE 12 ignora a aula, e a geração
    segue. Um arquivo de dados quebrado não pode impedir aula de nascer."""
    try:
        with open(os.path.join(ROOT, 'public', 'data', 'frameworks.json'), encoding='utf-8') as f:
            d = json.load(f)
    except Exception:
        return None
    for cat in d.get('categorias', []):
        for f_ in cat.get('frameworks', []):
            if f_['id'] == fw and f_.get('contrato'):
                return int(f_['contrato']['versao'])
    return None


def _framework_obj(cfg):
    """O objeto do framework desta aula em public/data/frameworks.json, ou None."""
    try:
        with open(os.path.join(ROOT, 'public', 'data', 'frameworks.json'), encoding='utf-8') as f:
            d = json.load(f)
    except Exception:
        return None
    fw = cfg.get('framework', FRAMEWORK_DEFAULT)
    for cat in d.get('categorias', []):
        for f_ in cat.get('frameworks', []):
            if f_['id'] == fw:
                return f_
    return None


def framework_contrato_etapas(cfg):
    """As etapas do CONTRATO (a funcao de cada uma, do normativo). [] se nao declara."""
    f_ = _framework_obj(cfg)
    return ((f_ or {}).get('contrato') or {}).get('etapas', []) or []


def framework_percurso_min(cfg):
    """percurso_min do contrato (55 nos quatro frameworks da anatomia). None se nao ha."""
    f_ = _framework_obj(cfg)
    return ((f_ or {}).get('contrato') or {}).get('percurso_min')


def lesson_stages(cfg):
    """As ETAPAS desta aula: [(rotulo, minutos|None), ...].

    O ROTULO E CONTEUDO AUTORAL DA AULA, nao o nome canonico do framework. Medido no
    artefato de referencia: a aula de ESP chama as etapas de "Real-world need / Situation
    analysis / First attempt / Toolkit / Rehearsal / Performance / Upgrade & plan", e a de
    Reading de "The brief / First read / Reading closely / ...". O normativo (slides 8-11)
    fixa a FUNCAO de cada etapa; o rotulo e a traducao daquela funcao para o assunto DESTA
    aula. Gerar a barra a partir do nome canonico apagaria essa camada.

    Fonte, em ordem:
      1. lesson.stages = [{"n": "The brief", "min": 5}, ...]  <- forma completa (com minutos)
      2. lesson.phases = ["The brief", ...]                   <- forma antiga, so nomes

    A forma 2 continua valendo e sai byte-a-byte igual ao que saia antes (sem minutos). E o
    que mantem a anatomia imersivo intocada: la a barra e de CAPITULOS da narrativa e nunca
    teve orcamento de minutos.
    """
    L = cfg['lesson']
    if L.get('stages'):
        return [(e['n'], e.get('min')) for e in L['stages']]
    return [(n, None) for n in L['phases']]


def assert_framework(cfg):
    """Falha CEDO (antes de escrever qualquer arquivo) se o config declarar um framework
    que não existe na categoria, ou se puser framework experimental num aluno real.

    É a mesma regra do GATE 11 (scripts/check_framework_isolation.py), aplicada aqui na
    entrada em vez de só no PR: melhor o builder recusar do que gerar 25 slides + 50 MP3
    de uma aula que o gate vai barrar depois. Fonte única: public/data/frameworks.json.
    """
    fw = cfg.get('framework', FRAMEWORK_DEFAULT)
    cat = cfg.get('model', 'adulto')
    path = os.path.join(ROOT, 'public', 'data', 'frameworks.json')
    if not os.path.exists(path):          # repo sem o catálogo ainda: não trava a geração
        return
    try:
        data = json.load(open(path, encoding='utf-8'))
    except (json.JSONDecodeError, OSError) as e:
        # NUNCA derrubar uma geração em andamento por causa deste arquivo. Se ele estiver
        # ilegível, avisa alto e segue: quem barra de verdade é o GATE 11 no CI, e lá o
        # JSON quebrado aparece como erro do próprio gate, no PR certo.
        print(f'  aviso: frameworks.json ilegível ({e}) — validação de framework PULADA '
              f'nesta geração. O GATE 11 ainda roda no PR.', file=sys.stderr)
        return
    cats = {c['id']: c for c in data['categorias']}
    assert cat in cats, (
        f'categoria "{cat}" não existe em public/data/frameworks.json '
        f'(disponíveis: {sorted(cats)})')
    disponiveis = {f['id']: f for f in cats[cat]['frameworks']}
    assert fw in disponiveis, (
        f'framework "{fw}" não está cadastrado na categoria "{cat}". '
        f'Disponíveis: {sorted(disponiveis)}. Para criar um novo, acrescente o objeto em '
        f'public/data/frameworks.json (é a fonte única — nada mais precisa mudar).')
    if disponiveis[fw]['status'] != 'producao':
        mocks = set(data.get('mocks', {}).get(fw, []))
        assert cfg['slug'] in mocks, (
            f'framework "{fw}" tem status "{disponiveis[fw]["status"]}" (não é de produção) '
            f'e o slug "{cfg["slug"]}" não está em mocks["{fw}"] de frameworks.json. '
            f'Aluno real NÃO recebe framework em validação — gere num aluno mock primeiro '
            f'(ordem do Dan, 27/07/2026).')

    # RODÍZIO (30/07/2026) — se este aluno tem uma sequência declarada, a aula que está
    # sendo gerada TEM de trazer o framework que a posição dela pede. Aqui a checagem vale
    # ainda mais do que no CI: o config é a ÚNICA fonte da aula, e um framework trocado só
    # apareceria depois de 25 slides e ~50 MP3 gerados.
    rod = next((r for r in data.get('rodizios', []) if r['slug'] == cfg['slug']), None)
    if rod:
        ciclo, desde = rod.get('ciclo') or [], rod.get('desde_aula', 1)
        n = (cfg.get('lesson') or {}).get('n')
        if ciclo and n and n >= desde:
            esperado = ciclo[(n - desde) % len(ciclo)]
            assert fw == esperado, (
                f'rodízio declarado para "{cfg["slug"]}": o ciclo {" > ".join(ciclo)} '
                f'(a partir da aula {desde}) pede "{esperado}" na aula {n}, mas o config '
                f'declara "{fw}". Corrija o config ou o rodizios[] de frameworks.json — '
                f'o GATE 11 barraria isto no PR de qualquer forma.')


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'  wrote {os.path.relpath(p, ROOT)} ({len(s)//1024} KB)')


def replace_between(s, start, end, new_inner):
    i = s.index(start)
    j = s.index(end, i + len(start))
    return s[:i + len(start)] + new_inner + s[j:]


# Fim do painel de IN CLASS. Era a string literal "TAB 4", o que amarrava o
# builder a UMA ordem de abas: na anatomia do molde stephanie-vicente o IN CLASS e a aba 4 e
# quem vem depois e a 5, e o builder cortava no lugar errado (ou estourava com ValueError).
# Generico resolve para as duas e para qualquer anatomia futura — o que importa e "o
# proximo comentario de aba", nao o numero dele.
FIM_DO_INCLASS = '<!-- ========== TAB '


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
#   {"kind":"timer","id":"w1","segundos":600,"label":"..."}
#   (o kind gist aceita "why": o racional, que nasce escondido e a professora revela)
#   {"kind":"evidence","title":"...","items":[["afirmacao","o trecho que sustenta"], ...]}
#   {"kind":"recap","title":"...","items":["...", ...]}
#   {"kind":"write","id":"fb1","title":"...","campos":[["Rotulo","chave"], ...]}
#   {"kind":"qsub","title":"...","items":[["pergunta","como responder"], ...]}
#   {"kind":"phrases","title":"...","items":[["frase","funcao","fala opcional"], ...]}
#   {"kind":"reveal","title":"...","sub":"...","dica":"click to reveal",
#    "items":[["frente","verso","essencial|condicional|extensao"], ...]}
#   {"kind":"selfassess","title":"...","sub":"...","items":["...", ...],"escala":[4 rotulos EN]}
#   {"kind":"sorting","title":"...","cols":["Unsorted","A","B"],"items":[["frase",1], ...]}
#       cols[0] e SEMPRE a caixa de partida ("Unsorted"): o item nasce nela e cicla ao
#       clique. O 2o valor do item e o INDICE da coluna certa — nunca 0.
#   {"kind":"matching","title":"...","words":[["1","word","c"], ...],"defs":[["a","def"], ...]}
#       3o item da palavra = LETRA da definicao certa (gabarito). E OBRIGATORIO: sem ele o
#       bloco vira duas listas mortas na tela e o aluno tenta clicar/arrastar e nada
#       acontece. As definicoes seguem EMBARALHADAS (REGRA 24) -- o gabarito e que liga.
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


def _titulo(b):
    """O CABECALHO DE UM BLOCO, do jeito do artefato.

    Nao ha wrapper e nao ha <h3>: DENTRO de um slide o artefato so tem o titulo da propria
    tela (<h2 class="slide-heading">) e, abaixo dele, a linha de instrucao
    <p class="slide-lead">. O <h3 class="sub"> existe no artefato, mas SO no chrome do
    Professor View (hub/syllabus) — nunca dentro de .slide; usa-lo aqui seria emitir uma
    classe sem CSS na aula, que foi o defeito que a comparacao lado a lado pegou.

    O ic-card/ic-card-h3 que envolvia tudo aqui NAO EXISTE no artefato — era invencao do
    porte de 07/08, e era o que mais separava a tela gerada da tela do artefato.
    """
    if not b.get('title'):
        return ''
    return f'<p class="slide-lead">{_esc(b["title"])}</p>'


def _lead(b, campo='sub'):
    """A segunda linha de instrucao: <p class="subprompt"> no artefato (6,2 usos/aula)."""
    if not b.get(campo):
        return ''
    return f'<p class="subprompt">{_esc(b[campo])}</p>'


def _audio(fala, pequeno=True):
    """Botao de audio. FORMA do artefato (.audio-btn-sm.ghost com o glifo), MOTOR do repo.

    O artefato chama say(), que e Web Speech. Aqui o mesmo botao toca o MP3 do audioMap
    (REGRA 7) e o texto vai no ATRIBUTO, nunca dentro da string JS (REGRA 7.1) — o ingles
    tem apostrofo e o handler morreria. Isso e camada por cima, nao divergencia de
    interface: mesma classe, mesmo lugar, mesmo glifo.
    """
    if not fala:
        return ''
    cls = 'audio-btn-sm ghost' if pequeno else 'audio-btn'
    return (f'<button class="{cls}" data-speak="{_esc(fala)}" '
            f'onclick="speakText(this.dataset.speak,this)">&#9654;</button>')


def _render_block(b):
    """Emite o HTML de UM bloco, com as classes DO ARTEFATO.

    Fonte: _build/model/artefatos/erica-professor-view.html. Copia-se dele — mesmos nomes
    de classe, mesma estrutura de tags, mesmo aninhamento. Decisao do Dan (11/08/2026):
    "SE AS AULAS NAO ESTAO IDENTICAS AO ARTEFATO, NO QUESITO INTERFACE, ENTAO ESTA ERRADO".

    TRES kinds seguem em .ic-* de proposito — matching, call e quickfire NAO EXISTEM no
    artefato em nenhuma forma, e inventar markup "no estilo dele" seria repetir o erro de
    07/08. Aguardam decisao da autora; ver anatomias.json -> _pendente_sem_forma_no_artefato.
    """
    k = b['kind']

    # ── callout: a peca MAIS usada do artefato (23,8/aula) e que nunca tinha sido portada
    if k in ('vocabnote', 'followup'):
        # .callout e a peca MAIS usada do artefato (23,8/aula) e nunca tinha sido portada.
        # O titulo e opcional la, e quando existe vem como <span class="callout-title">.
        tit = (f'<span class="callout-title">{_esc(b["title"])}</span>'
               if b.get('title') else '')
        variante = b.get('variante', '')
        assert variante in ('', 'rule-box', 'warn', 'danger', 'ok'), (
            f'callout: variante "{variante}" nao existe no artefato '
            f'(use rule-box, warn, danger ou ok)')
        cls = f'callout {variante}'.strip()
        return f'<div class="{cls}">{tit}{_esc(b["text"])}</div>'

    if k in ('questions', 'guiding', 'analyse'):
        itens = ''.join(f'<div class="q-item">{_esc(q)}</div>' for q in b['items'])
        return f'{_titulo(b)}<div class="qlist">{itens}</div>'

    if k == 'qsub':
        # a pergunta e a instrucao de COMO responder: <div class="q-item"> + <p class="subprompt">
        itens = ''.join(f'<div class="q-item">{_esc(q)}</div>'
                        f'<p class="subprompt">{_esc(sub)}</p>' for q, sub in b['items'])
        return f'{_titulo(b)}<div class="qlist">{itens}</div>'

    if k == 'reveal':
        STATUS = {'essencial': ('', ''), 'condicional': ('cond', 'cond-tag'),
                  'extensao': ('ext', 'ext-tag')}
        itens = ''
        for it in b['items']:
            frente, verso = it[0], it[1]
            st = it[2] if len(it) > 2 else 'essencial'
            assert st in STATUS, (
                f'reveal: status "{st}" invalido — use essencial, condicional ou extensao')
            cls, tagcls = STATUS[st]
            rot = {'cond-tag': 'Conditional', 'ext-tag': 'Extension'}.get(tagcls, '')
            tag = f'<span class="{tagcls}">{rot}</span>' if tagcls else ''
            itens += (f'<div class="reveal-item{" " + cls if cls else ""}" '
                      f'onclick="this.classList.toggle(\'revealed\')">'
                      f'{tag}<div class="r-front">{_esc(frente)}</div>'
                      f'<div class="r-back">{_esc(verso)}</div></div>')
        return f'{_titulo(b)}{_lead(b)}{itens}'

    if k == 'gist':
        # quiz-item / quiz-question / quiz-options / quiz-option / option-letter / rationale
        LETRAS = 'ABCDEFGH'
        ch = ''
        for i, c in enumerate(b['choices']):
            right = '1' if c[2] else '0'
            ch += (f'<div class="quiz-option" onclick="icPick(this,{right})">'
                   f'<span class="option-letter">{LETRAS[i]}</span><span>{_esc(c[1])}</span></div>')
        why = f'<div class="rationale">{_esc(b["why"])}</div>' if b.get('why') else ''
        return (f'<div class="quiz-item"><p class="quiz-question">{_esc(b["prompt"])}</p>'
                f'<div class="quiz-options">{ch}</div>{why}</div>')

    if k == 'tf':
        # No artefato nao ha true/false proprio: a forma dele para "escolha uma e veja por
        # que" e o quiz-item com opcoes + rationale. E o que se usa aqui — copia de FORMA,
        # nao invencao: zero classe nova.
        out = ''
        for i, it in enumerate(b['items']):
            ans = str(it[1]).strip().lower()
            assert ans in ('t', 'f', 'true', 'false'), f'tf item[1] deve ser t/f: {it!r}'
            verdadeiro = ans in ('t', 'true')
            just = f'<div class="rationale">{_esc(it[2])}</div>' if len(it) > 2 and it[2] else ''
            opts = ''.join(
                f'<div class="quiz-option" onclick="icPick(this,{1 if (rot == "TRUE") == verdadeiro else 0})">'
                f'<span class="option-letter">{rot[0]}</span><span>{rot}</span></div>'
                for rot in ('TRUE', 'FALSE'))
            out += (f'<div class="quiz-item"><p class="quiz-question">{i + 1}. {_esc(it[0])}</p>'
                    f'<div class="quiz-options">{opts}</div>{just}</div>')
        return f'{_titulo(b)}{out}'

    if k == 'recap':
        itens = ''.join(
            f'<label class="recap-item"><input type="checkbox" onchange="icSave(this)">'
            f'<span>{_esc(t)}</span></label>' for t in b['items'])
        tit = _esc(b.get('title', 'What we built'))
        sub = f'<p class="cb-sub">{_esc(b["sub"])}</p>' if b.get('sub') else ''
        return f'<div class="close-block"><h5>{tit}</h5>{sub}{itens}</div>'

    if k == 'write':
        campos = ''
        for c in b['campos']:
            rot, chave = (c if isinstance(c, list) else [c, snake(c)])
            wid = f'{_esc(b["id"])}-{_esc(chave)}'
            campos += (f'<div class="fb-field"><label for="{wid}">{_esc(rot)}</label>'
                       f'<textarea id="{wid}" class="writebox" data-k="{wid}" '
                       f'oninput="icWriteSave(this)" aria-label="{_esc(rot)}"></textarea></div>')
        return f'{_titulo(b)}<div class="fb-board">{campos}</div>'

    if k == 'whiteboard':
        lbl = _esc(b.get('label', ''))
        head = f'<label for="wb">{lbl}</label>' if lbl else ''
        return (f'<div class="fb-field">{head}<textarea id="wb" class="writebox" data-k="wb" '
                f'oninput="icWriteSave(this)" style="min-height:190px"></textarea></div>')

    if k == 'selfassess':
        escala = b.get('escala', ['Not yet', 'Getting there', 'Comfortable', 'Confident'])
        for r in escala:
            assert not re.search(r'[ãõçáéíóúâêô]', r), (
                f'selfassess: rotulo "{r}" tem acento — a tela do aluno e em ingles a partir '
                f'de A2 (REGRA 13).')
        linhas = ''
        for i, q in enumerate(b['items']):
            botoes = ''.join(
                f'<button class="conf-btn" data-cf="{i}" data-v="{v}" '
                f'onclick="icConfPick(this)">{_esc(r)}</button>'
                for v, r in enumerate(escala))
            linhas += (f'<div class="conf-item"><div class="cf-label">{_esc(q)}</div>'
                       f'<div class="conf-scale">{botoes}</div></div>')
        tit = _esc(b.get('title', 'How confident do you feel right now?'))
        return (f'<p class="slide-lead">{tit}</p>{_lead(b)}{linhas}'
                f'<div class="score-out">0 / {len(b["items"])} answered</div>')

    if k == 'timer':
        # O timer-btn EXISTE no artefato (30 usos), so que no chrome do Professor View e
        # nunca dentro de .slide. A FORMA e copiavel, entao vem como esta — decisao do Dan
        # (11/08/2026). Nao e invencao: mesma classe, mesmo markup, mesmo CSS.
        tid = f'tmr-{_esc(b["id"])}'
        total = int(b['segundos'])
        rot = _esc(b.get('label', 'Time yourself'))
        return (f'<p class="slide-lead">{rot}</p>'
                f'<div class="timerbox"><span class="timer-read" id="{tid}">'
                f'{total // 60}:{total % 60:02d}</span>'
                f'<button class="timer-btn" onclick="icTimerStart(this,\'{tid}\',{total})">Start / Pause</button>'
                f'<button class="timer-btn" onclick="icTimerReset(this,\'{tid}\',{total})">Reset</button>'
                f'</div>')

    if k == 'evidence':
        itens = ''.join(
            f'<div class="evi"><span class="evi-src">{_esc(f)}</span>{_esc(a)}</div>'
            for a, f in b['items'])
        return f'{_titulo(b)}<div class="evi-list">{itens}</div>'

    if k == 'reading':
        ps = ''.join(f'<p>{_esc(p)}</p>' for p in b['paras'])
        src = ''
        if b.get('source'):
            link = (f' <a href="{_esc(b["link"])}" target="_blank" rel="noopener">'
                    f'{_esc(b["link"])}</a>') if b.get('link') else ''
            src = f'<span class="evi-src">{_esc(b["source"])}{link}</span>'
        rt = f'<p class="slide-lead">{_esc(b["rtitle"])}</p>' if b.get('rtitle') else ''
        return f'{rt}<div class="evi-list"><div class="evi">{src}{ps}</div></div>'

    if k in ('phrases', 'lf'):
        linhas = ''
        if k == 'phrases':
            for it in b['items']:
                frase, funcao = it[0], it[1]
                fala = it[2] if len(it) > 2 and it[2] else frase
                linhas += (f'<div class="phrase-row"><span class="phrase-en">{_esc(frase)}</span>'
                           f'<span class="phrase-fn">{_esc(funcao)}</span>{_audio(fala)}</div>')
        else:
            for it in b['items']:
                forte = ' cond-row' if (len(it) > 4 and it[4] == 'strong') else ''
                fala = it[5] if len(it) > 5 and it[5] else None
                frase = f'{it[1]}{it[2]}{it[3]}'
                linhas += (f'<div class="phrase-row{forte}">'
                           f'<span class="phrase-en">{_esc(frase)}</span>'
                           f'<span class="phrase-fn">{_esc(it[0])}</span>{_audio(fala)}</div>')
        tit = b.get('title') or ('Read the advice' if k == 'lf' else None)
        head = f'<p class="slide-lead">{_esc(tit)}</p>' if tit else ''
        return f'{head}<div class="phrase-list">{linhas}</div>'

    if k == 'bank':
        itens = ''.join(
            f'<div class="phrase-row"><span class="phrase-en">{_esc(w)}</span></div>'
            for w in b['items'])
        tit = _esc(b.get('label', 'Useful language'))
        return f'<p class="slide-lead">{tit}</p><div class="phrase-list">{itens}</div>'

    if k == 'modals':
        cards = ''.join(
            f'<div class="s-card"><div class="s-meta">{_esc(c[1])}</div>'
            f'<h5>{_esc(c[0])}</h5><span class="rc-body">{_esc(c[2])}</span></div>'
            for c in b['cards'])
        tit = _esc(b.get('title', 'Meaning guide'))
        return f'<p class="slide-lead">{tit}</p><div class="card-row">{cards}</div>'

    if k == 'scenarios':
        dl = ''.join(f'<dt>{_esc(it[0])}</dt><dd>{_esc(it[1])}</dd>' for it in b['items'])
        return f'<div class="brief"><dl>{dl}</dl></div>'

    if k == 'gapfill':
        html = ''
        for p in b['parts']:
            if isinstance(p, list):
                html += f'<input class="blank-input" data-n="{_esc(p[0])}" aria-label="gap {_esc(p[0])}">'
            else:
                html += _esc(p)
        ordem = b['bank'][1::2] + b['bank'][0::2]
        assert len(b['bank']) < 2 or ordem != list(b['bank']), (
            f'gapfill: o banco {b["bank"]!r} ficou na ordem original depois do embaralho')
        banco = ''.join(f'<span class="phrase-en">{_esc(w)}</span>' for w in ordem)
        return (f'<div class="fill-blank-item"><span class="fill-blank-sentence">{html}</span></div>'
                f'<div class="phrase-list"><div class="phrase-row">{banco}</div></div>')

    if k == 'rephrase':
        rows = ''
        for it in b['items']:
            rows += (f'<div class="fill-blank-item"><span class="fill-blank-sentence">'
                     f'{_esc(it[0])} <em>({_esc(it[1])})</em> '
                     f'<input class="blank-input" aria-label="rephrase"></span></div>')
        return f'{_titulo(b)}{rows}'

    if k == 'sorting':
        # .sort-group e o CONTAINER DE ESTADO (data-cols/data-items/data-state). Ele nao
        # existe no artefato — la o sorting usa id="gdsort" FIXO, o que so permite UM por
        # aula. O container com estado proprio permite varios na mesma aula, e por isso a
        # divergencia e MELHORIA, nao desvio. Visualmente e nulo: quem desenha e o .sortbox
        # interno, com o grid do artefato. Declarado em anatomias.json ->
        # _divergencia_por_limitacao_do_artefato. Nao leva prefixo ic-: nao e reescrita.

        cols = b['cols']
        assert len(cols) >= 3, 'sorting: precisa de cols[0] (partida) + 2 categorias no minimo'
        items = b['items']
        for texto, certa in items:
            assert 1 <= certa < len(cols), (
                f'sorting: "{texto[:40]}" aponta para a coluna {certa}; '
                f'0 e a caixa de partida e nao pode ser gabarito')
        dados = json.dumps([{'t': t, 'a': a} for t, a in items], ensure_ascii=False)
        estado = json.dumps([0] * len(items))
        return (f'{_titulo(b)}<div class="sort-group" '
                f'data-cols=\'{json.dumps(cols, ensure_ascii=False)}\' '
                f'data-items=\'{dados}\' data-state=\'{estado}\'>'
                f'<div class="sortbox"></div><div class="score-out"></div>'
                f'<div class="btn-bar"><button class="verify-all-btn" onclick="icSortCheck(this)">Check</button>'
                f'<button class="verify-all-btn ghost" onclick="icSortReset(this)">Reset</button></div></div>')

    if k == 'answer':
        titulo = _esc(b.get('title', 'Reveal answer key'))
        if b.get('key'):
            inner = ' · '.join(_esc(a) for a in b['key'])
        elif b.get('list'):
            nota = f'{_esc(b["note"])}<br><br>' if b.get('note') else ''
            inner = nota + '<br>'.join(f'{i + 1}. {_esc(a)}' for i, a in enumerate(b['list']))
        else:
            inner = ''
        return (f'<div class="btn-bar"><button class="verify-all-btn ghost" '
                f'onclick="icReveal(this)">{titulo}</button></div>'
                f'<div class="rationale"><div class="callout rule-box">{inner}</div></div>')

    # ── SEM CONTRAPARTIDA NO ARTEFATO — seguem em .ic-*, por decisao registrada ──────────
    if k == 'call':
        cast = b['cast']
        chips = ''.join(
            f'<span class="ic-spk" data-spk="{i}">{_esc(c["nome"])}<span class="ic-sub">'
            f'{_esc(c.get("papel", ""))}</span></span>' for i, c in enumerate(cast))
        turnos = json.dumps(
            [{'s': t[0], 'f': f'/audio/{b["slug"]}/{b["prefixo"]}{i + 1:02d}.mp3'}
             for i, t in enumerate(b['turnos'])], ensure_ascii=False)
        segs = ''
        for rot, de, ate in b.get('segmentos', [['Play the call', None, None]]):
            a = 'null' if de is None else de
            z = 'null' if ate is None else ate
            segs += (f'<button class="ic-seg" onclick="icCallPlay(this,{a},{z})">'
                     f'{_esc(rot)}</button>')
        segs += ('<button class="ic-seg" onclick="icCallPlay(this,null,null,0.8)">Slower</button>'
                 '<button class="ic-seg ic-stop" onclick="icCallStop()">Stop</button>')
        return (f'{_titulo(b)}<div class="ic-call" data-turnos=\'{turnos}\'>'
                f'<div class="ic-call-cast">{chips}</div>'
                f'<div class="ic-call-segs">{segs}</div></div>')

    if k == 'matching':
        defkeys = [str(d[0]) for d in b['defs']]
        assert len(set(defkeys)) == len(defkeys), f'matching: letras de defs repetidas: {defkeys}'
        keys = []
        for w in b['words']:
            assert len(w) >= 3 and str(w[2]).strip(), (
                f'matching: a palavra "{w[1] if len(w) > 1 else w}" nao declara a definicao certa.')
            k2 = str(w[2]).strip()
            assert k2 in defkeys, (
                f'matching: palavra "{w[1]}" aponta para a definicao "{k2}", '
                f'que nao existe em defs {defkeys}')
            keys.append(k2)
        assert len(set(keys)) == len(keys), (
            f'matching: duas palavras apontam para a mesma definicao: {keys}')
        words = ''.join(
            f'<div class="ic-chip ic-word" role="button" tabindex="0" data-k="{_esc(w[0])}" '
            f'data-match="{_esc(w[2])}" onclick="icPickMatch(this)">'
            f'<span class="ic-k">{_esc(w[0])}</span><span>{_esc(w[1])}</span>'
            f'<span class="ic-pair"></span></div>'
            for w in b['words'])
        defs = ''.join(
            f'<div class="ic-chip ic-def" role="button" tabindex="0" data-k="{_esc(d[0])}" '
            f'onclick="icPickMatch(this)">'
            f'<span class="ic-k">{_esc(d[0])}</span><span>{_esc(d[1])}</span>'
            f'<span class="ic-pair"></span></div>'
            for d in b['defs'])
        hint = _esc(b.get('hint') or 'Tap a word, then tap its meaning')
        return (f'{_titulo(b)}<p class="ic-match-hint">{hint}</p>'
                f'<div class="ic-match-score">0 / {len(b["words"])} matched</div>'
                f'<div class="ic-match" data-interactive="1">'
                f'<div class="ic-match-col"><h4>Words &amp; expressions</h4>{words}</div>'
                f'<div class="ic-match-col"><h4>Definitions</h4>{defs}</div></div>')

    if k == 'quickfire':
        items = b['items']
        assert items, 'quickfire sem items'
        btn_st = ('background:var(--accent);color:#fff;border:none;border-radius:8px;'
                  'padding:.5rem 1.2rem;font-size:.85rem;font-weight:600;cursor:pointer')
        nav_prev = ('background:transparent;color:var(--accent);border:2px solid var(--accent);'
                    'border-radius:8px;padding:.5rem 1.2rem;font-size:.85rem;font-weight:600;'
                    'cursor:pointer')
        cards = ''
        for i, it in enumerate(items):
            disp = '' if i == 0 else 'display:none;'
            tips = ''.join(f'<li style="margin-bottom:.3rem">{_esc(t)}</li>' for t in it['tips'])
            cards += (
                f'<div class="qf-card" data-qf="{i + 1}" style="{disp}background:var(--bg-card);'
                f'border:1px solid var(--border);border-radius:12px;padding:1.2rem;'
                f'margin-bottom:.8rem">'
                f'<p class="qf-situation" style="font-size:.92rem;font-weight:600;'
                f'margin-bottom:.6rem">{_esc(it["situation"])}</p>'
                f'<button class="primary-btn qf-tips-btn" onclick="qfTips(this)" '
                f'style="{btn_st}">Tips</button>'
                f'<div class="qf-tips" style="display:none;margin-top:.6rem">'
                f'<ul style="font-size:.84rem;color:var(--text-mid);padding-left:1.1rem;'
                f'margin:0">{tips}</ul></div></div>')
        score = (f'<p style="text-align:center;font-size:.82rem;color:var(--text-dim);'
                 f'margin-top:.3rem"><span id="qfScore">1 / {len(items)}</span></p>')
        nav = ('<div class="qf-nav" style="display:flex;gap:.6rem;justify-content:center;'
               'margin-top:1rem">'
               f'<button class="qf-prev" onclick="qfNav(-1)" style="{nav_prev}">&#8592; Previous</button>'
               f'<button class="primary-btn qf-next" onclick="qfNav(1)" style="{btn_st}">Next &#8594;</button></div>')
        return f'{score}<div id="qfContainer" style="max-width:560px;margin:1rem auto 0">{cards}{nav}</div>'

    raise AssertionError(f'inclass_blocks: kind desconhecido "{k}"')


def render_block(b):
    """Emite o bloco e CARIMBA `data-kind` no primeiro elemento.

    POR QUE O CARIMBO EXISTE. O banco de exercicios (public/data/exercicios.json) e o
    GATE 12 identificavam cada exercicio por uma CLASSE EXCLUSIVA dele. Isso funcionava
    enquanto cada kind tinha classe propria (.ic-tf, .ic-gist...). Ao copiar o vocabulario
    do ARTEFATO, kinds diferentes passaram a compartilhar classe de proposito — um
    true/false E um quiz-item la, com as mesmas .quiz-option/.rationale. Resultado: 12
    exercicios ficaram indistinguiveis e o GATE 12 parou de conseguir cobra-los (a
    verificabilidade caiu de 25/28 para 13/28).

    Identificar componente pela APARENCIA e frágil por construcao — e a mesma familia de
    erro que custou o dia 11/08/2026 (inventario lendo a reescrita, gate lendo comentario,
    classe de imagem contada como player). O `data-kind` separa as duas perguntas: a CLASSE
    diz como a peca se PARECE (e e a do artefato, sem excecao); o ATRIBUTO diz o que ela E.
    Invisivel na tela, estavel, e nao toca o vocabulario copiado.
    """
    html = _render_block(b)
    k = b['kind']
    m = re.match(r'\s*<(\w+)([^>]*)>', html)
    if not m or 'data-kind=' in html[:m.end()]:
        return html
    corte = m.start(2) if m.group(2) else m.end(1)
    return html[:corte] + f' data-kind="{k}"' + html[corte:]


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


def _pergunta_de_gist(ch):
    """A pergunta de GIST do slide (o prompt do bloco kind:'gist'), sem as alternativas."""
    ch = _estrutura(ch)
    if 'class="ic-choices"' not in ch:
        return None
    m = re.search(r'<div class="ic-card-h3">(.*?)</div><div class="ic-choices">', ch, re.S)
    return _texto(m.group(1)) if m else None


def _perguntas_da_checagem(ch):
    """(kind, [perguntas]) do slide de CHECAGEM — a fonte ÚNICA das perguntas.

    ORDEM DE PREFERÊNCIA: gist > true/false > comp-q.

    A TAREFA DE PRÉ-LEITURA É DE GIST, NUNCA DE DETALHE. Até 28/07/2026 esta função
    pegava as afirmações do True/False, e o slide de tarefa abria com cinco frases
    afirmativas sobre um texto que a aluna ainda não tinha visto. Feedback da chefe:
    *"o slide 4 pode ser um exercício de prediction antes do input, mas não faz muito
    sentido ser algo de detail; tem que ser de gist, senão a sequência fica confusa."*

    Ela está certa e o motivo é a ordem em que se lê: primeiro se busca a IDEIA (uma
    passada rápida), depois o DETALHE (com o texto na frente). Uma tarefa de detalhe
    antes da primeira leitura pede as duas coisas ao mesmo tempo — e ainda entrega, de
    graça, cinco afirmações que o exercício seguinte ia cobrar.

    dialogue -> .q-text do slide de Comprehension
    reading  -> o prompt do gist; só na falta dele, as .ic-stmt do True/False.
    """
    g = _pergunta_de_gist(ch)
    if g:
        return 'gist', [g]
    ch = _estrutura(ch)
    if 'ic-tfrow' in ch:
        out = []
        for st in re.findall(r'<span class="ic-stmt">(.*?)</span>\s*<span class="ic-verdict', ch, re.S):
            out.append(_texto(re.sub(r'<span class="ic-just">.*?</span>', '', st, flags=re.S)))
        return 'tf', [q for q in out if q]
    if 'class="comp-q"' in ch and 'mock-player' not in ch:
        return 'comp', [_texto(q) for q in re.findall(r'<div class="q-text">(.*?)</div>', ch, re.S)]
    # VARIANTE LEGADA: material antigo escreve a checagem como
    #   <div class="comp-question" onclick="this.classList.toggle('revealed')">
    #     <p>a pergunta</p><p>a resposta</p></div>
    # em vez de .comp-q + .q-text. Sem reconhecer isto, inject_task_slides nao acha o
    # slide de checagem, nao emite a tarefa, e a REGRA 2.2 fica sem como ser cumprida
    # em toda aula ja gerada nesse formato. A PERGUNTA e o PRIMEIRO <p>; o segundo e o
    # gabarito e NAO pode ir para o slide de tarefa.
    if 'class="comp-question"' in ch:
        out = []
        for bloco in re.findall(r'<div class="comp-question"[^>]*>(.*?)</div>', ch, re.S):
            ps = re.findall(r'<p[^>]*>(.*?)</p>', bloco, re.S)
            if ps:
                out.append(_texto(ps[0]))
        return 'comp', [q for q in out if q]
    return None, []


def _slide_de_tarefa(kind, perguntas, phase, ancora=None):
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
            f'data-task-for="{kind}" data-teacher="{t}{_PREDICT_T}">\n'
            f'  <div class="slide-inner">\n'
            f'    <div class="chapter-label">{label}</div>\n'
            f'    <h2 class="slide-heading">{head} <span class="accent">{acc}</span></h2>\n'
            f'    {_predict_html(kind, ancora)}\n'
            f'    <div style="display:flex;flex-direction:column;gap:1rem;max-width:520px;margin:1.2rem auto 0">\n'
            f'      {qs}\n'
            f'    </div>\n'
            f'  </div>\n'
            f'</div>\n\n')


def _primeira_frase(txt, maxlen=170):
    """A primeira frase de um texto puro — a ANCORA da predicao."""
    t = ' '.join(re.sub(r'<[^>]+>', ' ', txt or '').split())
    m = re.match(r'(.{20,%d}?[.!?])\s' % maxlen, t + ' ')
    return (m.group(1) if m else t[:maxlen]).strip()


def _predict_html(kind, ancora=None):
    """A pergunta de PREDICAO — com uma ANCORA, nunca no vacuo.

    Feedback da chefe (28/07/2026), sobre a primeira versao: *"Esse daqui ficou sem
    sentido. Nao tem nenhuma informacao sobre o texto pra fazer prediction."* Ela estava
    certa: um slide que so pergunta "what do you think this text is going to be about?"
    diante de uma tela vazia nao pede predicao, pede adivinhacao. Predicao e uma hipotese
    a partir de ALGUMA evidencia — sem evidencia nao ha o que ativar.

    A saida veio do Luiz: *"podemos fornecer um trecho ou uma linha do texto, ou do audio
    em questao e ai sim debater 'What will it be about? What do you think it'll happen?'"*

    Entao aqui vai UMA linha do proprio input (a primeira frase, extraida pelo builder) e
    so entao a pergunta. Uma linha nao entrega o texto — ela da o fio.

    NAO usa .q-text: o gate da REGRA 2.2 compara as .q-text da tarefa com as da checagem,
    e a predicao nao e item de compreensao. Classe propria, fora da contagem.

    NAO pergunta mais "and what do you think happens?". Feedback da chefe (29/07/2026):
    *"Acredito que da pra remover tambem a parte que ta escrito: 'What do you think
    happens?'"* Sao DUAS perguntas onde cabe uma: a segunda so faz sentido para narrativa
    com enredo, e diante de um depoimento ou de uma conversa ela nao tem o que responder.
    Sobre o que e? ja e a hipotese inteira.
    """
    alvo = {'reading': 'text', 'dialogue': 'conversation'}.get(kind, 'audio')
    linha = (f'<div class="ic-predict-line">&ldquo;{ancora}&rdquo;</div>' if ancora else '')
    return (f'<div class="ic-predict">{linha}'
            f'<div class="ic-predict-q">This is the first line. What do you think this '
            f'{alvo} is going to be about?</div></div>')


_PREDICT_T = ('<strong>Predição (2 min):</strong> leia a frase da tela com a aluna e faça a '
              'pergunta. Aceite QUALQUER palpite, não confirme nem corrija — ela serve para '
              'ativar o que a aluna já sabe, não para acertar. Depois toque o áudio UMA vez, '
              'inteiro e sem pausa: a única tarefa aqui é ver se o palpite dela bateu. As '
              'perguntas de compreensão só aparecem no PRÓXIMO slide.')

_SEGUNDA_ESCUTA_T = (' Esta é a SEGUNDA escuta: leia as perguntas em voz alta COM a aluna '
                     'ANTES de tocar de novo — agora ela ouve procurando as respostas, não '
                     'mais para descobrir o assunto.')


def _slide_de_predicao(ancora, src, phase, label, idx):
    """O slide de PREDICAO do listening — sozinho, ANTES das perguntas.

    Feedback da chefe (29/07/2026), sobre a primeira versao (predicao dentro do proprio
    slide de listening, em cima das perguntas):

        *"vale a pena essa etapa de 'previsao' do audio vir em um slide separado, antes
        das perguntas. Porque ai o aluno debate sobre o que ele acha o que vai acontecer
        no audio, escuta uma vez, e ve se o que ele achava ta certo ou nao. Depois podemos
        exibir as perguntas, pra tocar o audio uma segunda vez e o aluno responder."*

    Ela esta certa, e o motivo e que as duas coisas competem pela MESMA tela. Com a lista
    de perguntas ja visivel ao lado, ninguem arrisca hipotese nenhuma: o olho vai direto
    no que vai ser cobrado, e a predicao — que existe para ativar o que a aluna ja sabe —
    vira um enfeite que a professora pula. Separadas, cada escuta tem UM proposito:

        [predicao: a linha + o palpite + 1a escuta]  ->  [perguntas + 2a escuta]

    Isto NAO viola a REGRA 2.1. O que ela proibe e esconder a TAREFA do aluno; aqui a
    tarefa da primeira escuta e a propria predicao, escrita na tela. As perguntas de
    compreensao continuam visiveis desde a entrada no slide em que sao cobradas.
    """
    player = _LP_TPL.format(id=f'mp-pred{idx}', src=src, qs='',
                            style=' style="max-width:460px;margin:1.4rem auto 0"')
    return ('<div class="slide slide-dark" data-slide="0" data-phase="{phase}" '
            'data-predict-for="audio" data-teacher="{t}">\n'
            '  <div class="slide-inner" style="text-align:center">\n'
            '    <div class="chapter-label">{label}</div>\n'
            '    <h2 class="slide-heading" style="color:#fff">Before You '
            '<span class="accent">Listen</span></h2>\n'
            '    {predict}\n'
            '    {player}\n'
            '  </div>\n'
            '</div>\n\n').format(phase=phase, t=_PREDICT_T, label=label,
                                 predict=_predict_html('audio', ancora), player=player)


def inject_predict_prompts(slides, cfg=None):
    """Emite o slide de PREDICAO antes de todo listening de EXPOSICAO — nunca no lead-in.

    O slide de TAREFA (dialogo/leitura) ja nasce com a predicao em _slide_de_tarefa() — e
    ele ja e um slide separado, que e exatamente a forma pedida. O listening nao tem slide
    de tarefa (as perguntas dividem a tela com o player, REGRA 2.1), entao quem cria o
    slate separado dele e esta funcao. Ver _slide_de_predicao() para o porque.

    POR QUE O LEAD-IN FICA DE FORA. Feedback da chefe (28/07/2026): *"Acho que ele
    interpretou a sugestao do Luis de colocar essa pergunta como fixa para todo momento
    que tiver audio/texto, mas aqui no lead-in nao precisa."* Ela esta certa e o motivo e
    estrutural: no lead-in o audio e CONTEXTUALIZACAO — nao ha tarefa de compreensao a
    preparar, e o aluno ainda nao tem contexto nenhum sobre o qual arriscar uma hipotese.
    Predicao no primeiro slide da aula nao ativa conhecimento previo: nao ha o que ativar.
    Regra: data-phase="1" nao recebe predicao.

    A ANCORA vem da primeira frase do script do listening (config.lesson.listenings), que
    o builder ja tem em maos. Uma linha nao e transcricao — o sound-first continua de pe.

    IDEMPOTENTE, inclusive sobre a forma ANTIGA: se o listening ainda carrega o
    .ic-predict inline (aula gerada antes de 29/07/2026 e reconstruida agora), ele sai de
    dentro do slide e vira o slide novo. Rodar duas vezes nao duplica.
    """
    scripts = {}
    for ls in ((cfg or {}).get('lesson') or {}).get('listenings', []) or []:
        if ls.get('file'):
            scripts[ls['file']] = ls.get('text', '')
    partes = re.split(r'(?=<div class="slide )', slides)
    out, idx = [], 0
    for ch in partes:
        est = _estrutura(ch)
        tem_player = 'data-src="/audio/' in est
        tem_qs = 'class="comp-questions"' in est
        eh_leadin = 'data-phase="1"' in est
        ja_tem = bool(out and 'data-predict-for=' in out[-1])
        if tem_player and tem_qs and not eh_leadin and not ja_tem:
            # forma antiga: a predicao morava DENTRO do slide de listening. Tira de la.
            # _match_div_end porque o bloco tem divs aninhados (.ic-predict-line/-q): um
            # regex .*?</div> cortaria no primeiro fechamento e deixaria lixo na tela.
            i = ch.find('<div class="ic-predict">')
            if i >= 0:
                fim = _match_div_end(ch, i)
                if fim > 0:
                    ch = ch[:i] + ch[fim:].lstrip('\n')
            m = re.search(r'data-src="([^"]*/([^"/]+\.mp3))"', est)
            if m:
                idx += 1
                ancora = _primeira_frase(scripts.get(m.group(2), ''))
                lab = re.search(r'<div class="chapter-label">([^<]*)</div>', _estrutura(ch))
                phase = (re.search(r'data-phase="(\d+)"', est) or [None, '4'])[1]
                out.append(_slide_de_predicao(ancora, m.group(1), phase,
                                              lab.group(1) if lab else 'Listening', idx))
                ch = re.sub(r'(data-teacher="(?:[^"\\]|\\.)*?)"',
                            lambda m2: m2.group(1) + _SEGUNDA_ESCUTA_T + '"', ch, count=1)
        out.append(ch)
    return ''.join(out)


# Player de listening COMPLETO (REGRA 2.1: seekbar + tempo + play/pause + ±5s + velocidade).
# O shorthand <div class="audio-player" data-src="..."></div> era um DIV VAZIO: sem
# controles, sem CSS, sem JS. A aula ia ao ar com o MP3 gerado e um retângulo em branco
# na tela — a professora abria o slide e não havia o que tocar (achado no feedback dos
# mocks, 28/07/2026). O builder passa a expandir o shorthand para o markup real, que fala
# com o mpGet/mpToggle já existentes no shell do modelo.
_LP_TPL = (
    '<div class="mock-player lp" id="{id}" data-src="{src}"{qs}{style}>'
    '<div class="lp-seekbar" onclick="mpSeek(event,\'{id}\')"><div class="lp-progress" id="progress-{id}"></div></div>'
    '<div class="lp-times"><span id="time-current-{id}">0:00</span><span id="time-total-{id}">0:00</span></div>'
    '<div class="lp-row">'
    '<button class="lp-btn" onclick="mpSkip(\'{id}\',-5)" aria-label="Back 5 seconds">-5s</button>'
    '<button class="lp-btn lp-play" id="play-{id}" onclick="mpToggle(\'{id}\')" aria-label="Play or pause">'
    '<svg class="lp-icon-play" viewBox="0 0 24 24" width="18" height="18"><polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg>'
    '<svg class="lp-icon-pause" viewBox="0 0 24 24" width="18" height="18" style="display:none">'
    '<rect x="6" y="4" width="4" height="16" fill="currentColor"/><rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg>'
    '</button>'
    '<button class="lp-btn" onclick="mpSkip(\'{id}\',5)" aria-label="Forward 5 seconds">+5s</button>'
    '</div>'
    '<div class="lp-speeds">'
    '<button class="lp-speed-btn" onclick="mpSpeed(\'{id}\',0.5,this)">0.5x</button>'
    '<button class="lp-speed-btn" onclick="mpSpeed(\'{id}\',0.75,this)">0.75x</button>'
    '<button class="lp-speed-btn lp-speed-active" onclick="mpSpeed(\'{id}\',1,this)">1x</button>'
    '<button class="lp-speed-btn" onclick="mpSpeed(\'{id}\',1.25,this)">1.25x</button>'
    '</div></div>')


def expand_audio_players(slides):
    """<div class="audio-player" data-src="X"></div>  ->  player COMPLETO.

    IDEMPOTENTE: a saída não tem mais a classe .audio-player, então rodar duas vezes
    não duplica. Aula sem o shorthand = no-op byte-a-byte.
    """
    n = [0]

    def repl(m):
        attrs = m.group(1)
        src = re.search(r'data-src="([^"]+)"', attrs)
        assert src, f'<div class="audio-player"> sem data-src: {m.group(0)[:120]}'
        n[0] += 1
        pid = f'mp-a{n[0]}'
        style = re.search(r'\sstyle="([^"]*)"', attrs)
        st = f' style="{style.group(1)}"' if style else ' style="max-width:520px;margin:1.2rem auto 0"'
        q = re.search(r'\sdata-questions="([^"]*)"', attrs)
        qs = f' data-questions="{q.group(1)}"' if q else ''
        return _LP_TPL.format(id=pid, src=src.group(1), style=st, qs=qs)

    return re.sub(r'<div class="audio-player"([^>]*)>\s*</div>', repl, slides)


def inject_input_recap(slides):
    """O INPUT VOLTA PARA O DETALHE (feedback da chefe, 28/07/2026).

        *"Antes do slide 07, para a parte do detail/true or false, o texto deveria
        aparecer novamente."* (Lara)  ·  *"Slide 3 — atividade de True or False, mas
        falta ter o áudio novamente."* (Vitor)

    Leitura/escuta acontece em DUAS passadas com propósitos diferentes: a primeira busca
    a ideia (gist) e pode ser feita com o texto longe; a segunda cobra DETALHE — e aí o
    aluno precisa VOLTAR ao input para localizar a evidência. Sem o texto na tela, o
    true/false vira memória, que é exatamente o defeito que a REGRA 2.1/2.2 combate, só
    que um estágio adiante.

    O que injeta, antes do bloco de true/false:
      leitura -> uma cópia compacta do texto (.ic-reading-recap)
      áudio   -> o player de novo, com ID PRÓPRIO (mp-r*). Copiar o id do player
                 original faria getElementById devolver o primeiro, e o segundo player
                 ficaria morto — dois controles disputando o mesmo áudio.

    IDEMPOTENTE. Aula sem true/false depois de exposição = no-op.
    """
    partes = re.split(r'(?=<div class="slide )', slides)
    ultimo_texto, ultimo_audio, n = None, None, [0]
    out = []
    for ch in partes:
        est = _estrutura(ch)
        i = est.find('<div class="ic-reading">')
        if i >= 0:
            fim = _match_div_end(est, i)          # o bloco tem divs aninhados (rtitle/src):
            if fim > 0:                            # regex .*? cortaria no primeiro </div>
                ultimo_texto = est[i:fim]
        ma = re.search(r'data-src="([^"]+\.mp3)"', est)
        if ma and 'lp-play' in est:
            ultimo_audio = ma.group(1)
        if 'ic-tfrow' in est and 'ic-reading-recap' not in est and 'id="mp-r' not in est:
            recap = None
            if ultimo_texto:
                recap = ultimo_texto.replace('<div class="ic-reading">',
                                             '<div class="ic-reading ic-reading-recap">', 1)
            elif ultimo_audio:
                n[0] += 1
                recap = _LP_TPL.format(id=f'mp-r{n[0]}', src=ultimo_audio, qs='',
                                       style=' style="max-width:460px;margin:0 auto 1rem"')
            if recap:
                ch = ch.replace('<div class="ic-card"><div class="ic-tf">',
                                recap + '<div class="ic-card"><div class="ic-tf">', 1)
        out.append(ch)
    return ''.join(out)


def vocab_ensinado(slides):
    """As palavras que a aula ENSINA: o .card-word de cada reveal card de vocabulario."""
    return [_texto(w) for w in re.findall(r'class="card-word">(.*?)</div>', slides, re.S)]


def norm_vocab(w):
    """Forma canonica para comparar palavra ensinada x resposta de exercicio.

    Tira pontuacao, caixa e o 'to' do infinitivo: o card ensina "To settle down" e a
    lacuna pede "settle down" — e a MESMA palavra, e um exercicio nao pode ser acusado de
    cobrar vocabulario nao ensinado por causa de uma particula.
    """
    w = re.sub(r'[^a-z ]', ' ', (w or '').lower())
    w = ' '.join(w.split())
    return re.sub(r'^(to be|to|a|an|the) ', '', w).strip()


def inject_gap_banks(slides):
    """BANCO DE PALAVRAS no gap-fill de VOCABULARIO. IDEMPOTENTE.

    Feedback da chefe (29/07/2026): *"senti falta do banco de palavras tambem no exercicio
    do slide 9."*

    Sem o banco, "complete a frase" nao e recuperacao lexical — e adivinhacao com uma so
    tentativa: ou a palavra exata vem a cabeca, ou o exercicio nao tem saida e a aluna
    trava. Com o banco, ela LE as candidatas e decide qual cabe, que e a operacao que a
    gente quer treinar. O banco sai EMBARALHADO pelo builder (REGRA 24: em ordem, o
    exercicio vira copia de cima para baixo).

    SO no gap-fill de VOCABULARIO. O gap-fill de GRAMATICA ("I ___ (paint) the kitchen
    right now") cobra a FORMA do verbo, e o banco entregaria a resposta pronta — o verbo
    ali nao e o desafio, a conjugacao e. O criterio nao e um flag que alguem marca: e o
    proprio conteudo. Se TODA resposta do slide e uma palavra que a aula ensinou nos
    reveal cards, o exercicio e de vocabulario e ganha banco. Senao, nao ganha nada.

    O componente ja existe (.ic-bank .ic-b, do bloco B2 gapfill) — CSS no shell do modelo,
    nada novo a manter.
    """
    ensinado = {norm_vocab(w) for w in vocab_ensinado(slides)}
    if not ensinado:
        return slides
    partes = re.split(r'(?=<div class="slide )', slides)
    out = []
    for ch in partes:
        i = ch.find('<div class="fill-grid"')
        if i < 0 or 'ic-bank' in ch:
            out.append(ch)
            continue
        fim = _match_div_end(ch, i)
        if fim <= 0:
            out.append(ch)
            continue
        respostas = [_texto(a) for a in re.findall(r'class="fill-answer">(.*?)</span>', ch[i:fim], re.S)]
        if not respostas or not all(norm_vocab(r) in ensinado for r in respostas):
            out.append(ch)          # gap-fill de gramatica (ou vocab nao ensinado): sem banco
            continue
        ordem = respostas[1::2] + respostas[0::2]
        bank = ''.join(f'<span class="ic-b">{_esc(w)}</span>' for w in ordem)
        ch = ch[:fim] + f'\n    <div class="ic-bank ic-soft">{bank}</div>' + ch[fim:]
        out.append(ch)
    return ''.join(out)


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
                # ANCORA: a primeira frase do proprio input. Predicao sem evidencia e
                # adivinhacao — ver _predict_html().
                exp = _estrutura(ch)
                if kind == 'reading':
                    mtxt = re.search(r'<div class="ic-reading">.*?<p>(.*?)</p>', exp, re.S)
                else:
                    # A fala do diálogo vive num <div class="dialogue-bubble">, NUNCA num
                    # <p> — é assim no shell do modelo (helen-mendes) e em tudo que o
                    # builder emite. Procurando só por <p>, a âncora NUNCA casava e o
                    # slide ia ao ar dizendo "This is the first line." sem linha nenhuma
                    # acima: predição sem evidência, que é exatamente o que a chefe
                    # reprovou em 28/07/2026. O <p> fica primeiro por causa de material
                    # antigo que escreve a fala assim.
                    mtxt = (re.search(r'class="dialogue-line[^>]*>.*?<p[^>]*>(.*?)</p>', exp, re.S)
                            or re.search(r'class="dialogue-bubble[^"]*"[^>]*>(.*?)</div>', exp, re.S))
                ancora = _primeira_frase(mtxt.group(1)) if mtxt else None
                out.append(_slide_de_tarefa(kind, perguntas, phase, ancora))
        out.append(ch)
        i += 1
    novo = ''.join(out)
    # RENUMERA data-slide em ordem de documento (a inserção desloca todo mundo).
    cont = [0]

    def _n(m):
        cont[0] += 1
        return f'data-slide="{cont[0]}"'

    return re.sub(r'data-slide="\d+"', _n, novo)


# Ícone de áudio inline por fala do diálogo — MESMO markup do modelo (helen-mendes):
# .audio-inline + data-speak + speakText. O texto vive num ATRIBUTO (REGRA 7.1), então
# apóstrofo do inglês não quebra nada.
_DLG_AUDIO = ('<span class="audio-inline" data-speak="{t}" '
              'onclick="speakText(this.dataset.speak,this)">'
              '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
              '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
              '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span>')


def inject_dialogue_audio(slides):
    """Todo diálogo line-by-line DEVE poder ser OUVIDO (REGRA 7 + REGRA 2.2).

    O slide de tarefa diz "Listen for this" e o `data-teacher` manda "Toque cada audio" —
    mas a fala só tem áudio se a linha carregar um gatilho (data-speak). O modelo
    (helen-mendes) traz um ícone `.audio-inline` em CADA fala; conteúdo autoral (kids,
    Bento) saiu SEM — diálogo mudo, e o extract_phrases nem gerava o MP3 (sem data-speak
    não há frase a sintetizar). Resultado: "Listen for this" -> diálogo silencioso
    (reportado 23/07, Bento aula 1 e 2).

    Aqui o BUILDER injeta o ícone em toda `.dialogue-bubble` que ainda não tem áudio,
    derivando o texto falado da própria bolha (sem o rótulo do falante `<b>Nome:</b>` e
    sem tags). IDEMPOTENTE (pula bolha que já tem audio-inline/data-speak, então o modelo
    e o adulto passam intactos). Como o data-speak entra na MESMA linha física do
    data-voice do diálogo, o extract_phrases herda a voz certa e o MP3 nasce no manifest.
    """
    def repl(m):
        inner = m.group(1)
        if 'audio-inline' in inner or 'data-speak' in inner:
            return m.group(0)  # já tem áudio — não duplica (modelo/adulto intactos)
        spoken = _texto(re.sub(r'^\s*<b>[^<]*</b>', '', inner))  # tira "Nome:" e tags
        # _texto troca cada tag por espaço; quando uma tag inline é seguida de pontuação
        # ("...<span>green</span>.") isso vira "green ." — espaço solto antes do ponto.
        # Cola a pontuação de volta (senão a frase falada e a chave do audioMap ficam feias).
        spoken = re.sub(r'\s+([.,!?;:])', r'\1', spoken)
        # DESESCAPA ANTES DE REESCAPAR. A bolha vem do HTML AUTORAL, onde travessão e "&"
        # vivem como ENTIDADE (`&mdash;`, `&amp;`). Escapar direto transformava `&mdash;` em
        # `&amp;mdash;`; o extract_phrases desescapa UMA vez e entrega a STRING LITERAL
        # "&mdash;" pra ElevenLabs — a voz LÊ "ampersand m dash" no meio da fala, e a chave
        # do audioMap fica com o lixo dentro. O texto falado tem de ser o texto que o humano
        # LÊ na tela, não o que está ESCRITO no arquivo (mesmo princípio da REGRA 7.1).
        spoken = html_unescape(spoken)
        if not spoken:
            return m.group(0)
        esc = (spoken.replace('&', '&amp;').replace('<', '&lt;')
               .replace('>', '&gt;').replace('"', '&quot;'))  # apóstrofo fica literal (REGRA 7.1)
        return m.group(0)[:-len('</div>')] + ' ' + _DLG_AUDIO.format(t=esc) + '</div>'
    # `[^>]*` depois da classe: a bolha do conteúdo autoral costuma trazer style inline
    # (`class="dialogue-bubble x-bubble" style="...">`). Com a classe obrigatoriamente
    # colada no `>`, essas bolhas NUNCA casavam e o diálogo nascia MUDO sem ninguém ver —
    # o gate só acusa depois, e o autor acaba escrevendo o ícone na mão (aulas 17/18 da
    # Izabel). Idempotente: a bolha que já tem audio-inline/data-speak segue intocada.
    return re.sub(r'<div class="dialogue-bubble[^"]*"[^>]*>(.*?)</div>', repl, slides, flags=re.S)


def audio_da_call(cfg):
    """Entradas de audio dos blocos kind=call. UMA FONTE: o mesmo bloco que vira markup
    gera o manifesto, entao o arquivo que o player pede e o arquivo que o gen_audio grava.
    Declarar nos dois lugares seria convite a divergir — e divergencia aqui e audio mudo."""
    out = []
    blocos = ((cfg.get('lesson') or {}).get('inclass_blocks') or {})
    for lista in blocos.values():
        for b in lista:
            if b.get('kind') != 'call':
                continue
            cast = b['cast']
            for i, (falante, texto) in enumerate(b['turnos']):
                assert 0 <= falante < len(cast), (
                    f'call: turno {i + 1} aponta para o falante {falante}, e o cast tem '
                    f'{len(cast)}')
                out.append(dict(text=texto, voice=cast[falante]['voz'],
                                file=f'{b["prefixo"]}{i + 1:02d}.mp3'))
    vistos = set()
    for e in out:
        assert e['file'] not in vistos, f'call: dois turnos gravariam {e["file"]}'
        vistos.add(e['file'])
    return out


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
        # [a-z0-9_]+ e NAO [a-z]+: chave de voz de sotaque tem underscore (dutch_m,
        # nordic_m). Com [a-z]+ o hint NAO casava, a fala caia na alternancia
        # arthur/ellen e o MP3 do personagem estrangeiro nascia com voz americana —
        # o data-voice dizia uma coisa e o audio era outra.
        mv = re.search(r'data-voice="([a-z0-9_]+)"', line)
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
    # O BADGE SE TROCA PELA ESTRUTURA, NAO PELO TEXTO DO MOLDE. A linha acima casa o
    # texto do shell STANDALONE ("Business English -- 30 Aulas") e por isso nunca casou
    # o do HUB, que diz outra coisa ("Travel English -- 48 Aulas"): todo hub gerado com
    # hub:"new" saiu com o programa e o numero de aulas de OUTRA aluna no cabecalho.
    # Ancorar na classe resolve os dois de uma vez e nao depende de qual frase o molde
    # tem hoje. Idempotente: reescreve o conteudo do badge, seja ele qual for.
    s = re.sub(r'(<div class="passport-badge">)[^<]*',
               lambda m: f'{m.group(1)}{cfg["program"]} -- {cfg["total_aulas"]} Aulas', s)
    # PROVENIÊNCIA (rastreio modelo × nível — CONTRATOS-E-RASTREIO.md §3): toda aula nasce
    # declarando de qual MOLDE e NÍVEL herdou. É o que torna o retrofit ESCOPADO possível e
    # seguro num mundo com >1 modelo (um conserto no Modelo Kids nunca toca uma aula do
    # Adulto) e deixa o catálogo saber quem herdou o quê. Default 'adulto' → configs antigos
    # (sem a chave) seguem corretos. Nível vem do config OU do 1º item do header (CEFR).
    # Idempotente: só injeta se ainda não houver a etiqueta.
    if 'name="alumni-model"' not in s:
        prov_model = cfg.get('model', 'adulto')
        prov_level = cfg.get('level') or (cfg['header'][0] if cfg.get('header') else '')
        prov = f'<meta name="alumni-model" content="{prov_model}">'
        if prov_level:
            prov += f'\n    <meta name="alumni-level" content="{prov_level}">'
        # FRAMEWORK (o MÉTODO, dentro da categoria). É esta etiqueta que o GATE 11
        # (scripts/check_framework_isolation.py) lê pra garantir que aluno real nunca
        # receba framework em validação. Aula sem a etiqueta = legado, e o gate ignora.
        fw_id = cfg.get('framework', FRAMEWORK_DEFAULT)
        prov += f'\n    <meta name="alumni-framework" content="{fw_id}">'
        # CONTRATO (GATE 12): a versão do contrato em que esta aula NASCEU. É o que
        # permite editar o contrato no catálogo sem reprovar aula antiga — o gate
        # julga cada aula pela versão dela, não pela versão de hoje. Framework sem
        # contrato não carimba nada, e o gate simplesmente ignora a aula.
        v = contrato_versao(fw_id)
        if v:
            prov += f'\n    <meta name="alumni-contrato" content="{fw_id}@{v}">'
        s = re.sub(r'(<meta name="viewport"[^>]*>)',
                   lambda m: m.group(1) + '\n    ' + prov, s, count=1)
    # CARIMBO DE GERAÇÃO — a data de nascimento da aula, em versões do builder.
    #
    # Sem ele, toda invariante NOVA nasce cobrando o PASSADO. Foi o que aconteceu ao criar
    # o gate da pergunta de predição: a etiqueta de framework existe desde 27/07 e já está
    # em ~8 aulas PUBLICADAS de alunos reais, que passaram a ser acusadas por não terem uma
    # coisa que não existia quando foram geradas. Isso é exatamente o que a REGRA 30 proíbe
    # — subir a baseline de legado sem melhorar aula nenhuma.
    #
    # O carimbo separa "geração nova" de "já publicada" por FATO, não por proxy. Gate de
    # regra nova roda só em quem tem GEN >= a versão em que a regra entrou; o resto passa
    # intocado, para sempre. SOBE quando uma invariante nova entra no builder — nunca por
    # mudança cosmética (senão volta a ser um proxy de data).
    if 'name="alumni-gen"' not in s:
        s = re.sub(r'(<meta name="alumni-framework"[^>]*>)',
                   lambda m: m.group(1) + f'\n    <meta name="alumni-gen" content="{BUILDER_GEN}">', s, count=1)
    # PELE DO MODELO (CONTRATOS-E-RASTREIO.md §1): quando o modelo tem pele própria
    # (kids, teens, ...), injeta o reskin (forma/fonte/tamanho/tom) antes de </style>. A COR
    # vem da paleta do aluno; os OSSOS e classes-mecanismo continuam os do adulto — então os
    # 12 Contratos passam de graça e um conserto de estrutura no shell vale pra TODOS os
    # modelos. O canal é por CONVENÇÃO DE ARQUIVO: `{model}-theme.css` existe => é injetado;
    # não existe (adulto) => nada acontece. Modelo novo não precisa tocar no builder.
    # Idempotente.
    model = cfg.get('model', 'adulto')
    theme_css = os.path.join(os.path.dirname(__file__), f'{model}-theme.css')
    if os.path.exists(theme_css) and f'PELE {model.upper()} (injetada' not in s:
        theme = read(theme_css)
        s = s.replace('</style>',
                      f'\n/* PELE {model.upper()} (injetada pelo builder — model={model}) */\n{theme}\n</style>', 1)
    # JS DO MODELO: canal analogo ao css (mini-games — dino-tap no kids, word arena no
    # teens). SO quando o modelo tem o arquivo => adulto intocado. Vai antes de </body>
    # (depois do script principal do shell, que ja definiu speakText/updateProgress que os
    # engines usam). Idempotente.
    theme_js = os.path.join(os.path.dirname(__file__), f'{model}-theme.js')
    if os.path.exists(theme_js) and f'{model}-theme.js (injetada' not in s and '</body>' in s:
        mjs = read(theme_js)
        s = s.replace('</body>',
                      f'<script>\n/* {model}-theme.js (injetada pelo builder — model={model}) */\n{mjs}\n</script>\n</body>', 1)
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
    # O rótulo do slide de descoberta NÃO é sempre "Grammar Discovery": uma aula de
    # pronúncia/prosódia descobre um SISTEMA que não é gramática, e forçá-la a se rotular
    # "Grammar Discovery" na tela seria mentir para a aluna só para agradar ao gate.
    # Aceita-se também o rótulo curto "Discovery" — o marcador continua sendo emitido pelo
    # BUILDER, um por aula, e só quando lesson.grammar_point existe (opt-in explícito).
    idx = -1
    for marker in ('chapter-label">Grammar Discovery', 'chapter-label">Discovery'):
        idx = slides.find(marker)
        if idx != -1:
            break
    if idx == -1:
        return slides  # aula sem slide de descoberta — no-op silencioso
    start = slides.rfind('<div class="slide', 0, idx)
    if start == -1:
        return slides
    tag_end = _opening_tag_end(slides, start)
    if tag_end == -1:
        return slides
    if 'data-grammar=' in slides[start:tag_end]:
        return slides  # idempotente
    return slides[:tag_end] + f' data-grammar="{_attr_escape(g)}"' + slides[tag_end:]


def inject_kids_images(s):
    """MODELO KIDS — ilustração real no vocab card. Troca o ícone SVG do `card-icon` pela
    imagem da BIBLIOTECA COMPARTILHADA public/assets/kids/{word}.{jpg|png}: foto (.jpg) para
    concretos, cartoon (.png) para abstratos. Chaveada por PALAVRA → reaproveitada entre TODOS
    os alunos kids: 'dinosaur' usa sempre dinosaur.jpg, em qualquer aula. Palavra sem imagem na
    biblioteca MANTÉM o SVG (fallback seguro). O autor do conteúdo não wire imagem — o builder
    emite (mesma filosofia das task-slides). Idempotente. Ver memória kids-image-library."""
    assets = os.path.join(ROOT, 'public', 'assets', 'kids')

    def find_img(word):
        for ext in ('jpg', 'jpeg', 'webp', 'png'):
            if os.path.exists(os.path.join(assets, f'{word}.{ext}')):
                return f'{word}.{ext}', ('photo' if ext != 'png' else 'cartoon')
        return None, None

    def repl(m):
        word = m.group(2).strip().lower()
        img, typ = find_img(word)
        if not img:
            return m.group(0)
        return (f'<div class="card-icon voc-icon"><img src="/assets/kids/{img}" alt="{word}" '
                f'class="voc-img {typ}"></div>' + m.group(1))

    return re.sub(
        r'<div class="card-icon"[^>]*>.*?<div class="card-hint">[^<]*</div></div>'
        r'(\s*<div class="card-body"><div class="card-word">([^<]+)</div>)',
        repl, s, flags=re.S)


# Palavras "tappable": concretas, com imagem NITIDA e nao-ambigua na lib kids. Adjetivo
# relacional (big/small) e cor (green) NAO entram — no game "toque a figura" a imagem
# vira ambigua (big.png e small.png sao quase iguais). Ver [[kids-image-library]].
TAPPABLE_KIDS = {'dinosaur', 'tree', 'rocket', 'star', 'moon', 'planet', 'cat', 'dog', 'run',
                 # objetos concretos INTEIROS, nitidos como silhueta no jogo de tocar.
                 # NAO entram: parte de corpo (wings/claws/tail/scales), lugar (cave),
                 # abstracao (shift/heavy) e acao com pessoa (lift/ride/carry) — no
                 # 'toque a figura' elas viram adivinhacao. Ver assets/kids/README.md.
                 'brick', 'wheel', 'tower', 'bridge', 'street', 'piece', 'battery', 'fix',
                 # acao cuja FIGURA e o proprio referente (fogo, alguem montando).
                 # 'wings'/'claws' ficam de fora de proposito: a figura (borboleta,
                 # caranguejo) ensina o bicho, nao a parte -- no reveal card a
                 # definicao corrige, no jogo de tocar nao ha definicao nenhuma.
                 'breathe fire', 'ride'}


def inject_kids_game(preclass, cfg):
    """MODELO KIDS — injeta o mini-game 'Dino Tap' (Listen and tap) como card de pratica no
    Pre-class de cada aula (REGRA 4 etapa 2). Deck = palavras DA AULA que sao TAPPABLE. O
    widget e .think-card (conta no updateProgress do shell) + .dino-tap-game (engine em
    kids-theme.js). Idempotente. So model==kids. Aula sem palavra tappable => sem game."""
    if cfg.get('model') != 'kids':
        return preclass
    assets = os.path.join(ROOT, 'public', 'assets', 'kids')

    def has_img(w):
        return any(os.path.exists(os.path.join(assets, f'{w}.{ext}'))
                   for ext in ('png', 'jpg', 'jpeg', 'webp'))

    def repl(m):
        block, lid = m.group(0), m.group(1)
        if 'dino-tap-game' in block:
            return block  # idempotente
        deck = []
        for w in re.findall(r'class="vocab-card-word">([^<]+)<', block):
            lw = w.strip().lower()
            if lw in TAPPABLE_KIDS and has_img(lw) and lw not in deck:
                deck.append(lw)
        if not deck or '<div class="survival-card">' not in block:
            return block
        game = (f'<div class="think-card dino-tap-game" data-key="{cfg["slug"]}-{lid}" '
                f"data-deck='{json.dumps(deck)}'></div>\n")
        return block.replace('<div class="survival-card">', game + '<div class="survival-card">', 1)

    return re.sub(
        r'<div class="lesson-card" id="ex-lesson-(\d+)">.*?(?=<div class="lesson-card" id="ex-lesson-|\Z)',
        repl, preclass, flags=re.S)


# ── MECANICA x KIND: o vocabulario do banco (03 §4) sobre os kinds do builder ────────────
#
# O documento fala em MECANICA ("Matching", "Sorting", "Role-play/simulation"); o config
# fala em KIND ("matching", "sorting", "scenarios"). Sem esta tabela as duas linguas nao se
# encontram, e "registrar mecanica, funcao, operacao, controle e evidencia" (03 §4.2) fica
# sendo prosa que ninguem consegue conferir.
#
# So entra aqui o kind que E exercicio. Os que sao INPUT ou APOIO (o texto, o cenario, o
# banco de frases, o gabarito, o fechamento) nao sao mecanica e nao viram divida de
# repeticao — declarar o contrario encheria o registro de ruido e escondaria a repeticao
# real. Ficam em KIND_APOIO, explicitos, para ninguem achar que foram esquecidos.
MECANICA_POR_KIND = {
    'matching': 'Matching',
    'gist': 'Multiple choice',
    'tf': 'True/False + correction',
    'sorting': 'Sorting',
    'gapfill': 'Fill in the blanks',
    'rephrase': 'Rephrasing',
    'quickfire': 'Replicas rapidas',
    'call': 'Escuta por segmentos',
    'reveal': 'Noticing por revelacao',
    'questions': 'Perguntas abertas dirigidas',
    'qsub': 'Perguntas abertas dirigidas',
    'analyse': 'Perguntas abertas dirigidas',
    'timer': 'Fala cronometrada',
    'write': 'Quadro de feedback',
}
KIND_APOIO = ('scenarios', 'reading', 'evidence', 'phrases', 'lf', 'bank', 'modals',
              'vocabnote', 'followup', 'answer', 'recap', 'selfassess', 'whiteboard',
              'guiding')


def kinds_da_aula(cfg):
    """Todo `kind` que a aula de fato usa, na ordem em que aparece no config."""
    ks = []

    def walk(o):
        if isinstance(o, dict):
            if 'kind' in o:
                ks.append(o['kind'])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(cfg['lesson'].get('inclass_blocks', {}))
    return ks


def registra_mecanicas_gastas(cfg):
    """Escreve em _build/{slug}/estado.json o que ESTA AULA gastou de mecanica.

    POR QUE: o docx §5 exige um estado pedagogico acumulativo e diz por que — "o gerador
    nao deve depender de memoria narrativa presumida". O campo `mecanicas_gastas` existia
    no esquema desde 07/08/2026 e ficou VAZIO enquanto as quatro aulas do bloco 1 eram
    geradas: nada escrevia nele. Sem isso, o lote seguinte e gerado sem saber o que ja foi
    usado, e a regra "nao repetir a mesma combinacao dentro do bloco" (03 §4.2) vira
    memoria de quem gera.

    MEDE o que a aula tem (os kinds do config) e CRUZA com o que o syllabus declarou para
    aquela aula. O que foi medido e nao foi declarado entra com `sem_declaracao: true` —
    visivel, e o GATE 24 cobra. O contrario (declarado e nao usado) tambem: `nao_usada`.

    Idempotente: reescreve as entradas desta aula, preserva as das outras.
    """
    est_p = os.path.join(ROOT, '_build', cfg['slug'], 'estado.json')
    if not os.path.exists(est_p):
        return
    syl_p = syllabus_json_path(cfg)
    if not os.path.exists(syl_p):
        return
    n = cfg['lesson']['n']
    with open(est_p, encoding='utf-8') as fh:
        estado = json.load(fh)
    with open(syl_p, encoding='utf-8') as fh:
        syl = json.load(fh)
    # A comparacao normaliza acento: o syllabus e material de leitura ("Replicas rapidas"
    # aparece acentuado la) e a tabela deste arquivo e ASCII, como o resto do builder.
    # Comparar as duas cruas produziria divergencia inventada — dois nomes da MESMA coisa.
    def _norm(t):
        return unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()

    decl, decl_nome = {}, {}
    for a in syl.get('aulas', []):
        if a.get('n') == n:
            for m in a.get('mecanicas', []):
                decl[_norm(m['mecanica'])] = m
                decl_nome[_norm(m['mecanica'])] = m['mecanica']
            break

    medidas = {}
    for k in kinds_da_aula(cfg):
        mec = MECANICA_POR_KIND.get(k)
        if mec:
            medidas.setdefault(mec, []).append(k)

    novas = []
    for mec, kinds in medidas.items():
        d = decl.get(_norm(mec))
        e = dict(aula=n, mecanica=decl_nome.get(_norm(mec), mec), kinds=sorted(set(kinds)))
        if d:
            e.update(funcao=d['funcao'], operacao=d['operacao'], controle=d['controle'],
                     evidencia=d['evidencia'])
        else:
            e['sem_declaracao'] = True
        novas.append(e)
    medidas_norm = {_norm(m) for m in medidas}
    for chave, d in decl.items():
        if chave in medidas_norm:
            continue
        # `sem_widget` = mecanica que acontece na CONDUCAO, nao num componente de tela
        # (role-play, retask, decisao de caso). Nao ter kind e propriedade dela, nao
        # esquecimento — e cobrar kind aqui seria pedir widget para o que e conversa.
        novas.append(dict(aula=n, mecanica=d['mecanica'], kinds=[],
                          nao_usada=not d.get('sem_widget'),
                          sem_widget=bool(d.get('sem_widget')),
                          funcao=d['funcao'], operacao=d['operacao'],
                          controle=d['controle'], evidencia=d['evidencia']))

    outras = [m for m in estado.get('mecanicas_gastas', []) if m.get('aula') != n]
    estado['mecanicas_gastas'] = sorted(outras + novas,
                                        key=lambda m: (m['aula'], m['mecanica']))
    with open(est_p, 'w', encoding='utf-8') as fh:
        json.dump(estado, fh, ensure_ascii=False, indent=2)
        fh.write('\n')
    sd = sum(1 for m in novas if m.get('sem_declaracao'))
    nu = sum(1 for m in novas if m.get('nao_usada'))
    print(f'  estado.json: aula {n} gastou {len(medidas)} mecanica(s)'
          + (f' — {sd} sem declaracao no syllabus' if sd else '')
          + (f', {nu} declarada(s) e nao usada(s)' if nu else ''))


def build_standalone(cfg, content_dir, manifest):
    L = cfg['lesson']
    n = L['n']
    audio_base = f'/audio/{cfg["slug"]}/'
    slides = read(os.path.join(content_dir, 'slides.html'))
    slides = expand_inclass_blocks(slides, cfg)  # B2 blocks (no-op se a aula não usar)
    # O player de listening COMPLETO (REGRA 2.1). O shorthand .audio-player era um div
    # vazio: MP3 gerado, e nada na tela para tocar. Aula sem shorthand = no-op.
    slides = expand_audio_players(slides)
    # A pergunta de PREDIÇÃO antes do áudio (o slide de tarefa ganha a dele em
    # _slide_de_tarefa). Idempotente; aula sem listening = no-op.
    slides = inject_predict_prompts(slides, cfg)
    # O INPUT VOLTA para a etapa de DETALHE: leitura de detalhe se faz COM o texto na
    # frente; sem ele o true/false vira memória. Idempotente; sem true/false = no-op.
    slides = inject_input_recap(slides)
    # BANCO DE PALAVRAS no gap-fill de VOCABULÁRIO (nunca no de gramática, que cobra a
    # forma do verbo). Idempotente; aula sem .fill-grid de vocab = no-op.
    slides = inject_gap_banks(slides)
    # A TAREFA VEM ANTES DA EXPOSIÇÃO (REGRA 2.2): emite o slide de perguntas antes de
    # todo diálogo/leitura, a partir das perguntas do slide de checagem. Idempotente e
    # renumera os data-slide. Aula sem diálogo nem leitura = no-op.
    slides = inject_task_slides(slides)
    # REGRA 7 + 2.2: toda fala do diálogo ganha botão de áudio (senão "Listen for this"
    # leva a um diálogo mudo). Idempotente — modelo/adulto (que já têm audio-inline) passam.
    slides = inject_dialogue_audio(slides)
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
    # O slide "Common Mistake" (erro em vermelho vs correcao em verde) saiu do material
    # por decisao do coordenador (04/08/2026). O polimento cosmetico dele vivia aqui e foi
    # removido junto. Se o slide reaparecer num config, o GATE do validate_lesson barra.

    s = read(shell_path(cfg))
    s = base_swaps(s, cfg, n=n)
    s = re.sub(r'<title>[^<]*</title>', f'<title>{L["title_tag"]}</title>', s, count=1)
    s = re.sub(r'<h1>[^<]*</h1>', f'<h1>{cfg["student_name"]}</h1>', s, count=1)
    s = patch_header(s, cfg, L['subtitle'])

    # ── A ESPINHA DA AULA: barra de etapas + rotulos com o orcamento de minutos ──────
    #
    # A unidade que o professor enxerga e a ETAPA, nao a tela: 7 ou 8 etapas, cada uma com
    # 1 a 6 telas dentro, e ele percorre tudo ou so parte. E o que o artefato de referencia
    # faz (stage-bar + stage-labels + data-stage por tela) e o que a anatomia
    # guided-discovery declara em _build/model/anatomias.json -> estrutura.
    #
    # POR QUE AQUI A PECA SE CHAMA phase-*, e nao stage-*: e a MESMA mecanica que o shell
    # ja tinha — updatePhaseBar() pinta completed/current/upcoming a partir do data-phase
    # da tela, exatamente como o paint() do artefato faz com data-stage. Clonar uma segunda
    # barra com outro nome seria manter duas coisas iguais em dois lugares, que e o defeito
    # que o GATE 18 existe para impedir.
    #
    # POR QUE NAO HA STAGE_SETS AQUI: no artefato, tres aulas moram no MESMO arquivo, entao
    # a barra precisa ser remontada em runtime (deckInit troca STAGES por aula). Aqui cada
    # aula e um arquivo standalone proprio, entao a barra daquela aula ja sai pronta do
    # builder. Portar o mapa seria portar maquinario morto.
    #
    # DOIS DEFEITOS CORRIGIDOS AQUI (11/08/2026):
    #  1. os SEGMENTOS vinham fixos do shell (7, da narrativa do imersivo) e nunca eram
    #     re-emitidos. As quatro aulas da stephanie tem 8 etapas => a etapa 8 nunca acendia
    #     em nenhuma delas. Agora o numero de segmentos vem das etapas declaradas.
    #  2. faltava o ORCAMENTO DE MINUTOS no rotulo. E o minuto por etapa que da sentido a
    #     frase "o numero de telas deriva do orcamento de minutos" (anatomias.json): agora
    #     ela tem de onde derivar.
    stages = lesson_stages(cfg)
    etapas_contrato = len(framework_contrato_etapas(cfg))
    if etapas_contrato and len(stages) != etapas_contrato:
        # AVISO, nao assert. Medido no artefato: a aula de ESP condensa as 8 funcoes do
        # normativo em 7 etapas de tela, e a de Reading mantem 8. Transformar isso em erro
        # proibiria uma aula que a propria referencia contem.
        print(f'  aviso: a aula declara {len(stages)} etapas e o contrato do framework '
              f'"{cfg.get("framework", FRAMEWORK_DEFAULT)}" tem {etapas_contrato}. '
              f'E permitido (o artefato condensa funcoes em etapas de tela), mas confira '
              f'se foi intencional.', file=sys.stderr)
    soma = sum(m for _, m in stages if m)
    if soma:
        alvo = framework_percurso_min(cfg)
        assert not alvo or soma == alvo, (
            f'o orcamento das etapas soma {soma} min e o contrato do framework '
            f'"{cfg.get("framework", FRAMEWORK_DEFAULT)}" declara percurso_min={alvo}. '
            f'A barra mostraria um percurso que o contrato nao reconhece — iguale os dois.')

    # ATENCAO ao fecho: o marcador de fim NAO pode ser '</div>', porque o primeiro '</div>'
    # depois do <div class="phase-bar"> e o do PROPRIO primeiro segmento — replace_between
    # pararia ali e deixaria os segmentos antigos do shell para tras (foi o que aconteceu na
    # primeira versao deste bloco: 8 segmentos novos + 6 sobras). Os rotulos nao tinham o
    # problema por serem <span>. Ancoramos no <div> seguinte, e o </div> do fecho vai junto.
    segs = '\n' + '\n'.join(
        f'  <div class="phase-segment{" current" if i == 0 else " upcoming"}" '
        f'data-phase="{i+1}"></div>'
        for i in range(len(stages))) + '\n</div>\n'
    s = replace_between(s, '<div class="phase-bar" id="phaseBar">',
                        '<div class="phase-labels"', segs)

    def _rotulo(i, nome, m):
        nome_attr = nome.replace('&', '&amp;').replace('"', '&quot;')
        nome_txt = nome.replace('&', '&amp;')
        attr = f' data-name="{nome_attr}"' + (f' data-min="{m}"' if m else '')
        texto = f'{nome_txt}<br>{m}&#8242;' if m else nome_txt
        cur = ' current' if i == 0 else ''
        return f'  <span class="phase-label{cur}" data-phase="{i+1}"{attr}>{texto}</span>'

    labels = '\n' + '\n'.join(
        _rotulo(i, nome, m) for i, (nome, m) in enumerate(stages)) + '\n'
    s = replace_between(s, '<div class="phase-labels" id="phaseLabels">', '</div>', labels)

    # ── O MAPA TELA -> ETAPA ────────────────────────────────────────────────────────
    # updatePhaseBar() pinta a barra a partir de slidePhases[telaAtual]. Esse mapa vinha
    # FIXO do shell — as 27 telas / 7 capitulos da aula do MODELO — e o builder nunca o
    # regenerava. Ou seja: numa aula de 16 telas e 8 etapas, a barra acendia a etapa que o
    # mapa da OUTRA aula mandava, e as telas 17+ nao existiam no mapa (undefined => nenhum
    # segmento current). O data-phase correto ja estava em cada tela desde sempre; ninguem
    # o lia. Achado em 11/08/2026 pelo GATE 20, ao passar a cobrar a estrutura.
    #
    # So emite quando TODA tela declara a sua etapa: mapa com buraco e pior que mapa velho.
    pares = re.findall(r'data-slide="(\d+)"[^>]*data-phase="(\d+)"', slides)
    n_telas = len(re.findall(r'data-slide=', slides))
    if len(pares) == n_telas and n_telas:
        mapa = ','.join(f'{a}:{b}' for a, b in pares)
        s = re.sub(r'var slidePhases = \{[^}]*\};',
                   lambda _: 'var slidePhases = {' + mapa + '};', s, count=1)
    else:
        print(f'  aviso: {len(pares)}/{n_telas} telas com data-phase — slidePhases NAO '
              f'regenerado (a barra de etapas usa o mapa do shell).', file=sys.stderr)

    s = replace_between(s, '<div class="tab-content active" id="tab-inclass">', FIM_DO_INCLASS,
                        inclass_menu([menu_card(cfg, 'enterSlideMode')]))
    s = replace_between(s, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->',
                        '\n' + slides + '\n')
    if cfg.get('model') == 'kids':
        s = inject_kids_images(s)
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
    for item in audio_da_call(cfg):
        assert item['voice'] in VOICES, f'call com voz desconhecida: {item["voice"]}'
        manifest.append(item)

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
    # ESTADO ACUMULATIVO (docx §5): a aula escreve o que gastou. No-op para quem nao tem
    # _build/{slug}/estado.json + syllabus.json — nenhum aluno existente e afetado.
    registra_mecanicas_gastas(cfg)
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


def syllabus_json_path(cfg):
    """_build/{slug}/syllabus.json — a fonte de dados do syllabus do ciclo (docx §3.1)."""
    return os.path.join(ROOT, '_build', cfg['slug'], 'syllabus.json')


# ESTILO INLINE, e nao classes novas no shell: as abas de hub (planning/evidencias) ja sao
# escritas assim, e classe nova no shell mexeria no que o GATE 18 (drift) e o GATE 21
# (paridade com o artefato) vigiam. O conteudo da aba nao e anatomia — e material do professor.
_SYL_ROT = ('display:block;font-size:.72rem;font-weight:700;letter-spacing:.6px;'
            'text-transform:uppercase;color:var(--accent);margin-bottom:.25rem')
_SYL_VAL = 'display:block;font-size:.87rem;line-height:1.6;color:var(--text-mid)'
_SYL_SUB = 'font-size:.8rem;color:var(--text-dim)'


def _syl_campo(rot, val):
    return (f'<div style="margin-bottom:.85rem">'
            f'<span style="{_SYL_ROT}">{rot}</span>'
            f'<span style="{_SYL_VAL}">{val}</span></div>')


def syllabus_tab_html(cfg):
    """A aba 'Syllabus 20 aulas' do hub, montada a partir de _build/{slug}/syllabus.json.

    POR QUE O BUILDER EMITE ISTO, e nao um syllabus.html escrito a mao: o docx §3.1 exige DEZ
    campos de CADA aula do ciclo. Escrito a mao, isso e uma tabela de 20 linhas x 10 colunas
    que ninguem mantem — e o resultado medido em 11/08/2026 foi a aba mostrar UMA frase de
    esqueleto ("Syllabus do ciclo.") e nenhuma aula, enquanto as 20 viviam num .md que a
    interface nao abre. Emitido do JSON, o campo ou existe (e aparece) ou falta (e o GATE 22
    barra). Mesma logica dos slides de tarefa: se o builder emite, o defeito nao tem por onde
    entrar.

    Retorna None quando o aluno nao tem syllabus.json — a aba entao segue o caminho antigo
    (syllabus.html escrito a mao), e nenhum aluno existente muda de comportamento.
    """
    p = syllabus_json_path(cfg)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        d = json.load(f)
    FW = {'reading-into-speaking': 'Reading', 'listening-into-interaction': 'Listening',
          'grammar-for-communication': 'Grammar', 'esp-real-world': 'ESP'}
    out = []
    out.append('<div class="teacher-section">')
    out.append('<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.35rem;'
               'margin-bottom:.5rem">Syllabus do ciclo &mdash; %d aulas</h3>'
               % d['aulas_do_ciclo'])
    out.append('<p style="font-size:.87rem;line-height:1.6;color:var(--text-mid);'
               'margin-bottom:.7rem">Ciclo %s &middot; n&iacute;vel <strong>%s</strong> &middot; '
               '5 blocos &middot; 60 min nominais (55 de percurso + 5 de margem). '
               '<strong>Provis&oacute;rio at&eacute; o checkpoint da aula 4</strong>: o perfil inicial &eacute; uma '
               'hip&oacute;tese, e o que sair das aulas 1&ndash;4 confirma, ajusta ou reconfigura as '
               'aulas 5&ndash;20.</p>' % (d['ciclo'], d['nivel']))
    out.append('<p style="font-size:.82rem;line-height:1.6;color:var(--text-dim);'
               'margin-bottom:.9rem;padding:.7rem;border-left:3px solid var(--accent);'
               'background:var(--accent-dim)">O horizonte pedag&oacute;gico &eacute; sempre de 20 aulas. '
               'O pacote contratado determina quantas podem ser produzidas &mdash; n&atilde;o redefine '
               'a l&oacute;gica curricular. Se o pacote terminar antes da aula 20, emitir relat&oacute;rio '
               'parcial e preservar o estado. Fonte: <code>_build/model/ciclo.json</code>.</p>')
    out.append('<div class="tbl-wrap"><table class="data"><thead><tr>'
               '<th>#</th><th>Bloco</th><th>Framework</th><th>Aula</th>'
               '<th>Produto / evid&ecirc;ncia</th><th>Estado</th></tr></thead><tbody>')
    for a in d['aulas']:
        est = ('<strong>produzida</strong>' if a['estado'] == 'produzida'
               else 'provis&oacute;ria')
        out.append('<tr><td>%02d</td><td>%s</td><td>%s</td><td><strong>%s</strong></td>'
                   '<td>%s</td><td>%s</td></tr>'
                   % (a['n'], a['bloco'], FW.get(a['framework'], a['framework']),
                      a['titulo'], a['produto'], est))
    out.append('</tbody></table></div>')
    out.append('<p style="font-size:.8rem;color:var(--text-dim);margin-top:.6rem">'
               'Cada aula abaixo traz os <strong>dez campos</strong> que o normativo de '
               'planejamento exige (&sect;3.1) e a <strong>ficha de especifica&ccedil;&atilde;o</strong> do '
               'prompt controlador. Clique para abrir.</p>')
    out.append('</div>')

    for a in d['aulas']:
        out.append('<details style="border:1px solid var(--border);border-radius:10px;padding:.7rem .9rem;margin-bottom:.6rem;background:var(--bg-card)"><summary style="cursor:pointer;font-size:.9rem;color:var(--text)"><strong>%02d</strong> &middot; %s '
                   '&middot; <em>%s</em>%s</summary>'
                   % (a['n'], FW.get(a['framework'], a['framework']), a['titulo'],
                      '' if a['estado'] == 'produzida' else ' &middot; provis&oacute;ria'))
        out.append('<div style="margin-top:.8rem;padding-top:.8rem;border-top:1px solid var(--border)">')
        out.append(_syl_campo('1 &middot; Posi&ccedil;&atilde;o',
                              '%s &middot; %s &middot; %s' % (a['bloco'],
                                                              FW.get(a['framework'], a['framework']),
                                                              a['posicao_na_rotacao'])))
        out.append(_syl_campo('2 &middot; Objetivo comunicativo',
                              ('%s <br><span style="' + _SYL_SUB + '">Relacao com o perfil: '
                               '%s</span>')
                              % (a['objetivo_comunicativo'], a['relacao_com_o_perfil'])))
        out.append(_syl_campo('3 &middot; Opera&ccedil;&atilde;o NOVA', a['operacao_nova']))
        out.append(_syl_campo('4 &middot; Input e autenticidade',
                              ('%s <br><span style="' + _SYL_SUB + '">%s</span>')
                              % (a['input']['material'], a['input']['autenticidade'])))
        out.append(_syl_campo('5 &middot; Functional language', a['linguagem']))
        mic = a['microciclo']
        out.append(_syl_campo('6 &middot; Microciclo de Guided Discovery',
                              '<ol style="margin:.3rem 0 0 1.1rem;padding:0">' + ''.join(
                                  '<li><strong>%s.</strong> %s</li>'
                                  % (rot, mic[chave]) for rot, chave in (
                                      ('Evid&ecirc;ncia inicial', 'evidencia_inicial'),
                                      ('Opera&ccedil;&atilde;o cognitiva', 'operacao_cognitiva'),
                                      ('Formula&ccedil;&atilde;o de hip&oacute;tese', 'formulacao_hipotese'),
                                      ('Verifica&ccedil;&atilde;o pr&aacute;tica', 'verificacao_pratica'),
                                      ('Clarifica&ccedil;&atilde;o did&aacute;tica', 'clarificacao_didatica'),
                                      ('Aplica&ccedil;&atilde;o real', 'aplicacao_real'))) + '</ol>'))
        out.append(_syl_campo('7 &middot; Produto e crit&eacute;rios de sucesso',
                              '%s<ul style="margin:.3rem 0 0 1.1rem;padding:0">%s</ul>'
                              % (a['produto'], ''.join('<li>%s</li>' % c
                                                       for c in a['criterios_de_sucesso']))))
        out.append(_syl_campo('8 &middot; Evid&ecirc;ncia a registrar',
                              '<ul style="margin:.3rem 0 0 1.1rem;padding:0">%s</ul>'
                              % ''.join('<li>%s</li>' % e for e in a['evidencia_a_registrar'])))
        linhas = ''.join(
            '<tr><td><strong>%s</strong>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
            % (m['mecanica'],
               '' if m.get('no_banco', True) else ' <span style="font-size:.72rem;color:var(--warn);font-weight:600">fora do banco</span>',
               m['funcao'], m['operacao'], m['controle'], m['evidencia'])
            for m in a['mecanicas'])
        out.append(_syl_campo('9 &middot; Mec&acirc;nicas e grau de controle',
                              '<div class="tbl-wrap"><table class="data"><thead><tr>'
                              '<th>Mec&acirc;nica</th><th>Fun&ccedil;&atilde;o</th><th>Opera&ccedil;&atilde;o</th>'
                              '<th>Controle</th><th>Evid&ecirc;ncia</th></tr></thead><tbody>'
                              + linhas + '</tbody></table></div>'))
        out.append(_syl_campo('10 &middot; Avalia&ccedil;&atilde;o e progress&atilde;o', a['avaliacao']))
        sp = a['spec']
        out.append('<div class="callout"><span class="callout-title">Ficha de especificacao '
                   '(prompt controlador, fase 1)</span></div>')
        for rot, chave in (('Necessidade', 'necessidade'),
                           ('Por que este framework', 'framework_justificativa'),
                           ('Origem da necessidade', 'origem'),
                           ('Conte&uacute;do recuperado', 'conteudo_recuperado'),
                           ('Conte&uacute;do exclu&iacute;do', 'conteudo_excluido'),
                           ('Retask', 'retask')):
            out.append(_syl_campo(rot, sp[chave]))
        out.append('</div></details>')

    for c in d.get('_conflitos_declarados', []):
        out.append('<div class="teacher-section"><div class="callout warn">'
                   '<span class="callout-title">Conflito declarado &mdash; decis&atilde;o pendente</span>'
                   '%s</div><p style="font-size:.84rem;line-height:1.6;color:var(--text-mid);'
                   'margin-top:.5rem"><strong>Por que nao foi resolvido:</strong> %s<br>'
                   '<strong>Quem decide:</strong> %s<br>'
                   '<strong>Enquanto isso:</strong> %s</p></div>'
                   % (c['conflito'], c['por_que_nao_foi_resolvido'], c['quem_decide'],
                      c['enquanto_isso']))
    return '\n'.join(out)


def hub_tab_path(cfg, content_dir, nome):
    """Onde mora o conteudo de uma ABA DE HUB (planning/evidencias/syllabus).

    A aba de hub e do ALUNO, nao da aula: existe UMA por aluno, e o hub e montado uma vez
    so (modo "new"). Ate 11/08/2026 esses arquivos moravam no diretorio da aula que criava
    o hub — o que so nao mordia porque essa aula era sempre a de numero 1.

    Quando a ordem do bloco 1 da stephanie mudou (o normativo de agosto fixou Reading na
    aula 1 e o ESP na 4), o plano e a ficha, que descrevem o ESP, teriam de ou viajar para
    _build/{slug}-aula4/ (onde o builder nunca os leria, e o hub perderia as duas abas) ou
    ficar em _build/{slug}-aula1/ mentindo sobre a aula que descrevem. Nenhum dos dois e
    verdade: eles nao pertencem a nenhuma aula, pertencem ao aluno.

    Ordem de busca: _build/{slug}/{nome} (o lugar certo) e, se nao houver, o diretorio da
    aula (o lugar antigo). O fallback mantem TODO aluno ja existente byte-a-byte igual.
    """
    aluno_dir = os.path.join(ROOT, '_build', cfg['slug'], nome)
    if os.path.exists(aluno_dir):
        return aluno_dir
    return os.path.join(content_dir, nome)


def build_hub_new(cfg, content_dir, manifest):
    """Hub completo (aluno NOVO, sem hub existente). Clona os hubs do modelo."""
    L = cfg['lesson']
    audio_base = f'/audio/{cfg["slug"]}/'
    preclass = read(os.path.join(content_dir, 'preclass.html'))
    preclass = inject_kids_game(preclass, cfg)  # MODELO KIDS: mini-game Dino Tap (no-op p/ adulto)
    planning = read(hub_tab_path(cfg, content_dir, 'planning.html'))
    # ABAS DA ANATOMIA guided-discovery. Sao OPCIONAIS por arquivo: se o autor nao escreveu
    # evidencias.html/syllabus.html, o painel fica com o texto de esqueleto do shell em vez
    # de estourar. Mas a aba Evidencias e onde vive a ficha pos-aula, e sem ela as aulas
    # 5-20 nao podem ser geradas — entao vale um aviso alto, nao um silencio.
    evidencias = syllabus_tab = None
    hub_html_ = read(hub_path(cfg))
    if 'id="tab-evidencias"' in hub_html_:
        pe = hub_tab_path(cfg, content_dir, 'evidencias.html')
        if os.path.exists(pe):
            evidencias = read(pe)
        else:
            print('  AVISO: anatomia tem aba Evidencias e nao ha evidencias.html — '
                  'a ficha pos-aula fica vazia, e sem ela as aulas 5-20 nao saem.')
    if 'id="tab-syllabus"' in hub_html_:
        # FONTE UNICA: _build/{slug}/syllabus.json (os 10 campos do docx §3.1). O
        # syllabus.html escrito a mao continua valendo como fallback — nenhum aluno
        # existente muda de comportamento por causa disto.
        syllabus_tab = syllabus_tab_html(cfg)
        if syllabus_tab is None:
            ps = hub_tab_path(cfg, content_dir, 'syllabus.html')
            if os.path.exists(ps):
                syllabus_tab = read(ps)
        if syllabus_tab is None:
            print('  AVISO: anatomia tem aba Syllabus e nao ha syllabus.json nem '
                  'syllabus.html — a aba fica com o texto de esqueleto do shell, que '
                  'anuncia 20 aulas e nao mostra nenhuma.')
    # Complementares so e LIDO se a anatomia do hub tiver a aba. Ler incondicionalmente
    # obrigaria a existir um arquivo que nao tem onde entrar.
    complementary = ''
    if not sem_aba_complementares(read(hub_path(cfg))):
        complementary = normalize_complementary(read(os.path.join(content_dir, 'complementary.html')), cfg)

    entries = assign_voices(extract_phrases(preclass), prefix='pc_', cfg=cfg)
    extra = L.get('extra_audio', [])
    amap = audio_map_js(entries, audio_base, extra)
    for text, meta in entries.items():
        manifest.append(dict(text=text, voice=meta['voice'], file=meta['file']))

    card = menu_card(cfg, f'/professor/{cfg["slug"]}-aula{L["n"]}.html?autostart=1')

    s = read(hub_path(cfg))
    s = base_swaps(s, cfg)
    s = re.sub(r'<title>[^<]*</title>',
               f'<title>Professor View -- {cfg["student_name"]} | {cfg["program"]}</title>', s, count=1)
    s = re.sub(r'<h1>[^<]*</h1>', f'<h1>{cfg["student_name"]}</h1>', s, count=1)
    s = patch_header(s, cfg, cfg.get('hub_subtitle', cfg['program']))
    s = replace_between(s, '<div class="tab-content active" id="tab-planning">', '</div><!-- /tab-planning -->', '\n' + planning + '\n')
    s = replace_between(s, '<div class="tab-content" id="tab-exercises">', '</div><!-- /tab-exercises -->', '\n' + preclass + '\n')
    s = replace_between(s, '<div class="tab-content" id="tab-inclass">', FIM_DO_INCLASS, inclass_menu([card]))
    if not sem_aba_complementares(s):
        s = replace_between(s, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', '\n' + complementary + '\n')
    if evidencias:
        s = replace_between(s, '<div class="tab-content" id="tab-evidencias">',
                            '</div><!-- /tab-evidencias -->', '\n' + evidencias + '\n')
    if syllabus_tab:
        s = replace_between(s, '<div class="tab-content" id="tab-syllabus">',
                            '</div><!-- /tab-syllabus -->', '\n' + syllabus_tab + '\n')
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=1', s)
    s = re.sub(r'var audioMap = \{.*?\};', lambda _: amap, s, count=1, flags=re.S)
    final_asserts(s, cfg, 'hub prof', is_hub=True)
    write(os.path.join(PROF, f'{cfg["slug"]}.html'), apply_ui_strings(s, cfg))

    a = read(hub_path(cfg, aluno=True))
    a = base_swaps(a, cfg)
    a = re.sub(r'<title>[^<]*</title>', f'<title>{cfg["student_name"]} | {cfg["program"]} -- Alumni</title>', a, count=1)
    a = re.sub(r'<h1>[^<]*</h1>', f'<h1>{cfg["student_name"]}</h1>', a, count=1)
    a = patch_header(a, cfg, cfg.get('hub_subtitle', cfg['program']))
    a = replace_between(a, '<div class="tab-content active" id="tab-exercises">', '</div><!-- /tab-exercises -->', '\n' + preclass + '\n')
    if not sem_aba_complementares(a):
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
        # CARIMBO DE GERAÇÃO NO BLOCO, não no arquivo. O hub é antigo e o insert_hub só
        # injeta trechos nele: ele nunca ganha <meta name="alumni-gen">, e por isso TODO
        # gate escopado por geração era cego para o Pre-class inteiro (achado em 29/07/2026,
        # ao tentar cobrir os fill-in-the-blank da aula 1 da Ana Claudia). Carimbar o hub
        # inteiro seria pior: passaria a cobrar as invariantes novas dos blocos LEGADOS que
        # convivem nele (REGRA 30). O carimbo vai no accordion que este build emitiu — e só
        # nele.
        pc = re.sub(r'<div class="lesson-card"(?![^>]*\bdata-gen=)',
                    f'<div class="lesson-card" data-gen="{BUILDER_GEN}"', pc, count=1)
        parts.append(pc + '\n\n')
    # COMPLEMENTARES da aula: obrigatório (classe de bug do PR #106 — aula sem
    # complementares no hub). data-media deve usar prefixo l{N}- (validador cobra).
    #
    # EXCECAO: molde cuja ANATOMIA nao tem a aba. O shell decide — se o arquivo de shell
    # daquele slug nao traz `id="tab-complementary"`, exigir o bloco seria exigir conteudo
    # para uma aba que nao existe, e ele acabaria injetado no vazio. Nao e afrouxamento: a
    # obrigacao continua inteira para todo molde que TEM a aba (que e todo o resto hoje).
    # Ver a secao 0 do RULEBOOK-PEDAGOGICO: obrigatoriedade e propriedade do molde.
    tem_aba_complementares = 'id="tab-complementary"' in read(shell_path(cfg))
    comp_path = os.path.join(content_dir, 'complementary.html')
    if not tem_aba_complementares:
        assert not os.path.exists(comp_path), (
            f'{os.path.relpath(content_dir, ROOT)} tem complementary.html, mas o shell de '
            f'"{cfg.get("slug")}" nao tem a aba Complementares. O bloco nao teria onde '
            f'entrar — apague o arquivo ou use um shell que tenha a aba.')
    else:
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
    # vozes da AULA = global + cfg['voices'] (eixo de sotaque por aluno). MESMA resolucao
    # do gen_audio.py e do validate_lesson.py.
    global VOICES
    _extra = cfg.get('voices') or {}
    if isinstance(_extra, dict):
        VOICES = {**VOICES, **_extra}
    # 3 e limite do SHELL (so ha 3 cores de dialogo: 2 + .guest), nao de vozes.
    assert len(cfg['characters']) <= 3, \
        'máx 3 personagens por diálogo — o shell só tem 3 cores (2 + .guest)'
    for v in cfg['characters'].values():
        assert v in VOICES, (f'voz desconhecida no characters: {v} '
                             f'(disponíveis: {sorted(VOICES)}). Voz de sotaque vai em '
                             f'cfg["voices"] da aula — ver _build/model/README.md)')
    assert_framework(cfg)

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
