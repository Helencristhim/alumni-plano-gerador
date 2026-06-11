# -*- coding: utf-8 -*-
# slides_block() -> HTML of the 28 IN CLASS slides for Simone Aula 3 (Corporate Emails)
BG = "linear-gradient(rgba(20,20,30,.85),rgba(20,20,30,.92)),url('https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80')"
LB = '<svg viewBox="0 0 24 24" width="16" height="16"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen'
LBI = '<svg viewBox="0 0 24 24" width="14" height="14"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg>'

def esc(s):
    return s.replace("'", "\\'")

def listen_row(phrase):
    return ('<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;'
            'display:flex;justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.92rem">%s</p>'
            '<button class="audio-btn-sm" onclick="speakText(\'%s\',this)">%s</button></div>' % (phrase, esc(phrase), LB))

VOCAB_IC = [
    ('Subject line', 'The short title that says what the email is about', '"Write a clear subject line."',
     '<path d="M4 7h16M4 12h10M4 17h7"/>'),
    ('Recipient', 'The person who receives the email', '"Add the recipient’s address."',
     '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0116 0"/>'),
    ('Attachment', 'A file you send together with the email', '"The contract is the attachment."',
     '<path d="M21 11l-8.5 8.5a5 5 0 01-7-7L14 4a3.5 3.5 0 015 5l-9 9a2 2 0 01-3-3l8.5-8.5"/>'),
    ('Regarding', 'About / concerning (formal)', '"I am writing regarding the contract."',
     '<circle cx="12" cy="12" r="9"/><path d="M12 16v-4M12 8h.01"/>'),
    ('Forward', 'To send a received email to another person', '"I will forward it to the team."',
     '<polyline points="15 17 20 12 15 7"/><path d="M4 18v-2a4 4 0 014-4h12"/>'),
    ('Reply', 'To answer an email', '"Please reply by Friday."',
     '<polyline points="9 17 4 12 9 7"/><path d="M20 18v-2a4 4 0 00-4-4H4"/>'),
    ('Follow up', 'To send a second message to check progress', '"I will follow up next week."',
     '<path d="M21 12a9 9 0 11-3-6.7"/><polyline points="21 3 21 8 16 8"/>'),
    ('Best regards', 'A polite, formal way to close an email', '"Best regards, Simone."',
     '<path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4 20-7z"/>'),
]

def vocab_card_ic(word, clue, ex, icon):
    return ('''      <div class="vocab-card-ic" onclick="revealVocab(this)" style="cursor:pointer;background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem;text-align:center;min-height:120px;display:flex;flex-direction:column;align-items:center;justify-content:center">
        <div class="vocab-front"><svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5">%s</svg><p style="font-size:.8rem;color:var(--text-dim);margin-top:.5rem">%s</p></div>
        <div class="vocab-back" style="display:none"><p style="font-weight:700;font-size:1.1rem">%s</p><p style="font-size:.8rem;color:var(--text-dim)">%s</p><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('%s',this)">%s</button></div>
      </div>''' % (icon, clue, word, ex, esc(word), LB))

def reveal_phrase(html, plain):
    return ('<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;'
            'display:flex;justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.92rem">%s</p>'
            '<button class="audio-btn-sm" onclick="speakText(\'%s\',this)">%s</button></div>' % (html, esc(plain), LB))

def oral_item(phrase):
    return ('<div class="oral-item" style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;'
            'padding:.8rem;display:flex;align-items:center;gap:.8rem"><button class="audio-btn-sm" onclick="speakText(\'%s\',this)">%s</button>'
            '<p style="font-size:.88rem">"%s"</p></div>' % (esc(phrase), LBI, phrase))

def comp_q(q, a):
    return ('<div class="comp-q" style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem">'
            '<p style="font-size:.9rem;font-weight:600;margin-bottom:.5rem">%s</p>'
            '<p style="font-size:.85rem;color:var(--accent);cursor:pointer" onclick="this.textContent=this.textContent===\'Click to reveal\'?\'%s\':\'Click to reveal\'">Click to reveal</p></div>' % (q, esc(a).replace('"', '&quot;')))

def qf_item(n, sit, ans):
    return ('<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem">'
            '<p style="font-size:.88rem;margin-bottom:.4rem"><strong>%d.</strong> %s</p>'
            '<p style="font-size:.82rem;color:var(--accent);cursor:pointer" onclick="this.textContent=this.textContent===\'Show Answer\'?\'%s\':\'Show Answer\'">Show Answer</p></div>' % (n, sit, ans.replace('"', '&quot;')))

def err_card(wrong, fix):
    return ('<div class="error-card" style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem">'
            '<p style="font-size:.9rem;margin-bottom:.5rem"><span style="color:var(--danger);text-decoration:line-through">"%s"</span></p>'
            '<p style="font-size:.82rem;color:var(--success);cursor:pointer" onclick="this.textContent=this.textContent===\'Click to correct\'?\'%s\':\'Click to correct\'">Click to correct</p></div>' % (wrong, fix.replace('"', '&quot;')))

def dlg_line(n, speaker, voice, text, plain, student=False):
    if student:
        av = '<div class="dialogue-avatar elaine">S</div>'
        bub = 'elaine-bubble'
        vis = ''
    else:
        av = '<div class="dialogue-avatar" style="background:#2d5a8e">D</div>'
        bub = 'sarah-bubble'
        vis = ' visible' if n == 1 else ''
    cls = 'dialogue-line' + (' visible' if n == 1 else '')
    return ('      <div class="%s" data-line="%d" data-speaker="%s" data-voice="%s">%s<div class="dialogue-bubble %s">%s '
            '<span class="audio-inline" onclick="speakText(\'%s\',this)">%s</span></div></div>' % (
                cls, n, speaker, voice, av, bub, text, esc(plain), LBI))

def slides_block():
    S = []
    def slide(n, cls, phase, teacher, inner, bg=False):
        bgstyle = (' style="background-image:%s;background-size:cover;background-position:center"' % BG) if bg else ''
        S.append('<div class="slide%s%s" data-slide="%d" data-lesson="3" data-phase="%d" data-teacher="%s"%s>\n  <div class="slide-inner"%s>\n%s\n  </div>\n</div>' % (
            (' active' if n == 1 else ''), (' ' + cls), n, phase, teacher.replace('"', '&quot;'),
            bgstyle, ('' if 'text-align' not in inner[:0] else ''), inner))

    # ---------- PHASE 1: The Brief ----------
    slide(1, 'slide-dark', 1,
          '<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: \'You draft contracts every week. Today we write the emails around them -- clear and professional.\' Crie expectativa.',
          '''    <div style="text-align:center">
    <div class="chapter-label">Day 3 -- Email Essentials</div>
    <h1 class="slide-heading" style="font-size:2.5rem">Corporate <span class="accent">Emails</span></h1>
    <p style="color:rgba(255,255,255,.6);font-size:1.1rem;margin-top:1rem">Open, write and close an email with confidence</p>
    </div>''', bg=True)

    slide(2, 'slide-light', 1,
          '<strong>Warm-up + callback (3 min):</strong> Ponte com a Aula 2. Toque os 2 audios e peca Simone repetir. Pergunte: \'Last class you described your routine. How do you say what you usually do at work?\' Depois: \'After you draft the contract, you write an email about it. That is today.\'',
          '''    <div class="chapter-label">Warm-up</div>
    <h2 class="slide-heading">From Routine to <span class="accent">Email</span></h2>
    <p style="color:var(--text-dim);font-size:1rem;margin-top:1rem;max-width:600px;margin-left:auto;margin-right:auto">Last class you talked about your work routine. Let's remember:</p>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:520px;margin:1.2rem auto 0">
      %s
      %s
    </div>
    <div style="max-width:520px;margin:1.5rem auto 0;background:var(--accent-dim);border:1px solid var(--accent);border-radius:12px;padding:1.2rem">
      <p style="font-weight:600;font-size:.95rem;margin-bottom:.5rem">Now think:</p>
      <p style="font-size:.9rem;color:var(--text-dim)">After you draft a contract, you have to email the client about it. How do you start that email in English?</p>
    </div>''' % (listen_row('I usually start work at nine o’clock.'), listen_row('I often draft contracts in the afternoon.')))

    slide(3, 'slide-light', 1,
          '<strong>Bridge (2 min):</strong> Diga: \'Every professional email has three parts. Tonight you learn all three.\' Mostre os 3 passos.',
          '''    <div class="chapter-label">Today's Goal</div>
    <h2 class="slide-heading">Three Parts of an <span class="accent">Email</span></h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:.8rem;max-width:640px;margin:1.5rem auto 0">
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;padding:.9rem;text-align:center"><p style="font-weight:700;font-size:.9rem">1. Open</p><p style="font-size:.78rem;color:var(--text-dim)">greeting &amp; topic</p></div>
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;padding:.9rem;text-align:center"><p style="font-weight:700;font-size:.9rem">2. Body</p><p style="font-size:.78rem;color:var(--text-dim)">attach &amp; request</p></div>
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;padding:.9rem;text-align:center"><p style="font-weight:700;font-size:.9rem">3. Close</p><p style="font-size:.78rem;color:var(--text-dim)">sign off politely</p></div>
    </div>''')

    # ---------- PHASE 2: Key Words ----------
    slide(4, 'slide-dark', 2,
          '<strong>Transicao vocab (1 min):</strong> Diga: \'First, the email words. Eight words. Click each card to reveal.\' Passe ao proximo.',
          '''    <div style="text-align:center">
    <div class="chapter-label">Chapter 2</div>
    <h2 class="slide-heading" style="font-size:2rem">Email <span class="accent">Words</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">8 words for corporate emails</p>
    </div>''', bg=True)

    slide(5, 'slide-light', 2,
          '<strong>Vocab reveal 1-4 (4 min):</strong> Mostre os 4 cards. Leia a pista, pergunte, depois revele. Toque o audio e peca Simone repetir. CCQ: \'Is the subject line the long text or the short title? (The short title.)\'',
          '''    <div class="chapter-label">Email Words</div>
    <h2 class="slide-heading">Words <span class="accent">1-4</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="vocabCount1">0 / 4 words revealed</span></p>
    <div class="vocab-grid" id="vocabGrid1" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;max-width:600px;margin:1rem auto 0">
%s
    </div>''' % '\n'.join(vocab_card_ic(*v) for v in VOCAB_IC[:4]))

    slide(6, 'slide-light', 2,
          '<strong>Vocab reveal 5-8 (4 min):</strong> Mesma dinamica. Para \'forward\' vs \'reply\', mostre a diferenca (encaminhar a terceiros vs responder ao remetente). Para \'follow up\', explique: segundo email para cobrar resposta.',
          '''    <div class="chapter-label">Email Words</div>
    <h2 class="slide-heading">Words <span class="accent">5-8</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="vocabCount2">0 / 4 words revealed</span></p>
    <div class="vocab-grid" id="vocabGrid2" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;max-width:600px;margin:1rem auto 0">
%s
    </div>''' % '\n'.join(vocab_card_ic(*v) for v in VOCAB_IC[4:]))

    slide(7, 'slide-light', 2,
          '<strong>Pronunciation drill (3 min):</strong> Toque cada audio e peca Simone repetir. Corrija: \'Recipient\' (ri-SI-pi-ent), \'Attachment\' (a-TACH-ment), \'Regarding\' (ri-GAR-ding).',
          '''    <div class="chapter-label">Pronunciation Drill</div>
    <h2 class="slide-heading">Say It <span class="accent">Clearly</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:500px;margin:1.2rem auto 0">
%s
    </div>''' % '\n'.join(
        '      <div style="background:rgba(255,255,255,.08);border:1px solid var(--border);border-radius:10px;padding:1rem;display:flex;justify-content:space-between;align-items:center"><span style="font-size:1.1rem;font-weight:600">%s</span><button class="audio-btn-sm" onclick="speakText(\'%s\',this)">%s</button></div>' % (w, esc(w), LB)
        for w in ['Recipient', 'Attachment', 'Regarding', 'Best regards']))

    # ---------- PHASE 3: The Structure ----------
    slide(8, 'slide-dark', 3,
          '<strong>Transicao grammar (1 min):</strong> Diga: \'Now, HOW do you write each part? Let us discover the formulas together.\' Passe ao proximo.',
          '''    <div style="text-align:center">
    <div class="chapter-label">Chapter 3</div>
    <h2 class="slide-heading" style="font-size:2rem">The <span class="accent">Formulas</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">Open, request and close like a professional</p>
    </div>''', bg=True)

    slide(9, 'slide-light', 3,
          '<strong>Grammar discovery (4 min):</strong> Leia os 4 exemplos. Pergunte \'What do these phrases have in common? Are they formal or informal?\'. Clique \'Reveal the Rule\'. Reforce: regarding = topic; Please find attached = anexo; Could you please...? = pedido educado; I look forward... = fechamento.',
          '''    <div class="chapter-label">Discover the Rule</div>
    <h2 class="slide-heading">Listen and <span class="accent">Notice</span></h2>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:560px;margin:1rem auto 0">
      %s
      %s
      %s
      %s
    </div>
    <button class="primary-btn" style="margin:1.2rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer" onclick="var t=document.getElementById('rule3');t.style.display=(t.style.display==='none'||!t.style.display)?'block':'none'">Reveal the Rule</button>
    <div id="rule3" style="display:none;max-width:560px;margin:1rem auto 0;overflow-x:auto">
      <table style="width:100%%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.6rem;text-align:left">Part</th><th style="padding:.6rem;text-align:left">Formula</th><th style="padding:.6rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.5rem;font-weight:600">Open</td><td style="padding:.5rem">I am writing regarding + topic</td><td style="padding:.5rem">I am writing regarding the contract.</td></tr>
          <tr style="background:var(--bg-elevated);border-bottom:1px solid var(--border)"><td style="padding:.5rem;font-weight:600">Body</td><td style="padding:.5rem">Please find + (file) + attached / Could you please + verb?</td><td style="padding:.5rem">Please find the report attached.</td></tr>
          <tr><td style="padding:.5rem;font-weight:600">Close</td><td style="padding:.5rem">I look forward to your reply. Best regards,</td><td style="padding:.5rem">I look forward to your reply.</td></tr>
        </tbody>
      </table>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem;text-align:center">These are <strong>formal</strong> phrases -- perfect for clients and contracts.</p>
    </div>''' % (
        reveal_phrase('"<span class="accent" style="font-weight:700">I am writing regarding</span> the contract."', 'I am writing regarding the contract.'),
        reveal_phrase('"<span class="accent" style="font-weight:700">Please find</span> the report <span class="accent" style="font-weight:700">attached</span>."', 'Please find the report attached.'),
        reveal_phrase('"<span class="accent" style="font-weight:700">Could you please</span> send me the document?"', 'Could you please send me the document?'),
        reveal_phrase('"<span class="accent" style="font-weight:700">I look forward to</span> your reply."', 'I look forward to your reply.')))

    slide(10, 'slide-light', 3,
          '<strong>Common mistake (3 min):</strong> Mostre os erros: \'I send you in attach\' (use Please find attached) e \'I wait your reply\' (use I look forward to your reply). Mostre certo (verde) e errado (vermelho).',
          '''    <div class="chapter-label">Common Mistake</div>
    <h2 class="slide-heading">Right vs <span class="accent">Wrong</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;max-width:520px;margin:1.2rem auto 0">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem">
        <div style="background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--danger);font-weight:700;margin-bottom:.3rem">&#10007; WRONG</p><p style="font-size:.88rem">"I send you the report in attach."</p></div>
        <div style="background:var(--success-bg);border:1px solid var(--success-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--success);font-weight:700;margin-bottom:.3rem">&#10003; RIGHT</p><p style="font-size:.88rem">"<strong>Please find</strong> the report <strong>attached</strong>."</p></div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem">
        <div style="background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--danger);font-weight:700;margin-bottom:.3rem">&#10007; WRONG</p><p style="font-size:.88rem">"I wait your reply."</p></div>
        <div style="background:var(--success-bg);border:1px solid var(--success-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--success);font-weight:700;margin-bottom:.3rem">&#10003; RIGHT</p><p style="font-size:.88rem">"I <strong>look forward to</strong> your reply."</p></div>
      </div>
    </div>''')

    slide(11, 'slide-light', 3,
          '<strong>Grammar practice (3 min):</strong> Leia cada frase com o espaco. Peca Simone completar ORALMENTE antes de revelar.',
          '''    <div class="chapter-label">Grammar Practice</div>
    <h2 class="slide-heading">Complete the <span class="accent">Email</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:550px;margin:1.2rem auto 0">
%s
    </div>''' % '\n'.join(
        '      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem"><p style="font-size:.9rem">%s <span style="color:var(--accent);font-weight:600;cursor:pointer;font-size:.8rem" onclick="this.textContent=this.textContent===\'[show]\'?\'%s\':\'[show]\'">[show]</span></p></div>' % (q, a)
        for q, a in [
            ('"I am writing _____ the contract."', 'regarding'),
            ('"Please _____ the report attached."', 'find'),
            ('"_____ you please reply by Friday?"', 'Could'),
            ('"I look _____ to your reply."', 'forward'),
            ('"Best _____, Simone."', 'regards'),
        ]))

    # ---------- PHASE 4: The Email ----------
    slide(12, 'slide-dark', 4,
          '<strong>Transicao contexto (1 min):</strong> Diga: \'Look at a real corporate email. Let us read it together.\' Passe ao proximo.',
          '''    <div style="text-align:center">
    <div class="chapter-label">Chapter 4</div>
    <h2 class="slide-heading" style="font-size:2rem">A Real <span class="accent">Email</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">From Simone to a client</p>
    </div>''', bg=True)

    slide(13, 'slide-light', 4,
          '<strong>Artifact -- email (3 min):</strong> Mostre o email. Peca Simone ler o subject line, o recipient, a frase do attachment e o fechamento. Pergunte: \'What is the email regarding? Where is the attachment mentioned?\'',
          '''    <div class="chapter-label">Artifact</div>
    <h2 class="slide-heading">The <span class="accent">Email</span></h2>
    <div class="email-card" style="max-width:420px;margin:1.2rem auto 0;background:#fff;border:1px solid var(--border);border-radius:12px;padding:0;box-shadow:0 4px 20px rgba(0,0,0,.08);overflow:hidden;text-align:left">
      <div style="background:var(--accent);color:#fff;padding:.7rem 1rem;font-size:.8rem;font-weight:600">New Message</div>
      <div style="padding:1rem;font-size:.82rem;line-height:1.7">
        <div style="display:flex;gap:.5rem;border-bottom:1px solid var(--border);padding-bottom:.4rem"><span style="color:var(--text-dim);min-width:64px">To:</span><span style="font-weight:600">m.carter@client.com</span></div>
        <div style="display:flex;gap:.5rem;border-bottom:1px solid var(--border);padding:.4rem 0"><span style="color:var(--text-dim);min-width:64px">Subject:</span><span style="font-weight:600">Service Contract -- Telefonica</span></div>
        <div style="display:flex;gap:.5rem;border-bottom:1px solid var(--border);padding:.4rem 0;align-items:center"><span style="color:var(--text-dim);min-width:64px">Attachment:</span><span style="display:inline-flex;align-items:center;gap:.3rem;background:var(--accent-dim);border:1px solid var(--accent);border-radius:6px;padding:.15rem .5rem;font-size:.75rem"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M21 11l-8.5 8.5a5 5 0 01-7-7L14 4a3.5 3.5 0 015 5l-9 9a2 2 0 01-3-3l8.5-8.5"/></svg> contract.pdf</span></div>
        <p style="margin-top:.7rem">Dear Mr. Carter,</p>
        <p style="margin-top:.5rem">I am writing <strong>regarding</strong> our service contract. Please find the signed document <strong>attached</strong>. Could you please review it and <strong>reply</strong> by Friday?</p>
        <p style="margin-top:.5rem">I look forward to your reply.</p>
        <p style="margin-top:.5rem"><strong>Best regards</strong>,<br>Simone</p>
      </div>
    </div>''')

    slide(14, 'slide-dark', 4,
          "<strong>Listening 1 (4 min):</strong> Diga: 'Listen to Simone's email read aloud. Close your eyes and just listen.' Toque o audio. NAO mostre o texto antes.",
          '''    <div style="text-align:center">
    <div class="chapter-label">Listening 1</div>
    <h2 class="slide-heading" style="color:#fff">The <span class="accent">Email</span> Aloud</h2>
    <p style="color:rgba(255,255,255,.6);font-size:.9rem;margin-top:.5rem;margin-bottom:1.5rem">Listen to the full email. Close your eyes and focus.</p>
    <div style="max-width:400px;margin:0 auto;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:12px;padding:1.2rem">
      <button class="audio-btn" onclick="speakText('listening3_email',this)" style="width:100%;padding:.8rem;font-size:1rem">&#9654; Play the Email</button>
      <p style="color:rgba(255,255,255,.5);font-size:.75rem;margin-top:.5rem">Duration: ~30 sec</p>
    </div>
    </div>''', bg=True)

    slide(15, 'slide-light', 4,
          '<strong>Listening 2 + comprehension (4 min):</strong> Diga: \'Now Simone leaves a follow-up message.\' Toque o audio. Depois faca as 3 perguntas. Clique para revelar.',
          '''    <div class="chapter-label">Listening 2</div>
    <h2 class="slide-heading">The <span class="accent">Follow-up</span></h2>
    <div style="max-width:420px;margin:1rem auto;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1.1rem;text-align:center">
      <button class="audio-btn" onclick="speakText('listening3_followup',this)" style="width:100%%;padding:.8rem;font-size:1rem">&#9654; Play the Message</button>
      <p style="color:var(--text-dim);font-size:.75rem;margin-top:.5rem">Simone follows up on her email.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:520px;margin:1rem auto 0">
      %s
      %s
      %s
    </div>''' % (
        comp_q('1. Why is Simone calling?', 'To follow up on her email.'),
        comp_q('2. What did she send last week?', 'An email regarding the contract.'),
        comp_q('3. What does she want the client to confirm?', 'That they received the attachment.')))

    dlg = [
        ('David', 'arthur', 'Hi Simone, did you send the email to the client?', 'Hi Simone, did you send the email to the client?', False),
        ('Simone', 'ellen', 'Not yet. I am writing it now, regarding the new contract.', 'Not yet. I am writing it now, regarding the new contract.', True),
        ('David', 'arthur', 'Great. Please attach the signed document.', 'Great. Please attach the signed document.', False),
        ('Simone', 'ellen', 'Of course. I will add it as an <strong>attachment</strong>.', 'Of course. I will add it as an attachment.', True),
        ('David', 'arthur', 'Can you also <strong>forward</strong> it to the legal team?', 'Can you also forward it to the legal team?', False),
        ('Simone', 'ellen', 'Sure. I will <strong>forward</strong> it to them today.', 'Sure. I will forward it to them today.', True),
        ('David', 'arthur', 'Perfect. Ask them to <strong>reply</strong> by Friday.', 'Perfect. Ask them to reply by Friday.', False),
        ('Simone', 'ellen', 'I will. I will also <strong>follow up</strong> on Monday.', 'I will. I will also follow up on Monday.', True),
        ('David', 'arthur', 'Excellent. How do you close the email?', 'Excellent. How do you close the email?', False),
        ('Simone', 'ellen', 'I always write <strong>Best regards</strong> and my name.', 'I always write Best regards and my name.', True),
        ('David', 'arthur', 'That is very professional. Thank you, Simone.', 'That is very professional. Thank you, Simone.', False),
        ('Simone', 'ellen', 'You are welcome. I will send it now.', 'You are welcome. I will send it now.', True),
    ]
    dlg_html = '\n'.join(dlg_line(i + 1, sp, v, tx, pl, st) for i, (sp, v, tx, pl, st) in enumerate(dlg))
    slide(16, 'slide-dark', 4,
          '<strong>Dialogo (6 min):</strong> Diga: \'Now the conversation step by step. I am David, your colleague in London. You are Simone.\' Clique \'Next Line\' para revelar cada fala. Para cada fala de Simone, peca que ELA fale antes de tocar o audio.',
          '''    <div class="chapter-label">At the Office</div>
    <h2 class="slide-heading" style="color:#fff">Sending the <span class="accent">Email</span></h2>
    <div class="dialogue-box" id="dialogue3">
%s
    </div>
    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin:1.2rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Next Line</button>''' % dlg_html)

    slide(17, 'slide-light', 4,
          '<strong>Comprehension (2 min):</strong> Pergunte sobre o DAVID (o colega), nao sobre Simone. Clique para revelar.',
          '''    <div class="chapter-label">Comprehension</div>
    <h2 class="slide-heading">About <span class="accent">David</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;max-width:520px;margin:1.2rem auto 0">
      %s
      %s
      %s
    </div>''' % (
        comp_q('What does David ask Simone to attach?', 'The signed document.'),
        comp_q('Who should Simone forward the email to?', 'The legal team.'),
        comp_q('When should the legal team reply?', 'By Friday.')))

    # ---------- PHASE 5: Practice ----------
    slide(18, 'slide-dark', 5,
          '<strong>Transicao Quick Fire (1 min):</strong> Diga: \'Great! Now fast practice. I give you a situation, you give me the email phrase. Ready?\' Passe ao proximo.',
          '''    <div style="text-align:center">
    <div class="chapter-label">Chapter 5</div>
    <h2 class="slide-heading" style="font-size:2rem">Quick <span class="accent">Fire</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">6 situations -- Answer fast!</p>
    </div>''', bg=True)

    slide(19, 'slide-light', 5,
          '<strong>Quick Fire (5 min):</strong> Leia cada situacao. Espere 5-10 segundos. Se Simone travar, de a primeira palavra. Clique \'Show Answer\' so se ela travar.',
          '''    <div class="chapter-label">Quick Fire</div>
    <h2 class="slide-heading">Situation <span class="accent">Challenge</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:560px;margin:1.2rem auto 0">
%s
    </div>''' % '\n'.join(qf_item(i + 1, s, a) for i, (s, a) in enumerate([
        ('Start a formal email to Mr. Carter.', 'Dear Mr. Carter, I hope this email finds you well.'),
        ('Say the email is about the contract.', 'I am writing regarding the contract.'),
        ('Tell him the document is attached.', 'Please find the document attached.'),
        ('Ask him to reply by Friday.', 'Could you please reply by Friday?'),
        ('Close the email politely.', 'Best regards, Simone.'),
        ('Say you will follow up next week.', 'I will follow up next week.'),
    ])))

    slide(20, 'slide-light', 5,
          '<strong>Spot the Error (3 min):</strong> Leia cada frase com erro. Pergunte \'What is wrong here?\'. Clique para revelar a correcao.',
          '''    <div class="chapter-label">Spot the Error</div>
    <h2 class="slide-heading">Find the <span class="accent">Mistake</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:560px;margin:1.2rem auto 0">
      %s
      %s
      %s
      %s
    </div>''' % (
        err_card('I send you the contract in attach.', 'Please find the contract attached. (Please find ... attached)'),
        err_card('I am writing about regarding the contract.', 'I am writing regarding the contract. (not "about regarding")'),
        err_card('I wait your reply.', 'I look forward to your reply.'),
        err_card('Reply me until Friday.', 'Could you please reply by Friday? (reply TO me, BY Friday)')))

    slide(21, 'slide-light', 5,
          '<strong>Oral Drilling (3 min):</strong> Toque cada audio. Peca Simone repetir IMEDIATAMENTE. Foque em ritmo e fluidez.',
          '''    <div class="chapter-label">Oral Drilling</div>
    <h2 class="slide-heading">Repeat <span class="accent">After</span> the Audio</h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:540px;margin:1.2rem auto 0">
      %s
      %s
      %s
      %s
    </div>''' % (
        oral_item('I am writing regarding the contract.'),
        oral_item('Please find the document attached.'),
        oral_item('Could you please reply by Friday?'),
        oral_item('I look forward to your reply.')))

    slide(22, 'slide-light', 5,
          '<strong>Error Correction (3 min):</strong> Anote os erros que Simone cometeu durante a aula. Digite no campo editavel. Leia cada erro e peca a correcao.',
          '''    <div class="chapter-label">Error Correction</div>
    <h2 class="slide-heading">Let's <span class="accent">Fix</span> These</h2>
    <p style="font-size:.9rem;color:var(--text-dim);margin-bottom:1rem;max-width:500px;margin-left:auto;margin-right:auto">Errors from today's class:</p>
    <div class="error-correction-area" contenteditable="true" style="max-width:500px;margin:0 auto;min-height:150px;background:var(--bg-card);border:2px dashed var(--accent);border-radius:10px;padding:1.2rem;font-size:.9rem;line-height:1.8;outline:none"></div>''')

    # ---------- PHASE 6: Your Turn ----------
    slide(23, 'slide-dark', 6,
          '<strong>Transicao Role-play (1 min):</strong> Diga: \'Now YOU write the email out loud. Three role-plays: guided, semi-free, free. Ready?\' Passe ao proximo.',
          '''    <div style="text-align:center">
    <div class="chapter-label">Chapter 6</div>
    <h2 class="slide-heading" style="font-size:2rem">Your <span class="accent">Turn</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">Guided &gt; Semi-free &gt; Free</p>
    </div>''', bg=True)

    slide(24, 'slide-light', 6,
          '<strong>Role-play Guided (4 min):</strong> Voce e Mr. Carter, o cliente. Simone abre o email e diz o assunto. De as keywords na tela.',
          '''    <div class="chapter-label">Role-Play: Guided</div>
    <h2 class="slide-heading">Open the <span class="accent">Email</span></h2>
    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,var(--accent-dim),rgba(136,19,55,.05));border:1px solid var(--accent);border-radius:12px;padding:1.5rem">
      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> Greet the client and say the email is regarding the contract.</p>
      <p style="font-size:.85rem;font-weight:600;margin-bottom:.5rem">Keyword chips:</p>
      <div style="display:flex;flex-wrap:wrap;gap:.4rem">
        <span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;padding:.3rem .7rem;font-size:.8rem">Dear Mr. Carter</span>
        <span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;padding:.3rem .7rem;font-size:.8rem">I am writing regarding...</span>
        <span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;padding:.3rem .7rem;font-size:.8rem">the contract</span>
      </div>
    </div>''')

    slide(25, 'slide-light', 6,
          '<strong>Role-play Semi-free (4 min):</strong> Voce e Mr. Carter. Simone menciona o anexo e faz o pedido de resposta. Menos pistas.',
          '''    <div class="chapter-label">Role-Play: Semi-free</div>
    <h2 class="slide-heading">Attach and <span class="accent">Request</span></h2>
    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba(136,19,55,.08),rgba(136,19,55,.02));border:1px solid var(--accent);border-radius:12px;padding:1.5rem">
      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> Say the document is attached and ask the client to reply by Friday.</p>
      <p style="font-size:.85rem;font-weight:600;margin-bottom:.5rem">Keywords:</p>
      <div style="display:flex;flex-wrap:wrap;gap:.4rem">
        <span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;padding:.3rem .7rem;font-size:.8rem">Please find attached</span>
        <span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;padding:.3rem .7rem;font-size:.8rem">Could you please...?</span>
        <span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;padding:.3rem .7rem;font-size:.8rem">by Friday</span>
      </div>
    </div>''')

    slide(26, 'slide-light', 6,
          '<strong>Role-play Free (4 min):</strong> Voce e Mr. Carter. Simone escreve o email INTEIRO em voz alta: abre, diz o assunto, menciona o anexo, pede resposta e fecha. ZERO pistas. CELEBRE.',
          '''    <div class="chapter-label">Role-Play: Free</div>
    <h2 class="slide-heading">The Whole <span class="accent">Email</span></h2>
    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba(136,19,55,.12),rgba(136,19,55,.03));border:1px solid var(--accent);border-radius:12px;padding:1.5rem">
      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> Write the full email out loud: open formally, say it is regarding the contract, mention the attachment, ask for a reply by Friday, and close with Best regards.</p>
      <p style="font-size:.85rem;color:var(--text-dim);font-style:italic">No keywords. You are on your own!</p>
    </div>''')

    # ---------- PHASE 7: Wrap-Up ----------
    checks = [
        'I can open an email: "I am writing regarding..."',
        'I can mention an attachment: "Please find ... attached."',
        'I can make a polite request: "Could you please ...?"',
        'I can close an email: "I look forward to your reply. Best regards,"',
        'I know the words: subject line, recipient, attachment, forward, reply, follow up.',
    ]
    checks_html = '\n'.join(
        '        <div class="check-item" onclick="toggleCheck(this)" style="background:rgba(255,255,255,.95);border-radius:8px;padding:.7rem 1rem;display:flex;align-items:center;gap:.6rem;cursor:pointer"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div><span style="font-size:.88rem;color:#1a1a2e">%s</span></div>' % c
        for c in checks)
    slide(27, 'slide-dark', 7,
          '<strong>Checklist (2 min):</strong> Diga: \'Let us review what you can do now. Check each item if you feel confident.\' Leia cada item. Todos os 5 checks = aula completa.',
          '''    <div style="text-align:center">
    <div class="chapter-label">What I Learned</div>
    <h2 class="slide-heading" style="color:#fff">Lesson 3 <span class="accent">Checklist</span></h2>
    <div style="max-width:480px;margin:1.2rem auto 0;text-align:left">
      <div id="checklist-3" class="check-grid" style="display:flex;flex-direction:column;gap:.6rem">
%s
      </div>
    </div>
    </div>''' % checks_html)

    slide(28, 'slide-dark', 7,
          '<strong>Encerramento (2 min):</strong> Diga: \'Day 3 is complete, Simone! You earned your Email Pro Badge!\' Homework (oralmente): 1) Escrever uma resposta a um email ficticio de um cliente (abrir, anexo, pedido, fechar). 2) Gravar um audio lendo o seu email em voz alta. Proxima aula: Phone and Video Calls.',
          '''    <div style="text-align:center">
    <div class="badge-card">
      <div class="badge-icon">
        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 4h16v16H4z"/><path d="M4 6l8 6 8-6"/></svg></div>
        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>
      </div>
      <h2 class="slide-heading" style="color:#fff">Email Pro Badge <span class="accent">Earned!</span></h2>
      <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">You can write a corporate email in English now, Simone.</p>
      <p style="color:rgba(255,255,255,.7);font-size:.85rem;margin-top:1.5rem">Day 3 -- Complete.</p>
      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">Next lesson: Phone and Video Calls</p>
    </div>
    </div>''', bg=True)

    return '\n\n'.join(S)
