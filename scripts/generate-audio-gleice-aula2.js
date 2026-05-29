const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'gleice-leonardo-rocha-de-souza');

const PHRASES = [
  // Vocab words (Ellen - female student)
  { text: "Department", file: "aula2_department.mp3", voice: ELLEN },
  { text: "Responsibility", file: "aula2_responsibility.mp3", voice: ELLEN },
  { text: "Report (to)", file: "aula2_report_to.mp3", voice: ELLEN },
  { text: "Colleague", file: "aula2_colleague.mp3", voice: ELLEN },
  { text: "Process", file: "aula2_process.mp3", voice: ELLEN },
  { text: "Transformation", file: "aula2_transformation.mp3", voice: ELLEN },
  { text: "Strategy", file: "aula2_strategy.mp3", voice: ELLEN },
  { text: "Performance", file: "aula2_performance.mp3", voice: ELLEN },

  // Vocab examples (alternate)
  { text: "My department is Commercial Excellence.", file: "aula2_ex_department.mp3", voice: ELLEN },
  { text: "Her responsibility is to lead transformation projects.", file: "aula2_ex_responsibility.mp3", voice: ARTHUR },
  { text: "I report to the Commercial Director.", file: "aula2_ex_report.mp3", voice: ELLEN },
  { text: "My colleagues and I improve commercial processes.", file: "aula2_ex_colleague.mp3", voice: ARTHUR },
  { text: "We are changing our sales processes.", file: "aula2_ex_process.mp3", voice: ELLEN },
  { text: "The transformation of our department is going well.", file: "aula2_ex_transformation.mp3", voice: ARTHUR },
  { text: "Our strategy is to expand into new markets.", file: "aula2_ex_strategy.mp3", voice: ELLEN },
  { text: "The team's performance has been strong this year.", file: "aula2_ex_performance.mp3", voice: ARTHUR },

  // Fill-in sentences (alternate)
  { text: "My department has thirty-four colleagues.", file: "aula2_fill1.mp3", voice: ELLEN },
  { text: "Her responsibility is to oversee our strategy.", file: "aula2_fill2.mp3", voice: ARTHUR },
  { text: "I report to the Commercial Director every week.", file: "aula2_fill3.mp3", voice: ELLEN },
  { text: "The transformation of our processes is almost complete.", file: "aula2_fill4.mp3", voice: ARTHUR },
  { text: "Our team's performance is strong this year.", file: "aula2_fill5.mp3", voice: ELLEN },

  // Speech practice (Ellen)
  { text: "My department is Commercial Excellence. We have thirty-four colleagues.", file: "aula2_speech1.mp3", voice: ELLEN },
  { text: "My responsibility is to lead transformation projects.", file: "aula2_speech2.mp3", voice: ELLEN },
  { text: "I report to the Commercial Director.", file: "aula2_speech3.mp3", voice: ELLEN },
  { text: "Our team's performance has been strong this year.", file: "aula2_speech4.mp3", voice: ELLEN },

  // Dialogue (David=Arthur, Gleice=Ellen)
  { text: "I am visiting the Sanofi Medley office. Can you tell me about your department?", file: "aula2_dialogue_david_1.mp3", voice: ARTHUR },
  { text: "Of course! My department is Commercial Excellence. We have thirty-four colleagues.", file: "aula2_dialogue_gleice_1.mp3", voice: ELLEN },
  { text: "That is impressive! What are your main responsibilities?", file: "aula2_dialogue_david_2.mp3", voice: ARTHUR },
  { text: "My responsibility is to lead transformation projects. My colleagues and I improve our processes.", file: "aula2_dialogue_gleice_2.mp3", voice: ELLEN },
  { text: "Who do you report to?", file: "aula2_dialogue_david_3.mp3", voice: ARTHUR },
  { text: "I report to the Commercial Director. His role is to oversee our strategy.", file: "aula2_dialogue_gleice_3.mp3", voice: ELLEN },
  { text: "And how is your team's performance?", file: "aula2_dialogue_david_4.mp3", voice: ARTHUR },
  { text: "Our performance is strong. We are meeting all our goals this year.", file: "aula2_dialogue_gleice_4.mp3", voice: ELLEN },

  // Grammar examples (alternate)
  { text: "My team works in Commercial Excellence.", file: "aula2_grammar1.mp3", voice: ELLEN },
  { text: "Her responsibility is very important.", file: "aula2_grammar2.mp3", voice: ARTHUR },
  { text: "His strategy focuses on new markets.", file: "aula2_grammar3.mp3", voice: ELLEN },
  { text: "Our process improves every quarter.", file: "aula2_grammar4.mp3", voice: ARTHUR },

  // Listening 1 (Ellen - Gleice describing team)
  { text: "Good morning, David. My name is Gleice. I work at Sanofi Medley here in Brazil. My department is Commercial Excellence. We have thirty-four colleagues on our team. My responsibility is to lead transformation projects. My colleagues and I improve our commercial processes every day. I report to the Commercial Director. His role is to oversee our strategy. Our team's performance has been strong this year. We are meeting all our goals.", file: "aula2_listening1.mp3", voice: ELLEN },

  // Listening 2 (Arthur - David describing his team)
  { text: "Hello, Gleice. Thank you for showing me around. Let me tell you about my team. I work at Global Pharma Partners in London. My department is International Business Development. Our team has twelve colleagues. My responsibility is to find new partners in emerging markets. I report to the Managing Director. Her strategy is to expand into Latin America. Our performance has been excellent. We completed five new partnerships this year.", file: "aula2_listening2.mp3", voice: ARTHUR },

  // Order exercise (Ellen)
  { text: "My department is Commercial Excellence. We have thirty-four colleagues. My responsibility is to lead transformation projects. I report to the Commercial Director. Our team's performance is strong this year.", file: "aula2_order_team_description.mp3", voice: ELLEN },

  // Survival IN CLASS (Ellen)
  { text: "My department is Commercial Excellence.", file: "aula2_survival_ic_1.mp3", voice: ELLEN },
  { text: "My responsibility is to lead transformation projects.", file: "aula2_survival_ic_2.mp3", voice: ELLEN },
  { text: "I report to the Commercial Director.", file: "aula2_survival_ic_3.mp3", voice: ELLEN },
  { text: "Our team has thirty-four colleagues.", file: "aula2_survival_ic_4.mp3", voice: ELLEN },
  { text: "Our performance is strong this year.", file: "aula2_survival_ic_5.mp3", voice: ELLEN },
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
  console.log('Generating ' + unique.length + ' audio files for Gleice Aula 2...');
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
  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + unique.length);
}

main().catch(console.error);
