#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = {
  ash: 'VU16byTywsWv5JpI8rbc',    // Male neutral (Rafael)
  riley: 'hA4zGnmTwX2NQiTRMt7o'   // Female neutral (Ana, general)
};
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'rafael-de-andrade-brandao');

const PHRASES = [
  // ===== Vocab words (Rafael=male → Ash) =====
  { text: "Schedule", file: "aula2_schedule.mp3", voice: VOICES.ash },
  { text: "Manage", file: "aula2_manage.mp3", voice: VOICES.ash },
  { text: "Department", file: "aula2_department.mp3", voice: VOICES.ash },
  { text: "Colleague", file: "aula2_colleague.mp3", voice: VOICES.ash },
  { text: "Usually", file: "aula2_usually.mp3", voice: VOICES.ash },
  { text: "Report", file: "aula2_report.mp3", voice: VOICES.ash },
  { text: "Attend", file: "aula2_attend.mp3", voice: VOICES.ash },
  { text: "Deadline", file: "aula2_deadline.mp3", voice: VOICES.ash },

  // ===== Vocab example sentences (alternate Ash/Riley) =====
  { text: "I check my schedule every morning.", file: "aula2_i_check_my_schedule_every_morning.mp3", voice: VOICES.ash },
  { text: "I manage a team of ten people at TVT.", file: "aula2_i_manage_a_team_of_ten_people.mp3", voice: VOICES.riley },
  { text: "The sales department is on the third floor.", file: "aula2_the_sales_department_is_on_the_third_floor.mp3", voice: VOICES.ash },
  { text: "My colleague Ana works in marketing.", file: "aula2_my_colleague_ana_works_in_marketing.mp3", voice: VOICES.riley },
  { text: "I usually start work at 8 AM.", file: "aula2_i_usually_start_work_at_8_am.mp3", voice: VOICES.ash },
  { text: "I report to the CEO every Friday.", file: "aula2_i_report_to_the_ceo_every_friday.mp3", voice: VOICES.riley },
  { text: "I attend three meetings every day.", file: "aula2_i_attend_three_meetings_every_day.mp3", voice: VOICES.ash },
  { text: "The deadline for the proposal is next Monday.", file: "aula2_the_deadline_for_the_proposal_is_next_monday.mp3", voice: VOICES.riley },

  // ===== Fill-in sentences (alternate) =====
  { text: "I usually start my day at 8 AM and check my emails.", file: "aula2_i_usually_start_my_day_at_8_am.mp3", voice: VOICES.ash },
  { text: "She manages the marketing department at our company.", file: "aula2_she_manages_the_marketing_department.mp3", voice: VOICES.riley },
  { text: "My colleagues and I attend a team meeting every Monday.", file: "aula2_my_colleagues_and_i_attend_a_team_meeting.mp3", voice: VOICES.ash },
  { text: "He usually reports to the director before the deadline.", file: "aula2_he_usually_reports_to_the_director.mp3", voice: VOICES.riley },
  { text: "We always have a meeting on Monday mornings.", file: "aula2_we_always_have_a_meeting_on_monday.mp3", voice: VOICES.ash },
  { text: "I sometimes work late before a big deadline.", file: "aula2_i_sometimes_work_late_before_deadline.mp3", voice: VOICES.riley },

  // ===== Speech/pronunciation cards (alternate) =====
  { text: "I usually start at 8 AM. I check my schedule every morning.", file: "aula2_speech_i_usually_start_at_8.mp3", voice: VOICES.ash },
  { text: "I manage the sales team. We have ten people in the department.", file: "aula2_speech_i_manage_the_sales_team.mp3", voice: VOICES.riley },
  { text: "I always attend the Monday meeting. We discuss our deadlines.", file: "aula2_speech_i_always_attend_monday.mp3", voice: VOICES.ash },
  { text: "I report to the CEO every Friday. I usually prepare the report on Thursday.", file: "aula2_speech_i_report_to_ceo.mp3", voice: VOICES.riley },

  // ===== Survival card phrases (alternate) =====
  { text: "I usually start my day at 8 AM.", file: "aula2_survival_i_usually_start.mp3", voice: VOICES.ash },
  { text: "I am in charge of the sales department.", file: "aula2_survival_i_am_in_charge.mp3", voice: VOICES.riley },
  { text: "We always have a team meeting on Mondays.", file: "aula2_survival_we_always_have.mp3", voice: VOICES.ash },
  { text: "I need to finish this before the deadline.", file: "aula2_survival_i_need_to_finish.mp3", voice: VOICES.riley },
  { text: "Could I schedule a meeting for next week?", file: "aula2_survival_could_i_schedule.mp3", voice: VOICES.ash },

  // ===== Ordering exercise =====
  { text: "I usually start my day at 8 AM and check my emails. Then I attend a team meeting with my colleagues at 9 AM. After lunch, I usually attend meetings with clients. Before I leave, I always check my schedule for the next day. I usually leave the office at 6 PM.", file: "aula2_order_l2_ordering.mp3", voice: VOICES.ash },

  // ===== Dialogue: Ana (Riley) + Rafael (Ash) =====
  { text: "Good morning, Rafael! I just joined the sales department. What is your typical day like?", file: "aula2_dialogue_ana_1.mp3", voice: VOICES.riley },
  { text: "Good morning, Ana! I usually start at 8 AM. I check my emails and schedule first.", file: "aula2_dialogue_rafael_2.mp3", voice: VOICES.ash },
  { text: "Do you have many meetings?", file: "aula2_dialogue_ana_3.mp3", voice: VOICES.riley },
  { text: "Yes, I usually attend three or four meetings a day. I manage the whole sales team.", file: "aula2_dialogue_rafael_4.mp3", voice: VOICES.ash },
  { text: "What about your colleagues? How often do you work together?", file: "aula2_dialogue_ana_5.mp3", voice: VOICES.riley },
  { text: "We always have a team meeting on Monday mornings. We discuss deadlines and reports.", file: "aula2_dialogue_rafael_6.mp3", voice: VOICES.ash },
  { text: "That sounds busy! Do you sometimes work late?", file: "aula2_dialogue_ana_7.mp3", voice: VOICES.riley },
  { text: "Sometimes, especially before a big deadline. But I usually leave at 6 PM.", file: "aula2_dialogue_rafael_8.mp3", voice: VOICES.ash },

  // ===== Listening passages =====
  { text: "Hello. My name is Carlos Rivera. I am the IT Director at DataCore Systems. I usually arrive at the office at 7:30 AM. First, I check my emails and attend a quick team meeting. I manage a department of twelve engineers. We often work on complex projects with tight deadlines. I sometimes travel to meet clients, but I usually work from the office. I always try to leave by 6 PM because I believe in work-life balance.", file: "aula2_listening_intro.mp3", voice: VOICES.ash },
  { text: "Hi, I am Priya Sharma. I work as Head of Sales at NovaTech. My department has twenty people. We usually start the day with a brief team call at 9 AM. My colleagues and I always review our sales targets on Mondays. I often attend meetings with international clients in the afternoon. I rarely work on weekends, but before a big deadline, I sometimes stay late. I report directly to the CEO.", file: "aula2_listening_meeting.mp3", voice: VOICES.riley },

  // ===== IN CLASS toolkit phrases =====
  { text: "I usually start my day at 8 AM.", file: "aula2_toolkit_1.mp3", voice: VOICES.ash },
  { text: "I am in charge of the sales department.", file: "aula2_toolkit_2.mp3", voice: VOICES.riley },
  { text: "We always have a team meeting on Mondays.", file: "aula2_toolkit_3.mp3", voice: VOICES.ash },
  { text: "I need to finish this before the deadline.", file: "aula2_toolkit_4.mp3", voice: VOICES.riley },
  { text: "Could I schedule a meeting for next week?", file: "aula2_toolkit_5.mp3", voice: VOICES.ash },

  // ===== Grammar examples (alternate) =====
  { text: "I usually start at 8 AM.", file: "aula2_gram_i_usually_start.mp3", voice: VOICES.ash },
  { text: "She always checks her emails first.", file: "aula2_gram_she_always_checks.mp3", voice: VOICES.riley },
  { text: "We often attend client meetings.", file: "aula2_gram_we_often_attend.mp3", voice: VOICES.ash },
  { text: "He sometimes works late on Fridays.", file: "aula2_gram_he_sometimes_works.mp3", voice: VOICES.riley },
  { text: "I am always on time for meetings.", file: "aula2_gram_i_am_always_on_time.mp3", voice: VOICES.ash },
  { text: "They never miss the Monday meeting.", file: "aula2_gram_they_never_miss.mp3", voice: VOICES.riley },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch(API_URL + '/' + voiceId, {
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
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => {
    const k = p.file.toLowerCase();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });

  console.log('Generating ' + unique.length + ' audio files for Rafael Aula 2...');
  let generated = 0, skipped = 0;

  for (const p of unique) {
    const outPath = path.join(OUTPUT_DIR, p.file);
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
