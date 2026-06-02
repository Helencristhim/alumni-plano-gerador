const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'diogo-leal');

const PHRASES = [
  // Vocab words (Arthur — male student)
  { text: "Schedule", voice: ARTHUR, filename: "aula3_schedule" },
  { text: "Deadline", voice: ARTHUR, filename: "aula3_deadline" },
  { text: "Prioritize", voice: ARTHUR, filename: "aula3_prioritize" },
  { text: "Coordinate", voice: ARTHUR, filename: "aula3_coordinate" },
  { text: "Attend", voice: ARTHUR, filename: "aula3_attend" },
  { text: "Report", voice: ARTHUR, filename: "aula3_report" },
  { text: "Commute", voice: ARTHUR, filename: "aula3_commute" },
  { text: "Routine", voice: ARTHUR, filename: "aula3_routine" },

  // Fill-in-the-blank phrases (alternate Arthur/Ellen)
  { text: "I check my schedule every morning before the first meeting.", voice: ARTHUR, filename: "aula3_fill_schedule_morning" },
  { text: "The deadline for this project is next Friday.", voice: ELLEN, filename: "aula3_fill_deadline_friday" },
  { text: "I always prioritize urgent tasks from my stakeholders.", voice: ARTHUR, filename: "aula3_fill_prioritize_urgent" },
  { text: "I coordinate with teams in different countries every day.", voice: ELLEN, filename: "aula3_fill_coordinate_countries" },
  { text: "My commute from Parada Inglesa takes about forty-five minutes.", voice: ARTHUR, filename: "aula3_fill_commute_parada" },

  // Speech card / pronunciation phrases (Arthur — student protagonist)
  { text: "I usually start my day at seven and check my schedule.", voice: ARTHUR, filename: "aula3_speech_start_day" },
  { text: "I always coordinate with my team before attending meetings.", voice: ARTHUR, filename: "aula3_speech_coordinate_meetings" },
  { text: "I rarely miss a deadline because I prioritize my tasks.", voice: ARTHUR, filename: "aula3_speech_rarely_miss" },

  // Survival card (alternate Arthur/Ellen)
  { text: "I usually start my day at seven in the morning.", voice: ARTHUR, filename: "aula3_surv_start_day" },
  { text: "I always prioritize my deadlines.", voice: ELLEN, filename: "aula3_surv_prioritize_deadlines" },
  { text: "I often coordinate with international teams.", voice: ARTHUR, filename: "aula3_surv_coordinate_intl" },
  { text: "My routine involves meetings, reports, and team coordination.", voice: ELLEN, filename: "aula3_surv_routine_meetings" },
  { text: "I rarely leave the office before seven PM.", voice: ARTHUR, filename: "aula3_surv_rarely_leave" },

  // IN CLASS — Vocab card example phrases (alternate)
  { text: "I check my schedule every morning before the first meeting.", voice: ARTHUR, filename: "aula3_ic_schedule_morning" },
  { text: "The deadline for this project is next Friday.", voice: ELLEN, filename: "aula3_ic_deadline_friday" },
  { text: "I always prioritize urgent tasks from my stakeholders.", voice: ARTHUR, filename: "aula3_ic_prioritize_urgent" },
  { text: "I coordinate with teams in Colombia, Chile, and Mexico every day.", voice: ELLEN, filename: "aula3_ic_coordinate_latam" },
  { text: "I attend at least three meetings every morning.", voice: ARTHUR, filename: "aula3_ic_attend_meetings" },
  { text: "I report to the VP of Operations every Friday.", voice: ELLEN, filename: "aula3_ic_report_vp" },
  { text: "My commute from Parada Inglesa takes about forty-five minutes.", voice: ARTHUR, filename: "aula3_ic_commute_parada" },
  { text: "My routine at Oracle is very structured and organized.", voice: ELLEN, filename: "aula3_ic_routine_structured" },

  // IN CLASS — Key phrases (slide 8)
  { text: "I usually start my day at seven in the morning.", voice: ARTHUR, filename: "aula3_ic_phrase_start" },
  { text: "I always check my schedule and emails before the first meeting.", voice: ELLEN, filename: "aula3_ic_phrase_check" },
  { text: "I often coordinate with teams in different countries.", voice: ARTHUR, filename: "aula3_ic_phrase_coordinate" },
  { text: "I rarely miss a deadline because I prioritize my tasks.", voice: ELLEN, filename: "aula3_ic_phrase_rarely" },

  // IN CLASS — Dialogue: Rachel (Ellen) and Diogo (Arthur)
  { text: "Hey Diogo! I just joined the São Paulo team. What does a typical Monday look like for you?", voice: ELLEN, filename: "aula3_ic_dlg_rachel_1" },
  { text: "Well, I usually start my day at seven. My commute from Parada Inglesa takes about forty-five minutes.", voice: ARTHUR, filename: "aula3_ic_dlg_diogo_1" },
  { text: "That is early! What do you do first when you arrive?", voice: ELLEN, filename: "aula3_ic_dlg_rachel_2" },
  { text: "I always check my schedule and emails before the first meeting. Then I coordinate with my teams in Colombia and Chile.", voice: ARTHUR, filename: "aula3_ic_dlg_diogo_2" },
  { text: "How many meetings do you attend per day?", voice: ELLEN, filename: "aula3_ic_dlg_rachel_3" },
  { text: "I usually attend three or four. I sometimes have five when we are close to a deadline.", voice: ARTHUR, filename: "aula3_ic_dlg_diogo_3" },
  { text: "Do you ever work late?", voice: ELLEN, filename: "aula3_ic_dlg_rachel_4" },
  { text: "I rarely leave before seven PM. But I never miss a deadline, so it is worth it.", voice: ARTHUR, filename: "aula3_ic_dlg_diogo_4" },

  // IN CLASS — Listening: Marcus routine (Arthur — male narrator)
  { text: "My name is Marcus Rivera. I work as a Senior Developer at a tech company in Austin, Texas. I usually start my day at eight thirty. I always prioritize checking my code reviews first. I often coordinate with our team in Berlin because of the time difference. I attend a standup meeting at nine every morning. I rarely skip lunch because it helps me stay focused. My commute is only fifteen minutes by bike. The routine keeps me productive. I sometimes work from home on Fridays.", voice: ARTHUR, filename: "aula3_listening_marcus_routine" },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });
  console.log('Generating ' + PHRASES.length + ' audio files for Diogo Leal Aula 3...\n');
  for (const p of PHRASES) {
    const fname = p.filename + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + fname); continue; }
    try {
      const bytes = await gen(p.text, p.voice, outPath);
      console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
      await new Promise(r => setTimeout(r, 500));
    } catch (e) { console.error('FAIL: ' + fname + ' — ' + e.message); }
  }
  console.log('\nDone!');
}
main().catch(e => { console.error(e); process.exit(1); });
