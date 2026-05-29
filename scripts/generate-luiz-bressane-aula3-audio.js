const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

const PHRASES = [
  // === VOCAB WORDS (Arthur) ===
  { text: "Defendant", voice: ARTHUR, filename: "aula3_defendant" },
  { text: "Charge", voice: ARTHUR, filename: "aula3_charge" },
  { text: "Represent", voice: ARTHUR, filename: "aula3_represent" },
  { text: "Legal Aid", voice: ARTHUR, filename: "aula3_legal_aid" },
  { text: "Jury", voice: ARTHUR, filename: "aula3_jury" },
  { text: "Courthouse", voice: ARTHUR, filename: "aula3_courthouse" },
  { text: "Role", voice: ARTHUR, filename: "aula3_role" },
  { text: "Involve", voice: ARTHUR, filename: "aula3_involve" },

  // === VOCAB EXAMPLE PHRASES (alternate) ===
  { text: "I represent defendants in homicide cases.", voice: ELLEN, filename: "aula3_i_represent_defendants_in_homicide_cases" },
  { text: "My clients are charged with serious crimes.", voice: ARTHUR, filename: "aula3_my_clients_are_charged_with_serious_crimes" },
  { text: "I represent people who cannot afford a lawyer.", voice: ELLEN, filename: "aula3_i_represent_people_who_cannot_afford" },
  { text: "Legal aid is a right in Brazil and in the United States.", voice: ARTHUR, filename: "aula3_legal_aid_is_a_right" },
  { text: "The jury listens to all the evidence before making a decision.", voice: ELLEN, filename: "aula3_the_jury_listens_to_all_the_evidence" },
  { text: "I work at the courthouse in Barra Funda every day.", voice: ARTHUR, filename: "aula3_i_work_at_the_courthouse_in_barra_funda" },
  { text: "My role involves preparing cases for trial.", voice: ELLEN, filename: "aula3_my_role_involves_preparing_cases" },
  { text: "My job involves long hours of research and preparation.", voice: ARTHUR, filename: "aula3_my_job_involves_long_hours" },

  // === FILL-IN PHRASES (alternate) ===
  { text: "I represent defendants who cannot afford a private lawyer.", voice: ELLEN, filename: "aula3_fill_i_represent_defendants" },
  { text: "The defendant was charged with murder.", voice: ARTHUR, filename: "aula3_fill_the_defendant_was_charged" },
  { text: "The jury found the defendant not guilty.", voice: ELLEN, filename: "aula3_fill_the_jury_found" },
  { text: "My role involves meeting with clients at the courthouse.", voice: ARTHUR, filename: "aula3_fill_my_role_involves" },
  { text: "Legal aid guarantees that everyone has a lawyer.", voice: ELLEN, filename: "aula3_fill_legal_aid_guarantees" },
  { text: "I deal with criminal cases on a daily basis.", voice: ARTHUR, filename: "aula3_fill_i_deal_with_criminal" },

  // === PRONUNCIATION PHRASES ===
  { text: "I am a public defender. I represent defendants in criminal cases.", voice: ARTHUR, filename: "aula3_pron_i_am_a_public_defender" },
  { text: "My role involves preparing cases for trial at the courthouse.", voice: ELLEN, filename: "aula3_pron_my_role_involves" },
  { text: "I am responsible for defending people who cannot afford a lawyer.", voice: ARTHUR, filename: "aula3_pron_i_am_responsible" },

  // === DIALOGUE LINES (James=Arthur, Luiz=Ellen for alternation) ===
  { text: "Hi, I am James. I am a public defender in New York. What do you do?", voice: ARTHUR, filename: "aula3_dlg_james_1" },
  { text: "I am also a public defender. I work for the Public Defender's Office in Sao Paulo.", voice: ELLEN, filename: "aula3_dlg_luiz_1" },
  { text: "Interesting! What kind of cases do you deal with?", voice: ARTHUR, filename: "aula3_dlg_james_2" },
  { text: "I deal with criminal cases. I represent defendants in homicide trials.", voice: ELLEN, filename: "aula3_dlg_luiz_2" },
  { text: "That sounds intense. How does the jury system work in Brazil?", voice: ARTHUR, filename: "aula3_dlg_james_3" },
  { text: "It is similar to the United States. The jury decides if the defendant is guilty or not guilty.", voice: ELLEN, filename: "aula3_dlg_luiz_3" },
  { text: "Who are your clients? Can they choose their own lawyer?", voice: ARTHUR, filename: "aula3_dlg_james_4" },
  { text: "My clients are people who cannot afford a lawyer. Legal aid is a constitutional right in Brazil.", voice: ELLEN, filename: "aula3_dlg_luiz_4" },
  { text: "What does your daily routine at the courthouse look like?", voice: ARTHUR, filename: "aula3_dlg_james_5" },
  { text: "On a daily basis, I review evidence, meet with defendants, and prepare for trial. My role involves a lot of research.", voice: ELLEN, filename: "aula3_dlg_luiz_5" },

  // === SURVIVAL CARD PHRASES ===
  { text: "I am a public defender. I work for the Public Defender's Office.", voice: ARTHUR, filename: "aula3_surv_1" },
  { text: "I represent defendants in criminal cases.", voice: ELLEN, filename: "aula3_surv_2" },
  { text: "My role involves preparing cases for trial.", voice: ARTHUR, filename: "aula3_surv_3" },
  { text: "I deal with homicide cases on a daily basis.", voice: ELLEN, filename: "aula3_surv_4" },
  { text: "Legal aid is a constitutional right in Brazil.", voice: ARTHUR, filename: "aula3_surv_5" },

  // === GRAMMAR EXAMPLES ===
  { text: "I am a public defender.", voice: ARTHUR, filename: "aula3_gram_i_am_a" },
  { text: "I work as a public defender.", voice: ELLEN, filename: "aula3_gram_i_work_as" },
  { text: "I work for the Public Defender's Office.", voice: ARTHUR, filename: "aula3_gram_i_work_for" },
  { text: "She is a judge.", voice: ELLEN, filename: "aula3_gram_she_is_a" },

  // === EXPRESSIONS ===
  { text: "I am responsible for defending people in criminal cases.", voice: ARTHUR, filename: "aula3_expr_responsible" },
  { text: "I deal with homicide cases on a daily basis.", voice: ELLEN, filename: "aula3_expr_deal_with" },
  { text: "My role involves preparing defendants for trial.", voice: ARTHUR, filename: "aula3_expr_role_involves" },
  { text: "On a daily basis, I work with evidence and witnesses.", voice: ELLEN, filename: "aula3_expr_daily_basis" },

  // === LISTENING 1 (long passage) ===
  { text: "My name is Luiz Bressane and I am a public defender in Sao Paulo, Brazil. I work for the Public Defender's Office at the Criminal Court in Barra Funda. My role involves representing defendants in serious criminal cases, especially homicide trials before a jury. I am responsible for making sure that every person has access to legal aid, regardless of their financial situation. On a daily basis, I review evidence, meet with my clients, and prepare for trial. I deal with very intense cases, but I believe that everyone deserves a fair defense. It is similar to the public defender system in the United States.", voice: ARTHUR, filename: "aula3_listening_1" },

  // === LISTENING 2 (6th Amendment) ===
  { text: "The Sixth Amendment of the United States Constitution guarantees the right to counsel. This means that if a defendant cannot afford a lawyer, the government must provide one. This is the basis of the public defender system in America. Public defenders represent thousands of clients every year. Their role involves handling criminal cases from start to finish.", voice: ELLEN, filename: "aula3_listening_2" },

  // === ORDER EXERCISE ===
  { text: "I am a public defender in Sao Paulo. I work for the Public Defender's Office. I represent defendants in criminal cases. My role involves preparing for trial. I deal with homicide cases on a daily basis.", voice: ARTHUR, filename: "aula3_order_l3" },
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
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });
  console.log('Generating ' + PHRASES.length + ' audio files for Luiz Bressane Aula 3...');
  for (const p of PHRASES) {
    const fname = p.filename + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + fname); }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' -- ' + e.message); }
    }
  }
  console.log('\nDone! Total MP3s: ' + fs.readdirSync(DIR).filter(f => f.endsWith('.mp3')).length);
}
main().catch(e => { console.error(e); process.exit(1); });
