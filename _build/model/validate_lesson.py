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

USO (da raiz do repo):
  python3 _build/model/validate_lesson.py public/professor/{slug}-aula{N}.html [mais.html ...]
Exit code 1 se algum arquivo falhar.
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VOICES = json.load(open(os.path.join(HERE, 'voices.json'), encoding='utf-8'))

# funções nativas/inline aceitas em handlers sem definição no arquivo
BUILTIN_OK = {'event', 'window', 'document', 'this', 'location', 'localStorage', 'alert', 'confirm'}


def strip_code(c):
    c = re.sub(r'<script\b.*?</script>', '', c, flags=re.S | re.I)
    c = re.sub(r'<style\b.*?</style>', '', c, flags=re.S | re.I)
    c = re.sub(r'<!--.*?-->', '', c, flags=re.S)
    return c


def get_css(c):
    css = '\n'.join(re.findall(r'<style\b[^>]*>(.*?)</style>', c, flags=re.S | re.I))
    return re.sub(r'/\*.*?\*/', '', css, flags=re.S)


def repo_root_for(path):
    p = os.path.abspath(path)
    while p != '/' and not os.path.isdir(os.path.join(p, 'public', 'audio')):
        p = os.path.dirname(p)
    return p if os.path.isdir(os.path.join(p, 'public', 'audio')) else None


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
        missing_disk = [v for v in set(amap_norm.values()) if not os.path.exists(os.path.join(root, 'public' + v))]
        if missing_disk:
            fails.append(f'{len(missing_disk)} MP3(s) do audioMap NÃO existem no disco (ex: {sorted(missing_disk)[0]})')

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
        else:
            warns.append(f'hub {slug}.html não encontrado — checagem de integração pulada (ok se aluno novo em build)')

    # ===== regras novas do modelo =====
    check_dialogue_voices(c, path, root, fails, warns)
    check_fix_regressions(c, css, is_standalone_slides, fails, warns)
    check_handlers_exist(c, fails)

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
