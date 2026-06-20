#!/usr/bin/env python3
"""build_mock.py — Helen Mendes (aluna mock MODELO) a partir do dialeto Roberto Pires (aula 5).

Gera:
  public/professor/helen-mendes-aula1.html   standalone aula 1 (27 slides)
  public/professor/helen-mendes-aula2.html   standalone aula 2 (27 slides)
  public/professor/helen-mendes.html         hub 4 abas (planning + preclass accordion + inclass menu + complementares)
  public/aluno/helen-mendes.html             espelho aluno (2 abas)
  _build/helen-mendes/audio_manifest.json    frase -> voz -> mp3 (consumido por gen_audio_helen.py)

Correções embutidas (vs. o modelo Roberto):
  1. EXIT usa exitSlideMode() -> volta ao hub #inclass (bug original: só removia a classe)
  2. Handler de Escape fora da tag <script src> (no original ele nunca executa)
  3. Listening = MP3 único com player completo (mpToggle/mpSeek/mpSkip/mpSpeed) — REGRA cumprida
  4. revealError dinâmico (conta .revealed, total real) — original tinha "/5" fixo e dupla contagem
  5. Áudios com prefixo a{N}_/pc_ (sem colisão entre aulas)
  6. contrast-guard.js plugado em todas as páginas
"""
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

# B2 IN-CLASS BLOCKS: reaproveita o render do builder genérico do modelo (única fonte
# de verdade do HTML dos blocos .ic-*). A aula 3 do modelo mistura componentes existentes
# + os blocos B2 novos; os placeholders <!--IC-BLOCKS:chave--> no slides.html são expandidos
# a partir de LESSONS[n]['inclass_blocks']. Aula sem placeholder/inclass_blocks = no-op.
sys.path.insert(0, os.path.join(ROOT, '_build', 'model'))
from build_from_model import render_block  # noqa: E402


def expand_inclass_blocks(slides, blocks_cfg):
    used = set()

    def sub(m):
        key = m.group(1).strip()
        assert key in blocks_cfg, f'placeholder IC-BLOCKS:{key} sem entrada em inclass_blocks'
        used.add(key)
        return '\n'.join(render_block(b) for b in blocks_cfg[key])

    out = re.sub(r'<!--\s*IC-BLOCKS:([^>]+?)\s*-->', sub, slides)
    unused = set(blocks_cfg) - used
    assert not unused, f'inclass_blocks declarados mas sem placeholder no slides.html: {sorted(unused)}'
    return out
PROF = os.path.join(ROOT, 'public', 'professor')
ALUNO = os.path.join(ROOT, 'public', 'aluno')
SLUG = 'helen-mendes'
AUDIO_BASE = f'/audio/{SLUG}/'

SRC_STANDALONE = os.path.join(PROF, 'roberto-pires-aula5.html')
SRC_HUB = os.path.join(PROF, 'roberto-pires.html')
SRC_HUB_ALUNO = os.path.join(ALUNO, 'roberto-pires.html')

COLOR_SWAPS = [
    ('#C2410C', '#BE123C'), ('#c2410c', '#be123c'),
    ('#F97316', '#F43F5E'), ('#f97316', '#f43f5e'),
    ('rgba(194,65,12', 'rgba(190,18,60'),
]

LESSONS = {
    1: dict(
        menu_num='01',
        menu_title='Who Is Helen? First Impressions',
        menu_desc='To be + present simple, summit networking -- 27 slides',
        subtitle='Aula 1 -- Who Is Helen? First Impressions at the Marketing Summit',
        title_tag='Professor View -- Helen Mendes | Aula 1 -- First Impressions',
        phases=['The Summit', 'Packing Words', 'The Code', 'The Summit Floor', 'Practice', 'Your Turn', 'Wrap-Up'],
        listenings=[
            dict(file='a1_listening1.mp3', voice='ellen', text=(
                "Good morning, and welcome to the International Marketing Summit! "
                "We are happy to see you here today. The opening keynote begins at ten o'clock, in the main hall. "
                "Please take your seats a few minutes early. After the keynote, you can visit the brand stands "
                "and meet our international partners. Have a great summit!")),
            dict(file='a1_listening2.mp3', voice='arthur', text=(
                "Hi Helen, this is James — we met at the summit today. It was great to talk to you! "
                "Thank you for your business card. I am calling because I want to plan a meeting about the launch "
                "next week. Is Tuesday good for you? Call me back when you can. Talk soon!")),
        ],
    ),
    2: dict(
        menu_num='02',
        menu_title='My Workday',
        menu_desc='Routines + frequency adverbs, the Tuesday call -- 27 slides',
        subtitle='Aula 2 -- My Workday: Routines, Rhythm, and the Tuesday Call with James',
        title_tag='Professor View -- Helen Mendes | Aula 2 -- My Workday',
        phases=['The Tuesday Call', 'Packing Words', 'The Code', 'The Call', 'Practice', 'Your Turn', 'Wrap-Up'],
        listenings=[
            dict(file='a2_listening1.mp3', voice='ellen', text=(
                "My name is Carla, and I work in marketing too. My day has a clear rhythm. "
                "I always check the social media numbers first — every morning, before everything else. "
                "Then we usually have a short team meeting. I take my break at noon, always with a good coffee. "
                "In the afternoon, I often work on reports. I love my routine!")),
            dict(file='a2_listening2.mp3', voice='arthur', text=(
                "Let me describe a good workday. At eight o'clock, she always checks her inbox and makes a list of tasks. "
                "The most important task is the priority of the day. She usually has meetings in the morning, "
                "and she often works on the campaign in the afternoon. Before a deadline, she sometimes works late. "
                "But she never works on weekends. Weekends are for family.")),
        ],
    ),
    3: dict(
        menu_num='03',
        menu_title='The Mind-Body Reset',
        menu_desc='Modals of advice + B2 reading blocks, wellness at work -- 28 slides',
        subtitle='Aula 3 -- The Mind-Body Reset: Wellness, Balance, and the Language of Advice',
        title_tag='Professor View -- Helen Mendes | Aula 3 -- The Mind-Body Reset',
        phases=['The Reset', 'Words of Wellbeing', 'Read & Think', 'Language of Advice', 'Practice', 'Your Turn', 'Wrap-Up'],
        # MISTURA: componentes existentes (vocab reveal, grammar discovery, dialogue,
        # listening, role-play, survival, comprehension) + blocos B2 NOVOS abaixo.
        inclass_blocks={
            'vocab': [
                {'kind': 'matching', 'title': 'Match each word to its meaning',
                 'words': [['1', 'burnout'], ['2', 'boundary'], ['3', 'recharge'], ['4', 'resilience'],
                           ['5', 'mindful'], ['6', 'downtime'], ['7', 'prioritize'], ['8', 'unwind']],
                 'defs': [['a', 'to rest and get your energy back'],
                          ['b', 'a clear line between work and personal life'],
                          ['c', 'deep exhaustion from long-term stress'],
                          ['d', 'fully present and aware in the moment'],
                          ['e', 'strength to recover quickly from difficulty'],
                          ['f', 'to rank a task as more important than others'],
                          ['g', 'to relax and let go of tension after work'],
                          ['h', 'a short break to rest the mind and body']]},
                {'kind': 'vocabnote',
                 'text': 'Notice the pairs: burnout is the problem; recharge and unwind are the cure. A boundary protects your downtime.'},
            ],
            'reading': [
                {'kind': 'reading', 'rtitle': 'Energy, Not Just Time',
                 'paras': [
                     'For years, productivity advice focused on one thing: time. Plan every hour, fill every gap, and you will get more done. But many high performers who manage their time perfectly still hit a wall. They reach the edge of burnout while their calendars look flawless.',
                     'A newer idea has taken hold: energy is the real resource. You can have hours free and still have nothing left to give. The professionals who last are not the ones who work the longest; they are the ones who recharge on purpose. They set a clear boundary around their downtime and treat rest as part of the job, not a reward for finishing it.',
                     'The practical advice is simple. Take a short, screen-free break every ninety minutes. Prioritize sleep over one more email. And once a week, fully unwind — a walk, a meal with friends, anything that lets the mind reset. Resilience, it turns out, is built in the pauses.'],
                 'source': 'Adapted for class use from public wellbeing-at-work research',
                 'link': 'https://hbr.org/topic/health-and-wellness'},
                {'kind': 'gist', 'prompt': 'What is the best title for this article?',
                 'choices': [
                     ['a', 'Why you should always work longer hours', False],
                     ['b', 'Managing energy matters more than managing time', True],
                     ['c', 'How to delete emails faster', False]]},
            ],
            'tf': [
                {'kind': 'tf', 'items': [
                    ['People with perfect calendars can still reach burnout.', 't',
                     'The article says high performers who manage time well still "hit a wall".'],
                    ['The article says rest is a reward you earn after finishing the work.', 'f',
                     'It says the opposite: treat rest as part of the job, not a reward.'],
                    ['The author recommends a screen-free break every ninety minutes.', 't',
                     'This is given as the first piece of practical advice.']]},
            ],
            'guiding': [
                {'kind': 'guiding', 'items': [
                    'Do you manage your time, your energy, or both? Give an example.',
                    'What is one boundary you could set this week to protect your downtime?',
                    'The article says resilience is "built in the pauses." Do you agree? Why?']},
            ],
            'modals': [
                {'kind': 'modals', 'title': 'How strong is the advice?', 'cards': [
                    ['might want to', 'Softest', 'A gentle suggestion. Easy to refuse: "You might want to try a shorter meeting."'],
                    ['should / ought to', 'Standard', 'Clear, friendly advice. The everyday choice: "You should prioritize sleep."'],
                    ['had better', 'Strongest', 'A warning with a consequence: "You had better rest, or you will burn out."']]},
            ],
            'practice': [
                {'kind': 'scenarios', 'items': [
                    ['Scenario 1', 'A teammate replies to emails at midnight and looks exhausted.'],
                    ['Scenario 2', 'A new hire skips lunch every day to finish reports.'],
                    ['Scenario 3', 'Your manager has not taken a day off in two months.']]},
                {'kind': 'rephrase', 'title': 'Give each person advice — use the modal in brackets',
                 'items': [
                     ['The teammate emailing at midnight', 'had better'],
                     ['The new hire skipping lunch', 'should'],
                     ['The manager with no days off', 'might want to']]},
            ],
            'answerkey': [
                {'kind': 'answer', 'title': 'Reveal model answers',
                 'list': [
                     'You had better stop emailing at midnight, or you will burn out.',
                     'You should take a real lunch break to recharge.',
                     'You might want to book a day off and fully unwind.'],
                 'note': 'Models only — accept any natural answer with the right modal and no "to" after should / had better.'},
            ],
        },
        listenings=[
            dict(file='a3_listening1.mp3', voice='ellen', text=(
                "Welcome back to the show. Today, one simple shift: stop thinking about time, and start thinking about energy. "
                "Time is fixed — you always have twenty-four hours. But energy is a resource you manage. "
                "You can protect it or you can drain it. So here is my first recommendation: take a short, screen-free break every ninety minutes. "
                "Just five minutes. Stand up, breathe, look out a window. You should treat that pause as part of the work, not a reward for it. "
                "Do that for one week, and tell me how your afternoons feel.")),
        ],
    ),
}

ORDER_NARRATIONS = {
    '[order-l1]': dict(file='pc_order_l1.mp3', voice='arthur', text=(
        "James says hello at the summit. Helen introduces herself: her name, her city, her profession. "
        "She talks about her work and the new launch. They exchange business cards. "
        "They say goodbye. It was a pleasure.")),
    '[order-l2]': dict(file='pc_order_l2.mp3', voice='ellen', text=(
        "Helen checks her inbox at eight. The team has a meeting at nine. "
        "She takes a coffee break at noon. She works on the campaign in the afternoon. "
        "She finishes the day and closes her schedule.")),
}

HEADER_INFO = (
    '      <span>A2</span>\n'
    '      <span>S&#227;o Paulo, SP</span>\n'
    '      <span>Diretora Executiva</span>\n'
    '      <span>60 min / Online</span>\n'
)

STAMPS_HTML = (
    '<div class="stamps-row">\n'
    '<div class="stamp" id="stamp1" data-label="First Impressions" style="background-image:url(\'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=200&q=80\')"></div>\n'
    '<div class="stamp" id="stamp2" data-label="My Workday" style="background-image:url(\'https://images.unsplash.com/photo-1497032628192-86f99bcd76bc?w=200&q=80\')"></div>\n'
    '<div class="stamp" id="stamp3" data-label="The Mind-Body Reset" style="background-image:url(\'https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=200&q=80\')"></div>\n'
    '</div>\n'
)

MP_PLAYER_JS = """// ===== LISTENING PLAYER (MP3 unico + controles completos) =====
var mpAudios = {};
function mpGet(id) {
  if (mpAudios[id]) return mpAudios[id];
  var box = document.getElementById(id);
  var a = new Audio(box.dataset.src);
  a.preload = 'metadata';
  mpAudios[id] = a;
  a.addEventListener('loadedmetadata', function() { var t = document.getElementById('time-total-' + id); if (t) t.textContent = mpFmt(a.duration); });
  a.addEventListener('timeupdate', function() {
    var p = document.getElementById('progress-' + id);
    if (p && a.duration) p.style.width = (a.currentTime / a.duration * 100) + '%';
    var c = document.getElementById('time-current-' + id);
    if (c) c.textContent = mpFmt(a.currentTime);
  });
  a.addEventListener('play', function() { mpIcon(id, true); var w = document.getElementById(box.dataset.waveform); if (w) w.classList.remove('waveform-paused'); });
  a.addEventListener('pause', function() { mpIcon(id, false); var w = document.getElementById(box.dataset.waveform); if (w) w.classList.add('waveform-paused'); });
  a.addEventListener('ended', function() {
    mpIcon(id, false);
    var w = document.getElementById(box.dataset.waveform); if (w) w.classList.add('waveform-paused');
    var q = document.getElementById(box.dataset.questions); if (q) q.style.display = 'block';
  });
  return a;
}
function mpFmt(s) { s = Math.max(0, Math.floor(s || 0)); return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); }
function mpIcon(id, playing) {
  var btn = document.getElementById('play-' + id); if (!btn) return;
  btn.querySelector('.lp-icon-play').style.display = playing ? 'none' : '';
  btn.querySelector('.lp-icon-pause').style.display = playing ? '' : 'none';
}
function mpToggle(id) {
  var a = mpGet(id);
  if (a.paused) {
    if (currentAudio) { currentAudio.pause(); currentAudio.currentTime = 0; }
    Object.keys(mpAudios).forEach(function(k) { if (k !== id) mpAudios[k].pause(); });
    a.play();
  } else { a.pause(); }
}
function mpSkip(id, sec) { var a = mpGet(id); a.currentTime = Math.max(0, Math.min(a.duration || 0, a.currentTime + sec)); }
function mpSeek(event, id) {
  var a = mpGet(id); if (!a.duration) return;
  var rect = event.currentTarget.getBoundingClientRect();
  a.currentTime = ((event.clientX - rect.left) / rect.width) * a.duration;
}
function mpSpeed(id, speed, btn) {
  var a = mpGet(id); a.playbackRate = speed;
  document.getElementById(id).querySelectorAll('.lp-speed-btn').forEach(function(b) {
    b.style.background = 'transparent'; b.style.border = '1px solid rgba(255,255,255,.25)'; b.style.color = 'rgba(255,255,255,.7)';
  });
  btn.style.background = 'var(--accent)'; btn.style.border = '1px solid var(--accent)'; btn.style.color = '#fff';
}

"""

REVEAL_ERROR_JS = """function revealError(card) {
  card.classList.toggle('revealed');
  var scope = card.closest('.error-grid') || document;
  var n = scope.querySelectorAll('.error-card.revealed').length;
  var total = scope.querySelectorAll('.error-card').length;
  document.getElementById('errorScore').textContent = n + ' / ' + total + ' errors found';
}
"""


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'  wrote {os.path.relpath(p, ROOT)} ({len(s)//1024} KB)')


def replace_between(s, start, end, new_inner, label=''):
    """Substitui o trecho ENTRE os marcadores (exclusivo), mantendo-os."""
    i = s.index(start, 0)
    j = s.index(end, i + len(start))
    return s[:i + len(start)] + new_inner + s[j:]


def swap_all(s, pairs):
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def snake(text, maxlen=48):
    t = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    t = re.sub(r"[^a-z0-9]+", '_', t.lower()).strip('_')
    return t[:maxlen].rstrip('_')


def extract_phrases(html):
    """(texto, voz_sugerida|None) em ordem de documento; data-voice na mesma linha vence."""
    out = []
    for line in html.split('\n'):
        mv = re.search(r'data-voice="(arthur|ellen)"', line)
        hint = mv.group(1) if mv else None
        for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", line):
            t = m.group(1).replace("\\'", "'")
            if not t.startswith('['):
                out.append((t, hint))
        for m in re.finditer(r'data-phrase="([^"]*)"', line):
            out.append((m.group(1), hint))
    return out


def assign_voices(phrases, prefix):
    """REGRA 7: 1-2 palavras = Arthur; frases alternam Ellen/Arthur; data-voice (diálogo) vence;
    falas em 1a pessoa da Helen = Ellen."""
    entries = {}
    alt = 0
    for text, hint in phrases:
        if text in entries:
            continue
        if hint:
            voice = hint
        elif len(text.split()) <= 2:
            voice = 'arthur'
        elif re.search(r'\bI am Helen\b|\bLet me introduce myself\b', text):
            voice = 'ellen'
        else:
            voice = 'ellen' if alt % 2 == 0 else 'arthur'
            alt += 1
        entries[text] = dict(voice=voice, file=f'{prefix}{snake(text)}.mp3')
    return entries


def audio_map_js(entries, extra=None):
    lines = ['var audioMap = {']
    for text, meta in entries.items():
        lines.append(f'  {json.dumps(text, ensure_ascii=False)}: {json.dumps(AUDIO_BASE + meta["file"])},')
    for key, meta in (extra or {}).items():
        lines.append(f'  {json.dumps(key, ensure_ascii=False)}: {json.dumps(AUDIO_BASE + meta["file"])},')
    lines.append('};')
    return '\n'.join(lines)


def base_swaps(s, n=None):
    s = swap_all(s, COLOR_SWAPS)
    # personagens do dialogo: roberto/agent -> helen/james
    s = s.replace('.dialogue-avatar.roberto', '.dialogue-avatar.helen')
    s = s.replace('.dialogue-bubble.roberto-bubble', '.dialogue-bubble.helen-bubble')
    s = s.replace('.dialogue-avatar.agent', '.dialogue-avatar.james')
    s = s.replace('.dialogue-bubble.agent-bubble', '.dialogue-bubble.james-bubble')
    if n:
        s = s.replace('roberto-pires-aula5', f'{SLUG}-aula{n}')
    s = s.replace('roberto-pires', SLUG)
    s = s.replace('Roberto Pires', 'Helen Mendes')
    s = s.replace('Roberto', 'Helen')
    s = re.sub(r'window\.TOTAL_AULAS=\d+', 'window.TOTAL_AULAS=30', s)
    s = s.replace('Travel English -- 10 Aulas', 'Business English -- 30 Aulas')
    s = s.replace('Travel English — 10 Aulas', 'Business English — 30 Aulas')
    return s


def patch_header(s, subtitle):
    s = re.sub(r'<p class="subtitle">[^<]*</p>', f'<p class="subtitle">{subtitle}</p>', s, count=1)
    s = re.sub(r'<div class="student-info">.*?</div>', '<div class="student-info">\n' + HEADER_INFO + '    </div>', s, count=1, flags=re.S)
    i = s.index('<div class="stamps-row">')
    j = s.index('</div>\n', s.index('stamp', i))
    # fecha no </div> da stamps-row: procura a primeira linha que é só </div> apos os stamps
    m = re.search(r'\n</div>\n', s[i:])
    s = s[:i] + STAMPS_HTML + s[i + m.end() - 1:]
    return s


def inclass_menu_cards():
    cards = []
    for n, L in LESSONS.items():
        cards.append(
            f'    <a href="/professor/{SLUG}-aula{n}.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
            f'      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">{L["menu_num"]}</div>\n'
            f'      <div><div style="font-weight:600;font-size:.95rem">{L["menu_title"]}</div><div style="font-size:.8rem;color:var(--text-dim)">{L["menu_desc"]}</div></div>\n'
            f'    </a>')
    return ('\n  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS -- Selecione a Aula</h3>\n'
            '  <div style="display:flex;flex-direction:column;gap:1rem">\n' + '\n'.join(cards) + '\n  </div>\n</div>\n\n')


def fix_tail_scripts(s):
    broken = re.search(r'<script src="/lib/activity-sync\.js">\s*(document\.addEventListener\(\'keydown\'.*?\);)\s*</script>', s, flags=re.S)
    if broken:
        s = s[:broken.start()] + (
            '<script src="/lib/activity-sync.js"></script>\n<script>\n' + broken.group(1) + '\n</script>'
        ) + s[broken.end():]
    if '/lib/contrast-guard.js' not in s:
        s = s.replace('</body>', '<script src="/lib/contrast-guard.js"></script>\n</body>')
    return s


def build_standalone(n, manifest):
    L = LESSONS[n]
    slides = read(os.path.join(HERE, f'aula{n}-slides.html'))
    if L.get('inclass_blocks'):
        slides = expand_inclass_blocks(slides, L['inclass_blocks'])  # B2 blocks (no-op p/ aulas 1-2)

    # SHELL: aulas 1-2 clonam do dialeto roberto (com as correções embutidas abaixo).
    # Aulas que usam blocos B2 (inclass_blocks) clonam da PRÓPRIA aula 1 do modelo, que
    # JÁ traz CSS/JS dos blocos .ic-* (icPickGist/icRevealTf/icToggleAnswer) + os fixes
    # mais novos (nav-bar flex, oral-model toggle). Assim os blocos novos saem "ligados"
    # e a aula prova que o novo convive com o existente — sem reaplicar swaps do roberto.
    from_model = bool(L.get('inclass_blocks'))
    s = read(os.path.join(PROF, f'{SLUG}-aula1.html')) if from_model else read(SRC_STANDALONE)
    if not from_model:
        s = base_swaps(s, n=n)
    else:
        # shell já é helen-mendes-aula1: só re-aponta o slug do arquivo (links/localStorage)
        s = s.replace(f'{SLUG}-aula1', f'{SLUG}-aula{n}')
    s = re.sub(r'<title>[^<]*</title>', f'<title>{L["title_tag"]}</title>', s, count=1)
    s = patch_header(s, L['subtitle'])

    # phase labels
    labels = '\n' + '\n'.join(
        f'  <span class="phase-label{" current" if i == 0 else ""}" data-phase="{i+1}">{name}</span>'
        for i, name in enumerate(L['phases'])) + '\n'
    s = replace_between(s, '<div class="phase-labels" id="phaseLabels">', '</div>', labels)

    # menu IN CLASS (1 card desta aula)
    card = (
        '\n  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS -- Selecione a Aula</h3>\n'
        '  <div style="display:flex;flex-direction:column;gap:1rem">\n'
        '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode();" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
        f'      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">{L["menu_num"]}</div>\n'
        f'      <div><div style="font-weight:600;font-size:.95rem">{L["menu_title"]}</div><div style="font-size:.8rem;color:var(--text-dim)">{L["menu_desc"]}</div></div>\n'
        '    </div>\n  </div>\n</div>\n\n')
    s = replace_between(s, '<div class="tab-content active" id="tab-inclass">', '<!-- ========== TAB 4', card)

    # slides
    s = replace_between(s, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->', '\n' + slides + '\n')
    # totalSlides bate com a contagem real desta aula (nav/dots/counter)
    actual_slides = len(re.findall(r'data-slide=', slides))
    s = re.sub(r'var totalSlides = \d+', f'var totalSlides = {actual_slides}', s)

    # nav: label da aula (LESSON N no contador da fase). helen-aula1 já tem LESSON 1.
    s = s.replace('>LESSON 5<' if not from_model else '>LESSON 1<', f'>LESSON {n}<')
    if not from_model:
        # correções da JS só fazem sentido no shell antigo do roberto:
        s = s.replace('onclick="document.body.classList.remove(\'slide-mode\')" aria-label="Exit presentation"',
                      'onclick="exitSlideMode()" aria-label="Exit presentation"')
        s = replace_between(s, '// ===== QUICK CHALLENGE =====', '// ===== LISTENING AUDIO =====', '\n')
        s = replace_between(s, '// ===== LISTENING AUDIO =====', 'function stopAllAudio', '\n' + MP_PLAYER_JS)
        s = replace_between(s, 'var errorCount = 0;', '// ===== DIALOGUE LINE-BY-LINE =====', '\n' + REVEAL_ERROR_JS + '\n')

    # audioMap
    entries = assign_voices(extract_phrases(slides), prefix=f'a{n}_')
    s = re.sub(r'var audioMap = \{.*?\};', lambda _: audio_map_js(entries), s, count=1, flags=re.S)

    s = fix_tail_scripts(s)

    for text, meta in entries.items():
        manifest.append(dict(text=text, voice=meta['voice'], file=meta['file']))
    for li in L['listenings']:
        manifest.append(dict(text=li['text'], voice=li['voice'], file=li['file']))

    assert 'roberto' not in s.lower(), f'sobrou referencia a roberto na aula {n}'
    assert 'toggleListening' not in s, 'sobrou listening fake'
    write(os.path.join(PROF, f'{SLUG}-aula{n}.html'), s)

    # espelho ALUNO do standalone (REGRA 34): sem instrucoes de professor, exit volta ao hub do aluno
    a = s.replace('<title>Professor View --', '<title>Aluno --')
    a = a.replace('<span class="prof-badge">Professor View</span>', '<span class="prof-badge">Aluno</span>')
    a = re.sub(r'\sdata-teacher="(?:[^"\\]|\\.)*"', '', a)
    a = a.replace('</style>', '.teacher-t{display:none !important}\n</style>')
    a = a.replace(f"window.location.href = '/professor/{SLUG}.html#inclass'",
                  f"window.location.href = '/aluno/{SLUG}.html#inclass'")
    a = a.replace(f'{SLUG}-aula{n}-professor', f'{SLUG}-aula{n}-aluno')
    write(os.path.join(ALUNO, f'{SLUG}-aula{n}.html'), a)


def build_hub(manifest):
    preclass = read(os.path.join(HERE, 'preclass.html'))
    planning = read(os.path.join(HERE, 'planning.html'))
    complementary = read(os.path.join(HERE, 'complementary.html'))

    entries = assign_voices(extract_phrases(preclass), prefix='pc_')
    amap = audio_map_js(entries, extra=ORDER_NARRATIONS)
    for text, meta in entries.items():
        manifest.append(dict(text=text, voice=meta['voice'], file=meta['file']))
    for key, meta in ORDER_NARRATIONS.items():
        manifest.append(dict(text=meta['text'], voice=meta['voice'], file=meta['file']))

    # ---------- professor ----------
    s = read(SRC_HUB)
    s = base_swaps(s)
    s = re.sub(r'<title>[^<]*</title>', '<title>Professor View -- Helen Mendes | Business English</title>', s, count=1)
    s = patch_header(s, 'Business English para Marketing -- da primeira apresenta&#231;&#227;o &#224; reuni&#227;o com Nova York')
    s = replace_between(s, '<div class="tab-content active" id="tab-planning">', '</div><!-- /tab-planning -->', '\n' + planning + '\n')
    s = replace_between(s, '<div class="tab-content" id="tab-exercises">', '</div><!-- /tab-exercises -->', '\n' + preclass + '\n')
    s = replace_between(s, '<div class="tab-content" id="tab-inclass">', '<!-- ========== TAB 4', inclass_menu_cards())
    s = replace_between(s, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', '\n' + complementary + '\n')
    s = replace_between(s, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->', '\n')
    # hub nao tem slides inline (aulas abrem nos standalones); evita literal data-slide="1" no JS
    s = s.replace("document.querySelector('.slide[data-slide=\"1\"]')", "document.querySelector('.slide')")
    s = re.sub(r'var totalLessons = \d+', 'var totalLessons = 2', s)
    s = re.sub(r'var audioMap = \{.*?\};', lambda _: amap, s, count=1, flags=re.S)
    s = fix_tail_scripts(s)
    assert 'roberto' not in s.lower(), 'sobrou referencia a roberto no hub professor'
    write(os.path.join(PROF, f'{SLUG}.html'), s)

    # ---------- aluno ----------
    a = read(SRC_HUB_ALUNO)
    a = base_swaps(a)
    a = re.sub(r'<title>[^<]*</title>', '<title>Helen Mendes | Business English -- Alumni</title>', a, count=1)
    a = patch_header(a, 'Business English para Marketing -- da primeira apresenta&#231;&#227;o &#224; reuni&#227;o com Nova York')
    a = replace_between(a, '<div class="tab-content active" id="tab-exercises">', '</div><!-- /tab-exercises -->', '\n' + preclass + '\n')
    a = replace_between(a, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', '\n' + complementary + '\n')
    a = re.sub(r'var totalLessons = \d+', 'var totalLessons = 2', a)
    a = re.sub(r'var audioMap = \{.*?\};', lambda _: amap, a, count=1, flags=re.S)
    a = fix_tail_scripts(a)
    assert 'roberto' not in a.lower(), 'sobrou referencia a roberto no hub aluno'
    write(os.path.join(ALUNO, f'{SLUG}.html'), a)


def main():
    # Uso aditivo: `build_mock.py 3` constrói SÓ a aula 3 (não toca aula 1/2 nem o hub).
    # Sem argumentos, rebuilda tudo (comportamento original do mock).
    only = [int(a) for a in sys.argv[1:] if a.isdigit()]
    manifest = []
    print('== standalones ==')
    for n in LESSONS:
        if only and n not in only:
            continue
        build_standalone(n, manifest)
    if not only:
        print('== hub ==')
        build_hub(manifest)
    # dedupe manifest por arquivo
    seen, dedup = set(), []
    for e in manifest:
        if e['file'] in seen:
            continue
        seen.add(e['file'])
        dedup.append(e)
    # build aditivo (só algumas aulas) escreve um manifesto separado pra não apagar o
    # manifesto completo das aulas 1-2 (que já têm áudio no disco).
    mf_name = f'audio_manifest_aula{only[0]}.json' if only else 'audio_manifest.json'
    write(os.path.join(HERE, mf_name), json.dumps(dedup, ensure_ascii=False, indent=1))
    print(f'manifest ({mf_name}): {len(dedup)} audios')


if __name__ == '__main__':
    main()
