const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'simone-quiles-de-santana-marques');

const PHRASES = [
  // Vocab words (ELLEN)
  { text: 'Schedule', voice: ELLEN, file: 'schedule.mp3' },
  { text: 'Review', voice: ELLEN, file: 'aula2_review.mp3' },
  { text: 'Deadline', voice: ELLEN, file: 'aula2_deadline.mp3' },
  { text: 'Report', voice: ELLEN, file: 'aula2_report.mp3' },
  { text: 'Attend', voice: ELLEN, file: 'aula2_attend.mp3' },
  { text: 'Approve', voice: ELLEN, file: 'aula2_approve.mp3' },
  { text: 'Draft', voice: ELLEN, file: 'aula2_draft.mp3' },
  { text: 'Department', voice: ELLEN, file: 'aula2_department.mp3' },
  { text: 'Brief', voice: ELLEN, file: 'aula2_brief.mp3' },
  { text: 'Coordinate', voice: ELLEN, file: 'aula2_coordinate.mp3' },

  // Vocab example sentences (alternate)
  { text: 'I check my schedule every morning before work.', voice: ELLEN, file: 'aula2_i_check_my_schedule_every_morning.mp3' },
  { text: 'Simone reviews contracts carefully before signing.', voice: ARTHUR, file: 'aula2_simone_reviews_contracts_carefully.mp3' },
  { text: 'The deadline for the report is next Friday.', voice: ELLEN, file: 'aula2_the_deadline_for_the_report.mp3' },
  { text: 'I need to send a report to the London office.', voice: ARTHUR, file: 'aula2_i_need_to_send_a_report.mp3' },
  { text: 'She attends three meetings every day.', voice: ELLEN, file: 'aula2_she_attends_three_meetings.mp3' },
  { text: 'The manager approved the new contract yesterday.', voice: ARTHUR, file: 'aula2_the_manager_approved_the_new_contract.mp3' },
  { text: 'I am drafting a new agreement for the client.', voice: ELLEN, file: 'aula2_i_am_drafting_a_new_agreement.mp3' },
  { text: 'The legal department has fifteen lawyers.', voice: ARTHUR, file: 'aula2_the_legal_department_has_fifteen.mp3' },
  { text: 'I need to brief my team before the call.', voice: ELLEN, file: 'aula2_i_need_to_brief_my_team.mp3' },
  { text: 'We coordinate with offices in three countries.', voice: ARTHUR, file: 'aula2_we_coordinate_with_offices.mp3' },

  // Dialogue (Tom=ARTHUR, Simone=ELLEN)
  { text: 'Good morning, Simone! What does a typical day look like for you?', voice: ARTHUR, file: 'aula2_tom_good_morning_simone.mp3' },
  { text: 'I usually start at eight thirty. I review my emails and check my schedule for the day.', voice: ELLEN, file: 'aula2_simone_i_usually_start.mp3' },
  { text: 'Do you attend many meetings?', voice: ARTHUR, file: 'aula2_tom_do_you_attend.mp3' },
  { text: 'Yes, I usually attend two or three meetings a day. I often coordinate with the London and Munich offices.', voice: ELLEN, file: 'aula2_simone_yes_i_usually_attend.mp3' },
  { text: 'What about deadlines? How do you manage them?', voice: ARTHUR, file: 'aula2_tom_what_about_deadlines.mp3' },
  { text: 'I always check my deadlines first thing in the morning. I never miss a deadline for contract reviews.', voice: ELLEN, file: 'aula2_simone_i_always_check.mp3' },
  { text: 'That is very organized. Do you draft contracts yourself?', voice: ARTHUR, file: 'aula2_tom_that_is_very_organized.mp3' },
  { text: 'Yes, I draft the initial versions and then my team reviews them. I always brief my department before important meetings.', voice: ELLEN, file: 'aula2_simone_yes_i_draft.mp3' },

  // Listening 1 (monologue — ELLEN)
  { text: 'Let me tell you about my typical day. I usually arrive at the office at eight thirty. The first thing I do is check my emails and review my schedule. I always have two or three meetings in the morning. I attend calls with our offices in London and Munich almost every day. After lunch, I usually draft contracts or review legal documents. I coordinate with my colleagues to make sure we meet all our deadlines. I never leave the office without checking tomorrow\'s schedule. On Fridays, I always brief my department about the week\'s progress and send a report to the management team.', voice: ELLEN, file: 'aula2_listening1_typical_day.mp3' },

  // Listening 2 (meeting — ARTHUR)
  { text: 'Good morning, team. Let us go around the table and share our schedules for this week. Please tell us your main deadlines, the meetings you need to attend, and any reports that are due. If you need to coordinate with another department, let us know now so we can plan ahead.', voice: ARTHUR, file: 'aula2_listening2_team_meeting.mp3' },

  // Fill-in phrases (alternate)
  { text: 'Simone always reviews her emails in the morning.', voice: ELLEN, file: 'aula2_fillin_simone_always_reviews.mp3' },
  { text: 'She usually attends three meetings a day.', voice: ARTHUR, file: 'aula2_fillin_she_usually_attends.mp3' },
  { text: 'The deadline for the contract is next Monday.', voice: ELLEN, file: 'aula2_fillin_the_deadline_for_the_contract.mp3' },
  { text: 'I need to coordinate with the Munich office today.', voice: ARTHUR, file: 'aula2_fillin_i_need_to_coordinate.mp3' },
  { text: 'He drafts all the agreements for the department.', voice: ELLEN, file: 'aula2_fillin_he_drafts_all_the_agreements.mp3' },
  { text: 'We never miss a deadline for important reports.', voice: ARTHUR, file: 'aula2_fillin_we_never_miss_a_deadline.mp3' },

  // Speech practice (ELLEN)
  { text: 'I usually start my day at eight thirty.', voice: ELLEN, file: 'aula2_speech_i_usually_start.mp3' },
  { text: 'I review contracts and attend meetings every day.', voice: ELLEN, file: 'aula2_speech_i_review_contracts.mp3' },
  { text: 'I always brief my team before important calls.', voice: ELLEN, file: 'aula2_speech_i_always_brief_my_team.mp3' },
  { text: 'I coordinate with offices in London and Munich.', voice: ELLEN, file: 'aula2_speech_i_coordinate_with_offices.mp3' },
  { text: 'I never miss a deadline for contract reviews.', voice: ELLEN, file: 'aula2_speech_i_never_miss_a_deadline.mp3' },

  // Survival card phrases (alternate)
  { text: 'What time does the meeting start?', voice: ARTHUR, file: 'aula2_what_time_does_the_meeting.mp3' },
  { text: 'I usually review contracts in the morning.', voice: ELLEN, file: 'aula2_i_usually_review_contracts.mp3' },
  { text: 'Could you send me the report by Friday?', voice: ARTHUR, file: 'aula2_could_you_send_me_the_report.mp3' },
  { text: 'I need to coordinate with the London office.', voice: ELLEN, file: 'aula2_i_need_to_coordinate_with_london.mp3' },
  { text: 'Let me check my schedule.', voice: ARTHUR, file: 'aula2_let_me_check_my_schedule.mp3' },

  // Ordering (ELLEN)
  { text: 'I usually arrive at eight thirty. First, I check my emails and review my schedule. Then, I attend meetings with the London and Munich offices. In the afternoon, I draft contracts and review legal documents. Before I leave, I always check tomorrow\'s deadlines.', voice: ELLEN, file: 'aula2_ordering_daily_routine.mp3' },

  // Grammar examples (ARTHUR)
  { text: 'Simone always reviews her emails first.', voice: ARTHUR, file: 'aula2_grammar_simone_always_reviews.mp3' },
  { text: 'She usually briefs her team in the morning.', voice: ARTHUR, file: 'aula2_grammar_she_usually_briefs.mp3' },
  { text: 'They sometimes coordinate with the London office.', voice: ARTHUR, file: 'aula2_grammar_they_sometimes_coordinate.mp3' },
  { text: 'She never misses a deadline.', voice: ARTHUR, file: 'aula2_grammar_she_never_misses.mp3' },
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

  console.log('Generating ' + unique.length + ' audio files for Simone Aula 2...');
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
