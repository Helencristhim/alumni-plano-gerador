#!/usr/bin/env node
/**
 * Build script for Maísa de Oliveira Santos — Professor HTML
 * Generates: public/professor/maisa-de-oliveira-santos.html
 * Run: node scripts/build-maisa-professor.js
 */

const fs = require('fs');
const path = require('path');

// ─── Read audioMap ───
const audioMapPath = path.resolve(__dirname, '../public/audio/maisa-de-oliveira-santos/audioMap.json');
const audioMap = JSON.parse(fs.readFileSync(audioMapPath, 'utf-8'));
const audioMapJSON = JSON.stringify(audioMap, null, 2);

// ─── Vocabulary Data ───
const vocabData = {
  1: [
    { word: 'name', pt: 'nome', example: 'My name is Maísa.' },
    { word: 'work', pt: 'trabalho / trabalhar', example: 'I work in finance.' },
    { word: 'live', pt: 'morar', example: 'I live in São Paulo.' },
    { word: 'company', pt: 'empresa', example: 'My company has international partners.' },
    { word: 'meeting', pt: 'reunião', example: 'I have a meeting today.' },
    { word: 'client', pt: 'cliente', example: 'The client called this morning.' },
    { word: 'partner', pt: 'sócio / parceiro', example: 'My partner is from New York.' }
  ],
  2: [
    { word: 'Good morning', pt: 'Bom dia', example: 'Good morning, David. How\'s it going?' },
    { word: 'How are you', pt: 'Como você está', example: 'How are you today?' },
    { word: 'What do you do', pt: 'O que você faz', example: 'What do you do for a living?' },
    { word: 'Where are you from', pt: 'De onde você é', example: 'Where are you from originally?' },
    { word: 'Nice to meet you', pt: 'Prazer em conhecê-lo', example: 'Nice to meet you. I\'m Maísa.' },
    { word: 'weekend', pt: 'fim de semana', example: 'Do you have plans for the weekend?' },
    { word: 'elevator', pt: 'elevador', example: 'I take the elevator every morning.' }
  ],
  3: [
    { word: 'attend meetings', pt: 'participar de reuniões', example: 'I usually attend meetings on Mondays.' },
    { word: 'review reports', pt: 'revisar relatórios', example: 'I review market data every morning.' },
    { word: 'send emails', pt: 'enviar e-mails', example: 'I send emails to clients daily.' },
    { word: 'meet clients', pt: 'encontrar clientes', example: 'I meet clients in the afternoon.' },
    { word: 'work from home', pt: 'trabalhar de casa', example: 'I sometimes work from home.' },
    { word: 'always', pt: 'sempre', example: 'I always check my emails first.' },
    { word: 'usually', pt: 'geralmente', example: 'I usually finish around seven.' }
  ],
  4: [
    { word: 'floor', pt: 'andar', example: 'My office is on the third floor.' },
    { word: 'meeting room', pt: 'sala de reunião', example: 'There is a meeting room on every floor.' },
    { word: 'reception', pt: 'recepção', example: 'Please wait at the reception.' },
    { word: 'next to', pt: 'ao lado de', example: 'The meeting room is next to the elevator.' },
    { word: 'across from', pt: 'em frente a', example: 'The kitchen is across from my office.' },
    { word: 'schedule', pt: 'agenda / horário', example: 'My schedule is very full today.' },
    { word: 'conference call', pt: 'conferência telefônica', example: 'We have a conference call at three.' }
  ],
  5: [
    { word: 'team', pt: 'equipe', example: 'My team manages client portfolios.' },
    { word: 'department', pt: 'departamento', example: 'The finance department is on the fifth floor.' },
    { word: 'headquarters', pt: 'sede', example: 'Our headquarters is in São Paulo.' },
    { word: 'senior analyst', pt: 'analista sênior', example: 'I am a senior analyst.' },
    { word: 'portfolio manager', pt: 'gestor de portfólio', example: 'The portfolio manager reviews assets weekly.' },
    { word: 'investment firm', pt: 'firma de investimentos', example: 'Our firm is well-known in the market.' },
    { word: 'branch office', pt: 'filial', example: 'We have a branch office in Rio.' }
  ],
  6: [
    { word: 'send', pt: 'enviar', example: 'Could you send me the file?' },
    { word: 'confirm', pt: 'confirmar', example: 'Can you confirm the meeting?' },
    { word: 'reschedule', pt: 'reagendar', example: 'Can we reschedule the meeting?' },
    { word: 'forward', pt: 'encaminhar', example: 'Could you forward this email?' },
    { word: 'prepare', pt: 'preparar', example: 'I need to prepare for the presentation.' },
    { word: 'handle', pt: 'lidar com', example: 'I can handle that.' },
    { word: 'Can you...?', pt: 'Você pode...?', example: 'Can you join the meeting at three?' }
  ],
  7: [
    { word: 'enjoy', pt: 'gostar / aproveitar', example: 'I enjoy reading market analysis.' },
    { word: 'prefer', pt: 'preferir', example: 'I prefer email to phone calls.' },
    { word: 'binge-watch', pt: 'maratonar', example: 'I binge-watch series on weekends.' },
    { word: 'episode', pt: 'episódio', example: 'I watched three episodes last night.' },
    { word: 'season', pt: 'temporada', example: 'The new season starts next week.' },
    { word: 'streaming', pt: 'streaming', example: 'I watch everything on streaming platforms.' },
    { word: 'plot twist', pt: 'reviravolta', example: 'The plot twist was unexpected.' }
  ],
  8: [
    { word: 'worked', pt: 'trabalhou', example: 'I worked late yesterday.' },
    { word: 'attended', pt: 'participou', example: 'I attended a meeting yesterday.' },
    { word: 'sent', pt: 'enviou', example: 'I sent the report this morning.' },
    { word: 'missed', pt: 'perdeu', example: 'Last March, I missed a trip to Miami.' },
    { word: 'went', pt: 'foi', example: 'I went to the office early.' },
    { word: 'had', pt: 'teve', example: 'I had a meeting with the team.' },
    { word: 'decided', pt: 'decidiu', example: 'She decided to accept the offer.' }
  ],
  9: [
    { word: 'tomorrow', pt: 'amanhã', example: 'I am going to attend the meeting tomorrow.' },
    { word: 'next week', pt: 'semana que vem', example: 'We need to reschedule for next week.' },
    { word: 'postpone', pt: 'adiar', example: 'Can we postpone the deadline?' },
    { word: 'set up a call', pt: 'marcar uma ligação', example: 'Let me set up a call with David.' },
    { word: 'block the calendar', pt: 'bloquear a agenda', example: 'I will block the calendar for Thursday.' },
    { word: 'unavailable', pt: 'indisponível', example: 'I am unavailable on Monday morning.' },
    { word: 'by the end of the month', pt: 'até o final do mês', example: 'The report is due by the end of the month.' }
  ],
  10: [
    { word: 'confident', pt: 'confiante', example: 'I feel more confident about speaking.' },
    { word: 'comfortable', pt: 'confortável', example: 'I am comfortable with small talk now.' },
    { word: 'nervous', pt: 'nervoso(a)', example: 'I was nervous in the first class.' },
    { word: 'improvement', pt: 'melhoria', example: 'My biggest improvement is vocabulary.' },
    { word: 'grammar', pt: 'gramática', example: 'I still need to work on grammar.' },
    { word: 'vocabulary', pt: 'vocabulário', example: 'My vocabulary has grown a lot.' },
    { word: 'fluency', pt: 'fluência', example: 'Fluency takes time and practice.' }
  ]
};

// ─── Matching data (English → Portuguese, 3 options) ───
const matchingData = {
  1: [
    { en: 'name', options: ['nome', 'empresa', 'reunião'], correct: 'nome' },
    { en: 'work', options: ['morar', 'trabalhar', 'cliente'], correct: 'trabalhar' },
    { en: 'meeting', options: ['parceiro', 'reunião', 'nome'], correct: 'reunião' },
    { en: 'client', options: ['cliente', 'empresa', 'trabalhar'], correct: 'cliente' },
    { en: 'partner', options: ['reunião', 'morar', 'parceiro'], correct: 'parceiro' }
  ],
  2: [
    { en: 'Good morning', options: ['Bom dia', 'Boa noite', 'Até logo'], correct: 'Bom dia' },
    { en: 'How are you', options: ['O que você faz', 'Como você está', 'De onde você é'], correct: 'Como você está' },
    { en: 'Nice to meet you', options: ['Até logo', 'Prazer em conhecê-lo', 'Bom dia'], correct: 'Prazer em conhecê-lo' },
    { en: 'weekend', options: ['elevador', 'fim de semana', 'escritório'], correct: 'fim de semana' },
    { en: 'elevator', options: ['elevador', 'reunião', 'andar'], correct: 'elevador' }
  ],
  3: [
    { en: 'attend meetings', options: ['enviar e-mails', 'participar de reuniões', 'trabalhar de casa'], correct: 'participar de reuniões' },
    { en: 'send emails', options: ['enviar e-mails', 'revisar relatórios', 'encontrar clientes'], correct: 'enviar e-mails' },
    { en: 'work from home', options: ['encontrar clientes', 'trabalhar de casa', 'participar de reuniões'], correct: 'trabalhar de casa' },
    { en: 'always', options: ['geralmente', 'nunca', 'sempre'], correct: 'sempre' },
    { en: 'usually', options: ['sempre', 'geralmente', 'raramente'], correct: 'geralmente' }
  ],
  4: [
    { en: 'floor', options: ['sala de reunião', 'andar', 'recepção'], correct: 'andar' },
    { en: 'meeting room', options: ['sala de reunião', 'andar', 'agenda'], correct: 'sala de reunião' },
    { en: 'next to', options: ['em frente a', 'ao lado de', 'entre'], correct: 'ao lado de' },
    { en: 'schedule', options: ['agenda', 'andar', 'recepção'], correct: 'agenda' },
    { en: 'across from', options: ['ao lado de', 'entre', 'em frente a'], correct: 'em frente a' }
  ],
  5: [
    { en: 'team', options: ['equipe', 'departamento', 'filial'], correct: 'equipe' },
    { en: 'headquarters', options: ['filial', 'sede', 'departamento'], correct: 'sede' },
    { en: 'investment firm', options: ['gestor de portfólio', 'firma de investimentos', 'analista sênior'], correct: 'firma de investimentos' },
    { en: 'branch office', options: ['filial', 'sede', 'equipe'], correct: 'filial' },
    { en: 'department', options: ['equipe', 'departamento', 'firma de investimentos'], correct: 'departamento' }
  ],
  6: [
    { en: 'send', options: ['confirmar', 'enviar', 'reagendar'], correct: 'enviar' },
    { en: 'confirm', options: ['confirmar', 'encaminhar', 'preparar'], correct: 'confirmar' },
    { en: 'reschedule', options: ['lidar com', 'preparar', 'reagendar'], correct: 'reagendar' },
    { en: 'forward', options: ['encaminhar', 'enviar', 'confirmar'], correct: 'encaminhar' },
    { en: 'handle', options: ['preparar', 'lidar com', 'reagendar'], correct: 'lidar com' }
  ],
  7: [
    { en: 'enjoy', options: ['preferir', 'gostar', 'maratonar'], correct: 'gostar' },
    { en: 'prefer', options: ['preferir', 'gostar', 'assistir'], correct: 'preferir' },
    { en: 'binge-watch', options: ['maratonar', 'temporada', 'episódio'], correct: 'maratonar' },
    { en: 'episode', options: ['temporada', 'episódio', 'reviravolta'], correct: 'episódio' },
    { en: 'plot twist', options: ['reviravolta', 'temporada', 'streaming'], correct: 'reviravolta' }
  ],
  8: [
    { en: 'worked', options: ['trabalhou', 'participou', 'enviou'], correct: 'trabalhou' },
    { en: 'attended', options: ['participou', 'perdeu', 'decidiu'], correct: 'participou' },
    { en: 'sent', options: ['foi', 'enviou', 'teve'], correct: 'enviou' },
    { en: 'missed', options: ['decidiu', 'perdeu', 'trabalhou'], correct: 'perdeu' },
    { en: 'decided', options: ['foi', 'participou', 'decidiu'], correct: 'decidiu' }
  ],
  9: [
    { en: 'tomorrow', options: ['amanhã', 'semana que vem', 'ontem'], correct: 'amanhã' },
    { en: 'postpone', options: ['adiar', 'marcar', 'bloquear'], correct: 'adiar' },
    { en: 'set up a call', options: ['marcar uma ligação', 'bloquear a agenda', 'adiar'], correct: 'marcar uma ligação' },
    { en: 'unavailable', options: ['disponível', 'indisponível', 'ocupado'], correct: 'indisponível' },
    { en: 'next week', options: ['semana passada', 'semana que vem', 'mês que vem'], correct: 'semana que vem' }
  ],
  10: [
    { en: 'confident', options: ['nervoso', 'confiante', 'confortável'], correct: 'confiante' },
    { en: 'comfortable', options: ['confortável', 'confiante', 'nervoso'], correct: 'confortável' },
    { en: 'improvement', options: ['gramática', 'melhoria', 'fluência'], correct: 'melhoria' },
    { en: 'fluency', options: ['vocabulário', 'gramática', 'fluência'], correct: 'fluência' },
    { en: 'nervous', options: ['confiante', 'nervoso', 'confortável'], correct: 'nervoso' }
  ]
};

// ─── Fill-in data ───
const fillData = {
  1: [
    { sentence: 'My ___ is Maísa de Oliveira Santos.', answer: 'name', hint: 'nome' },
    { sentence: 'I ___ in finance in São Paulo.', answer: 'work', hint: 'trabalho' },
    { sentence: 'I ___ in São Paulo.', answer: 'live', hint: 'moro' },
    { sentence: 'My ___ has international partners.', answer: 'company', hint: 'empresa' },
    { sentence: 'I have a ___ today.', answer: 'meeting', hint: 'reunião' }
  ],
  2: [
    { sentence: '___, David. How are you?', answer: 'Good morning', hint: 'Bom dia' },
    { sentence: '___ to meet you. I\'m Maísa.', answer: 'Nice', hint: 'Prazer' },
    { sentence: 'Do you have plans for the ___?', answer: 'weekend', hint: 'fim de semana' },
    { sentence: 'I take the ___ every morning.', answer: 'elevator', hint: 'elevador' },
    { sentence: '___ are you from?', answer: 'Where', hint: 'De onde' }
  ],
  3: [
    { sentence: 'I ___ attend meetings on Mondays.', answer: 'usually', hint: 'geralmente' },
    { sentence: 'I ___ check my emails first thing.', answer: 'always', hint: 'sempre' },
    { sentence: 'I ___ clients in the afternoon.', answer: 'meet', hint: 'encontro' },
    { sentence: 'I sometimes ___ from home.', answer: 'work', hint: 'trabalho' },
    { sentence: 'I ___ reports every morning.', answer: 'review', hint: 'reviso' }
  ],
  4: [
    { sentence: 'My office is on the third ___.', answer: 'floor', hint: 'andar' },
    { sentence: 'There is a meeting room ___ to the elevator.', answer: 'next', hint: 'ao lado' },
    { sentence: 'The reception is ___ from my office.', answer: 'across', hint: 'em frente' },
    { sentence: 'My ___ is very full today.', answer: 'schedule', hint: 'agenda' },
    { sentence: 'We have a ___ call at three.', answer: 'conference', hint: 'conferência' }
  ],
  5: [
    { sentence: 'My ___ manages client portfolios.', answer: 'team', hint: 'equipe' },
    { sentence: 'Our ___ is in São Paulo.', answer: 'headquarters', hint: 'sede' },
    { sentence: 'I am a senior ___.', answer: 'analyst', hint: 'analista' },
    { sentence: 'Our ___ is well-known in the market.', answer: 'firm', hint: 'firma' },
    { sentence: 'We have a ___ office in Rio.', answer: 'branch', hint: 'filial' }
  ],
  6: [
    { sentence: 'Could you ___ me the file?', answer: 'send', hint: 'enviar' },
    { sentence: 'Can you ___ the meeting time?', answer: 'confirm', hint: 'confirmar' },
    { sentence: 'Can we ___ the meeting?', answer: 'reschedule', hint: 'reagendar' },
    { sentence: 'Could you ___ this email to David?', answer: 'forward', hint: 'encaminhar' },
    { sentence: 'I need to ___ for the presentation.', answer: 'prepare', hint: 'preparar' }
  ],
  7: [
    { sentence: 'I ___ reading market analysis.', answer: 'enjoy', hint: 'gosto de' },
    { sentence: 'I ___ email to phone calls.', answer: 'prefer', hint: 'prefiro' },
    { sentence: 'I like to ___ series on weekends.', answer: 'binge-watch', hint: 'maratonar' },
    { sentence: 'The new ___ starts next Monday.', answer: 'season', hint: 'temporada' },
    { sentence: 'The ___ was unexpected.', answer: 'plot twist', hint: 'reviravolta' }
  ],
  8: [
    { sentence: 'I ___ a meeting yesterday.', answer: 'attended', hint: 'participei' },
    { sentence: 'I ___ the report this morning.', answer: 'sent', hint: 'enviei' },
    { sentence: 'Last March, I ___ a trip to Miami.', answer: 'missed', hint: 'perdi' },
    { sentence: 'I ___ with David on Friday.', answer: 'spoke', hint: 'falei' },
    { sentence: 'We ___ the deal last week.', answer: 'closed', hint: 'fechamos' }
  ],
  9: [
    { sentence: 'I am going to attend the meeting ___.', answer: 'tomorrow', hint: 'amanhã' },
    { sentence: 'We need to reschedule for ___.', answer: 'next week', hint: 'semana que vem' },
    { sentence: 'Can we ___ the deadline?', answer: 'postpone', hint: 'adiar' },
    { sentence: 'I will ___ the calendar for Thursday.', answer: 'block', hint: 'bloquear' },
    { sentence: 'I am ___ on Monday morning.', answer: 'unavailable', hint: 'indisponível' }
  ],
  10: [
    { sentence: 'I feel more ___ about speaking English.', answer: 'confident', hint: 'confiante' },
    { sentence: 'I am ___ with small talk now.', answer: 'comfortable', hint: 'confortável' },
    { sentence: 'My biggest ___ is vocabulary.', answer: 'improvement', hint: 'melhoria' },
    { sentence: 'I still need to work on ___.', answer: 'grammar', hint: 'gramática' },
    { sentence: '___ takes time and practice.', answer: 'Fluency', hint: 'Fluência' }
  ]
};

// ─── Multiple Choice data ───
const mcData = {
  1: { q: 'How do you say "Eu trabalho em finanças" in English?', options: ['I work in finance.', 'I works in finance.', 'I working in finance.', 'I am work in finance.'], correct: 0 },
  2: { q: 'Which phrase is correct for greeting someone in the morning?', options: ['Good night!', 'Good morning!', 'Good afternoon!', 'Good evening!'], correct: 1 },
  3: { q: 'Which sentence uses "usually" correctly?', options: ['I usually attend meetings.', 'Usually I meetings attend.', 'I attend usually meetings.', 'Meetings I usually attend.'], correct: 0 },
  4: { q: 'How do you say "A sala de reunião é no terceiro andar"?', options: ['The meeting room is in the third floor.', 'The meeting room is on the third floor.', 'The meeting room is at the third floor.', 'The meeting room is to the third floor.'], correct: 1 },
  5: { q: 'Which is the correct way to describe your role?', options: ['I am a senior analyst at my firm.', 'I am senior analyst at my firm.', 'I am a senior analyst in my firm.', 'I am the senior analyst from my firm.'], correct: 0 },
  6: { q: 'Which is a polite request?', options: ['Send me the file!', 'You send me the file.', 'Could you send me the file?', 'File send me.'], correct: 2 },
  7: { q: 'Which sentence expresses preference correctly?', options: ['I prefer email to phone calls.', 'I prefer email than phone calls.', 'I prefer email from phone calls.', 'I prefer email of phone calls.'], correct: 0 },
  8: { q: 'Which is the correct past form?', options: ['I sended the report.', 'I sent the report.', 'I sented the report.', 'I send the report yesterday.'], correct: 1 },
  9: { q: 'How do you talk about a future plan?', options: ['I going to attend the meeting.', 'I am going to attend the meeting.', 'I am go to attend the meeting.', 'I going attend the meeting.'], correct: 1 },
  10: { q: 'Which word means "melhoria" in English?', options: ['Grammar', 'Vocabulary', 'Improvement', 'Fluency'], correct: 2 }
};

// ─── Ordering data ───
const orderingData = {
  1: { correct: ['My', 'name', 'is', 'Maísa.'], shuffled: ['is', 'Maísa.', 'My', 'name'] },
  2: { correct: ['Good', 'morning,', 'how', 'are', 'you?'], shuffled: ['are', 'Good', 'you?', 'morning,', 'how'] },
  3: { correct: ['I', 'usually', 'attend', 'meetings', 'on', 'Mondays.'], shuffled: ['meetings', 'I', 'on', 'usually', 'Mondays.', 'attend'] },
  4: { correct: ['The', 'meeting', 'room', 'is', 'on', 'the', 'third', 'floor.'], shuffled: ['floor.', 'The', 'on', 'room', 'third', 'is', 'the', 'meeting'] },
  5: { correct: ['My', 'team', 'manages', 'client', 'portfolios.'], shuffled: ['manages', 'portfolios.', 'My', 'client', 'team'] },
  6: { correct: ['Could', 'you', 'send', 'me', 'the', 'file?'], shuffled: ['me', 'Could', 'file?', 'you', 'the', 'send'] },
  7: { correct: ['I', 'prefer', 'email', 'to', 'phone', 'calls.'], shuffled: ['phone', 'I', 'to', 'calls.', 'prefer', 'email'] },
  8: { correct: ['I', 'sent', 'the', 'report', 'this', 'morning.'], shuffled: ['report', 'I', 'morning.', 'sent', 'this', 'the'] },
  9: { correct: ['I', 'am', 'going', 'to', 'attend', 'the', 'meeting.'], shuffled: ['attend', 'I', 'the', 'going', 'meeting.', 'am', 'to'] },
  10: { correct: ['I', 'feel', 'more', 'confident', 'now.'], shuffled: ['confident', 'I', 'now.', 'feel', 'more'] }
};

// ─── Pronunciation phrases ───
const pronPhrases = {
  1: 'My name is Maísa.',
  2: 'Good morning, David. How\'s it going?',
  3: 'I usually attend meetings on Mondays.',
  4: 'The meeting is on the 10th floor.',
  5: 'My team manages client portfolios.',
  6: 'Could you send me the file?',
  7: 'I prefer email to phone calls.',
  8: 'I sent the report this morning.',
  9: 'I am going to attend the meeting tomorrow.',
  10: 'I feel more confident about speaking.'
};

// ─── Think About It questions ───
const thinkQuestions = {
  1: 'Think about your first day at work. How would you introduce yourself in English to a new colleague?',
  2: 'Imagine you are in the elevator with David. What are three things you could say to start a conversation?',
  3: 'What does your typical Monday look like? Can you describe your routine using "always," "usually," and "sometimes"?',
  4: 'If a visitor came to your office, how would you give them directions to the meeting room?',
  5: 'How would you explain what your company does to someone at a networking event?',
  6: 'Think of a situation where you needed to ask a colleague for help. How would you make that request politely in English?',
  7: 'What do you enjoy doing in your free time? How are your preferences different from your colleagues\'?',
  8: 'What happened at work last week that was interesting or challenging? Can you tell the story in the past tense?',
  9: 'What are your plans for next week? Think about both work and personal plans.',
  10: 'Compare how you felt about English in lesson 1 versus now. What has changed? What still challenges you?'
};

// ─── Survival Card phrases ───
const survivalPhrases = {
  1: ['My name is Maísa.', 'I work in finance.', 'I live in São Paulo.', 'Nice to meet you.', 'I\'m from Brazil.'],
  2: ['Good morning!', 'How are you?', 'Pretty good, thanks.', 'Have a good day!', 'See you later.'],
  3: ['I usually start at eight thirty.', 'I always check my emails first.', 'I sometimes work from home.', 'I review reports every morning.', 'I attend meetings in the afternoon.'],
  4: ['My office is on the third floor.', 'The meeting room is next to the elevator.', 'There are 12 people in the room.', 'The schedule is full today.', 'We have a conference call at three.'],
  5: ['I am a senior analyst.', 'My team manages client portfolios.', 'Our headquarters is in São Paulo.', 'Our firm has an international partner.', 'I work for a finance company.'],
  6: ['Could you send me the file?', 'Can you confirm the meeting?', 'Is it possible to reschedule?', 'I can handle that.', 'Would you mind checking this?'],
  7: ['I enjoy reading market analysis.', 'I prefer email to phone calls.', 'I like watching series.', 'What are you watching now?', 'Do you like thrillers?'],
  8: ['I attended a meeting yesterday.', 'I sent the report this morning.', 'We closed the deal last week.', 'I spoke with David on Friday.', 'Last March, I missed a trip to Miami.'],
  9: ['I am going to attend the meeting tomorrow.', 'We are meeting David at ten.', 'I will send you the agenda by Friday.', 'Are you free on Wednesday afternoon?', 'I will let you know by tomorrow.'],
  10: ['I feel more confident about speaking.', 'My biggest improvement is vocabulary.', 'I still need to work on grammar.', 'I think my English is improving.', 'Actually, I feel more confident now.']
};

// ─── Lesson titles ───
const lessonTitles = {
  1: 'Who Is Maísa? — Diagnostic Session',
  2: 'Elevator Moment — Small Talk',
  3: 'What Do You Do All Day? — Routine',
  4: 'People, Places, Numbers',
  5: 'This Is My World — Company & Role',
  6: 'Can You, or Can\'t You?',
  7: 'Like, Love, Hate — Preferences',
  8: 'Past Moments',
  9: 'What\'s Next? — Plans',
  10: 'Checkpoint 10 — Consolidation',
  11: 'Describing People and Personalities',
  12: 'São Paulo Through International Eyes',
  13: 'Professional Emails Part 1',
  14: 'Career History and Past Narratives',
  15: 'Opinions and Arguments',
  16: 'Business Dining Language',
  17: 'Presentations and Updates',
  18: 'Hypotheticals and Diplomatic Language',
  19: 'Travel Ready — Airports and Hotels',
  20: 'Block 1 Closing — Fluency Review'
};

// ─── Helper: escape HTML in JS strings ───
function esc(str) {
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

// ─── Helper: generate vocab cards HTML ───
function genVocabCards(lessonNum) {
  const items = vocabData[lessonNum];
  if (!items) return '';
  return items.map(item => {
    const escapedWord = esc(item.word);
    const escapedExample = esc(item.example);
    const speakWord = item.word.replace(/'/g, "\\'");
    return `<div class="vocab-card"><span class="word">${escapedWord}</span><span class="translation">${esc(item.pt)}</span><span class="example">${escapedExample}</span><button class="audio-btn" onclick="speakText('${speakWord}')">&#9654; Ouvir</button></div>`;
  }).join('');
}

// ─── Helper: JSON for exercises (escape for template literal in JS) ───
function jsonForJS(obj) {
  return JSON.stringify(obj).replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/</g, '\\u003c');
}

// ─── Grammar Tips ───
function getGrammarTip(n) {
  const tips = {
    1: '<strong>Verb TO BE</strong> — Em inglês, "to be" (ser/estar) muda de forma: I <u>am</u>, you <u>are</u>, he/she <u>is</u>. Não esqueça: "I am" pode virar "I\'m" na fala. Exemplo: "I\'m Maísa. I\'m from São Paulo. I\'m a professional."',
    2: '<strong>Small Talk Pattern</strong> — Conversas curtas seguem um padrão: Greeting → Question → Response → Return question → Closing. Exemplo: "Good morning! How are you? — Pretty good! And you? — Great, thanks. Have a good day!"',
    3: '<strong>Frequency Adverbs</strong> — Eles vão ANTES do verbo principal: "I <u>always</u> check emails." "She <u>usually</u> finishes at seven." "We <u>sometimes</u> work from home." Ordem de frequência: always (100%) > usually (80%) > often (60%) > sometimes (40%) > rarely (10%) > never (0%).',
    4: '<strong>There is / There are</strong> — Use "there IS" para singular: "There is ONE meeting room." Use "there ARE" para plural: "There are TWELVE people." Dica: ouça o que vem DEPOIS para escolher is/are.',
    5: '<strong>Have vs. Has</strong> — I/you/we/they HAVE. He/she/it HAS. "I <u>have</u> a team." "My company <u>has</u> offices in two cities." "She <u>has</u> international partners." Não diga "she have" — sempre HAS para terceira pessoa.',
    6: '<strong>Can vs. Can\'t — Pronúncia</strong> — "Can" em frases soa fraco: /kən/. "Can\'t" soa forte: /kænt/. A diferença é sutil! Dica: em "I can DO it" o CAN é quase invisível. Em "I CAN\'T do it" o CAN\'T é enfatizado. Pratique os dois lado a lado.',
    7: '<strong>Verb + -ING</strong> — Depois de like, love, enjoy, hate, prefer, usamos o verbo com -ING: "I enjoy <u>reading</u>." "I prefer <u>working</u> from home." "She loves <u>watching</u> series." NUNCA: "I enjoy read" ou "I prefer work."',
    8: '<strong>Past Simple — Regular vs. Irregular</strong> — Regulares: add -ed (worked, attended, reviewed). Irregulares: mudam completamente (go→went, send→sent, speak→spoke, have→had, meet→met). Os irregulares precisam ser memorizados — mas os mais comuns são poucos!',
    9: '<strong>Três formas de futuro</strong> — (1) "I\'m <u>going to</u> attend" = plano decidido. (2) "I\'m <u>meeting</u> David at 10" = compromisso agendado. (3) "I\'<u>ll</u> send it" = decisão/promessa no momento. Dica para Maísa: para agendamentos, use present continuous ("I\'m meeting...").',
    10: '<strong>Discourse Markers</strong> — Para organizar sua fala: "First of all..." (primeiro), "Then..." (depois), "After that..." (depois disso), "Also..." (além disso), "To be honest..." (para ser honesta), "Actually..." (na verdade). Estes conectores fazem sua fala parecer mais natural e fluente.'
  };
  return tips[n] || '';
}

// ─── Build Pre-class tab content ───
function buildPreclassTab() {
  let html = '';

  // Onboarding
  html += `<div class="onboarding-welcome">
  <h2>Bem-vinda, Maísa!</h2>
  <p class="quote">"Every expert was once a beginner."</p>
  <p style="font-size:.9rem;color:var(--text-mid);margin-top:1rem">Complete os exercícios antes de cada aula para maximizar seu aprendizado.</p>
</div>

<div class="card">
  <h3><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:6px"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Frases de Emergência</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Memorize estas frases antes de começar. Use-as sempre que precisar durante qualquer aula.</p>
  <div style="display:grid;gap:.8rem">
    <div style="background:var(--bg-elevated);padding:.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between">
      <div><strong style="font-size:.9rem">I am sorry, I did not understand.</strong><br><span style="font-size:.8rem;color:var(--text-dim)">Desculpe, não entendi.</span></div>
      <button class="audio-btn" onclick="speakText('I am sorry, I did not understand.')" style="background:var(--navy);color:#fff;border:none;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:.75rem">&#9654; Ouvir</button>
    </div>
    <div style="background:var(--bg-elevated);padding:.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between">
      <div><strong style="font-size:.9rem">Could you speak more slowly, please?</strong><br><span style="font-size:.8rem;color:var(--text-dim)">Pode falar mais devagar, por favor?</span></div>
      <button class="audio-btn" onclick="speakText('Could you speak more slowly, please?')" style="background:var(--navy);color:#fff;border:none;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:.75rem">&#9654; Ouvir</button>
    </div>
    <div style="background:var(--bg-elevated);padding:.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between">
      <div><strong style="font-size:.9rem">How do you say that in English?</strong><br><span style="font-size:.8rem;color:var(--text-dim)">Como se diz isso em inglês?</span></div>
      <button class="audio-btn" onclick="speakText('How do you say that in English?')" style="background:var(--navy);color:#fff;border:none;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:.75rem">&#9654; Ouvir</button>
    </div>
    <div style="background:var(--bg-elevated);padding:.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between">
      <div><strong style="font-size:.9rem">Excuse me, could you repeat that?</strong><br><span style="font-size:.8rem;color:var(--text-dim)">Com licença, pode repetir?</span></div>
      <button class="audio-btn" onclick="speakText('Excuse me, could you repeat that?')" style="background:var(--navy);color:#fff;border:none;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:.75rem">&#9654; Ouvir</button>
    </div>
    <div style="background:var(--bg-elevated);padding:.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between">
      <div><strong style="font-size:.9rem">One moment, please.</strong><br><span style="font-size:.8rem;color:var(--text-dim)">Um momento, por favor.</span></div>
      <button class="audio-btn" onclick="speakText('One moment, please.')" style="background:var(--navy);color:#fff;border:none;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:.75rem">&#9654; Ouvir</button>
    </div>
  </div>
</div>\n`;

  // Lessons 1-10
  for (let n = 1; n <= 10; n++) {
    html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula ${n}</span> ${esc(lessonTitles[n])}</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <div id="preclass-lesson-${n}"></div>
    <script>
    (function(){
      var vocabHTML = '<h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Vocabulário da Aula ${n}</h4><div class="vocab-grid">${genVocabCards(n).replace(/'/g, "\\'").replace(/\n/g, '')}</div>';

      var matchHTML = createMatchingDropdown("l${n}_match", ${JSON.stringify(matchingData[n])});

      var fillHTML = createFillBlankWithHint("l${n}_fill", ${JSON.stringify(fillData[n])});

      var mcHTML = createMultipleChoice("l${n}_mc", ${JSON.stringify(mcData[n].q)}, ${JSON.stringify(mcData[n].options)}, ${mcData[n].correct});

      var orderHTML = createOrdering("l${n}_order", ${JSON.stringify(orderingData[n].correct)}, ${JSON.stringify(orderingData[n].shuffled)});

      var pronHTML = createPronunciation("l${n}_pron", ${JSON.stringify(pronPhrases[n])}, null);

      var thinkHTML = createThinkAboutIt("l${n}_think", ${JSON.stringify(thinkQuestions[n])});

      document.getElementById("preclass-lesson-${n}").innerHTML = vocabHTML + matchHTML + fillHTML + mcHTML + orderHTML + pronHTML + thinkHTML;
    })();
    </script>

    <div class="section-divider"><span>&#9830;</span></div>

    <div class="card" style="background:var(--accent-dim);border-left:3px solid var(--accent);margin:1.5rem 0">
      <h4 style="color:var(--accent);margin-bottom:.6rem">Grammar Tip — Aula ${n}</h4>
      <p style="font-size:.85rem;line-height:1.7;color:var(--text)">${getGrammarTip(n)}</p>
    </div>

    <div class="survival-card">
      <h3>Survival Card — Lesson ${n}</h3>
      <ol>${survivalPhrases[n].map(p => `<li>${esc(p)} <button onclick="speakText('${p.replace(/'/g, "\\'")}')" style="background:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.4);color:#fff;padding:4px 10px;border-radius:4px;cursor:pointer;font-size:.75rem;margin-left:8px;">Ouvir</button></li>`).join('')}</ol>
    </div>
  </div>
</div>\n`;
  }

  // Lessons 11-20 placeholder
  for (let n = 11; n <= 20; n++) {
    html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula ${n}</span> ${esc(lessonTitles[n])}</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <div class="placeholder-card">Conteúdo será adicionado progressivamente.</div>
  </div>
</div>\n`;
  }

  return html;
}

// ─── Build Plano de Aula tab ───
function buildPlanoDeAulaTab() {
  let html = '';

  // Lesson 1 — Full plan
  html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula 1</span> Who Is Maísa? — Diagnostic Session</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <table class="timing-table">
      <thead><tr><th>Tempo</th><th>Fase</th><th>Atividade</th></tr></thead>
      <tbody>
        <tr><td>0-10 min</td><td>Warm-up & Rapport</td><td>Apresentação em português. Explicar estrutura do curso. Criar ambiente seguro.</td></tr>
        <tr><td>10-25 min</td><td>Diagnostic — Listening</td><td>Apresentar vocabulário base (name, work, live, company, meeting, client, partner). Verificar compreensão receptiva.</td></tr>
        <tr><td>25-40 min</td><td>Diagnostic — Speaking</td><td>Pedir que Maísa se apresente em inglês (sem pressão). Gravar áudio baseline. Observar: pronúncia, estrutura, confiança.</td></tr>
        <tr><td>40-55 min</td><td>Presentation</td><td>Ensinar: verb to be (I am / I'm, you are, she is), personal pronouns, estrutura de self-introduction. Usar exemplos do contexto dela.</td></tr>
        <tr><td>55-70 min</td><td>Practice</td><td>Exercícios controlados: completar frases (My name is ___, I work in ___). Drilling oral com correção gentil.</td></tr>
        <tr><td>70-85 min</td><td>Production</td><td>Maísa faz uma self-introduction completa (30-60 segundos). Professor grava para referência. Feedback positivo.</td></tr>
        <tr><td>85-90 min</td><td>Wrap-up</td><td>Recapitular o que foi aprendido. Explicar homework. Reforçar: "You did great today."</td></tr>
      </tbody>
    </table>

    <div class="teacher-guide">
      <h5>Guia do Professor — Frases-Chave</h5>
      <ul>
        <li>"Today is just about getting to know each other. No pressure at all."</li>
        <li>"Can you try saying that one more time? You're doing great."</li>
        <li>"Let's record your voice now — this is your starting point. In 10 lessons, you'll be amazed at the difference."</li>
        <li>"Repeat after me: My name is Maísa. I work in finance. I live in São Paulo."</li>
        <li>"Excellent! You just spoke English for 30 seconds. That's real progress."</li>
      </ul>
    </div>

    <div class="teacher-guide">
      <h5>CCQs — Concept Check Questions</h5>
      <ul>
        <li>"If I say 'I am Maísa' — am I talking about you or about me?" (About you/the speaker)</li>
        <li>"Is 'I live in São Paulo' about NOW or about YESTERDAY?" (Now — present simple)</li>
        <li>"If I say 'She works in finance' — am I talking about a man or a woman?" (A woman)</li>
      </ul>
    </div>

    <div class="teacher-guide">
      <h5>Antecipação de Obstáculos</h5>
      <ul>
        <li><strong>Bloqueio emocional:</strong> Maísa pode travar ao tentar falar. Solução: permitir uso de português como ponte ("Fale em português primeiro, depois vamos traduzir juntas").</li>
        <li><strong>Autocrítica excessiva:</strong> Pode pedir desculpas por erros. Solução: normalizar erros ("Errors are how we learn. Every error is progress.").</li>
        <li><strong>Comparação com nível receptivo:</strong> Pode ficar frustrada por entender mais do que consegue produzir. Solução: explicar a diferença entre compreensão e produção.</li>
      </ul>
    </div>

    <div class="card" style="background:var(--accent-dim);border-left:3px solid var(--accent)">
      <h4>Homework</h4>
      <p style="font-size:.9rem;line-height:1.8">Record a self-introduction audio (60 seconds minimum): your name, where you live, where you work, your role. Write 5 sentences using "I am," "I work," "I live."</p>
    </div>

    <div style="margin-top:1.5rem">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.8rem">O que eu aprendi — Checklist</h4>
      <div class="checklist-item"><input type="checkbox" id="cl_1_1" onchange="toggleChecklist(this)"><label for="cl_1_1">Sei me apresentar em inglês (nome, cidade, profissão)</label></div>
      <div class="checklist-item"><input type="checkbox" id="cl_1_2" onchange="toggleChecklist(this)"><label for="cl_1_2">Entendo o verbo "to be" no presente (I am, you are, she is)</label></div>
      <div class="checklist-item"><input type="checkbox" id="cl_1_3" onchange="toggleChecklist(this)"><label for="cl_1_3">Consigo dizer 5 frases sobre mim mesma em inglês</label></div>
      <div class="checklist-item"><input type="checkbox" id="cl_1_4" onchange="toggleChecklist(this)"><label for="cl_1_4">Gravei meu áudio de self-introduction</label></div>
    </div>
  </div>
</div>\n`;

  // Lesson 2 — Full plan
  html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula 2</span> Elevator Moment — Small Talk</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <table class="timing-table">
      <thead><tr><th>Tempo</th><th>Fase</th><th>Atividade</th></tr></thead>
      <tbody>
        <tr><td>0-10 min</td><td>Warm-up</td><td>Revisar self-introduction da aula 1. Ouvir áudio do homework. Dar feedback. Perguntar: "How are you today?"</td></tr>
        <tr><td>10-20 min</td><td>Lead-in</td><td>Apresentar cenário: "Imagine you're in the elevator with David. What can you say?" Brainstorm em português → traduzir.</td></tr>
        <tr><td>20-35 min</td><td>Presentation</td><td>Verb to be paradigma completo. Frases de small talk: How are you? What do you do? Where are you from? Nice to meet you. Drilling de pronúncia.</td></tr>
        <tr><td>35-50 min</td><td>Practice</td><td>Exercícios controlados: matching perguntas e respostas. Completar diálogo. Prática de entonação.</td></tr>
        <tr><td>50-70 min</td><td>Production</td><td>Role-play: encontro no elevador. Professor = David. Três rounds com crescente complexidade. Gravar o melhor.</td></tr>
        <tr><td>70-80 min</td><td>Feedback</td><td>Ouvir gravação juntas. Destacar acertos. Correção seletiva (máximo 3 pontos). Celebrar progresso.</td></tr>
        <tr><td>80-90 min</td><td>Wrap-up</td><td>Survival Card da aula. Explicar homework. Encerrar com: "You just had a conversation in English!"</td></tr>
      </tbody>
    </table>

    <div class="teacher-guide">
      <h5>Guia do Professor — Frases-Chave</h5>
      <ul>
        <li>"Let's imagine you're in the elevator. David walks in. What do you say?"</li>
        <li>"Good morning! is perfect. Now let's add: How are you?"</li>
        <li>"Try again: 'I work in finance.' Great pronunciation!"</li>
        <li>"Now let's do it faster — like a real elevator ride. Ready?"</li>
        <li>"You just had a complete conversation in English. How does that feel?"</li>
      </ul>
    </div>

    <div class="teacher-guide">
      <h5>CCQs — Concept Check Questions</h5>
      <ul>
        <li>"When I ask 'How are you?' — do I expect a long answer or a short one?" (Short)</li>
        <li>"Is 'What do you do?' about your hobbies or your job?" (Job)</li>
        <li>"If someone says 'Nice to meet you,' is this the first time or the tenth?" (First time)</li>
      </ul>
    </div>

    <div class="teacher-guide">
      <h5>Antecipação de Obstáculos</h5>
      <ul>
        <li><strong>Velocidade:</strong> Maísa pode achar que precisa falar rápido. Solução: "In real life, elevator talks are short. Slow and clear is better than fast and unclear."</li>
        <li><strong>Medo de errar na frente do sócio:</strong> Normalizar com: "David doesn't care about grammar. He cares about connection."</li>
      </ul>
    </div>

    <div class="card" style="background:var(--accent-dim);border-left:3px solid var(--accent)">
      <h4>Homework</h4>
      <p style="font-size:.9rem;line-height:1.8">Record a 90-second elevator scenario: greet David, make small talk, say goodbye. Practice the Survival Card phrases 3 times each.</p>
    </div>

    <div style="margin-top:1.5rem">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.8rem">O que eu aprendi — Checklist</h4>
      <div class="checklist-item"><input type="checkbox" id="cl_2_1" onchange="toggleChecklist(this)"><label for="cl_2_1">Consigo cumprimentar alguém em inglês</label></div>
      <div class="checklist-item"><input type="checkbox" id="cl_2_2" onchange="toggleChecklist(this)"><label for="cl_2_2">Sei perguntar "What do you do?" e "Where are you from?"</label></div>
      <div class="checklist-item"><input type="checkbox" id="cl_2_3" onchange="toggleChecklist(this)"><label for="cl_2_3">Consigo manter um small talk de 30 segundos</label></div>
      <div class="checklist-item"><input type="checkbox" id="cl_2_4" onchange="toggleChecklist(this)"><label for="cl_2_4">Gravei meu cenário de elevador</label></div>
    </div>
  </div>
</div>\n`;

  // Lesson 3 — Full plan
  html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula 3</span> What Do You Do All Day? — Routine</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <table class="timing-table">
      <thead><tr><th>Tempo</th><th>Fase</th><th>Atividade</th></tr></thead>
      <tbody>
        <tr><td>0-10 min</td><td>Warm-up</td><td>Small talk prática (revisão aula 2). "How was your weekend?" Ouvir homework. Feedback.</td></tr>
        <tr><td>10-25 min</td><td>Presentation</td><td>Present simple para rotinas. Frequency adverbs (always, usually, sometimes, rarely, never). Work routine vocabulary (attend, review, send, meet, check). Conjugação: I check / she checks.</td></tr>
        <tr><td>25-40 min</td><td>Practice — Controlled</td><td>Fill-in-the-blank com frases da rotina dela. Matching adverbs + activities. Correção de pronúncia contínua.</td></tr>
        <tr><td>40-55 min</td><td>Practice — Freer</td><td>Construir rotina real de Maísa juntas no quadro. "What do you do on Monday morning?" → "I check my emails." Build paragraph oralmente.</td></tr>
        <tr><td>55-75 min</td><td>Production</td><td>Maísa descreve segunda-feira inteira sem ajuda. Professor anota erros (corrige depois). Gravação final. Repetir com terça-feira se tempo permitir.</td></tr>
        <tr><td>75-85 min</td><td>Feedback & Error Correction</td><td>Selecionar 3-4 erros mais importantes. Reformulação. Drilling das formas corretas.</td></tr>
        <tr><td>85-90 min</td><td>Wrap-up</td><td>Homework explanation. "You just described your entire day in English!"</td></tr>
      </tbody>
    </table>

    <div class="teacher-guide">
      <h5>Guia do Professor — Frases-Chave</h5>
      <ul>
        <li>"What do you usually do on Monday mornings? Tell me in English — even just one word is fine."</li>
        <li>"Great! 'I check emails.' Now let's add WHEN: 'I always check emails first.'"</li>
        <li>"Notice: I check, SHE checks. The -s is only for he/she/it."</li>
        <li>"Let's build your whole Monday. Start with: 'I wake up at...'"</li>
        <li>"Fantastic! You just described your entire day. That's a huge step."</li>
      </ul>
    </div>

    <div class="teacher-guide">
      <h5>CCQs — Concept Check Questions</h5>
      <ul>
        <li>"'I always check emails' — does this happen every day or just sometimes?" (Every day)</li>
        <li>"'She usually finishes at seven' — is 'usually' 100% or about 80%?" (About 80%)</li>
        <li>"'I rarely work from home' — do I work from home a lot or a little?" (A little)</li>
      </ul>
    </div>

    <div class="teacher-guide">
      <h5>Antecipação de Obstáculos</h5>
      <ul>
        <li><strong>Terceira pessoa:</strong> Maísa pode esquecer o -s (she work → she works). Solução: visual claro + drilling focado.</li>
        <li><strong>Monotonia:</strong> Pode ficar tedioso descrever rotina. Solução: conectar com objetivo ("Imagine David asks: What do you do all day?").</li>
        <li><strong>Tradução literal:</strong> "Eu costumo" ≠ "I custom." Alertar sobre false friends.</li>
      </ul>
    </div>

    <div class="card" style="background:var(--accent-dim);border-left:3px solid var(--accent)">
      <h4>Homework</h4>
      <p style="font-size:.9rem;line-height:1.8">Write a paragraph about your Monday routine (minimum 8 sentences). Use at least 3 different frequency adverbs. Record the paragraph as audio.</p>
    </div>

    <div style="margin-top:1.5rem">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.8rem">O que eu aprendi — Checklist</h4>
      <div class="checklist-item"><input type="checkbox" id="cl_3_1" onchange="toggleChecklist(this)"><label for="cl_3_1">Sei usar present simple para descrever rotina</label></div>
      <div class="checklist-item"><input type="checkbox" id="cl_3_2" onchange="toggleChecklist(this)"><label for="cl_3_2">Conheço e uso frequency adverbs (always, usually, sometimes)</label></div>
      <div class="checklist-item"><input type="checkbox" id="cl_3_3" onchange="toggleChecklist(this)"><label for="cl_3_3">Consigo descrever minha rotina de segunda-feira em inglês</label></div>
      <div class="checklist-item"><input type="checkbox" id="cl_3_4" onchange="toggleChecklist(this)"><label for="cl_3_4">Escrevi e gravei meu parágrafo de rotina</label></div>
    </div>
  </div>
</div>\n`;

  // Lessons 4-10 shorter plans
  const shortPlans = {
    4: {
      title: 'People, Places, Numbers',
      timing: [
        ['0-10 min', 'Warm-up', 'Review routines. "Tell me about your Tuesday." Quick speaking warm-up.'],
        ['10-25 min', 'Presentation', 'Numbers 1-1000 (focus on financial numbers). There is/are. Prepositions of place (on, in, next to, across from, between).'],
        ['25-45 min', 'Practice', 'Dictation with numbers. "There are 12 people in the room." Building descriptions of the office.'],
        ['45-65 min', 'Production', 'Describe your office: how many floors, where things are, how many people. Use numbers and prepositions.'],
        ['65-80 min', 'Drilling', 'Number pronunciation drill. Preposition gaps exercise. Peer correction.'],
        ['80-90 min', 'Wrap-up', 'Homework: Write 5 sentences about your office using numbers. Record audio reading financial figures.']
      ]
    },
    5: {
      title: 'This Is My World — Company & Role',
      timing: [
        ['0-10 min', 'Warm-up', 'Number dictation review. "How many people are on your team?"'],
        ['10-25 min', 'Presentation', 'Have/has. Work with/for/at distinctions. Possessives (my, your, his, her, our, their). Company vocabulary.'],
        ['25-45 min', 'Practice', 'Company Profile Card — fill in details about her firm. Matching exercise: roles and descriptions.'],
        ['45-70 min', 'Production', 'Simulation: Introduce your company at a networking event. "I work for... My team manages... Our headquarters is..."'],
        ['70-85 min', 'Feedback', 'Listen to recording. Highlight use of have/has and possessives. Correct max 3 errors.'],
        ['85-90 min', 'Wrap-up', 'Homework: Write LinkedIn-style company bio in English.']
      ]
    },
    6: {
      title: 'Can You, or Can\'t You?',
      timing: [
        ['0-10 min', 'Warm-up', 'Quick company description review. "Tell me about your firm in 30 seconds."'],
        ['10-25 min', 'Presentation', 'Modal "can" for ability, permission, requests. Pronunciation: can /kən/ vs. can\'t /kænt/. Polite request forms.'],
        ['25-45 min', 'Practice', 'Back-and-forth drill: "Can you send me the file?" "Yes, I can." / "Can you attend on Thursday?" "No, I can\'t."'],
        ['45-70 min', 'Production', 'Office scenario role-play: making and responding to requests. Include: reschedule, forward, confirm, prepare.'],
        ['70-85 min', 'Feedback', 'Focus on can/can\'t pronunciation. Politeness level check.'],
        ['85-90 min', 'Wrap-up', 'Homework: Write 6 sentences with can/can\'t. Record response audio.']
      ]
    },
    7: {
      title: 'Like, Love, Hate — Preferences',
      timing: [
        ['0-10 min', 'Warm-up', '"Can you describe what you did yesterday using can/can\'t?" Review polite requests.'],
        ['10-25 min', 'Presentation', 'Like/love/enjoy/hate/prefer + gerund (-ing). Opinion phrases: "I think...", "For me...", "Personally, I prefer..."'],
        ['25-45 min', 'Practice', 'Coffee conversation with David: discuss preferences about work, food, weekends, shows.'],
        ['45-70 min', 'Production', 'Extended conversation about preferences: "What do you like to do on weekends? What shows do you enjoy?"'],
        ['70-85 min', 'Feedback', 'Check gerund usage after like/enjoy/prefer. Celebrate fluency moments.'],
        ['85-90 min', 'Wrap-up', 'Homework: Write 8 preference sentences. Record audio.']
      ]
    },
    8: {
      title: 'Past Moments',
      timing: [
        ['0-10 min', 'Warm-up', '"What do you enjoy doing on weekends?" Quick preference review.'],
        ['10-25 min', 'Presentation', 'Simple past: regular (-ed) + irregular (went, had, sent, spoke, met). Time markers: yesterday, last week, last month, in March.'],
        ['25-45 min', 'Practice', 'Narrative building: "What happened last week at work?" Fill-in with past forms. Pronunciation of -ed endings.'],
        ['45-70 min', 'Production', 'Tell the Miami story: "Last March, I missed a trip to Miami because..." Extended narrative in past simple.'],
        ['70-85 min', 'Feedback', 'Focus on irregular verb forms. Celebrate storytelling ability.'],
        ['85-90 min', 'Wrap-up', 'Homework: Write a paragraph about last week. Record Miami story audio.']
      ]
    },
    9: {
      title: 'What\'s Next? — Plans',
      timing: [
        ['0-10 min', 'Warm-up', '"Tell me about last week." Past simple review.'],
        ['10-25 min', 'Presentation', 'Going to (plans/intentions). Present continuous for future arrangements. Will (decisions/promises). Calendar vocabulary.'],
        ['25-45 min', 'Practice', 'Scheduling call role-play: "Are you free on Wednesday?" "I\'m going to..." "I\'ll send you..."'],
        ['45-70 min', 'Production', 'Plan a full business week: meetings, deadlines, calls. Use all three future forms.'],
        ['70-85 min', 'Feedback', 'Distinguish going to / present continuous / will. Check natural usage.'],
        ['85-90 min', 'Wrap-up', 'Homework: Write real schedule for next week in English. Record availability audio.']
      ]
    },
    10: {
      title: 'Checkpoint 10 — Consolidation',
      timing: [
        ['0-10 min', 'Warm-up', 'Free conversation: "Tell me about your plans for this week." Natural speaking.'],
        ['10-30 min', 'Review Activity', 'Integrated exercises covering all structures from aulas 1-9. Quick-fire questions across all topics.'],
        ['30-50 min', 'Speaking Assessment', 'Elevator simulation (real-time, no preparation). 3-minute monologue: past, present, future.'],
        ['50-65 min', 'Self-Assessment', 'Maísa listens to Lesson 1 recording vs. today. Discuss progress. Identify areas for continued work.'],
        ['65-80 min', 'Celebration & Planning', 'Acknowledge progress. Preview next 10 lessons. Set goals for block 2.'],
        ['80-90 min', 'Wrap-up', 'Homework: Record 3-minute progress report covering past, present, future.']
      ]
    }
  };

  // Key instructions for each lesson 4-10
  const keyInstructions = {
    4: [
      '"How many floors does your building have? Let\'s count together."',
      '"There IS one reception. There ARE twelve meeting rooms. Notice the difference?"',
      '"My office is ON the third floor. We use ON for floors, IN for cities, AT for addresses."',
      '"Let\'s practice numbers: one hundred, two hundred fifty, one thousand, one million."'
    ],
    5: [
      '"I work FOR a company. I work WITH David. I work AT the headquarters. Three different prepositions!"',
      '"My team HAS twelve people. I HAVE international clients. She HAS a meeting. Notice: has for he/she/it."',
      '"Let\'s build your Company Profile Card. What does your firm do? How big is your team?"',
      '"Imagine you\'re at a networking event. Introduce your company in 60 seconds. Ready? Go!"'
    ],
    6: [
      '"CAN you send me the file? Listen: /kən/. I CAN\'T attend. Listen: /kænt/. Hear the difference?"',
      '"Could you is more polite than Can you. Use \'could\' with people you don\'t know well."',
      '"Let\'s practice: I ask, you answer. Can you attend on Thursday? — No, I can\'t. But I can attend on Friday."',
      '"Now you ask ME. Make 5 requests using \'Can you\' and \'Could you\'."'
    ],
    7: [
      '"I enjoy READING. I like WATCHING. After enjoy/like/love/hate/prefer, we use -ING."',
      '"What do you enjoy doing on weekends? Tell me three things you like and one thing you hate."',
      '"Let\'s have a coffee conversation. Imagine we\'re in the kitchen. What are you watching these days?"',
      '"I prefer email TO phone calls. Not \'than\' — TO. I prefer A to B."'
    ],
    8: [
      '"Yesterday I WENT to the office. Last week we CLOSED a deal. These are irregular — no -ed!"',
      '"Regular: worked, attended, reviewed. Irregular: went, had, sent, spoke, met. Let\'s drill these."',
      '"Tell me the Miami story. Start with: Last March, I missed a trip to Miami because..."',
      '"First... Then... After that... Finally... Use these connectors to tell a story."'
    ],
    9: [
      '"I\'m GOING TO attend — this is a plan. I WILL send — this is a promise. I\'M MEETING David at 10 — this is arranged."',
      '"Are you free on Wednesday? I\'m going to block the calendar. I\'ll send you the agenda by Friday."',
      '"Let\'s plan your real next week. What meetings do you have? What do you need to prepare?"',
      '"Practice declining: I can\'t make it on Thursday. Would Wednesday work instead?"'
    ],
    10: [
      '"Let\'s listen to your Lesson 1 recording. Now listen to today. Can you hear the difference?"',
      '"Five-minute challenge: Tell me about your past (what happened), present (what you do), and future (your plans)."',
      '"Elevator simulation: I\'m David. I walk in. Go! No preparation. Just react naturally."',
      '"What are you most proud of from these 10 lessons? What do you want to improve in the next 10?"'
    ]
  };

  const lessonChecklists = {
    4: ['Sei usar números em inglês (1-1000, financeiros)', 'Entendo there is/there are', 'Consigo usar preposições de lugar (on, in, next to, across from)', 'Descrevi meu escritório em inglês'],
    5: ['Sei usar have/has corretamente', 'Entendo work for/with/at', 'Consigo apresentar minha empresa em inglês', 'Escrevi minha bio profissional'],
    6: ['Sei usar can/can\'t para habilidade e pedidos', 'Consigo fazer pedidos educados com could', 'Entendo a diferença de pronúncia entre can e can\'t', 'Gravei minhas respostas com can/can\'t'],
    7: ['Sei usar like/enjoy/prefer + -ing', 'Consigo expressar preferências em inglês', 'Tive uma conversa sobre séries e hobbies', 'Escrevi 8 frases de preferência'],
    8: ['Sei usar past simple regular e irregular', 'Consigo contar uma história no passado', 'Contei a história de Miami em inglês', 'Escrevi um parágrafo sobre semana passada'],
    9: ['Sei usar going to, will e present continuous para futuro', 'Consigo planejar uma semana em inglês', 'Fiz role-play de agendamento por telefone', 'Escrevi minha agenda da semana que vem'],
    10: ['Consigo manter conversa de 5 minutos em inglês', 'Percebo minha evolução desde a aula 1', 'Fiz simulação de elevador em tempo real', 'Gravei meu progress report de 3 minutos']
  };

  for (let n = 4; n <= 10; n++) {
    const plan = shortPlans[n];
    html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula ${n}</span> ${esc(plan.title)}</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <table class="timing-table">
      <thead><tr><th>Tempo</th><th>Fase</th><th>Atividade</th></tr></thead>
      <tbody>
        ${plan.timing.map(row => `<tr><td>${row[0]}</td><td>${row[1]}</td><td>${row[2]}</td></tr>`).join('\n        ')}
      </tbody>
    </table>

    <div class="teacher-guide">
      <h5>Instruções-Chave para o Professor</h5>
      <ul>
        ${keyInstructions[n].map(instr => `<li>${instr}</li>`).join('\n        ')}
      </ul>
    </div>

    <div style="margin-top:1.5rem">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.8rem">O que eu aprendi — Checklist</h4>
      ${lessonChecklists[n].map((item, i) => `<div class="checklist-item"><input type="checkbox" id="cl_${n}_${i+1}" onchange="toggleChecklist(this)"><label for="cl_${n}_${i+1}">${esc(item)}</label></div>`).join('\n      ')}
    </div>
  </div>
</div>\n`;
  }

  // Lessons 11-20 placeholder
  for (let n = 11; n <= 20; n++) {
    html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula ${n}</span> ${esc(lessonTitles[n])}</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <div class="placeholder-card">Conteúdo será adicionado progressivamente.</div>
  </div>
</div>\n`;
  }

  // Progress milestones
  html += `<div class="section-divider"><span>&#9830;</span></div>

<div class="card">
  <h3>Marcos de Progresso — Bloco 1</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Celebre cada conquista! Estes marcos ajudam a visualizar o avanço de Maísa.</p>
  <div style="display:grid;gap:.8rem">
    <div style="background:var(--success-bg);padding:1rem;border-radius:8px;border:1px solid var(--success-border);display:flex;align-items:center;gap:1rem">
      <input type="checkbox" id="mile_1" onchange="toggleChecklist(this)" style="width:22px;height:22px;accent-color:var(--success)">
      <div><strong style="font-size:.9rem;color:var(--success)">Aula 1 — Primeira frase em inglês</strong><br><span style="font-size:.8rem;color:var(--text-mid)">Maísa disse "My name is Maísa. I work in finance." pela primeira vez.</span></div>
    </div>
    <div style="background:var(--success-bg);padding:1rem;border-radius:8px;border:1px solid var(--success-border);display:flex;align-items:center;gap:1rem">
      <input type="checkbox" id="mile_2" onchange="toggleChecklist(this)" style="width:22px;height:22px;accent-color:var(--success)">
      <div><strong style="font-size:.9rem;color:var(--success)">Aula 2 — Primeira conversa completa</strong><br><span style="font-size:.8rem;color:var(--text-mid)">Small talk no elevador de 30 segundos sem travar.</span></div>
    </div>
    <div style="background:var(--success-bg);padding:1rem;border-radius:8px;border:1px solid var(--success-border);display:flex;align-items:center;gap:1rem">
      <input type="checkbox" id="mile_3" onchange="toggleChecklist(this)" style="width:22px;height:22px;accent-color:var(--success)">
      <div><strong style="font-size:.9rem;color:var(--success)">Aula 5 — Apresentação da empresa</strong><br><span style="font-size:.8rem;color:var(--text-mid)">60 segundos descrevendo a firma sem apoio visual.</span></div>
    </div>
    <div style="background:var(--success-bg);padding:1rem;border-radius:8px;border:1px solid var(--success-border);display:flex;align-items:center;gap:1rem">
      <input type="checkbox" id="mile_4" onchange="toggleChecklist(this)" style="width:22px;height:22px;accent-color:var(--success)">
      <div><strong style="font-size:.9rem;color:var(--success)">Aula 8 — Primeira narrativa no passado</strong><br><span style="font-size:.8rem;color:var(--text-mid)">Contou a história de Miami usando past simple corretamente.</span></div>
    </div>
    <div style="background:var(--success-bg);padding:1rem;border-radius:8px;border:1px solid var(--success-border);display:flex;align-items:center;gap:1rem">
      <input type="checkbox" id="mile_5" onchange="toggleChecklist(this)" style="width:22px;height:22px;accent-color:var(--success)">
      <div><strong style="font-size:.9rem;color:var(--success)">Aula 10 — 5 minutos de speaking contínuo</strong><br><span style="font-size:.8rem;color:var(--text-mid)">Monólogo de 5 minutos cobrindo passado, presente e futuro.</span></div>
    </div>
  </div>
</div>

<div class="card">
  <h3>Notas do Professor</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Espaço para anotações sobre o progresso, dificuldades e observações importantes sobre Maísa.</p>
  <div style="display:grid;gap:1rem">
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Pontos de atenção emocional</h4>
      <ul style="font-size:.85rem;line-height:1.8;padding-left:1.2rem;color:var(--text-mid)">
        <li>Maísa tende a se comparar com colegas que falam inglês fluentemente</li>
        <li>Histórico de desistência — celebrar cada aula concluída</li>
        <li>Ansiedade aumenta quando precisa falar "na frente" de alguém</li>
        <li>Responde bem a feedback positivo específico (não genérico)</li>
        <li>Motivação aumenta quando conecta conteúdo a situação real com David</li>
      </ul>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--accent)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Estratégias que funcionam com Maísa</h4>
      <ul style="font-size:.85rem;line-height:1.8;padding-left:1.2rem;color:var(--text-mid)">
        <li>Permitir uso de português como ponte ("Fale em PT, depois traduzimos")</li>
        <li>Gravar áudio para ela ouvir depois — prova concreta de progresso</li>
        <li>Conectar TUDO ao contexto dela (David, Faria Lima, Miami)</li>
        <li>Máximo 3 correções por atividade — priorizar comunicação</li>
        <li>Terminar toda aula com algo positivo e específico que ela fez bem</li>
        <li>Role-plays curtos (30-60s) antes de longos — build confidence gradually</li>
      </ul>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--warn)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--warn);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Red Flags — Sinais de alerta</h4>
      <ul style="font-size:.85rem;line-height:1.8;padding-left:1.2rem;color:var(--text-mid)">
        <li>2 homeworks não entregues seguidos → conversa motivacional</li>
        <li>Pedidos de cancelamento em sequência → reunião de realinhamento</li>
        <li>Frases como "não vou conseguir" ou "é muito difícil" → refocar em wins</li>
        <li>Comparação constante com outros → redirecionar para progresso pessoal</li>
        <li>Silêncio prolongado em aula (>30s) → dar escolha, não pressionar</li>
      </ul>
    </div>
  </div>
</div>\n`;

  return html;
}

// ─── Build Material do Professor tab ───
function buildMaterialTab() {
  let html = '';

  // Lesson 1 — Full material
  html += `<div class="lesson-card">
  <div class="lesson-card-header open" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula 1</span> Who Is Maísa? — Diagnostic Session</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body open">
    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Warm-up Questions</h4>
    <ul style="font-size:.9rem;line-height:2;padding-left:1.2rem">
      <li>What is your full name? (Qual é o seu nome completo?)</li>
      <li>Where do you live? (Onde você mora?)</li>
      <li>What do you do for work? (O que você faz profissionalmente?)</li>
      <li>How do you feel about learning English? (Como você se sente sobre aprender inglês?)</li>
    </ul>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Vocabulary — Teacher Reference</h4>
    <table class="timing-table">
      <thead><tr><th>Word</th><th>PT</th><th>Example (different from Pre-class)</th></tr></thead>
      <tbody>
        <tr><td><strong>name</strong></td><td>nome</td><td>Her name is Maísa de Oliveira Santos.</td></tr>
        <tr><td><strong>work</strong></td><td>trabalhar</td><td>She works in the financial sector.</td></tr>
        <tr><td><strong>live</strong></td><td>morar</td><td>Maísa lives in São Paulo, Brazil.</td></tr>
        <tr><td><strong>company</strong></td><td>empresa</td><td>The company has offices in two cities.</td></tr>
        <tr><td><strong>meeting</strong></td><td>reunião</td><td>We have a meeting every Monday.</td></tr>
        <tr><td><strong>client</strong></td><td>cliente</td><td>Our client is very important.</td></tr>
        <tr><td><strong>partner</strong></td><td>parceiro/sócio</td><td>The foreign partner visits every month.</td></tr>
      </tbody>
    </table>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Model Dialogue</h4>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px;border-left:3px solid var(--accent);font-size:.9rem;line-height:2">
      <strong>Teacher:</strong> Good morning! What is your name?<br>
      <strong>Maísa:</strong> My name is Maísa.<br>
      <strong>Teacher:</strong> Nice to meet you, Maísa. Where are you from?<br>
      <strong>Maísa:</strong> I am from São Paulo.<br>
      <strong>Teacher:</strong> And what do you do?<br>
      <strong>Maísa:</strong> I work in finance.<br>
      <strong>Teacher:</strong> Excellent! Tell me more about your company.<br>
      <strong>Maísa:</strong> My company has international partners.
    </div>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Grammar Structure — Verb TO BE</h4>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px;font-size:.9rem;line-height:2;font-family:monospace">
      I <strong>am</strong> Maísa. (I'm)<br>
      You <strong>are</strong> a student. (You're)<br>
      He/She <strong>is</strong> a professional. (He's / She's)<br>
      We <strong>are</strong> from Brazil. (We're)<br>
      They <strong>are</strong> partners. (They're)
    </div>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Oral Drilling Prompts</h4>
    <ol style="font-size:.9rem;line-height:2;padding-left:1.2rem">
      <li>Repeat: "My name is Maísa." (3x, increasing speed)</li>
      <li>Repeat: "I work in finance." (3x)</li>
      <li>Repeat: "I live in São Paulo." (3x)</li>
      <li>Chain drill: Name → City → Job → Company (without stopping)</li>
      <li>Substitution drill: "My name is ___. I work in ___. I live in ___."</li>
    </ol>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Production Role-Play Scenarios</h4>
    <div style="background:#fef9e7;border:1px solid rgba(240,216,97,.4);border-radius:8px;padding:1.2rem;margin-bottom:1rem">
      <strong>Scenario A:</strong> You are at a conference. Someone asks "Who are you?" Introduce yourself fully.<br>
      <strong>Scenario B:</strong> You are on a video call with a new international colleague. Introduce yourself and your role.<br>
      <strong>Scenario C:</strong> David introduces you to a client: "This is Maísa." Continue the conversation.
    </div>

    <div style="margin-top:1.5rem">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.8rem">Teacher Checklist — End of Class</h4>
      <div class="checklist-item"><input type="checkbox" id="tcl_1_1" onchange="toggleChecklist(this)"><label for="tcl_1_1">Baseline recording captured</label></div>
      <div class="checklist-item"><input type="checkbox" id="tcl_1_2" onchange="toggleChecklist(this)"><label for="tcl_1_2">Student can produce self-introduction (30+ seconds)</label></div>
      <div class="checklist-item"><input type="checkbox" id="tcl_1_3" onchange="toggleChecklist(this)"><label for="tcl_1_3">Verb to be understood in context</label></div>
      <div class="checklist-item"><input type="checkbox" id="tcl_1_4" onchange="toggleChecklist(this)"><label for="tcl_1_4">Homework clearly explained</label></div>
      <div class="checklist-item"><input type="checkbox" id="tcl_1_5" onchange="toggleChecklist(this)"><label for="tcl_1_5">Positive emotional state at end of class</label></div>
    </div>
  </div>
</div>\n`;

  // Lesson 2 — Full material
  html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula 2</span> Elevator Moment — Small Talk</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Warm-up Questions</h4>
    <ul style="font-size:.9rem;line-height:2;padding-left:1.2rem">
      <li>How are you today? (Como você está hoje?)</li>
      <li>Did you practice your self-introduction? (Você praticou sua apresentação?)</li>
      <li>What did you think about the homework? (O que achou do homework?)</li>
    </ul>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Vocabulary — Teacher Reference</h4>
    <table class="timing-table">
      <thead><tr><th>Expression</th><th>PT</th><th>Example (different from Pre-class)</th></tr></thead>
      <tbody>
        <tr><td><strong>Good morning</strong></td><td>Bom dia</td><td>Good morning, David. How's it going?</td></tr>
        <tr><td><strong>How are you</strong></td><td>Como você está</td><td>How are you doing today?</td></tr>
        <tr><td><strong>What do you do</strong></td><td>O que você faz</td><td>So, what do you do here?</td></tr>
        <tr><td><strong>Where are you from</strong></td><td>De onde você é</td><td>Where are you from originally?</td></tr>
        <tr><td><strong>Nice to meet you</strong></td><td>Prazer</td><td>It's really nice to meet you.</td></tr>
        <tr><td><strong>weekend</strong></td><td>fim de semana</td><td>Any plans for the weekend?</td></tr>
        <tr><td><strong>elevator</strong></td><td>elevador</td><td>We met in the elevator this morning.</td></tr>
      </tbody>
    </table>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Model Dialogue — Elevator Encounter</h4>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px;border-left:3px solid var(--accent);font-size:.9rem;line-height:2">
      <strong>Maísa:</strong> Good morning, David. How's it going?<br>
      <strong>David:</strong> Pretty good, thanks. Busy week?<br>
      <strong>Maísa:</strong> Very busy. Lots of meetings.<br>
      <strong>David:</strong> I know the feeling. Any plans for the weekend?<br>
      <strong>Maísa:</strong> Not really. Maybe some rest. You?<br>
      <strong>David:</strong> Same here. Have a good day!<br>
      <strong>Maísa:</strong> You too. See you later.
    </div>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Grammar Structure — Verb TO BE (Full Paradigm)</h4>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px;font-size:.9rem;line-height:2;font-family:monospace">
      <strong>Affirmative:</strong> I am / You are / He is / She is / We are / They are<br>
      <strong>Negative:</strong> I am not / You aren't / He isn't / She isn't / We aren't / They aren't<br>
      <strong>Question:</strong> Am I? / Are you? / Is he? / Is she? / Are we? / Are they?<br>
      <strong>Short answers:</strong> Yes, I am. / No, I'm not. / Yes, she is. / No, they aren't.
    </div>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Oral Drilling Prompts</h4>
    <ol style="font-size:.9rem;line-height:2;padding-left:1.2rem">
      <li>Repeat the full dialogue line by line (teacher reads, student repeats)</li>
      <li>Substitution drill: "Good morning, [name]. How's it going?"</li>
      <li>Speed drill: The entire dialogue in under 30 seconds</li>
      <li>Improv drill: Teacher changes the responses, student adapts</li>
    </ol>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Production Role-Play Scenarios</h4>
    <div style="background:#fef9e7;border:1px solid rgba(240,216,97,.4);border-radius:8px;padding:1.2rem;margin-bottom:1rem">
      <strong>Scenario A:</strong> Morning elevator — David is in a hurry. Keep it short (15 seconds).<br>
      <strong>Scenario B:</strong> Kitchen coffee area — more relaxed, talk about the weekend (45 seconds).<br>
      <strong>Scenario C:</strong> After a meeting — David introduces you to a visitor. Small talk with a stranger.
    </div>

    <div style="margin-top:1.5rem">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.8rem">Teacher Checklist — End of Class</h4>
      <div class="checklist-item"><input type="checkbox" id="tcl_2_1" onchange="toggleChecklist(this)"><label for="tcl_2_1">Student can initiate small talk</label></div>
      <div class="checklist-item"><input type="checkbox" id="tcl_2_2" onchange="toggleChecklist(this)"><label for="tcl_2_2">Verb to be paradigm understood</label></div>
      <div class="checklist-item"><input type="checkbox" id="tcl_2_3" onchange="toggleChecklist(this)"><label for="tcl_2_3">Can maintain 30-second conversation</label></div>
      <div class="checklist-item"><input type="checkbox" id="tcl_2_4" onchange="toggleChecklist(this)"><label for="tcl_2_4">Elevator scenario recorded</label></div>
    </div>
  </div>
</div>\n`;

  // Lesson 3 — Full material
  html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula 3</span> What Do You Do All Day? — Routine</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Warm-up Questions</h4>
    <ul style="font-size:.9rem;line-height:2;padding-left:1.2rem">
      <li>How was your weekend? (Como foi seu fim de semana?)</li>
      <li>What time did you wake up today? (Que horas você acordou hoje?)</li>
      <li>What do you usually do on Monday mornings? (O que você geralmente faz nas manhãs de segunda?)</li>
    </ul>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Vocabulary — Teacher Reference</h4>
    <table class="timing-table">
      <thead><tr><th>Word/Expression</th><th>PT</th><th>Example (different from Pre-class)</th></tr></thead>
      <tbody>
        <tr><td><strong>attend meetings</strong></td><td>participar de reuniões</td><td>Maísa attends three meetings every Monday.</td></tr>
        <tr><td><strong>review reports</strong></td><td>revisar relatórios</td><td>She reviews financial reports before lunch.</td></tr>
        <tr><td><strong>send emails</strong></td><td>enviar e-mails</td><td>The team sends about 50 emails a day.</td></tr>
        <tr><td><strong>meet clients</strong></td><td>encontrar clientes</td><td>She meets clients for lunch on Thursdays.</td></tr>
        <tr><td><strong>work from home</strong></td><td>trabalhar de casa</td><td>Hybrid work means office and home.</td></tr>
        <tr><td><strong>always</strong></td><td>sempre</td><td>She always starts her day early.</td></tr>
        <tr><td><strong>usually</strong></td><td>geralmente</td><td>Most people usually finish work around six.</td></tr>
      </tbody>
    </table>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Grammar Structure — Present Simple for Routines</h4>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px;font-size:.9rem;line-height:2;font-family:monospace">
      <strong>Affirmative:</strong> I/You/We/They check | He/She checks<br>
      <strong>Negative:</strong> I don't check | She doesn't check<br>
      <strong>Question:</strong> Do you check? | Does she check?<br><br>
      <strong>Frequency Adverbs (position):</strong><br>
      Subject + adverb + verb: "I <u>always</u> check emails first."<br>
      100% always → usually → often → sometimes → rarely → never 0%
    </div>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Oral Drilling Prompts</h4>
    <ol style="font-size:.9rem;line-height:2;padding-left:1.2rem">
      <li>Chain drill: "I always..., I usually..., I sometimes..., I rarely..., I never..."</li>
      <li>Substitution: "I [adverb] [verb] [complement]." Change one element each time.</li>
      <li>Question/Answer: "What do you usually do at 9 AM?" → "I usually check my emails."</li>
      <li>Third person conversion: "Tell me about Maísa's routine" → "She checks... She attends..."</li>
    </ol>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Production Role-Play Scenarios</h4>
    <div style="background:#fef9e7;border:1px solid rgba(240,216,97,.4);border-radius:8px;padding:1.2rem;margin-bottom:1rem">
      <strong>Scenario A:</strong> David asks: "What does your typical day look like?" Describe your full Monday.<br>
      <strong>Scenario B:</strong> A new colleague asks about the team's routine. Describe what everyone does.<br>
      <strong>Scenario C:</strong> Compare your routine with a colleague's: "I always... but she usually..."
    </div>

    <div style="margin-top:1.5rem">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.8rem">Teacher Checklist — End of Class</h4>
      <div class="checklist-item"><input type="checkbox" id="tcl_3_1" onchange="toggleChecklist(this)"><label for="tcl_3_1">Present simple used correctly for routines</label></div>
      <div class="checklist-item"><input type="checkbox" id="tcl_3_2" onchange="toggleChecklist(this)"><label for="tcl_3_2">Frequency adverbs in correct position</label></div>
      <div class="checklist-item"><input type="checkbox" id="tcl_3_3" onchange="toggleChecklist(this)"><label for="tcl_3_3">Can describe full Monday routine (60+ seconds)</label></div>
      <div class="checklist-item"><input type="checkbox" id="tcl_3_4" onchange="toggleChecklist(this)"><label for="tcl_3_4">Third person -s understood (she checks, he works)</label></div>
    </div>
  </div>
</div>\n`;

  // Lessons 4-10 — shorter (vocab table + key drills)
  const shortMaterial = {
    4: {
      title: 'People, Places, Numbers',
      vocab: [
        ['floor', 'andar', 'The office is on the 10th floor of the building.'],
        ['meeting room', 'sala de reunião', 'There is a meeting room on every floor.'],
        ['reception', 'recepção', 'Visitors wait at the reception area.'],
        ['next to', 'ao lado de', 'The printer is next to the kitchen.'],
        ['across from', 'em frente a', 'The parking garage is across from the main entrance.'],
        ['schedule', 'agenda/horário', 'Maísa\'s schedule includes client lunches.'],
        ['conference call', 'conferência', 'We have a conference call with London at four.']
      ],
      drills: ['Number dictation: read financial figures aloud (1.2 million, 3.5%, 52,000 points)', 'Preposition gap-fill: "The meeting room is ___ the elevator." (next to/across from/between)', 'Description chain: "On the first floor, there is... On the second floor, there are..."', 'Pair work: Draw your office layout and describe it to your partner.']
    },
    5: {
      title: 'This Is My World — Company & Role',
      vocab: [
        ['team', 'equipe', 'The investment team has twelve members.'],
        ['department', 'departamento', 'Our department handles institutional clients.'],
        ['headquarters', 'sede', 'The headquarters is located on Faria Lima.'],
        ['senior analyst', 'analista sênior', 'She is a senior professional in finance.'],
        ['portfolio manager', 'gestor de portfólio', 'The portfolio manager oversees all accounts.'],
        ['investment firm', 'firma de investimentos', 'The firm has international partners.'],
        ['branch office', 'filial', 'They opened a branch office in Miami.']
      ],
      drills: ['Company Profile Card: fill in Name, Role, Team Size, Headquarters, Focus Area', 'Substitution drill: "I work for ___ / My team manages ___ / Our headquarters is ___"', 'Networking simulation: Introduce your company in 60 seconds', 'Have/has practice: "My company has... / David has... / We have..."']
    },
    6: {
      title: 'Can You, or Can\'t You?',
      vocab: [
        ['send', 'enviar', 'I\'ll send the report by end of day.'],
        ['confirm', 'confirmar', 'I\'ll confirm the time by email.'],
        ['reschedule', 'reagendar', 'We need to reschedule for next week.'],
        ['forward', 'encaminhar', 'Please forward the document to David.'],
        ['prepare', 'preparar', 'Maísa is going to prepare for the meeting.'],
        ['handle', 'lidar com', 'She deals with complex transactions.'],
        ['Can you...?', 'Você pode...?', 'Can you join the meeting at four?']
      ],
      drills: ['Can/Can\'t pronunciation: minimal pairs drill (can /kən/ vs. can\'t /kænt/)', 'Request chain: Make 5 polite requests using "Could you...?" and "Can you...?"', 'Response drill: "Can you attend?" → "Yes, I can." / "No, I can\'t. But I can..."', 'Role-play: Call a colleague to reschedule a meeting politely.']
    },
    7: {
      title: 'Like, Love, Hate — Preferences',
      vocab: [
        ['enjoy', 'gostar de', 'I enjoy client meetings when I am prepared.'],
        ['prefer', 'preferir', 'Personally, I prefer working in the morning.'],
        ['binge-watch', 'maratonar', 'I binge-watch Succession on weekends.'],
        ['episode', 'episódio', 'Each episode is about 60 minutes.'],
        ['season', 'temporada', 'Industry has four seasons now.'],
        ['streaming', 'streaming', 'I watch everything on streaming.'],
        ['plot twist', 'reviravolta', 'The Season 3 plot twist was incredible.']
      ],
      drills: ['Preference structure: like/enjoy/love + -ing → "I enjoy watching...", "I love reading..."', 'Opinion expressions: "I think...", "For me...", "Personally, I prefer..."', 'Coffee conversation simulation: Discuss weekend plans, shows, preferences', 'Comparison: "I prefer ___ to ___" / "I like ___ more than ___"']
    },
    8: {
      title: 'Past Moments',
      vocab: [
        ['worked', 'trabalhou', 'She worked on the project all week.'],
        ['attended', 'participou', 'Maísa attended three meetings last Tuesday.'],
        ['sent', 'enviou', 'David sent an email late last night.'],
        ['missed', 'perdeu', 'She missed the conference in Miami.'],
        ['went', 'foi', 'I went to the office early on Monday.'],
        ['had', 'teve', 'Then, I had a meeting with the team.'],
        ['decided', 'decidiu', 'The team decided to close the deal.']
      ],
      drills: ['Regular -ed pronunciation: /t/ (worked), /d/ (reviewed), /ɪd/ (attended)', 'Irregular verb flash: present → past (go→went, send→sent, speak→spoke, meet→met)', 'Story sequencing: "First... Then... After that... Finally..."', 'The Miami Story: Narrate what happened using past simple only']
    },
    9: {
      title: 'What\'s Next? — Plans',
      vocab: [
        ['tomorrow', 'amanhã', 'I am going to attend the meeting tomorrow.'],
        ['next week', 'semana que vem', 'We\'re meeting the client on Friday morning.'],
        ['postpone', 'adiar', 'I\'d like to propose a new timeline.'],
        ['set up a call', 'marcar uma ligação', 'Let\'s schedule the meeting for Monday.'],
        ['block the calendar', 'bloquear a agenda', 'I need to block Thursday afternoon.'],
        ['unavailable', 'indisponível', 'My availability is limited this week.'],
        ['by the end of the month', 'até o final do mês', 'The annual budget needs revision by month-end.']
      ],
      drills: ['Going to vs. will vs. present continuous: When to use each form', 'Scheduling call simulation: Propose, accept, decline, reschedule', 'Calendar drill: Describe your real next week using future forms', 'Email: Write a short email proposing a meeting time']
    },
    10: {
      title: 'Checkpoint 10 — Consolidation',
      vocab: [
        ['confident', 'confiante', 'Actually, I feel more confident now.'],
        ['comfortable', 'confortável', 'I\'m comfortable with elevator conversations.'],
        ['nervous', 'nervoso(a)', 'I was very nervous in the first lesson.'],
        ['improvement', 'melhoria', 'I think my English is improving.'],
        ['grammar', 'gramática', 'I still need to work on grammar.'],
        ['vocabulary', 'vocabulário', 'My vocabulary has expanded significantly.'],
        ['fluency', 'fluência', 'Fluency is the goal for the next 10 lessons.']
      ],
      drills: ['Self-assessment: Compare Lesson 1 recording with today', '5-minute monologue: Past (what happened), Present (what I do now), Future (my plans)', 'Elevator simulation: Real-time, no preparation, just react', 'Meta-language: Use repair strategies ("Sorry, what I mean is...", "Let me rephrase that.")']
    }
  };

  const matScenarios = {
    4: ['Scenario: A visitor arrives. Give directions from reception to the 10th floor meeting room.', 'Scenario: Describe your office building to a foreign partner on a video call.', 'Scenario: Read financial figures from a report aloud (numbers practice).'],
    5: ['Scenario: Networking event — introduce your firm to a potential client in 60 seconds.', 'Scenario: Video call with London office — explain your team structure.', 'Scenario: LinkedIn message — describe your role and company in writing.'],
    6: ['Scenario: Ask a colleague to send a file, confirm a meeting, and reschedule another.', 'Scenario: Your boss asks if you can handle a new project. Respond with can/can\'t.', 'Scenario: Call reception to make several requests politely.'],
    7: ['Scenario: Coffee break conversation about weekend plans and TV shows.', 'Scenario: Business dinner — discuss food preferences and recommend restaurants.', 'Scenario: Team survey — express opinions about work-from-home vs. office.'],
    8: ['Scenario: Monday morning — tell David about your weekend using past simple.', 'Scenario: Quarterly review — describe what the team accomplished last quarter.', 'Scenario: The Miami story — narrate the full story of the missed trip.'],
    9: ['Scenario: Schedule a meeting with three people who have different availabilities.', 'Scenario: Plan a business trip to Miami — flights, hotel, meetings.', 'Scenario: Promise deliverables to a client — use will for commitments.'],
    10: ['Scenario: 5-minute presentation about yourself — past, present, future.', 'Scenario: Real-time elevator conversation with David (no preparation).', 'Scenario: Self-assessment interview — discuss your progress honestly.']
  };

  const matChecklists = {
    4: ['Number pronunciation accurate (hundred, thousand, million)', 'There is/are used correctly', 'Prepositions of place applied naturally', 'Office description fluent (30+ seconds)'],
    5: ['Have/has distinction clear', 'Work for/with/at used correctly', 'Company introduction confident (60 seconds)', 'Possessives (my, your, his, her, our) accurate'],
    6: ['Can/can\'t pronunciation distinguishable', 'Polite requests with could mastered', 'Can respond to requests naturally', 'Makes and declines requests confidently'],
    7: ['Verb + -ing structure automatic after like/enjoy', 'Expresses preferences with variety', 'Sustains preference conversation (2+ minutes)', 'Uses opinion phrases naturally'],
    8: ['Regular past -ed pronunciation correct', 'Key irregular verbs memorized (10+)', 'Can narrate a story with connectors', 'Miami story told fluently'],
    9: ['Three future forms distinguished', 'Scheduling vocabulary natural', 'Can plan a full week in English', 'Accepts/declines/proposes alternatives'],
    10: ['5-minute monologue achieved', 'Clear progress from lesson 1 baseline', 'Elevator simulation natural', 'Self-assessment articulate']
  };

  for (let n = 4; n <= 10; n++) {
    const mat = shortMaterial[n];
    html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula ${n}</span> ${esc(mat.title)}</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Vocabulary — Teacher Reference</h4>
    <table class="timing-table">
      <thead><tr><th>Word</th><th>PT</th><th>Example</th></tr></thead>
      <tbody>
        ${mat.vocab.map(v => `<tr><td><strong>${esc(v[0])}</strong></td><td>${esc(v[1])}</td><td>${esc(v[2])}</td></tr>`).join('\n        ')}
      </tbody>
    </table>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Key Drills</h4>
    <ol style="font-size:.9rem;line-height:2;padding-left:1.2rem">
      ${mat.drills.map(d => `<li>${esc(d)}</li>`).join('\n      ')}
    </ol>

    <h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Production Scenarios</h4>
    <div style="background:#fef9e7;border:1px solid rgba(240,216,97,.4);border-radius:8px;padding:1.2rem;margin-bottom:1rem">
      ${matScenarios[n].map(s => `<p style="font-size:.85rem;line-height:1.7;margin-bottom:.5rem"><strong>${esc(s.split(':')[0])}:</strong>${esc(s.split(':').slice(1).join(':'))}</p>`).join('\n      ')}
    </div>

    <div style="margin-top:1.5rem">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.8rem">Teacher Checklist — End of Class</h4>
      ${matChecklists[n].map((item, i) => `<div class="checklist-item"><input type="checkbox" id="tcl_${n}_${i+1}" onchange="toggleChecklist(this)"><label for="tcl_${n}_${i+1}">${esc(item)}</label></div>`).join('\n      ')}
    </div>
  </div>
</div>\n`;
  }

  // Lessons 11-20 placeholder
  for (let n = 11; n <= 20; n++) {
    html += `<div class="lesson-card">
  <div class="lesson-card-header" onclick="toggleLesson(this)">
    <h3><span class="lesson-number-badge">Aula ${n}</span> ${esc(lessonTitles[n])}</h3>
    <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
  </div>
  <div class="lesson-card-body">
    <div class="placeholder-card">Conteúdo será adicionado progressivamente.</div>
  </div>
</div>\n`;
  }

  // Quick Reference Card
  html += `<div class="section-divider"><span>&#9830;</span></div>

<div class="card">
  <h3>Quick Reference — Estruturas Gramaticais do Bloco 1</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Resumo rápido de todas as estruturas ensinadas nas aulas 1-10 para consulta durante a aula.</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1rem">
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Verb TO BE (Aulas 1-2)</h4>
      <p style="font-size:.8rem;line-height:1.7;font-family:monospace;color:var(--text-mid)">I am / You are / He-She is<br>I'm not / You aren't / He isn't<br>Am I? / Are you? / Is she?</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Present Simple (Aulas 3-4)</h4>
      <p style="font-size:.8rem;line-height:1.7;font-family:monospace;color:var(--text-mid)">I check / She checks (+s!)<br>I don't check / She doesn't check<br>Do you check? / Does she check?</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Have/Has (Aula 5)</h4>
      <p style="font-size:.8rem;line-height:1.7;font-family:monospace;color:var(--text-mid)">I/You/We/They have<br>He/She/It has<br>Do you have? / Does she have?</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Modal CAN (Aula 6)</h4>
      <p style="font-size:.8rem;line-height:1.7;font-family:monospace;color:var(--text-mid)">I can send / She can attend<br>I can't make it / He can't join<br>Can you send? / Could you forward?</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Verb + -ING (Aula 7)</h4>
      <p style="font-size:.8rem;line-height:1.7;font-family:monospace;color:var(--text-mid)">I enjoy reading / I like watching<br>I prefer working / She loves traveling<br>I hate waiting / We enjoy meeting</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Past Simple (Aula 8)</h4>
      <p style="font-size:.8rem;line-height:1.7;font-family:monospace;color:var(--text-mid)">Regular: worked, attended, reviewed<br>Irregular: went, had, sent, spoke, met<br>Did you send? / I didn't attend</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Future Forms (Aula 9)</h4>
      <p style="font-size:.8rem;line-height:1.7;font-family:monospace;color:var(--text-mid)">Going to: I'm going to attend (plan)<br>Pres. Cont: I'm meeting David (arranged)<br>Will: I'll send it now (promise/decision)</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Discourse Markers (Aula 10)</h4>
      <p style="font-size:.8rem;line-height:1.7;font-family:monospace;color:var(--text-mid)">First of all... / Then... / After that...<br>Also... / To be honest... / Actually...<br>Sorry, what I mean is... / Let me rephrase.</p>
    </div>
  </div>
</div>\n`;

  return html;
}

// ─── Build Atividades Complementares tab ───
function buildAtividadesTab() {
  const media = [
    { title: 'Succession (HBO)', type: 'SÉRIE', desc: 'Dinâmica de poder corporativo, linguagem financeira, family business. Ideal para vocabulário de board meetings e corporate politics.', lessons: '1-5' },
    { title: 'Industry (HBO)', type: 'SÉRIE', desc: 'Mercado financeiro de Londres, young professionals, alta pressão. Vocabulário técnico de trading, risk, e office dynamics.', lessons: '3-8' },
    { title: 'Planet Money (NPR)', type: 'PODCAST', desc: 'Economia explicada de forma acessível. Episódios de 20-30 minutos sobre temas financeiros do dia a dia. Ótimo para listening.', lessons: '4-10' },
    { title: 'The Indicator (NPR)', type: 'PODCAST', desc: 'Episódios de 10 minutos sobre indicadores econômicos. Perfeito para praticar listening curto diariamente.', lessons: '1-10' },
    { title: 'Suits (USA Network)', type: 'SÉRIE', desc: 'Inglês corporativo e jurídico. Ótimo para formal register, negotiation language, e professional relationships.', lessons: '6-10' },
    { title: 'The Big Short (2015)', type: 'FILME', desc: 'Crise financeira de 2008 explicada com humor. Vocabulário de mercado financeiro denso mas acessível pela narrativa.', lessons: '5-8' },
    { title: 'How I Built This (NPR)', type: 'PODCAST', desc: 'Histórias de empreendedores contando como construíram suas empresas. Linguagem de business acessível e inspiradora.', lessons: '5-10' }
  ];

  let html = `<div class="card">
  <h3>Atividades Complementares — Mídia Recomendada</h3>
  <p style="font-size:.9rem;color:var(--text-mid);margin-bottom:1.5rem">Conteúdos selecionados especificamente para o perfil profissional e nível de Maísa. Marque os que já assistiu/ouviu para acompanhar seu progresso.</p>
  <ul class="media-list">
    ${media.map((m, i) => `<li>
      <div style="flex-shrink:0;">
        <input type="checkbox" id="media_${i}" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--navy);cursor:pointer;">
      </div>
      <div style="flex:1">
        <div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.3rem">
          <span class="media-tag">${m.type}</span>
          <strong style="font-size:.95rem">${esc(m.title)}</strong>
        </div>
        <p style="font-size:.85rem;color:var(--text-mid);line-height:1.6;margin:0">${esc(m.desc)}</p>
        <span style="font-size:.7rem;color:var(--accent);font-weight:600;margin-top:.3rem;display:inline-block">Recomendado para: Aulas ${m.lessons}</span>
      </div>
    </li>`).join('\n    ')}
  </ul>
</div>

<div class="card">
  <h3>Como Usar o Conteúdo Complementar</h3>
  <div style="display:grid;gap:1rem;margin-top:1rem">
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Para Séries</h4>
      <p style="font-size:.85rem;line-height:1.7">Assista com legendas em inglês. Pause e repita frases que achar úteis. Anote 3 expressões novas por episódio. Na próxima aula, conte ao professor o que assistiu.</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--accent)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Para Podcasts</h4>
      <p style="font-size:.85rem;line-height:1.7">Ouça no trajeto ou durante exercícios. Na primeira vez, apenas escute. Na segunda, tente entender detalhes. Velocidade 0.75x é ok no início.</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--success)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--success);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Para Filmes</h4>
      <p style="font-size:.85rem;line-height:1.7">Assista primeiro por diversão. Depois, escolha uma cena de 5 minutos e analise: vocabulário, estruturas, pronúncia. Tente resumir o filme em inglês na próxima aula.</p>
    </div>
  </div>
</div>

<div class="card">
  <h3>Recomendações por Aula</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Conteúdo específico para complementar cada aula do bloco 1.</p>

  <div class="lesson-card">
    <div class="lesson-card-header" onclick="toggleLesson(this)">
      <h3><span class="lesson-number-badge">Aulas 1-2</span> Introdução e Small Talk</h3>
      <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
    </div>
    <div class="lesson-card-body">
      <table class="timing-table">
        <thead><tr><th>Mídia</th><th>O que observar</th><th>Exercício sugerido</th></tr></thead>
        <tbody>
          <tr><td>Succession S1E1 (primeiros 10 min)</td><td>Como os personagens se apresentam. Frases de greeting.</td><td>Anote 3 formas que os personagens usam para se cumprimentar.</td></tr>
          <tr><td>The Indicator — qualquer episódio</td><td>O host se apresenta no início. Ouça apenas a intro (1 min).</td><td>Tente entender: nome, cargo, tema do episódio.</td></tr>
          <tr><td>Industry S1E1 (primeiros 15 min)</td><td>Novos funcionários se apresentam. Small talk no escritório.</td><td>Escolha 2 frases de small talk e pratique em voz alta.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="lesson-card">
    <div class="lesson-card-header" onclick="toggleLesson(this)">
      <h3><span class="lesson-number-badge">Aulas 3-4</span> Rotina e Escritório</h3>
      <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
    </div>
    <div class="lesson-card-body">
      <table class="timing-table">
        <thead><tr><th>Mídia</th><th>O que observar</th><th>Exercício sugerido</th></tr></thead>
        <tbody>
          <tr><td>Suits S1E1</td><td>A rotina dos advogados. Como descrevem seu dia.</td><td>Descreva a rotina de um personagem usando present simple.</td></tr>
          <tr><td>Planet Money — "The Office"</td><td>Vocabulário de escritório e workplace culture.</td><td>Liste 5 palavras novas sobre escritório que ouviu.</td></tr>
          <tr><td>Industry S1E2-E3</td><td>Os personagens descrevem números e resultados financeiros.</td><td>Anote como dizem números grandes (millions, percentages).</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="lesson-card">
    <div class="lesson-card-header" onclick="toggleLesson(this)">
      <h3><span class="lesson-number-badge">Aulas 5-6</span> Empresa e Pedidos</h3>
      <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
    </div>
    <div class="lesson-card-body">
      <table class="timing-table">
        <thead><tr><th>Mídia</th><th>O que observar</th><th>Exercício sugerido</th></tr></thead>
        <tbody>
          <tr><td>How I Built This — qualquer episódio</td><td>Como empreendedores descrevem suas empresas. Uso de have/has.</td><td>Resuma a empresa do episódio em 5 frases com have/has.</td></tr>
          <tr><td>Succession S1E3-E4</td><td>Pedidos e requests entre personagens. Linguagem de poder.</td><td>Identifique 3 requests polite e 3 diretos. Qual a diferença?</td></tr>
          <tr><td>The Big Short (primeiros 30 min)</td><td>Vocabulário financeiro. Como explicam conceitos complexos.</td><td>Escolha 5 termos financeiros do filme e defina em inglês simples.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="lesson-card">
    <div class="lesson-card-header" onclick="toggleLesson(this)">
      <h3><span class="lesson-number-badge">Aulas 7-8</span> Preferências e Passado</h3>
      <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
    </div>
    <div class="lesson-card-body">
      <table class="timing-table">
        <thead><tr><th>Mídia</th><th>O que observar</th><th>Exercício sugerido</th></tr></thead>
        <tbody>
          <tr><td>Succession S2 (qualquer episódio)</td><td>Personagens expressam opinões: like, prefer, hate. Narrativas no passado.</td><td>Escolha um personagem e descreva o que ele/ela likes e hates.</td></tr>
          <tr><td>Planet Money — episódio sobre crise</td><td>Narrativas no passado. "What happened was..." "They decided to..."</td><td>Resuma o episódio usando past simple: First... Then... Finally...</td></tr>
          <tr><td>The Big Short (segunda metade)</td><td>Storytelling sobre eventos passados. Uso extensivo de past simple.</td><td>Conte a história do filme para alguém usando past simple.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="lesson-card">
    <div class="lesson-card-header" onclick="toggleLesson(this)">
      <h3><span class="lesson-number-badge">Aulas 9-10</span> Planos e Consolidação</h3>
      <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
    </div>
    <div class="lesson-card-body">
      <table class="timing-table">
        <thead><tr><th>Mídia</th><th>O que observar</th><th>Exercício sugerido</th></tr></thead>
        <tbody>
          <tr><td>Industry S1E5-E6</td><td>Personagens fazem planos: "I'm going to...", "We're meeting..."</td><td>Anote 5 frases sobre planos futuros que ouvir nos episódios.</td></tr>
          <tr><td>How I Built This — episódio favorito</td><td>O empreendedor fala sobre passado, presente e futuro.</td><td>Grave um áudio de 3 minutos sobre SEU passado, presente e futuro.</td></tr>
          <tr><td>Suits S1E5-E6</td><td>Agendamento de reuniões, scheduling, calendars.</td><td>Role-play: agende uma reunião fictícia baseada em uma cena do episódio.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="card">
  <h3>Playlist de Vocabulário Financeiro</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Recursos adicionais para exposição ao inglês financeiro — área de atuação de Maísa.</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1rem">
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.6rem">Bloomberg Quicktake (YouTube)</h4>
      <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Vídeos curtos (3-5 min) sobre mercado financeiro. Ideal para vocabulário técnico com visual explicativo.</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.6rem">Financial Times — Podcast "Behind the Money"</h4>
      <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Episódios de 20-30 min sobre bastidores do mercado financeiro. Inglês britânico, bom para diversificar sotaque.</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.6rem">Wall Street Journal — "The Journal" Podcast</h4>
      <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Notícias financeiras diárias em 15-20 min. Inglês americano claro, ritmo acessível para A1-A2.</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.6rem">Margin Call (2011) — Filme</h4>
      <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Drama sobre crise financeira. Diálogos rápidos mas repetitivos. Bom para a fase 2 (aulas 11-20).</p>
    </div>
  </div>
</div>

<div class="card">
  <h3>Diário de Exposição ao Inglês</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Use este checklist semanal para garantir exposição mínima ao inglês fora da sala de aula.</p>
  <div style="display:grid;gap:.5rem">
    <div class="checklist-item"><input type="checkbox" id="exp_1" onchange="toggleChecklist(this)"><label for="exp_1">Assisti pelo menos 1 episódio de série em inglês esta semana</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_2" onchange="toggleChecklist(this)"><label for="exp_2">Ouvi pelo menos 1 podcast em inglês esta semana</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_3" onchange="toggleChecklist(this)"><label for="exp_3">Li pelo menos 1 artigo/notícia em inglês esta semana</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_4" onchange="toggleChecklist(this)"><label for="exp_4">Pratiquei speaking sozinha (gravei áudio) pelo menos 1x esta semana</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_5" onchange="toggleChecklist(this)"><label for="exp_5">Anotei pelo menos 5 palavras/expressões novas esta semana</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_6" onchange="toggleChecklist(this)"><label for="exp_6">Tentei pensar em inglês por pelo menos 5 minutos (internal monologue)</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_7" onchange="toggleChecklist(this)"><label for="exp_7">Mudei o idioma de algum app/site para inglês</label></div>
  </div>
</div>\n`;

  return html;
}

// ─── Build full HTML ───
const html = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title>Alumni — Maísa de Oliveira Santos | Professor</title>
    <style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:wght@400;500;600;700&display=swap');</style>
    <link rel="stylesheet" href="/styles/design-system.css">
    <script src="/components/exercises.js"></script>
    <script src="/components/audio-generator.js"></script>
    <script src="/components/image-validator.js"></script>
    <style>
        :root{--accent:#946B2D;--accent-light:#b07d35;--accent-dim:rgba(148,107,45,.08);--accent-ring:rgba(148,107,45,.15);--navy:#003080;--navy-light:#1a4a9e;--black:#1a1a2e;--bg:#f5f5f0;--bg-card:#ffffff;--bg-card-hover:#fafaf7;--bg-elevated:#f0f0eb;--bg-input:#fafaf7;--border:rgba(0,0,0,.06);--border-accent:rgba(0,48,128,.08);--white:#1a1a2e;--text:#2d2d3a;--text-mid:#555566;--text-dim:#6b6b7b;--success:#16a34a;--success-bg:rgba(22,163,74,.08);--success-border:rgba(22,163,74,.25);--danger:#dc2626;--danger-bg:rgba(220,38,38,.08);--danger-border:rgba(220,38,38,.25);--warn:#d97706;--warn-bg:rgba(217,119,6,.08);--warn-border:rgba(217,119,6,.25);--shadow-sm:0 2px 12px rgba(0,0,0,.04);--shadow-md:0 4px 20px rgba(0,0,0,.06);--shadow-hover:0 6px 24px rgba(0,0,0,.08);--transition:200ms ease-out}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Inter',-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.7;font-size:16px;-webkit-font-smoothing:antialiased}

        /* LOGO BAR */
        .logo-bar{display:flex;align-items:center;justify-content:space-between;padding:1rem 2rem;background:var(--bg-card);border-bottom:1px solid var(--border)}
        .logo-bar img{height:36px}
        .logo-bar .prof-badge{font-size:.6rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--navy);border:1px solid var(--navy);padding:.25rem .8rem;border-radius:3px;backdrop-filter:blur(4px)}

        /* HEADER */
        .header{position:relative;min-height:320px;display:flex;align-items:flex-end;padding:3rem 2rem;overflow:hidden;background:url('https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=1400&q=80') center/cover no-repeat}
        .header::before{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.78) 0%,rgba(0,0,0,.45) 40%,rgba(0,0,0,.2) 100%)}
        .header::after{content:'';position:absolute;inset:0;background-image:url("data:image/svg+xml,%3Csvg width='60' height='60' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h60v60H0z' fill='none'/%3E%3Cpath d='M0 0v60M60 0v60M0 0h60M0 60h60M0 30h60M30 0v60' stroke='rgba(255,255,255,0.05)' stroke-width='0.5'/%3E%3C/svg%3E");opacity:1;pointer-events:none}
        .header-content{position:relative;z-index:2;max-width:960px;margin:0 auto;width:100%}
        .header h1{font-family:'Cormorant Garamond',serif;font-size:3.2rem;font-weight:700;color:#fff;line-height:1.1;margin-bottom:.5rem;letter-spacing:-0.02em}
        .header .subtitle{font-size:1rem;color:#fff;margin-bottom:1.5rem;opacity:.9;font-weight:300}
        .student-info{display:flex;gap:1.2rem;flex-wrap:wrap;font-size:.8rem;color:#fff;font-weight:500;letter-spacing:.5px}
        .student-info span{display:flex;align-items:center;gap:.5rem;background:rgba(255,255,255,.12);backdrop-filter:blur(10px);padding:.35rem .8rem;border-radius:4px;border:1px solid rgba(255,255,255,.1)}
        .progress-passport{margin-top:1.5rem}
        .progress-label{display:flex;justify-content:space-between;font-size:.75rem;color:#e8e8e8;margin-bottom:.5rem;font-weight:500}
        .progress-bar-outer{width:100%;height:6px;background:rgba(255,255,255,.15);border-radius:3px;overflow:hidden}
        .progress-bar-inner{height:100%;background:linear-gradient(90deg,var(--accent-light),var(--accent));border-radius:3px;transition:width .5s var(--transition);width:0%;box-shadow:0 0 8px rgba(148,107,45,.3)}
        .header-accent-line{height:3px;background:linear-gradient(90deg,var(--navy),var(--accent),var(--navy));opacity:.8}

        /* CONTAINER */
        .container{max-width:960px;margin:0 auto;padding:2rem 1.5rem}
        @media(min-width:768px){.container{padding:2.5rem 3rem}}

        /* SPEED CONTROL */
        .speed-control{display:flex;align-items:center;gap:6px;justify-content:flex-end;margin-bottom:12px;padding:8px 12px;background:rgba(255,255,255,.8);backdrop-filter:blur(20px);border-radius:100px;border:1px solid var(--border);width:fit-content;margin-left:auto}
        .speed-label{font-size:.8rem;color:var(--text-dim);font-weight:500;display:flex;align-items:center;gap:4px}
        .speed-btn{padding:5px 12px;font-size:.75rem;border:1px solid var(--border);background:transparent;border-radius:100px;cursor:pointer;min-height:36px;min-width:36px;transition:all var(--transition);font-family:'Inter',sans-serif;font-weight:500;color:var(--text-mid)}
        .speed-btn:hover{border-color:var(--navy);color:var(--navy)}
        .speed-btn.active{background:var(--navy);color:#fff;border-color:var(--navy);font-weight:600;box-shadow:0 2px 8px rgba(0,48,128,.2)}

        /* TAB NAVIGATION */
        .tabs-wrapper{position:sticky;top:0;z-index:100;background:rgba(245,245,240,.8);backdrop-filter:blur(20px);padding:.5rem 0;margin-bottom:2rem;border-bottom:1px solid var(--border)}
        .tabs{display:flex;gap:0;overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:960px;margin:0 auto;padding:0 1.5rem}
        @media(min-width:768px){.tabs{padding:0 3rem}}
        .tab-btn{flex:1;padding:1rem .6rem;border:none;background:transparent;cursor:pointer;font-family:'Inter',sans-serif;font-size:.65rem;font-weight:500;color:var(--text-dim);transition:all var(--transition);letter-spacing:1px;text-transform:uppercase;position:relative;white-space:nowrap;min-height:44px;min-width:44px;border-radius:0}
        .tab-btn.active{color:var(--navy);font-weight:700}
        .tab-btn.active::after{content:'';position:absolute;bottom:0;left:20%;right:20%;height:2px;background:linear-gradient(90deg,var(--navy),var(--accent));border-radius:1px}
        .tab-btn:hover:not(.active){color:var(--text-mid)}
        .tab-btn:focus-visible{outline:3px solid var(--navy);outline-offset:2px;border-radius:4px}

        /* TAB CONTENT */
        .tab-content{display:none}
        .tab-content.active{display:block;animation:fadeIn .2s ease-out}
        @keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
        @keyframes shake{0%,100%{transform:translateX(0)}25%{transform:translateX(-4px)}75%{transform:translateX(4px)}}

        /* SECTION DIVIDER */
        .section-divider{display:flex;align-items:center;justify-content:center;margin:2.5rem 0;color:var(--border);font-size:.7rem;letter-spacing:4px}
        .section-divider::before,.section-divider::after{content:'';flex:1;height:1px;background:var(--border)}
        .section-divider span{padding:0 1rem;color:var(--accent);font-size:.8rem}

        /* CARDS */
        .card{background:var(--bg-card);border:1px solid var(--border-accent);border-radius:10px;padding:1.8rem;margin-bottom:1.5rem;box-shadow:var(--shadow-sm);transition:all var(--transition)}
        .card:hover{border-color:rgba(148,107,45,.15);box-shadow:var(--shadow-md)}
        .card h3{font-family:'Cormorant Garamond',serif;font-size:1.8rem;font-weight:600;color:var(--white);margin-bottom:1rem}
        .card h4{font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.5rem}

        /* CURRICULUM TABLE */
        .curriculum-wrapper{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--border-accent);border-radius:10px;box-shadow:var(--shadow-sm)}
        .curriculum-table{width:100%;min-width:900px;border-collapse:collapse;font-size:.8rem}
        .curriculum-table thead th{background:var(--navy);color:#fff;padding:1rem 1.2rem;text-align:left;font-weight:600;font-size:.7rem;letter-spacing:.5px;text-transform:uppercase;position:sticky;top:0;font-family:'Inter',sans-serif}
        .curriculum-table tbody tr:nth-child(even){background:#f8f8f5}
        .curriculum-table tbody tr:nth-child(odd){background:#fff}
        .curriculum-table tbody tr{transition:background var(--transition)}
        .curriculum-table tbody tr:hover{background:rgba(0,48,128,.03)}
        .curriculum-table tbody td{padding:1rem 1.2rem;vertical-align:top;border-bottom:1px solid var(--border);line-height:1.6}
        .curriculum-table tbody td:first-child{font-weight:700;color:var(--accent);text-align:center;width:40px}

        /* LESSON CARDS */
        .lesson-card{background:var(--bg-card);border:1px solid var(--border-accent);overflow:hidden;margin-bottom:1.5rem;border-radius:10px;box-shadow:var(--shadow-sm);transition:all var(--transition)}
        .lesson-card:hover{box-shadow:var(--shadow-md);transform:translateY(-1px)}
        .lesson-card-header{padding:1.2rem 1.5rem;cursor:pointer;display:flex;align-items:center;justify-content:space-between;min-height:64px;user-select:none;transition:background var(--transition)}
        .lesson-card-header:hover{background:var(--bg-elevated)}
        .lesson-card-header h3{font-family:'Inter',sans-serif;font-size:.95rem;font-weight:600;color:var(--white);margin:0;display:flex;align-items:center;gap:.6rem}
        .lesson-number-badge{display:inline-flex;align-items:center;justify-content:center;font-size:.55rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--navy);background:rgba(0,48,128,.06);padding:.3rem .7rem;border-radius:4px}
        .lesson-card-body{display:none;padding:0 1.5rem 1.5rem;border-top:1px solid var(--border)}
        .lesson-card-body.open{display:block}
        .lesson-card-header.open{border-top:2px solid transparent;border-image:linear-gradient(90deg,var(--navy),var(--accent)) 1}
        .expand-icon{color:var(--text-dim);transition:transform var(--transition);flex-shrink:0}
        .lesson-card-header.open .expand-icon{transform:rotate(180deg)}

        /* PPP SECTIONS */
        .ppp-section{margin:1.5rem 0;padding:1.2rem 1.5rem;border-left:3px solid var(--accent);background:var(--accent-dim);border-radius:0 8px 8px 0}
        .ppp-section h4{font-size:.65rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:0.15em;margin-bottom:.8rem}
        .ppp-section .timing{display:inline-block;font-size:.6rem;font-weight:600;background:var(--accent);color:#fff;padding:.2rem .6rem;border-radius:100px;margin-left:.5rem}

        /* TEACHER GUIDE */
        .teacher-guide{background:#fef9e7;border:1px solid rgba(240,216,97,.4);border-radius:10px;padding:1.4rem;margin:1.2rem 0;border-left:3px dotted #f0d861}
        .teacher-guide h5{font-size:.65rem;font-weight:700;color:#92600a;text-transform:uppercase;letter-spacing:0.15em;margin-bottom:.6rem}
        .teacher-guide p,.teacher-guide li{font-size:.85rem;color:#5c3d00;line-height:1.7}

        /* ANSWER KEY */
        .answer-key{background:#eef7ee;border:1px solid rgba(184,224,184,.5);border-radius:10px;padding:1.4rem;margin:1.2rem 0}
        .answer-key h5{font-size:.65rem;font-weight:700;color:#1a6b1a;text-transform:uppercase;letter-spacing:0.15em;margin-bottom:.6rem}

        /* SURVIVAL CARD */
        .survival-card{background:linear-gradient(135deg,var(--navy) 0%,var(--accent) 100%);border-radius:12px;padding:2rem;color:#fff;margin:2rem 0;box-shadow:0 8px 32px rgba(0,48,128,.2)}
        .survival-card h3{font-family:'Cormorant Garamond',serif;font-size:1.6rem;color:#fff;margin-bottom:1rem}
        .survival-card ol{padding-left:1.2rem}
        .survival-card li{margin-bottom:.6rem;font-size:.9rem;line-height:1.5}

        /* ONBOARDING */
        .onboarding-welcome{background:var(--bg-card);border:2px solid var(--accent);border-radius:12px;padding:2.5rem;margin-bottom:2rem;text-align:center;box-shadow:var(--shadow-md)}
        .onboarding-welcome h2{font-family:'Cormorant Garamond',serif;font-size:2rem;color:var(--accent);margin-bottom:.5rem}
        .onboarding-welcome .quote{font-style:italic;color:var(--text-mid);margin:1rem 0;font-size:.95rem}

        /* PLACEHOLDER */
        .placeholder-card{background:var(--bg-elevated);border:1px dashed rgba(0,0,0,.12);border-radius:10px;padding:2.5rem;text-align:center;color:var(--text-dim);margin:1.5rem 0}

        /* VOCAB */
        .vocab-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;margin:1rem 0}
        .vocab-card{background:var(--bg-card);border:1px solid var(--border-accent);border-left:3px solid var(--accent);border-radius:8px;padding:1rem 1rem 1rem 1.2rem;display:flex;flex-direction:column;gap:.4rem;transition:all var(--transition)}
        .vocab-card:hover{border-color:rgba(148,107,45,.25);box-shadow:var(--shadow-sm)}
        .vocab-card .word{font-weight:700;font-size:1rem;color:var(--accent)}
        .vocab-card .translation{font-size:.8rem;color:var(--text-dim);font-style:italic}
        .vocab-card .example{font-size:.85rem;color:var(--text-mid);line-height:1.6}
        .vocab-card .audio-btn{align-self:flex-start;margin-top:.4rem;padding:6px 14px;font-size:.75rem;border:none;background:var(--navy);color:#fff;border-radius:6px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;min-height:44px;min-width:44px;font-family:'Inter',sans-serif;font-weight:500;transition:all var(--transition)}
        .vocab-card .audio-btn:hover{background:var(--navy-light);box-shadow:0 2px 8px rgba(0,48,128,.2)}

        /* MEDIA LIST */
        .media-list{list-style:none;padding:0}
        .media-list li{padding:1rem 0;border-bottom:1px solid var(--border);display:flex;gap:1rem;align-items:flex-start}
        .media-list li:last-child{border-bottom:none}
        .media-tag{display:inline-block;font-size:.6rem;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;padding:.25rem .6rem;border-radius:4px;background:rgba(0,48,128,.06);color:var(--navy);flex-shrink:0}

        /* CANCELLATION */
        .cancellation-rules{background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1.4rem}
        .cancellation-rules h4{color:var(--danger)}

        /* TIMING TABLE */
        .timing-table{width:100%;border-collapse:collapse;font-size:.8rem;margin:1rem 0;border-radius:8px;overflow:hidden;border:1px solid var(--border)}
        .timing-table th{background:var(--navy);color:#fff;padding:.7rem 1rem;text-align:left;font-size:.65rem;letter-spacing:0.15em;text-transform:uppercase;font-family:'Inter',sans-serif;font-weight:600}
        .timing-table td{padding:.7rem 1rem;border-bottom:1px solid var(--border);vertical-align:top;line-height:1.6}
        .timing-table tr:nth-child(even){background:#f8f8f5}
        .timing-table tr:nth-child(odd){background:#fff}
        .timing-table tr:hover{background:rgba(0,48,128,.03)}

        /* CHECKLIST */
        .checklist-item{display:flex;align-items:center;gap:.6rem;padding:.5rem 0;font-size:.85rem}
        .checklist-item input[type="checkbox"]{width:20px;height:20px;accent-color:var(--navy);cursor:pointer;border-radius:4px}

        /* FOOTER */
        .footer{border-top:2px solid transparent;border-image:linear-gradient(90deg,var(--navy),var(--accent),var(--navy)) 1;padding:2rem;text-align:center}
        .footer p{font-size:.7rem;font-weight:500;letter-spacing:0.15em;text-transform:uppercase;color:var(--text-dim);font-variant:small-caps}

        /* RESPONSIVE */
        @media(max-width:767px){
            .header{min-height:260px;padding:2rem 1rem}
            .header h1{font-size:2.2rem}
            .student-info{gap:.6rem;font-size:.7rem}
            .student-info span{padding:.25rem .6rem}
            .container{padding:1.5rem 1rem}
            .tabs{padding:0 1rem}
            .tab-btn{font-size:.55rem;padding:.8rem .4rem}
            .card{padding:1.2rem;border-radius:8px}
            .card h3{font-size:1.5rem}
            .vocab-grid{grid-template-columns:1fr}
            .speed-control{width:100%;justify-content:center}
        }
        @media(min-width:1440px){.container{max-width:1100px}}

        /* ACCESSIBILITY */
        @media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}
        *:focus-visible{outline:3px solid var(--navy);outline-offset:2px;border-radius:4px}

        /* PRINT */
        @media print{
            .tabs-wrapper,.logo-bar,.speed-control,.header-accent-line,.footer{display:none}
            .tab-content{display:block!important;page-break-before:always}
            .header{min-height:auto;padding:1.5rem;background:none!important}
            .header::before,.header::after{display:none}
            .header h1{color:#000}
            .header .subtitle,.student-info span{color:#333}
            .progress-passport{display:none}
            .vocab-card .audio-btn{display:none}
            body{background:#fff;color:#000}
            .card,.lesson-card{box-shadow:none;border:1px solid #ddd}
        }
    </style>
</head>
<body>
<div class="logo-bar"><img src="/assets/logo-alumni.png" alt="Alumni by Better"><span class="prof-badge">Professor View</span></div>
<header class="header">
    <div class="header-content">
        <h1>Maísa de Oliveira Santos</h1>
        <p class="subtitle">Inglês 360° — Conversação, Business English e Fluência Profissional</p>
        <div class="student-info"><span>A1</span><span>72 aulas</span><span>90 min</span><span>São Paulo</span><span>Online</span></div>
        <div class="progress-passport">
            <div class="progress-label"><span>Progresso Geral</span><span id="progressPercent">0%</span></div>
            <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
        </div>
    </div>
</header>
<div class="header-accent-line"></div>
<main class="container">
<div class="speed-control">
    <span class="speed-label"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg> Velocidade:</span>
    <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>
    <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>
    <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>
    <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>
</div>
<div class="tabs-wrapper">
<nav class="tabs" role="tablist">
    <button class="tab-btn active" role="tab" aria-selected="true" onclick="switchTab(0)">Planejamento Pedagógico</button>
    <button class="tab-btn" role="tab" aria-selected="false" onclick="switchTab(1)">Pre-class</button>
    <button class="tab-btn" role="tab" aria-selected="false" onclick="switchTab(2)">Plano de Aula</button>
    <button class="tab-btn" role="tab" aria-selected="false" onclick="switchTab(3)">Material do Professor</button>
    <button class="tab-btn" role="tab" aria-selected="false" onclick="switchTab(4)">Atividades Complementares</button>
</nav>
</div>

<!-- TAB 1: PLANEJAMENTO PEDAGOGICO -->
<section class="tab-content active" id="tab-0">
<div class="card">
    <h3>Programa Private — Inglês 360°</h3>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-top:1rem">
        <div><strong style="font-size:.65rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-dim);font-weight:700">Aluna</strong><br><span style="font-size:.9rem">Maísa de Oliveira Santos, 35 anos</span></div>
        <div><strong style="font-size:.65rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-dim);font-weight:700">Profissão</strong><br><span style="font-size:.9rem">Profissional do Mercado Financeiro</span></div>
        <div><strong style="font-size:.65rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-dim);font-weight:700">Cidade</strong><br><span style="font-size:.9rem">São Paulo</span></div>
        <div><strong style="font-size:.65rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-dim);font-weight:700">Nível</strong><br><span style="font-size:.9rem">A1</span></div>
        <div><strong style="font-size:.65rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-dim);font-weight:700">Foco</strong><br><span style="font-size:.9rem">Inglês 360°</span></div>
        <div><strong style="font-size:.65rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-dim);font-weight:700">Frequência</strong><br><span style="font-size:.9rem">2x/semana</span></div>
        <div><strong style="font-size:.65rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-dim);font-weight:700">Professor</strong><br><span style="font-size:.9rem">Maria Luisa</span></div>
        <div><strong style="font-size:.65rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-dim);font-weight:700">Horário</strong><br><span style="font-size:.9rem">Terças 7h</span></div>
        <div><strong style="font-size:.65rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-dim);font-weight:700">Início</strong><br><span style="font-size:.9rem">2026-05-05</span></div>
        <div><strong style="font-size:.65rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-dim);font-weight:700">Término</strong><br><span style="font-size:.9rem">2027-02-02</span></div>
    </div>
</div>

<div class="card">
    <h3>Objetivo do Programa</h3>
    <p style="line-height:1.8;font-size:.9rem">O programa de 72 aulas de 90 minutos, 2 vezes por semana, responde diretamente ao padrão histórico de Maísa: ela desistiu de programas mais intensos por sobrecarga e de programas mais espaçados por perda de momentum. Duas aulas semanais criam consistência sem esgotamento.</p>
    <p style="line-height:1.8;font-size:.9rem;margin-top:.8rem">As 72 aulas (~36 semanas, aproximadamente 9 meses) cobrem com folga as três fases propostas:</p>
    <ul style="font-size:.9rem;line-height:2;padding-left:1.2rem;margin-top:.5rem">
        <li><strong>Fase 1 (aulas 1-24):</strong> Desbloqueio oral, conversação cotidiana, gramática funcional A2 consolidada</li>
        <li><strong>Fase 2 (aulas 25-48):</strong> Business English aplicado ao mercado financeiro, e-mails, reuniões com o sócio</li>
        <li><strong>Fase 3 (aulas 49-72):</strong> Fluência em contextos de alto risco, preparação para Miami e clientes internacionais</li>
    </ul>
</div>

<div class="card">
    <h3>Metodologia Alumni</h3>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem;margin-top:1rem">
        <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px;border-top:3px solid var(--navy)">
            <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.5rem">PPP Framework</h4>
            <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Presentation → Practice → Production. Cada aula segue este ciclo: apresentação do conteúdo, prática controlada com exercícios, e produção livre com role-plays reais.</p>
        </div>
        <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px;border-top:3px solid var(--accent)">
            <h4 style="font-size:.7rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.5rem">Flipped Classroom</h4>
            <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">O Pre-class garante que Maísa chegue à aula com o vocabulário ativo. O tempo de aula é maximizado para PRODUÇÃO ORAL — não para exposição passiva.</p>
        </div>
        <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px;border-top:3px solid var(--success)">
            <h4 style="font-size:.7rem;font-weight:700;color:var(--success);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.5rem">Context-Based Learning</h4>
            <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Todo conteúdo é contextualizado na vida real de Maísa: mercado financeiro, São Paulo, sócio David, viagens a Miami. Nada é genérico.</p>
        </div>
        <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px;border-top:3px solid var(--warn)">
            <h4 style="font-size:.7rem;font-weight:700;color:var(--warn);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.5rem">Safe to Fail</h4>
            <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Ambiente seguro para errar. Correção seletiva (máximo 3 pontos por aula). Foco em comunicação antes de perfeição gramatical. Celebração de pequenas vitórias.</p>
        </div>
    </div>
</div>

<div class="card" style="border-left:4px solid var(--accent)">
    <h4>Jornada Transformadora</h4>
    <div style="display:grid;grid-template-columns:1fr auto 1fr;gap:1.5rem;align-items:center;margin-top:1rem">
        <div style="background:var(--danger-bg);padding:1.2rem;border-radius:8px;border:1px solid var(--danger-border)">
            <h4 style="color:var(--danger);margin-bottom:.5rem">De</h4>
            <p style="font-size:.9rem;line-height:1.7">"Profissional que não tem mais para onde fugir"</p>
        </div>
        <div style="color:var(--accent)"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>
        <div style="background:var(--success-bg);padding:1.2rem;border-radius:8px;border:1px solid var(--success-border)">
            <h4 style="color:var(--success);margin-bottom:.5rem">Para</h4>
            <p style="font-size:.9rem;line-height:1.7">"Conversar no elevador, reuniões com sócio, Miami"</p>
        </div>
    </div>
</div>

<div class="card" style="border-left:4px solid var(--navy)">
    <h4>Promessa Transformadora</h4>
    <p style="font-size:1.05rem;font-weight:500;line-height:1.7;color:var(--white);margin-top:.5rem">De 'me esquivando de todas as oportunidades de passar vergonha' a conversar no elevador, responder e-mails e chegar em Miami sem medo — em 72 aulas.</p>
</div>

<div class="card">
    <h3>Forças da Aluna</h3>
    <ul style="font-size:.9rem;line-height:2;padding-left:1.2rem">
        <li>Autoconsciência pedagógica excepcional — sabe exatamente o que funciona e o que não funciona para ela</li>
        <li>Compreensão receptiva em B1 — base passiva sólida que acelera o desbloqueio da produção oral</li>
        <li>Motivação por urgência real — pressão profissional concreta sustenta engajamento</li>
        <li>Clareza de objetivo imediato — "conversar no elevador" como primeiro passo tangível</li>
        <li>Comprometimento com consistência — escolheu formato 2x/semana para manter ritmo</li>
    </ul>
</div>

<div class="card">
    <h3>Pontos de Melhoria</h3>
    <ul style="font-size:.9rem;line-height:2;padding-left:1.2rem">
        <li>Bloqueio de produção oral por ansiedade — principal barreira técnica e emocional</li>
        <li>Lacunas gramaticais sistemáticas — especialmente conjugação verbal</li>
        <li>Histórico de desistência por sobrecarga ou desmotivação</li>
        <li>Baixa exposição extraclasse — zero uso real do inglês fora de sala</li>
        <li>Tolerância ao erro baixa em contexto público</li>
    </ul>
</div>

<div class="card">
    <h3>Currículo Completo — 20 Aulas (Bloco 1)</h3>
    <div class="curriculum-wrapper"><table class="curriculum-table"><thead><tr><th>#</th><th>Tema</th><th>Foco Linguístico</th><th>Atividade em Aula</th><th>Homework</th></tr></thead><tbody>
<tr><td>1</td><td>Who Is Maísa? — Diagnostic Session</td><td>Verb to be, personal pronouns, self-introduction</td><td>Diagnostic + rapport + baseline recording</td><td>Record self-intro + 5 sentences</td></tr>
<tr><td>2</td><td>Elevator Moment — Small Talk</td><td>Verb to be full paradigm, What do you do?, small talk</td><td>Role-play elevator encounter</td><td>Record 90s elevator scenario</td></tr>
<tr><td>3</td><td>What Do You Do All Day? — Routine</td><td>Present simple, frequency adverbs, work routine vocab</td><td>Build real daily routine together</td><td>Write Monday paragraph + audio</td></tr>
<tr><td>4</td><td>People, Places, Numbers</td><td>Numbers 1-1000, there is/are, prepositions</td><td>Dictation + building description</td><td>5 sentences about office + numbers audio</td></tr>
<tr><td>5</td><td>This Is My World — Company &amp; Role</td><td>Have/has, work with/for/at, possessives, company vocab</td><td>Company Profile Card + simulation</td><td>LinkedIn-style company bio</td></tr>
<tr><td>6</td><td>Can You, or Can't You?</td><td>Modal can (ability/permission/request), pronunciation can/can't</td><td>Back-and-forth can requests drill</td><td>6 sentences can/can't + response audio</td></tr>
<tr><td>7</td><td>Like, Love, Hate — Preferences</td><td>Like/love/enjoy/hate/prefer + gerund, opinion phrases</td><td>Coffee conversation with David</td><td>8 preference sentences + audio</td></tr>
<tr><td>8</td><td>Past Moments</td><td>Simple past regular + irregular, time markers</td><td>Narrative production - Miami story</td><td>Paragraph about last week + Miami audio</td></tr>
<tr><td>9</td><td>What's Next? — Plans</td><td>Going to, present continuous future, will</td><td>Scheduling call role-play</td><td>Real schedule + availability audio</td></tr>
<tr><td>10</td><td>Checkpoint 10 — Consolidation</td><td>Full review aulas 1-9, meta-language</td><td>Integrated speaking + elevator simulation</td><td>3-min progress report</td></tr>
<tr><td>11</td><td>Describing People and Personalities</td><td>Adjectives, comparatives, personality vocab</td><td>Describe colleagues and compare work styles</td><td>Write descriptions of 3 colleagues</td></tr>
<tr><td>12</td><td>São Paulo Through International Eyes</td><td>Present simple for places, superlatives, city vocab</td><td>Be a tour guide: present SP to a visitor</td><td>Write a short guide to favorite SP area</td></tr>
<tr><td>13</td><td>Professional Emails Part 1</td><td>Email structure, register, greeting/closing formulas</td><td>Write and review professional emails</td><td>Draft 3 emails: greeting, request, follow-up</td></tr>
<tr><td>14</td><td>Career History and Past Narratives</td><td>Past simple + past continuous, career vocab, time linkers</td><td>Tell your career story chronologically</td><td>Write career timeline in English</td></tr>
<tr><td>15</td><td>Opinions and Arguments</td><td>Opinion expressions, agreeing/disagreeing, hedging</td><td>Debate a business topic with opinions</td><td>Write 5 opinions about market trends</td></tr>
<tr><td>16</td><td>Business Dining Language</td><td>Restaurant vocab, ordering, social English</td><td>Role-play: business dinner with David</td><td>Record ordering a meal + conversation</td></tr>
<tr><td>17</td><td>Presentations and Updates</td><td>Signposting language, data description, chart vocab</td><td>Give a 5-minute presentation</td><td>Prepare slides and script</td></tr>
<tr><td>18</td><td>Hypotheticals and Diplomatic Language</td><td>First/second conditional, negotiation vocab</td><td>Negotiation simulation with conditionals</td><td>Write 5 conditional sentences</td></tr>
<tr><td>19</td><td>Travel Ready — Airports and Hotels</td><td>Travel vocab, airport/hotel phrases, business travel</td><td>Full travel simulation: check-in to checkout</td><td>Write a travel itinerary for Miami</td></tr>
<tr><td>20</td><td>Block 1 Closing — Fluency Review</td><td>Full integration of all structures, self-assessment</td><td>Extended speaking test + self-assessment</td><td>Record final 5-min speaking sample</td></tr>
</tbody></table></div>
</div>

<div class="card">
    <h3>Critérios de Avaliação Contínua</h3>
    <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">A cada 10 aulas, a aluna será avaliada informalmente nos seguintes critérios:</p>
    <table class="timing-table">
        <thead><tr><th>Critério</th><th>Checkpoint 10</th><th>Checkpoint 20</th><th>Meta Final</th></tr></thead>
        <tbody>
            <tr><td><strong>Produção Oral</strong></td><td>30-60 segundos contínuos</td><td>2-3 minutos contínuos</td><td>5+ minutos fluentes</td></tr>
            <tr><td><strong>Vocabulário Ativo</strong></td><td>50-70 palavras</td><td>120-150 palavras</td><td>300+ palavras</td></tr>
            <tr><td><strong>Gramática</strong></td><td>Present simple + to be</td><td>Past + Future + Modals</td><td>Conditionals + Complex</td></tr>
            <tr><td><strong>Compreensão Auditiva</strong></td><td>Frases simples isoladas</td><td>Conversas curtas</td><td>Meetings reais</td></tr>
            <tr><td><strong>Confiança</strong></td><td>Fala com apoio do professor</td><td>Inicia conversas</td><td>Conversa naturalmente</td></tr>
            <tr><td><strong>Autonomia</strong></td><td>Faz homework</td><td>Busca exposição extra</td><td>Usa inglês no trabalho</td></tr>
        </tbody>
    </table>
</div>

<div class="card">
    <h3>Tracking de Homework</h3>
    <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Registro de entrega de tarefas — essencial para manter o ritmo de Maísa.</p>
    <table class="timing-table">
        <thead><tr><th>#</th><th>Homework</th><th>Entregue</th></tr></thead>
        <tbody>
            <tr><td>1</td><td>Record self-intro + 5 sentences</td><td><input type="checkbox" id="hw_1" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>2</td><td>Record 90s elevator scenario</td><td><input type="checkbox" id="hw_2" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>3</td><td>Write Monday paragraph + audio</td><td><input type="checkbox" id="hw_3" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>4</td><td>5 sentences about office + numbers audio</td><td><input type="checkbox" id="hw_4" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>5</td><td>LinkedIn-style company bio</td><td><input type="checkbox" id="hw_5" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>6</td><td>6 sentences can/can't + response audio</td><td><input type="checkbox" id="hw_6" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>7</td><td>8 preference sentences + audio</td><td><input type="checkbox" id="hw_7" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>8</td><td>Paragraph about last week + Miami audio</td><td><input type="checkbox" id="hw_8" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>9</td><td>Real schedule + availability audio</td><td><input type="checkbox" id="hw_9" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>10</td><td>3-min progress report</td><td><input type="checkbox" id="hw_10" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>11</td><td>Write descriptions of 3 colleagues</td><td><input type="checkbox" id="hw_11" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>12</td><td>Write a short guide to favorite SP area</td><td><input type="checkbox" id="hw_12" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>13</td><td>Draft 3 emails: greeting, request, follow-up</td><td><input type="checkbox" id="hw_13" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>14</td><td>Write career timeline in English</td><td><input type="checkbox" id="hw_14" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>15</td><td>Write 5 opinions about market trends</td><td><input type="checkbox" id="hw_15" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>16</td><td>Record ordering a meal + conversation</td><td><input type="checkbox" id="hw_16" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>17</td><td>Prepare slides and script</td><td><input type="checkbox" id="hw_17" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>18</td><td>Write 5 conditional sentences</td><td><input type="checkbox" id="hw_18" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>19</td><td>Write a travel itinerary for Miami</td><td><input type="checkbox" id="hw_19" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
            <tr><td>20</td><td>Record final 5-min speaking sample</td><td><input type="checkbox" id="hw_20" onchange="toggleChecklist(this)" style="width:18px;height:18px;accent-color:var(--navy)"></td></tr>
        </tbody>
    </table>
</div>

<div class="card">
    <div class="cancellation-rules">
        <h4><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg> Regras de Cancelamento</h4>
        <ul style="font-size:.85rem;line-height:1.8;padding-left:1.2rem;margin-top:.5rem">
            <li>Cancelamento com mais de 24h de antecedência: aula reagendada sem custo.</li>
            <li>Cancelamento com menos de 24h: aula contabilizada.</li>
            <li>No-show (não comparecimento sem aviso): aula contabilizada.</li>
            <li>Atrasos superiores a 15 minutos: aula pode ser encurtada ou reagendada.</li>
            <li>Máximo de 3 cancelamentos consecutivos — reunião de realinhamento obrigatória.</li>
        </ul>
    </div>
</div>
</section>

<!-- TAB 2: PRE-CLASS -->
<section class="tab-content" id="tab-1">
${buildPreclassTab()}
</section>

<!-- TAB 3: PLANO DE AULA -->
<section class="tab-content" id="tab-2">
${buildPlanoDeAulaTab()}
</section>

<!-- TAB 4: MATERIAL DO PROFESSOR -->
<section class="tab-content" id="tab-3">
${buildMaterialTab()}
</section>

<!-- TAB 5: ATIVIDADES COMPLEMENTARES -->
<section class="tab-content" id="tab-4">
${buildAtividadesTab()}
</section>

</main>

<footer class="footer">
    <p>Alumni by Better — Plano Pedagógico Personalizado</p>
    <p style="margin-top:.5rem;font-size:.6rem;color:var(--text-dim);letter-spacing:0.1em">Maísa de Oliveira Santos — Inglês 360° — Gerado em ${new Date().toISOString().split('T')[0]}</p>
    <p style="margin-top:.3rem;font-size:.55rem;color:var(--text-dim);letter-spacing:0.08em">Professora: Maria Luisa | Início: 2026-05-05 | Término previsto: 2027-02-02</p>
    <p style="margin-top:.3rem;font-size:.55rem;color:var(--text-dim);letter-spacing:0.08em">Bloco 1: Aulas 1-20 | Foco: Desbloqueio oral + Business English básico</p>
    <div style="margin-top:1rem;padding-top:1rem;border-top:1px solid var(--border)">
        <p style="font-size:.55rem;color:var(--text-dim);letter-spacing:0.05em;line-height:1.8">
            Este plano pedagógico foi desenvolvido com base no perfil individual da aluna, incluindo análise de necessidades,<br>
            estilo de aprendizagem, objetivos profissionais e histórico educacional. O conteúdo é atualizado progressivamente<br>
            pelo corpo docente Alumni by Better conforme o avanço da aluna. Todos os materiais são de uso exclusivo e confidencial.<br>
            Reprodução ou compartilhamento sem autorização expressa é proibido.
        </p>
    </div>
</footer>

<script>
// ─── Audio Map ───
var audioMap = ${audioMapJSON};

// ─── speakText function ───
function speakText(text) {
    if (audioMap[text]) {
        var audio = new Audio('/' + audioMap[text]);
        audio.playbackRate = window._audioSpeed || 1;
        audio.play().catch(function(){
            _speakFallback(text);
        });
    } else {
        _speakFallback(text);
    }
}

function _speakFallback(text) {
    if (typeof speakWithFallback === 'function') {
        speakWithFallback(text, { rate: window._audioSpeed || 1 });
    } else {
        var u = new SpeechSynthesisUtterance(text);
        u.lang = 'en-US';
        u.rate = (window._audioSpeed || 1) * 0.85;
        speechSynthesis.speak(u);
    }
}

// ─── Tab Switching ───
function switchTab(index) {
    var tabs = document.querySelectorAll('.tab-content');
    var btns = document.querySelectorAll('.tab-btn');
    tabs.forEach(function(t, i) {
        t.classList.toggle('active', i === index);
    });
    btns.forEach(function(b, i) {
        b.classList.toggle('active', i === index);
        b.setAttribute('aria-selected', i === index ? 'true' : 'false');
    });
    localStorage.setItem('maisa_prof_tab', index);
}

// ─── Lesson Toggle ───
function toggleLesson(header) {
    header.classList.toggle('open');
    var body = header.nextElementSibling;
    body.classList.toggle('open');
}

// ─── Audio Speed ───
function setAudioSpeed(speed, btn) {
    window._audioSpeed = speed;
    document.querySelectorAll('.speed-btn').forEach(function(b) {
        b.classList.remove('active');
    });
    btn.classList.add('active');
    localStorage.setItem('maisa_prof_speed', speed);
}

// ─── Checklist Persistence ───
function toggleChecklist(el) {
    var key = 'maisa_prof_cl_' + el.id;
    localStorage.setItem(key, el.checked ? '1' : '0');
    updateProgress();
}

// ─── Progress Bar ───
function updateProgress() {
    var checks = document.querySelectorAll('.checklist-item input[type="checkbox"]');
    var total = checks.length;
    if (total === 0) return;
    var done = 0;
    checks.forEach(function(c) { if (c.checked) done++; });
    var pct = Math.round((done / total) * 100);
    var bar = document.getElementById('progressBar');
    var label = document.getElementById('progressPercent');
    if (bar) bar.style.width = pct + '%';
    if (label) label.textContent = pct + '%';
}

// ─── State Restore ───
(function restoreState() {
    // Restore tab
    var savedTab = localStorage.getItem('maisa_prof_tab');
    if (savedTab !== null) {
        switchTab(parseInt(savedTab));
    }
    // Restore speed
    var savedSpeed = localStorage.getItem('maisa_prof_speed');
    if (savedSpeed) {
        window._audioSpeed = parseFloat(savedSpeed);
        document.querySelectorAll('.speed-btn').forEach(function(b) {
            b.classList.toggle('active', b.getAttribute('data-speed') === savedSpeed);
        });
    }
    // Restore checklists
    var checks = document.querySelectorAll('.checklist-item input[type="checkbox"]');
    checks.forEach(function(c) {
        var key = 'maisa_prof_cl_' + c.id;
        var val = localStorage.getItem(key);
        if (val === '1') c.checked = true;
    });
    // Restore media checkboxes
    for (var i = 0; i < 10; i++) {
        var el = document.getElementById('media_' + i);
        if (el) {
            var key = 'maisa_prof_cl_media_' + i;
            var val = localStorage.getItem(key);
            if (val === '1') el.checked = true;
        }
    }
    updateProgress();
})();
</script>
</body>
</html>`;

// ─── Write output ───
const outputPath = path.resolve(__dirname, '../public/professor/maisa-de-oliveira-santos.html');
const outputDir = path.dirname(outputPath);
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}
fs.writeFileSync(outputPath, html, 'utf-8');

const lines = html.split('\n').length;
console.log(`Generated: ${outputPath}`);
console.log(`Total lines: ${lines}`);
console.log(`File size: ${(Buffer.byteLength(html, 'utf-8') / 1024).toFixed(1)} KB`);
