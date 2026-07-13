#!/usr/bin/env python3
"""Gerador dos INPUTS do builder para Diogo Leal (aulas conversacionais 11-20).

Le _build/diogo-leal-data/aulaN.json e escreve
_build/diogo-leal-aulaN/{slides.html,preclass.html,complementary.html,config.json}.

NAO substitui o builder: apenas produz os 4 arquivos de entrada, que continuam
passando por _build/model/build_from_model.py. Estrutura identica as aulas 8/9/10
(aprovadas): modelo LEITURA (aula par) e modelo FALA (aula impar), REGRA 29.
"""
import json, random, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))

SPK = ('<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">'
       '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen')

GRADS = ["#1d4ed8,#60a5fa", "#6d28d9,#a78bfa", "#15803d,#4ade80", "#b45309,#f59e0b",
         "#9f1239,#fb7185", "#0d9488,#2dd4bf", "#0e7490,#22d3ee", "#ca8a04,#facc15"]

ICONS = [
    '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    '<polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 014-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 01-4 4H3"/>',
    '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18"/>',
    '<path d="M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"/>',
    '<line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>',
    '<path d="M9 12l2 2 4-4"/><path d="M21 12a9 9 0 11-6.219-8.56"/>',
    '<path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/>',
    '<path d="M12 3v18"/><path d="M5 8h14"/><path d="M5 16h14"/>',
]

GOAL_ICONS = [
    '<path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/>',
    '<path d="M8 3H5a2 2 0 00-2 2v3m18 0V5a2 2 0 00-2-2h-3m0 18h3a2 2 0 002-2v-3M3 16v3a2 2 0 002 2h3"/>',
    '<path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/>',
]

MEDIA_SVG = {
    "Film": '<rect x="2" y="3" width="20" height="14" rx="2"/><polyline points="8 21 16 21"/><line x1="12" y1="17" x2="12" y2="21"/>',
    "Series": '<rect x="2" y="3" width="20" height="14" rx="2"/><polyline points="8 21 16 21"/><line x1="12" y1="17" x2="12" y2="21"/>',
    "Podcast": '<path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/>',
    "YouTube": '<polygon points="5 3 19 12 5 21 5 3"/>',
}

HERO = ("background-image:linear-gradient(rgba(20,20,30,.85),rgba(20,20,30,.92)),url('{img}');"
        "background-size:cover;background-position:center")
DARK = ("background-image:linear-gradient(rgba(20,20,30,.78),rgba(20,20,30,.88)),url('{img}');"
        "background-size:cover;background-position:center")


def head(pair, color=None):
    c = ';color:#fff' if color == 'w' else ''
    return f'{pair[0]} <span class="accent">{pair[1]}</span>'


def listen_btn(text, voice=None, stop=False, style=''):
    v = f' data-voice="{voice}"' if voice else ''
    oc = 'event.stopPropagation();speakText(this.dataset.speak,this)' if stop else 'speakText(this.dataset.speak,this)'
    st = f' style="{style}"' if style else ''
    return f'<button class="audio-btn-sm"{v} data-speak="{text}" onclick="{oc}"{st}>{SPK}</button>'


def phrase_row(html, speak):
    return ('<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;'
            'display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
            f'<p style="font-size:.9rem">{html}</p>{listen_btn(speak)}</div>')


def player(pid, src, qid):
    return f'''
    <div class="mp-player" id="{pid}" data-src="/audio/diogo-leal/{src}" data-questions="{qid}" style="max-width:500px;margin:1.5rem auto 0;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:1.2rem">
      <div class="mp-bar" onclick="mpSeek(event,'{pid}')" style="width:100%;height:6px;background:rgba(255,255,255,.15);border-radius:3px;cursor:pointer;margin-bottom:.8rem"><div class="mp-fill" id="progress-{pid}" style="width:0%;height:100%;background:var(--accent);border-radius:3px;transition:width .1s"></div></div>
      <div class="mp-controls" style="display:flex;align-items:center;justify-content:center;gap:.8rem">
        <button onclick="mpSkip('{pid}',-5)" style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:#fff;border-radius:6px;padding:.4rem .6rem;font-size:.75rem;cursor:pointer">-5s</button>
        <button class="mp-play" id="play-{pid}" onclick="mpToggle('{pid}')" style="background:var(--accent);border:none;color:#fff;border-radius:50%;width:44px;height:44px;font-size:1.2rem;cursor:pointer;display:flex;align-items:center;justify-content:center"><span class="lp-icon-play">&#9654;</span><span class="lp-icon-pause" style="display:none">&#10074;&#10074;</span></button>
        <button onclick="mpSkip('{pid}',5)" style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:#fff;border-radius:6px;padding:.4rem .6rem;font-size:.75rem;cursor:pointer">+5s</button>
        <span class="mp-time" style="color:rgba(255,255,255,.6);font-size:.75rem;min-width:80px"><span id="time-current-{pid}">0:00</span> / <span id="time-total-{pid}">0:00</span></span>
      </div>
      <div class="mp-speed" style="display:flex;gap:.4rem;justify-content:center;margin-top:.6rem">
        <button class="lp-speed-btn" onclick="mpSpeed('{pid}',0.75,this)" style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);color:rgba(255,255,255,.7);border-radius:4px;padding:.2rem .5rem;font-size:.7rem;cursor:pointer">0.75x</button>
        <button class="lp-speed-btn active" onclick="mpSpeed('{pid}',1,this)" style="background:var(--accent);border:1px solid var(--accent);color:#fff;border-radius:4px;padding:.2rem .5rem;font-size:.7rem;cursor:pointer">1x</button>
        <button class="lp-speed-btn" onclick="mpSpeed('{pid}',1.25,this)" style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);color:rgba(255,255,255,.7);border-radius:4px;padding:.2rem .5rem;font-size:.7rem;cursor:pointer">1.25x</button>
      </div>
    </div>'''


def comp_qs(items, qid=None, mw=560):
    idattr = f' id="{qid}"' if qid else ''
    rows = ''.join(f'<div class="comp-q" onclick="revealComp(this)"><div class="q-text">{i+1}. {q}</div>'
                   f'<div class="q-answer">{a}</div></div>' for i, (q, a) in enumerate(items))
    return f'<div class="comp-questions"{idattr} style="max-width:{mw}px;margin:1.2rem auto 0">{rows}</div>'


def chips(words, color='var(--accent)'):
    return ''.join(f'<span style="background:var(--bg-card);border:1px solid {color};border-radius:20px;'
                   f'padding:.4rem .8rem;font-size:.8rem;font-weight:600">{w}</span>' for w in words)


def slide(n, ln, phase, teacher, cls='slide-light', style='', inner_style='', body=''):
    st = f' style="{style}"' if style else ''
    ist = f' style="{inner_style}"' if inner_style else ''
    active = ' active' if n == 1 else ''
    return (f'\n<div class="slide{active} {cls}" data-slide="{n}" data-lesson="{ln}" data-phase="{phase}" '
            f'data-teacher="{teacher}"{st}>\n  <div class="slide-inner"{ist}>{body}\n  </div>\n</div>\n')


def build_slides(d):
    n = d['n']
    ln = n
    T = d['teacher']
    ph = d['phases']
    out = []
    S = lambda *a, **k: out.append(slide(*a, **k))

    # ---------- CH1 ----------
    S(1, ln, 1, T['title'], 'slide-dark', HERO.format(img=d['hero_img']), 'text-align:center', f'''
    <div class="chapter-label">Chapter 1 -- {ph[0]}</div>
    <h1 class="slide-heading" style="font-size:2.5rem">Day {n} -- {d['title_line'][0]} <span class="accent">{d['title_line'][1]}</span></h1>
    <p style="color:rgba(255,255,255,.6);font-size:1.1rem;margin-top:1rem">{d['title_sub']}</p>
    <p style="color:rgba(255,255,255,.4);font-size:.9rem;margin-top:.5rem">Business English -- 60 min</p>''')

    w = d['warmup']
    cb = ''.join(phrase_row(f'"{c["text"]}"', c['speak']) for c in w['callback'])
    S(2, ln, 1, T['warmup'], body=f'''
    <div class="chapter-label">Warm-up</div>
    <h2 class="slide-heading">{head(w['heading'])}</h2>
    <p style="color:var(--text-dim);font-size:1rem;margin-top:1rem;max-width:620px;margin-left:auto;margin-right:auto">{w['intro']}</p>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:560px;margin:1.2rem auto 0">{cb}</div>
    <div style="max-width:600px;margin:1.5rem auto 0;background:var(--accent-dim);border:1px solid var(--accent);border-radius:12px;padding:1.3rem">
      <p style="font-weight:600;font-size:1rem;margin-bottom:.5rem">{w['box_title']}</p>
      <p style="font-size:.95rem;color:var(--text-dim)">{w['box_text']}</p>
    </div>''')

    goals = ''.join(f'''
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;padding:1rem;text-align:center">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5" style="margin-bottom:.5rem">{GOAL_ICONS[i]}</svg>
        <p style="font-weight:700;font-size:.95rem">{g['t']}</p>
        <p style="font-size:.8rem;color:var(--text-dim)">{g['d']}</p>
      </div>''' for i, g in enumerate(d['goal']))
    S(3, ln, 1, T['goal'], body=f'''
    <div class="chapter-label">Today's Goal</div>
    <h2 class="slide-heading">Three Steps <span class="accent">Today</span></h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;max-width:640px;margin:1.5rem auto 0">{goals}
    </div>''')

    # ---------- CH2 vocab ----------
    vc = d['vocab_ch']
    S(4, ln, 2, T['vocab_transition'], 'slide-dark', DARK.format(img=d['vocab_img']), 'text-align:center', f'''
    <div class="chapter-label">Chapter 2 -- {ph[1]}</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{head(vc['heading'])}</h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">{vc['sub']}</p>''')

    def vcard(i, v):
        return f'''
      <div class="vocab-card" onclick="revealVocab(this)" style="cursor:pointer;border:1px solid var(--border);border-radius:12px;overflow:hidden;transition:all .3s">
        <div class="card-icon" style="background:linear-gradient(135deg,{GRADS[i]});padding:1.2rem;text-align:center;position:relative"><svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#fff" stroke-width="1.5">{ICONS[i]}</svg><div class="card-hint" style="color:rgba(255,255,255,.85);font-size:.78rem;margin-top:.5rem">{v['hint']}</div></div>
        <div class="card-body"><div class="card-word">{v['w']}</div><div class="card-def">{v['def']}</div><div class="card-example">"{v['ex']}"</div><div class="card-audio">{listen_btn(v['w'], stop=True)}</div></div>
      </div>'''

    for grid, rng, sl in ((1, range(0, 4), 5), (2, range(4, 8), 6)):
        cards = ''.join(vcard(i, d['vocab'][i]) for i in rng)
        S(sl, ln, 2, T[f'vocab{grid}'], body=f'''
    <div class="chapter-label">Vocabulary</div>
    <h2 class="slide-heading">Words <span class="accent">{'1-4' if grid == 1 else '5-8'}</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="vocabCount{grid}">0 / 4 words revealed</span></p>
    <div class="vocab-grid" id="vocabGrid{grid}" style="display:grid;grid-template-columns:repeat(2,1fr);gap:.8rem;max-width:600px;margin:1rem auto 0">{cards}
    </div>''')

    vk = d['vocab_check']
    S(7, ln, 2, T['vocab_check'], body=f'''
    <div class="chapter-label">Vocabulary Check</div>
    <h2 class="slide-heading">{head(vk['heading'])}</h2>
    <div style="max-width:600px;margin:1.3rem auto 0;background:var(--accent-dim);border:1px solid var(--accent);border-radius:12px;padding:1.4rem">
      <p style="font-size:1rem;font-weight:600;margin-bottom:.6rem">{vk['prompt']}</p>
      <p style="font-size:.9rem;color:var(--text-dim)">{vk['sub']}</p>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center;margin-top:1.2rem;max-width:600px;margin-left:auto;margin-right:auto">
      {''.join(f'<span style="background:var(--bg-card);border:1px solid var(--border);border-radius:20px;padding:.4rem .8rem;font-size:.8rem;font-weight:500">{v["w"].lower()}</span>' for v in d['vocab'])}
    </div>''')

    # ---------- pieces reusable ----------
    def s_listening(num, sl, phase, lid):
        L = d['listenings'][lid]
        qid = f'listening{num}Questions'
        extra = comp_qs(L['comp'], qid, 520) if num == 2 else ''
        body = f'''
    <div class="chapter-label" style="color:rgba(255,255,255,.6)">Listening {num}</div>
    <h2 class="slide-heading" style="color:#fff">{head(L['heading'])}</h2>
    <p style="color:rgba(255,255,255,.5);font-size:.9rem;margin-top:.5rem">{L['lead']}</p>
    {player(f'player{num}', L['file'], qid)}
    {extra}'''
        S(sl, ln, phase, T[f'listening{num}'], 'slide-dark', '', 'text-align:center', body)

    def s_listening1_comp(sl, phase):
        L = d['listenings'][0]
        S(sl, ln, phase, T['listening1_comp'], body=f'''
    <div class="chapter-label">Comprehension</div>
    <h2 class="slide-heading">About Sophia's <span class="accent">Message</span></h2>
    {comp_qs(L['comp'], 'listening1Questions')}
    <p style="font-size:.78rem;color:var(--text-dim);text-align:center;margin-top:.8rem">Answer out loud first. Then click to check.</p>''')

    def s_artefact(sl, phase):
        a = d['artefact']
        badge_bg = {'A': 'var(--accent)', 'B': 'var(--warn)', 'C': 'var(--text-dim)',
                    '&#10003;': 'var(--success)'}
        rows = ''
        for i, (b, txt) in enumerate(a['rows']):
            border = 'border-bottom:1px solid var(--border)' if i < len(a['rows']) - 1 else ''
            rows += (f'<div style="display:flex;align-items:center;gap:.6rem;padding:.55rem 0;{border}">'
                     f'<span style="background:{badge_bg.get(b, "var(--accent)")};color:#fff;width:22px;height:22px;border-radius:50%;'
                     f'display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0">{b}</span>'
                     f'<span style="font-size:.86rem;color:var(--text)">{txt}</span></div>')
        S(sl, ln, phase, T['artefact'], body=f'''
    <div class="chapter-label">Artefact</div>
    <h2 class="slide-heading">{head(a['heading'])}</h2>
    <div style="max-width:450px;margin:1.2rem auto 0;background:#fff;border:1px solid var(--border);border-radius:14px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,.12)">
      <div style="background:var(--accent);padding:1.1rem 1rem;color:#fff;text-align:center">
        <p style="font-size:.72rem;letter-spacing:1px;text-transform:uppercase;color:rgba(255,255,255,.8)">{a['kicker']}</p>
        <p style="font-weight:700;font-size:1.05rem;margin-top:.2rem">{a['title']}</p>
        <p style="font-size:.8rem;color:rgba(255,255,255,.85);margin-top:.2rem">Owner: Diogo Leal</p>
      </div>
      <div style="padding:1rem 1.1rem;text-align:left">
        <p style="font-size:.82rem;color:var(--text-dim);border-bottom:1px solid var(--border);padding-bottom:.5rem">{a['reason']}</p>
        {rows}
        <p style="font-size:.78rem;color:var(--text-dim);border-top:1px solid var(--border);padding-top:.5rem;margin-top:.2rem">{a['footer']}</p>
      </div>
    </div>''')

    def s_grammar(sl, phase):
        g = d['grammar']
        lines = ''.join(phrase_row(x['html'], x['speak']) for x in g['discovery'])
        S(sl, ln, phase, T['grammar'], body=f'''
    <div class="chapter-label">Grammar Discovery</div>
    <h2 class="slide-heading">Listen and <span class="accent">Notice</span></h2>
    <p style="font-size:.88rem;color:var(--text-dim);text-align:center;margin-top:.5rem">{g['prompt']}</p>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:640px;margin:1rem auto 0">{lines}</div>''')

    def s_rule(sl, phase):
        g = d['grammar']
        rows = ''
        for i, (mv, st, ex) in enumerate(g['rows']):
            bg = 'background:var(--bg-elevated);' if i % 2 else ''
            bd = 'border-bottom:1px solid var(--border)' if i < len(g['rows']) - 1 else ''
            rows += f'<tr style="{bg}{bd}"><td style="padding:.5rem">{mv}</td><td style="padding:.5rem">{st}</td><td style="padding:.5rem">{ex}</td></tr>'
        S(sl, ln, phase, T['rule'], body=f'''
    <div class="chapter-label">Grammar Rule</div>
    <h2 class="slide-heading">{head(g['rule_heading'])}</h2>
    <button class="primary-btn" style="margin:1rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer" onclick="var t=document.getElementById('grammarTable');t.style.display=(t.style.display==='none'||!t.style.display)?'block':'none'">Reveal the Rule</button>
    <div id="grammarTable" style="display:none;max-width:660px;margin:1rem auto 0;overflow-x:auto;animation:fadeIn .4s ease">
      <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.6rem;text-align:left">Move</th><th style="padding:.6rem;text-align:left">Structure</th><th style="padding:.6rem;text-align:left">Example</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:8px;padding:.8rem;margin-top:.8rem">
        <p style="font-size:.82rem;color:var(--text-mid)">{g['note']}</p>
      </div>
    </div>''')

    def s_mistake(sl, phase):
        g = d['grammar']
        items = ''
        for wrong, right in g['mistakes']:
            items += ('<div class="mistake-item mistake-wrong"><div class="mistake-icon"><svg viewBox="0 0 24 24" style="stroke:#dc2626;fill:none">'
                      '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>'
                      f'<span>"{wrong}"</span></div>'
                      '<div class="mistake-item mistake-right"><div class="mistake-icon"><svg viewBox="0 0 24 24" style="stroke:#15803d;fill:none">'
                      '<polyline points="20 6 9 17 4 12"/></svg></div>'
                      f'<span>"{right}"</span></div>')
        S(sl, ln, phase, T['mistake'], body=f'''
    <div class="chapter-label">Common Mistake</div>
    <h2 class="slide-heading">Watch <span class="accent">Out</span></h2>
    <div class="mistake-card">{items}</div>
    <p style="font-size:.82rem;color:var(--text-dim);text-align:center;margin-top:1rem;max-width:540px;margin-left:auto;margin-right:auto">{g['mistake_note']}</p>''')

    def s_bank(sl, phase):
        b = d['bank']
        S(sl, ln, phase, T['bank'], body=f'''
    <div class="chapter-label">Useful Language</div>
    <h2 class="slide-heading">{head(b['heading'])}</h2>
    <p style="font-size:.88rem;color:var(--text-dim);text-align:center;margin-top:.4rem">{b['sub']}</p>
    <!--IC-BLOCKS:bank-->''')

    def s_dialogue(sl, phase):
        dg = d['dialogue']
        lines = ''
        for i, L in enumerate(dg['lines']):
            is_d = L['s'] == 'diogo'
            voice = 'arthur' if is_d else 'ellen'
            av_bg = '#4F46E5' if is_d else '#B7950B'
            letter = 'D' if is_d else dg.get('other_letter', 'S')
            bub = ('background:rgba(79,70,229,.25);border:1px solid rgba(79,70,229,.4)' if is_d
                   else 'background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15)')
            vis = ' visible' if i == 0 else ''
            lines += f'''
      <div class="dialogue-line{vis}" data-line="{i+1}" data-voice="{voice}">
        <div class="dialogue-avatar {'diogo' if is_d else 'sophia'}" style="background:{av_bg};width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:.85rem;flex-shrink:0">{letter}</div>
        <div class="dialogue-bubble {'diogo-bubble' if is_d else 'sophia-bubble'}" style="{bub};border-radius:10px;padding:.7rem;flex:1">
          <p style="font-size:.88rem;color:#fff">"{L['html']}"</p>
          {listen_btn(L['speak'], voice=voice, stop=True, style='margin-top:.4rem')}
        </div>
      </div>'''
        S(sl, ln, phase, T['dialogue'], 'slide-dark', body=f'''
    <div class="chapter-label">Dialogue</div>
    <h2 class="slide-heading" style="color:#fff">{head(dg['heading'])}</h2>
    <div class="dialogue-box" id="dialogue1" style="max-width:560px;margin:1rem auto 0;max-height:340px;overflow-y:auto">{lines}
    </div>
    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin:1rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Next Line</button>''')

    def s_dialogue_comp(sl, phase):
        dg = d['dialogue']
        S(sl, ln, phase, T['dialogue_comp'], body=f'''
    <div class="chapter-label">Dialogue Review</div>
    <h2 class="slide-heading">About <span class="accent">{dg.get('other_name', 'Sophia')}</span></h2>
    {comp_qs(dg['comp'])}''')

    def s_quickfire(sl, phase):
        S(sl, ln, phase, T['quickfire'], body='''
    <div class="chapter-label">Quick Fire</div>
    <h2 class="slide-heading">Answer <span class="accent">Now</span></h2>
    <!--IC-BLOCKS:quickfire-->''')

    def s_rp_guided(sl, phase):
        r = d['roleplays']['guided']
        S(sl, ln, phase, T['rp_guided'], body=f'''
    <div class="chapter-label">Your Turn -- Guided</div>
    <h2 class="slide-heading">{head(r['heading'])}</h2>
    <div style="max-width:560px;margin:1.2rem auto 0;background:linear-gradient(135deg,rgba(79,70,229,.12),rgba(129,140,248,.06));border:1px solid var(--accent);border-radius:14px;padding:1.4rem">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:.8rem">
        <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="var(--accent)" stroke-width="1.5" style="flex-shrink:0"><path d="M14 9V5a3 3 0 00-3-3l-4 9v11h11.28a2 2 0 002-1.7l1.38-9a2 2 0 00-2-2.3zM7 22H4a2 2 0 01-2-2v-7a2 2 0 012-2h3"/></svg>
        <p style="font-weight:700;font-size:1rem">{r['prompt']}</p>
      </div>
      <p style="font-size:.9rem;color:var(--text-mid)">{r['sub']}</p>
      <div style="display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.9rem">{chips(r['chips'])}</div>
    </div>''')

    def s_rp_semi(sl, phase):
        r = d['roleplays']['semi']
        S(sl, ln, phase, T['rp_semi'], body=f'''
    <div class="chapter-label">Your Turn -- Semi-free</div>
    <h2 class="slide-heading">{head(r['heading'])}</h2>
    <div style="max-width:560px;margin:1.2rem auto 0;background:linear-gradient(135deg,rgba(183,149,11,.14),rgba(250,204,21,.06));border:1px solid var(--warn);border-radius:14px;padding:1.4rem">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:.8rem">
        <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="var(--warn)" stroke-width="1.5" style="flex-shrink:0"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>
        <p style="font-weight:700;font-size:1rem">"{r['quote']}"</p>
      </div>
      <p style="font-size:.9rem;color:var(--text-mid)">{r['sub']}</p>
      <div style="display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.9rem">{chips(r['chips'], 'var(--warn)')}</div>
    </div>''')

    def s_rp_free(sl, phase):
        r = d['roleplays']['free']
        S(sl, ln, phase, T['rp_free'], body=f'''
    <div class="chapter-label">Your Turn -- Free</div>
    <h2 class="slide-heading">{head(r['heading'])}</h2>
    <div style="max-width:560px;margin:1.2rem auto 0;background:linear-gradient(135deg,rgba(21,128,61,.12),rgba(74,222,128,.06));border:1px solid var(--success);border-radius:14px;padding:1.5rem;text-align:center">
      <svg viewBox="0 0 24 24" width="36" height="36" fill="none" stroke="var(--success)" stroke-width="1.5" style="margin-bottom:.6rem"><path d="M8 3H5a2 2 0 00-2 2v3m18 0V5a2 2 0 00-2-2h-3m0 18h3a2 2 0 002-2v-3M3 16v3a2 2 0 002 2h3"/><circle cx="12" cy="12" r="3"/></svg>
      <p style="font-weight:700;font-size:1.05rem;margin-bottom:.5rem">{r['headline']}</p>
      <p style="font-size:.92rem;color:var(--text-mid)">{r['sub']}</p>
    </div>''')

    def s_pressure(sl, phase):
        S(sl, ln, phase, T['pressure'], body='''
    <div class="chapter-label">Under Pressure</div>
    <h2 class="slide-heading">Three Hard <span class="accent">Questions</span></h2>
    <!--IC-BLOCKS:pressure-->''')

    def s_survival(sl, phase):
        rows = ''
        for i, s in enumerate(d['survival']):
            rows += ('<div style="background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:.8rem;'
                     'display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
                     '<div style="display:flex;align-items:center;gap:.6rem">'
                     f'<span style="background:var(--accent);color:#fff;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;'
                     f'justify-content:center;font-weight:700;font-size:.75rem;flex-shrink:0">{i+1}</span>'
                     f'<p style="font-size:.9rem;color:#fff">"{s["en"]}"</p></div>{listen_btn(s["en"])}</div>')
        S(sl, ln, phase, T['survival'], 'slide-dark', body=f'''
    <div class="chapter-label" style="color:rgba(255,255,255,.6)">Survival Card</div>
    <h2 class="slide-heading" style="color:#fff">{head(d['survival_heading'])}</h2>
    <div style="display:flex;flex-direction:column;gap:.6rem;max-width:640px;margin:1.2rem auto 0">{rows}</div>''')

    def s_learned(sl, phase):
        items = ''.join('<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">'
                        '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="#fff" stroke-width="3">'
                        f'<polyline points="20 6 9 17 4 12"/></svg></div><span>{c}</span></div>' for c in d['checks'])
        S(sl, ln, phase, T['learned'], body=f'''
    <div class="chapter-label">Wrap-up</div>
    <h2 class="slide-heading">What I <span class="accent">Learned</span></h2>
    <div class="check-grid" data-lesson="{ln}" style="display:flex;flex-direction:column;gap:.5rem;max-width:560px;margin:1.2rem auto 0">{items}
    </div>''')

    def s_closing(sl, phase):
        c = d['closing']
        S(sl, ln, phase, T['closing'], 'slide-dark', HERO.format(img=d['closing_img']), 'text-align:center', f'''
    <div class="chapter-label">Complete</div>
    <h1 class="slide-heading" style="font-size:2.2rem">Day {n} -- <span class="accent">Complete</span></h1>
    <p style="color:rgba(255,255,255,.65);font-size:1rem;margin-top:1rem">{c['line']}</p>
    <div style="max-width:460px;margin:1.5rem auto 0;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:12px;padding:1.2rem">
      <p style="font-size:.8rem;letter-spacing:1px;text-transform:uppercase;color:rgba(255,255,255,.5)">Next class</p>
      <p style="font-weight:700;font-size:1.05rem;color:#fff;margin-top:.3rem">{c['next_title']}</p>
      <p style="font-size:.88rem;color:rgba(255,255,255,.6);margin-top:.3rem">{c['next_desc']}</p>
    </div>''')

    def s_chapter(sl, phase, idx, heading, sub, img, teacher):
        S(sl, ln, phase, teacher, 'slide-dark', DARK.format(img=img), 'text-align:center', f'''
    <div class="chapter-label">Chapter {idx} -- {ph[idx-1]}</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{head(heading)}</h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">{sub}</p>''')

    if d['model'] == 'reading':
        r = d['reading']
        s_chapter(8, 3, 3, r['ch_heading'], r['ch_sub'], d['ch3_img'], T['ch3'])
        S(9, ln, 3, T['reading'], body=f'''
    <div class="chapter-label">Reading</div>
    <h2 class="slide-heading">{head(r['heading'])}</h2>
    <!--IC-BLOCKS:reading-->''')
        S(10, ln, 3, T['tf'], body='''
    <div class="chapter-label">Check</div>
    <h2 class="slide-heading">True or <span class="accent">False?</span></h2>
    <!--IC-BLOCKS:tf-->''')
        s_bank(11, 3)
        s_grammar(12, 4); s_rule(13, 4); s_mistake(14, 4)
        s_chapter(15, 5, 5, d['ch5_heading'], d['ch5_sub'], d['ch5_img'], T['ch5'])
        s_listening(1, 16, 5, 0); s_listening1_comp(17, 5); s_artefact(18, 5)
        s_dialogue(19, 5); s_dialogue_comp(20, 5); s_listening(2, 21, 5, 1)
        s_chapter(22, 6, 6, d['ch6_heading'], d['ch6_sub'], d['ch6_img'], T['ch6'])
        s_quickfire(23, 6); s_rp_guided(24, 6); s_rp_semi(25, 6); s_rp_free(26, 6); s_pressure(27, 6)
        s_survival(28, 7); s_learned(29, 7); s_closing(30, 7)
    else:
        s_chapter(8, 3, 3, d['ch3_heading'], d['ch3_sub'], d['ch3_img'], T['ch3'])
        s_listening(1, 9, 3, 0); s_listening1_comp(10, 3); s_artefact(11, 3)
        s_grammar(12, 4); s_rule(13, 4); s_mistake(14, 4); s_bank(15, 4)
        s_chapter(16, 5, 5, d['ch5_heading'], d['ch5_sub'], d['ch5_img'], T['ch5'])
        s_dialogue(17, 5); s_dialogue_comp(18, 5); s_listening(2, 19, 5, 1)
        S(20, ln, 5, T['scenarios'], body=f'''
    <div class="chapter-label">Say It</div>
    <h2 class="slide-heading">{head(d['scenarios_heading'])}</h2>
    <p style="font-size:.88rem;color:var(--text-dim);text-align:center;margin-top:.4rem">{d['scenarios_sub']}</p>
    <!--IC-BLOCKS:scenarios-->''')
        s_chapter(21, 6, 6, d['ch6_heading'], d['ch6_sub'], d['ch6_img'], T['ch6'])
        s_quickfire(22, 6); s_rp_guided(23, 6); s_rp_semi(24, 6); s_rp_free(25, 6); s_pressure(26, 6)
        s_survival(27, 7); s_learned(28, 7); s_closing(29, 7)

    return ''.join(out)


def build_preclass(d):
    n = d['n']
    pc = d['preclass']
    vocab = d['vocab']

    cards = ''.join(f'''<div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'''
                    f'''<span class="vocab-card-word">{v['w']}</span><span class="vocab-card-dot"> -- </span>'''
                    f'''<span class="vocab-card-def">{v['def_pc']}</span></div>'''
                    f'''<div class="vocab-card-example">"{v['ex']}" ({v['pt']})</div></div>'''
                    f'''<button class="audio-btn" data-speak="{v['w']}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>'''
                    for v in vocab)

    pts = [v['pt_short'] for v in vocab]
    rnd = random.Random(n * 7 + 3)
    opts = pts[:]
    for _ in range(50):
        rnd.shuffle(opts)
        if all(opts[i] != pts[i] for i in range(len(pts))):
            break
    optlist = ''.join(f'<option value="{o}">{o}</option>' for o in opts)
    rows = ''.join(
        f'<div class="match-row" data-answer="{v["pt_short"]}"><span class="match-word" style="flex:0 0 130px">{v["w"]}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)"><option value="">Selecione...</option>{optlist}</select></div>'
        for v in vocab)

    def quiz(items):
        out = ''
        for i, (q, opts_) in enumerate(items):
            o = ''.join(f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{"true" if ok else "false"}">'
                        f'<span class="option-letter">{"ABC"[j]}</span> {t}</div>' for j, (t, ok) in enumerate(opts_))
            out += f'<div class="quiz-item"><div class="quiz-question">{i+1}. {q}</div><div class="quiz-options">{o}</div></div>'
        return out

    tip_rows = ''
    for i, row in enumerate(pc['tip_rows']):
        bg = 'background:var(--bg-elevated);' if i % 2 else ''
        tip_rows += (f'<tr style="{bg}border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">{row[0]}</td>'
                     f'<td style="padding:.6rem">{row[1]}</td><td style="padding:.6rem">{row[2]}</td></tr>')
    tip_rows += ('<tr><td style="padding:.6rem;font-weight:600">Ponto-chave / Key point</td>'
                 f'<td style="padding:.6rem" colspan="2">{pc["tip_key"]}</td></tr>')

    blanks = ''.join(
        f'<div class="fill-blank-item"><div class="fill-blank-sentence">{b["pre"]}'
        f'<input class="blank-input" data-answer="{b["answer"]}" data-hint="{b["hint"]}" data-phrase="{b["phrase"]}" placeholder="___">'
        f'{b["post"]}</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
        f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
        for b in pc['blanks'])

    order_items = ''.join(
        f'<div class="order-item" draggable="true" data-order="{o}" onclick="selectOrderItem(this,\'order-l{n}\')">'
        f'<span class="order-num">?</span><span class="order-text">{t}</span>'
        f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l{n}\')">&#9650;</button>'
        f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l{n}\')">&#9660;</button></span></div>'
        for o, t in d['order_audio']['items'])

    speech = ''.join(f'''
      <div class="speech-card" data-phrase="{s['en']}">
        <div class="speech-phrase">{s['en']}</div>
        <div class="speech-translation">{s['pt']}</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>''' for s in d['survival'])

    think = ''.join(f'''
      <div class="think-card">
        <div class="think-question">{t}</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-{n}{'' if i == 0 else 'b'}"></div>
      </div>''' for i, t in enumerate(pc['think']))

    surv = ''.join(f'<div class="survival-phrase"><span class="sp-num">{i+1}</span><span class="sp-en">{s["en"]}</span>'
                   f'<span class="sp-pt">{s["pt"]}</span>'
                   f'<button class="btn btn-listen" data-speak="{s["en"]}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>'
                   for i, s in enumerate(d['survival']))

    return f'''<div class="lesson-card" id="ex-lesson-{n}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('{d['hero_img'].replace('?w=1400','?w=600')}')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula {n} -- Pre-class</div>
      <h3>{d['menu_title']}</h3>
      <div class="lesson-desc">{pc['desc']} New vocabulary: {', '.join(v['w'].lower() for v in vocab)}.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="{n}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="{n}">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Say it out loud after the audio.</p>
      <div class="vocab-cards">{cards}</div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with its translation.</p>
      <div class="match-grid" id="match-l{n}">{rows}</div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l{n}')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>{pc['context']}</p>
      </div>
      {quiz(pc['quiz_ctx'])}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- {pc['tip_title']}</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">{pc['tip_sub']}</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Move</th><th style="padding:.7rem;text-align:left">Estrutura / Structure</th><th style="padding:.7rem;text-align:left">Exemplo / Example</th></tr></thead>
        <tbody>{tip_rows}</tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence, then tap Listen and say it out loud.</p>
      {blanks}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: {pc['order_title']}</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the events in the correct order.</p>
      <button class="btn btn-listen" data-speak="[order-l{n}]" onclick="speakText(this.dataset.speak,this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l{n}">{order_items}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l{n}')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{pc['speech_intro']}</p>{speech}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best response for each situation at work.</p>
      {quiz(pc['quiz_sit'])}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Two recordings. Speak first, do not write. This is the exercise that matters most this week.</p>{think}
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson {n}</h4>
      {surv}
    </div>

  </div>
</div>
'''


def build_complementary(d):
    out = []
    for c in d['complementary']:
        svg = MEDIA_SVG[c['type']]
        out.append(f'''<div class="media-card-wrapper" data-media="l{d['n']}-{c['slot']}">
  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
  <div class="media-card">
    <div class="media-thumb"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="var(--accent)" stroke-width="1.5">{svg}</svg></div>
    <div class="media-info">
      <div class="media-type">{c['type']}</div>
      <h5><a href="{c['url']}" target="_blank" rel="noopener">{c['title']}</a></h5>
      <p>{c['desc']}</p>
      <p class="media-tip">{c['tip']}</p>
    </div>
  </div>
</div>''')
    return '\n'.join(out) + '\n'


STAMPS = [
    (1, "Oracle", "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=200&q=80"),
    (2, "Meetings", "https://images.unsplash.com/photo-1552664730-d307ca884978?w=200&q=80"),
    (3, "Present", "https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=200&q=80"),
    (4, "Writing", "https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=200&q=80"),
    (5, "Networking", "https://images.unsplash.com/photo-1543269865-cbf427effbad?w=200&q=80"),
    (6, "Mastery", "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=200&q=80"),
    (7, "Kickoff", "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=200&q=80"),
    (8, "Status", "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=200&q=80"),
    (9, "Bad News", "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=200&q=80"),
    (10, "Buying Time", "https://images.unsplash.com/photo-1556157382-97eda2d62296?w=200&q=80"),
]


def build_config(d, nslides):
    n = d['n']
    stamps = [{"id": i, "label": l, "img": img} for i, l, img in STAMPS if i <= n]
    for k in range(11, n + 1):
        prev = json.load(open(f'{ROOT}/diogo-leal-data/aula{k}.json'))
        stamps.append({"id": k, "label": prev['stamp_label'], "img": prev['stamp_img']})
    blocks = {}
    if d['model'] == 'reading':
        r = d['reading']
        blocks['reading'] = [
            {"kind": "reading", "rtitle": r['rtitle'], "paras": r['paras']},
            {"kind": "gist", "prompt": r['gist']['prompt'],
             "choices": [[c[0], c[1], c[2]] for c in r['gist']['choices']]},
        ]
        blocks['tf'] = [{"kind": "tf", "items": [[t[0], t[1], t[2]] for t in r['tf']]}]
    else:
        blocks['scenarios'] = [{"kind": "scenarios", "items": [[s[0], s[1]] for s in d['scenarios']]}]
    blocks['bank'] = [{"kind": "bank", "label": d['bank']['label'], "items": d['bank']['items']}]
    blocks['quickfire'] = [{"kind": "quickfire", "items": d['quickfire']}]
    blocks['pressure'] = [
        {"kind": "questions", "title": "Answer live", "ordered": True, "items": d['pressure']['items']},
        {"kind": "followup", "text": d['pressure']['followup']},
    ]
    if d['model'] == 'reading':
        order = ["reading", "tf", "bank", "quickfire", "pressure"]
    else:
        order = ["bank", "scenarios", "quickfire", "pressure"]
    blocks = {k: blocks[k] for k in order}

    return {
        "slug": "diogo-leal", "student_name": "Diogo Leal", "first_name": "Diogo", "gender": "m",
        "program": "Business English Executivo", "total_aulas": 36,
        "palette": {"accent": "#4F46E5", "accent_light": "#818CF8"},
        "header": ["A2+ (Pre-Intermediate)", "S&#227;o Paulo, SP", "IT Project Manager / Oracle",
                   "60 min / Presencial / 1x semana"],
        "characters": {"diogo": "arthur", "sophia": "ellen"},
        "stamps": stamps,
        "lesson": {
            "n": n, "menu_num": f"{n:02d}",
            "menu_title": d['menu_title'],
            "menu_desc": f"{d['menu_desc']} -- {nslides} slides",
            "subtitle": f"Aula {n} -- {d['menu_title']}",
            "title_tag": f"Professor View -- Diogo Leal | Aula {n} -- {d['title_line'][0]} {d['title_line'][1]}",
            "phases": d['phases'],
            "plan_row": d['plan_row'],
            "inclass_blocks": blocks,
            "listenings": [{"file": L['file'], "voice": L['voice'], "text": L['text']} for L in d['listenings']],
            "extra_audio": [{"key": f"[order-l{n}]", "file": f"a{n}_order.mp3",
                             "voice": d['order_audio'].get('voice', 'ellen'), "text": d['order_audio']['text']}],
        },
        "hub": "snippets",
    }


def main():
    n = int(sys.argv[1])
    d = json.load(open(f'{ROOT}/diogo-leal-data/aula{n}.json'))
    assert d['n'] == n
    assert d['model'] == ('reading' if n % 2 == 0 else 'speech'), 'REGRA 29: par=leitura, impar=fala'
    outdir = f'{ROOT}/diogo-leal-aula{n}'
    os.makedirs(outdir, exist_ok=True)
    slides = build_slides(d)
    nslides = slides.count('data-slide="')
    open(f'{outdir}/slides.html', 'w').write(slides)
    open(f'{outdir}/preclass.html', 'w').write(build_preclass(d))
    open(f'{outdir}/complementary.html', 'w').write(build_complementary(d))
    cfg = build_config(d, nslides)
    json.dump(cfg, open(f'{outdir}/config.json', 'w'), indent=2, ensure_ascii=False)
    print(f'aula {n}: {nslides} slides, {len(d["vocab"])} vocab, modelo {d["model"]} -> {outdir}')


if __name__ == '__main__':
    main()
