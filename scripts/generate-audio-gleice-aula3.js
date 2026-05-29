const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'gleice-leonardo-rocha-de-souza');

const PHRASES = [
  // Vocab words (Ellen - female student)
  { text: "Schedule", file: "aula3_schedule.mp3", voice: ELLEN },
  { text: "Meeting", file: "aula3_meeting.mp3", voice: ELLEN },
  { text: "Deadline", file: "aula3_deadline.mp3", voice: ELLEN },
  { text: "Review", file: "aula3_review.mp3", voice: ELLEN },
  { text: "Commute", file: "aula3_commute.mp3", voice: ELLEN },
  { text: "Routine", file: "aula3_routine.mp3", voice: ELLEN },
  { text: "Prioritize", file: "aula3_prioritize.mp3", voice: ELLEN },
  { text: "Coordinate", file: "aula3_coordinate.mp3", voice: ELLEN },

  // Vocab examples (alternate)
  { text: "My schedule is very busy this week.", file: "aula3_ex_schedule.mp3", voice: ELLEN },
  { text: "I have three meetings every day.", file: "aula3_ex_meeting.mp3", voice: ARTHUR },
  { text: "The deadline for the report is Friday.", file: "aula3_ex_deadline.mp3", voice: ELLEN },
  { text: "I review our sales numbers every morning.", file: "aula3_ex_review.mp3", voice: ARTHUR },
  { text: "I commute from Santo Andre to the office.", file: "aula3_ex_commute.mp3", voice: ELLEN },
  { text: "My morning routine starts at six.", file: "aula3_ex_routine.mp3", voice: ARTHUR },
  { text: "I always prioritize my team's needs.", file: "aula3_ex_prioritize.mp3", voice: ELLEN },
  { text: "I coordinate projects across departments.", file: "aula3_ex_coordinate.mp3", voice: ARTHUR },

  // Fill-in sentences (alternate)
  { text: "I always review my schedule in the morning.", file: "aula3_fill1.mp3", voice: ELLEN },
  { text: "She usually has three meetings before lunch.", file: "aula3_fill2.mp3", voice: ARTHUR },
  { text: "I never miss a deadline.", file: "aula3_fill3.mp3", voice: ELLEN },
  { text: "He sometimes commutes by train.", file: "aula3_fill4.mp3", voice: ARTHUR },
  { text: "We always coordinate our projects together.", file: "aula3_fill5.mp3", voice: ELLEN },

  // Speech practice (Ellen)
  { text: "I usually start my day at seven in the morning.", file: "aula3_speech1.mp3", voice: ELLEN },
  { text: "I always prioritize my team's needs.", file: "aula3_speech2.mp3", voice: ELLEN },
  { text: "I commute from Santo Andre every day.", file: "aula3_speech3.mp3", voice: ELLEN },
  { text: "I never miss a deadline.", file: "aula3_speech4.mp3", voice: ELLEN },

  // Dialogue (Sarah read by Arthur for audio differentiation, Gleice=Ellen)
  { text: "Good morning, Gleice! What does your typical day look like?", file: "aula3_dialogue_sarah_1.mp3", voice: ARTHUR },
  { text: "I usually start at seven. I review my schedule and prioritize my tasks.", file: "aula3_dialogue_gleice_1.mp3", voice: ELLEN },
  { text: "That is early! How do you commute to work?", file: "aula3_dialogue_sarah_2.mp3", voice: ARTHUR },
  { text: "I commute from Santo Andre. It usually takes about forty minutes.", file: "aula3_dialogue_gleice_2.mp3", voice: ELLEN },
  { text: "Do you have many meetings?", file: "aula3_dialogue_sarah_3.mp3", voice: ARTHUR },
  { text: "Yes! I always have at least three meetings a day. I coordinate projects with different departments.", file: "aula3_dialogue_gleice_3.mp3", voice: ELLEN },
  { text: "How do you manage your deadlines?", file: "aula3_dialogue_sarah_4.mp3", voice: ARTHUR },
  { text: "I never miss a deadline. I always check my calendar and prioritize what is urgent.", file: "aula3_dialogue_gleice_4.mp3", voice: ELLEN },

  // Grammar examples (alternate)
  { text: "I always review the numbers.", file: "aula3_grammar1.mp3", voice: ELLEN },
  { text: "She usually has three meetings.", file: "aula3_grammar2.mp3", voice: ARTHUR },
  { text: "We sometimes work late.", file: "aula3_grammar3.mp3", voice: ELLEN },
  { text: "He never misses a deadline.", file: "aula3_grammar4.mp3", voice: ARTHUR },

  // Listening 1 (Ellen - Gleice's full day)
  { text: "Let me tell you about my typical day. I usually wake up at six in the morning. My routine starts with coffee and checking my emails. I commute from Santo Andre to the Sanofi Medley office. It usually takes about forty minutes. I always arrive before eight. First, I review my schedule and prioritize my tasks for the day. I usually have three or four meetings. I coordinate projects with different departments. I always check my deadlines before lunch. In the afternoon, I sometimes review reports with my team. I never leave the office without checking tomorrow's schedule. I usually finish work around six in the evening.", file: "aula3_listening1.mp3", voice: ELLEN },

  // Listening 2 (Arthur - Sarah's London routine)
  { text: "My name is Sarah and I work in London. My routine is quite different from Gleice's. I usually wake up at seven thirty. I never commute by car. I always take the tube to the office. It usually takes about twenty-five minutes. I sometimes have meetings in the morning, but I usually start with emails. I always prioritize urgent tasks first. My biggest challenge is coordinating with teams in different time zones. I sometimes work late to meet deadlines. I usually review my schedule before I leave. I never forget to check my calendar for the next day.", file: "aula3_listening2.mp3", voice: ARTHUR },

  // Order exercise (Ellen)
  { text: "I usually wake up at six in the morning. I commute from Santo Andre to the office. I always review my schedule first. I have three meetings every day. I never miss a deadline.", file: "aula3_order_daily_routine.mp3", voice: ELLEN },

  // Survival IC (Ellen)
  { text: "I usually start my day at seven in the morning.", file: "aula3_survival_ic_1.mp3", voice: ELLEN },
  { text: "I always prioritize my team's needs.", file: "aula3_survival_ic_2.mp3", voice: ELLEN },
  { text: "I have three meetings every day.", file: "aula3_survival_ic_3.mp3", voice: ELLEN },
  { text: "I never miss a deadline.", file: "aula3_survival_ic_4.mp3", voice: ELLEN },
  { text: "I commute from Santo Andre to the office.", file: "aula3_survival_ic_5.mp3", voice: ELLEN },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
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
  const unique = PHRASES.filter(p => { const k = p.file.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });
  console.log('Generating ' + unique.length + ' audio files for Gleice Aula 3...');
  let generated = 0, skipped = 0;
  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) { console.log('  SKIP: ' + p.file); skipped++; continue; }
    try {
      const size = await gen(p.text, p.voice, outPath);
      generated++;
      console.log('  OK (' + (size / 1024).toFixed(1) + 'KB): ' + p.file + ' [' + (p.voice === ARTHUR ? 'Arthur' : 'Ellen') + ']');
      await new Promise(resolve => setTimeout(resolve, 500));
    } catch (err) { console.error('  FAIL: ' + p.file + ' -> ' + err.message); }
  }
  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped);
}
main().catch(console.error);
