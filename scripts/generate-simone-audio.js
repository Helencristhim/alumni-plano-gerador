const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'simone-quiles-de-santana-marques');

const PHRASES = [
  // Emergency/Survival phrases (alternate)
  { text: 'Could you repeat that, please?', voice: ARTHUR, file: 'could_you_repeat_that_please.mp3' },
  { text: 'I am not sure I understand. Could you explain?', voice: ELLEN, file: 'i_am_not_sure_i_understand.mp3' },
  { text: 'Let me think about that for a moment.', voice: ARTHUR, file: 'let_me_think_about_that.mp3' },
  { text: 'Could I ask a question?', voice: ELLEN, file: 'could_i_ask_a_question.mp3' },
  { text: 'In my experience, I would say...', voice: ARTHUR, file: 'in_my_experience_i_would_say.mp3' },

  // Vocabulary words (ELLEN)
  { text: 'Contract', voice: ELLEN, file: 'contract.mp3' },
  { text: 'Negotiate', voice: ELLEN, file: 'negotiate.mp3' },
  { text: 'Agreement', voice: ELLEN, file: 'agreement.mp3' },
  { text: 'Corporate', voice: ELLEN, file: 'corporate.mp3' },
  { text: 'Responsible', voice: ELLEN, file: 'responsible.mp3' },
  { text: 'Currently', voice: ELLEN, file: 'currently.mp3' },
  { text: 'Deal', voice: ELLEN, file: 'deal.mp3' },
  { text: 'Meeting', voice: ELLEN, file: 'meeting.mp3' },
  { text: 'Colleague', voice: ELLEN, file: 'colleague.mp3' },
  { text: 'Introduce', voice: ELLEN, file: 'introduce.mp3' },

  // Vocab example sentences (alternate)
  { text: 'Simone works on international contracts at Telefonica.', voice: ELLEN, file: 'simone_works_on_international_contracts.mp3' },
  { text: 'We need to negotiate the terms of this agreement.', voice: ARTHUR, file: 'we_need_to_negotiate_the_terms.mp3' },
  { text: 'Both parties signed the agreement last week.', voice: ELLEN, file: 'both_parties_signed_the_agreement.mp3' },
  { text: 'She handles corporate legal matters for the company.', voice: ARTHUR, file: 'she_handles_corporate_legal_matters.mp3' },
  { text: 'I am responsible for reviewing all contracts.', voice: ELLEN, file: 'i_am_responsible_for_reviewing.mp3' },
  { text: 'We are currently working on a new international deal.', voice: ARTHUR, file: 'we_are_currently_working_on_a_new_deal.mp3' },
  { text: 'I deal with international clients every day.', voice: ELLEN, file: 'i_deal_with_international_clients.mp3' },
  { text: 'The meeting with the London office is at three.', voice: ARTHUR, file: 'the_meeting_with_the_london_office.mp3' },
  { text: 'My colleague from Germany will join the call.', voice: ELLEN, file: 'my_colleague_from_germany.mp3' },
  { text: 'Let me introduce myself. I am Simone Marques.', voice: ELLEN, file: 'let_me_introduce_myself_simone.mp3' },

  // Dialogue lines (James=ARTHUR, Simone=ELLEN)
  { text: 'Good morning! I do not think we have met. I am James Wilson from the London office.', voice: ARTHUR, file: 'james_good_morning_i_do_not_think.mp3' },
  { text: 'Nice to meet you, James. I am Simone Marques. I work in the legal department here in Brazil.', voice: ELLEN, file: 'simone_nice_to_meet_you_james.mp3' },
  { text: 'What do you do exactly in the legal department?', voice: ARTHUR, file: 'james_what_do_you_do_exactly.mp3' },
  { text: 'I am a corporate lawyer. I am responsible for contracts and mergers and acquisitions.', voice: ELLEN, file: 'simone_i_am_a_corporate_lawyer.mp3' },
  { text: 'That sounds very interesting. How long have you been at Telefonica?', voice: ARTHUR, file: 'james_that_sounds_very_interesting.mp3' },
  { text: 'I have worked here for several years. I currently deal with international agreements.', voice: ELLEN, file: 'simone_i_have_worked_here.mp3' },
  { text: 'We should definitely talk more. I deal with contracts for the UK operations.', voice: ARTHUR, file: 'james_we_should_definitely_talk_more.mp3' },
  { text: 'I would love to discuss that. Could we schedule a meeting this week?', voice: ELLEN, file: 'simone_i_would_love_to_discuss.mp3' },

  // Listening 1 (long monologue - ELLEN)
  { text: 'Good afternoon, everyone. My name is Simone Marques. I am a corporate lawyer at Telefonica in Brazil. I am responsible for contracts and mergers and acquisitions. I currently deal with international agreements between our offices in Brazil, the United Kingdom, and Germany. I negotiate terms with partners and review legal documents every day. I have worked in corporate law for over twenty years. It is a pleasure to meet all of you.', voice: ELLEN, file: 'listening1_simone_intro_monologue.mp3' },

  // Listening 2 (meeting opening - ARTHUR)
  { text: 'Welcome, everyone. Let us start the meeting. First, I would like each person to introduce themselves briefly. Please say your name, your role, and what office you are from. We have colleagues from London, Munich, and Sao Paulo joining us today. After introductions, we will discuss the agenda for the quarter.', voice: ARTHUR, file: 'listening2_meeting_opening.mp3' },

  // Fill-in exercise phrases (alternate)
  { text: 'I work at Telefonica in the legal department.', voice: ELLEN, file: 'fillin_i_work_at_telefonica.mp3' },
  { text: 'She negotiates contracts with international partners.', voice: ARTHUR, file: 'fillin_she_negotiates_contracts.mp3' },
  { text: 'He is responsible for the London office operations.', voice: ARTHUR, file: 'fillin_he_is_responsible_for_london.mp3' },
  { text: 'They currently deal with a new corporate agreement.', voice: ELLEN, file: 'fillin_they_currently_deal_with.mp3' },
  { text: 'We introduce ourselves at every meeting.', voice: ARTHUR, file: 'fillin_we_introduce_ourselves.mp3' },
  { text: 'My colleague and I negotiate deals together.', voice: ELLEN, file: 'fillin_my_colleague_and_i_negotiate.mp3' },

  // Speech practice phrases (ELLEN)
  { text: 'Good morning. My name is Simone Marques.', voice: ELLEN, file: 'speech_good_morning_my_name.mp3' },
  { text: 'I am a corporate lawyer at Telefonica.', voice: ELLEN, file: 'speech_i_am_a_corporate_lawyer.mp3' },
  { text: 'I am responsible for contracts and mergers and acquisitions.', voice: ELLEN, file: 'speech_i_am_responsible_for_contracts.mp3' },
  { text: 'I currently deal with international agreements.', voice: ELLEN, file: 'speech_i_currently_deal_with.mp3' },
  { text: 'I negotiate terms with partners from the United Kingdom and Germany.', voice: ELLEN, file: 'speech_i_negotiate_terms_with_partners.mp3' },

  // Quick Fire answers (ELLEN)
  { text: 'I am a corporate lawyer at Telefonica. I am responsible for contracts and M and A.', voice: ELLEN, file: 'quickfire_i_am_a_corporate_lawyer.mp3' },
  { text: 'I have worked in corporate law for over twenty years.', voice: ELLEN, file: 'quickfire_i_have_worked_in_corporate.mp3' },
  { text: 'I am currently working on international agreements.', voice: ELLEN, file: 'quickfire_i_am_currently_working.mp3' },
  { text: 'I deal with contracts between our offices in Brazil, the UK, and Germany.', voice: ELLEN, file: 'quickfire_i_deal_with_contracts.mp3' },
  { text: 'I would love to discuss this further. Could we schedule a meeting?', voice: ELLEN, file: 'quickfire_i_would_love_to_discuss.mp3' },
  { text: 'Let me introduce myself. I am Simone Marques from the legal department.', voice: ELLEN, file: 'quickfire_let_me_introduce_myself.mp3' },

  // Grammar practice sentences (IN CLASS)
  { text: 'Simone works at Telefonica.', voice: ARTHUR, file: 'grammar_simone_works_at_telefonica.mp3' },
  { text: 'She does not work in the marketing department.', voice: ARTHUR, file: 'grammar_she_does_not_work_marketing.mp3' },
  { text: 'Does she negotiate contracts?', voice: ARTHUR, file: 'grammar_does_she_negotiate_contracts.mp3' },
  { text: 'They deal with international partners every day.', voice: ELLEN, file: 'grammar_they_deal_with_international.mp3' },

  // Ordering exercise (full intro - ELLEN)
  { text: 'Good morning. Let me introduce myself. My name is Simone Marques. I am a corporate lawyer at Telefonica in Brazil. I am responsible for contracts and mergers and acquisitions. I currently deal with international agreements. I negotiate terms with partners from the United Kingdom and Germany.', voice: ELLEN, file: 'ordering_full_intro_simone.mp3' },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => {
    const k = p.file.toLowerCase();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });

  console.log('Generating ' + unique.length + ' audio files for Simone...');
  let generated = 0;
  let skipped = 0;

  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) {
      console.log('  SKIP (exists): ' + p.file);
      skipped++;
      continue;
    }
    try {
      const size = await gen(p.text, p.voice, outPath);
      generated++;
      console.log('  OK: ' + p.file + ' (' + Math.round(size / 1024) + ' KB)');
      await new Promise(r => setTimeout(r, 500));
    } catch (e) {
      console.error('  FAIL: ' + p.file + ' - ' + e.message);
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + unique.length);
}

main();
