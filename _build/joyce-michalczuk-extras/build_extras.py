# -*- coding: utf-8 -*-
"""Abas suplementares da Joyce Michalczuk: Your Daily Plan, Shadowing, Explain Brazil.

Pedidos dela na consultoria de 29/09/2026: 'me fala o que fazer, shadow 30 minutos, ler uma hora'
(direcao em minutos), 4 a 6 horas de estudo por dia, e a dor central: explicar ICMS, VAT e a
reforma tributaria ao time global. Tudo em ingles na tela (B1). So chama funcoes que ja existem
no hub (toggleLesson, speakText, speakPhrase, startRecording, stopRecording,
startFreeRecording, stopFreeRecording). Sem fill-in, matching nem quiz: nada que o loadState
restaure por texto e possa colidir com as aulas."""
import html as H
import os

AQUI = os.path.dirname(os.path.abspath(__file__))


def q(s):
    return s.replace('"', '&quot;')


def card_open(cid, img, num, title, desc):
    return (f'<div class="lesson-card" id="{cid}">\n  <div class="lesson-header" onclick="toggleLesson(this)">\n'
            f'    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/{img}?w=600&q=80\')"></div>\n'
            f'    <div class="lesson-header-content">\n      <div class="lesson-number">{num}</div>\n      <h3>{title}</h3>\n'
            f'      <div class="lesson-desc">{desc}</div>\n    </div>\n    <div class="expand-icon">&#9660;</div>\n  </div>\n  <div class="lesson-body">\n')


CARD_CLOSE = '  </div>\n</div>\n'


def section(title, badge_cls, badge, instr, body):
    return (f'\n    <div class="exercise-section">\n      <div class="section-header-row"><h4>{title}</h4><span class="badge {badge_cls}">{badge}</span></div>\n'
            f'      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{instr}</p>\n{body}    </div>\n')


def speech(p):
    return (f'      <div class="speech-card" data-phrase="{q(p)}">\n        <div class="speech-phrase">{p}</div>\n'
            '        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
            '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div>\n'
            '        <div class="speech-result"></div>\n      </div>\n')


def free(rid, prompt):
    return (f'      <div class="think-card">\n        <div class="think-question">{prompt}</div>\n'
            '        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button>'
            '<button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div>\n'
            f'        <div id="{rid}"></div>\n      </div>\n')


def listen_btn(text, accent):
    return (f'      <button class="audio-btn" data-accent="{accent}" data-speak="{q(text)}" onclick="speakText(this.dataset.speak,this)" '
            'style="margin-bottom:1rem">Listen</button>\n')


def transcript(text):
    return ('      <details style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:.7rem 1rem;margin-bottom:.8rem">'
            '<summary style="cursor:pointer;font-size:.85rem;font-weight:600;color:var(--accent)">Transcript</summary>'
            f'<p style="font-size:.9rem;line-height:1.7;margin-top:.6rem">{text}</p></details>\n')


def tab(slot, title, intro, body):
    return (f'<!-- ========== EXTRAS: {title.upper()} (aditivo) ========== -->\n<div class="tab-content" id="tab-{slot}">\n'
            f'<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;margin-bottom:1rem">{title}</h3>\n'
            f'<p style="font-size:.85rem;color:var(--text-dim);margin-bottom:1.5rem">{intro}</p>\n{body}</div><!-- /tab-{slot} -->\n')


def rule_box(label, text):
    return (f'<div style="margin:.2rem 0 1.2rem;padding:.9rem 1.1rem;background:var(--accent-dim);border-left:3px solid var(--accent);'
            f'border-radius:0 8px 8px 0;font-size:.85rem;line-height:1.65;color:var(--text-mid)"><strong style="color:var(--accent)">{label}</strong> {text}</div>\n')


def table(head, rows):
    th = ''.join(f'<th style="text-align:left;padding:.6rem .7rem">{h}</th>' for h in head)
    tr = ''
    for r in rows:
        tds = ''.join(f'<td style="padding:.6rem .7rem;border-top:1px solid var(--border){";font-weight:600;white-space:nowrap" if i == 0 else ""}'
                      f'{";white-space:nowrap;color:var(--accent);font-weight:600" if i == len(r) - 1 else ""}">{c}</td>' for i, c in enumerate(r))
        tr += f'      <tr>{tds}</tr>\n'
    return ('<div style="overflow-x:auto;margin-bottom:1.5rem">\n<table style="width:100%;min-width:520px;border-collapse:collapse;font-size:.86rem;'
            f'background:var(--bg-card);border:1px solid var(--border);border-radius:8px">\n      <tr>{th}</tr>\n{tr}</table>\n</div>\n')


def bullets(title, items):
    li = ''.join(f'        <li style="margin-bottom:.45rem">{i}</li>\n' for i in items)
    return (f'<div class="exercise-section">\n  <div class="section-header-row"><h4>{title}</h4></div>\n'
            f'  <ul style="font-size:.88rem;line-height:1.6;color:var(--text-mid);padding-left:1.2rem;margin:0">\n{li}  </ul>\n</div>\n')


# ======================= 1. YOUR DAILY PLAN =======================
DAILY = tab('dailyplan', 'Your Daily Plan',
    'You told us: tell me what to do, and for how long. This is the answer. Four hours a day from Wednesday to Friday, five on the weekend, '
    'and a short plan for Monday and Tuesday, when you are at the office. Every block has one job, and the reason is next to it.',
    rule_box('The one rule.', 'Speak out loud every single day, even on the busy days. You said it yourself: you only learned to drive when you drove every day. '
             'Ten minutes of speaking beats two hours of reading.') +
    table(['Day', 'What to do', 'Time'], [
        ('Monday', 'On the way to the office: one podcast or talk from the Complementary tab, just listening &middot; at night: record your 60-second introduction', '30 min'),
        ('Tuesday', 'On the way: one Shadowing card, listening only &middot; at night: one card of Explain Brazil, recorded', '30 min'),
        ('Wednesday', 'Class &middot; Pre-class of the next lesson &middot; Complementary of today &middot; Shadowing 30 min &middot; reading out loud 45 min &middot; one Explain Brazil card &middot; review of your recordings', '4 h'),
        ('Thursday', 'Class &middot; Pre-class of the next lesson &middot; Shadowing 30 min &middot; one long listening (a talk or a podcast episode) &middot; reading out loud 45 min', '4 h'),
        ('Friday', 'Class &middot; Pre-class of the next lesson &middot; Shadowing 30 min &middot; write and record your status of the week in 45 seconds', '4 h'),
        ('Saturday', 'Class &middot; Pre-class of the next lesson &middot; a full episode of a series in English, in three passes &middot; Shadowing 45 min &middot; mock meeting with yourself', '5 h'),
        ('Sunday', 'No class &middot; review the week: listen to Monday&rsquo;s recording and record it again &middot; the two hardest Shadowing cards &middot; reading out loud &middot; plan the week', '5 h'),
    ]) +
    table(['Block', 'How to do it', 'Why'], [
        ('Shadowing', 'Play one sentence, pause, say it at the same speed with the same melody. Then the whole text with the audio, three times.', 'Rhythm and pronunciation'),
        ('Reading out loud', 'A real article about finance or the tax reform, in English. Read it out loud, standing up, slower than you think.', 'Your mouth learns the long words'),
        ('Recording', 'Record, listen once, write one thing to fix, record again. Keep the first recording of each week.', 'You hear your own progress'),
        ('Long listening', 'A talk or a podcast from the Complementary tab. First without the transcript, then with it.', 'Your listening is strong: keep it'),
        ('Mock meeting', 'Stand up, set a timer, and give your status, your reform explanation and one answer to a hard question, as if the camera were on.', 'Pressure, without the risk'),
    ]) +
    bullets('How to shadow, step by step', [
        'Choose one card from the Shadowing tab. Do not change cards for three days: repetition is the method.',
        'Day 1: listen three times without reading. Then open the transcript and read along.',
        'Day 2: one sentence at a time. Play, pause, repeat. Copy the speed, the pauses and where the voice goes down.',
        'Day 3: say the whole text together with the audio, three times. Record the last one.',
    ]) +
    bullets('The week of a real global meeting', [
        'Three days before: rehearse the 3-minute update from lesson 8, out loud, with a timer, once a day.',
        'Two days before: write the three questions you fear most and answer each one with one point and one reason.',
        'The day before: one Shadowing card with the accent of the person who will be in the meeting.',
        'One hour before: say your first sentence out loud three times. Nothing new on the day.',
    ]))

# ======================= 2. SHADOWING =======================
SHADOW = [
    ('ny_f', 'American', 'The Monthly Close', 'photo-1600880292203-757bb62b4baf',
     "Quick update on the close. We have finished the bank reconciliations and the fixed assets. We are still waiting for three supplier invoices, "
     "so the accruals are not final yet. The main risk is the intercompany balance with Mexico, which did not match last month either. "
     "I am meeting their controller tomorrow at nine. You will have the final numbers by Thursday at noon.",
     ["We have finished the bank reconciliations and the fixed assets.",
      "The main risk is the intercompany balance with Mexico.",
      "You will have the final numbers by Thursday at noon."]),
    ('us_m', 'American', 'Bad News, Clear Structure', 'photo-1454165804606-c3d57bc86b40',
     "I want to flag a problem early. The tax provision for the quarter is higher than we forecast, by about four percent. "
     "The reason is a change in the state rules that came out last week. We have already asked our advisors to review it. "
     "I do not have the final number yet. I will get back to you by Monday with the updated figure and one option to reduce it.",
     ["I want to flag a problem early.",
      "The reason is a change in the state rules that came out last week.",
      "I do not have the final number yet."]),
    ('indian_f', 'Indian', 'The Shared Service Center', 'photo-1521737604893-d14cc237f11d',
     "Good morning, everyone. From the shared service center side, invoice processing for Brazil is on track this month. "
     "We processed ninety-two percent within three days, which is our best result this year. The only open point is the new invoice layout "
     "for the reform. Our team needs the final field list by the fifteenth, otherwise the January invoices will be delayed.",
     ["Invoice processing for Brazil is on track this month.",
      "The only open point is the new invoice layout.",
      "Our team needs the final field list by the fifteenth."]),
    ('german_f', 'German', 'The Director in Zurich', 'photo-1486406146926-c627a92ad1ab',
     "Thank you for the presentation. I have two comments. First, the numbers are clear, but I am missing the impact on cash, not only on profit. "
     "Second, I would like to see the timeline on one page, with the decisions we need from headquarters and the dates. "
     "Please send both before Friday, so we can discuss them in the board meeting next week.",
     ["I am missing the impact on cash, not only on profit.",
      "I would like to see the timeline on one page.",
      "Please send both before Friday."]),
    ('french_m', 'French', 'The CFO in Paris', 'photo-1542744173-8e7e53415bb0',
     "Joyce, I understand the logic of the reform, I think. But let me be honest, for us in Paris the question is simple. "
     "Is Brazil becoming easier or more difficult for the group in the next three years? Because we are deciding now where to invest, "
     "and I need to explain Brazil to my own board in two sentences. Can you help me with those two sentences?",
     ["Let me be honest.",
      "Is Brazil becoming easier or more difficult for the group?",
      "Can you help me with those two sentences?"]),
    ('indian_m', 'Indian', 'The Tax Colleague in Bangalore', 'photo-1515187029135-18ee286d815b',
     "When India moved to the goods and services tax, the first year was very hard. Systems were not ready and suppliers made mistakes on invoices. "
     "My advice for Brazil is to start the supplier checks early. Test the new invoice fields with your ten biggest suppliers first. "
     "If those ten are correct, most of the volume is correct, and the rest you can fix step by step.",
     ["The first year was very hard.",
      "Test the new invoice fields with your ten biggest suppliers first.",
      "The rest you can fix step by step."]),
    ('british_m', 'British', 'The Auditor', 'photo-1450101499163-c8848c66ca85',
     "Right, just a couple of points before we close the meeting. We are broadly comfortable with the tax provision, "
     "but we would like to see the calculation for the two largest entities in more detail. Could you share the working papers by Wednesday? "
     "And going forward, it would be helpful to document any judgement calls on the reform as they happen, not at year end.",
     ["We are broadly comfortable with the tax provision.",
      "Could you share the working papers by Wednesday?",
      "It would be helpful to document any judgement calls."]),
    ('us_m', 'American', 'Closing the Meeting', 'photo-1573164713988-8665fc963095',
     "OK, we are at time, so let me wrap up. Three decisions today. We keep the close calendar as it is. "
     "Brazil sends the reform timeline by Friday. And we review the cash impact in the next meeting. "
     "If I missed anything, please send me a note today. Thanks, everyone, and have a good week.",
     ["We are at time, so let me wrap up.",
      "Three decisions today.",
      "If I missed anything, please send me a note today."]),
]

sh_body = ''
for i, (acc, accname, title, img, text, lines) in enumerate(SHADOW, 1):
    sh_body += card_open(f'sh-card-{i}', img, f'Shadowing {i:02d} -- {accname}', title,
                         f'A real voice from a global call, about thirty to forty seconds. Three days with this card.')
    sh_body += section('Step 1: Listen, then read', 'badge-quiz', 'Listening',
                       'Listen three times with the transcript closed. Then open it and read along while you listen.',
                       listen_btn(text, acc) + transcript(text))
    sh_body += section('Step 2: One sentence at a time', 'badge-speak', 'Speaking',
                       'Listen, then say it at the same speed and with the same melody. Record, and compare.',
                       ''.join(speech(l) for l in lines))
    sh_body += section('Step 3: The whole text', 'badge-think', 'Recording',
                       'Play the full audio again. Then record the whole text yourself, at the same speed.',
                       free(f'sh-free-{i}', 'Say the whole text, as if you were the person in this meeting. Then listen: where did your speed or your melody change?'))
    sh_body += CARD_CLOSE

SHADOWING = tab('shadowing', 'Shadowing',
    'Eight real voices from the global calls you have every day: American, Indian, German, French and British. '
    'One card, three days: listen, copy one sentence at a time, then say the whole text with the same speed and melody. '
    'Start with the accent you find the hardest.', sh_body)

# ======================= 3. EXPLAIN BRAZIL =======================
BR = [
    ('ICMS', 'photo-1454165804606-c3d57bc86b40',
     "ICMS is a state tax on the sale of goods and on some services, like transport and communication. Each of the twenty-seven states sets its own rules and rates, "
     "and the tax is charged at every step of the chain, with a credit for what was paid before. That is why selling from one state to another is so complicated in Brazil.",
     ["ICMS is a state tax on the sale of goods.", "Each state sets its own rules and rates.",
      "Selling from one state to another is complicated."]),
    ('PIS and COFINS', 'photo-1600880292203-757bb62b4baf',
     "PIS and COFINS are two federal contributions calculated on revenue. Most large companies pay them in a system with credits, "
     "which works a bit like a VAT, but the rules on what gives a credit have always caused disputes. "
     "With the reform, both are replaced by a single federal tax, the CBS.",
     ["PIS and COFINS are two federal contributions on revenue.", "The rules on credits have always caused disputes.",
      "Both are replaced by a single federal tax, the CBS."]),
    ('IPI and ISS', 'photo-1521737604893-d14cc237f11d',
     "IPI is a federal tax on manufactured products, and ISS is a city tax on services. "
     "Brazil has more than five thousand cities, and each one can have its own ISS rules. "
     "With the reform, ISS disappears into the new IBS, and IPI goes to zero for almost all products.",
     ["IPI is a federal tax on manufactured products.", "ISS is a city tax on services.",
      "ISS disappears into the new IBS."]),
    ('The Reform in One Minute', 'photo-1486406146926-c627a92ad1ab',
     "In short, Brazil is moving to a dual VAT. Five old taxes are replaced by two new ones: the CBS, which is federal, and the IBS, "
     "which is shared by states and cities. The tax is charged at every step, with full credits, and it goes to the place where the product is consumed.",
     ["In short, Brazil is moving to a dual VAT.", "Five old taxes are replaced by two new ones.",
      "It goes to the place where the product is consumed."]),
    ('The Transition, 2026 to 2033', 'photo-1590602847861-f357a9332bbc',
     "The change does not happen in one day. 2026 is a test year, with very low rates. In 2027 the CBS starts for real and PIS and COFINS end. "
     "Between 2029 and 2032 the state and city taxes go down step by step while the IBS goes up, and in 2033 the old system is gone.",
     ["2026 is a test year, with very low rates.", "In 2027 the CBS starts for real.",
      "In 2033 the old system is gone."]),
    ('Split Payment', 'photo-1573164713988-8665fc963095',
     "Split payment means that when a customer pays an invoice, the tax part of the payment is separated automatically and goes to the government. "
     "The seller receives only the net amount. For the government it reduces fraud, and for companies it changes cash flow, because the tax never stays in your account.",
     ["The tax part of the payment is separated automatically.", "The seller receives only the net amount.",
      "It changes cash flow for companies."]),
    ('The Selective Tax', 'photo-1542744173-8e7e53415bb0',
     "The reform also creates a selective tax, a federal excise tax on products that are harmful to health or to the environment, "
     "like tobacco, alcohol and sugary drinks. It is charged only once, and its goal is to change behavior, not only to raise money.",
     ["The reform also creates a selective tax.", "It is charged only once.",
      "Its goal is to change behavior, not only to raise money."]),
    ('Why It Matters for the Group', 'photo-1515187029135-18ee286d815b',
     "For the group, the reform matters in three ways. Prices and margins change, because the tax on each product changes. "
     "Systems and invoices have to change, because the new taxes need new fields. And for a few years we run two systems at the same time, "
     "which means more work and more risk of errors.",
     ["For the group, the reform matters in three ways.", "Systems and invoices have to change.",
      "For a few years we run two systems at the same time."]),
]
br_body = ''
for i, (title, img, text, lines) in enumerate(BR, 1):
    br_body += card_open(f'br-card-{i}', img, f'Explain Brazil {i:02d}', title,
                         'A model explanation in three sentences, for somebody who has never paid a Brazilian tax. Then yours.')
    br_body += section('Step 1: Listen to the model', 'badge-quiz', 'Listening',
                       'Listen once. Notice the order: what it is, how it works, why it matters.',
                       listen_btn(text, 'us_f') + transcript(text))
    br_body += section('Step 2: Say the key sentences', 'badge-speak', 'Speaking',
                       'Listen, then record each sentence. Clear, not fast.',
                       ''.join(speech(l) for l in lines))
    br_body += section('Step 3: Your version', 'badge-think', 'Recording',
                       'Now explain it with your own words, to a real person on your global team. Three sentences, under thirty seconds.',
                       free(f'br-free-{i}', f'Explain {title} to your director in Zurich in three sentences: what it is, how it works, and why it matters for the group. Then add one comparison with something they already know.'))
    br_body += CARD_CLOSE

BRAZIL = tab('brazil', 'Explain Brazil',
    'You said it is hard to explain even in Portuguese. Here are the pieces of the Brazilian tax system, each one explained in three simple sentences '
    'for somebody in Zurich, Chicago or Bangalore. Listen to the model, say the key sentences, then record your own version. One card a day.',
    rule_box('The ladder from lesson 2.', 'What changes, one comparison with something they know, the impact, and what you need. '
             'If a sentence has an acronym, the next sentence explains it.') + br_body)

for nome, conteudo in [('dailyplan.html', DAILY), ('shadowing.html', SHADOWING), ('brazil.html', BRAZIL)]:
    open(os.path.join(AQUI, nome), 'w', encoding='utf-8').write(conteudo)
    print(nome, len(conteudo))
