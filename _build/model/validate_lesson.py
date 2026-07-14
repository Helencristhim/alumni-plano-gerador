#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_lesson.py — GATE de qualidade do MODELO. Roda ANTES de mergear qualquer aula.

Herda todas as regras do validar_aula.py (div extra, wildcard de contraste, áudio
faltando, fantasma no exit, target=_blank...) e adiciona as regras do modelo:

  VOZES POR PERSONAGEM (bloqueante):
   - toda dialogue-line tem data-voice
   - cada personagem (classe do avatar) usa UMA voz consistente no arquivo inteiro
   - personagens DIFERENTES no mesmo diálogo (mesmo slide) têm vozes DIFERENTES
   - diálogo com mais falantes do que vozes disponíveis (voices.json) = ERRO
   - cross-check com audio_manifest.json: o MP3 de cada fala foi gerado com a voz
     declarada no data-voice (pega manifest gerado antes de trocar a voz no HTML)

  ANTI-REGRESSÃO dos fixes globais (bloqueante em arquivo com slides):
   - nav-bar flex (fix Andreia e615c853): slide-mode usa display:flex + nav-bar DENTRO do wrapper
   - contrast-guard.js plugado
   - EXIT do standalone usa exitSlideMode() (nunca só classList.remove)
   - handler de teclado fora de <script src=...> (senão nunca roda)
   - mistake-item sem <p>/<strong> direto (flex espalha inline — REGRA Common Mistake)
   - todo onclick/onchange aponta pra função que EXISTE no arquivo (exercício novo quebrado)

  PERSISTÊNCIA / SYNC CROSS-DEVICE (REGRA 28, bloqueante em material do aluno):
   - activity-sync.js + supabase + STUDENT_SLUG presentes (sem eles a gravação de
     áudio do Pre-class SOME ao atualizar a página / abrir de outro device)
   - lesson-progress.js + controle-aulas.js presentes; ordem e TOTAL_AULAS = WARN

USO (da raiz do repo):
  python3 _build/model/validate_lesson.py public/professor/{slug}-aula{N}.html [mais.html ...]
Exit code 1 se algum arquivo falhar.
"""
import glob
import json
import os
import re
import subprocess
import sys
from html import unescape as html_unescape

HERE = os.path.dirname(os.path.abspath(__file__))
VOICES = json.load(open(os.path.join(HERE, 'voices.json'), encoding='utf-8'))

# O DISCO NÃO É A FONTE DA VERDADE — o repositório é.
# O repo usa sparse-checkout com `!/public/audio/`: os 60 mil MP3s estão versionados
# mas não materializados na árvore local. Um os.path.exists() puro responde "não existe"
# para TODO áudio do projeto e este check acusa "N MP3s faltando" numa aula cujos MP3s
# estão commitados. Já mordeu na geração do Diogo (24 falsos positivos, 0 reais).
# Mesmo conserto que o scripts/check_lesson_integrity.py.
_VERSIONADOS = {}


def audio_existe(root, ref):
    """ref = '/audio/slug/x.mp3'. Existe se estiver no disco OU versionado no git."""
    ref = ref.split('?')[0]         # tira o cache-buster (?v=2): no disco o arquivo não o tem
    if os.path.exists(os.path.join(root, 'public' + ref)):
        return True
    if root not in _VERSIONADOS:
        try:
            saida = subprocess.run(['git', 'ls-files', 'public/audio'], cwd=root,
                                   capture_output=True, text=True, timeout=60).stdout
            _VERSIONADOS[root] = {l.strip() for l in saida.splitlines() if l.strip()}
        except Exception:
            _VERSIONADOS[root] = set()      # sem git: cai para o disco (comportamento antigo)
    return ('public' + ref) in _VERSIONADOS[root]

# funções nativas/inline aceitas em handlers sem definição no arquivo
BUILTIN_OK = {'event', 'window', 'document', 'this', 'location', 'localStorage', 'alert', 'confirm'}

# ===== IDIOMA (REGRA 13 / docs/RULEBOOK-PEDAGOGICO.md) =====
# "Português é permitido APENAS nos níveis A0 e A1. A partir do A2, ZERO português em
#  QUALQUER parte do material. Única exceção: instruções ao professor via ícone T."
#
# Marcadores de PT que NÃO são palavras inglesas. Os homógrafos ficam DE FORA de
# propósito — 'do', 'no', 'so', 'a', 'as', 'complete', 'imagine', 'combine', 'use',
# 'real', 'total' existem nas DUAS línguas e dariam falso positivo em TODA aula de
# inglês (medido: o Pre-class do modelo, já 100% em inglês, casa 'complete', 'imagine'
# e 'do'). Um gate que grita em material correto é desligado pela equipe — e aí não
# gateia nada.
PT_MARCADORES = [
    'nao', 'voce', 'voces', 'dica', 'dicas', 'aula', 'aulas', 'frase', 'frases',
    'palavra', 'palavras', 'ouvir', 'ouca', 'gravar', 'selecione', 'traducao',
    'resposta', 'respostas', 'pergunta', 'perguntas', 'exemplo', 'exemplos',
    'trabalho', 'rotina', 'texto', 'conteudo', 'conteudos', 'marque', 'leia',
    'pratique', 'descreva', 'apresente', 'escolha', 'antes', 'depois', 'melhor',
    'cada', 'muito', 'tambem', 'entao', 'assim', 'apenas', 'ainda', 'agora',
    'aqui', 'isso', 'este', 'esta', 'esse', 'essa', 'materiais', 'complementares',
    'estruturas', 'missao', 'para', 'uma', 'seu', 'sua', 'seus', 'suas', 'sobre',
    'quando', 'onde', 'porque', 'sem', 'pelo', 'pela', 'mais', 'menos', 'todos',
    'todas', 'primeiro', 'segundo', 'coisa', 'coisas', 'fazer', 'usando', 'sempre',
    'nunca', 'exercicio', 'livre', 'assista', 'assistir', 'ouvindo', 'traga',
]
PT_RE = re.compile(r'\b(?:' + '|'.join(PT_MARCADORES) + r')\b', re.I)
# palavra acentuada em MINÚSCULA. Maiúscula é nome próprio legítimo em texto inglês
# ("I work in São Paulo", "Renê"), então não conta.
ACENTO_RE = re.compile(r'\b[\wÀ-ÿ]*[àáâãéêíóôõúüç][\wÀ-ÿ]*\b')
# sufixos PT sem acento que o resto da heurística não pegaria
SUFIXO_RE = re.compile(r'\b\w+(?:mente|acao|acoes|avel)\b', re.I)
# HOMÓGRAFOS DO SUFIXO. Mesma razão pela qual 'do'/'complete'/'imagine' ficam de fora da
# lista de marcadores: são palavras INGLESAS que a heurística de PT vê como português.
# 'tr-avel' e 'gr-avel' terminam em -avel (o sufixo de 'responsavel', 'amavel') e viravam
# PORTUGUÊS aos olhos do gate. Numa aluna cujo programa é "English for Travel", isso reprova
# TODA aula correta — e gate que grita em material certo é gate que a equipe desliga.
SUFIXO_EN_OK = {'travel', 'gravel', 'ravel', 'unravel'}


def nivel_do_html(c):
    """Nível CEFR lido do header (student-info) — funciona sem config de build."""
    m = re.search(r'<div class="student-info">(.*?)</div>', c, re.S)
    if not m:
        return None
    for sp in re.findall(r'<span>([^<]+)</span>', m.group(1)):
        mm = re.match(r'^\s*([ABC][0-2])\b', sp.strip())
        if mm:
            return mm.group(1)
    return None


def pt_na_tela(html):
    """Português VISÍVEL AO ALUNO dentro de `html` (bloco de Pre-class ou cards da aula).

    Varre TEXTO **e ATRIBUTO**. Só limpar as tags é um furo: o strip apaga
    data-hint="Dica: ...", <option>público</option> e placeholder — e as 30 dicas em
    português passariam invisíveis pelo gate que existe para pegá-las. Atributo também
    é tela: o aluno lê a dica e escolhe a opção.

    data-teacher fica de FORA: é a exceção do rulebook (instrução ao professor, removida
    do espelho do aluno pelo builder). PT ali é obrigatório, não defeito.
    """
    alvo = re.sub(r'\sdata-teacher="(?:[^"\\]|\\.)*"', '', html)
    alvo = re.sub(r'<script\b.*?</script>', '', alvo, flags=re.S)
    atributos = []
    for a in ('data-hint', 'data-answer', 'placeholder', 'aria-label'):
        atributos += re.findall(rf'{a}="([^"]*)"', alvo)
    atributos += re.findall(r'<option value="[^"]*">([^<]*)</option>', alvo)
    texto = re.sub(r'<[^>]+>', ' ', alvo)
    texto = re.sub(r'https?://\S+', ' ', texto)          # URL não é prosa
    alvo_txt = texto + ' \n ' + ' \n '.join(atributos)
    achados = {t for t in ACENTO_RE.findall(alvo_txt) if t[:1].islower()}
    achados |= {w.lower() for w in PT_RE.findall(alvo_txt)}
    achados |= {w.lower() for w in SUFIXO_RE.findall(alvo_txt)} - SUFIXO_EN_OK
    return sorted(achados)


def matching_nao_ingles(blk):
    """Linhas de matching cuja RESPOSTA não é uma definição em inglês.

    Acento não basta aqui e foi exatamente por isso que 32 opções passaram: as opções do
    matching são palavras PT CURTAS e SEM ACENTO — 'marca', 'meta', 'prazo', 'parceiro',
    'tarefa', 'limite', 'marco'. Nenhuma heurística de acento as vê.

    Em vez de tentar adivinhar a língua de uma palavra solta (insolúvel), exige-se o
    FORMATO que a REGRA 13 manda em A2+: palavra EN <-> DEFINIÇÃO EM INGLÊS (o mesmo
    formato que o IN CLASS já usa). Uma definição em inglês SEMPRE carrega uma function
    word ("a company or person who works with you"). 'marca' não carrega — e é isso que
    se quer barrar.
    """
    FW = (r"\b(?:a|an|the|to|of|that|who|what|which|you|your|it|its|is|are|be|for|with|"
          r"and|or|from|in|on|at|when|someone|something|not|no|more|than|other|others)\b")
    ruins = []
    for m in re.finditer(r'<div class="match-row"[^>]*data-answer="([^"]*)"', blk):
        ans = m.group(1)
        if ans and not re.search(FW, ans, re.I):
            ruins.append(ans)
    return ruins


def strip_code(c):
    c = re.sub(r'<script\b.*?</script>', '', c, flags=re.S | re.I)
    c = re.sub(r'<style\b.*?</style>', '', c, flags=re.S | re.I)
    c = re.sub(r'<!--.*?-->', '', c, flags=re.S)
    return c


def get_css(c):
    css = '\n'.join(re.findall(r'<style\b[^>]*>(.*?)</style>', c, flags=re.S | re.I))
    return re.sub(r'/\*.*?\*/', '', css, flags=re.S)


def _e_raiz(p):
    # A raiz é onde há .git + public/. NÃO usar public/audio/ como sinal: sob
    # sparse-checkout esse diretório não existe, repo_root_for devolvia None e a
    # checagem de áudio inteira era PULADA em silêncio — gate desligado, não gate
    # falhando. (.git é diretório no clone e ARQUIVO num worktree.)
    return os.path.exists(os.path.join(p, '.git')) and os.path.isdir(os.path.join(p, 'public'))


def repo_root_for(path):
    p = os.path.abspath(path)
    while p != '/' and not _e_raiz(p):
        p = os.path.dirname(p)
    return p if _e_raiz(p) else None


def find_manifest(path, root):
    m = re.search(r'/(?:professor|aluno)/(.+)-aula(\d+)\.html$', path.replace('\\', '/'))
    if not (m and root):
        return None
    for d in (f'{m.group(1)}-aula{m.group(2)}', m.group(1)):
        p = os.path.join(root, '_build', d, 'audio_manifest.json')
        if os.path.exists(p):
            return p
    return None


def check_dialogue_voices(c, path, root, fails, warns):
    """Vozes por personagem: data-voice obrigatório, 1 voz por personagem,
    personagens distintos = vozes distintas, cross-check com o manifest."""
    # posição de cada slide pra agrupar diálogos
    slide_marks = [(m.start(), m.group(1)) for m in re.finditer(r'data-slide="(\d+)"', c)]

    def slide_of(pos):
        cur = 'preclass'
        for p, n in slide_marks:
            if p > pos:
                break
            cur = n
        return cur

    lines = []  # (slide, speaker, voice, frase, pos)
    for m in re.finditer(r'<div class="dialogue-line[^"]*"[^>]*>', c):
        tag = m.group(0)
        mv = re.search(r'data-voice="([a-z]+)"', tag)
        seg = c[m.end():m.end() + 1200]
        ma = re.search(r'dialogue-avatar ([\w-]+)', seg)
        mt = re.search(r"speakText\('((?:[^'\\]|\\.)*)'", seg)
        if not mv:
            fails.append(f'dialogue-line SEM data-voice (pos {m.start()}): {tag[:90]}')
            continue
        voice = mv.group(1)
        if voice not in VOICES:
            fails.append(f'data-voice="{voice}" não existe em voices.json (disponíveis: {sorted(VOICES)})')
            continue
        lines.append((slide_of(m.start()), ma.group(1) if ma else '?',
                      voice, mt.group(1).replace("\\'", "'") if mt else None, m.start()))

    if not lines:
        return

    # 1 voz consistente por personagem (arquivo inteiro)
    by_speaker = {}
    for sl, sp, v, t, pos in lines:
        by_speaker.setdefault(sp, set()).add(v)
    for sp, vs in by_speaker.items():
        if len(vs) > 1:
            fails.append(f'personagem "{sp}" com MAIS DE UMA voz: {sorted(vs)} (1 voz por personagem)')

    # dentro de cada diálogo (slide): falantes distintos = vozes distintas
    by_slide = {}
    for sl, sp, v, t, pos in lines:
        by_slide.setdefault(sl, {}).setdefault(sp, set()).add(v)
    for sl, speakers in by_slide.items():
        if len(speakers) > len(VOICES):
            fails.append(f'diálogo do slide {sl} tem {len(speakers)} falantes ({", ".join(speakers)}) '
                         f'mas só há {len(VOICES)} vozes ({", ".join(sorted(VOICES))}) — impossível diferenciar. '
                         f'Reescrever com menos falantes ou adicionar voz em voices.json')
        used = {}
        for sp, vs in speakers.items():
            for v in vs:
                if v in used and used[v] != sp:
                    fails.append(f'diálogo do slide {sl}: "{sp}" e "{used[v]}" usam a MESMA voz ({v}) — '
                                 f'cada pessoa do diálogo precisa de voz própria')
                used[v] = sp

    # cross-check manifest: MP3 da fala gerado com a voz do data-voice
    mp = find_manifest(path, root)
    if mp:
        manifest = {e['file']: e['voice'] for e in json.load(open(mp, encoding='utf-8'))}
        amap = dict(re.findall(r'"((?:[^"\\]|\\.)*)"\s*:\s*"(/audio/[^"]+)"', c))
        amap = {k.replace('\\"', '"'): os.path.basename(v) for k, v in amap.items()}
        for sl, sp, v, t, pos in lines:
            if not t:
                continue
            f = amap.get(t) or amap.get(t.rstrip('.')) or amap.get(t + '.')
            if not f:
                continue  # áudio faltando já é outra regra
            mv = manifest.get(f)
            if mv and mv != v:
                fails.append(f'fala de "{sp}" (slide {sl}) declara voz {v} mas o MP3 {f} '
                             f'foi gerado com {mv} (manifest) — regenerar o áudio')
    else:
        warns.append('audio_manifest.json não encontrado em _build/ — cross-check de voz dos MP3s pulado')


def check_fix_regressions(c, css, is_standalone_slides, fails, warns):
    """Cada fix global vira regra permanente — regressão = FAIL."""
    if 'slidesContainer' in c and 'data-slide=' in c:
        if 'body.slide-mode .slides-wrapper { display:flex;flex-direction:column; }' not in c:
            fails.append('REGRESSÃO fix nav-bar (e615c853): slide-mode sem display:flex;flex-direction:column '
                         '— nav-bar volta a flutuar no meio da tela')
        m_wrap = re.search(r'</div><!-- /slides-wrapper -->', c)
        m_nav = re.search(r'<div class="nav-bar"', c)
        if m_wrap and m_nav and m_nav.start() > m_wrap.start():
            fails.append('REGRESSÃO fix nav-bar: <div class="nav-bar"> está FORA do slides-wrapper')
        if is_standalone_slides:
            ex = re.search(r'aria-label="Exit presentation"', c)
            if ex and 'exitSlideMode()' not in c[max(0, ex.start() - 300):ex.start() + 100]:
                fails.append('EXIT do standalone não usa exitSlideMode() (bug original do Roberto)')
    if '/lib/contrast-guard.js' not in c:
        fails.append('contrast-guard.js NÃO plugado (obrigatório em toda página do modelo)')
    # script com src NÃO pode ter corpo (handler dentro nunca roda)
    for m in re.finditer(r'<script src="[^"]+">([^<]*)</script>', c):
        if m.group(1).strip():
            fails.append(f'código DENTRO de <script src=...> (nunca executa): {m.group(1).strip()[:60]}')
    # mistake-item: texto direto, sem <p>/<strong> filhos (flex espalha inline)
    for m in re.finditer(r'<div class="mistake-item[^"]*"[^>]*>(.{0,200})', c, flags=re.S):
        seg = m.group(1)
        if re.match(r'\s*<(p|strong)\b', seg):
            fails.append('mistake-item com <p>/<strong> direto — texto deve ser direto no div (display:flex espalha)')
    # Rolagem de slide (#1071/#1073/#1074, "centraliza-se-cabe / rola-se-passa"): slide
    # alto (ex: vocab de 5 cards, leitura+atividade) NÃO pode cortar conteúdo atrás da
    # nav-bar sem barra de rolagem. Todo arquivo com slides + .slide-inner DEVE ter o
    # override de rolagem — inclusive o ESPELHO ALUNO (que o #1074 esqueceu).
    if 'data-slide=' in c and 'slide-inner' in c:
        if not re.search(r'\.slide\s*>\s*\.slide-inner\s*\{[^}]*overflow-y\s*:\s*auto', css):
            fails.append('REGRESSÃO fix rolagem de slide (#1074): falta '
                         '".slide>.slide-inner{...max-height:calc(100vh - 11rem);overflow-y:auto...}" — '
                         'slide alto corta conteúdo atrás da nav-bar sem barra de rolagem (incidente Patricia aula 1)')
    # Sentence Building (.oral-item): a RESPOSTA (.oral-model) deve começar escondida
    # e só aparecer no clique. Sem isso, o gabarito vaza na tela.
    # Só checa se o EXERCÍCIO existe de fato (class="oral-item" no HTML) — a mera presença
    # do CSS .oral-model herdado do shell do modelo NÃO é vazamento (não há gabarito na tela).
    # Aceita as duas variantes de revelar: .revealed (modelo novo) e .open (materiais antigos).
    if re.search(r'class="oral-item[\s"]', c):
        hidden = re.search(r'\.oral-model\b[^{]*\{[^}]*display\s*:\s*none', css)
        reveal = re.search(r'\.oral-item\.(revealed|open)\b[^{]*\.oral-model', css)
        if not (hidden and reveal):
            fails.append('Sentence Building VAZA o gabarito: .oral-model precisa começar com display:none '
                         'e ser revelado por ".oral-item.revealed .oral-model" (ou .open) no clique')
        # ESTILO-BASE do card (irmão do gate acima: aquele cuida do COMPORTAMENTO, este do
        # VISUAL). O .oral-item nasceu sem NENHUM layout — background/border/padding todos
        # ausentes — e o bloco saía como uma lista <div> nua no meio de um deck todo em
        # cards. O override .slide-dark .oral-item{background:#fff} existia e enganava:
        # dava a impressão de que havia estilo. NÃO basta: fora do slide escuro não há nada.
        # Exige o estilo-base REAL (regra .oral-item sem prefixo .slide-dark).
        decl = ''
        for m in re.finditer(r'(?:^|[},])\s*([^{},]*\.oral-item[^{},]*)\{([^}]*)\}', css):
            sel = m.group(1)
            if ('.slide-dark' not in sel and ':hover' not in sel and ':focus' not in sel
                    and '.revealed' not in sel and '.oral-model' not in sel):
                decl += m.group(2) + ';'
        falta = [p for p in ('background', 'border', 'padding') if not re.search(rf'\b{p}\b\s*:', decl)]
        if falta:
            fails.append(f'Sentence Building SEM ESTILO-BASE: .oral-item não define '
                         f'{", ".join(falta) or "nada"} — o bloco sai como lista nua enquanto o resto do '
                         f'deck é em cards. Definir .oral-item{{background;border;padding;border-radius}} '
                         f'junto dos .error-card/.challenge-card (o override .slide-dark NÃO conta)')

    # LISTENING: a PERGUNTA vem ANTES do áudio (CLAUDE.md REGRA 2.1, bloqueante).
    # O container .comp-questions NUNCA nasce escondido. Se o aluno só vê a pergunta
    # DEPOIS de ouvir, ele ouviu sem saber o que procurar: listening virou teste de
    # MEMÓRIA. A pergunta É a tarefa de escuta.
    # "Sound-first" = esconder a TRANSCRIÇÃO, jamais a PERGUNTA.
    # O bug nasceu da REGRA errada no CLAUDE.md ("perguntas aparecem após audio.ended"):
    # o shell do modelo sempre esteve certo, mas o LLM que escrevia a aula injetava
    # style="display:none" no container. 224 arquivos saíram assim.
    # Os handlers play/ended do shell podem seguir fazendo display='block' (no-op com o
    # container já visível) — o que se proíbe aqui é o ESTADO INICIAL escondido.
    for m in re.finditer(r'<div[^>]*class="comp-questions"[^>]*>', c):
        tag = m.group(0)
        ms = re.search(r'style="([^"]*)"', tag)
        if ms and re.search(r'display\s*:\s*none|visibility\s*:\s*hidden|opacity\s*:\s*0(?![.\d])', ms.group(1)):
            mid = re.search(r'id="([^"]*)"', tag)
            fails.append(f'LISTENING com a PERGUNTA ESCONDIDA (#{mid.group(1) if mid else "?"}): '
                         f'.comp-questions nasce com display:none/visibility:hidden/opacity:0 e só aparece '
                         f'no fim do áudio — o aluno ouve SEM SABER O QUE PROCURAR (listening vira teste de '
                         f'memória). As perguntas ficam VISÍVEIS desde a entrada no slide, ANTES do play. '
                         f'"Sound-first" = esconder a TRANSCRIÇÃO, nunca a PERGUNTA (CLAUDE.md REGRA 2.1)')
    if re.search(r'class="comp-questions"', c):
        if re.search(r'\.comp-questions\b[^{]*\{[^}]*(?:display\s*:\s*none|visibility\s*:\s*hidden)', css):
            fails.append('LISTENING com a PERGUNTA ESCONDIDA: o CSS de .comp-questions tem '
                         'display:none/visibility:hidden — as perguntas devem estar VISÍVEIS antes do play '
                         '(CLAUDE.md REGRA 2.1)')


def _sem_teacher(ch):
    """O slide SEM data-teacher. Estrutura se lê na CLASSE, nunca na prosa do professor —
    o data-teacher pode CITAR o nome de uma classe ("volte ao ic-reading") e um match por
    substring passa a ver estrutura onde só há texto. (Foi assim que o slide de tarefa da
    leitura sumiu do arquivo do professor e não do aluno, na aula 3 do modelo.)"""
    return re.sub(r'\sdata-teacher="(?:[^"\\]|\\.)*"', '', ch)


def _txt(s):
    return ' '.join(re.sub(r'<[^>]+>', ' ', s).split())


def check_task_before_exposure(c, fails, warns):
    """A TAREFA VEM ANTES DA EXPOSIÇÃO (CLAUDE.md REGRA 2.2, bloqueante).

        [TAREFA: as perguntas, sem resposta] -> [diálogo/texto] -> [checagem: as MESMAS
        perguntas, com click-to-reveal]

    O aluno precisa saber O QUE PROCURAR antes de ser exposto. Sem a tarefa antes, a
    compreensão testa MEMÓRIA — outra habilidade, que não é a que se está ensinando.
    Mesmo princípio do listening (REGRA 2.1), aplicado a diálogo e leitura.

    O slide de ARTEFATO (email/boarding pass) fica FORA: lá a pergunta já divide a tela
    com o objeto, e o aluno pode olhar enquanto responde.
    """
    i = c.find('<div class="slides-container"')
    j = c.find('</div><!-- /slides-container -->')
    if i < 0 or j < 0:
        return
    partes = [p for p in re.split(r'(?=<div class="slide )', c[i:j]) if 'data-slide=' in p]

    def expo(ch):
        e = _sem_teacher(ch)
        if 'class="dialogue-line' in e:
            return 'dialogue'
        if 'class="ic-reading"' in e:
            return 'reading'
        return None

    def perguntas_checagem(ch):
        e = _sem_teacher(ch)
        if 'ic-tfrow' in e:
            out = []
            for st in re.findall(r'<span class="ic-stmt">(.*?)</span>\s*<span class="ic-verdict', e, re.S):
                out.append(_txt(re.sub(r'<span class="ic-just">.*?</span>', '', st, flags=re.S)))
            return [q for q in out if q]
        if 'class="comp-q"' in e and 'mock-player' not in e:
            return [_txt(q) for q in re.findall(r'<div class="q-text">(.*?)</div>', e, re.S)]
        return []

    for k, ch in enumerate(partes):
        kind = expo(ch)
        if not kind:
            continue
        n = (re.search(r'data-slide="(\d+)"', ch) or [None, '?'])[1]
        # perguntas do slide de CHECAGEM que vem depois (a fonte)
        alvo = []
        for m in range(k + 1, min(k + 6, len(partes))):
            if expo(partes[m]):
                break
            alvo = perguntas_checagem(partes[m])
            if alvo:
                break
        if not alvo:
            warns.append(f'slide {n} ({kind}) sem slide de checagem depois — tarefa não verificável')
            continue
        ant = partes[k - 1] if k > 0 else ''
        mt = re.search(r'data-task-for="(\w+)"', ant)
        if not mt:
            fails.append(
                f'TAREFA AUSENTE antes do {kind} (slide {n}): o aluno é exposto ao '
                f'{"diálogo" if kind == "dialogue" else "texto"} SEM saber o que procurar — a '
                f'compreensão vira teste de MEMÓRIA. Falta o slide de tarefa ANTES, com as '
                f'{len(alvo)} pergunta(s) do slide de checagem e SEM as respostas '
                f'(CLAUDE.md REGRA 2.2). O builder emite esse slide sozinho: '
                f'build_from_model.inject_task_slides()')
            continue
        if mt.group(1) != kind:
            fails.append(f'slide de tarefa antes do {kind} (slide {n}) está marcado como '
                         f'data-task-for="{mt.group(1)}" — deveria ser "{kind}"')
            continue
        # o GABARITO não pode estar no HTML do slide de tarefa — nem escondido.
        # (o professor compartilha a tela; display:none continua no DOM, a um Ctrl+U de distância)
        vaza = [x for x in ('q-answer', 'ic-verdict', 'ic-just', 'data-answer', 'revealComp')
                if x in _sem_teacher(ant)]
        if vaza:
            fails.append(f'slide de TAREFA antes do slide {n} CARREGA O GABARITO no HTML '
                         f'({", ".join(vaza)}) — a resposta não pode existir nesse slide nem escondida '
                         f'(display:none continua no DOM). Só a pergunta (REGRA 2.2)')
        # a tarefa TEM de ser a mesma coisa que a checagem cobra
        tq = [_txt(q) for q in re.findall(r'<div class="q-text">(.*?)</div>', _sem_teacher(ant), re.S)]
        if tq != alvo:
            fails.append(f'as perguntas do slide de TAREFA não casam com as da CHECAGEM (slide {n}, '
                         f'{kind}): tarefa={len(tq)} vs checagem={len(alvo)}. Se a tarefa não é a mesma '
                         f'coisa que se cobra depois, ela não é a tarefa. Devem sair da MESMA fonte '
                         f'(inject_task_slides)')


def check_handlers_exist(c, fails):
    """Todo onclick/onchange chama função que existe no arquivo (pega exercício novo quebrado)."""
    defined = set(re.findall(r'function\s+([A-Za-z_$][\w$]*)\s*\(', c))
    defined |= set(re.findall(r'(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=\s*function', c))
    missing = {}
    for m in re.finditer(r'on(?:click|change|input|submit)="\s*([A-Za-z_$][\w$]*)\s*\(', c):
        fn = m.group(1)
        if fn not in defined and fn not in BUILTIN_OK and not fn.startswith('mp'):
            missing[fn] = missing.get(fn, 0) + 1
    if 'mpToggle' in c and 'function mpToggle' not in c:
        missing['mpToggle'] = 1
    for fn, n in sorted(missing.items()):
        fails.append(f'handler onclick/onchange chama "{fn}()" ({n}x) mas a função NÃO existe no arquivo '
                     f'— exercício/elemento estruturalmente quebrado')


def check_audio_collision(c, fails):
    """Duas frases DIFERENTES apontando para o MESMO mp3 = o aluno ouve a frase errada.

    O snake() do builder corta o nome do arquivo em 48 chars e NÃO é injetivo. Duas
    frases com o mesmo começo caem no mesmo arquivo:

        "I started my career in technology ten years ago."  ┐
        "I got my first job in 2008."                       ┘ -> mesmo .mp3

    O aluno lê uma frase na tela e ouve OUTRA. Silencioso e invisível: o arquivo
    EXISTE, e existência é a única coisa que o check_lesson_integrity sabe perguntar.
    De novo o padrão do dia: o gate testa o proxy, não o comportamento.

    Encontrado em 13/07: 224 colisões em 45 alunos em produção. O builder já foi
    corrigido (sufixo de hash só quando há colisão real, então nada é renomeado);
    este gate impede que a classe volte a entrar.

    Ponto final / caixa / espaço extra NÃO são colisão — o speakText normaliza e as
    duas devem mesmo compartilhar o áudio.
    """
    bloco = re.search(r'(?:var|const|let)\s+audioMap\s*=\s*\{.*?\n\};', c, re.S)
    if not bloco:
        return
    por_mp3 = {}
    for k, v in re.findall(r'"((?:[^"\\]|\\.)*)"\s*:\s*"([^"]+\.mp3)"', bloco.group(0)):
        chave = k.replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')
        norm = re.sub(r'\s+', ' ', chave).strip().rstrip('.').lower()
        por_mp3.setdefault(v.split('?')[0], set()).add(norm)

    for mp3, frases in sorted(por_mp3.items()):
        if len(frases) > 1:
            a, b = sorted(frases)[:2]
            fails.append(
                f'COLISÃO DE ÁUDIO: {len(frases)} frases distintas apontam para '
                f'{mp3.split("/")[-1]} — o aluno lê uma e OUVE OUTRA. '
                f'Ex: "{a[:45]}..." vs "{b[:45]}..."')


def check_speaktext_escaping(c, fails):
    """speakText('...') com apóstrofo que fecha a string JS no meio: o onclick quebra
    (áudio não toca) E o áudio sai truncado (gerador lê a mesma frase cortada).

    DESESCAPA ANTES DE VARRER — e é ESTE o furo que deixou 208 botões passarem.
    A versão anterior varria a fonte CRUA procurando o caractere `'`. Só que no HTML
    o apóstrofo quase sempre está escrito `&#39;` — que não é um apóstrofo, são cinco
    caracteres. O validador não via nada de errado. Mas o NAVEGADOR desescapa o
    atributo ANTES de compilar o handler: para ele, `&#39;` É um apóstrofo, e a string
    fecha no lugar errado. O botão morre.

    Ou seja: o validador cometia o mesmo erro conceitual que o bug que ele deveria
    pegar — tratar o HTML ESCRITO como se fosse o JS EXECUTADO. Varremos o texto já
    desescapado, exatamente como o browser o vê. (Ver scripts/check_inline_js.mjs,
    que compila o handler no V8 — o motor do Chrome — e é a rede definitiva.)
    """
    c = html_unescape(c)
    broken = []
    for m in re.finditer(r"speakText\('", c):
        k = m.end()
        while k < len(c):
            ch = c[k]
            if ch == '\\':
                k += 2
                continue
            if ch == "'":
                after = c[k + 1:k + 8]
                if after.startswith((',this)', ', this)', ')', ',')):
                    pass  # string bem-formada
                else:
                    broken.append(c[m.end():k][:45])
                break
            k += 1
    if broken:
        fails.append(
            f'{len(broken)} speakText() com apóstrofo que FECHA A STRING JS no meio '
            f'-> o botão morre (o aluno clica e nada acontece) + o áudio sai truncado. '
            f'Ex: "{broken[0]}...". '
            f'NÃO conserte escapando (\\\' só adia): tire o texto de dentro da string JS. '
            f'Em ATRIBUTO, apóstrofo é caractere comum e não há string para fechar: '
            f'<button data-speak="It\'s ready." onclick="speakText(this.dataset.speak,this)">')


def check_b2_blocks(c, fails, warns):
    """B2 IN-CLASS BLOCKS (aditivo): reconhece os blocos novos e garante que os
    interativos estão BEM ligados (handler presente). NÃO reprova uma aula por
    USAR um bloco novo — só pega bloco interativo emitido sem o handler do shell
    (regressão estrutural, mesma classe do check_handlers_exist). Aula que não usa
    nenhum bloco .ic-* passa direto (no-op)."""
    if 'class="ic-' not in c:
        return
    for marker, fn in (('class="ic-choice"', 'icPickGist'),
                       ('class="ic-tfrow"', 'icRevealTf'),
                       ('class="ic-answer"', 'icToggleAnswer')):
        if marker in c and f'function {fn}' not in c:
            fails.append(f'B2 block interativo presente ({marker}) mas a função {fn}() do shell '
                         f'NÃO está no arquivo — bloco quebrado (handler ausente)')
    # gist: avisar se nenhuma alternativa marcada como correta
    for m in re.finditer(r'<div class="ic-choices">(.*?)</div>\s*</div>', c, flags=re.S):
        if 'data-right="true"' not in m.group(1):
            warns.append('B2 gist sem alternativa correta (data-right="true") — confira o config')


def check_persistence_wiring(c, path, fails, warns):
    """REGRA 28: persistência cross-device dos exercícios/gravações do aluno.

    O bug que isto pega: o aluno grava um áudio no Pre-class, atualiza a página
    (ou abre de outro device) e a gravação SUMIU. Causa = a página não tem o
    wiring de sync que a REGRA 28 exige. A gravação só persiste se a página
    incluir activity-sync.js + seus pré-requisitos (supabase + STUDENT_SLUG):
    é o activity-sync que intercepta o MediaRecorder e sobe o blob pro Supabase.

    FAIL (sync de gravação quebrado de fato):
      - falta supabase.min.js / supabase-config.js / window.STUDENT_SLUG
      - falta /lib/activity-sync.js, /lib/lesson-progress.js ou /lib/controle-aulas.js
    WARN (degradação coberta pelo auto-save de 30s, não perde gravação):
      - ordem errada dos 3 libs ou activity-sync ANTES do saveState() inline
      - falta window.TOTAL_AULAS (só a barra global do header)

    Só roda em MATERIAL DO MODELO (tem saveState inline + exercícios). Páginas
    bespoke com sync próprio (-speech-training) e templates legados (-v2/-v-a/-v-b,
    REGRA 20) ficam fora de escopo."""
    p = path.replace('\\', '/')
    if (re.search(r'-speech-training\.html$', p) or re.search(r'-v(?:2|-[ab])\.html$', p)
            or re.search(r'-test(?:-aula\d+)?\.html$', p)):
        return
    # gatilho: material padrão com infra de exercícios do aluno
    if 'function saveState' not in c or ('vocab-card-pc' not in c and 'speech-card' not in c):
        return

    def pos(needle):
        return c.find(needle)

    for needle, desc in (('supabase.min.js', 'supabase.min.js no <head> (cliente Supabase)'),
                         ('/lib/supabase-config.js', 'supabase-config.js no <head>'),
                         ('window.STUDENT_SLUG', 'window.STUDENT_SLUG no <head>')):
        if pos(needle) < 0:
            fails.append(f'PERSISTÊNCIA (REGRA 28): falta {desc} — sem isso a gravação do aluno '
                         f'não sobe pro Supabase e SOME ao atualizar a página / trocar de device')
    libs = (('/lib/lesson-progress.js', 'lesson-progress.js'),
            ('/lib/controle-aulas.js', 'controle-aulas.js'),
            ('/lib/activity-sync.js', 'activity-sync.js'))
    for needle, name in libs:
        if pos(needle) < 0:
            extra = (' (O MAIS IMPORTANTE: é ele que intercepta a gravação e a salva na nuvem; '
                     'sem ele as gravações/exercícios do Pre-class se perdem ao atualizar a página)'
                     if name == 'activity-sync.js' else '')
            fails.append(f'PERSISTÊNCIA (REGRA 28): falta /lib/{name}{extra}')

    lp, ca, asy = pos('/lib/lesson-progress.js'), pos('/lib/controle-aulas.js'), pos('/lib/activity-sync.js')
    if lp >= 0 and ca >= 0 and asy >= 0 and not (lp < ca < asy):
        warns.append('PERSISTÊNCIA (REGRA 28): ordem dos scripts deveria ser '
                     'lesson-progress.js -> controle-aulas.js -> activity-sync.js')
    sv = pos('function saveState')
    if asy >= 0 and sv >= 0 and asy < sv:
        warns.append('PERSISTÊNCIA (REGRA 28): activity-sync.js carregado ANTES do saveState() inline — '
                     'o wrap do save instantâneo não pega (auto-save de 30s ainda cobre). '
                     'Carregar activity-sync DEPOIS do <script> principal')
    if pos('window.TOTAL_AULAS') < 0:
        warns.append('PERSISTÊNCIA (REGRA 28): falta window.TOTAL_AULAS (barra de progresso global do header)')


def validate(path):
    fails, warns = [], []
    if not os.path.exists(path):
        return [f'arquivo não existe: {path}'], []
    c = open(path, encoding='utf-8').read()
    is_aluno = '/aluno/' in path.replace('\\', '/')
    body = strip_code(c)
    css = get_css(c)
    root = repo_root_for(path)
    is_standalone_slides = bool(re.search(r'-aula\d+\.html$', path)) and 'data-slide=' in c

    # ===== regras herdadas do validar_aula.py =====
    o, cl = body.count('<div'), body.count('</div>')
    if o != cl:
        fails.append(f'<div> DESBALANCEADO: {o} abre / {cl} fecha (diff {o-cl})')
    if c.count('<style') != c.count('</style>'):
        fails.append(f'<style> desbalanceado: {c.count("<style")}/{c.count("</style>")}')
    wc = re.findall(r'\[class\*=', css)
    if wc:
        kinds = sorted(set(re.findall(r'\[class\*=["\']?([^"\'\]]+)', css)))
        fails.append(f'{len(wc)} WILDCARD(s) [class*=] no CSS ({", ".join(kinds)}) — PROIBIDO (força cor errada)')
    if 'data-exercise' in c:
        fails.append('data-exercise presente (REGRA 5: exercícios são HTML manual)')
    emojis = [e for e in re.findall(r'[\U0001F000-\U0001FAFF☀-➿⬀-⯿]', body) if e not in '←→↑↓⇄']
    if emojis:
        warns.append(f'{len(emojis)} possível(is) emoji(s) na tela: {" ".join(sorted(set(emojis))[:8])} (REGRA: SVG)')

    # HEADER EM PORTUGUÊS (REGRA 13). O <p class="subtitle"> e o <title> são TELA: o subtitle
    # aparece no header que o aluno lê (A2+ = ZERO português) e que o professor compartilha no
    # Zoom. "Aula 6 -- ..." é português e passava BATIDO pelo gate de idioma — que (a) só varre
    # o Pre-class do hub, nunca o header do standalone, e (b) caça ACENTO, e "Aula" não tem.
    # Ancora na ESTRUTURA (a classe .subtitle e a tag <title>), não em heurística de acento.
    # O certo é INGLÊS: "Lesson 6 -- ...". O "Aula N" português continua legítimo onde é do
    # PROFESSOR (aba Planejamento, data-teacher) — que NÃO casa este seletor. O padrão
    # \bAula\s+\d (palavra INTEIRA + número) não colide com nenhuma palavra inglesa.
    AULA_HEADER_RE = re.compile(r'\bAula\s+\d')
    sub_m = re.search(r'<p class="subtitle">([^<]*)</p>', c)
    if sub_m and AULA_HEADER_RE.search(sub_m.group(1)):
        fails.append(f'HEADER em português: subtitle "{sub_m.group(1)[:50]}" traz "Aula N" — '
                     f'é TELA (A2+ = zero PT), usar "Lesson N" em inglês (REGRA 13)')
    ttl_m = re.search(r'<title>([^<]*)</title>', c)
    if ttl_m and AULA_HEADER_RE.search(ttl_m.group(1)):
        fails.append(f'HEADER em português: <title> "{ttl_m.group(1)[:60]}" traz "Aula N" — '
                     f'usar "Lesson N" em inglês (REGRA 13)')

    if not is_aluno:
        tabs = set(re.findall(r"switchTab\('(planning|exercises|inclass|complementary)'\)", c))
        miss = {'planning', 'exercises', 'inclass', 'complementary'} - tabs
        if miss:
            fails.append(f'abas faltando: {", ".join(sorted(miss))} (professor tem 4)')
    if 'data-slide=' in c:
        nslide = len(re.findall(r'data-slide="\d+"', c))
        if nslide and nslide < 25:
            warns.append(f'só {nslide} slides (REGRA: >=25 p/ 60min)')
        if not is_aluno and nslide:
            nteacher = len(re.findall(r'data-teacher=', c))
            if nteacher < nslide * 0.8:
                fails.append(f'data-teacher em só {nteacher}/{nslide} slides (ícone T em TODOS)')
            elif nteacher < nslide - 1:
                warns.append(f'data-teacher em {nteacher}/{nslide} (faltam {nslide-nteacher})')
        if nslide and ('id="prevBtn"' not in c or 'id="nextBtn"' not in c):
            fails.append('nav-bar sem prevBtn/nextBtn')
    if re.search(r'onclick="(startLesson|enterSlideMode)[^"]*"[^>]*target="_blank"', c):
        fails.append('card de aula do IN CLASS com target="_blank" (deve abrir slides)')

    # áudio: toda frase tem MP3 no audioMap + no disco
    phrases = set()
    for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", c):
        phrases.add(m.group(1).replace("\\'", "'"))
    for m in re.finditer(r'data-phrase="([^"]+)"', c):
        phrases.add(m.group(1))
    amap = dict(re.findall(r'"((?:[^"\\]|\\.)*)"\s*:\s*"(/audio/[^"]+)"', c))
    amap_norm = {k.replace('\\"', '"').replace("\\'", "'"): v for k, v in amap.items()}
    missing_map = [p for p in phrases if p and not p.startswith('[') and p not in amap_norm
                   and p.rstrip('.') not in amap_norm and (p + '.') not in amap_norm]
    if phrases and missing_map:
        fails.append(f'{len(missing_map)} frase(s) SEM entrada no audioMap (ex: "{missing_map[0][:50]}")')
    if root and amap_norm:
        missing_disk = [v for v in set(amap_norm.values()) if not audio_existe(root, v)]
        if missing_disk:
            fails.append(f'{len(missing_disk)} MP3(s) do audioMap NÃO existem (ex: {sorted(missing_disk)[0]})')

    # integração hub + espelho (standalone de professor)
    m = re.search(r'/professor/(.+)-aula(\d+)\.html$', path.replace('\\', '/'))
    if m and root:
        slug, N = m.group(1), m.group(2)
        if not os.path.exists(os.path.join(root, 'public', 'aluno', f'{slug}-aula{N}.html')):
            fails.append(f'falta o espelho public/aluno/{slug}-aula{N}.html (REGRA 34)')
        hub = os.path.join(root, 'public', 'professor', f'{slug}.html')
        if os.path.exists(hub):
            hc = open(hub, encoding='utf-8').read()
            if f'{slug}-aula{N}.html' not in hc and f'id="ex-lesson-{N}"' not in hc:
                fails.append(f'aula {N} NÃO integrada no hub {slug}.html (aula ÓRFÃ — inserir hub_snippets)')
            if f'id="stamp{N}"' not in hc:
                fails.append(f'falta stamp{N} no hub professor (REGRA 29)')
            # BARRA DE PROGRESSO: totalLessons do loop tem que cobrir TODAS as aulas do hub.
            # Se totalLessons < maior ex-lesson, a barra das aulas acima nunca enche (REGRA 18).
            tl_m = re.search(r'var totalLessons *= *(\d+)', hc)
            ex_ns = [int(x) for x in re.findall(r'id="ex-lesson-(\d+)"', hc)]
            max_ex = max(ex_ns) if ex_ns else 0
            if tl_m and max_ex and int(tl_m.group(1)) < max_ex:
                fails.append(f'BARRA DE PROGRESSO quebrada no hub {slug}.html: var totalLessons='
                             f'{tl_m.group(1)} mas há aulas até ex-lesson-{max_ex} — a barra das aulas '
                             f'> {tl_m.group(1)} nunca enche. Ajustar totalLessons para {max_ex} (REGRA 18)')
            # COMPLEMENTARES da aula no hub (classe de bug do PR #106)
            n_media = len(re.findall(rf'data-media="l{N}-', hc))
            if n_media == 0:
                fails.append(f'aula {N} SEM complementares no hub (nenhum data-media="l{N}-...") — gerar complementary.html e inserir o snippet 3b')
            elif n_media < 3:
                warns.append(f'só {n_media} complementar(es) da aula {N} no hub (padrão do modelo: 3)')
            # LINK obrigatório em CADA complementar (REGRA 17): todo media-card da aula
            # precisa de um <a href="http..."> clicável (série/filme, podcast, vídeo).
            # Card sem link = bug bloqueante (saíram cards sem link em alunos novos).
            comp_i = hc.find('id="tab-complementary"')
            comp_cards = []
            if comp_i >= 0 and n_media > 0:
                comp_seg = hc[comp_i:]
                cards = re.findall(
                    rf'data-media="l{N}-[^"]*".*?(?=<div class="media-card-wrapper"|</div><!-- /tab-complementary -->|$)',
                    comp_seg, re.S)
                comp_cards = cards
                no_link = [c for c in cards if 'href="http' not in c]
                if no_link:
                    fails.append(f'aula {N}: {len(no_link)} de {len(cards)} complementar(es) SEM link '
                                 f'clicável (<a href="http...">) — todo media-card precisa de link (REGRA 17)')
                # LINK PLACEHOLDER de busca (GATE, bloqueante): um card com link do tipo
                # youtube.com/results?search_query=... / google search / bing search NÃO aponta
                # pro episódio/vídeo exato — é o padrão preguiçoso que engana o check acima
                # (tem href="http" mas cai numa busca). Memória links-episodio-real: link vai ao
                # episódio/vídeo EXATO, verificado. Ex.: modelo helen-mendes saiu com 6 desses.
                PLACEHOLDER_LINK = re.compile(
                    r'href="https?://[^"]*'
                    r'(?:/results\?|[?&]search_query=|google\.[a-z.]+/search|bing\.com/search|/search\?q=)',
                    re.I)
                placeholder = [c for c in cards if PLACEHOLDER_LINK.search(c)]
                if placeholder:
                    fails.append(f'aula {N}: {len(placeholder)} complementar(es) com link PLACEHOLDER de '
                                 f'busca (youtube.com/results, search_query=, google/bing search) em vez do '
                                 f'episódio/vídeo DIRETO — trocar pelo link exato verificado (REGRA 17)')
                # LAYOUT media-grid (REGRA 17): os cards da aula DEVEM estar agrupados num
                # <div class="media-grid"> sob o <h4> da aula (2 em cima + 1 embaixo, igual à
                # maria-claudia). Card de aula fora de media-grid = layout em coluna única = FAIL.
                first_card = comp_seg.find(f'data-media="l{N}-')
                if first_card >= 0:
                    head = comp_seg[:first_card]
                    h4_pos = head.rfind('<h4')
                    region = head[h4_pos:] if h4_pos >= 0 else head
                    if 'class="media-grid"' not in region:
                        fails.append(f'aula {N}: complementares FORA de <div class="media-grid"> — '
                                     f'agrupar os cards da aula num media-grid sob o <h4> '
                                     f'(layout 2+1, REGRA 17)')
            # ESTRUTURA mínima do Pre-class (ex-lesson-N do hub)
            bi = hc.find(f'id="ex-lesson-{N}"')
            if bi >= 0:
                bj = hc.find('id="ex-lesson-', bi + 15)
                if bj < 0:
                    bj = hc.find('tab-inclass', bi)
                blk = hc[bi:bj if bj > 0 else len(hc)]
                REQ = [('vocab-card-pc', 6), ('match-row', 4), ('quiz-item', 3), ('fill-blank-item', 3),
                       ('order-container', 1), ('speech-card', 2), ('think-card', 1), ('survival-card', 1)]
                missing = [f'{k} ({blk.count(k)}/{mn})' for k, mn in REQ if blk.count(k) < mn]
                if missing:
                    fails.append(f'Pre-class da aula {N} INCOMPLETO no hub: ' + ', '.join(missing))
            # DOSAGEM + IDIOMA por nível.
            # O nível vem do HTML (student-info do header) e, na falta dele, do config do
            # build. Antes vinha SÓ do config — e sem config o gate inteiro era pulado EM
            # SILÊNCIO (inclusive no próprio MODELO, que não tem config: gate desligado,
            # não gate passando).
            cfg_p = os.path.join(root, '_build', f'{slug}-aula{N}', 'config.json')
            level, lesson_lang = None, 'en'  # 'en' (padrão) | 'es' (espanhol) | ...
            if os.path.exists(cfg_p):
                try:
                    cfg = json.load(open(cfg_p, encoding='utf-8'))
                    level = next((h for h in cfg.get('header', []) if re.match(r'^[ABC]\d', str(h))), None)
                    lesson_lang = cfg.get('lang', 'en')
                except Exception:
                    pass
            level = nivel_do_html(c) or level
            if not level:
                # Nível desconhecido NÃO pode virar buraco: o gate de idioma é BIDIRECIONAL
                # (A0/A1 EXIGE português; A2+ PROÍBE). Sem nível, ele não roda — e "não roda"
                # tem de ser BARULHENTO, nunca um PASS silencioso.
                warns.append(f'IDIOMA: nível CEFR não encontrado (nem no header student-info do HTML, '
                             f'nem no _build/{slug}-aula{N}/config.json) — o gate de idioma da REGRA 13 '
                             f'foi PULADO nesta aula. Declarar o nível para que ele rode.')
            if level:
                    beginner = level[:2] in ('A0', 'A1')
                    if beginner and bi >= 0:
                        # A0/A1: o bilíngue é OBRIGATÓRIO (é o único nível em que PT entra).
                        # O gate é BIDIRECIONAL de propósito: um gate que só PROIBISSE português
                        # estragaria todo material A0/A1, que PRECISA dele — o erro simétrico
                        # exato do que este PR conserta.
                        for need, desc in [('sp-pt', 'survival sem tradução PT (.sp-pt)'),
                                           ('speech-translation', 'pronúncia sem tradução PT (.speech-translation)')]:
                            if need not in blk:
                                fails.append(f'DOSAGEM {level}: Pre-class da aula {N} — {desc}')
                        # matching de A0/A1 = palavra EN <-> TRADUÇÃO PT. Se NENHUMA resposta é PT,
                        # a aula veio no formato de A2+ (definição em inglês) — nível errado.
                        if blk.count('match-row') and not matching_nao_ingles(blk):
                            fails.append(f'DOSAGEM {level}: MATCHING da aula {N} está no formato de A2+ '
                                         f'(palavra EN <-> definição em INGLÊS), mas {level} exige '
                                         f'palavra EN <-> TRADUÇÃO em português (REGRA 13)')
                    elif bi >= 0 and lesson_lang == 'en':
                        # A2+: ZERO português na tela do aluno (REGRA 13 / RULEBOOK).
                        # Esta checagem era INVERTIDA: até 14/07/2026 ela EXIGIA .sp-pt e
                        # .speech-translation em A2 — ou seja, o gate COBRAVA o defeito.
                        # Quem manda é o docs/RULEBOOK-PEDAGOGICO.md: PT só em A0/A1.
                        pt = pt_na_tela(blk)
                        if pt:
                            fails.append(f'IDIOMA {level}: PORTUGUÊS no Pre-class da aula {N} — em A2+ é '
                                         f'ZERO português na tela do aluno (REGRA 13 / RULEBOOK). '
                                         f'Achado: {", ".join(pt[:8])}'
                                         f'{" ..." if len(pt) > 8 else ""}. '
                                         f'(Tradução -> definição em inglês simples; "Dica:" -> "Hint:"; '
                                         f'remover .sp-pt e .speech-translation. PT do PROFESSOR — '
                                         f'aba Planejamento e data-teacher — continua permitido.)')
                        ruins = matching_nao_ingles(blk)
                        if ruins:
                            fails.append(f'IDIOMA {level}: MATCHING em português na aula {N} '
                                         f'({len(ruins)} de {blk.count("match-row")} linhas): '
                                         f'{", ".join(repr(r) for r in ruins[:5])}. Em A2+ o matching é '
                                         f'palavra EN <-> DEFINIÇÃO EM INGLÊS (formato do IN CLASS). '
                                         f'O checkMatch() só compara string (select.value === data-answer): '
                                         f'trocar para inglês custa ZERO mudança de JS.')
                        ptc = pt_na_tela('\n'.join(comp_cards))
                        if ptc:
                            fails.append(f'IDIOMA {level}: PORTUGUÊS nos Complementares da aula {N} — '
                                         f'Complementares são TELA DO ALUNO (REGRA 13). '
                                         f'Achado: {", ".join(ptc[:8])}')
                    if not beginner:
                        si = c.find('<div class="slides-container"')
                        sj = c.find('</div><!-- /slides-container -->')
                        if si >= 0 and sj > si:
                            scr = re.sub(r'\sdata-teacher="(?:[^"\\]|\\.)*"', '', c[si:sj])
                            scr = re.sub(r'<[^>]+>', ' ', re.sub(r'<script\b.*?</script>', '', scr, flags=re.S))
                            if lesson_lang == 'en':
                                # aula de inglês: QUALQUER palavra acentuada na tela = vazamento de PT
                                acc = re.findall(r'\b[\wÀ-ÿ]*[àáâãéêíóôõúüç][\wÀ-ÿ]*\b', scr)
                                low = sorted(set(t for t in acc if t[:1].islower()))
                                PT_SEM_ACENTO = ['rotina', 'trabalho', 'exemplo', 'resposta', 'pergunta',
                                                 'palavra', 'frase', 'ouvir', 'gravar', 'clique', 'escolha', 'voce']
                                low += sorted(set(re.findall(r'\b(?:' + '|'.join(PT_SEM_ACENTO) + r')\b', scr)))
                            else:
                                # idioma-alvo usa acentos (ex.: 'es'): acento é legítimo. Marcar só o que é
                                # IMPOSSÍVEL na ortografia espanhola (ã, õ, ç) + palavras PT inequívocas.
                                low = sorted(set(re.findall(r'\b[\wÀ-ÿ]*[ãõç][\wÀ-ÿ]*\b', scr, re.I)))
                                PT_INEQUIVOCO = ['não', 'nao', 'você', 'voce', 'também', 'tambem',
                                                 'então', 'entao', 'obrigado', 'trabalho', 'rotina']
                                low += sorted(set(re.findall(r'\b(?:' + '|'.join(PT_INEQUIVOCO) + r')\b', scr, re.I)))
                            if low:
                                fails.append(f'DOSAGEM {level}: português na tela IN CLASS fora de data-teacher: {", ".join(low[:6])}')
        else:
            warns.append(f'hub {slug}.html não encontrado — checagem de integração pulada (ok se aluno novo em build)')

    # ===== regras novas do modelo =====
    check_dialogue_voices(c, path, root, fails, warns)
    check_fix_regressions(c, css, is_standalone_slides, fails, warns)
    check_task_before_exposure(c, fails, warns)
    check_handlers_exist(c, fails)
    check_speaktext_escaping(c, fails)
    check_audio_collision(c, fails)
    check_b2_blocks(c, fails, warns)
    check_persistence_wiring(c, path, fails, warns)

    return fails, warns


def main():
    args = []
    for a in sys.argv[1:]:
        args.extend(glob.glob(a) or [a])
    if not args:
        print(__doc__)
        sys.exit(2)
    any_fail = False
    for path in args:
        fails, warns = validate(path)
        tag = 'aluno' if '/aluno/' in path.replace('\\', '/') else 'prof'
        if fails:
            any_fail = True
            print(f'❌ FAIL  {os.path.basename(path)} [{tag}]')
            for f in fails:
                print(f'     ✗ {f}')
        else:
            print(f'✅ PASS  {os.path.basename(path)} [{tag}]')
        for w in warns:
            print(f'     ⚠ {w}')
    print('\n' + ('=== ALGUM ARQUIVO FALHOU — corrigir antes de mergear ===' if any_fail else '=== TODOS PASSARAM ==='))
    sys.exit(1 if any_fail else 0)


if __name__ == '__main__':
    main()
