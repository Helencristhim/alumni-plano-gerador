# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genlib

IMG = "https://images.unsplash.com/"
D = {
 'n': 22,
 'phases': ["Then and Now", "Change Words", "Used to", "The Story Behind the Numbers", "Practice", "Your Turn", "Wrap-up"],
 'bg': {
   'title': IMG + "photo-1551288049-bebda4e38f71?w=1200&q=80",
   'vocab': IMG + "photo-1454165804606-c3d57bc86b40?w=1200&q=80",
   'grammar': IMG + "photo-1517245386807-bb43f82c33c4?w=1200&q=80",
   'context': IMG + "photo-1542744173-8e7e53415bb0?w=1200&q=80",
   'practice': IMG + "photo-1600880292203-757bb62b4baf?w=1200&q=80",
   'production': IMG + "photo-1475721027785-f74eccf877e2?w=1200&q=80",
 },
 'title_a': "Numbers That", 'title_b': "Tell a Story",
 'subtitle1': "Then and now: used to for past habits",
 'hook_a': "Then and", 'hook_b': "Now",
 'hook_prompt': "Think about your first year in HR. What is one thing that was very different from today?",
 'recall_a': "From Meeting", 'recall_b': "to Story",
 'recall_text': "Last class you prepared the Sydney meeting with verb patterns. Today you tell the story behind your HR numbers: how things used to be and how they are now.",
 'recall_chips': ["suggest starting", "postpone", "look forward to"],
 'vocab_sub': "The words for telling how work has changed",
 'vocab_head1': ("Back Then and", "Nowadays"),
 'vocab_head2': ("Words for", "Change"),
 'vocab': [
   ("Back then", "at that time in the past", "", "Back then, we used to print every contract."),
   ("Nowadays", "at the present time, different from the past", "", "Nowadays, we sign contracts online."),
   ("Paperwork", "the documents and forms you have to complete", "", "We used to spend hours on paperwork."),
   ("Timesheet", "a record of the hours a person works", "", "Employees used to fill in paper timesheets."),
   ("Payroll", "the process of paying employees their salaries", "", "Payroll used to take three full days."),
   ("Outdated", "old and not useful anymore", "", "Our old evaluation form was outdated."),
   ("Digitize", "to change paper information into digital files", "", "We digitized all employee records in 2019."),
   ("Replace", "to put something new in the place of something old", "", "An app replaced the paper timesheets."),
   ("Hierarchy", "a system where people have different levels of power", "", "The hierarchy used to be very rigid."),
   ("Commute", "the trip between your home and your work", "", "My commute used to take two hours."),
   ("Hybrid", "partly at the office and partly at home", "", "Most of the HR team has a hybrid schedule now."),
   ("Evolve", "to change and develop slowly over time", "", "Our HR policies evolved a lot."),
 ],
 'concept_label': "Then and Now at a Glance",
 'concept_a': "Then or", 'concept_b': "Now?",
 'concept_sub': "Used to for the past; present simple for today",
 'concept_cols': [
   ("THEN: USED TO", "past habits and states that are not true now: used to print, used to take"),
   ("NOW: PRESENT SIMPLE", "the situation today: nowadays we sign, we work hybrid"),
 ],
 'concept_drill': [
   ("Say how contracts were in the past.", "We used to print every contract."),
   ("Say how contracts are today.", "Nowadays, we sign contracts online."),
   ("Say something you didn't have before.", "We didn't use to have a hybrid schedule."),
   ("Ask a colleague about the past.", "Did you use to work on Saturdays?"),
 ],
 'pron': [
   "We used to print every contract.",
   "Payroll used to take three days.",
   "We didn't use to have a hybrid schedule.",
   "Did you use to work on Saturdays?",
 ],
 'gram_title_a': "Used", 'gram_title_b': "To",
 'gram_title_sub': "Past habits and states that are not true now",
 'discovery': [
   ('"Back then, we <span class="accent" style="font-weight:700">used to print</span> every contract."', "Back then, we used to print every contract."),
   ('"Payroll <span class="accent" style="font-weight:700">used to take</span> three full days."', "Payroll used to take three full days."),
   ('"We <span class="accent" style="font-weight:700">didn\'t use to have</span> a hybrid schedule."', "We didn't use to have a hybrid schedule."),
   ('"<span class="accent" style="font-weight:700">Did</span> you <span class="accent" style="font-weight:700">use to work</span> on Saturdays?"', "Did you use to work on Saturdays?"),
 ],
 'rule_head': ["Form", "Use", "Example"],
 'rule_rows': [
   ("used to + base verb", "past habit or state, not true now", "We used to print every contract."),
   ("didn't use to + base verb", "negative (no -d after didn't)", "We didn't use to have a hybrid schedule."),
   ("Did + subject + use to ...?", "question (no -d after did)", "Did you use to work on Saturdays?"),
   ("present simple", "the situation today", "Nowadays, we sign contracts online."),
 ],
 'gpr_a': "Then or", 'gpr_b': "Now",
 'gpractice': [
   ('"Back then, we ', "used to print", ' every contract. (print)"'),
   ('"Payroll ', "used to take", ' three full days. (take)"'),
   ('"We ', "didn't use to have", ' a hybrid schedule. (not / have)"'),
   ('"', "Did you use to work", ' on Saturdays? (you / work)"'),
   ('"Nowadays, we ', "sign", ' contracts online. (sign)"'),
 ],
 'build1_label': "Build the Story",
 'build1_a': "Say the", 'build1_b': "Story",
 'build1': [
   ("we / used to / print / every contract", "We used to print every contract."),
   ("payroll / used to / take / three days", "Payroll used to take three days."),
   ("we / not / use to / have / a hybrid schedule", "We didn't use to have a hybrid schedule."),
   ("you / use to / work / on Saturdays? (question)", "Did you use to work on Saturdays?"),
   ("nowadays / we / sign / contracts online", "Nowadays, we sign contracts online."),
 ],
 'context_sub': "Preparing the HR story for the Sydney team",
 'dlg_title_a': "The Story Behind the", 'dlg_title_b': "Numbers",
 'dialogue': [
   ("E", "#1b4965", "ethan", "arthur",
    "Murielle, the Sydney team wants the story behind our HR numbers. How did things use to work here?",
    "Murielle, the Sydney team wants the story behind our HR numbers. How did things use to work here?"),
   ("M", "#86198F", "murielle", "ellen",
    '<span class="vocab-highlight">Back then</span>, we used to do everything on paper. The <span class="vocab-highlight">paperwork</span> never ended, and <span class="vocab-highlight">payroll</span> used to take three full days.',
    "Back then, we used to do everything on paper. The paperwork never ended, and payroll used to take three full days."),
   ("E", "#1b4965", "ethan", "arthur",
    "And turnover? I hear it used to be high.",
    "And turnover? I hear it used to be high."),
   ("M", "#86198F", "murielle", "ellen",
    'Yes, it used to be eighteen percent. <span class="vocab-highlight">Nowadays</span>, it is around nine percent.',
    "Yes, it used to be eighteen percent. Nowadays, it is around nine percent."),
   ("E", "#1b4965", "ethan", "arthur",
    'That\'s a great story. At my old company, turnover used to be high too, mostly because of the long <span class="vocab-highlight">commute</span>.',
    "That's a great story. At my old company, turnover used to be high too, mostly because of the long commute."),
   ("M", "#86198F", "murielle", "ellen",
    'That was our problem too. We didn\'t use to have a <span class="vocab-highlight">hybrid</span> schedule, and the <span class="vocab-highlight">hierarchy</span> was very rigid.',
    "That was our problem too. We didn't use to have a hybrid schedule, and the hierarchy was very rigid."),
   ("E", "#1b4965", "ethan", "arthur",
    "So what changed? Did the company use to resist new technology?",
    "So what changed? Did the company use to resist new technology?"),
   ("M", "#86198F", "murielle", "ellen",
    'A little. But in 2019 we <span class="vocab-highlight">digitized</span> all employee records, and an app <span class="vocab-highlight">replaced</span> the paper <span class="vocab-highlight">timesheets</span>. Our HR has really <span class="vocab-highlight">evolved</span>, and the old process looks <span class="vocab-highlight">outdated</span> now.',
    "A little. But in 2019 we digitized all employee records, and an app replaced the paper timesheets. Our HR has really evolved, and the old process looks outdated now."),
 ],
 'dlg_comp': [
   ("What does the Sydney team want, according to Ethan?", "The story behind the HR numbers."),
   ("What does Ethan say about his old company?", "Turnover used to be high there too, mostly because of the long commute."),
   ("What does Ethan ask about technology?", "If the company used to resist new technology."),
 ],
 'listenings': [
   {"title_a": "The Sydney", "title_b": "Story", "file": "a22_listening_sydney.mp3", "voice": "arthur",
    "text": ("Hi Murielle, it's Daniel from the Sydney office again. Thanks for the call last week. You asked me how "
             "our HR team used to work before the merger, so here is a quick answer. Ten years ago, we used to have "
             "four separate offices, and each office used to run its own payroll. Managers didn't use to share data, "
             "so nobody had the full picture. Recruitment used to take about three months. Nowadays, we have one HR "
             "system for the whole country, and we hire in about five weeks. People used to complain about the "
             "paperwork, but now most of it is digital. One thing hasn't changed: we still meet face to face every "
             "Friday morning. Speak soon."),
    "qs": [
      ("How many offices did they use to have?", "Four separate offices."),
      ("How long did recruitment use to take, and how long does it take now?", "About three months; now about five weeks."),
      ("What hasn't changed?", "They still meet face to face every Friday morning."),
    ]},
   {"title_a": "Reviews Then and", "title_b": "Now", "file": "a22_listening_reviews.mp3", "voice": "ellen",
    "text": ("When I started my career in HR, performance reviews used to happen once a year. Managers used to fill in "
             "a long form, and employees used to wait twelve months for any feedback. Most people hated it. Nowadays, "
             "many companies use short check-ins every month instead. Managers didn't use to talk about wellbeing, "
             "but today it is part of almost every conversation. Some things should stay the same, though. Good "
             "managers always listened carefully, and that is still the most important skill. So my advice is "
             "simple: keep what worked, and replace what is outdated."),
    "qs": [
      ("How often did performance reviews use to happen?", "Once a year."),
      ("What do many companies use instead today?", "Short check-ins every month."),
      ("What is still the most important skill, according to her?", "Listening carefully."),
    ]},
 ],
 'art_title_a': "HR Then and", 'art_title_b': "Now",
 'art_kicker': "Presentation Slide &middot; Minerva Foods HR",
 'art_subtitle': "For the Sydney Team -- The Story Behind Our Numbers",
 'art_lines': [
   "Turnover: 18% then, 9% now.",
   "Time to hire: 60 days then, 25 days now.",
   "Payroll: three days then, one morning now.",
   "Timesheets: paper then, a mobile app now.",
 ],
 'art_sign': "Prepared by: Murielle Xavier",
 'art_note': "Turn each line into two sentences: Turnover used to be 18%. Nowadays, it is 9%.",
 'quickfire': [
   ("Tell Ethan about an old habit: printing every contract.", "We used to print every contract."),
   ("Say payroll took three days in the past, but not now.", "Payroll used to take three days."),
   ("Ask a colleague about working on Saturdays in the past.", "Did you use to work on Saturdays?"),
   ("Say the company had no hybrid schedule before.", "We didn't use to have a hybrid schedule."),
   ("Compare contracts then and now.", "We used to print contracts. Nowadays, we sign them online."),
 ],
 'spot': [
   ("I use to work on Saturdays.", "I used to work on Saturdays. (past habit: used to)"),
   ("We didn't used to have a hybrid schedule.", "We didn't use to have a hybrid schedule. (after didn't: use to)"),
   ("Did you used to print the contracts?", "Did you use to print the contracts? (after did: use to)"),
   ("Payroll used to taking three days.", "Payroll used to take three days. (used to + base verb)"),
 ],
 'build2': [
   ("employees / used to / fill in / paper timesheets", "Employees used to fill in paper timesheets."),
   ("managers / not / use to / share / data", "Managers didn't use to share data."),
   ("my commute / used to / take / two hours", "My commute used to take two hours."),
   ("the company / use to / resist / change? (question)", "Did the company use to resist change?"),
   ("an app / replace / the paper timesheets (past simple)", "An app replaced the paper timesheets."),
 ],
 'production_sub': "From guided to free. Tell the story behind your numbers.",
 'roleplays': {
   'guided': {'h': ("Then and", "Now"),
     'scenario': "Ethan is preparing the slides for the Sydney team. Tell him three things HR used to do at Minerva Foods and what the team does nowadays.",
     'chips': ["we used to ...", "back then", "nowadays", "paperwork"]},
   'semi': {'h': ("The Sydney", "Question"),
     'scenario': "Daniel from Sydney asks how Brazilian HR used to work before the digital system. Explain two old habits and one thing you didn't use to have. Then ask him about the past in his office.",
     'chips': ["didn't use to", "Did you use to ...?", "digitize"]},
   'free': {'h': ("Your Career Then and", "Now"),
     'scenario': "Tell the story of your own career: how your work used to be when you started in HR and how it is today. Use used to, didn't use to, and nowadays.",
     'note': "No keywords. The stage is yours, Murielle!"},
 },
 'keyphrases': [
   "We used to print every contract.",
   "Payroll used to take three days.",
   "We didn't use to have a hybrid schedule.",
   "Did you use to work on Saturdays?",
   "Nowadays, we sign contracts online.",
 ],
 'checklist': [
   "I can talk about past habits with used to + base verb: We used to print every contract.",
   "I can make negatives with didn't use to: We didn't use to have a hybrid schedule.",
   "I can ask questions with Did you use to ...?: Did you use to work on Saturdays?",
   "I can tell the story behind HR numbers with back then and nowadays.",
   "I can use the new words: back then, nowadays, paperwork, timesheet, payroll, outdated, digitize, replace, hierarchy, commute, hybrid, evolve.",
 ],
 'badge_a': "Then and Now",
 'badge_text': "You can now tell the story behind your HR numbers, Murielle.",
 'next_lesson': "Recommending HR actions in executive meetings",
 # ----- Pre-class -----
 'pc_title': "Numbers That Tell a Story -- Used To",
 'pc_desc': "Telling the story behind HR numbers with used to for past habits and states (used to, didn't use to, Did you use to...?) and the present simple for today. New words: back then, nowadays, paperwork, timesheet, payroll, outdated, digitize, replace, hierarchy, commute, hybrid, evolve.",
 'gic_text': ("When I joined Minerva Foods, HR was very different. <strong>Back then</strong>, we <strong>used to "
              "do</strong> everything on paper, and the <strong>paperwork</strong> never ended. Employees "
              "<strong>used to fill in</strong> paper <strong>timesheets</strong> every week, and "
              "<strong>payroll used to take</strong> three full days. We <strong>didn't use to have</strong> a "
              "<strong>hybrid</strong> schedule, so many people had a long <strong>commute</strong>. Turnover "
              "<strong>used to be</strong> eighteen percent. In 2019 we <strong>digitized</strong> all employee "
              "records, and an app <strong>replaced</strong> the paper timesheets. <strong>Nowadays</strong>, "
              "turnover is around nine percent, and the old process looks <strong>outdated</strong>. Our HR has "
              "really <strong>evolved</strong>."),
 'gic_quiz': [
   ('1. What did employees use to fill in every week?',
    [("Paper timesheets.", True), ("Online forms on the new mobile app.", False), ("Nothing at all.", False)]),
   ('2. Which sentence is correct?',
    [('"We didn\'t used to have a hybrid schedule."', False), ('"We didn\'t use to have a hybrid schedule."', True), ('"We not use to have a hybrid schedule."', False)]),
   ('3. Why do we say "Nowadays, we sign" and not "Nowadays, we used to sign"?',
    [("Because used to is only for the past; for today we use the present simple.", True), ("Because sign is an irregular verb.", False), ("Because nowadays is a question word.", False)]),
 ],
 'gt_title': "Used To (Past Habits and States)",
 'gt_intro': ("Use <strong>used to + base verb</strong> for habits and states in the past that are <strong>not true "
              "now</strong>: We used to print every contract. In negatives and questions, use <strong>didn't use "
              "to</strong> and <strong>Did ... use to</strong> (no -d). For the situation today, use the "
              "<strong>present simple</strong>."),
 'gt_head': ["Form", "Use", "Example"],
 'gt_rows': [
   ("used to + base verb", "past habit or state, not true now", "We used to print every contract."),
   ("didn't use to + base verb", "negative (no -d after didn't)", "We didn't use to have a hybrid schedule."),
   ("Did + subject + use to ...?", "question (no -d after did)", "Did you use to work on Saturdays?"),
   ("present simple", "the situation today", "Nowadays, we sign contracts online."),
 ],
 'gt_note': "Tip: used to is only for the past. After did and didn't, write use to without -d. For today, say Nowadays + present simple: Nowadays, we work hybrid.",
 'fill': [
   ('"Back then, we ', "used to print", "Hint: past habit, not true now (print)", "Back then, we used to print every contract.", ' every contract."'),
   ('"Payroll ', "used to take", "Hint: used to + base verb (take)", "Payroll used to take three full days.", ' three full days."'),
   ('"We ', "didn't use to have", "Hint: negative: didn't use to + base verb (have)", "We didn't use to have a hybrid schedule.", ' a hybrid schedule."'),
   ('"', "Did you use to work", "Hint: question: Did + you + use to + base verb (work)", "Did you use to work on Saturdays?", ' on Saturdays?"'),
   ('"Turnover ', "used to be", "Hint: past state, not true now (be)", "Turnover used to be eighteen percent.", ' eighteen percent."'),
   ('"Nowadays, we ', "sign", "Hint: the situation today: present simple (sign)", "Nowadays, we sign contracts online.", ' contracts online."'),
 ],
 'order_title': "Put the HR Story in Order",
 'order_instr': "Put the parts of the presentation story in the correct order.",
 'order': [
   ("Open with the past: Back then, we used to do everything on paper.", 1),
   ("Give a number: Turnover used to be eighteen percent.", 2),
   ("Explain the change: In 2019, we digitized all employee records.", 3),
   ("Show the present: Nowadays, turnover is around nine percent.", 4),
   ("Close with the message: Our HR has really evolved.", 5),
 ],
 'speech': [
   ("We used to print every contract.", ""),
   ("Payroll used to take three days.", ""),
   ("We didn't use to have a hybrid schedule.", ""),
   ("Did you use to work on Saturdays?", ""),
   ("Nowadays, we sign contracts online.", ""),
 ],
 'sit_quiz': [
   ("You describe an old habit at work. You say:",
    [('"We use to print every contract."', False), ('"We used to print every contract."', True), ('"We used to printing every single contract by hand."', False)]),
   ("You ask a colleague about the past. You say:",
    [('"Did you use to work on Saturdays?"', True), ('"Did you used to work on Saturdays at the old office?"', False), ('"Used you to work on Saturdays?"', False)]),
   ("You say the company had no hybrid schedule before. You say:",
    [('"We not used to have a hybrid schedule."', False), ('"We didn\'t use to have a hybrid schedule."', True), ('"We didn\'t used have a hybrid schedule."', False)]),
   ("You describe the situation today. You say:",
    [('"Nowadays, we used to sign all our contracts online."', False), ('"Nowadays, we sign contracts online."', True), ('"Nowadays, we use to sign contracts."', False)]),
 ],
 'think': ("Think about your career in HR. Describe how your work used to be when you started and how it is nowadays. "
           "Talk about tools, paperwork, meetings, and the team. Use used to, didn't use to, nowadays, and at least "
           "four new words. Take your time."),
 'survival': [
   ("We used to print every contract.", ""),
   ("Payroll used to take three days.", ""),
   ("We didn't use to have a hybrid schedule.", ""),
   ("Did you use to work on Saturdays?", ""),
   ("Nowadays, we sign contracts online.", ""),
 ],
 'comp_heading': "Numbers That Tell a Story -- Used To",
 'media': [
   ("podcast", "Podcast", "Freakonomics Radio -- The Unintended Consequences of Working from Home",
    "A full episode about how office work used to be and what changed when people started working from home. You will hear many comparisons between then and now. Direct connection to Lesson 22: the story behind HR changes.",
    "write down 5 sentences about the past that you hear, and say them again with used to.", "Listen on Freakonomics", "https://freakonomics.com/podcast/the-unintended-consequences-of-working-from-home/"),
   ("series", "Series", "Mad Men -- Season 1, Episode 1: Smoke Gets in Your Eyes",
    "A New York advertising agency in 1960: typewriters, a rigid hierarchy, and paper everywhere. A clear picture of how offices used to work. Connection to Lesson 22: then and now at work.",
    "pause and say three things offices used to do: People used to ...", "View on IMDb", "https://www.imdb.com/title/tt1059578/"),
   ("youtube", "YouTube", '"Used To, Be Used To, Get Used To" -- engVid',
    "A clear video lesson on used to for past habits, with many examples and common mistakes. Connection to Lesson 22: telling how things used to be.",
    "pause and make one sentence about your own career with used to and one with didn't use to.", "Watch on YouTube", "https://www.youtube.com/watch?v=ymq-OAaSK08"),
 ],
 't': {
   's1': "<strong>Abertura (2 min):</strong> Aula 22. Tema: contar a historia por tras dos numeros de RH para o time de Sydney (como era antes e como e hoje). Foco B1: used to + base verb para habitos e estados do passado (used to / didn't use to / Did you use to...?) + present simple para hoje + 12 palavras novas. Zero portugues na tela.",
   's2': "<strong>Hook (3 min):</strong> Pergunte: no seu primeiro ano em RH, o que era muito diferente de hoje? Deixe a Murielle responder livremente. NAO corrija ainda; anote se ela ja usa used to ou so o past simple.",
   's3': "<strong>Recall da aula 21 (3 min):</strong> Callback dos verb patterns: suggest starting, postpone, look forward to. Peca uma frase com cada chip sobre a reuniao com Sydney. Ponte: na aula passada voce preparou a reuniao; hoje voce conta a HISTORIA por tras dos numeros.",
   's4': "<strong>Transicao (1 min):</strong> Diga: para contar como as coisas mudaram voce precisa de palavras de antes e agora. Vamos construi-las.",
   'vocab1': "<strong>Vocabulario 1-6 (5 min):</strong> Antes e agora. Drilling de cada card. PRONUNCIA: BACK then, NOW-a-days, PA-per-work, TIME-sheet, PAY-roll, out-DA-ted. CCQ: Is nowadays past or present? (present). Peca uma frase com cada palavra sobre a Minerva.",
   'vocab2': "<strong>Vocabulario 7-12 (5 min):</strong> Palavras de mudanca. PRONUNCIA: DI-gi-tize, re-PLACE, HI-e-rar-chy (4 silabas), com-MUTE, HY-brid, e-VOLVE. CCQ: If something evolves, does it change fast or slowly? (slowly). Peca uma frase com cada palavra.",
   's7': "<strong>Antes ou agora (5 min):</strong> Duas colunas: THEN (used to) e NOW (present simple). Leia a situacao e peca a frase ANTES de clicar Show. Aceite variacoes corretas.",
   's8': "<strong>Pronuncia (4 min):</strong> A Murielle e auditiva. Toque, ela ouve, repete 2-3x. Foco: used to soa /YOOS-tuh/, com S (nao Z) e o to fraco. Em didn't use to, o mesmo som. Did you use to: /DID-ja-YOOS-tuh/.",
   's9': "<strong>Transicao (1 min):</strong> Diga: agora a regra &mdash; como falar de habitos do passado que nao sao mais verdade.",
   's10': "<strong>Grammar Discovery (5 min):</strong> Leia cada exemplo e pergunte: is this true now? CCQ 1: Do we print every contract now? (no). CCQ 2: Was it a habit or one time? (a habit). CCQ 3: after did / didn't, used or use? (use, sem -d). So entao clique Reveal the Rule.",
   's11': "",
   's12': "<strong>Grammar Practice (3 min):</strong> Peca a resposta em voz alta ANTES de clicar. Atencao ao didn't use to e Did you use to (sem -d). A ultima e present simple (hoje).",
   's13': "<strong>Build the Story (3 min):</strong> Peca a frase completa em voz alta com a forma certa. So clique para comparar depois que ela tentar.",
   's14': "<strong>Transicao (1 min):</strong> Diga: hora de usar de verdade. Voce e Ethan, e a Murielle prepara a historia dos numeros para o time de Sydney.",
   's15': "<strong>Dialogo (6 min):</strong> Voce e Ethan. Clique Next Line um de cada vez; toque o audio de cada fala. Reforce cada used to (used to do, used to take, used to be) e o didn't use to. OBSTACULO: Did the company use to (sem -d).",
   's16': "<strong>Compreensao (3 min):</strong> Pergunte cada questao sobre o que o Ethan disse. Espere a resposta ANTES de revelar.",
   'listen1': "<strong>Listening 1 (5 min):</strong> Voz masculina: recado de voz do Daniel, do escritorio de Sydney, sobre como o RH deles funcionava antes da fusao. ANTES de tocar, leia as perguntas COM a Murielle para ela saber o que procurar. Toque 1x completo, depois 0.75x se precisar. Confira as respostas clicando em cada pergunta.",
   'listen2': "<strong>Listening 2 (4 min):</strong> Voz feminina: uma consultora de RH compara as avaliacoes de desempenho de antes e de hoje. Leia as perguntas COM a Murielle ANTES de tocar. OBSTACULO: separar used to (antes) do present simple (hoje).",
   's19': "<strong>Artefato (3 min):</strong> Mostre o slide de apresentacao e peca a Murielle para transformar cada linha em duas frases (Turnover used to be 18%. Nowadays, it is 9%.). CCQ: Is turnover 18% now? (no, 9%).",
   's20': "<strong>Transicao (1 min):</strong> Diga: voce tem as palavras, a regra e uma historia real. Agora juntamos tudo.",
   's21': "<strong>Quick Fire (4 min):</strong> Leia cada situacao e peca a frase em voz alta ANTES de revelar. Ritmo rapido, maximo 30 segundos.",
   's22': "<strong>Detective (4 min):</strong> Peca a Murielle para achar o erro ANTES de clicar. Dicas: is there a did / didn't before it? What comes after used to?",
   's23': "<strong>Sentence Building (4 min):</strong> Mostre as palavras-chave e peca a frase completa em voz alta com a forma certa. Aceite variacoes corretas.",
   's24': "<strong>Transicao (1 min):</strong> Diga: agora o palco e seu, Murielle. Guiado, semi-livre e livre. Conte a historia por tras dos seus numeros.",
   's25': "<strong>Role-Play Guided (5 min):</strong> Voce e Ethan preparando os slides para Sydney. A Murielle usa os chips para contar tres habitos antigos e como e hoje. Se travar, de o comeco (Back then, we used to ...). FOCO: used to + base verb, nowadays + present simple.",
   's26': "<strong>Role-Play Semi-Free (5 min):</strong> Voce e Daniel, de Sydney, perguntando como o RH brasileiro funcionava antes do sistema digital. A Murielle explica dois habitos antigos, uma coisa que nao existia (didn't use to) e faz uma pergunta com Did you use to...?",
   's27': "<strong>Free Practice (5 min):</strong> Sem script. A Murielle conta a historia da propria carreira: como era quando comecou em RH e como e hoje. NAO corrija durante a fala (delayed feedback). Anote 3-5 erros com used to.",
   's28': "<strong>Delayed Feedback (5 min):</strong> Compartilhe 3-5 erros do role-play livre. Para cada: diga o que ela falou, peca a correcao, de a versao correta se preciso, peca 2x. Use o campo editavel.",
   's29': "<strong>Key Phrases (3 min):</strong> Leia cada frase e peca repeticao. Atencao ao som /YOOS-tuh/.",
   's30': "<strong>Checklist + Encerramento (3 min):</strong> Leia cada item: can you do this? Marque os confirmados. 5/5 conclui a aula. Homework (diga oralmente): gravar 8-10 frases contando como o RH da Minerva era antes e como e hoje (used to, didn't use to, nowadays) usando 5 palavras novas.",
   's31': "<strong>Encerramento (1 min):</strong> Diga: great work, Murielle! Your numbers tell a story now. Celebre. Preview: next class &mdash; recommending HR actions in executive meetings.",
 },
}

if __name__ == '__main__':
    genlib.build(D)
