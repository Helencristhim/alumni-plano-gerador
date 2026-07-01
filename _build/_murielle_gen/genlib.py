# -*- coding: utf-8 -*-
"""Gerador de aula (slides IN CLASS + Pre-class + Complementares) para Murielle Xavier.
Reproduz EXATAMENTE o markup da aula 14 (template validado), parametrizado por um dict D.
Escreve slides.html / preclass.html / complementary.html em _build/murielle-xavier-aula{N}/.
Depois: build_from_model.py -> gen_audio.py -> insert_hub.py (fluxo normal)."""
import os
import random

ACCENT_RGB = "134,25,143"  # #86198F fixo
LISTEN_SVG = ('<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" '
              'stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
              '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')
LISTEN_SVG12 = LISTEN_SVG.replace('width="14" height="14"', 'width="12" height="12"')

# 12 icones (gradiente, svg 28x28) — genericos (Lucide), reusados em toda aula
ICONS = [
 ("#7c3aed,#a78bfa", '<path d="M18 11.5V9a1.5 1.5 0 00-3 0V3.5a1.5 1.5 0 00-3 0V8"/><path d="M12 8V4.5a1.5 1.5 0 00-3 0V12"/><path d="M9 12v-1.5a1.5 1.5 0 00-3 0V15a6 6 0 006 6h1a6 6 0 006-6v-3.5"/>'),
 ("#1d4ed8,#60a5fa", '<path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 000-7.78z"/>'),
 ("#0891b2,#22d3ee", '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/>'),
 ("#059669,#34d399", '<path d="M12 2l2.4 7.4H22l-6 4.4 2.3 7.2L12 16.6 5.7 21l2.3-7.2-6-4.4h7.6z"/>'),
 ("#c026d3,#e879f9", '<path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>'),
 ("#d97706,#fbbf24", '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>'),
 ("#0369a1,#38bdf8", '<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>'),
 ("#0d9488,#2dd4bf", '<path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>'),
 ("#ea580c,#fb923c", '<path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 01-3.46 0"/>'),
 ("#b45309,#f59e0b", '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>'),
 ("#4f46e5,#818cf8", '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>'),
 ("#0f766e,#5eead4", '<path d="M20.24 12.24a6 6 0 00-8.49-8.49L5 10.5V19h8.5z"/><line x1="16" y1="8" x2="2" y2="22"/><line x1="17.5" y1="15" x2="9" y2="15"/>'),
]

DARK = "linear-gradient(rgba(20,20,30,.78),rgba(20,20,30,.88))"


def js(s):
    return s.replace("'", "\\'")


def slide_img(n, phase, N, img, teacher):
    return (f'<div class="slide slide-image" data-slide="{n}" data-phase="{phase}" data-lesson="{N}" '
            f'style="background-image:{DARK},url(\'{img}\');background-size:cover;background-position:center" '
            f'data-teacher="{teacher}">')


def listen_btn(phrase, cls="audio-btn-sm", extra=""):
    return (f'<button class="{cls}"{extra} onclick="speakText(\'{js(phrase)}\',this)">{LISTEN_SVG} Listen</button>')


# ---------------------------------------------------------------- SLIDES
def render_slides(D):
    N = D['n']
    P = D['bg']
    o = []
    ap = o.append

    ap('<!-- ============ SLIDE 1: Title ============ -->')
    ap(slide_img(1, 1, N, P['title'], D['t']['s1']))
    ap('  <div class="slide-inner" style="text-align:center">')
    ap(f'    <div class="chapter-label">Lesson {N}</div>')
    ap(f'    <h1 class="slide-heading" style="font-size:2.4rem;color:#fff">{D["title_a"]} <span class="accent">{D["title_b"]}</span></h1>')
    ap(f'    <p style="color:rgba(255,255,255,.82);font-size:1.1rem;margin-top:1rem">{D["subtitle1"]}</p>')
    ap('  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 2: Warm-up Hook ============ -->')
    ap(f'<div class="slide slide-dark" data-slide="2" data-phase="1" data-lesson="{N}" data-teacher="{D["t"]["s2"]}">')
    ap('  <div class="slide-inner" style="text-align:center">')
    ap(f'    <div class="chapter-label">Chapter 1: {D["phases"][0]}</div>')
    ap(f'    <h2 class="slide-heading" style="color:#fff">{D["hook_a"]} <span class="accent">{D["hook_b"]}</span></h2>')
    ap(f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;max-width:540px;margin:.8rem auto 0">{D["hook_prompt"]}</p>')
    ap('  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 3: Warm-up Recall ============ -->')
    ap(f'<div class="slide slide-dark" data-slide="3" data-phase="1" data-lesson="{N}" data-teacher="{D["t"]["s3"]}">')
    ap('  <div class="slide-inner" style="text-align:center">')
    ap(f'    <div class="chapter-label">Chapter 1: {D["phases"][0]}</div>')
    ap(f'    <h2 class="slide-heading" style="color:#fff">{D["recall_a"]} <span class="accent">{D["recall_b"]}</span></h2>')
    ap(f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;max-width:560px;margin:.8rem auto 0">{D["recall_text"]}</p>')
    ap('    <div style="display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center;margin-top:1.2rem">')
    for ch in D['recall_chips']:
        ap(f'      <span style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:.3rem .8rem;font-size:.82rem;color:rgba(255,255,255,.85)">{ch}</span>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 4: Transition to Vocab ============ -->')
    ap(slide_img(4, 2, N, P['vocab'], D['t']['s4']))
    ap('  <div class="slide-inner" style="text-align:center">')
    ap('    <div class="chapter-label">Chapter 2</div>')
    ap(f'    <h1 class="slide-heading" style="font-size:2rem;color:#fff">{D["phases"][1]}</h1>')
    ap(f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.8rem">{D["vocab_sub"]}</p>')
    ap('  </div>\n</div>\n')

    for gi, (start, head) in enumerate([(0, D['vocab_head1']), (6, D['vocab_head2'])], 1):
        sn = 4 + gi
        ap(f'<!-- ============ SLIDE {sn}: Vocab Reveal {start+1}-{start+6} ============ -->')
        ap(f'<div class="slide slide-light" data-slide="{sn}" data-phase="2" data-lesson="{N}" data-teacher="{D["t"]["vocab"+str(gi)]}">')
        ap('  <div class="slide-inner">')
        ap('    <div class="chapter-label">Vocabulary</div>')
        ap(f'    <h2 class="slide-heading">{head[0]} <span class="accent">{head[1]}</span></h2>')
        ap(f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="vocabCount{gi}">0 / 6 words revealed</span></p>')
        ap(f'    <div class="vocab-grid" id="vocabGrid{gi}">')
        for k in range(start, start + 6):
            word, dfn, pt, ex = D['vocab'][k]
            grad, icon = ICONS[k]
            ap('      <div class="vocab-card" onclick="revealVocab(this)">')
            ap(f'        <div class="card-icon" style="background:linear-gradient(135deg,{grad})"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.5">{icon}</svg><div class="card-hint">{dfn}</div></div>')
            ap(f'        <div class="card-body"><div class="card-word">{word}</div><div class="card-def">{dfn}</div><div class="card-example">"{ex}"</div><div class="card-audio">{listen_btn(word)}</div></div>')
            ap('      </div>')
        ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 7: Concept + Drill ============ -->')
    ap(f'<div class="slide slide-light" data-slide="7" data-phase="2" data-lesson="{N}" data-teacher="{D["t"]["s7"]}">')
    ap('  <div class="slide-inner">')
    ap(f'    <div class="chapter-label">{D["concept_label"]}</div>')
    ap(f'    <h2 class="slide-heading">{D["concept_a"]} <span class="accent">{D["concept_b"]}</span></h2>')
    ap(f'    <p style="text-align:center;font-size:.82rem;color:var(--text-dim);margin-top:.3rem">{D["concept_sub"]}</p>')
    ap('    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem;max-width:560px;margin:1rem auto 0">')
    for lab, txt in D['concept_cols']:
        ap(f'      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:.8rem"><p style="font-size:.78rem;font-weight:700;color:var(--accent);margin-bottom:.4rem">{lab}</p><p style="font-size:.82rem">{txt}</p></div>')
    ap('    </div>')
    ap('    <div style="display:flex;flex-direction:column;gap:.6rem;max-width:540px;margin:1.2rem auto 0">')
    for sit, ans in D['concept_drill']:
        ap(f'      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.7rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.86rem">{sit}</p><p style="font-size:.82rem;color:var(--accent);cursor:pointer" onclick="this.textContent=this.textContent===\'Show\'?\'{js(ans)}\':\'Show\'">Show</p></div>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 8: Pronunciation Focus ============ -->')
    ap(f'<div class="slide slide-light" data-slide="8" data-phase="2" data-lesson="{N}" data-teacher="{D["t"]["s8"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Sound Focus</div>')
    ap('    <h2 class="slide-heading">Listen and <span class="accent">Repeat</span></h2>')
    ap('    <p style="text-align:center;font-size:.82rem;color:var(--text-dim);margin-top:.3rem">Listen first, then say it slowly</p>')
    ap('    <div style="display:flex;flex-direction:column;gap:.6rem;max-width:520px;margin:1rem auto 0">')
    for ph in D['pron']:
        ap(f'      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.95rem;font-weight:600">{ph}</p>{listen_btn(ph)}</div>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 9: Transition to Grammar ============ -->')
    ap(slide_img(9, 3, N, P['grammar'], D['t']['s9']))
    ap('  <div class="slide-inner" style="text-align:center">')
    ap('    <div class="chapter-label">Chapter 3</div>')
    ap(f'    <h1 class="slide-heading" style="font-size:2rem;color:#fff">{D["gram_title_a"]} <span class="accent">{D["gram_title_b"]}</span></h1>')
    ap(f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.8rem">{D["gram_title_sub"]}</p>')
    ap('  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 10: Grammar Discovery ============ -->')
    ap(f'<div class="slide slide-light" data-slide="10" data-phase="3" data-lesson="{N}" data-teacher="{D["t"]["s10"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Grammar Discovery</div>')
    ap('    <h2 class="slide-heading">Listen and <span class="accent">Notice</span></h2>')
    ap('    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:560px;margin:1rem auto 0">')
    for html_ex, phrase in D['discovery']:
        ap(f'      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.92rem">{html_ex}</p><button class="audio-btn-sm" onclick="speakText(\'{js(phrase)}\',this)">{LISTEN_SVG}</button></div>')
    ap('    </div>')
    ap('    <button class="primary-btn" onclick="var t=document.getElementById(\'rule1\');t.style.display=(t.style.display===\'none\'||!t.style.display)?\'block\':\'none\'" style="margin:1.2rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Reveal the Rule</button>')
    ap('    <div id="rule1" style="display:none;max-width:560px;margin:1rem auto 0;overflow-x:auto">')
    ap('      <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
    ap(f'        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.6rem;text-align:left">{D["rule_head"][0]}</th><th style="padding:.6rem;text-align:left">{D["rule_head"][1]}</th><th style="padding:.6rem;text-align:left">{D["rule_head"][2]}</th></tr></thead>')
    ap('        <tbody>')
    for i, row in enumerate(D['rule_rows']):
        bg = ';background:var(--bg-elevated)' if i % 2 else ''
        ap(f'          <tr style="border-bottom:1px solid var(--border){bg}"><td style="padding:.5rem;font-weight:600">{row[0]}</td><td style="padding:.5rem">{row[1]}</td><td style="padding:.5rem">{row[2]}</td></tr>')
    ap('        </tbody>\n      </table>\n    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 11: Common Mistake ============ -->')
    ap(f'<div class="slide slide-light" data-slide="11" data-phase="3" data-lesson="{N}" data-teacher="{D["t"]["s11"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Common Mistake</div>')
    ap('    <h2 class="slide-heading">Right vs <span class="accent">Wrong</span></h2>')
    ap('    <div style="display:flex;flex-direction:column;gap:1rem;max-width:520px;margin:1.2rem auto 0">')
    for wrong, right in D['mistakes']:
        ap('      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem">')
        ap(f'        <div style="background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--danger);font-weight:700;margin-bottom:.3rem">&#10007; WRONG</p><p style="font-size:.88rem">{wrong}</p></div>')
        ap(f'        <div style="background:var(--success-bg);border:1px solid var(--success-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--success);font-weight:700;margin-bottom:.3rem">&#10003; RIGHT</p><p style="font-size:.88rem">{right}</p></div>')
        ap('      </div>')
    ap('    </div>')
    ap(f'    <p style="font-size:.82rem;color:var(--text-dim);margin-top:1rem;text-align:center;max-width:500px;margin-left:auto;margin-right:auto">{D["mistake_note"]}</p>')
    ap('  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 12: Grammar Practice ============ -->')
    ap(f'<div class="slide slide-light" data-slide="12" data-phase="3" data-lesson="{N}" data-teacher="{D["t"]["s12"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Practice</div>')
    ap(f'    <h2 class="slide-heading">{D["gpr_a"]} <span class="accent">{D["gpr_b"]}</span></h2>')
    ap('    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Say it first, then click to check</p>')
    ap('    <div class="fill-grid">')
    for pre, ans, post in D['gpractice']:
        ap(f'      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">{pre}<span class="fill-blank">___</span><span class="fill-answer">{ans}</span>{post}</div></div>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 13: Build the Sentence ============ -->')
    ap(f'<div class="slide slide-light" data-slide="13" data-phase="3" data-lesson="{N}" data-teacher="{D["t"]["s13"]}">')
    ap('  <div class="slide-inner">')
    ap(f'    <div class="chapter-label">{D["build1_label"]}</div>')
    ap(f'    <h2 class="slide-heading">{D["build1_a"]} <span class="accent">{D["build1_b"]}</span></h2>')
    ap('    <p style="text-align:center;font-size:.82rem;color:var(--text-dim);margin-top:.3rem">Build the full sentence, then click to compare</p>')
    ap('    <div class="oral-grid">')
    for i, (sit, model) in enumerate(D['build1'], 1):
        ap(f'      <div class="oral-item" onclick="this.classList.toggle(\'revealed\')"><div class="oral-situation">{i}. {sit}</div><div class="oral-model">"{model}"</div></div>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 14: Transition to Context ============ -->')
    ap(slide_img(14, 4, N, P['context'], D['t']['s14']))
    ap('  <div class="slide-inner" style="text-align:center">')
    ap('    <div class="chapter-label">Chapter 4</div>')
    ap(f'    <h1 class="slide-heading" style="font-size:2rem;color:#fff">{D["phases"][3]}</h1>')
    ap(f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.8rem">{D["context_sub"]}</p>')
    ap('  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 15: Dialogue ============ -->')
    ap(f'<div class="slide slide-dark" data-slide="15" data-phase="4" data-lesson="{N}" data-teacher="{D["t"]["s15"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Dialogue</div>')
    ap(f'    <h2 class="slide-heading" style="color:#fff">{D["dlg_title_a"]} <span class="accent">{D["dlg_title_b"]}</span></h2>')
    ap('    <div class="dialogue-box" id="dialogueBox">')
    for i, ln in enumerate(D['dialogue'], 1):
        letter, bg, cls, voice, text_html, plain = ln
        vis = ' visible' if i == 1 else ''
        ap(f'      <div class="dialogue-line{vis}" data-line="{i}" data-voice="{voice}"><div class="dialogue-avatar {cls}" style="background:{bg}">{letter}</div><div class="dialogue-bubble {cls}-bubble" style="background:rgba(255,255,255,.95);color:#1a1a2e">{text_html} <span class="audio-inline" onclick="speakText(\'{js(plain)}\',this)">{LISTEN_SVG}</span></div></div>')
    ap('    </div>')
    ap('    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin:1.2rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Next Line</button>')
    ap('  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 16: Dialogue Comprehension ============ -->')
    ap(f'<div class="slide slide-dark" data-slide="16" data-phase="4" data-lesson="{N}" data-teacher="{D["t"]["s16"]}">')
    ap('  <div class="slide-inner" style="text-align:center">')
    ap('    <div class="chapter-label">Comprehension</div>')
    ap('    <h2 class="slide-heading" style="color:#fff">Did You <span class="accent">Catch</span> It?</h2>')
    ap('    <div class="comp-questions" id="dialogueQs" style="max-width:520px;margin:1.2rem auto 0;text-align:left">')
    for i, (q, a) in enumerate(D['dlg_comp'], 1):
        ap(f'      <div class="comp-q" onclick="revealComp(this)"><div class="q-text" style="color:rgba(255,255,255,.9)">{i}. {q}</div><div class="q-answer">{a}</div></div>')
    ap('    </div>\n  </div>\n</div>\n')

    for li, L in enumerate(D['listenings'], 1):
        sn = 16 + li
        pid = f'mp-listen{li}'
        wid = f'waveform{li}'
        qid = f'listening{li}Qs'
        bars = ''.join('<div class="bar"></div>' for _ in range(20))
        ap(f'<!-- ============ SLIDE {sn}: Listening {li} (MONOLOGUE) ============ -->')
        ap(f'<div class="slide slide-dark" data-slide="{sn}" data-phase="4" data-lesson="{N}" data-teacher="{D["t"]["listen"+str(li)]}">')
        ap('  <div class="slide-inner" style="text-align:center">')
        ap('    <div class="chapter-label">Listening</div>')
        ap(f'    <h2 class="slide-heading" style="color:#fff">{L["title_a"]} <span class="accent">{L["title_b"]}</span></h2>')
        ap('    <p style="color:rgba(255,255,255,.78);font-size:.9rem;margin-bottom:1rem">Listen first. No text. Sound only.</p>')
        ap(f'    <div class="waveform waveform-paused" id="{wid}">{bars}</div>')
        ap(f'    <div class="mock-player" id="{pid}" data-src="/audio/murielle-xavier/{L["file"]}" data-waveform="{wid}" data-questions="{qid}" style="max-width:460px;margin:.8rem auto 0">')
        ap(f'      <div class="lp-seekbar" onclick="mpSeek(event,\'{pid}\')" style="width:100%;height:6px;background:rgba(255,255,255,.12);border-radius:3px;cursor:pointer;position:relative"><div class="lp-progress" id="progress-{pid}" style="width:0%;height:100%;background:var(--accent-light);border-radius:3px;transition:width .1s"></div></div>')
        ap(f'      <div style="display:flex;justify-content:space-between;margin:.4rem 0 .6rem"><span id="time-current-{pid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span><span id="time-total-{pid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span></div>')
        ap('      <div style="display:flex;align-items:center;justify-content:center;gap:1rem;margin-bottom:.6rem">')
        ap(f'        <button class="lp-btn" onclick="mpSkip(\'{pid}\',-5)" aria-label="Back 5 seconds" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">-5s</button>')
        ap(f'        <button class="lp-btn lp-play" id="play-{pid}" onclick="mpToggle(\'{pid}\')" aria-label="Play or pause" style="background:var(--accent);border:none;color:#fff;border-radius:50%;width:48px;height:48px;cursor:pointer"><svg class="lp-icon-play" viewBox="0 0 24 24" width="18" height="18"><polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg><svg class="lp-icon-pause" viewBox="0 0 24 24" width="18" height="18" style="display:none"><rect x="6" y="4" width="4" height="16" fill="currentColor"/><rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg></button>')
        ap(f'        <button class="lp-btn" onclick="mpSkip(\'{pid}\',5)" aria-label="Forward 5 seconds" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">+5s</button>')
        ap('      </div>')
        spd = ''.join(
            f'<button class="lp-speed-btn{" lp-speed-active" if s==1 else ""}" onclick="mpSpeed(\'{pid}\',{s},this)" '
            f'style="background:{"var(--accent)" if s==1 else "transparent"};border:1px solid {"var(--accent)" if s==1 else "rgba(255,255,255,.25)"};'
            f'color:{"#fff" if s==1 else "rgba(255,255,255,.82)"};border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">{s}x</button>'
            for s in [0.5, 0.75, 1, 1.25])
        ap(f'      <div style="display:flex;gap:.4rem;justify-content:center">{spd}</div>')
        ap('    </div>')
        ap(f'    <div class="comp-questions" id="{qid}" style="display:none;max-width:520px;margin:1.2rem auto 0">')
        for i, (q, a) in enumerate(L['qs'], 1):
            ap(f'      <div class="comp-q" onclick="revealComp(this)"><div class="q-text" style="color:rgba(255,255,255,.9)">{i}. {q}</div><div class="q-answer">{a}</div></div>')
        ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 19: Real Artifact ============ -->')
    ap(f'<div class="slide slide-light" data-slide="19" data-phase="4" data-lesson="{N}" data-teacher="{D["t"]["s19"]}">')
    ap('  <div class="slide-inner" style="text-align:center">')
    ap('    <div class="chapter-label">Real Artifact</div>')
    ap(f'    <h2 class="slide-heading">{D["art_title_a"]} <span class="accent">{D["art_title_b"]}</span></h2>')
    ap('    <div style="max-width:460px;margin:1.2rem auto 0;background:#fffef8;border:1px solid #e8e4d0;border-radius:8px;padding:1.6rem;color:#2d2d3a;position:relative;text-align:left;box-shadow:0 4px 18px rgba(0,0,0,.1)">')
    ap(f'      <p style="font-size:.72rem;letter-spacing:2px;text-transform:uppercase;color:#9a8f6a;margin-bottom:.6rem">{D["art_kicker"]}</p>')
    ap(f'      <p style="font-size:.9rem;margin-bottom:.9rem"><strong>{D["art_subtitle"]}</strong></p>')
    ap('      <div style="display:flex;flex-direction:column;gap:.55rem">')
    for line in D['art_lines']:
        ap(f'        <p style="font-size:.86rem;padding-left:1rem;border-left:3px solid var(--accent)">{line}</p>')
    ap('      </div>')
    ap(f'      <p style="font-size:.78rem;color:#9a8f6a;margin-top:1rem;text-align:right">{D["art_sign"]}</p>')
    ap('    </div>')
    ap(f'    <p style="font-size:.82rem;color:var(--text-dim);margin-top:1rem;max-width:440px;margin-left:auto;margin-right:auto">{D["art_note"]}</p>')
    ap('  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 20: Transition to Practice ============ -->')
    ap(slide_img(20, 5, N, P['practice'], D['t']['s20']))
    ap('  <div class="slide-inner" style="text-align:center">')
    ap('    <div class="chapter-label">Chapter 5</div>')
    ap(f'    <h1 class="slide-heading" style="font-size:2rem;color:#fff"><span class="accent">{D["phases"][4]}</span></h1>')
    ap('    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.8rem">Put it all together</p>')
    ap('  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 21: Quick Fire ============ -->')
    ap(f'<div class="slide slide-light" data-slide="21" data-phase="5" data-lesson="{N}" data-teacher="{D["t"]["s21"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Quick Fire</div>')
    ap('    <h2 class="slide-heading">Say It Like a <span class="accent">Pro</span></h2>')
    ap('    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="qfScore">0 / 5</span></p>')
    ap('    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:560px;margin:1.2rem auto 0">')
    for i, (sit, ans) in enumerate(D['quickfire'], 1):
        ap(f'      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem"><p style="font-size:.88rem;margin-bottom:.4rem"><strong>{i}.</strong> {sit}</p><p style="font-size:.82rem;color:var(--accent);cursor:pointer" onclick="this.textContent=this.textContent===\'Show Answer\'?\'{js(ans)}\':\'Show Answer\'">Show Answer</p></div>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 22: Spot the Error ============ -->')
    ap(f'<div class="slide slide-light" data-slide="22" data-phase="5" data-lesson="{N}" data-teacher="{D["t"]["s22"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Detective</div>')
    ap('    <h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>')
    ap('    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="errorScore">0 / 4 errors found</span></p>')
    ap('    <div class="error-grid" id="errorGrid">')
    for bad, fix in D['spot']:
        ap(f'      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"{bad}"</div><div class="error-fix">"{fix}"</div></div>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 23: Sentence Building ============ -->')
    ap(f'<div class="slide slide-light" data-slide="23" data-phase="5" data-lesson="{N}" data-teacher="{D["t"]["s23"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Build</div>')
    ap('    <h2 class="slide-heading">Sentence <span class="accent">Building</span></h2>')
    ap('    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Use the words to build a full sentence, then click to compare</p>')
    ap('    <div class="oral-grid">')
    for i, (sit, model) in enumerate(D['build2'], 1):
        ap(f'      <div class="oral-item" onclick="this.classList.toggle(\'revealed\')"><div class="oral-situation">{i}. {sit}</div><div class="oral-model">"{model}"</div></div>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 24: Transition to Production ============ -->')
    ap(slide_img(24, 6, N, P['production'], D['t']['s24']))
    ap('  <div class="slide-inner" style="text-align:center">')
    ap('    <div class="chapter-label">Chapter 6</div>')
    ap('    <h1 class="slide-heading" style="font-size:2rem;color:#fff">Your <span class="accent">Turn</span></h1>')
    ap(f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.8rem">{D["production_sub"]}</p>')
    ap('  </div>\n</div>\n')

    rp = D['roleplays']
    ap('<!-- ============ SLIDE 25: Role-Play Guided ============ -->')
    ap(f'<div class="slide slide-light" data-slide="25" data-phase="6" data-lesson="{N}" data-teacher="{D["t"]["s25"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Role-Play</div>')
    ap(f'    <h2 class="slide-heading">{rp["guided"]["h"][0]} <span class="accent">{rp["guided"]["h"][1]}</span></h2>')
    ap('    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,var(--accent-dim),rgba(' + ACCENT_RGB + ',.05));border:1px solid var(--accent);border-radius:12px;padding:1.5rem">')
    ap(f'      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> {rp["guided"]["scenario"]}</p>')
    ap('      <p style="font-size:.85rem;font-weight:600;margin-bottom:.5rem">Use these:</p>')
    ap('      <div style="display:flex;flex-wrap:wrap;gap:.4rem">')
    for chip in rp['guided']['chips']:
        ap(f'        <span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;padding:.3rem .7rem;font-size:.8rem">{chip}</span>')
    ap('      </div>\n    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 26: Role-Play Semi-Free ============ -->')
    ap(f'<div class="slide slide-light" data-slide="26" data-phase="6" data-lesson="{N}" data-teacher="{D["t"]["s26"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Role-Play</div>')
    ap(f'    <h2 class="slide-heading">{rp["semi"]["h"][0]} <span class="accent">{rp["semi"]["h"][1]}</span></h2>')
    ap('    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba(' + ACCENT_RGB + ',.08),rgba(' + ACCENT_RGB + ',.02));border:1px solid var(--accent);border-radius:12px;padding:1.5rem">')
    ap(f'      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> {rp["semi"]["scenario"]}</p>')
    ap('      <p style="font-size:.85rem;font-weight:600;margin-bottom:.5rem">Keywords:</p>')
    ap('      <div style="display:flex;flex-wrap:wrap;gap:.4rem">')
    for chip in rp['semi']['chips']:
        ap(f'        <span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;padding:.3rem .7rem;font-size:.8rem">{chip}</span>')
    ap('      </div>\n    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 27: Role-Play Free ============ -->')
    ap(f'<div class="slide slide-light" data-slide="27" data-phase="6" data-lesson="{N}" data-teacher="{D["t"]["s27"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Free Practice</div>')
    ap(f'    <h2 class="slide-heading">{rp["free"]["h"][0]} <span class="accent">{rp["free"]["h"][1]}</span></h2>')
    ap('    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba(' + ACCENT_RGB + ',.12),rgba(' + ACCENT_RGB + ',.03));border:1px solid var(--accent);border-radius:12px;padding:1.5rem">')
    ap(f'      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> {rp["free"]["scenario"]}</p>')
    ap(f'      <p style="font-size:.85rem;color:var(--text-dim);font-style:italic">{rp["free"]["note"]}</p>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 28: Delayed Error Correction ============ -->')
    ap(f'<div class="slide slide-light" data-slide="28" data-phase="6" data-lesson="{N}" data-teacher="{D["t"]["s28"]}">')
    ap('  <div class="slide-inner">')
    ap('    <div class="chapter-label">Error Correction</div>')
    ap('    <h2 class="slide-heading">Let Us <span class="accent">Fix</span> It</h2>')
    ap('    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin-top:.3rem">Errors from the free practice. Say the correct version.</p>')
    ap('    <div style="max-width:520px;margin:1.2rem auto 0;display:flex;flex-direction:column;gap:1rem">')
    for _ in range(3):
        ap('      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--danger);font-weight:600;margin-bottom:.3rem">What you said:</p><p contenteditable="true" style="font-size:.9rem;min-height:1.5em;border-bottom:1px dashed var(--border);padding-bottom:.3rem;outline:none">(Type the error here)</p><p style="font-size:.78rem;color:var(--success);font-weight:600;margin-top:.5rem;margin-bottom:.3rem">Better version:</p><p contenteditable="true" style="font-size:.9rem;min-height:1.5em;border-bottom:1px dashed var(--border);padding-bottom:.3rem;outline:none">(Type the correction here)</p></div>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 29: Key Phrases ============ -->')
    ap(f'<div class="slide slide-dark" data-slide="29" data-phase="7" data-lesson="{N}" data-teacher="{D["t"]["s29"]}">')
    ap('  <div class="slide-inner" style="text-align:center">')
    ap('    <div class="chapter-label">Key Phrases</div>')
    ap('    <h2 class="slide-heading" style="color:#fff">Phrases to <span class="accent">Take Away</span></h2>')
    ap('    <div style="max-width:520px;margin:1.2rem auto 0;display:flex;flex-direction:column;gap:.6rem">')
    for i, ph in enumerate(D['keyphrases'], 1):
        ap(f'      <div style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:.7rem 1rem"><span style="color:var(--accent-light);font-weight:700;font-size:.9rem;min-width:24px">{i}</span><span style="color:rgba(255,255,255,.9);font-size:.88rem;flex:1">{ph}</span><button class="audio-btn-sm" onclick="speakText(\'{js(ph)}\',this)" style="background:var(--accent);border:none;color:#fff;border-radius:6px;padding:.3rem .6rem;font-size:.72rem;cursor:pointer;white-space:nowrap">{LISTEN_SVG12} Listen</button></div>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 30: Checklist ============ -->')
    ap(f'<div class="slide slide-dark" data-slide="30" data-phase="7" data-lesson="{N}" data-teacher="{D["t"]["s30"]}">')
    ap('  <div class="slide-inner" style="text-align:center">')
    ap('    <div class="chapter-label">Self-Assessment</div>')
    ap('    <h2 class="slide-heading" style="color:#fff">What I <span class="accent">Learned</span></h2>')
    ap(f'    <div class="check-grid" id="checklist-{N}" style="max-width:520px;margin:1.2rem auto 0;display:flex;flex-direction:column;gap:.5rem;text-align:left">')
    for item in D['checklist']:
        ap(f'      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>{item}</div>')
    ap('    </div>\n  </div>\n</div>\n')

    ap('<!-- ============ SLIDE 31: Lesson Complete ============ -->')
    ap(f'<div class="slide slide-dark" data-slide="31" data-phase="7" data-lesson="{N}" data-teacher="{D["t"]["s31"]}">')
    ap('  <div class="slide-inner" style="text-align:center">')
    ap('    <div class="chapter-label">Lesson Complete</div>')
    ap('    <div class="badge-card">')
    ap('      <div class="badge-icon">')
    ap('        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></div>')
    ap('        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>')
    ap('      </div>')
    ap(f'      <h2 class="slide-heading" style="color:#fff">{D["badge_a"]} <span class="accent">Earned!</span></h2>')
    ap(f'      <p style="color:rgba(255,255,255,.78);font-size:1rem;margin-top:.5rem">{D["badge_text"]}</p>')
    ap(f'      <p style="color:rgba(255,255,255,.82);font-size:.85rem;margin-top:1.5rem">Lesson {N} -- Complete.</p>')
    ap(f'      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">Next lesson: {D["next_lesson"]}</p>')
    ap('    </div>\n  </div>\n</div>')
    return '\n'.join(o) + '\n'


# ---------------------------------------------------------------- PRECLASS
def render_preclass(D):
    N = D['n']
    seed = D.get('seed', N * 101)
    rnd = random.Random(seed)
    vocab = D['vocab']
    defs = [v[1] for v in vocab]
    o = []
    ap = o.append
    ap(f'<div class="lesson-card" id="ex-lesson-{N}">')
    ap('  <div class="lesson-header" onclick="toggleLesson(this)">')
    ap(f'    <div class="lesson-header-img" style="background-image:url(\'{D["bg"]["title"].replace("w=1200","w=600")}\')"></div>')
    ap('    <div class="lesson-header-content">')
    ap(f'      <div class="lesson-number">Lesson {N} -- Pre-class</div>')
    ap(f'      <h3>{D["pc_title"]}</h3>')
    ap(f'      <div class="lesson-desc">{D["pc_desc"]}</div>')
    ap(f'      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="{N}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="{N}">0%</span></div>')
    ap('    </div>\n    <div class="expand-icon">&#9660;</div>\n  </div>')
    ap('  <div class="lesson-body">\n')

    ap('    <div class="exercise-section">')
    ap('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
    ap('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ouça cada palavra e leia o exemplo. A tradução em português está entre parênteses. (Listen and read the example.)</p>')
    ap('      <div class="vocab-cards">')
    for word, dfn, pt, ex in vocab:
        ap(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">{word}</span><span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{dfn} ({pt})</span></div><div class="vocab-card-example">"{ex}"</div></div><button class="audio-btn" onclick="speakText(\'{js(word)}\',this)">Listen</button></div>')
    ap('      </div>\n    </div>\n')

    ap('    <div class="exercise-section">')
    ap('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
    ap('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Combine cada palavra com a definição correta. (Match each word with the correct definition.)</p>')
    ap(f'      <div class="match-grid" id="match-l{N}">')
    for word, dfn, pt, ex in vocab:
        opts = defs[:]
        while True:
            rnd.shuffle(opts)
            if opts != defs:
                break
        ohtml = '<option value="">Select...</option>' + ''.join(f'<option value="{o2}">{o2}</option>' for o2 in opts)
        ap(f'        <div class="match-row" data-answer="{dfn}"><span class="match-word" style="flex:0 0 130px">{word}</span><select style="flex:1;width:100%" onchange="checkMatch(this)">{ohtml}</select></div>')
    ap('      </div>\n    </div>\n')

    ap('    <div class="exercise-section">')
    ap('      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
    ap('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda as perguntas. (Read the text and answer the questions.)</p>')
    ap('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
    ap(f'        <p>{D["gic_text"]}</p>')
    ap('      </div>')
    for q, opts in D['gic_quiz']:
        ap('      <div class="quiz-item"><div class="quiz-question">' + q + '</div><div class="quiz-options">' +
           ''.join(f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{"true" if corr else "false"}"><span class="option-letter">{chr(65+i)}</span> {txt}</div>' for i, (txt, corr) in enumerate(opts)) +
           '</div></div>')
    ap('    </div>\n')

    ap('    <div class="exercise-section">')
    ap(f'      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- {D["gt_title"]}</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
    ap(f'      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">{D["gt_intro"]}</p>')
    ap('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
    ap(f'        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">{D["gt_head"][0]}</th><th style="padding:.7rem;text-align:left">{D["gt_head"][1]}</th><th style="padding:.7rem;text-align:left">{D["gt_head"][2]}</th></tr></thead>')
    ap('        <tbody>')
    for i, row in enumerate(D['gt_rows']):
        bg = ';background:var(--bg-elevated)' if i % 2 else ''
        ap(f'          <tr style="border-bottom:1px solid var(--border){bg}"><td style="padding:.6rem;font-weight:600">{row[0]}</td><td style="padding:.6rem">{row[1]}</td><td style="padding:.6rem">{row[2]}</td></tr>')
    ap('        </tbody>\n      </table></div>')
    ap(f'      <p style="font-size:.8rem;color:var(--text-dim);margin-top:.8rem;font-style:italic">{D["gt_note"]}</p>')
    ap('    </div>\n')

    ap('    <div class="exercise-section">')
    ap('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
    ap('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase. A pista entre parênteses ajuda. (Complete each sentence. Tap Listen to hear it.)</p>')
    for pre, ans, hint, phrase, post in D['fill']:
        ap(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">{post}</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
    ap('    </div>\n')

    ap('    <div class="exercise-section">')
    ap(f'      <div class="section-header-row"><h4>Stage 2: {D["order_title"]}</h4><span class="badge badge-order">Order</span></div>')
    ap(f'      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{D["order_instr"]}</p>')
    ap(f'      <div class="order-container" id="order-l{N}">')
    for text, order in D['order']:
        ap(f'        <div class="order-item" draggable="true" data-order="{order}" onclick="selectOrderItem(this,\'order-l{N}\')"><span class="order-num">?</span><span class="order-text">{text}</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l{N}\')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,\'order-l{N}\')">&#9660;</button></span></div>')
    ap(f'      </div>\n      <button class="verify-all-btn" onclick="checkOrder(\'order-l{N}\')">Check Order</button>\n    </div>\n')

    ap('    <div class="exercise-section">')
    ap('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
    ap('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ouça cada frase e depois grave você mesma. (Listen, then record yourself.)</p>')
    for en, pt in D['speech']:
        ap(f'      <div class="speech-card" data-phrase="{en}">')
        ap(f'        <div class="speech-phrase">{en}</div>')
        ap(f'        <div class="speech-translation">{pt}</div>')
        ap('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>')
        ap('        <div class="speech-result"></div>')
        ap('      </div>')
    ap('    </div>\n')

    ap('    <div class="exercise-section">')
    ap('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
    ap('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada situação. (Choose the best answer for each situation.)</p>')
    for q, opts in D['sit_quiz']:
        ap('      <div class="quiz-item"><div class="quiz-question">' + q + '</div><div class="quiz-options">' +
           ''.join(f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{"true" if corr else "false"}"><span class="option-letter">{chr(65+i)}</span> {txt}</div>' for i, (txt, corr) in enumerate(opts)) +
           '</div></div>')
    ap('    </div>\n')

    ap('    <div class="exercise-section">')
    ap('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
    ap('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave você mesma respondendo a pergunta abaixo. Não existe resposta certa ou errada. (Record yourself. There is no right or wrong answer.)</p>')
    ap('      <div class="think-card">')
    ap(f'        <div class="think-question">{D["think"]}</div>')
    ap('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
    ap(f'        <div id="think-result-{N}"></div>')
    ap('      </div>\n    </div>\n')

    ap('    <div class="survival-card">')
    ap(f'      <h4>Survival Card -- Lesson {N}</h4>')
    for i, (en, pt) in enumerate(D['survival'], 1):
        ap(f'      <div class="survival-phrase"><span class="sp-num">{i}</span><span class="sp-en">{en}</span><span class="sp-pt">{pt}</span><button class="btn btn-listen" onclick="speakText(\'{js(en)}\',this)">&#9835;</button></div>')
    ap('    </div>\n')
    ap('  </div>\n</div>')
    return '\n'.join(o) + '\n'


# ---------------------------------------------------------------- COMPLEMENTARY
def render_complementary(D):
    N = D['n']
    o = []
    ap = o.append
    ap('')
    ap('<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;margin-bottom:1rem">Complementary Activities</h3>')
    ap('<p style="font-size:.85rem;color:var(--text-dim);margin-bottom:1.5rem">Extra materials to reinforce your learning outside class. Mark as done after watching or listening.</p>')
    ap('')
    ap(f'<h4 style="font-size:.95rem;margin-bottom:.8rem">Lesson {N} -- {D["comp_heading"]}</h4>')
    ap('')
    ICON_SVG = {
        'Podcast': '<path d="M3 18v-6a9 9 0 0118 0v6"/><path d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 2 0 012-2h3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"/>',
        'Series': '<rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><path d="M7 2v20"/><path d="M17 2v20"/><path d="M2 12h20"/><path d="M2 7h5"/><path d="M2 17h5"/><path d="M17 17h5"/>',
        'YouTube': '<path d="M22.54 6.42a2.78 2.78 0 00-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 00-1.94 2A29 29 0 001 11.75a29 29 0 00.46 5.33A2.78 2.78 0 003.4 19.1c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 001.94-2 29 29 0 00.46-5.25 29 29 0 00-.46-5.43z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/>',
    }
    for slug, typ, title, desc, tip, linktext, url in D['media']:
        ap(f'<div class="media-card-wrapper" data-media="l{N}-{slug}">')
        ap('  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>')
        ap('  <div class="media-card">')
        ap(f'    <div class="media-thumb" style="font-size:1.5rem;display:flex;align-items:center;justify-content:center;width:60px;height:60px;background:var(--accent-dim);border-radius:10px"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2">{ICON_SVG[typ]}</svg></div>')
        ap('    <div class="media-info">')
        ap(f'      <div class="media-type">{typ}</div>')
        ap(f'      <h5>{title}</h5>')
        ap(f'      <p style="font-size:.82rem;color:var(--text-mid)">{desc}</p>')
        ap(f'      <p class="media-tip" style="font-size:.78rem;color:var(--accent);margin-top:.3rem">Tip: {tip}</p>')
        ap(f'      <a href="{url}" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">{linktext} &#8599;</a>')
        ap('    </div>\n  </div>\n</div>\n')
    return '\n'.join(o)


def build(D):
    N = D['n']
    outdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', f'murielle-xavier-aula{N}'))
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, 'slides.html'), 'w', encoding='utf-8').write(render_slides(D))
    open(os.path.join(outdir, 'preclass.html'), 'w', encoding='utf-8').write(render_preclass(D))
    open(os.path.join(outdir, 'complementary.html'), 'w', encoding='utf-8').write(render_complementary(D))
    print(f'wrote slides/preclass/complementary for aula {N} -> {outdir}')
