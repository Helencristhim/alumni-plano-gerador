#!/usr/bin/env node
/**
 * Build script for Maisa de Oliveira Santos — Student (Aluno) HTML
 * Generates: public/aluno/maisa-de-oliveira-santos.html
 * Run: node scripts/build-maisa-aluno.js
 *
 * Only 2 tabs: Pre-class | Atividades Complementares
 * NO teacher guides, NO CCQs, NO answer keys, NO Plano de Aula, NO Material do Professor
 * NO homework section, NO checklists "O que eu aprendi"
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
    { word: 'name', pt: 'nome', example: 'My name is Maisa.' },
    { word: 'work', pt: 'trabalho / trabalhar', example: 'I work in finance.' },
    { word: 'live', pt: 'morar', example: 'I live in Sao Paulo.' },
    { word: 'company', pt: 'empresa', example: 'My company has international partners.' },
    { word: 'meeting', pt: 'reuniao', example: 'I have a meeting today.' },
    { word: 'client', pt: 'cliente', example: 'The client called this morning.' },
    { word: 'partner', pt: 'socio / parceiro', example: 'My partner is from New York.' }
  ],
  2: [
    { word: 'Good morning', pt: 'Bom dia', example: 'Good morning, David. How\'s it going?' },
    { word: 'How are you', pt: 'Como voce esta', example: 'How are you today?' },
    { word: 'What do you do', pt: 'O que voce faz', example: 'What do you do for a living?' },
    { word: 'Where are you from', pt: 'De onde voce e', example: 'Where are you from originally?' },
    { word: 'Nice to meet you', pt: 'Prazer em conhece-lo', example: 'Nice to meet you. I\'m Maisa.' },
    { word: 'weekend', pt: 'fim de semana', example: 'Do you have plans for the weekend?' },
    { word: 'elevator', pt: 'elevador', example: 'I take the elevator every morning.' }
  ],
  3: [
    { word: 'attend meetings', pt: 'participar de reunioes', example: 'I usually attend meetings on Mondays.' },
    { word: 'review reports', pt: 'revisar relatorios', example: 'I review market data every morning.' },
    { word: 'send emails', pt: 'enviar e-mails', example: 'I send emails to clients daily.' },
    { word: 'meet clients', pt: 'encontrar clientes', example: 'I meet clients in the afternoon.' },
    { word: 'work from home', pt: 'trabalhar de casa', example: 'I sometimes work from home.' },
    { word: 'always', pt: 'sempre', example: 'I always check my emails first.' },
    { word: 'usually', pt: 'geralmente', example: 'I usually finish around seven.' }
  ],
  4: [
    { word: 'floor', pt: 'andar', example: 'My office is on the third floor.' },
    { word: 'meeting room', pt: 'sala de reuniao', example: 'There is a meeting room on every floor.' },
    { word: 'reception', pt: 'recepcao', example: 'Please wait at the reception.' },
    { word: 'next to', pt: 'ao lado de', example: 'The meeting room is next to the elevator.' },
    { word: 'across from', pt: 'em frente a', example: 'The kitchen is across from my office.' },
    { word: 'schedule', pt: 'agenda / horario', example: 'My schedule is very full today.' },
    { word: 'conference call', pt: 'conferencia telefonica', example: 'We have a conference call at three.' }
  ],
  5: [
    { word: 'team', pt: 'equipe', example: 'My team manages client portfolios.' },
    { word: 'department', pt: 'departamento', example: 'The finance department is on the fifth floor.' },
    { word: 'headquarters', pt: 'sede', example: 'Our headquarters is in Sao Paulo.' },
    { word: 'senior analyst', pt: 'analista senior', example: 'I am a senior analyst.' },
    { word: 'portfolio manager', pt: 'gestor de portfolio', example: 'The portfolio manager reviews assets weekly.' },
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
    { word: 'Can you...?', pt: 'Voce pode...?', example: 'Can you join the meeting at three?' }
  ],
  7: [
    { word: 'enjoy', pt: 'gostar / aproveitar', example: 'I enjoy reading market analysis.' },
    { word: 'prefer', pt: 'preferir', example: 'I prefer email to phone calls.' },
    { word: 'binge-watch', pt: 'maratonar', example: 'I binge-watch series on weekends.' },
    { word: 'episode', pt: 'episodio', example: 'I watched three episodes last night.' },
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
    { word: 'tomorrow', pt: 'amanha', example: 'I am going to attend the meeting tomorrow.' },
    { word: 'next week', pt: 'semana que vem', example: 'We need to reschedule for next week.' },
    { word: 'postpone', pt: 'adiar', example: 'Can we postpone the deadline?' },
    { word: 'set up a call', pt: 'marcar uma ligacao', example: 'Let me set up a call with David.' },
    { word: 'block the calendar', pt: 'bloquear a agenda', example: 'I will block the calendar for Thursday.' },
    { word: 'unavailable', pt: 'indisponivel', example: 'I am unavailable on Monday morning.' },
    { word: 'by the end of the month', pt: 'ate o final do mes', example: 'The report is due by the end of the month.' }
  ],
  10: [
    { word: 'confident', pt: 'confiante', example: 'I feel more confident about speaking.' },
    { word: 'comfortable', pt: 'confortavel', example: 'I am comfortable with small talk now.' },
    { word: 'nervous', pt: 'nervoso(a)', example: 'I was nervous in the first class.' },
    { word: 'improvement', pt: 'melhoria', example: 'My biggest improvement is vocabulary.' },
    { word: 'grammar', pt: 'gramatica', example: 'I still need to work on grammar.' },
    { word: 'vocabulary', pt: 'vocabulario', example: 'My vocabulary has grown a lot.' },
    { word: 'fluency', pt: 'fluencia', example: 'Fluency takes time and practice.' }
  ]
};

// ─── Matching data (English → Portuguese, 3 options) ───
const matchingData = {
  1: [
    { en: 'name', options: ['nome', 'empresa', 'reuniao'], correct: 'nome' },
    { en: 'work', options: ['morar', 'trabalhar', 'cliente'], correct: 'trabalhar' },
    { en: 'meeting', options: ['parceiro', 'reuniao', 'nome'], correct: 'reuniao' },
    { en: 'client', options: ['cliente', 'empresa', 'trabalhar'], correct: 'cliente' },
    { en: 'partner', options: ['reuniao', 'morar', 'parceiro'], correct: 'parceiro' }
  ],
  2: [
    { en: 'Good morning', options: ['Bom dia', 'Boa noite', 'Ate logo'], correct: 'Bom dia' },
    { en: 'How are you', options: ['O que voce faz', 'Como voce esta', 'De onde voce e'], correct: 'Como voce esta' },
    { en: 'Nice to meet you', options: ['Ate logo', 'Prazer em conhece-lo', 'Bom dia'], correct: 'Prazer em conhece-lo' },
    { en: 'weekend', options: ['elevador', 'fim de semana', 'escritorio'], correct: 'fim de semana' },
    { en: 'elevator', options: ['elevador', 'reuniao', 'andar'], correct: 'elevador' }
  ],
  3: [
    { en: 'attend meetings', options: ['enviar e-mails', 'participar de reunioes', 'trabalhar de casa'], correct: 'participar de reunioes' },
    { en: 'send emails', options: ['enviar e-mails', 'revisar relatorios', 'encontrar clientes'], correct: 'enviar e-mails' },
    { en: 'work from home', options: ['encontrar clientes', 'trabalhar de casa', 'participar de reunioes'], correct: 'trabalhar de casa' },
    { en: 'always', options: ['geralmente', 'nunca', 'sempre'], correct: 'sempre' },
    { en: 'usually', options: ['sempre', 'geralmente', 'raramente'], correct: 'geralmente' }
  ],
  4: [
    { en: 'floor', options: ['sala de reuniao', 'andar', 'recepcao'], correct: 'andar' },
    { en: 'meeting room', options: ['sala de reuniao', 'andar', 'agenda'], correct: 'sala de reuniao' },
    { en: 'next to', options: ['em frente a', 'ao lado de', 'entre'], correct: 'ao lado de' },
    { en: 'schedule', options: ['agenda', 'andar', 'recepcao'], correct: 'agenda' },
    { en: 'across from', options: ['ao lado de', 'entre', 'em frente a'], correct: 'em frente a' }
  ],
  5: [
    { en: 'team', options: ['equipe', 'departamento', 'filial'], correct: 'equipe' },
    { en: 'headquarters', options: ['filial', 'sede', 'departamento'], correct: 'sede' },
    { en: 'investment firm', options: ['gestor de portfolio', 'firma de investimentos', 'analista senior'], correct: 'firma de investimentos' },
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
    { en: 'binge-watch', options: ['maratonar', 'temporada', 'episodio'], correct: 'maratonar' },
    { en: 'episode', options: ['temporada', 'episodio', 'reviravolta'], correct: 'episodio' },
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
    { en: 'tomorrow', options: ['amanha', 'semana que vem', 'ontem'], correct: 'amanha' },
    { en: 'postpone', options: ['adiar', 'marcar', 'bloquear'], correct: 'adiar' },
    { en: 'set up a call', options: ['marcar uma ligacao', 'bloquear a agenda', 'adiar'], correct: 'marcar uma ligacao' },
    { en: 'unavailable', options: ['disponivel', 'indisponivel', 'ocupado'], correct: 'indisponivel' },
    { en: 'next week', options: ['semana passada', 'semana que vem', 'mes que vem'], correct: 'semana que vem' }
  ],
  10: [
    { en: 'confident', options: ['nervoso', 'confiante', 'confortavel'], correct: 'confiante' },
    { en: 'comfortable', options: ['confortavel', 'confiante', 'nervoso'], correct: 'confortavel' },
    { en: 'improvement', options: ['gramatica', 'melhoria', 'fluencia'], correct: 'melhoria' },
    { en: 'fluency', options: ['vocabulario', 'gramatica', 'fluencia'], correct: 'fluencia' },
    { en: 'nervous', options: ['confiante', 'nervoso', 'confortavel'], correct: 'nervoso' }
  ]
};

// ─── Fill-in data ───
const fillData = {
  1: [
    { sentence: 'My ___ is Maisa de Oliveira Santos.', answer: 'name', hint: 'nome' },
    { sentence: 'I ___ in finance in Sao Paulo.', answer: 'work', hint: 'trabalho' },
    { sentence: 'I ___ in Sao Paulo.', answer: 'live', hint: 'moro' },
    { sentence: 'My ___ has international partners.', answer: 'company', hint: 'empresa' },
    { sentence: 'I have a ___ today.', answer: 'meeting', hint: 'reuniao' }
  ],
  2: [
    { sentence: '___, David. How are you?', answer: 'Good morning', hint: 'Bom dia' },
    { sentence: '___ to meet you. I\'m Maisa.', answer: 'Nice', hint: 'Prazer' },
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
    { sentence: 'We have a ___ call at three.', answer: 'conference', hint: 'conferencia' }
  ],
  5: [
    { sentence: 'My ___ manages client portfolios.', answer: 'team', hint: 'equipe' },
    { sentence: 'Our ___ is in Sao Paulo.', answer: 'headquarters', hint: 'sede' },
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
    { sentence: 'I am going to attend the meeting ___.', answer: 'tomorrow', hint: 'amanha' },
    { sentence: 'We need to reschedule for ___.', answer: 'next week', hint: 'semana que vem' },
    { sentence: 'Can we ___ the deadline?', answer: 'postpone', hint: 'adiar' },
    { sentence: 'I will ___ the calendar for Thursday.', answer: 'block', hint: 'bloquear' },
    { sentence: 'I am ___ on Monday morning.', answer: 'unavailable', hint: 'indisponivel' }
  ],
  10: [
    { sentence: 'I feel more ___ about speaking English.', answer: 'confident', hint: 'confiante' },
    { sentence: 'I am ___ with small talk now.', answer: 'comfortable', hint: 'confortavel' },
    { sentence: 'My biggest ___ is vocabulary.', answer: 'improvement', hint: 'melhoria' },
    { sentence: 'I still need to work on ___.', answer: 'grammar', hint: 'gramatica' },
    { sentence: '___ takes time and practice.', answer: 'Fluency', hint: 'Fluencia' }
  ]
};

// ─── Multiple Choice data ───
const mcData = {
  1: { q: 'How do you say "Eu trabalho em financas" in English?', options: ['I work in finance.', 'I works in finance.', 'I working in finance.', 'I am work in finance.'], correct: 0 },
  2: { q: 'Which phrase is correct for greeting someone in the morning?', options: ['Good night!', 'Good morning!', 'Good afternoon!', 'Good evening!'], correct: 1 },
  3: { q: 'Which sentence uses "usually" correctly?', options: ['I usually attend meetings.', 'Usually I meetings attend.', 'I attend usually meetings.', 'Meetings I usually attend.'], correct: 0 },
  4: { q: 'How do you say "A sala de reuniao e no terceiro andar"?', options: ['The meeting room is in the third floor.', 'The meeting room is on the third floor.', 'The meeting room is at the third floor.', 'The meeting room is to the third floor.'], correct: 1 },
  5: { q: 'Which is the correct way to describe your role?', options: ['I am a senior analyst at my firm.', 'I am senior analyst at my firm.', 'I am a senior analyst in my firm.', 'I am the senior analyst from my firm.'], correct: 0 },
  6: { q: 'Which is a polite request?', options: ['Send me the file!', 'You send me the file.', 'Could you send me the file?', 'File send me.'], correct: 2 },
  7: { q: 'Which sentence expresses preference correctly?', options: ['I prefer email to phone calls.', 'I prefer email than phone calls.', 'I prefer email from phone calls.', 'I prefer email of phone calls.'], correct: 0 },
  8: { q: 'Which is the correct past form?', options: ['I sended the report.', 'I sent the report.', 'I sented the report.', 'I send the report yesterday.'], correct: 1 },
  9: { q: 'How do you talk about a future plan?', options: ['I going to attend the meeting.', 'I am going to attend the meeting.', 'I am go to attend the meeting.', 'I going attend the meeting.'], correct: 1 },
  10: { q: 'Which word means "melhoria" in English?', options: ['Grammar', 'Vocabulary', 'Improvement', 'Fluency'], correct: 2 }
};

// ─── Ordering data ───
const orderingData = {
  1: { correct: ['My', 'name', 'is', 'Maisa.'], shuffled: ['is', 'Maisa.', 'My', 'name'] },
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
  1: 'My name is Maisa.',
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
  1: ['My name is Maisa.', 'I work in finance.', 'I live in Sao Paulo.', 'Nice to meet you.', 'I\'m from Brazil.'],
  2: ['Good morning!', 'How are you?', 'Pretty good, thanks.', 'Have a good day!', 'See you later.'],
  3: ['I usually start at eight thirty.', 'I always check my emails first.', 'I sometimes work from home.', 'I review reports every morning.', 'I attend meetings in the afternoon.'],
  4: ['My office is on the third floor.', 'The meeting room is next to the elevator.', 'There are 12 people in the room.', 'The schedule is full today.', 'We have a conference call at three.'],
  5: ['I am a senior analyst.', 'My team manages client portfolios.', 'Our headquarters is in Sao Paulo.', 'Our firm has an international partner.', 'I work for a finance company.'],
  6: ['Could you send me the file?', 'Can you confirm the meeting?', 'Is it possible to reschedule?', 'I can handle that.', 'Would you mind checking this?'],
  7: ['I enjoy reading market analysis.', 'I prefer email to phone calls.', 'I like watching series.', 'What are you watching now?', 'Do you like thrillers?'],
  8: ['I attended a meeting yesterday.', 'I sent the report this morning.', 'We closed the deal last week.', 'I spoke with David on Friday.', 'Last March, I missed a trip to Miami.'],
  9: ['I am going to attend the meeting tomorrow.', 'We are meeting David at ten.', 'I will send you the agenda by Friday.', 'Are you free on Wednesday afternoon?', 'I will let you know by tomorrow.'],
  10: ['I feel more confident about speaking.', 'My biggest improvement is vocabulary.', 'I still need to work on grammar.', 'I think my English is improving.', 'Actually, I feel more confident now.']
};

// ─── Lesson titles ───
const lessonTitles = {
  1: 'Who Is Maisa? — Diagnostic Session',
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
  12: 'Sao Paulo Through International Eyes',
  13: 'Professional Emails Part 1',
  14: 'Career History and Past Narratives',
  15: 'Opinions and Arguments',
  16: 'Business Dining Language',
  17: 'Presentations and Updates',
  18: 'Hypotheticals and Diplomatic Language',
  19: 'Travel Ready — Airports and Hotels',
  20: 'Block 1 Closing — Fluency Review'
};

// ─── Grammar Tips ───
function getGrammarTip(n) {
  const tips = {
    1: '<strong>Verb TO BE</strong> — Em ingles, "to be" (ser/estar) muda de forma: I <u>am</u>, you <u>are</u>, he/she <u>is</u>. Nao esqueca: "I am" pode virar "I\'m" na fala. Exemplo: "I\'m Maisa. I\'m from Sao Paulo. I\'m a professional."',
    2: '<strong>Small Talk Pattern</strong> — Conversas curtas seguem um padrao: Greeting → Question → Response → Return question → Closing. Exemplo: "Good morning! How are you? — Pretty good! And you? — Great, thanks. Have a good day!"',
    3: '<strong>Frequency Adverbs</strong> — Eles vao ANTES do verbo principal: "I <u>always</u> check emails." "She <u>usually</u> finishes at seven." "We <u>sometimes</u> work from home." Ordem de frequencia: always (100%) > usually (80%) > often (60%) > sometimes (40%) > rarely (10%) > never (0%).',
    4: '<strong>There is / There are</strong> — Use "there IS" para singular: "There is ONE meeting room." Use "there ARE" para plural: "There are TWELVE people." Dica: ouca o que vem DEPOIS para escolher is/are.',
    5: '<strong>Have vs. Has</strong> — I/you/we/they HAVE. He/she/it HAS. "I <u>have</u> a team." "My company <u>has</u> offices in two cities." "She <u>has</u> international partners." Nao diga "she have" — sempre HAS para terceira pessoa.',
    6: '<strong>Can vs. Can\'t — Pronuncia</strong> — "Can" em frases soa fraco: /k&#601;n/. "Can\'t" soa forte: /k&aelig;nt/. A diferenca e sutil! Dica: em "I can DO it" o CAN e quase invisivel. Em "I CAN\'T do it" o CAN\'T e enfatizado. Pratique os dois lado a lado.',
    7: '<strong>Verb + -ING</strong> — Depois de like, love, enjoy, hate, prefer, usamos o verbo com -ING: "I enjoy <u>reading</u>." "I prefer <u>working</u> from home." "She loves <u>watching</u> series." NUNCA: "I enjoy read" ou "I prefer work."',
    8: '<strong>Past Simple — Regular vs. Irregular</strong> — Regulares: add -ed (worked, attended, reviewed). Irregulares: mudam completamente (go→went, send→sent, speak→spoke, have→had, meet→met). Os irregulares precisam ser memorizados — mas os mais comuns sao poucos!',
    9: '<strong>Tres formas de futuro</strong> — (1) "I\'m <u>going to</u> attend" = plano decidido. (2) "I\'m <u>meeting</u> David at 10" = compromisso agendado. (3) "I\'<u>ll</u> send it" = decisao/promessa no momento. Dica para Maisa: para agendamentos, use present continuous ("I\'m meeting...").',
    10: '<strong>Discourse Markers</strong> — Para organizar sua fala: "First of all..." (primeiro), "Then..." (depois), "After that..." (depois disso), "Also..." (alem disso), "To be honest..." (para ser honesta), "Actually..." (na verdade). Estes conectores fazem sua fala parecer mais natural e fluente.'
  };
  return tips[n] || '';
}

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

// ─── Build Pre-class tab content ───
function buildPreclassTab() {
  let html = '';

  // Onboarding
  html += `<div class="onboarding-welcome">
  <h2>Bem-vinda, Maisa!</h2>
  <p class="quote">"Every expert was once a beginner."</p>
  <p style="font-size:.9rem;color:var(--text-mid);margin-top:1rem">Complete os exercicios antes de cada aula para maximizar seu aprendizado.</p>
</div>

<div class="card">
  <h3><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:6px"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Frases de Emergencia</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Memorize estas frases antes de comecar. Use-as sempre que precisar durante qualquer aula.</p>
  <div style="display:grid;gap:.8rem">
    <div style="background:var(--bg-elevated);padding:.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between">
      <div><strong style="font-size:.9rem">I am sorry, I did not understand.</strong><br><span style="font-size:.8rem;color:var(--text-dim)">Desculpe, nao entendi.</span></div>
      <button class="audio-btn" onclick="speakText('I am sorry, I did not understand.')" style="background:var(--navy);color:#fff;border:none;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:.75rem">&#9654; Ouvir</button>
    </div>
    <div style="background:var(--bg-elevated);padding:.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between">
      <div><strong style="font-size:.9rem">Could you speak more slowly, please?</strong><br><span style="font-size:.8rem;color:var(--text-dim)">Pode falar mais devagar, por favor?</span></div>
      <button class="audio-btn" onclick="speakText('Could you speak more slowly, please?')" style="background:var(--navy);color:#fff;border:none;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:.75rem">&#9654; Ouvir</button>
    </div>
    <div style="background:var(--bg-elevated);padding:.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between">
      <div><strong style="font-size:.9rem">How do you say that in English?</strong><br><span style="font-size:.8rem;color:var(--text-dim)">Como se diz isso em ingles?</span></div>
      <button class="audio-btn" onclick="speakText('How do you say that in English?')" style="background:var(--navy);color:#fff;border:none;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:.75rem">&#9654; Ouvir</button>
    </div>
    <div style="background:var(--bg-elevated);padding:.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between">
      <div><strong style="font-size:.9rem">Excuse me, could you repeat that?</strong><br><span style="font-size:.8rem;color:var(--text-dim)">Com licenca, pode repetir?</span></div>
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
      var vocabHTML = '<h4 style="margin:1.5rem 0 .8rem;font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;">Vocabulario da Aula ${n}</h4><div class="vocab-grid">${genVocabCards(n).replace(/'/g, "\\'").replace(/\n/g, '')}</div>';

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
    <div class="placeholder-card">Conteudo sera adicionado progressivamente.</div>
  </div>
</div>\n`;
  }

  return html;
}

// ─── Build Atividades Complementares tab ───
function buildAtividadesTab() {
  const media = [
    { title: 'Succession (HBO)', type: 'SERIE', desc: 'Dinamica de poder corporativo, linguagem financeira, family business. Ideal para vocabulario de board meetings e corporate politics.', lessons: '1-5' },
    { title: 'Industry (HBO)', type: 'SERIE', desc: 'Mercado financeiro de Londres, young professionals, alta pressao. Vocabulario tecnico de trading, risk, e office dynamics.', lessons: '3-8' },
    { title: 'Planet Money (NPR)', type: 'PODCAST', desc: 'Economia explicada de forma acessivel. Episodios de 20-30 minutos sobre temas financeiros do dia a dia. Otimo para listening.', lessons: '4-10' },
    { title: 'The Indicator (NPR)', type: 'PODCAST', desc: 'Episodios de 10 minutos sobre indicadores economicos. Perfeito para praticar listening curto diariamente.', lessons: '1-10' },
    { title: 'Suits (USA Network)', type: 'SERIE', desc: 'Ingles corporativo e juridico. Otimo para formal register, negotiation language, e professional relationships.', lessons: '6-10' },
    { title: 'The Big Short (2015)', type: 'FILME', desc: 'Crise financeira de 2008 explicada com humor. Vocabulario de mercado financeiro denso mas acessivel pela narrativa.', lessons: '5-8' },
    { title: 'How I Built This (NPR)', type: 'PODCAST', desc: 'Historias de empreendedores contando como construiram suas empresas. Linguagem de business acessivel e inspiradora.', lessons: '5-10' }
  ];

  let html = `<div class="card">
  <h3>Atividades Complementares — Midia Recomendada</h3>
  <p style="font-size:.9rem;color:var(--text-mid);margin-bottom:1.5rem">Conteudos selecionados especificamente para o seu perfil profissional e nivel. Marque os que ja assistiu/ouviu para acompanhar seu progresso.</p>
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
  <h3>Como Usar o Conteudo Complementar</h3>
  <div style="display:grid;gap:1rem;margin-top:1rem">
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--navy)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Para Series</h4>
      <p style="font-size:.85rem;line-height:1.7">Assista com legendas em ingles. Pause e repita frases que achar uteis. Anote 3 expressoes novas por episodio. Na proxima aula, conte ao professor o que assistiu.</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--accent)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Para Podcasts</h4>
      <p style="font-size:.85rem;line-height:1.7">Ouca no trajeto ou durante exercicios. Na primeira vez, apenas escute. Na segunda, tente entender detalhes. Velocidade 0.75x e ok no inicio.</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1rem;border-radius:8px;border-left:3px solid var(--success)">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--success);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.4rem">Para Filmes</h4>
      <p style="font-size:.85rem;line-height:1.7">Assista primeiro por diversao. Depois, escolha uma cena de 5 minutos e analise: vocabulario, estruturas, pronuncia. Tente resumir o filme em ingles na proxima aula.</p>
    </div>
  </div>
</div>

<div class="card">
  <h3>Recomendacoes por Aula</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Conteudo especifico para complementar cada aula do bloco 1.</p>

  <div class="lesson-card">
    <div class="lesson-card-header" onclick="toggleLesson(this)">
      <h3><span class="lesson-number-badge">Aulas 1-2</span> Introducao e Small Talk</h3>
      <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
    </div>
    <div class="lesson-card-body">
      <table class="timing-table">
        <thead><tr><th>Midia</th><th>O que observar</th><th>Exercicio sugerido</th></tr></thead>
        <tbody>
          <tr><td>Succession S1E1 (primeiros 10 min)</td><td>Como os personagens se apresentam. Frases de greeting.</td><td>Anote 3 formas que os personagens usam para se cumprimentar.</td></tr>
          <tr><td>The Indicator — qualquer episodio</td><td>O host se apresenta no inicio. Ouca apenas a intro (1 min).</td><td>Tente entender: nome, cargo, tema do episodio.</td></tr>
          <tr><td>Industry S1E1 (primeiros 15 min)</td><td>Novos funcionarios se apresentam. Small talk no escritorio.</td><td>Escolha 2 frases de small talk e pratique em voz alta.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="lesson-card">
    <div class="lesson-card-header" onclick="toggleLesson(this)">
      <h3><span class="lesson-number-badge">Aulas 3-4</span> Rotina e Escritorio</h3>
      <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
    </div>
    <div class="lesson-card-body">
      <table class="timing-table">
        <thead><tr><th>Midia</th><th>O que observar</th><th>Exercicio sugerido</th></tr></thead>
        <tbody>
          <tr><td>Suits S1E1</td><td>A rotina dos advogados. Como descrevem seu dia.</td><td>Descreva a rotina de um personagem usando present simple.</td></tr>
          <tr><td>Planet Money — "The Office"</td><td>Vocabulario de escritorio e workplace culture.</td><td>Liste 5 palavras novas sobre escritorio que ouviu.</td></tr>
          <tr><td>Industry S1E2-E3</td><td>Os personagens descrevem numeros e resultados financeiros.</td><td>Anote como dizem numeros grandes (millions, percentages).</td></tr>
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
        <thead><tr><th>Midia</th><th>O que observar</th><th>Exercicio sugerido</th></tr></thead>
        <tbody>
          <tr><td>How I Built This — qualquer episodio</td><td>Como empreendedores descrevem suas empresas. Uso de have/has.</td><td>Resuma a empresa do episodio em 5 frases com have/has.</td></tr>
          <tr><td>Succession S1E3-E4</td><td>Pedidos e requests entre personagens. Linguagem de poder.</td><td>Identifique 3 requests polite e 3 diretos. Qual a diferenca?</td></tr>
          <tr><td>The Big Short (primeiros 30 min)</td><td>Vocabulario financeiro. Como explicam conceitos complexos.</td><td>Escolha 5 termos financeiros do filme e defina em ingles simples.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="lesson-card">
    <div class="lesson-card-header" onclick="toggleLesson(this)">
      <h3><span class="lesson-number-badge">Aulas 7-8</span> Preferencias e Passado</h3>
      <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
    </div>
    <div class="lesson-card-body">
      <table class="timing-table">
        <thead><tr><th>Midia</th><th>O que observar</th><th>Exercicio sugerido</th></tr></thead>
        <tbody>
          <tr><td>Succession S2 (qualquer episodio)</td><td>Personagens expressam opinoes: like, prefer, hate. Narrativas no passado.</td><td>Escolha um personagem e descreva o que ele/ela likes e hates.</td></tr>
          <tr><td>Planet Money — episodio sobre crise</td><td>Narrativas no passado. "What happened was..." "They decided to..."</td><td>Resuma o episodio usando past simple: First... Then... Finally...</td></tr>
          <tr><td>The Big Short (segunda metade)</td><td>Storytelling sobre eventos passados. Uso extensivo de past simple.</td><td>Conte a historia do filme para alguem usando past simple.</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="lesson-card">
    <div class="lesson-card-header" onclick="toggleLesson(this)">
      <h3><span class="lesson-number-badge">Aulas 9-10</span> Planos e Consolidacao</h3>
      <span class="expand-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></span>
    </div>
    <div class="lesson-card-body">
      <table class="timing-table">
        <thead><tr><th>Midia</th><th>O que observar</th><th>Exercicio sugerido</th></tr></thead>
        <tbody>
          <tr><td>Industry S1E5-E6</td><td>Personagens fazem planos: "I'm going to...", "We're meeting..."</td><td>Anote 5 frases sobre planos futuros que ouvir nos episodios.</td></tr>
          <tr><td>How I Built This — episodio favorito</td><td>O empreendedor fala sobre passado, presente e futuro.</td><td>Grave um audio de 3 minutos sobre SEU passado, presente e futuro.</td></tr>
          <tr><td>Suits S1E5-E6</td><td>Agendamento de reunioes, scheduling, calendars.</td><td>Role-play: agende uma reuniao ficticia baseada em uma cena do episodio.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="card">
  <h3>Playlist de Vocabulario Financeiro</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Recursos adicionais para exposicao ao ingles financeiro — sua area de atuacao.</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1rem">
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.6rem">Bloomberg Quicktake (YouTube)</h4>
      <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Videos curtos (3-5 min) sobre mercado financeiro. Ideal para vocabulario tecnico com visual explicativo.</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.6rem">Financial Times — Podcast "Behind the Money"</h4>
      <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Episodios de 20-30 min sobre bastidores do mercado financeiro. Ingles britanico, bom para diversificar sotaque.</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.6rem">Wall Street Journal — "The Journal" Podcast</h4>
      <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Noticias financeiras diarias em 15-20 min. Ingles americano claro, ritmo acessivel para A1-A2.</p>
    </div>
    <div style="background:var(--bg-elevated);padding:1.2rem;border-radius:8px">
      <h4 style="font-size:.7rem;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:.6rem">Margin Call (2011) — Filme</h4>
      <p style="font-size:.85rem;line-height:1.6;color:var(--text-mid)">Drama sobre crise financeira. Dialogos rapidos mas repetitivos. Bom para a fase 2 (aulas 11-20).</p>
    </div>
  </div>
</div>

<div class="card">
  <h3>Diario de Exposicao ao Ingles</h3>
  <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:1rem">Use este checklist semanal para garantir exposicao minima ao ingles fora da sala de aula.</p>
  <div style="display:grid;gap:.5rem">
    <div class="checklist-item"><input type="checkbox" id="exp_1" onchange="toggleChecklist(this)"><label for="exp_1">Assisti pelo menos 1 episodio de serie em ingles esta semana</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_2" onchange="toggleChecklist(this)"><label for="exp_2">Ouvi pelo menos 1 podcast em ingles esta semana</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_3" onchange="toggleChecklist(this)"><label for="exp_3">Li pelo menos 1 artigo/noticia em ingles esta semana</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_4" onchange="toggleChecklist(this)"><label for="exp_4">Pratiquei speaking sozinha (gravei audio) pelo menos 1x esta semana</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_5" onchange="toggleChecklist(this)"><label for="exp_5">Anotei pelo menos 5 palavras/expressoes novas esta semana</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_6" onchange="toggleChecklist(this)"><label for="exp_6">Tentei pensar em ingles por pelo menos 5 minutos (internal monologue)</label></div>
    <div class="checklist-item"><input type="checkbox" id="exp_7" onchange="toggleChecklist(this)"><label for="exp_7">Mudei o idioma de algum app/site para ingles</label></div>
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
    <title>Alumni — Maisa de Oliveira Santos</title>
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
<div class="logo-bar"><img src="/assets/logo-alumni.png" alt="Alumni by Better"></div>
<header class="header">
    <div class="header-content">
        <h1>Maisa de Oliveira Santos</h1>
        <p class="subtitle">Ingles 360 — Conversacao, Business English e Fluencia Profissional</p>
        <div class="student-info"><span>A1</span><span>72 aulas</span><span>90 min</span><span>Sao Paulo</span><span>Online</span></div>
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
    <button class="tab-btn active" role="tab" aria-selected="true" onclick="switchTab(0)">Pre-class</button>
    <button class="tab-btn" role="tab" aria-selected="false" onclick="switchTab(1)">Atividades Complementares</button>
</nav>
</div>

<!-- TAB 1: PRE-CLASS -->
<section class="tab-content active" id="tab-0">
${buildPreclassTab()}
</section>

<!-- TAB 2: ATIVIDADES COMPLEMENTARES -->
<section class="tab-content" id="tab-1">
${buildAtividadesTab()}
</section>

</main>

<footer class="footer">
    <p>Alumni by Better — Plano de Estudos Personalizado</p>
    <p style="margin-top:.5rem;font-size:.6rem;color:var(--text-dim);letter-spacing:0.1em">Maisa de Oliveira Santos — Ingles 360 — Gerado em ${new Date().toISOString().split('T')[0]}</p>
    <p style="margin-top:.3rem;font-size:.55rem;color:var(--text-dim);letter-spacing:0.08em">Professora: Maria Luisa | Inicio: 2026-05-05</p>
    <p style="margin-top:.3rem;font-size:.55rem;color:var(--text-dim);letter-spacing:0.08em">Bloco 1: Aulas 1-20 | Foco: Desbloqueio oral + Business English basico</p>
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
    localStorage.setItem('maisa_aluno_tab', index);
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
    localStorage.setItem('maisa_aluno_speed', speed);
}

// ─── Checklist Persistence ───
function toggleChecklist(el) {
    var key = 'maisa_aluno_cl_' + el.id;
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
    var savedTab = localStorage.getItem('maisa_aluno_tab');
    if (savedTab !== null) {
        switchTab(parseInt(savedTab));
    }
    // Restore speed
    var savedSpeed = localStorage.getItem('maisa_aluno_speed');
    if (savedSpeed) {
        window._audioSpeed = parseFloat(savedSpeed);
        document.querySelectorAll('.speed-btn').forEach(function(b) {
            b.classList.toggle('active', b.getAttribute('data-speed') === savedSpeed);
        });
    }
    // Restore checklists
    var checks = document.querySelectorAll('.checklist-item input[type="checkbox"]');
    checks.forEach(function(c) {
        var key = 'maisa_aluno_cl_' + c.id;
        var val = localStorage.getItem(key);
        if (val === '1') c.checked = true;
    });
    // Restore media checkboxes
    for (var i = 0; i < 10; i++) {
        var el = document.getElementById('media_' + i);
        if (el) {
            var key = 'maisa_aluno_cl_media_' + i;
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
const outputPath = path.resolve(__dirname, '../public/aluno/maisa-de-oliveira-santos.html');
const outputDir = path.dirname(outputPath);
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}
fs.writeFileSync(outputPath, html, 'utf-8');

const lines = html.split('\n').length;
console.log(`Generated: ${outputPath}`);
console.log(`Total lines: ${lines}`);
console.log(`File size: ${(Buffer.byteLength(html, 'utf-8') / 1024).toFixed(1)} KB`);
